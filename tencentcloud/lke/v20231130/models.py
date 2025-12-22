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
    r"""智能通话

    """

    def __init__(self):
        r"""
        :param _EnableVoiceInteract: 启用语音互动功能
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableVoiceInteract: bool
        :param _EnableVoiceCall: 启用语音通话
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableVoiceCall: bool
        :param _EnableDigitalHuman: 启用数智人
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDigitalHuman: bool
        :param _Voice: 音色配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Voice: :class:`tencentcloud.lke.v20231130.models.VoiceConfig`
        :param _DigitalHuman: 数智人配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DigitalHuman: :class:`tencentcloud.lke.v20231130.models.DigitalHumanConfig`
        """
        self._EnableVoiceInteract = None
        self._EnableVoiceCall = None
        self._EnableDigitalHuman = None
        self._Voice = None
        self._DigitalHuman = None

    @property
    def EnableVoiceInteract(self):
        r"""启用语音互动功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableVoiceInteract

    @EnableVoiceInteract.setter
    def EnableVoiceInteract(self, EnableVoiceInteract):
        self._EnableVoiceInteract = EnableVoiceInteract

    @property
    def EnableVoiceCall(self):
        r"""启用语音通话
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableVoiceCall

    @EnableVoiceCall.setter
    def EnableVoiceCall(self, EnableVoiceCall):
        self._EnableVoiceCall = EnableVoiceCall

    @property
    def EnableDigitalHuman(self):
        r"""启用数智人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableDigitalHuman

    @EnableDigitalHuman.setter
    def EnableDigitalHuman(self, EnableDigitalHuman):
        self._EnableDigitalHuman = EnableDigitalHuman

    @property
    def Voice(self):
        r"""音色配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.VoiceConfig`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def DigitalHuman(self):
        r"""数智人配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.DigitalHumanConfig`
        """
        return self._DigitalHuman

    @DigitalHuman.setter
    def DigitalHuman(self, DigitalHuman):
        self._DigitalHuman = DigitalHuman


    def _deserialize(self, params):
        self._EnableVoiceInteract = params.get("EnableVoiceInteract")
        self._EnableVoiceCall = params.get("EnableVoiceCall")
        self._EnableDigitalHuman = params.get("EnableDigitalHuman")
        if params.get("Voice") is not None:
            self._Voice = VoiceConfig()
            self._Voice._deserialize(params.get("Voice"))
        if params.get("DigitalHuman") is not None:
            self._DigitalHuman = DigitalHumanConfig()
            self._DigitalHuman._deserialize(params.get("DigitalHuman"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Agent(AbstractModel):
    r"""Agent 的定义

    """

    def __init__(self):
        r"""
        :param _AgentId: AgentID
        :type AgentId: str
        :param _WorkflowId: WorkflowID，非空则当前Agent从workflow转换而来
        :type WorkflowId: str
        :param _Name: Agent名称，同一个应用内，Agent名称不能重复
        :type Name: str
        :param _IconUrl: Agent图标url
        :type IconUrl: str
        :param _Instructions: Agent指令；当该Agent被调用时，将作为“系统提示词”使用，描述Agent应执行的操作和响应方式
        :type Instructions: str
        :param _HandoffDescription: 当Agent作为转交目标时的描述，用于让其他Agent的LLM理解其功能和转交时机
        :type HandoffDescription: str
        :param _Handoffs: Agent可转交的子AgentId列表
        :type Handoffs: list of str
        :param _Model: Agent调用LLM时使用的模型配置
        :type Model: :class:`tencentcloud.lke.v20231130.models.AgentModelInfo`
        :param _Tools: Agent可使用的工具列表
        :type Tools: list of AgentToolInfo
        :param _Plugins: Agent可使用的插件列表
        :type Plugins: list of AgentPluginInfo
        :param _IsStartingAgent: 当前Agent是否是启动Agent
        :type IsStartingAgent: bool
        :param _AgentType: Agent类型; 0: 未指定类型; 1: 知识库检索Agent
        :type AgentType: int
        :param _AgentMode: 0 自由转交，1 计划与执行
        :type AgentMode: int
        :param _AdvancedConfig: 高级设置
        :type AdvancedConfig: :class:`tencentcloud.lke.v20231130.models.AgentAdvancedConfig`
        """
        self._AgentId = None
        self._WorkflowId = None
        self._Name = None
        self._IconUrl = None
        self._Instructions = None
        self._HandoffDescription = None
        self._Handoffs = None
        self._Model = None
        self._Tools = None
        self._Plugins = None
        self._IsStartingAgent = None
        self._AgentType = None
        self._AgentMode = None
        self._AdvancedConfig = None

    @property
    def AgentId(self):
        r"""AgentID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def WorkflowId(self):
        r"""WorkflowID，非空则当前Agent从workflow转换而来
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Name(self):
        r"""Agent名称，同一个应用内，Agent名称不能重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IconUrl(self):
        r"""Agent图标url
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Instructions(self):
        r"""Agent指令；当该Agent被调用时，将作为“系统提示词”使用，描述Agent应执行的操作和响应方式
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions

    @property
    def HandoffDescription(self):
        r"""当Agent作为转交目标时的描述，用于让其他Agent的LLM理解其功能和转交时机
        :rtype: str
        """
        return self._HandoffDescription

    @HandoffDescription.setter
    def HandoffDescription(self, HandoffDescription):
        self._HandoffDescription = HandoffDescription

    @property
    def Handoffs(self):
        r"""Agent可转交的子AgentId列表
        :rtype: list of str
        """
        return self._Handoffs

    @Handoffs.setter
    def Handoffs(self, Handoffs):
        self._Handoffs = Handoffs

    @property
    def Model(self):
        r"""Agent调用LLM时使用的模型配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentModelInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Tools(self):
        r"""Agent可使用的工具列表
        :rtype: list of AgentToolInfo
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def Plugins(self):
        r"""Agent可使用的插件列表
        :rtype: list of AgentPluginInfo
        """
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def IsStartingAgent(self):
        r"""当前Agent是否是启动Agent
        :rtype: bool
        """
        return self._IsStartingAgent

    @IsStartingAgent.setter
    def IsStartingAgent(self, IsStartingAgent):
        self._IsStartingAgent = IsStartingAgent

    @property
    def AgentType(self):
        r"""Agent类型; 0: 未指定类型; 1: 知识库检索Agent
        :rtype: int
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def AgentMode(self):
        r"""0 自由转交，1 计划与执行
        :rtype: int
        """
        return self._AgentMode

    @AgentMode.setter
    def AgentMode(self, AgentMode):
        self._AgentMode = AgentMode

    @property
    def AdvancedConfig(self):
        r"""高级设置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._WorkflowId = params.get("WorkflowId")
        self._Name = params.get("Name")
        self._IconUrl = params.get("IconUrl")
        self._Instructions = params.get("Instructions")
        self._HandoffDescription = params.get("HandoffDescription")
        self._Handoffs = params.get("Handoffs")
        if params.get("Model") is not None:
            self._Model = AgentModelInfo()
            self._Model._deserialize(params.get("Model"))
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = AgentToolInfo()
                obj._deserialize(item)
                self._Tools.append(obj)
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = AgentPluginInfo()
                obj._deserialize(item)
                self._Plugins.append(obj)
        self._IsStartingAgent = params.get("IsStartingAgent")
        self._AgentType = params.get("AgentType")
        self._AgentMode = params.get("AgentMode")
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
        


class AgentAdvancedConfig(AbstractModel):
    r"""Agent高级设置

    """

    def __init__(self):
        r"""
        :param _EnableClarification: 是否开启澄清询问
        :type EnableClarification: bool
        :param _ThinkingMode: 思考模式，0为效果优先，1为速度优先
        :type ThinkingMode: int
        :param _MaxReasoningRound: 最大推理轮数
        :type MaxReasoningRound: int
        :param _HistoryLimit: 上下文轮数
        :type HistoryLimit: int
        :param _EnableStructuredOutput: 是否开启结构化输出
        :type EnableStructuredOutput: bool
        :param _StructuredOutputConfig: 结构化输出配置
        :type StructuredOutputConfig: :class:`tencentcloud.lke.v20231130.models.StructuredOutputConfig`
        """
        self._EnableClarification = None
        self._ThinkingMode = None
        self._MaxReasoningRound = None
        self._HistoryLimit = None
        self._EnableStructuredOutput = None
        self._StructuredOutputConfig = None

    @property
    def EnableClarification(self):
        r"""是否开启澄清询问
        :rtype: bool
        """
        return self._EnableClarification

    @EnableClarification.setter
    def EnableClarification(self, EnableClarification):
        self._EnableClarification = EnableClarification

    @property
    def ThinkingMode(self):
        r"""思考模式，0为效果优先，1为速度优先
        :rtype: int
        """
        return self._ThinkingMode

    @ThinkingMode.setter
    def ThinkingMode(self, ThinkingMode):
        self._ThinkingMode = ThinkingMode

    @property
    def MaxReasoningRound(self):
        r"""最大推理轮数
        :rtype: int
        """
        return self._MaxReasoningRound

    @MaxReasoningRound.setter
    def MaxReasoningRound(self, MaxReasoningRound):
        self._MaxReasoningRound = MaxReasoningRound

    @property
    def HistoryLimit(self):
        r"""上下文轮数
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def EnableStructuredOutput(self):
        r"""是否开启结构化输出
        :rtype: bool
        """
        return self._EnableStructuredOutput

    @EnableStructuredOutput.setter
    def EnableStructuredOutput(self, EnableStructuredOutput):
        self._EnableStructuredOutput = EnableStructuredOutput

    @property
    def StructuredOutputConfig(self):
        r"""结构化输出配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.StructuredOutputConfig`
        """
        return self._StructuredOutputConfig

    @StructuredOutputConfig.setter
    def StructuredOutputConfig(self, StructuredOutputConfig):
        self._StructuredOutputConfig = StructuredOutputConfig


    def _deserialize(self, params):
        self._EnableClarification = params.get("EnableClarification")
        self._ThinkingMode = params.get("ThinkingMode")
        self._MaxReasoningRound = params.get("MaxReasoningRound")
        self._HistoryLimit = params.get("HistoryLimit")
        self._EnableStructuredOutput = params.get("EnableStructuredOutput")
        if params.get("StructuredOutputConfig") is not None:
            self._StructuredOutputConfig = StructuredOutputConfig()
            self._StructuredOutputConfig._deserialize(params.get("StructuredOutputConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDebugInfo(AbstractModel):
    r"""Agent调试信息

    """

    def __init__(self):
        r"""
        :param _Input: 工具、大模型的输入信息，json
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param _Output: 工具、大模型的输出信息，json
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _ModelName: 模型名
        :type ModelName: str
        """
        self._Input = None
        self._Output = None
        self._ModelName = None

    @property
    def Input(self):
        r"""工具、大模型的输入信息，json
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""工具、大模型的输出信息，json
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ModelName(self):
        r"""模型名
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentHandoffAdvancedSetting(AbstractModel):
    r"""Agent转交高级设置

    """

    def __init__(self):
        r"""
        :param _ConversationPolicy: 对话流转策略；0-由上一轮回复用户的 Agent 继续发起，1- 回到主Agent
        :type ConversationPolicy: int
        """
        self._ConversationPolicy = None

    @property
    def ConversationPolicy(self):
        r"""对话流转策略；0-由上一轮回复用户的 Agent 继续发起，1- 回到主Agent
        :rtype: int
        """
        return self._ConversationPolicy

    @ConversationPolicy.setter
    def ConversationPolicy(self, ConversationPolicy):
        self._ConversationPolicy = ConversationPolicy


    def _deserialize(self, params):
        self._ConversationPolicy = params.get("ConversationPolicy")
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
        :param _InputType: 输入来源类型：0 用户输入，3 自定义变量（API参数）
        :type InputType: int
        :param _UserInputValue: 用户手写输入
        :type UserInputValue: :class:`tencentcloud.lke.v20231130.models.AgentInputUserInputValue`
        :param _CustomVarId: 自定义变量（API参数）
        :type CustomVarId: str
        :param _EnvVarId: 环境变量参数
        :type EnvVarId: str
        :param _AppVarId: 应用变量参数
        :type AppVarId: str
        :param _SystemVariable: 系统参数
        :type SystemVariable: :class:`tencentcloud.lke.v20231130.models.AgentInputSystemVariable`
        """
        self._InputType = None
        self._UserInputValue = None
        self._CustomVarId = None
        self._EnvVarId = None
        self._AppVarId = None
        self._SystemVariable = None

    @property
    def InputType(self):
        r"""输入来源类型：0 用户输入，3 自定义变量（API参数）
        :rtype: int
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def UserInputValue(self):
        r"""用户手写输入
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentInputUserInputValue`
        """
        return self._UserInputValue

    @UserInputValue.setter
    def UserInputValue(self, UserInputValue):
        self._UserInputValue = UserInputValue

    @property
    def CustomVarId(self):
        r"""自定义变量（API参数）
        :rtype: str
        """
        return self._CustomVarId

    @CustomVarId.setter
    def CustomVarId(self, CustomVarId):
        self._CustomVarId = CustomVarId

    @property
    def EnvVarId(self):
        r"""环境变量参数
        :rtype: str
        """
        return self._EnvVarId

    @EnvVarId.setter
    def EnvVarId(self, EnvVarId):
        self._EnvVarId = EnvVarId

    @property
    def AppVarId(self):
        r"""应用变量参数
        :rtype: str
        """
        return self._AppVarId

    @AppVarId.setter
    def AppVarId(self, AppVarId):
        self._AppVarId = AppVarId

    @property
    def SystemVariable(self):
        r"""系统参数
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentInputSystemVariable`
        """
        return self._SystemVariable

    @SystemVariable.setter
    def SystemVariable(self, SystemVariable):
        self._SystemVariable = SystemVariable


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        if params.get("UserInputValue") is not None:
            self._UserInputValue = AgentInputUserInputValue()
            self._UserInputValue._deserialize(params.get("UserInputValue"))
        self._CustomVarId = params.get("CustomVarId")
        self._EnvVarId = params.get("EnvVarId")
        self._AppVarId = params.get("AppVarId")
        if params.get("SystemVariable") is not None:
            self._SystemVariable = AgentInputSystemVariable()
            self._SystemVariable._deserialize(params.get("SystemVariable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentInputSystemVariable(AbstractModel):
    r"""系统参数

    """

    def __init__(self):
        r"""
        :param _Name: 系统参数名
        :type Name: str
        :param _DialogHistoryLimit: 对话历史轮数的配置；如果Input是系统变量中的“对话历史”时才使用；
        :type DialogHistoryLimit: int
        """
        self._Name = None
        self._DialogHistoryLimit = None

    @property
    def Name(self):
        r"""系统参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DialogHistoryLimit(self):
        r"""对话历史轮数的配置；如果Input是系统变量中的“对话历史”时才使用；
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
        


class AgentInputUserInputValue(AbstractModel):
    r"""用户手写输入

    """

    def __init__(self):
        r"""
        :param _Values: 用户输入的值
        :type Values: list of str
        """
        self._Values = None

    @property
    def Values(self):
        r"""用户输入的值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledge(AbstractModel):
    r"""Agent 知识库检索插件支持多知识库搜索

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 知识库id
        :type KnowledgeBizId: str
        :param _KnowledgeType: 0-应用内知识库
1-共享知识库
        :type KnowledgeType: int
        :param _Filter: 0-全部知识
1-按文档和问答
2-按标签
        :type Filter: int
        :param _DocBizIds: 文档id
        :type DocBizIds: list of str
        :param _AllQa: true:包含所有问答
false:不包含问答
        :type AllQa: bool
        :param _Tag: 文档标签过滤器
        :type Tag: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterTag`
        """
        self._KnowledgeBizId = None
        self._KnowledgeType = None
        self._Filter = None
        self._DocBizIds = None
        self._AllQa = None
        self._Tag = None

    @property
    def KnowledgeBizId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def KnowledgeType(self):
        r"""0-应用内知识库
1-共享知识库
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType

    @property
    def Filter(self):
        r"""0-全部知识
1-按文档和问答
2-按标签
        :rtype: int
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def DocBizIds(self):
        r"""文档id
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def AllQa(self):
        r"""true:包含所有问答
false:不包含问答
        :rtype: bool
        """
        return self._AllQa

    @AllQa.setter
    def AllQa(self, AllQa):
        self._AllQa = AllQa

    @property
    def Tag(self):
        r"""文档标签过滤器
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterTag`
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._KnowledgeType = params.get("KnowledgeType")
        self._Filter = params.get("Filter")
        self._DocBizIds = params.get("DocBizIds")
        self._AllQa = params.get("AllQa")
        if params.get("Tag") is not None:
            self._Tag = AgentKnowledgeFilterTag()
            self._Tag._deserialize(params.get("Tag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledgeAttrLabel(AbstractModel):
    r"""标签过滤器

    """

    def __init__(self):
        r"""
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _Inputs: 标签值，标签值之间是或的关系，只有匹配的，才会进行知识检索，否则报检索不到
        :type Inputs: list of AgentInput
        """
        self._AttributeBizId = None
        self._Inputs = None

    @property
    def AttributeBizId(self):
        r"""属性ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def Inputs(self):
        r"""标签值，标签值之间是或的关系，只有匹配的，才会进行知识检索，否则报检索不到
        :rtype: list of AgentInput
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs


    def _deserialize(self, params):
        self._AttributeBizId = params.get("AttributeBizId")
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = AgentInput()
                obj._deserialize(item)
                self._Inputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledgeFilter(AbstractModel):
    r"""知识检索筛选范围

    """

    def __init__(self):
        r"""
        :param _FilterType: 知识检索筛选方式; 0: 全部知识; 1:按文档和问答; 2: 按标签
        :type FilterType: int
        :param _DocAndAnswer: 文档和问答过滤器
        :type DocAndAnswer: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterDocAndAnswer`
        :param _Tag: 标签过滤器
        :type Tag: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterTag`
        :param _KnowledgeList: 知识库列表
        :type KnowledgeList: list of AgentKnowledge
        :param _AllKnowledge: 是否检索全部知识
        :type AllKnowledge: bool
        """
        self._FilterType = None
        self._DocAndAnswer = None
        self._Tag = None
        self._KnowledgeList = None
        self._AllKnowledge = None

    @property
    def FilterType(self):
        r"""知识检索筛选方式; 0: 全部知识; 1:按文档和问答; 2: 按标签
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def DocAndAnswer(self):
        r"""文档和问答过滤器
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterDocAndAnswer`
        """
        return self._DocAndAnswer

    @DocAndAnswer.setter
    def DocAndAnswer(self, DocAndAnswer):
        self._DocAndAnswer = DocAndAnswer

    @property
    def Tag(self):
        r"""标签过滤器
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilterTag`
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def KnowledgeList(self):
        r"""知识库列表
        :rtype: list of AgentKnowledge
        """
        return self._KnowledgeList

    @KnowledgeList.setter
    def KnowledgeList(self, KnowledgeList):
        self._KnowledgeList = KnowledgeList

    @property
    def AllKnowledge(self):
        r"""是否检索全部知识
        :rtype: bool
        """
        return self._AllKnowledge

    @AllKnowledge.setter
    def AllKnowledge(self, AllKnowledge):
        self._AllKnowledge = AllKnowledge


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        if params.get("DocAndAnswer") is not None:
            self._DocAndAnswer = AgentKnowledgeFilterDocAndAnswer()
            self._DocAndAnswer._deserialize(params.get("DocAndAnswer"))
        if params.get("Tag") is not None:
            self._Tag = AgentKnowledgeFilterTag()
            self._Tag._deserialize(params.get("Tag"))
        if params.get("KnowledgeList") is not None:
            self._KnowledgeList = []
            for item in params.get("KnowledgeList"):
                obj = AgentKnowledge()
                obj._deserialize(item)
                self._KnowledgeList.append(obj)
        self._AllKnowledge = params.get("AllKnowledge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledgeFilterDocAndAnswer(AbstractModel):
    r"""文档和问答过滤器

    """

    def __init__(self):
        r"""
        :param _DocBizIds: 文档ID列表
        :type DocBizIds: list of str
        :param _AllQa: 问答
        :type AllQa: bool
        """
        self._DocBizIds = None
        self._AllQa = None

    @property
    def DocBizIds(self):
        r"""文档ID列表
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def AllQa(self):
        r"""问答
        :rtype: bool
        """
        return self._AllQa

    @AllQa.setter
    def AllQa(self, AllQa):
        self._AllQa = AllQa


    def _deserialize(self, params):
        self._DocBizIds = params.get("DocBizIds")
        self._AllQa = params.get("AllQa")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledgeFilterTag(AbstractModel):
    r"""标签过滤器

    """

    def __init__(self):
        r"""
        :param _Operator: 标签之间的关系;0:AND, 1:OR
        :type Operator: int
        :param _Labels: 标签
        :type Labels: list of AgentKnowledgeAttrLabel
        """
        self._Operator = None
        self._Labels = None

    @property
    def Operator(self):
        r"""标签之间的关系;0:AND, 1:OR
        :rtype: int
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Labels(self):
        r"""标签
        :rtype: list of AgentKnowledgeAttrLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AgentKnowledgeAttrLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentKnowledgeQAPlugin(AbstractModel):
    r"""知识库问答插件

    """

    def __init__(self):
        r"""
        :param _Filter: 知识检索筛选范围
        :type Filter: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""知识检索筛选范围
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = AgentKnowledgeFilter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentMCPServerInfo(AbstractModel):
    r"""mcp的服务信息

    """

    def __init__(self):
        r"""
        :param _McpServerUrl: mcp server URL地址
        :type McpServerUrl: str
        :param _Headers: mcp server header信息
        :type Headers: list of AgentPluginHeader
        :param _Timeout: 超时时间，单位秒
        :type Timeout: int
        :param _SseReadTimeout: sse服务超时时间，单位秒
        :type SseReadTimeout: int
        :param _Query: mcp server query信息
        :type Query: list of AgentPluginQuery
        """
        self._McpServerUrl = None
        self._Headers = None
        self._Timeout = None
        self._SseReadTimeout = None
        self._Query = None

    @property
    def McpServerUrl(self):
        r"""mcp server URL地址
        :rtype: str
        """
        return self._McpServerUrl

    @McpServerUrl.setter
    def McpServerUrl(self, McpServerUrl):
        self._McpServerUrl = McpServerUrl

    @property
    def Headers(self):
        r"""mcp server header信息
        :rtype: list of AgentPluginHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Timeout(self):
        r"""超时时间，单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def SseReadTimeout(self):
        r"""sse服务超时时间，单位秒
        :rtype: int
        """
        return self._SseReadTimeout

    @SseReadTimeout.setter
    def SseReadTimeout(self, SseReadTimeout):
        self._SseReadTimeout = SseReadTimeout

    @property
    def Query(self):
        r"""mcp server query信息
        :rtype: list of AgentPluginQuery
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._McpServerUrl = params.get("McpServerUrl")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = AgentPluginHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._Timeout = params.get("Timeout")
        self._SseReadTimeout = params.get("SseReadTimeout")
        if params.get("Query") is not None:
            self._Query = []
            for item in params.get("Query"):
                obj = AgentPluginQuery()
                obj._deserialize(item)
                self._Query.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentModelInfo(AbstractModel):
    r"""Agent 配置里面的模型定义

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelAliasName: 模型别名
        :type ModelAliasName: str
        :param _Temperature: 模型温度
        :type Temperature: float
        :param _TopP: 模型TopP
        :type TopP: float
        :param _IsEnabled: 模型是否可用
        :type IsEnabled: bool
        :param _HistoryLimit: 对话历史条数限制
        :type HistoryLimit: int
        :param _ModelContextWordsLimit: 模型上下文长度字符限制
        :type ModelContextWordsLimit: str
        :param _InstructionsWordsLimit: 指令长度字符限制
        :type InstructionsWordsLimit: int
        :param _MaxReasoningRound: 单次会话最大推理轮数
        :type MaxReasoningRound: int
        :param _ModelParams: 模型参数
        :type ModelParams: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        """
        self._ModelName = None
        self._ModelAliasName = None
        self._Temperature = None
        self._TopP = None
        self._IsEnabled = None
        self._HistoryLimit = None
        self._ModelContextWordsLimit = None
        self._InstructionsWordsLimit = None
        self._MaxReasoningRound = None
        self._ModelParams = None

    @property
    def ModelName(self):
        r"""模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelAliasName(self):
        r"""模型别名
        :rtype: str
        """
        return self._ModelAliasName

    @ModelAliasName.setter
    def ModelAliasName(self, ModelAliasName):
        self._ModelAliasName = ModelAliasName

    @property
    def Temperature(self):
        r"""模型温度
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        r"""模型TopP
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def IsEnabled(self):
        r"""模型是否可用
        :rtype: bool
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def HistoryLimit(self):
        r"""对话历史条数限制
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def ModelContextWordsLimit(self):
        r"""模型上下文长度字符限制
        :rtype: str
        """
        return self._ModelContextWordsLimit

    @ModelContextWordsLimit.setter
    def ModelContextWordsLimit(self, ModelContextWordsLimit):
        self._ModelContextWordsLimit = ModelContextWordsLimit

    @property
    def InstructionsWordsLimit(self):
        r"""指令长度字符限制
        :rtype: int
        """
        return self._InstructionsWordsLimit

    @InstructionsWordsLimit.setter
    def InstructionsWordsLimit(self, InstructionsWordsLimit):
        self._InstructionsWordsLimit = InstructionsWordsLimit

    @property
    def MaxReasoningRound(self):
        r"""单次会话最大推理轮数
        :rtype: int
        """
        return self._MaxReasoningRound

    @MaxReasoningRound.setter
    def MaxReasoningRound(self, MaxReasoningRound):
        self._MaxReasoningRound = MaxReasoningRound

    @property
    def ModelParams(self):
        r"""模型参数
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._ModelAliasName = params.get("ModelAliasName")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._IsEnabled = params.get("IsEnabled")
        self._HistoryLimit = params.get("HistoryLimit")
        self._ModelContextWordsLimit = params.get("ModelContextWordsLimit")
        self._InstructionsWordsLimit = params.get("InstructionsWordsLimit")
        self._MaxReasoningRound = params.get("MaxReasoningRound")
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
        


class AgentPluginHeader(AbstractModel):
    r"""应用配置MCP插件header信息

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _ParamValue: 参数值
        :type ParamValue: str
        :param _GlobalHidden: header参数配置是否隐藏不可见
        :type GlobalHidden: bool
        :param _Input: 输入的值
        :type Input: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        :param _IsRequired: 参数是否可以为空
        :type IsRequired: bool
        """
        self._ParamName = None
        self._ParamValue = None
        self._GlobalHidden = None
        self._Input = None
        self._IsRequired = None

    @property
    def ParamName(self):
        r"""参数名称
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamValue(self):
        r"""参数值
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue

    @property
    def GlobalHidden(self):
        r"""header参数配置是否隐藏不可见
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def Input(self):
        r"""输入的值
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def IsRequired(self):
        r"""参数是否可以为空
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamValue = params.get("ParamValue")
        self._GlobalHidden = params.get("GlobalHidden")
        if params.get("Input") is not None:
            self._Input = AgentInput()
            self._Input._deserialize(params.get("Input"))
        self._IsRequired = params.get("IsRequired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPluginInfo(AbstractModel):
    r"""Agent 的插件信息

    """

    def __init__(self):
        r"""
        :param _PluginId: 插件id
        :type PluginId: str
        :param _Headers: 应用配置的插件header信息
        :type Headers: list of AgentPluginHeader
        :param _Model: 插件调用LLM时使用的模型配置，一般用于指定知识库问答插件的生成模型
        :type Model: :class:`tencentcloud.lke.v20231130.models.AgentModelInfo`
        :param _PluginInfoType: 插件信息类型; 0: 未指定类型; 1: 知识库问答插件
        :type PluginInfoType: int
        :param _KnowledgeQa: 知识库问答插件配置
        :type KnowledgeQa: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeQAPlugin`
        :param _EnableRoleAuth: 是否使用一键授权
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRoleAuth: bool
        :param _Query: 应用配置的插件query信息
        :type Query: list of AgentPluginQuery
        :param _McpType: MCP类型
        :type McpType: int
        """
        self._PluginId = None
        self._Headers = None
        self._Model = None
        self._PluginInfoType = None
        self._KnowledgeQa = None
        self._EnableRoleAuth = None
        self._Query = None
        self._McpType = None

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
    def Headers(self):
        r"""应用配置的插件header信息
        :rtype: list of AgentPluginHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Model(self):
        r"""插件调用LLM时使用的模型配置，一般用于指定知识库问答插件的生成模型
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentModelInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def PluginInfoType(self):
        r"""插件信息类型; 0: 未指定类型; 1: 知识库问答插件
        :rtype: int
        """
        return self._PluginInfoType

    @PluginInfoType.setter
    def PluginInfoType(self, PluginInfoType):
        self._PluginInfoType = PluginInfoType

    @property
    def KnowledgeQa(self):
        r"""知识库问答插件配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentKnowledgeQAPlugin`
        """
        return self._KnowledgeQa

    @KnowledgeQa.setter
    def KnowledgeQa(self, KnowledgeQa):
        self._KnowledgeQa = KnowledgeQa

    @property
    def EnableRoleAuth(self):
        r"""是否使用一键授权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableRoleAuth

    @EnableRoleAuth.setter
    def EnableRoleAuth(self, EnableRoleAuth):
        self._EnableRoleAuth = EnableRoleAuth

    @property
    def Query(self):
        r"""应用配置的插件query信息
        :rtype: list of AgentPluginQuery
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def McpType(self):
        r"""MCP类型
        :rtype: int
        """
        return self._McpType

    @McpType.setter
    def McpType(self, McpType):
        self._McpType = McpType


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = AgentPluginHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        if params.get("Model") is not None:
            self._Model = AgentModelInfo()
            self._Model._deserialize(params.get("Model"))
        self._PluginInfoType = params.get("PluginInfoType")
        if params.get("KnowledgeQa") is not None:
            self._KnowledgeQa = AgentKnowledgeQAPlugin()
            self._KnowledgeQa._deserialize(params.get("KnowledgeQa"))
        self._EnableRoleAuth = params.get("EnableRoleAuth")
        if params.get("Query") is not None:
            self._Query = []
            for item in params.get("Query"):
                obj = AgentPluginQuery()
                obj._deserialize(item)
                self._Query.append(obj)
        self._McpType = params.get("McpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPluginQuery(AbstractModel):
    r"""应用配置MCP插件query信息

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _ParamValue: 参数值
        :type ParamValue: str
        :param _GlobalHidden: query参数配置是否隐藏不可见，true-隐藏不可见，false-可见
        :type GlobalHidden: bool
        :param _IsRequired: 参数是否可以为空
        :type IsRequired: bool
        :param _Input: 输入的值
        :type Input: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        """
        self._ParamName = None
        self._ParamValue = None
        self._GlobalHidden = None
        self._IsRequired = None
        self._Input = None

    @property
    def ParamName(self):
        r"""参数名称
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamValue(self):
        r"""参数值
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue

    @property
    def GlobalHidden(self):
        r"""query参数配置是否隐藏不可见，true-隐藏不可见，false-可见
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def IsRequired(self):
        r"""参数是否可以为空
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Input(self):
        r"""输入的值
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamValue = params.get("ParamValue")
        self._GlobalHidden = params.get("GlobalHidden")
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
        


class AgentProcedure(AbstractModel):
    r"""思考事件过程信息

    """

    def __init__(self):
        r"""
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Name: 执行过程英语名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Title: 中文名, 用于展示
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Status: 状态常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Icon: 图标
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param _Debugging: Agent调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Debugging: :class:`tencentcloud.lke.v20231130.models.AgentProcedureDebugging`
        :param _Switch: 是否切换Agent，取值为"main"或者"workflow",不切换为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _Elapsed: 当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Elapsed: int
        :param _NodeName: 工作流节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _ReplyIndex: 用于展示思考放在哪个回复气泡中
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyIndex: int
        :param _SourceAgentName: 主agent
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAgentName: str
        :param _TargetAgentName: 挂号agent
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAgentName: str
        :param _AgentIcon: Agent的图标
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentIcon: str
        """
        self._Index = None
        self._Name = None
        self._Title = None
        self._Status = None
        self._Icon = None
        self._Debugging = None
        self._Switch = None
        self._WorkflowName = None
        self._Elapsed = None
        self._NodeName = None
        self._ReplyIndex = None
        self._SourceAgentName = None
        self._TargetAgentName = None
        self._AgentIcon = None

    @property
    def Index(self):
        r"""索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        r"""执行过程英语名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""中文名, 用于展示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        r"""状态常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Icon(self):
        r"""图标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Debugging(self):
        r"""Agent调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentProcedureDebugging`
        """
        return self._Debugging

    @Debugging.setter
    def Debugging(self, Debugging):
        self._Debugging = Debugging

    @property
    def Switch(self):
        r"""是否切换Agent，取值为"main"或者"workflow",不切换为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Elapsed(self):
        r"""当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def NodeName(self):
        r"""工作流节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ReplyIndex(self):
        r"""用于展示思考放在哪个回复气泡中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReplyIndex

    @ReplyIndex.setter
    def ReplyIndex(self, ReplyIndex):
        self._ReplyIndex = ReplyIndex

    @property
    def SourceAgentName(self):
        r"""主agent
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceAgentName

    @SourceAgentName.setter
    def SourceAgentName(self, SourceAgentName):
        self._SourceAgentName = SourceAgentName

    @property
    def TargetAgentName(self):
        r"""挂号agent
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetAgentName

    @TargetAgentName.setter
    def TargetAgentName(self, TargetAgentName):
        self._TargetAgentName = TargetAgentName

    @property
    def AgentIcon(self):
        r"""Agent的图标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentIcon

    @AgentIcon.setter
    def AgentIcon(self, AgentIcon):
        self._AgentIcon = AgentIcon


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._Icon = params.get("Icon")
        if params.get("Debugging") is not None:
            self._Debugging = AgentProcedureDebugging()
            self._Debugging._deserialize(params.get("Debugging"))
        self._Switch = params.get("Switch")
        self._WorkflowName = params.get("WorkflowName")
        self._Elapsed = params.get("Elapsed")
        self._NodeName = params.get("NodeName")
        self._ReplyIndex = params.get("ReplyIndex")
        self._SourceAgentName = params.get("SourceAgentName")
        self._TargetAgentName = params.get("TargetAgentName")
        self._AgentIcon = params.get("AgentIcon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentProcedureDebugging(AbstractModel):
    r"""Agent思考过程调试信息

    """

    def __init__(self):
        r"""
        :param _Content: 模型思考内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _DisplayContent: 展示的具体文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayContent: str
        :param _DisplayType: 1：搜索引擎参考来源；2：知识库参考来源
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayType: int
        :param _QuoteInfos: 搜索引擎展示的索引
注意：此字段可能返回 null，表示取不到有效值。
        :type QuoteInfos: list of QuoteInfo
        :param _References: 具体的参考来源
注意：此字段可能返回 null，表示取不到有效值。
        :type References: list of AgentReference
        :param _DisplayStatus: 展示正在执行的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayStatus: str
        :param _SandboxUrl: 云桌面的URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SandboxUrl: str
        :param _DisplayUrl: 云桌面里面通过浏览器打开的URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayUrl: str
        """
        self._Content = None
        self._DisplayContent = None
        self._DisplayType = None
        self._QuoteInfos = None
        self._References = None
        self._DisplayStatus = None
        self._SandboxUrl = None
        self._DisplayUrl = None

    @property
    def Content(self):
        r"""模型思考内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DisplayContent(self):
        r"""展示的具体文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayContent

    @DisplayContent.setter
    def DisplayContent(self, DisplayContent):
        self._DisplayContent = DisplayContent

    @property
    def DisplayType(self):
        r"""1：搜索引擎参考来源；2：知识库参考来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DisplayType

    @DisplayType.setter
    def DisplayType(self, DisplayType):
        self._DisplayType = DisplayType

    @property
    def QuoteInfos(self):
        r"""搜索引擎展示的索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QuoteInfo
        """
        return self._QuoteInfos

    @QuoteInfos.setter
    def QuoteInfos(self, QuoteInfos):
        self._QuoteInfos = QuoteInfos

    @property
    def References(self):
        r"""具体的参考来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def DisplayStatus(self):
        r"""展示正在执行的状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayStatus

    @DisplayStatus.setter
    def DisplayStatus(self, DisplayStatus):
        self._DisplayStatus = DisplayStatus

    @property
    def SandboxUrl(self):
        r"""云桌面的URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SandboxUrl

    @SandboxUrl.setter
    def SandboxUrl(self, SandboxUrl):
        self._SandboxUrl = SandboxUrl

    @property
    def DisplayUrl(self):
        r"""云桌面里面通过浏览器打开的URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayUrl

    @DisplayUrl.setter
    def DisplayUrl(self, DisplayUrl):
        self._DisplayUrl = DisplayUrl


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._DisplayContent = params.get("DisplayContent")
        self._DisplayType = params.get("DisplayType")
        if params.get("QuoteInfos") is not None:
            self._QuoteInfos = []
            for item in params.get("QuoteInfos"):
                obj = QuoteInfo()
                obj._deserialize(item)
                self._QuoteInfos.append(obj)
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = AgentReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._DisplayStatus = params.get("DisplayStatus")
        self._SandboxUrl = params.get("SandboxUrl")
        self._DisplayUrl = params.get("DisplayUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentReference(AbstractModel):
    r"""Agent中的参考来源

    """

    def __init__(self):
        r"""
        :param _DocId: 来源文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        :param _Id: id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Url: 链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _DocBizId: 文档业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocBizId: str
        :param _DocName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DocName: str
        :param _QaBizId: 问答业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type QaBizId: str
        :param _Index: 搜索引擎索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Title: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _KnowledgeName: 知识库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeName: str
        :param _KnowledgeBizId: 知识库标识
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeBizId: str
        """
        self._DocId = None
        self._Id = None
        self._Name = None
        self._Type = None
        self._Url = None
        self._DocBizId = None
        self._DocName = None
        self._QaBizId = None
        self._Index = None
        self._Title = None
        self._KnowledgeName = None
        self._KnowledgeBizId = None

    @property
    def DocId(self):
        r"""来源文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def Id(self):
        r"""id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DocBizId(self):
        r"""文档业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def DocName(self):
        r"""文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def QaBizId(self):
        r"""问答业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Index(self):
        r"""搜索引擎索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Title(self):
        r"""标题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def KnowledgeName(self):
        r"""知识库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName

    @property
    def KnowledgeBizId(self):
        r"""知识库标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId


    def _deserialize(self, params):
        self._DocId = params.get("DocId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._DocBizId = params.get("DocBizId")
        self._DocName = params.get("DocName")
        self._QaBizId = params.get("QaBizId")
        self._Index = params.get("Index")
        self._Title = params.get("Title")
        self._KnowledgeName = params.get("KnowledgeName")
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentThought(AbstractModel):
    r"""Agent的思考过程

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _RequestId: 请求 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _RecordId: 对应哪条会话, 会话 ID, 用于回答的消息存储使用, 可提前生成, 保存消息时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _Elapsed: 当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Elapsed: int
        :param _IsWorkflow: 当前是否为工作流
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWorkflow: bool
        :param _WorkflowName: 如果当前是工作流，工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _Procedures: 具体思考过程详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of AgentProcedure
        :param _TraceId: TraceId
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param _Files: 文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Files: list of FileInfo
        """
        self._SessionId = None
        self._RequestId = None
        self._RecordId = None
        self._Elapsed = None
        self._IsWorkflow = None
        self._WorkflowName = None
        self._Procedures = None
        self._TraceId = None
        self._Files = None

    @property
    def SessionId(self):
        r"""会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        r"""请求 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RecordId(self):
        r"""对应哪条会话, 会话 ID, 用于回答的消息存储使用, 可提前生成, 保存消息时使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Elapsed(self):
        r"""当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def IsWorkflow(self):
        r"""当前是否为工作流
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsWorkflow

    @IsWorkflow.setter
    def IsWorkflow(self, IsWorkflow):
        self._IsWorkflow = IsWorkflow

    @property
    def WorkflowName(self):
        r"""如果当前是工作流，工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Procedures(self):
        r"""具体思考过程详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentProcedure
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TraceId(self):
        r"""TraceId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def Files(self):
        r"""文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FileInfo
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")
        self._RecordId = params.get("RecordId")
        self._Elapsed = params.get("Elapsed")
        self._IsWorkflow = params.get("IsWorkflow")
        self._WorkflowName = params.get("WorkflowName")
        if params.get("Procedures") is not None:
            self._Procedures = []
            for item in params.get("Procedures"):
                obj = AgentProcedure()
                obj._deserialize(item)
                self._Procedures.append(obj)
        self._TraceId = params.get("TraceId")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolInfo(AbstractModel):
    r"""Agent的工具信息

    """

    def __init__(self):
        r"""
        :param _PluginId: 插件id
        :type PluginId: str
        :param _PluginName: 插件名称
        :type PluginName: str
        :param _IconUrl: 插件图标url
        :type IconUrl: str
        :param _PluginType: 0 自定义插件
1 官方插件
2 第三方插件 目前用于第三方实现的mcp server
        :type PluginType: int
        :param _ToolId: 工具id
        :type ToolId: str
        :param _ToolName: 工具名称
        :type ToolName: str
        :param _ToolDesc: 工具描述
        :type ToolDesc: str
        :param _Inputs: 输入参数
        :type Inputs: list of AgentToolReqParam
        :param _Outputs: 输出参数
        :type Outputs: list of AgentToolRspParam
        :param _CreateType: 创建方式，0:服务创建，1:代码创建，2:MCP创建	
        :type CreateType: int
        :param _McpServer: MCP插件的配置信息
        :type McpServer: :class:`tencentcloud.lke.v20231130.models.AgentMCPServerInfo`
        :param _IsBindingKnowledge: 该工具是否和知识库绑定
        :type IsBindingKnowledge: bool
        :param _Status: 插件状态，1:可用，2:不可用	
        :type Status: int
        :param _Headers: header信息
        :type Headers: list of AgentPluginHeader
        :param _CallingMethod: NON_STREAMING: 非流式  STREAMIN: 流式
注意：此字段可能返回 null，表示取不到有效值。
        :type CallingMethod: str
        :param _Query: query信息
        :type Query: list of AgentPluginQuery
        :param _FinanceStatus: 工具计费状态 0-不计费 1-可用 2-不可用（欠费、无资源等）
        :type FinanceStatus: int
        :param _ToolSource: 工具来源: 0-来自插件，1-来自工作流
        :type ToolSource: int
        :param _FinanceType: 计费状态；0-不计费，1-限时免费，2-官方收费
        :type FinanceType: int
        """
        self._PluginId = None
        self._PluginName = None
        self._IconUrl = None
        self._PluginType = None
        self._ToolId = None
        self._ToolName = None
        self._ToolDesc = None
        self._Inputs = None
        self._Outputs = None
        self._CreateType = None
        self._McpServer = None
        self._IsBindingKnowledge = None
        self._Status = None
        self._Headers = None
        self._CallingMethod = None
        self._Query = None
        self._FinanceStatus = None
        self._ToolSource = None
        self._FinanceType = None

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
    def PluginName(self):
        r"""插件名称
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

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
    def PluginType(self):
        r"""0 自定义插件
1 官方插件
2 第三方插件 目前用于第三方实现的mcp server
        :rtype: int
        """
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def ToolId(self):
        r"""工具id
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""工具名称
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolDesc(self):
        r"""工具描述
        :rtype: str
        """
        return self._ToolDesc

    @ToolDesc.setter
    def ToolDesc(self, ToolDesc):
        self._ToolDesc = ToolDesc

    @property
    def Inputs(self):
        r"""输入参数
        :rtype: list of AgentToolReqParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Outputs(self):
        r"""输出参数
        :rtype: list of AgentToolRspParam
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def CreateType(self):
        r"""创建方式，0:服务创建，1:代码创建，2:MCP创建	
        :rtype: int
        """
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def McpServer(self):
        r"""MCP插件的配置信息
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentMCPServerInfo`
        """
        return self._McpServer

    @McpServer.setter
    def McpServer(self, McpServer):
        self._McpServer = McpServer

    @property
    def IsBindingKnowledge(self):
        r"""该工具是否和知识库绑定
        :rtype: bool
        """
        return self._IsBindingKnowledge

    @IsBindingKnowledge.setter
    def IsBindingKnowledge(self, IsBindingKnowledge):
        self._IsBindingKnowledge = IsBindingKnowledge

    @property
    def Status(self):
        r"""插件状态，1:可用，2:不可用	
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Headers(self):
        r"""header信息
        :rtype: list of AgentPluginHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def CallingMethod(self):
        r"""NON_STREAMING: 非流式  STREAMIN: 流式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallingMethod

    @CallingMethod.setter
    def CallingMethod(self, CallingMethod):
        self._CallingMethod = CallingMethod

    @property
    def Query(self):
        r"""query信息
        :rtype: list of AgentPluginQuery
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FinanceStatus(self):
        r"""工具计费状态 0-不计费 1-可用 2-不可用（欠费、无资源等）
        :rtype: int
        """
        return self._FinanceStatus

    @FinanceStatus.setter
    def FinanceStatus(self, FinanceStatus):
        self._FinanceStatus = FinanceStatus

    @property
    def ToolSource(self):
        r"""工具来源: 0-来自插件，1-来自工作流
        :rtype: int
        """
        return self._ToolSource

    @ToolSource.setter
    def ToolSource(self, ToolSource):
        self._ToolSource = ToolSource

    @property
    def FinanceType(self):
        r"""计费状态；0-不计费，1-限时免费，2-官方收费
        :rtype: int
        """
        return self._FinanceType

    @FinanceType.setter
    def FinanceType(self, FinanceType):
        self._FinanceType = FinanceType


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._IconUrl = params.get("IconUrl")
        self._PluginType = params.get("PluginType")
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ToolDesc = params.get("ToolDesc")
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = AgentToolReqParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = AgentToolRspParam()
                obj._deserialize(item)
                self._Outputs.append(obj)
        self._CreateType = params.get("CreateType")
        if params.get("McpServer") is not None:
            self._McpServer = AgentMCPServerInfo()
            self._McpServer._deserialize(params.get("McpServer"))
        self._IsBindingKnowledge = params.get("IsBindingKnowledge")
        self._Status = params.get("Status")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = AgentPluginHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._CallingMethod = params.get("CallingMethod")
        if params.get("Query") is not None:
            self._Query = []
            for item in params.get("Query"):
                obj = AgentPluginQuery()
                obj._deserialize(item)
                self._Query.append(obj)
        self._FinanceStatus = params.get("FinanceStatus")
        self._ToolSource = params.get("ToolSource")
        self._FinanceType = params.get("FinanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolReqParam(AbstractModel):
    r"""Agent工具的请求参数定义

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _Desc: 参数描述
        :type Desc: str
        :param _Type: 参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object
        :type Type: int
        :param _IsRequired: 参数是否必填
        :type IsRequired: bool
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _SubParams: 子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :type SubParams: list of AgentToolReqParam
        :param _GlobalHidden: 是否隐藏不可见
        :type GlobalHidden: bool
        :param _AgentHidden: agent模式下模型是否可见
        :type AgentHidden: bool
        :param _AnyOf: 其中任意
        :type AnyOf: list of AgentToolReqParam
        :param _OneOf: 其中一个
        :type OneOf: list of AgentToolReqParam
        :param _Input: 输入
        :type Input: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        """
        self._Name = None
        self._Desc = None
        self._Type = None
        self._IsRequired = None
        self._DefaultValue = None
        self._SubParams = None
        self._GlobalHidden = None
        self._AgentHidden = None
        self._AnyOf = None
        self._OneOf = None
        self._Input = None

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
    def Desc(self):
        r"""参数描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Type(self):
        r"""参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def DefaultValue(self):
        r"""参数默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def SubParams(self):
        r"""子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :rtype: list of AgentToolReqParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def GlobalHidden(self):
        r"""是否隐藏不可见
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def AgentHidden(self):
        r"""agent模式下模型是否可见
        :rtype: bool
        """
        return self._AgentHidden

    @AgentHidden.setter
    def AgentHidden(self, AgentHidden):
        self._AgentHidden = AgentHidden

    @property
    def AnyOf(self):
        r"""其中任意
        :rtype: list of AgentToolReqParam
        """
        return self._AnyOf

    @AnyOf.setter
    def AnyOf(self, AnyOf):
        self._AnyOf = AnyOf

    @property
    def OneOf(self):
        r"""其中一个
        :rtype: list of AgentToolReqParam
        """
        return self._OneOf

    @OneOf.setter
    def OneOf(self, OneOf):
        self._OneOf = OneOf

    @property
    def Input(self):
        r"""输入
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Type = params.get("Type")
        self._IsRequired = params.get("IsRequired")
        self._DefaultValue = params.get("DefaultValue")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = AgentToolReqParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._GlobalHidden = params.get("GlobalHidden")
        self._AgentHidden = params.get("AgentHidden")
        if params.get("AnyOf") is not None:
            self._AnyOf = []
            for item in params.get("AnyOf"):
                obj = AgentToolReqParam()
                obj._deserialize(item)
                self._AnyOf.append(obj)
        if params.get("OneOf") is not None:
            self._OneOf = []
            for item in params.get("OneOf"):
                obj = AgentToolReqParam()
                obj._deserialize(item)
                self._OneOf.append(obj)
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
        


class AgentToolRspParam(AbstractModel):
    r"""Agent工具的响应参数定义

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _Desc: 参数描述
        :type Desc: str
        :param _Type: 参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object
        :type Type: int
        :param _SubParams: 子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :type SubParams: list of AgentToolRspParam
        :param _AgentHidden: agent模式下模型是否可见
        :type AgentHidden: bool
        :param _GlobalHidden: 是否隐藏不可见
        :type GlobalHidden: bool
        :param _AnalysisMethod: COVER: 覆盖解析 INCREMENT:增量解析
        :type AnalysisMethod: str
        """
        self._Name = None
        self._Desc = None
        self._Type = None
        self._SubParams = None
        self._AgentHidden = None
        self._GlobalHidden = None
        self._AnalysisMethod = None

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
    def Desc(self):
        r"""参数描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Type(self):
        r"""参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubParams(self):
        r"""子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :rtype: list of AgentToolRspParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def AgentHidden(self):
        r"""agent模式下模型是否可见
        :rtype: bool
        """
        return self._AgentHidden

    @AgentHidden.setter
    def AgentHidden(self, AgentHidden):
        self._AgentHidden = AgentHidden

    @property
    def GlobalHidden(self):
        r"""是否隐藏不可见
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def AnalysisMethod(self):
        r"""COVER: 覆盖解析 INCREMENT:增量解析
        :rtype: str
        """
        return self._AnalysisMethod

    @AnalysisMethod.setter
    def AnalysisMethod(self, AnalysisMethod):
        self._AnalysisMethod = AnalysisMethod


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Type = params.get("Type")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = AgentToolRspParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._AgentHidden = params.get("AgentHidden")
        self._GlobalHidden = params.get("GlobalHidden")
        self._AnalysisMethod = params.get("AnalysisMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiVarAttrInfo(AbstractModel):
    r"""自定义变量和标签关系数据

    """

    def __init__(self):
        r"""
        :param _ApiVarId: 自定义变量id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiVarId: str
        :param _AttrBizId: 标签id
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrBizId: str
        """
        self._ApiVarId = None
        self._AttrBizId = None

    @property
    def ApiVarId(self):
        r"""自定义变量id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApiVarId

    @ApiVarId.setter
    def ApiVarId(self, ApiVarId):
        self._ApiVarId = ApiVarId

    @property
    def AttrBizId(self):
        r"""标签id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId


    def _deserialize(self, params):
        self._ApiVarId = params.get("ApiVarId")
        self._AttrBizId = params.get("AttrBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppBaseInfo(AbstractModel):
    r"""应用基础信息

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _AppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        """
        self._AppBizId = None
        self._AppName = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppName(self):
        r"""应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppConfig(AbstractModel):
    r"""应用配置

    """

    def __init__(self):
        r"""
        :param _KnowledgeQa: 知识问答管理应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeQa: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaConfig`
        :param _Summary: 知识摘要应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.lke.v20231130.models.SummaryConfig`
        :param _Classify: 标签提取应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Classify: :class:`tencentcloud.lke.v20231130.models.ClassifyConfig`
        """
        self._KnowledgeQa = None
        self._Summary = None
        self._Classify = None

    @property
    def KnowledgeQa(self):
        r"""知识问答管理应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaConfig`
        """
        return self._KnowledgeQa

    @KnowledgeQa.setter
    def KnowledgeQa(self, KnowledgeQa):
        self._KnowledgeQa = KnowledgeQa

    @property
    def Summary(self):
        r"""知识摘要应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SummaryConfig`
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Classify(self):
        r"""标签提取应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ClassifyConfig`
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify


    def _deserialize(self, params):
        if params.get("KnowledgeQa") is not None:
            self._KnowledgeQa = KnowledgeQaConfig()
            self._KnowledgeQa._deserialize(params.get("KnowledgeQa"))
        if params.get("Summary") is not None:
            self._Summary = SummaryConfig()
            self._Summary._deserialize(params.get("Summary"))
        if params.get("Classify") is not None:
            self._Classify = ClassifyConfig()
            self._Classify._deserialize(params.get("Classify"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppInfo(AbstractModel):
    r"""应用详情

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
注意：此字段可能返回 null，表示取不到有效值。
        :type AppType: str
        :param _AppTypeDesc: 应用类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AppTypeDesc: str
        :param _AppBizId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Avatar: 应用头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Desc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _AppStatus: 应用状态，1：未上线，2：运行中，3：停用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: int
        :param _AppStatusDesc: 状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatusDesc: str
        :param _UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Operator: 最后修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _ModelAliasName: 生成模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAliasName: str
        :param _Pattern: 应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
注意：此字段可能返回 null，表示取不到有效值。
        :type Pattern: str
        :param _ThoughtModelAliasName: 思考模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :type ThoughtModelAliasName: str
        :param _PermissionIds: 权限位信息
        :type PermissionIds: list of str
        :param _Creator: 创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        """
        self._AppType = None
        self._AppTypeDesc = None
        self._AppBizId = None
        self._Name = None
        self._Avatar = None
        self._Desc = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._UpdateTime = None
        self._Operator = None
        self._ModelName = None
        self._ModelAliasName = None
        self._Pattern = None
        self._ThoughtModelAliasName = None
        self._PermissionIds = None
        self._Creator = None

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        r"""应用类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def AppBizId(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Name(self):
        r"""应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        r"""应用头像
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        r"""应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def AppStatus(self):
        r"""应用状态，1：未上线，2：运行中，3：停用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        r"""状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

    @property
    def UpdateTime(self):
        r"""修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        r"""最后修改人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ModelName(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelAliasName(self):
        r"""生成模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelAliasName

    @ModelAliasName.setter
    def ModelAliasName(self, ModelAliasName):
        self._ModelAliasName = ModelAliasName

    @property
    def Pattern(self):
        r"""应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ThoughtModelAliasName(self):
        r"""思考模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ThoughtModelAliasName

    @ThoughtModelAliasName.setter
    def ThoughtModelAliasName(self, ThoughtModelAliasName):
        self._ThoughtModelAliasName = ThoughtModelAliasName

    @property
    def PermissionIds(self):
        r"""权限位信息
        :rtype: list of str
        """
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def Creator(self):
        r"""创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        self._AppBizId = params.get("AppBizId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._ModelName = params.get("ModelName")
        self._ModelAliasName = params.get("ModelAliasName")
        self._Pattern = params.get("Pattern")
        self._ThoughtModelAliasName = params.get("ThoughtModelAliasName")
        self._PermissionIds = params.get("PermissionIds")
        self._Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppModel(AbstractModel):
    r"""应用模型配置

    """

    def __init__(self):
        r"""
        :param _Name: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Desc: 模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _ContextLimit: 上下文指代轮次
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextLimit: int
        :param _AliasName: 模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _TokenBalance: token余量
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenBalance: float
        :param _IsUseContext: 是否使用上下文指代轮次
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUseContext: bool
        :param _HistoryLimit: 上下文记忆轮数
注意：此字段可能返回 null，表示取不到有效值。
        :type HistoryLimit: int
        :param _UsageType: 使用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageType: str
        :param _Temperature: 模型温度
注意：此字段可能返回 null，表示取不到有效值。
        :type Temperature: str
        :param _TopP: 模型TopP
注意：此字段可能返回 null，表示取不到有效值。
        :type TopP: str
        :param _ResourceStatus: 模型资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        :param _ModelParams: 模型参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelParams: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        """
        self._Name = None
        self._Desc = None
        self._ContextLimit = None
        self._AliasName = None
        self._TokenBalance = None
        self._IsUseContext = None
        self._HistoryLimit = None
        self._UsageType = None
        self._Temperature = None
        self._TopP = None
        self._ResourceStatus = None
        self._ModelParams = None

    @property
    def Name(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ContextLimit(self):
        r"""上下文指代轮次
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ContextLimit

    @ContextLimit.setter
    def ContextLimit(self, ContextLimit):
        self._ContextLimit = ContextLimit

    @property
    def AliasName(self):
        r"""模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TokenBalance(self):
        r"""token余量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TokenBalance

    @TokenBalance.setter
    def TokenBalance(self, TokenBalance):
        self._TokenBalance = TokenBalance

    @property
    def IsUseContext(self):
        r"""是否使用上下文指代轮次
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUseContext

    @IsUseContext.setter
    def IsUseContext(self, IsUseContext):
        self._IsUseContext = IsUseContext

    @property
    def HistoryLimit(self):
        r"""上下文记忆轮数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def UsageType(self):
        r"""使用类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UsageType

    @UsageType.setter
    def UsageType(self, UsageType):
        self._UsageType = UsageType

    @property
    def Temperature(self):
        r"""模型温度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        r"""模型TopP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def ResourceStatus(self):
        r"""模型资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ModelParams(self):
        r"""模型参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ContextLimit = params.get("ContextLimit")
        self._AliasName = params.get("AliasName")
        self._TokenBalance = params.get("TokenBalance")
        self._IsUseContext = params.get("IsUseContext")
        self._HistoryLimit = params.get("HistoryLimit")
        self._UsageType = params.get("UsageType")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._ResourceStatus = params.get("ResourceStatus")
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
        


class AppModelDetailInfo(AbstractModel):
    r"""模型详情

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelParams: 模型参数
        :type ModelParams: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        :param _HistoryLimit: 限制
        :type HistoryLimit: int
        :param _AliasName: 模型别名
        :type AliasName: str
        """
        self._ModelName = None
        self._ModelParams = None
        self._HistoryLimit = None
        self._AliasName = None

    @property
    def ModelName(self):
        r"""模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelParams(self):
        r"""模型参数
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParams`
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams

    @property
    def HistoryLimit(self):
        r"""限制
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def AliasName(self):
        r"""模型别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        if params.get("ModelParams") is not None:
            self._ModelParams = ModelParams()
            self._ModelParams._deserialize(params.get("ModelParams"))
        self._HistoryLimit = params.get("HistoryLimit")
        self._AliasName = params.get("AliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabel(AbstractModel):
    r"""标签详情信息

    """

    def __init__(self):
        r"""
        :param _Source: 标签来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _AttrBizId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrBizId: str
        :param _AttrKey: 标签标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrKey: str
        :param _AttrName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrName: str
        :param _Labels: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        """
        self._Source = None
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._Labels = None

    @property
    def Source(self):
        r"""标签来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttrBizId(self):
        r"""标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        r"""标签标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        r"""标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelDetail(AbstractModel):
    r"""标签详情

    """

    def __init__(self):
        r"""
        :param _AttrBizId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrBizId: str
        :param _AttrKey: 标签标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrKey: str
        :param _AttrName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrName: str
        :param _LabelNames: 标签值名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelNames: list of str
        :param _IsUpdating: 标签是否在更新中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdating: bool
        :param _Status: 发布状态(1 待发布 2 发布中 3 已发布 4 发布失败)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _LabelTotalCount: 标签值总数
        :type LabelTotalCount: str
        """
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNames = None
        self._IsUpdating = None
        self._Status = None
        self._StatusDesc = None
        self._LabelTotalCount = None

    @property
    def AttrBizId(self):
        r"""标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        warnings.warn("parameter `AttrKey` is deprecated", DeprecationWarning) 

        r"""标签标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        warnings.warn("parameter `AttrKey` is deprecated", DeprecationWarning) 

        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNames(self):
        r"""标签值名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LabelNames

    @LabelNames.setter
    def LabelNames(self, LabelNames):
        self._LabelNames = LabelNames

    @property
    def IsUpdating(self):
        r"""标签是否在更新中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUpdating

    @IsUpdating.setter
    def IsUpdating(self, IsUpdating):
        self._IsUpdating = IsUpdating

    @property
    def Status(self):
        r"""发布状态(1 待发布 2 发布中 3 已发布 4 发布失败)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def LabelTotalCount(self):
        r"""标签值总数
        :rtype: str
        """
        return self._LabelTotalCount

    @LabelTotalCount.setter
    def LabelTotalCount(self, LabelTotalCount):
        self._LabelTotalCount = LabelTotalCount


    def _deserialize(self, params):
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNames = params.get("LabelNames")
        self._IsUpdating = params.get("IsUpdating")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._LabelTotalCount = params.get("LabelTotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelRefer(AbstractModel):
    r"""标签引用信息

    """

    def __init__(self):
        r"""
        :param _Source: 标签来源，1：标签
        :type Source: int
        :param _AttributeBizId: 标签ID
        :type AttributeBizId: str
        :param _LabelBizIds: 标签值ID
        :type LabelBizIds: list of str
        """
        self._Source = None
        self._AttributeBizId = None
        self._LabelBizIds = None

    @property
    def Source(self):
        r"""标签来源，1：标签
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttributeBizId(self):
        r"""标签ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LabelBizIds(self):
        r"""标签值ID
        :rtype: list of str
        """
        return self._LabelBizIds

    @LabelBizIds.setter
    def LabelBizIds(self, LabelBizIds):
        self._LabelBizIds = LabelBizIds


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LabelBizIds = params.get("LabelBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeFilters(AbstractModel):
    r"""导出知识标签过滤器

    """

    def __init__(self):
        r"""
        :param _Query: 检索，属性或标签名称
        :type Query: str
        """
        self._Query = None

    @property
    def Query(self):
        r"""检索，属性或标签名称
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
        


class AttributeLabel(AbstractModel):
    r"""标签值

    """

    def __init__(self):
        r"""
        :param _LabelBizId: 标准词ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelBizId: str
        :param _LabelName: 标准词名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        :param _SimilarLabels: 同义词名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SimilarLabels: list of str
        """
        self._LabelBizId = None
        self._LabelName = None
        self._SimilarLabels = None

    @property
    def LabelBizId(self):
        r"""标准词ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        r"""标准词名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def SimilarLabels(self):
        r"""同义词名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SimilarLabels

    @SimilarLabels.setter
    def SimilarLabels(self, SimilarLabels):
        self._SimilarLabels = SimilarLabels


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        self._SimilarLabels = params.get("SimilarLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeLabelRefByWorkflow(AbstractModel):
    r"""标签值引用的工作流详情

    """

    def __init__(self):
        r"""
        :param _AttributeLabelBizId: 标签值id
        :type AttributeLabelBizId: str
        :param _WorkflowList: 标签值引用的工作流列表
        :type WorkflowList: list of WorkflowRef
        """
        self._AttributeLabelBizId = None
        self._WorkflowList = None

    @property
    def AttributeLabelBizId(self):
        r"""标签值id
        :rtype: str
        """
        return self._AttributeLabelBizId

    @AttributeLabelBizId.setter
    def AttributeLabelBizId(self, AttributeLabelBizId):
        self._AttributeLabelBizId = AttributeLabelBizId

    @property
    def WorkflowList(self):
        r"""标签值引用的工作流列表
        :rtype: list of WorkflowRef
        """
        return self._WorkflowList

    @WorkflowList.setter
    def WorkflowList(self, WorkflowList):
        self._WorkflowList = WorkflowList


    def _deserialize(self, params):
        self._AttributeLabelBizId = params.get("AttributeLabelBizId")
        if params.get("WorkflowList") is not None:
            self._WorkflowList = []
            for item in params.get("WorkflowList"):
                obj = WorkflowRef()
                obj._deserialize(item)
                self._WorkflowList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackgroundImageConfig(AbstractModel):
    r"""背景图相关配置

    """

    def __init__(self):
        r"""
        :param _LandscapeImageUrl: 横图(pc)
        :type LandscapeImageUrl: str
        :param _OriginalImageUrl: 原始图
        :type OriginalImageUrl: str
        :param _PortraitImageUrl: 长图(手机)
        :type PortraitImageUrl: str
        :param _ThemeColor: 主题色
        :type ThemeColor: str
        :param _Brightness: 亮度值
        :type Brightness: int
        """
        self._LandscapeImageUrl = None
        self._OriginalImageUrl = None
        self._PortraitImageUrl = None
        self._ThemeColor = None
        self._Brightness = None

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

    @property
    def Brightness(self):
        r"""亮度值
        :rtype: int
        """
        return self._Brightness

    @Brightness.setter
    def Brightness(self, Brightness):
        self._Brightness = Brightness


    def _deserialize(self, params):
        self._LandscapeImageUrl = params.get("LandscapeImageUrl")
        self._OriginalImageUrl = params.get("OriginalImageUrl")
        self._PortraitImageUrl = params.get("PortraitImageUrl")
        self._ThemeColor = params.get("ThemeColor")
        self._Brightness = params.get("Brightness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseConfig(AbstractModel):
    r"""应用基础配置

    """

    def __init__(self):
        r"""
        :param _Name: 应用名称
        :type Name: str
        :param _Avatar: 应用头像url，在CreateApp和ModifyApp中作为入参必填。
作为入参传入说明：
1. 传入的url图片限制为jpeg和png，大小限制为500KB，url链接需允许head请求。
2. 如果用户没有对象存储，可使用“获取文件上传临时密钥”(DescribeStorageCredential)接口，获取cos临时密钥和上传路径，自行上传头像至cos中并获取访问链接。
        :type Avatar: str
        :param _Desc: 应用描述
        :type Desc: str
        """
        self._Name = None
        self._Avatar = None
        self._Desc = None

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
    def Avatar(self):
        r"""应用头像url，在CreateApp和ModifyApp中作为入参必填。
作为入参传入说明：
1. 传入的url图片限制为jpeg和png，大小限制为500KB，url链接需允许head请求。
2. 如果用户没有对象存储，可使用“获取文件上传临时密钥”(DescribeStorageCredential)接口，获取cos临时密钥和上传路径，自行上传头像至cos中并获取访问链接。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        r"""应用描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDetail(AbstractModel):
    r"""调用类型

    """

    def __init__(self):
        r"""
        :param _Id: 关联ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _CallTime: 调用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CallTime: str
        :param _TotalTokenUsage: 总token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTokenUsage: float
        :param _InputTokenUsage: 输入token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type InputTokenUsage: float
        :param _OutputTokenUsage: 输出token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputTokenUsage: float
        :param _SearchUsage: 搜索服务调用次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchUsage: int
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _CallType: 调用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CallType: str
        :param _UinAccount: 账号
注意：此字段可能返回 null，表示取不到有效值。
        :type UinAccount: str
        :param _AppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _PageUsage: 总消耗页数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageUsage: int
        :param _SubScene: 筛选子场景
注意：此字段可能返回 null，表示取不到有效值。
        :type SubScene: str
        :param _BillingTag: 账单明细对应的自定义tag
        :type BillingTag: str
        """
        self._Id = None
        self._CallTime = None
        self._TotalTokenUsage = None
        self._InputTokenUsage = None
        self._OutputTokenUsage = None
        self._SearchUsage = None
        self._ModelName = None
        self._CallType = None
        self._UinAccount = None
        self._AppName = None
        self._PageUsage = None
        self._SubScene = None
        self._BillingTag = None

    @property
    def Id(self):
        r"""关联ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CallTime(self):
        r"""调用时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallTime

    @CallTime.setter
    def CallTime(self, CallTime):
        self._CallTime = CallTime

    @property
    def TotalTokenUsage(self):
        r"""总token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalTokenUsage

    @TotalTokenUsage.setter
    def TotalTokenUsage(self, TotalTokenUsage):
        self._TotalTokenUsage = TotalTokenUsage

    @property
    def InputTokenUsage(self):
        r"""输入token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._InputTokenUsage

    @InputTokenUsage.setter
    def InputTokenUsage(self, InputTokenUsage):
        self._InputTokenUsage = InputTokenUsage

    @property
    def OutputTokenUsage(self):
        r"""输出token消耗
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._OutputTokenUsage

    @OutputTokenUsage.setter
    def OutputTokenUsage(self, OutputTokenUsage):
        self._OutputTokenUsage = OutputTokenUsage

    @property
    def SearchUsage(self):
        r"""搜索服务调用次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SearchUsage

    @SearchUsage.setter
    def SearchUsage(self, SearchUsage):
        self._SearchUsage = SearchUsage

    @property
    def ModelName(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def CallType(self):
        r"""调用类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def UinAccount(self):
        r"""账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def AppName(self):
        r"""应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PageUsage(self):
        r"""总消耗页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageUsage

    @PageUsage.setter
    def PageUsage(self, PageUsage):
        self._PageUsage = PageUsage

    @property
    def SubScene(self):
        r"""筛选子场景
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubScene

    @SubScene.setter
    def SubScene(self, SubScene):
        self._SubScene = SubScene

    @property
    def BillingTag(self):
        r"""账单明细对应的自定义tag
        :rtype: str
        """
        return self._BillingTag

    @BillingTag.setter
    def BillingTag(self, BillingTag):
        self._BillingTag = BillingTag


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CallTime = params.get("CallTime")
        self._TotalTokenUsage = params.get("TotalTokenUsage")
        self._InputTokenUsage = params.get("InputTokenUsage")
        self._OutputTokenUsage = params.get("OutputTokenUsage")
        self._SearchUsage = params.get("SearchUsage")
        self._ModelName = params.get("ModelName")
        self._CallType = params.get("CallType")
        self._UinAccount = params.get("UinAccount")
        self._AppName = params.get("AppName")
        self._PageUsage = params.get("PageUsage")
        self._SubScene = params.get("SubScene")
        self._BillingTag = params.get("BillingTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CateInfo(AbstractModel):
    r"""分类信息

    """

    def __init__(self):
        r"""
        :param _CateBizId: 分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateBizId: str
        :param _Name: 分类名称

注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Total: 分类下的Record（如文档、同义词等）数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _CanAdd: 是否可新增

注意：此字段可能返回 null，表示取不到有效值。
        :type CanAdd: bool
        :param _CanEdit: 是否可编辑

注意：此字段可能返回 null，表示取不到有效值。
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

注意：此字段可能返回 null，表示取不到有效值。
        :type CanDelete: bool
        :param _Children: 子分类
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of CateInfo
        :param _IsLeaf: 是否为叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLeaf: bool
        """
        self._CateBizId = None
        self._Name = None
        self._Total = None
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._Children = None
        self._IsLeaf = None

    @property
    def CateBizId(self):
        r"""分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Name(self):
        r"""分类名称

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        r"""分类下的Record（如文档、同义词等）数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CanAdd(self):
        r"""是否可新增

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        r"""是否可编辑

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        r"""是否可删除

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Children(self):
        r"""子分类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CateInfo
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def IsLeaf(self):
        r"""是否为叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf


    def _deserialize(self, params):
        self._CateBizId = params.get("CateBizId")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = CateInfo()
                obj._deserialize(item)
                self._Children.append(obj)
        self._IsLeaf = params.get("IsLeaf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelListInfo(AbstractModel):
    r"""渠道详情信息

    """

    def __init__(self):
        r"""
        :param _ChannelType: 渠道类型 10000 微信订阅号 10001 微信服务号 10002 企微应用
        :type ChannelType: int
        :param _ChannelStatus: 渠道状态 1未发布 2运行中 3已下线
        :type ChannelStatus: int
        :param _ChannelName: 渠道名称
        :type ChannelName: str
        :param _ChannelId: 渠道id 数据库主键
        :type ChannelId: str
        :param _Comment: 备注
        :type Comment: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdatedUser: 最后更新人
        :type UpdatedUser: str
        :param _YuanQiInfo: 智能体应用可见范围，public-所有人可见 private-仅自己可见 share-通过分享可见
注意：此字段可能返回 null，表示取不到有效值。
        :type YuanQiInfo: :class:`tencentcloud.lke.v20231130.models.YuanQi`
        """
        self._ChannelType = None
        self._ChannelStatus = None
        self._ChannelName = None
        self._ChannelId = None
        self._Comment = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UpdatedUser = None
        self._YuanQiInfo = None

    @property
    def ChannelType(self):
        r"""渠道类型 10000 微信订阅号 10001 微信服务号 10002 企微应用
        :rtype: int
        """
        return self._ChannelType

    @ChannelType.setter
    def ChannelType(self, ChannelType):
        self._ChannelType = ChannelType

    @property
    def ChannelStatus(self):
        r"""渠道状态 1未发布 2运行中 3已下线
        :rtype: int
        """
        return self._ChannelStatus

    @ChannelStatus.setter
    def ChannelStatus(self, ChannelStatus):
        self._ChannelStatus = ChannelStatus

    @property
    def ChannelName(self):
        r"""渠道名称
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelId(self):
        r"""渠道id 数据库主键
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Comment(self):
        r"""备注
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
    def UpdatedUser(self):
        r"""最后更新人
        :rtype: str
        """
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def YuanQiInfo(self):
        r"""智能体应用可见范围，public-所有人可见 private-仅自己可见 share-通过分享可见
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.YuanQi`
        """
        return self._YuanQiInfo

    @YuanQiInfo.setter
    def YuanQiInfo(self, YuanQiInfo):
        self._YuanQiInfo = YuanQiInfo


    def _deserialize(self, params):
        self._ChannelType = params.get("ChannelType")
        self._ChannelStatus = params.get("ChannelStatus")
        self._ChannelName = params.get("ChannelName")
        self._ChannelId = params.get("ChannelId")
        self._Comment = params.get("Comment")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdatedUser = params.get("UpdatedUser")
        if params.get("YuanQiInfo") is not None:
            self._YuanQiInfo = YuanQi()
            self._YuanQiInfo._deserialize(params.get("YuanQiInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistRequest(AbstractModel):
    r"""CheckAttributeLabelExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _LabelName: 标签名称
        :type LabelName: str
        :param _AttributeBizId: 标签ID
        :type AttributeBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _LastLabelBizId: 最后一个标签ID。用于滚动加载：是一种分批、滚动式的存在性检查机制。客户端需要持续调用接口，并每次传入上一次返回的最后一个记录的ID，直到接口明确返回“存在”或“已检查全部数据且不存在”为止。
        :type LastLabelBizId: str
        """
        self._BotBizId = None
        self._LabelName = None
        self._AttributeBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LastLabelBizId = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LabelName(self):
        r"""标签名称
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def AttributeBizId(self):
        r"""标签ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LastLabelBizId(self):
        r"""最后一个标签ID。用于滚动加载：是一种分批、滚动式的存在性检查机制。客户端需要持续调用接口，并每次传入上一次返回的最后一个记录的ID，直到接口明确返回“存在”或“已检查全部数据且不存在”为止。
        :rtype: str
        """
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LabelName = params.get("LabelName")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LastLabelBizId = params.get("LastLabelBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistResponse(AbstractModel):
    r"""CheckAttributeLabelExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsExist: 是否存在
        :type IsExist: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsExist = None
        self._RequestId = None

    @property
    def IsExist(self):
        r"""是否存在
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

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
        self._IsExist = params.get("IsExist")
        self._RequestId = params.get("RequestId")


class CheckAttributeLabelReferRequest(AbstractModel):
    r"""CheckAttributeLabelRefer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _LabelBizId: 属性标签ID
        :type LabelBizId: str
        :param _AttributeBizId: 标签ID
        :type AttributeBizId: list of str
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LabelBizId = None
        self._AttributeBizId = None

    @property
    def BotBizId(self):
        r"""应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LabelBizId(self):
        r"""属性标签ID
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def AttributeBizId(self):
        r"""标签ID
        :rtype: list of str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LabelBizId = params.get("LabelBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelReferResponse(AbstractModel):
    r"""CheckAttributeLabelRefer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsRefer: 是否引用
        :type IsRefer: bool
        :param _List: 引用的工作流详情
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of AttributeLabelRefByWorkflow
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsRefer = None
        self._List = None
        self._RequestId = None

    @property
    def IsRefer(self):
        r"""是否引用
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def List(self):
        r"""引用的工作流详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttributeLabelRefByWorkflow
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._IsRefer = params.get("IsRefer")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttributeLabelRefByWorkflow()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ClassifyConfig(AbstractModel):
    r"""标签提取配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Labels: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of ClassifyLabel
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        """
        self._Model = None
        self._Labels = None
        self._Greeting = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Labels(self):
        r"""标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClassifyLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Greeting(self):
        r"""欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = ClassifyLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyLabel(AbstractModel):
    r"""标签信息

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 标签描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Values: 标签取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Name = None
        self._Description = None
        self._Values = None

    @property
    def Name(self):
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""标签描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Values(self):
        r"""标签取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Context(AbstractModel):
    r"""获取不满意回复上下文响

    """

    def __init__(self):
        r"""
        :param _RecordBizId: 消息记录ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordBizId: str
        :param _IsVisitor: 是否为用户
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVisitor: bool
        :param _NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Content: 消息内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _FileInfos: 文档信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of MsgFileInfo
        :param _ReplyMethod: 回复方式，15：澄清确认回复
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyMethod: int
        """
        self._RecordBizId = None
        self._IsVisitor = None
        self._NickName = None
        self._Avatar = None
        self._Content = None
        self._FileInfos = None
        self._ReplyMethod = None

    @property
    def RecordBizId(self):
        r"""消息记录ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def IsVisitor(self):
        r"""是否为用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVisitor

    @IsVisitor.setter
    def IsVisitor(self, IsVisitor):
        self._IsVisitor = IsVisitor

    @property
    def NickName(self):
        r"""昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Avatar(self):
        r"""头像
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Content(self):
        r"""消息内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileInfos(self):
        r"""文档信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MsgFileInfo
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def ReplyMethod(self):
        r"""回复方式，15：澄清确认回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod


    def _deserialize(self, params):
        self._RecordBizId = params.get("RecordBizId")
        self._IsVisitor = params.get("IsVisitor")
        self._NickName = params.get("NickName")
        self._Avatar = params.get("Avatar")
        self._Content = params.get("Content")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = MsgFileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        self._ReplyMethod = params.get("ReplyMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    r"""CreateApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理
        :type AppType: str
        :param _BaseConfig: 应用基础配置
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _Pattern: 应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :type Pattern: str
        :param _AgentType: 智能体类型 dialogue 对话式智能体，wechat 公众号智能体
        :type AgentType: str
        """
        self._AppType = None
        self._BaseConfig = None
        self._Pattern = None
        self._AgentType = None

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        r"""应用基础配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def Pattern(self):
        r"""应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def AgentType(self):
        r"""智能体类型 dialogue 对话式智能体，wechat 公众号智能体
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        self._Pattern = params.get("Pattern")
        self._AgentType = params.get("AgentType")
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
        :param _AppBizId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _IsCustomList: 判断账户应用列表权限是否是自定义的，用户交互提示
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCustomList: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._IsCustomList = None
        self._RequestId = None

    @property
    def AppBizId(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def IsCustomList(self):
        r"""判断账户应用列表权限是否是自定义的，用户交互提示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsCustomList

    @IsCustomList.setter
    def IsCustomList(self, IsCustomList):
        self._IsCustomList = IsCustomList

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
        self._AppBizId = params.get("AppBizId")
        self._IsCustomList = params.get("IsCustomList")
        self._RequestId = params.get("RequestId")


class CreateAttributeLabelRequest(AbstractModel):
    r"""CreateAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _AttrName: 标签名
        :type AttrName: str
        :param _Labels: 标签值
        :type Labels: list of AttributeLabel
        :param _AttrKey: 标签标识（不生效，无需填写） 已作废
        :type AttrKey: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttrName = None
        self._Labels = None
        self._AttrKey = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttrName(self):
        r"""标签名
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        r"""标签值
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def AttrKey(self):
        r"""标签标识（不生效，无需填写） 已作废
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._AttrKey = params.get("AttrKey")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttributeLabelResponse(AbstractModel):
    r"""CreateAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttrBizId: 标签ID
        :type AttrBizId: str
        :param _Labels: 标签值ID与名称
        :type Labels: list of AttributeLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttrBizId = None
        self._Labels = None
        self._RequestId = None

    @property
    def AttrBizId(self):
        r"""标签ID
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def Labels(self):
        r"""标签值ID与名称
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

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
        self._AttrBizId = params.get("AttrBizId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDocCateRequest(AbstractModel):
    r"""CreateDocCate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ParentBizId: 父级业务ID
        :type ParentBizId: str
        :param _Name: 分类名称

        :type Name: str
        """
        self._BotBizId = None
        self._ParentBizId = None
        self._Name = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ParentBizId(self):
        r"""父级业务ID
        :rtype: str
        """
        return self._ParentBizId

    @ParentBizId.setter
    def ParentBizId(self, ParentBizId):
        self._ParentBizId = ParentBizId

    @property
    def Name(self):
        r"""分类名称

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ParentBizId = params.get("ParentBizId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocCateResponse(AbstractModel):
    r"""CreateDocCate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CanAdd: 是否可新增

        :type CanAdd: bool
        :param _CanEdit: 是否可编辑
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

        :type CanDelete: bool
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def CanAdd(self):
        r"""是否可新增

        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        r"""是否可编辑
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        r"""是否可删除

        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class CreateQACateRequest(AbstractModel):
    r"""CreateQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ParentBizId: 父级业务ID，创建顶级分类时传字符串"0"
        :type ParentBizId: str
        :param _Name: 分类名称

        :type Name: str
        """
        self._BotBizId = None
        self._ParentBizId = None
        self._Name = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ParentBizId(self):
        r"""父级业务ID，创建顶级分类时传字符串"0"
        :rtype: str
        """
        return self._ParentBizId

    @ParentBizId.setter
    def ParentBizId(self, ParentBizId):
        self._ParentBizId = ParentBizId

    @property
    def Name(self):
        r"""分类名称

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ParentBizId = params.get("ParentBizId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQACateResponse(AbstractModel):
    r"""CreateQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CanAdd: 是否可新增

        :type CanAdd: bool
        :param _CanEdit: 是否可编辑
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

        :type CanDelete: bool
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def CanAdd(self):
        r"""是否可新增

        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        r"""是否可编辑
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        r"""是否可删除

        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class CreateQARequest(AbstractModel):
    r"""CreateQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
若要操作共享知识库，传KnowledgeBizId
        :type BotBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _AttrRange: 标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _AttrLabels: 标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _ExpireStart: 有效开始时间，单位是unix时间戳。默认值为0，表示问答为永久有效.
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        :param _SimilarQuestions: 相似问内容
        :type SimilarQuestions: list of str
        :param _QuestionDesc: 问题描述
        :type QuestionDesc: str
        :param _EnableScope: 问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        """
        self._BotBizId = None
        self._Question = None
        self._Answer = None
        self._AttrRange = None
        self._CustomParam = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestions = None
        self._QuestionDesc = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID
若要操作共享知识库，传KnowledgeBizId
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

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
    def Answer(self):
        r"""答案
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttrRange(self):
        r"""标签适用范围 1：全部，2：按条件
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def CustomParam(self):
        r"""自定义参数
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrLabels(self):
        r"""标签引用
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        r"""有效开始时间，单位是unix时间戳。默认值为0，表示问答为永久有效.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，unix时间戳，0代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestions(self):
        r"""相似问内容
        :rtype: list of str
        """
        return self._SimilarQuestions

    @SimilarQuestions.setter
    def SimilarQuestions(self, SimilarQuestions):
        self._SimilarQuestions = SimilarQuestions

    @property
    def QuestionDesc(self):
        r"""问题描述
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc

    @property
    def EnableScope(self):
        r"""问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._AttrRange = params.get("AttrRange")
        self._CustomParam = params.get("CustomParam")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._SimilarQuestions = params.get("SimilarQuestions")
        self._QuestionDesc = params.get("QuestionDesc")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQAResponse(AbstractModel):
    r"""CreateQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QaBizId = None
        self._RequestId = None

    @property
    def QaBizId(self):
        r"""问答ID
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

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
        self._QaBizId = params.get("QaBizId")
        self._RequestId = params.get("RequestId")


class CreateRejectedQuestionRequest(AbstractModel):
    r"""CreateRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID, 获取方式参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _Question: 拒答问题


        :type Question: str
        :param _BusinessSource: 拒答问题来源， 1- 来源于不满意回复;  2 - 来源于手动添加
        :type BusinessSource: int
        :param _BusinessId: 拒答问题来源的数据源唯一id


        :type BusinessId: str
        """
        self._BotBizId = None
        self._Question = None
        self._BusinessSource = None
        self._BusinessId = None

    @property
    def BotBizId(self):
        r"""应用ID, 获取方式参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        r"""拒答问题


        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def BusinessSource(self):
        r"""拒答问题来源， 1- 来源于不满意回复;  2 - 来源于手动添加
        :rtype: int
        """
        return self._BusinessSource

    @BusinessSource.setter
    def BusinessSource(self, BusinessSource):
        self._BusinessSource = BusinessSource

    @property
    def BusinessId(self):
        r"""拒答问题来源的数据源唯一id


        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._BusinessSource = params.get("BusinessSource")
        self._BusinessId = params.get("BusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRejectedQuestionResponse(AbstractModel):
    r"""CreateRejectedQuestion返回参数结构体

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


class CreateReleaseRequest(AbstractModel):
    r"""CreateRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Desc: 发布描述
        :type Desc: str
        :param _ChannelBizIds: 渠道业务ID，从ListChannel接口的响应字段ChannelId获取
        :type ChannelBizIds: list of str
        """
        self._BotBizId = None
        self._Desc = None
        self._ChannelBizIds = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Desc(self):
        r"""发布描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ChannelBizIds(self):
        r"""渠道业务ID，从ListChannel接口的响应字段ChannelId获取
        :rtype: list of str
        """
        return self._ChannelBizIds

    @ChannelBizIds.setter
    def ChannelBizIds(self, ChannelBizIds):
        self._ChannelBizIds = ChannelBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Desc = params.get("Desc")
        self._ChannelBizIds = params.get("ChannelBizIds")
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
        :param _ReleaseBizId: 发布ID
        :type ReleaseBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseBizId = None
        self._RequestId = None

    @property
    def ReleaseBizId(self):
        r"""发布ID
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

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
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._RequestId = params.get("RequestId")


class CreateSharedKnowledgeRequest(AbstractModel):
    r"""CreateSharedKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeName: 共享知识库名称，字符数量范围：[1, 50]
        :type KnowledgeName: str
        :param _KnowledgeDescription: 共享知识库描述，字符数量上限2000
        :type KnowledgeDescription: str
        :param _EmbeddingModel: Embedding模型，字符数量上限128
        :type EmbeddingModel: str
        :param _KnowledgeType: 共享知识库类型，0普通，1公众号
        :type KnowledgeType: int
        """
        self._KnowledgeName = None
        self._KnowledgeDescription = None
        self._EmbeddingModel = None
        self._KnowledgeType = None

    @property
    def KnowledgeName(self):
        r"""共享知识库名称，字符数量范围：[1, 50]
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName

    @property
    def KnowledgeDescription(self):
        r"""共享知识库描述，字符数量上限2000
        :rtype: str
        """
        return self._KnowledgeDescription

    @KnowledgeDescription.setter
    def KnowledgeDescription(self, KnowledgeDescription):
        self._KnowledgeDescription = KnowledgeDescription

    @property
    def EmbeddingModel(self):
        warnings.warn("parameter `EmbeddingModel` is deprecated", DeprecationWarning) 

        r"""Embedding模型，字符数量上限128
        :rtype: str
        """
        return self._EmbeddingModel

    @EmbeddingModel.setter
    def EmbeddingModel(self, EmbeddingModel):
        warnings.warn("parameter `EmbeddingModel` is deprecated", DeprecationWarning) 

        self._EmbeddingModel = EmbeddingModel

    @property
    def KnowledgeType(self):
        r"""共享知识库类型，0普通，1公众号
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType


    def _deserialize(self, params):
        self._KnowledgeName = params.get("KnowledgeName")
        self._KnowledgeDescription = params.get("KnowledgeDescription")
        self._EmbeddingModel = params.get("EmbeddingModel")
        self._KnowledgeType = params.get("KnowledgeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSharedKnowledgeResponse(AbstractModel):
    r"""CreateSharedKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBizId = None
        self._RequestId = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

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
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._RequestId = params.get("RequestId")


class CreateVarRequest(AbstractModel):
    r"""CreateVar请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _VarName: 变量名称，不允许重复，最大支持50个字符
        :type VarName: str
        :param _VarDesc: 变量描述，最大支持120个字符
        :type VarDesc: str
        :param _VarType: 变量类型定义，支持类型如下：(STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO);传输过程是json字符串，标签中仅支持"STRING"类型使用
        :type VarType: str
        :param _VarDefaultValue: 自定义变量默认值
        :type VarDefaultValue: str
        :param _VarDefaultFileName: 自定义变量文件默认名称
        :type VarDefaultFileName: str
        :param _VarModuleType: 参数类型
        :type VarModuleType: int
        """
        self._AppBizId = None
        self._VarName = None
        self._VarDesc = None
        self._VarType = None
        self._VarDefaultValue = None
        self._VarDefaultFileName = None
        self._VarModuleType = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def VarName(self):
        r"""变量名称，不允许重复，最大支持50个字符
        :rtype: str
        """
        return self._VarName

    @VarName.setter
    def VarName(self, VarName):
        self._VarName = VarName

    @property
    def VarDesc(self):
        r"""变量描述，最大支持120个字符
        :rtype: str
        """
        return self._VarDesc

    @VarDesc.setter
    def VarDesc(self, VarDesc):
        self._VarDesc = VarDesc

    @property
    def VarType(self):
        r"""变量类型定义，支持类型如下：(STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO);传输过程是json字符串，标签中仅支持"STRING"类型使用
        :rtype: str
        """
        return self._VarType

    @VarType.setter
    def VarType(self, VarType):
        self._VarType = VarType

    @property
    def VarDefaultValue(self):
        r"""自定义变量默认值
        :rtype: str
        """
        return self._VarDefaultValue

    @VarDefaultValue.setter
    def VarDefaultValue(self, VarDefaultValue):
        self._VarDefaultValue = VarDefaultValue

    @property
    def VarDefaultFileName(self):
        r"""自定义变量文件默认名称
        :rtype: str
        """
        return self._VarDefaultFileName

    @VarDefaultFileName.setter
    def VarDefaultFileName(self, VarDefaultFileName):
        self._VarDefaultFileName = VarDefaultFileName

    @property
    def VarModuleType(self):
        r"""参数类型
        :rtype: int
        """
        return self._VarModuleType

    @VarModuleType.setter
    def VarModuleType(self, VarModuleType):
        self._VarModuleType = VarModuleType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._VarName = params.get("VarName")
        self._VarDesc = params.get("VarDesc")
        self._VarType = params.get("VarType")
        self._VarDefaultValue = params.get("VarDefaultValue")
        self._VarDefaultFileName = params.get("VarDefaultFileName")
        self._VarModuleType = params.get("VarModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVarResponse(AbstractModel):
    r"""CreateVar返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VarId: 变量ID
        :type VarId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VarId = None
        self._RequestId = None

    @property
    def VarId(self):
        r"""变量ID
        :rtype: str
        """
        return self._VarId

    @VarId.setter
    def VarId(self, VarId):
        self._VarId = VarId

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
        self._VarId = params.get("VarId")
        self._RequestId = params.get("RequestId")


class CreateWorkflowRunRequest(AbstractModel):
    r"""CreateWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type AppBizId: str
        :param _RunEnv: 运行环境。0: 测试环境； 1: 正式环境
        :type RunEnv: int
        :param _Query: 用户输入的内容
        :type Query: str
        :param _CustomVariables: API参数配置
        :type CustomVariables: list of CustomVariable
        """
        self._AppBizId = None
        self._RunEnv = None
        self._Query = None
        self._CustomVariables = None

    @property
    def AppBizId(self):
        r"""应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def RunEnv(self):
        r"""运行环境。0: 测试环境； 1: 正式环境
        :rtype: int
        """
        return self._RunEnv

    @RunEnv.setter
    def RunEnv(self, RunEnv):
        self._RunEnv = RunEnv

    @property
    def Query(self):
        r"""用户输入的内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def CustomVariables(self):
        r"""API参数配置
        :rtype: list of CustomVariable
        """
        return self._CustomVariables

    @CustomVariables.setter
    def CustomVariables(self, CustomVariables):
        self._CustomVariables = CustomVariables


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._RunEnv = params.get("RunEnv")
        self._Query = params.get("Query")
        if params.get("CustomVariables") is not None:
            self._CustomVariables = []
            for item in params.get("CustomVariables"):
                obj = CustomVariable()
                obj._deserialize(item)
                self._CustomVariables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowRunResponse(AbstractModel):
    r"""CreateWorkflowRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _WorkflowRunId: 工作流运行实例的ID
        :type WorkflowRunId: str
        :param _RunEnv: 运行环境。0: 测试环境； 1: 正式环境
        :type RunEnv: int
        :param _Query: 用户输入的内容
        :type Query: str
        :param _CustomVariables: API参数配置
        :type CustomVariables: list of CustomVariable
        :param _CreateTime: 创建时间（毫秒时间戳）
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._WorkflowRunId = None
        self._RunEnv = None
        self._Query = None
        self._CustomVariables = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例的ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def RunEnv(self):
        r"""运行环境。0: 测试环境； 1: 正式环境
        :rtype: int
        """
        return self._RunEnv

    @RunEnv.setter
    def RunEnv(self, RunEnv):
        self._RunEnv = RunEnv

    @property
    def Query(self):
        r"""用户输入的内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def CustomVariables(self):
        r"""API参数配置
        :rtype: list of CustomVariable
        """
        return self._CustomVariables

    @CustomVariables.setter
    def CustomVariables(self, CustomVariables):
        self._CustomVariables = CustomVariables

    @property
    def CreateTime(self):
        r"""创建时间（毫秒时间戳）
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
        self._AppBizId = params.get("AppBizId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._RunEnv = params.get("RunEnv")
        self._Query = params.get("Query")
        if params.get("CustomVariables") is not None:
            self._CustomVariables = []
            for item in params.get("CustomVariables"):
                obj = CustomVariable()
                obj._deserialize(item)
                self._CustomVariables.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    r"""临时密钥结构

    """

    def __init__(self):
        r"""
        :param _Token: token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _TmpSecretId: 临时证书密钥ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时证书密钥Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param _AppId: 临时证书appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._Token = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._AppId = None

    @property
    def Token(self):
        r"""token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def TmpSecretId(self):
        r"""临时证书密钥ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""临时证书密钥Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def AppId(self):
        r"""临时证书appid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomVariable(AbstractModel):
    r"""工作流的API参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _Value: 参数的值
        :type Value: str
        """
        self._Name = None
        self._Value = None

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
        r"""参数的值
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
        


class DeleteAgentRequest(AbstractModel):
    r"""DeleteAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent的ID
        :type AgentId: str
        :param _AppBizId: 应用ID
        :type AppBizId: str
        """
        self._AgentId = None
        self._AppBizId = None

    @property
    def AgentId(self):
        r"""Agent的ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AppBizId = params.get("AppBizId")
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
        :param _AgentId: Agent的ID
        :type AgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""Agent的ID
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


class DeleteAppRequest(AbstractModel):
    r"""DeleteApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        """
        self._AppBizId = None
        self._AppType = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
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


class DeleteAttributeLabelRequest(AbstractModel):
    r"""DeleteAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _AttributeBizIds: 标签ID
        :type AttributeBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttributeBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizIds(self):
        r"""标签ID
        :rtype: list of str
        """
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizIds = params.get("AttributeBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttributeLabelResponse(AbstractModel):
    r"""DeleteAttributeLabel返回参数结构体

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


class DeleteDocCateRequest(AbstractModel):
    r"""DeleteDocCate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocCateResponse(AbstractModel):
    r"""DeleteDocCate返回参数结构体

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


class DeleteDocRequest(AbstractModel):
    r"""DeleteDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizIds: 文档业务ID列表
        :type DocBizIds: list of str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._DocBizIds = None
        self._BotBizId = None

    @property
    def DocBizIds(self):
        r"""文档业务ID列表
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._DocBizIds = params.get("DocBizIds")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocResponse(AbstractModel):
    r"""DeleteDoc返回参数结构体

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


class DeleteQACateRequest(AbstractModel):
    r"""DeleteQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQACateResponse(AbstractModel):
    r"""DeleteQACate返回参数结构体

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


class DeleteQARequest(AbstractModel):
    r"""DeleteQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: 问答ID
        :type QaBizIds: list of str
        """
        self._BotBizId = None
        self._QaBizIds = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        r"""问答ID
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQAResponse(AbstractModel):
    r"""DeleteQA返回参数结构体

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


class DeleteRejectedQuestionRequest(AbstractModel):
    r"""DeleteRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :type BotBizId: str
        :param _RejectedBizIds: 拒答问题来源的数据源唯一id



        :type RejectedBizIds: list of str
        """
        self._BotBizId = None
        self._RejectedBizIds = None

    @property
    def BotBizId(self):
        r"""应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def RejectedBizIds(self):
        r"""拒答问题来源的数据源唯一id



        :rtype: list of str
        """
        return self._RejectedBizIds

    @RejectedBizIds.setter
    def RejectedBizIds(self, RejectedBizIds):
        self._RejectedBizIds = RejectedBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._RejectedBizIds = params.get("RejectedBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRejectedQuestionResponse(AbstractModel):
    r"""DeleteRejectedQuestion返回参数结构体

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


class DeleteSharedKnowledgeRequest(AbstractModel):
    r"""DeleteSharedKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        """
        self._KnowledgeBizId = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSharedKnowledgeResponse(AbstractModel):
    r"""DeleteSharedKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBizId = None
        self._RequestId = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

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
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._RequestId = params.get("RequestId")


class DeleteVarRequest(AbstractModel):
    r"""DeleteVar请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _VarId: 变量ID
        :type VarId: str
        :param _VarModuleType: 参数类型
        :type VarModuleType: int
        """
        self._AppBizId = None
        self._VarId = None
        self._VarModuleType = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def VarId(self):
        r"""变量ID
        :rtype: str
        """
        return self._VarId

    @VarId.setter
    def VarId(self, VarId):
        self._VarId = VarId

    @property
    def VarModuleType(self):
        r"""参数类型
        :rtype: int
        """
        return self._VarModuleType

    @VarModuleType.setter
    def VarModuleType(self, VarModuleType):
        self._VarModuleType = VarModuleType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._VarId = params.get("VarId")
        self._VarModuleType = params.get("VarModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVarResponse(AbstractModel):
    r"""DeleteVar返回参数结构体

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


class DescribeAppAgentListRequest(AbstractModel):
    r"""DescribeAppAgentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        """
        self._AppBizId = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppAgentListResponse(AbstractModel):
    r"""DescribeAppAgentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StaringAgentId: 入口启动AgentID
        :type StaringAgentId: str
        :param _Agents: 应用Agent信息列表
        :type Agents: list of Agent
        :param _HandoffAdvancedSetting: Agent转交高级设置
        :type HandoffAdvancedSetting: :class:`tencentcloud.lke.v20231130.models.AgentHandoffAdvancedSetting`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StaringAgentId = None
        self._Agents = None
        self._HandoffAdvancedSetting = None
        self._RequestId = None

    @property
    def StaringAgentId(self):
        r"""入口启动AgentID
        :rtype: str
        """
        return self._StaringAgentId

    @StaringAgentId.setter
    def StaringAgentId(self, StaringAgentId):
        self._StaringAgentId = StaringAgentId

    @property
    def Agents(self):
        r"""应用Agent信息列表
        :rtype: list of Agent
        """
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def HandoffAdvancedSetting(self):
        r"""Agent转交高级设置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentHandoffAdvancedSetting`
        """
        return self._HandoffAdvancedSetting

    @HandoffAdvancedSetting.setter
    def HandoffAdvancedSetting(self, HandoffAdvancedSetting):
        self._HandoffAdvancedSetting = HandoffAdvancedSetting

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
        self._StaringAgentId = params.get("StaringAgentId")
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = Agent()
                obj._deserialize(item)
                self._Agents.append(obj)
        if params.get("HandoffAdvancedSetting") is not None:
            self._HandoffAdvancedSetting = AgentHandoffAdvancedSetting()
            self._HandoffAdvancedSetting._deserialize(params.get("HandoffAdvancedSetting"))
        self._RequestId = params.get("RequestId")


class DescribeAppRequest(AbstractModel):
    r"""DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _IsRelease: 是否发布后的配置
        :type IsRelease: bool
        """
        self._AppBizId = None
        self._AppType = None
        self._IsRelease = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def IsRelease(self):
        r"""是否发布后的配置
        :rtype: bool
        """
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._IsRelease = params.get("IsRelease")
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
        :param _AppBizId: 应用 ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _AppTypeDesc: 应用类型说明
        :type AppTypeDesc: str
        :param _BaseConfig: 应用类型说明
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        :param _AvatarInAppeal: 头像是否在申诉中
        :type AvatarInAppeal: bool
        :param _RoleInAppeal: 角色描述是否在申诉中
        :type RoleInAppeal: bool
        :param _NameInAppeal: 名称是否在申诉中
        :type NameInAppeal: bool
        :param _GreetingInAppeal: 欢迎语是否在申诉中
        :type GreetingInAppeal: bool
        :param _BareAnswerInAppeal: 未知问题回复语是否在申诉中
        :type BareAnswerInAppeal: bool
        :param _AppKey: 应用appKey
        :type AppKey: str
        :param _AppStatus: 应用状态，1：未上线，2：运行中，3：停用
        :type AppStatus: int
        :param _AppStatusDesc: 状态说明
        :type AppStatusDesc: str
        :param _IsCopying: 应用是否在复制中
        :type IsCopying: bool
        :param _AgentType: 智能体类型 dialogue 对话式智能体，wechat 公众号智能体
        :type AgentType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._AppType = None
        self._AppTypeDesc = None
        self._BaseConfig = None
        self._AppConfig = None
        self._AvatarInAppeal = None
        self._RoleInAppeal = None
        self._NameInAppeal = None
        self._GreetingInAppeal = None
        self._BareAnswerInAppeal = None
        self._AppKey = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._IsCopying = None
        self._AgentType = None
        self._RequestId = None

    @property
    def AppBizId(self):
        r"""应用 ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        r"""应用类型说明
        :rtype: str
        """
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def BaseConfig(self):
        r"""应用类型说明
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def AppConfig(self):
        r"""应用配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        """
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

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
    def RoleInAppeal(self):
        r"""角色描述是否在申诉中
        :rtype: bool
        """
        return self._RoleInAppeal

    @RoleInAppeal.setter
    def RoleInAppeal(self, RoleInAppeal):
        self._RoleInAppeal = RoleInAppeal

    @property
    def NameInAppeal(self):
        r"""名称是否在申诉中
        :rtype: bool
        """
        return self._NameInAppeal

    @NameInAppeal.setter
    def NameInAppeal(self, NameInAppeal):
        self._NameInAppeal = NameInAppeal

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
    def BareAnswerInAppeal(self):
        r"""未知问题回复语是否在申诉中
        :rtype: bool
        """
        return self._BareAnswerInAppeal

    @BareAnswerInAppeal.setter
    def BareAnswerInAppeal(self, BareAnswerInAppeal):
        self._BareAnswerInAppeal = BareAnswerInAppeal

    @property
    def AppKey(self):
        r"""应用appKey
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppStatus(self):
        r"""应用状态，1：未上线，2：运行中，3：停用
        :rtype: int
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        r"""状态说明
        :rtype: str
        """
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

    @property
    def IsCopying(self):
        r"""应用是否在复制中
        :rtype: bool
        """
        return self._IsCopying

    @IsCopying.setter
    def IsCopying(self, IsCopying):
        self._IsCopying = IsCopying

    @property
    def AgentType(self):
        r"""智能体类型 dialogue 对话式智能体，wechat 公众号智能体
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

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
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        self._AvatarInAppeal = params.get("AvatarInAppeal")
        self._RoleInAppeal = params.get("RoleInAppeal")
        self._NameInAppeal = params.get("NameInAppeal")
        self._GreetingInAppeal = params.get("GreetingInAppeal")
        self._BareAnswerInAppeal = params.get("BareAnswerInAppeal")
        self._AppKey = params.get("AppKey")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._IsCopying = params.get("IsCopying")
        self._AgentType = params.get("AgentType")
        self._RequestId = params.get("RequestId")


class DescribeAttributeLabelRequest(AbstractModel):
    r"""DescribeAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _AttributeBizId: 标签ID
        :type AttributeBizId: str
        :param _Limit: 每次请求返回的最大标签数量​，限制单次接口返回的标签数量，避免数据量过大。取值范围：大于0。

        :type Limit: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 搜索关键词，用于查询标签标准词或相似词
        :type Query: str
        :param _LastLabelBizId: 滚动加载游标，上一次请求返回的最后一个标签ID
        :type LastLabelBizId: str
        :param _QueryScope: 查询范围 all(或者传空):标准词和相似词 standard:标准词 similar:相似词
        :type QueryScope: str
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._Limit = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._LastLabelBizId = None
        self._QueryScope = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        r"""标签ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def Limit(self):
        r"""每次请求返回的最大标签数量​，限制单次接口返回的标签数量，避免数据量过大。取值范围：大于0。

        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        r"""搜索关键词，用于查询标签标准词或相似词
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LastLabelBizId(self):
        r"""滚动加载游标，上一次请求返回的最后一个标签ID
        :rtype: str
        """
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId

    @property
    def QueryScope(self):
        r"""查询范围 all(或者传空):标准词和相似词 standard:标准词 similar:相似词
        :rtype: str
        """
        return self._QueryScope

    @QueryScope.setter
    def QueryScope(self, QueryScope):
        self._QueryScope = QueryScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._Limit = params.get("Limit")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._LastLabelBizId = params.get("LastLabelBizId")
        self._QueryScope = params.get("QueryScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttributeLabelResponse(AbstractModel):
    r"""DescribeAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _AttrKey: 属性标识
        :type AttrKey: str
        :param _AttrName: 属性名称
        :type AttrName: str
        :param _LabelNumber: 标签数量
        :type LabelNumber: str
        :param _Labels: 标签名称
        :type Labels: list of AttributeLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttributeBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNumber = None
        self._Labels = None
        self._RequestId = None

    @property
    def AttributeBizId(self):
        r"""属性ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrKey(self):
        r"""属性标识
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        r"""属性名称
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNumber(self):
        r"""标签数量
        :rtype: str
        """
        return self._LabelNumber

    @LabelNumber.setter
    def LabelNumber(self, LabelNumber):
        self._LabelNumber = LabelNumber

    @property
    def Labels(self):
        r"""标签名称
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

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
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNumber = params.get("LabelNumber")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallStatsGraphRequest(AbstractModel):
    r"""DescribeCallStatsGraph请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UinAccount: uin
        :type UinAccount: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _SubBizType: 子业务类型
        :type SubBizType: str
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(废弃)
        :type EndTime: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _SubScenes: 筛选子场景(文档解析场景使用)
        :type SubScenes: list of str
        :param _AppType: 应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :type AppType: str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SubScenes = None
        self._AppType = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def UinAccount(self):
        r"""uin
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        r"""子业务类型
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SubScenes(self):
        r"""筛选子场景(文档解析场景使用)
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes

    @property
    def AppType(self):
        r"""应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SubScenes = params.get("SubScenes")
        self._AppType = params.get("AppType")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallStatsGraphResponse(AbstractModel):
    r"""DescribeCallStatsGraph返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 接口调用次数统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Stat
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""接口调用次数统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Stat
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Stat()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConcurrencyUsageGraphRequest(AbstractModel):
    r"""DescribeConcurrencyUsageGraph请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(废弃)
        :type EndTime: str
        :param _UinAccount: uin
        :type UinAccount: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _SubBizType: 子业务类型
        :type SubBizType: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._AppBizIds = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UinAccount(self):
        r"""uin
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        r"""子业务类型
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._AppBizIds = params.get("AppBizIds")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrencyUsageGraphResponse(AbstractModel):
    r"""DescribeConcurrencyUsageGraph返回参数结构体

    """

    def __init__(self):
        r"""
        :param _X: X轴: 时间区域；根据查询条件的粒度返回“分/小时/日”两种区间范围
        :type X: list of str
        :param _AvailableY: 可用并发y轴坐标
        :type AvailableY: list of int
        :param _SuccessCallY: 成功调用并发y轴坐标
        :type SuccessCallY: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._X = None
        self._AvailableY = None
        self._SuccessCallY = None
        self._RequestId = None

    @property
    def X(self):
        r"""X轴: 时间区域；根据查询条件的粒度返回“分/小时/日”两种区间范围
        :rtype: list of str
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def AvailableY(self):
        r"""可用并发y轴坐标
        :rtype: list of int
        """
        return self._AvailableY

    @AvailableY.setter
    def AvailableY(self, AvailableY):
        self._AvailableY = AvailableY

    @property
    def SuccessCallY(self):
        r"""成功调用并发y轴坐标
        :rtype: list of int
        """
        return self._SuccessCallY

    @SuccessCallY.setter
    def SuccessCallY(self, SuccessCallY):
        self._SuccessCallY = SuccessCallY

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
        self._X = params.get("X")
        self._AvailableY = params.get("AvailableY")
        self._SuccessCallY = params.get("SuccessCallY")
        self._RequestId = params.get("RequestId")


class DescribeConcurrencyUsageRequest(AbstractModel):
    r"""DescribeConcurrencyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(废弃)
        :type EndTime: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrencyUsageResponse(AbstractModel):
    r"""DescribeConcurrencyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableConcurrency: 可用并发数上限
        :type AvailableConcurrency: int
        :param _ConcurrencyPeak: 并发峰值
        :type ConcurrencyPeak: int
        :param _ExceedUsageTime: 超出可用并发数上限的次数
        :type ExceedUsageTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableConcurrency = None
        self._ConcurrencyPeak = None
        self._ExceedUsageTime = None
        self._RequestId = None

    @property
    def AvailableConcurrency(self):
        r"""可用并发数上限
        :rtype: int
        """
        return self._AvailableConcurrency

    @AvailableConcurrency.setter
    def AvailableConcurrency(self, AvailableConcurrency):
        self._AvailableConcurrency = AvailableConcurrency

    @property
    def ConcurrencyPeak(self):
        r"""并发峰值
        :rtype: int
        """
        return self._ConcurrencyPeak

    @ConcurrencyPeak.setter
    def ConcurrencyPeak(self, ConcurrencyPeak):
        self._ConcurrencyPeak = ConcurrencyPeak

    @property
    def ExceedUsageTime(self):
        r"""超出可用并发数上限的次数
        :rtype: int
        """
        return self._ExceedUsageTime

    @ExceedUsageTime.setter
    def ExceedUsageTime(self, ExceedUsageTime):
        self._ExceedUsageTime = ExceedUsageTime

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
        self._AvailableConcurrency = params.get("AvailableConcurrency")
        self._ConcurrencyPeak = params.get("ConcurrencyPeak")
        self._ExceedUsageTime = params.get("ExceedUsageTime")
        self._RequestId = params.get("RequestId")


class DescribeDocRequest(AbstractModel):
    r"""DescribeDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocResponse(AbstractModel):
    r"""DescribeDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _CosUrl: cos路径
        :type CosUrl: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 文档状态： 1-未生成 2-生成中 3-生成成功 4-生成失败 5-删除中 6-删除成功 7-审核中 8-审核失败 9-审核成功 10-待发布 11-发布中 12-已发布 13-学习中 14-学习失败 15-更新中 16-更新失败 17-解析中 18-解析失败 19-导入失败 20-已过期 21-超量失效 22-超量失效恢复
        :type Status: int
        :param _StatusDesc: 文档状态描述
        :type StatusDesc: str
        :param _Reason: 生成失败原因
        :type Reason: str
        :param _IsRefer: 答案中是否引用
        :type IsRefer: bool
        :param _QaNum: 问答对数量
        :type QaNum: int
        :param _IsDeleted: 是否删除
        :type IsDeleted: bool
        :param _Source: 文档来源
        :type Source: int
        :param _SourceDesc: 文档来源描述
        :type SourceDesc: str
        :param _IsAllowRestart: 是否允许重新生成
        :type IsAllowRestart: bool
        :param _IsDeletedQa: qa是否已删除
        :type IsDeletedQa: bool
        :param _IsCreatingQa: 问答是否生成中
        :type IsCreatingQa: bool
        :param _IsAllowDelete: 是否允许删除
        :type IsAllowDelete: bool
        :param _IsAllowRefer: 是否允许操作引用开关
        :type IsAllowRefer: bool
        :param _IsCreatedQa: 是否生成过问答
        :type IsCreatedQa: bool
        :param _DocCharSize: 文档字符量
        :type DocCharSize: str
        :param _IsAllowEdit: 是否允许编辑
        :type IsAllowEdit: bool
        :param _AttrRange: 标签适用范围 1：全部，2：按条件范围
        :type AttrRange: int
        :param _AttrLabels: 标签
        :type AttrLabels: list of AttrLabel
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _IsDisabled: 文档是否停用，false:未停用，true:已停用
        :type IsDisabled: bool
        :param _IsDownload: 是否支持下载
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDownload: bool
        :param _SplitRule: 自定义切分规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitRule: str
        :param _UpdatePeriodInfo: 文档更新频率
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatePeriodInfo: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        :param _CateBizIdPath: 从根节点开始的路径分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateBizIdPath: list of str
        :param _CateNamePath: 从根节点开始的路径分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CateNamePath: list of str
        :param _EnableScope: 文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._IsAllowEdit = None
        self._AttrRange = None
        self._AttrLabels = None
        self._CateBizId = None
        self._IsDisabled = None
        self._IsDownload = None
        self._SplitRule = None
        self._UpdatePeriodInfo = None
        self._CateBizIdPath = None
        self._CateNamePath = None
        self._EnableScope = None
        self._RequestId = None

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        r"""文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        r"""cos路径
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""文档状态： 1-未生成 2-生成中 3-生成成功 4-生成失败 5-删除中 6-删除成功 7-审核中 8-审核失败 9-审核成功 10-待发布 11-发布中 12-已发布 13-学习中 14-学习失败 15-更新中 16-更新失败 17-解析中 18-解析失败 19-导入失败 20-已过期 21-超量失效 22-超量失效恢复
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""文档状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        r"""生成失败原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        r"""答案中是否引用
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        r"""问答对数量
        :rtype: int
        """
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        r"""是否删除
        :rtype: bool
        """
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        r"""文档来源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        r"""文档来源描述
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        r"""是否允许重新生成
        :rtype: bool
        """
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        r"""qa是否已删除
        :rtype: bool
        """
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        r"""问答是否生成中
        :rtype: bool
        """
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        r"""是否允许删除
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        r"""是否允许操作引用开关
        :rtype: bool
        """
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        r"""是否生成过问答
        :rtype: bool
        """
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        r"""文档字符量
        :rtype: str
        """
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def IsAllowEdit(self):
        r"""是否允许编辑
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def AttrRange(self):
        r"""标签适用范围 1：全部，2：按条件范围
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""标签
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsDisabled(self):
        r"""文档是否停用，false:未停用，true:已停用
        :rtype: bool
        """
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled

    @property
    def IsDownload(self):
        r"""是否支持下载
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDownload

    @IsDownload.setter
    def IsDownload(self, IsDownload):
        self._IsDownload = IsDownload

    @property
    def SplitRule(self):
        r"""自定义切分规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitRule

    @SplitRule.setter
    def SplitRule(self, SplitRule):
        self._SplitRule = SplitRule

    @property
    def UpdatePeriodInfo(self):
        r"""文档更新频率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        """
        return self._UpdatePeriodInfo

    @UpdatePeriodInfo.setter
    def UpdatePeriodInfo(self, UpdatePeriodInfo):
        self._UpdatePeriodInfo = UpdatePeriodInfo

    @property
    def CateBizIdPath(self):
        r"""从根节点开始的路径分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CateBizIdPath

    @CateBizIdPath.setter
    def CateBizIdPath(self, CateBizIdPath):
        self._CateBizIdPath = CateBizIdPath

    @property
    def CateNamePath(self):
        r"""从根节点开始的路径分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CateNamePath

    @CateNamePath.setter
    def CateNamePath(self, CateNamePath):
        self._CateNamePath = CateNamePath

    @property
    def EnableScope(self):
        r"""文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope

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
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._CateBizId = params.get("CateBizId")
        self._IsDisabled = params.get("IsDisabled")
        self._IsDownload = params.get("IsDownload")
        self._SplitRule = params.get("SplitRule")
        if params.get("UpdatePeriodInfo") is not None:
            self._UpdatePeriodInfo = UpdatePeriodInfo()
            self._UpdatePeriodInfo._deserialize(params.get("UpdatePeriodInfo"))
        self._CateBizIdPath = params.get("CateBizIdPath")
        self._CateNamePath = params.get("CateNamePath")
        self._EnableScope = params.get("EnableScope")
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeUsagePieGraphRequest(AbstractModel):
    r"""DescribeKnowledgeUsagePieGraph请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizIds: 应用ID数组
        :type AppBizIds: list of str
        :param _SpaceId: 空间列表
        :type SpaceId: str
        """
        self._AppBizIds = None
        self._SpaceId = None

    @property
    def AppBizIds(self):
        r"""应用ID数组
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SpaceId(self):
        r"""空间列表
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._AppBizIds = params.get("AppBizIds")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeUsagePieGraphResponse(AbstractModel):
    r"""DescribeKnowledgeUsagePieGraph返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableCharSize: 所有应用已用的字符总数
        :type AvailableCharSize: str
        :param _List: 应用饼图详情列表
        :type List: list of KnowledgeCapacityPieGraphDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableCharSize = None
        self._List = None
        self._RequestId = None

    @property
    def AvailableCharSize(self):
        r"""所有应用已用的字符总数
        :rtype: str
        """
        return self._AvailableCharSize

    @AvailableCharSize.setter
    def AvailableCharSize(self, AvailableCharSize):
        self._AvailableCharSize = AvailableCharSize

    @property
    def List(self):
        r"""应用饼图详情列表
        :rtype: list of KnowledgeCapacityPieGraphDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._AvailableCharSize = params.get("AvailableCharSize")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = KnowledgeCapacityPieGraphDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeUsageRequest(AbstractModel):
    r"""DescribeKnowledgeUsage请求参数结构体

    """


class DescribeKnowledgeUsageResponse(AbstractModel):
    r"""DescribeKnowledgeUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableCharSize: 可用字符数上限
        :type AvailableCharSize: str
        :param _ExceedCharSize: 超过可用字符数上限的字符数
        :type ExceedCharSize: str
        :param _UsedCharSize: 知识库使用字符总数
        :type UsedCharSize: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableCharSize = None
        self._ExceedCharSize = None
        self._UsedCharSize = None
        self._RequestId = None

    @property
    def AvailableCharSize(self):
        r"""可用字符数上限
        :rtype: str
        """
        return self._AvailableCharSize

    @AvailableCharSize.setter
    def AvailableCharSize(self, AvailableCharSize):
        self._AvailableCharSize = AvailableCharSize

    @property
    def ExceedCharSize(self):
        r"""超过可用字符数上限的字符数
        :rtype: str
        """
        return self._ExceedCharSize

    @ExceedCharSize.setter
    def ExceedCharSize(self, ExceedCharSize):
        self._ExceedCharSize = ExceedCharSize

    @property
    def UsedCharSize(self):
        r"""知识库使用字符总数
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

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
        self._AvailableCharSize = params.get("AvailableCharSize")
        self._ExceedCharSize = params.get("ExceedCharSize")
        self._UsedCharSize = params.get("UsedCharSize")
        self._RequestId = params.get("RequestId")


class DescribeNodeRunRequest(AbstractModel):
    r"""DescribeNodeRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _NodeRunId: 节点运行实例ID
        :type NodeRunId: str
        """
        self._AppBizId = None
        self._NodeRunId = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def NodeRunId(self):
        r"""节点运行实例ID
        :rtype: str
        """
        return self._NodeRunId

    @NodeRunId.setter
    def NodeRunId(self, NodeRunId):
        self._NodeRunId = NodeRunId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._NodeRunId = params.get("NodeRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeRunResponse(AbstractModel):
    r"""DescribeNodeRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeRun: 节点运行实例详情
        :type NodeRun: :class:`tencentcloud.lke.v20231130.models.NodeRunDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeRun = None
        self._RequestId = None

    @property
    def NodeRun(self):
        r"""节点运行实例详情
        :rtype: :class:`tencentcloud.lke.v20231130.models.NodeRunDetail`
        """
        return self._NodeRun

    @NodeRun.setter
    def NodeRun(self, NodeRun):
        self._NodeRun = NodeRun

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
        if params.get("NodeRun") is not None:
            self._NodeRun = NodeRunDetail()
            self._NodeRun._deserialize(params.get("NodeRun"))
        self._RequestId = params.get("RequestId")


class DescribeQARequest(AbstractModel):
    r"""DescribeQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: QA业务ID

        :type QaBizId: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._QaBizId = None
        self._BotBizId = None

    @property
    def QaBizId(self):
        r"""QA业务ID

        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQAResponse(AbstractModel):
    r"""DescribeQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: QA业务ID

        :type QaBizId: str
        :param _Question: 问题

        :type Question: str
        :param _Answer: 答案

        :type Answer: str
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _Source: 来源 1-文档生成问答对  2-批量导入问答对  3-单条手动录入问答对
        :type Source: int
        :param _SourceDesc: 来源描述

        :type SourceDesc: str
        :param _UpdateTime: 更新时间

        :type UpdateTime: str
        :param _Status: 状态 <br>1-未校验  2-未发布 3-发布中 4-已发布  5-发布失败 6-不采纳 7-审核中  8-审核失败  9-审核失败申诉后人工审核中  11-审核失败申诉后人工审核不通过  12-已过期  13-超量失效  14-超量失效恢复 19-学习中  20-学习失败
        :type Status: int
        :param _StatusDesc: 状态描述

        :type StatusDesc: str
        :param _CateBizId: 分类ID

        :type CateBizId: str
        :param _IsAllowAccept: 是否允许校验

        :type IsAllowAccept: bool
        :param _IsAllowDelete: 是否允许删除

        :type IsAllowDelete: bool
        :param _IsAllowEdit: 是否允许编辑

        :type IsAllowEdit: bool
        :param _DocBizId: 文档id

        :type DocBizId: str
        :param _FileName: 文档名称

        :type FileName: str
        :param _FileType: 文档类型

        :type FileType: str
        :param _SegmentBizId: 分片ID

        :type SegmentBizId: str
        :param _PageContent: 分片内容
        :type PageContent: str
        :param _Highlights: 分片高亮内容
        :type Highlights: list of Highlight
        :param _OrgData: 分片内容

        :type OrgData: str
        :param _AttrRange: 标签适用范围
        :type AttrRange: int
        :param _AttrLabels: 标签
        :type AttrLabels: list of AttrLabel
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        :param _SimilarQuestions: 相似问列表信息
        :type SimilarQuestions: list of SimilarQuestion
        :param _QaAuditStatus: 问题和答案文本审核状态 1审核失败
        :type QaAuditStatus: int
        :param _PicAuditStatus: 答案中的图片审核状态 1审核失败
        :type PicAuditStatus: int
        :param _VideoAuditStatus: 答案中的视频审核状态 1审核失败
        :type VideoAuditStatus: int
        :param _QuestionDesc: 问题描述
        :type QuestionDesc: str
        :param _IsDisabled: 问答是否停用，false:未停用，true已停用
        :type IsDisabled: bool
        :param _CateBizIdPath: 从根节点开始的路径分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateBizIdPath: list of str
        :param _CateNamePath: 从根节点开始的路径分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CateNamePath: list of str
        :param _EnableScope: 问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableScope: int
        :param _DocEnableScope: 问答关联的文档生效域
        :type DocEnableScope: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._CateBizId = None
        self._IsAllowAccept = None
        self._IsAllowDelete = None
        self._IsAllowEdit = None
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._SegmentBizId = None
        self._PageContent = None
        self._Highlights = None
        self._OrgData = None
        self._AttrRange = None
        self._AttrLabels = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestions = None
        self._QaAuditStatus = None
        self._PicAuditStatus = None
        self._VideoAuditStatus = None
        self._QuestionDesc = None
        self._IsDisabled = None
        self._CateBizIdPath = None
        self._CateNamePath = None
        self._EnableScope = None
        self._DocEnableScope = None
        self._RequestId = None

    @property
    def QaBizId(self):
        r"""QA业务ID

        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

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
    def Answer(self):
        r"""答案

        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        r"""自定义参数
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def Source(self):
        r"""来源 1-文档生成问答对  2-批量导入问答对  3-单条手动录入问答对
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        r"""来源描述

        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        r"""更新时间

        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""状态 <br>1-未校验  2-未发布 3-发布中 4-已发布  5-发布失败 6-不采纳 7-审核中  8-审核失败  9-审核失败申诉后人工审核中  11-审核失败申诉后人工审核不通过  12-已过期  13-超量失效  14-超量失效恢复 19-学习中  20-学习失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述

        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CateBizId(self):
        r"""分类ID

        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsAllowAccept(self):
        r"""是否允许校验

        :rtype: bool
        """
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def IsAllowDelete(self):
        r"""是否允许删除

        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowEdit(self):
        r"""是否允许编辑

        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def DocBizId(self):
        r"""文档id

        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        r"""文档名称

        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文档类型

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SegmentBizId(self):
        r"""分片ID

        :rtype: str
        """
        return self._SegmentBizId

    @SegmentBizId.setter
    def SegmentBizId(self, SegmentBizId):
        self._SegmentBizId = SegmentBizId

    @property
    def PageContent(self):
        r"""分片内容
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Highlights(self):
        r"""分片高亮内容
        :rtype: list of Highlight
        """
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        r"""分片内容

        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def AttrRange(self):
        r"""标签适用范围
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""标签
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ExpireStart(self):
        r"""有效开始时间，unix时间戳
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，unix时间戳，0代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestions(self):
        r"""相似问列表信息
        :rtype: list of SimilarQuestion
        """
        return self._SimilarQuestions

    @SimilarQuestions.setter
    def SimilarQuestions(self, SimilarQuestions):
        self._SimilarQuestions = SimilarQuestions

    @property
    def QaAuditStatus(self):
        r"""问题和答案文本审核状态 1审核失败
        :rtype: int
        """
        return self._QaAuditStatus

    @QaAuditStatus.setter
    def QaAuditStatus(self, QaAuditStatus):
        self._QaAuditStatus = QaAuditStatus

    @property
    def PicAuditStatus(self):
        r"""答案中的图片审核状态 1审核失败
        :rtype: int
        """
        return self._PicAuditStatus

    @PicAuditStatus.setter
    def PicAuditStatus(self, PicAuditStatus):
        self._PicAuditStatus = PicAuditStatus

    @property
    def VideoAuditStatus(self):
        r"""答案中的视频审核状态 1审核失败
        :rtype: int
        """
        return self._VideoAuditStatus

    @VideoAuditStatus.setter
    def VideoAuditStatus(self, VideoAuditStatus):
        self._VideoAuditStatus = VideoAuditStatus

    @property
    def QuestionDesc(self):
        r"""问题描述
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc

    @property
    def IsDisabled(self):
        r"""问答是否停用，false:未停用，true已停用
        :rtype: bool
        """
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled

    @property
    def CateBizIdPath(self):
        r"""从根节点开始的路径分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CateBizIdPath

    @CateBizIdPath.setter
    def CateBizIdPath(self, CateBizIdPath):
        self._CateBizIdPath = CateBizIdPath

    @property
    def CateNamePath(self):
        r"""从根节点开始的路径分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CateNamePath

    @CateNamePath.setter
    def CateNamePath(self, CateNamePath):
        self._CateNamePath = CateNamePath

    @property
    def EnableScope(self):
        r"""问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope

    @property
    def DocEnableScope(self):
        r"""问答关联的文档生效域
        :rtype: int
        """
        return self._DocEnableScope

    @DocEnableScope.setter
    def DocEnableScope(self, DocEnableScope):
        self._DocEnableScope = DocEnableScope

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
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CateBizId = params.get("CateBizId")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._SegmentBizId = params.get("SegmentBizId")
        self._PageContent = params.get("PageContent")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        if params.get("SimilarQuestions") is not None:
            self._SimilarQuestions = []
            for item in params.get("SimilarQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._SimilarQuestions.append(obj)
        self._QaAuditStatus = params.get("QaAuditStatus")
        self._PicAuditStatus = params.get("PicAuditStatus")
        self._VideoAuditStatus = params.get("VideoAuditStatus")
        self._QuestionDesc = params.get("QuestionDesc")
        self._IsDisabled = params.get("IsDisabled")
        self._CateBizIdPath = params.get("CateBizIdPath")
        self._CateNamePath = params.get("CateNamePath")
        self._EnableScope = params.get("EnableScope")
        self._DocEnableScope = params.get("DocEnableScope")
        self._RequestId = params.get("RequestId")


class DescribeReferRequest(AbstractModel):
    r"""DescribeRefer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReferBizIds: 引用ID
        :type ReferBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReferBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReferBizIds(self):
        r"""引用ID
        :rtype: list of str
        """
        return self._ReferBizIds

    @ReferBizIds.setter
    def ReferBizIds(self, ReferBizIds):
        self._ReferBizIds = ReferBizIds

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReferBizIds = params.get("ReferBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReferResponse(AbstractModel):
    r"""DescribeRefer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 引用列表
        :type List: list of ReferDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""引用列表
        :rtype: list of ReferDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReferDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseInfoRequest(AbstractModel):
    r"""DescribeReleaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseInfoResponse(AbstractModel):
    r"""DescribeReleaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LastTime: 最后发布时间
        :type LastTime: str
        :param _Status: 发布状态 ， 1-待发布 , 2-发布中 , 3-发布成功 , 4-发布失败 , 5-审核中 , 6-审核成功 , 7-审核失败 , 8-发布成功回调处理中 , 9-发布暂停 , 10-申诉审核中 , 11-申诉审核通过 , 12-申诉审核不通过
        :type Status: int
        :param _IsUpdated: 是否编辑过, 当为true的时候表示可以发布
        :type IsUpdated: bool
        :param _Msg: 失败原因

        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LastTime = None
        self._Status = None
        self._IsUpdated = None
        self._Msg = None
        self._RequestId = None

    @property
    def LastTime(self):
        r"""最后发布时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def Status(self):
        r"""发布状态 ， 1-待发布 , 2-发布中 , 3-发布成功 , 4-发布失败 , 5-审核中 , 6-审核成功 , 7-审核失败 , 8-发布成功回调处理中 , 9-发布暂停 , 10-申诉审核中 , 11-申诉审核通过 , 12-申诉审核不通过
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsUpdated(self):
        r"""是否编辑过, 当为true的时候表示可以发布
        :rtype: bool
        """
        return self._IsUpdated

    @IsUpdated.setter
    def IsUpdated(self, IsUpdated):
        self._IsUpdated = IsUpdated

    @property
    def Msg(self):
        r"""失败原因

        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._LastTime = params.get("LastTime")
        self._Status = params.get("Status")
        self._IsUpdated = params.get("IsUpdated")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeReleaseRequest(AbstractModel):
    r"""DescribeRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReleaseBizId: 发布详情
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        r"""发布详情
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseResponse(AbstractModel):
    r"""DescribeRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Description: 发布描述
        :type Description: str
        :param _Status: 发布状态(1待发布 2发布中 3发布成功 4发布失败 5发布中(审核中) 6发布中(审核完成) 7发布失败(审核失败) 9发布暂停)
        :type Status: int
        :param _StatusDesc: 发布状态描述
        :type StatusDesc: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreateTime = None
        self._Description = None
        self._Status = None
        self._StatusDesc = None
        self._RequestId = None

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
    def Description(self):
        r"""发布描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""发布状态(1待发布 2发布中 3发布成功 4发布失败 5发布中(审核中) 6发布中(审核完成) 7发布失败(审核失败) 9发布暂停)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""发布状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

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
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._RequestId = params.get("RequestId")


class DescribeRobotBizIDByAppKeyRequest(AbstractModel):
    r"""DescribeRobotBizIDByAppKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppKey: 应用appkey
        :type AppKey: str
        """
        self._AppKey = None

    @property
    def AppKey(self):
        r"""应用appkey
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey


    def _deserialize(self, params):
        self._AppKey = params.get("AppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRobotBizIDByAppKeyResponse(AbstractModel):
    r"""DescribeRobotBizIDByAppKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用业务ID
        :type BotBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BotBizId = None
        self._RequestId = None

    @property
    def BotBizId(self):
        r"""应用业务ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

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
        self._BotBizId = params.get("BotBizId")
        self._RequestId = params.get("RequestId")


class DescribeSearchStatsGraphRequest(AbstractModel):
    r"""DescribeSearchStatsGraph请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _UinAccount: uin列表
        :type UinAccount: list of str
        :param _SubBizType: 子业务类型
        :type SubBizType: str
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(废弃)
        :type EndTime: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._UinAccount = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def UinAccount(self):
        r"""uin列表
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def SubBizType(self):
        r"""子业务类型
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._UinAccount = params.get("UinAccount")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchStatsGraphResponse(AbstractModel):
    r"""DescribeSearchStatsGraph返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Stat
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Stat
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Stat()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSegmentsRequest(AbstractModel):
    r"""DescribeSegments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _SegBizId: 文档片段ID
        :type SegBizId: list of str
        """
        self._BotBizId = None
        self._SegBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def SegBizId(self):
        r"""文档片段ID
        :rtype: list of str
        """
        return self._SegBizId

    @SegBizId.setter
    def SegBizId(self, SegBizId):
        self._SegBizId = SegBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._SegBizId = params.get("SegBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSegmentsResponse(AbstractModel):
    r"""DescribeSegments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 片段列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DocSegment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""片段列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DocSegment
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DocSegment()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSharedKnowledgeRequest(AbstractModel):
    r"""DescribeSharedKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        """
        self._KnowledgeBizId = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSharedKnowledgeResponse(AbstractModel):
    r"""DescribeSharedKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 知识库详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: :class:`tencentcloud.lke.v20231130.models.KnowledgeDetailInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""知识库详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeDetailInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = KnowledgeDetailInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStorageCredentialRequest(AbstractModel):
    r"""DescribeStorageCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，参数非必填不代表不需要填写，下面不同的参数组合会获取到不同的权限，具体请参考 https://cloud.tencent.com/document/product/1759/116238
        :type BotBizId: str
        :param _FileType: 文件类型,正常的文件名类型后缀，例如 xlsx、pdf、 docx、png 等
        :type FileType: str
        :param _IsPublic: IsPublic用于上传文件或图片时选择场景，当上传对话端图片时IsPublic为true，上传文件（包括文档库文件/图片等和对话端文件）时IsPublic为false

        :type IsPublic: bool
        :param _TypeKey: 存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :type TypeKey: str
        """
        self._BotBizId = None
        self._FileType = None
        self._IsPublic = None
        self._TypeKey = None

    @property
    def BotBizId(self):
        r"""应用ID，参数非必填不代表不需要填写，下面不同的参数组合会获取到不同的权限，具体请参考 https://cloud.tencent.com/document/product/1759/116238
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileType(self):
        r"""文件类型,正常的文件名类型后缀，例如 xlsx、pdf、 docx、png 等
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IsPublic(self):
        r"""IsPublic用于上传文件或图片时选择场景，当上传对话端图片时IsPublic为true，上传文件（包括文档库文件/图片等和对话端文件）时IsPublic为false

        :rtype: bool
        """
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TypeKey(self):
        r"""存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileType = params.get("FileType")
        self._IsPublic = params.get("IsPublic")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageCredentialResponse(AbstractModel):
    r"""DescribeStorageCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 密钥信息
        :type Credentials: :class:`tencentcloud.lke.v20231130.models.Credentials`
        :param _ExpiredTime: 失效时间
        :type ExpiredTime: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Bucket: 对象存储桶
        :type Bucket: str
        :param _Region: 对象存储可用区
        :type Region: str
        :param _FilePath: 文件存储目录
        :type FilePath: str
        :param _Type: 存储类型
        :type Type: str
        :param _CorpUin: 主号
        :type CorpUin: str
        :param _ImagePath: 图片存储目录
        :type ImagePath: str
        :param _UploadPath: 上传存储路径，到具体文件
        :type UploadPath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._StartTime = None
        self._Bucket = None
        self._Region = None
        self._FilePath = None
        self._Type = None
        self._CorpUin = None
        self._ImagePath = None
        self._UploadPath = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""密钥信息
        :rtype: :class:`tencentcloud.lke.v20231130.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        r"""失效时间
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Bucket(self):
        r"""对象存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""对象存储可用区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FilePath(self):
        r"""文件存储目录
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        r"""存储类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CorpUin(self):
        r"""主号
        :rtype: str
        """
        return self._CorpUin

    @CorpUin.setter
    def CorpUin(self, CorpUin):
        self._CorpUin = CorpUin

    @property
    def ImagePath(self):
        r"""图片存储目录
        :rtype: str
        """
        return self._ImagePath

    @ImagePath.setter
    def ImagePath(self, ImagePath):
        self._ImagePath = ImagePath

    @property
    def UploadPath(self):
        r"""上传存储路径，到具体文件
        :rtype: str
        """
        return self._UploadPath

    @UploadPath.setter
    def UploadPath(self, UploadPath):
        self._UploadPath = UploadPath

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
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._StartTime = params.get("StartTime")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._FilePath = params.get("FilePath")
        self._Type = params.get("Type")
        self._CorpUin = params.get("CorpUin")
        self._ImagePath = params.get("ImagePath")
        self._UploadPath = params.get("UploadPath")
        self._RequestId = params.get("RequestId")


class DescribeTokenUsageGraphRequest(AbstractModel):
    r"""DescribeTokenUsageGraph请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UinAccount: 腾讯云主账号
        :type UinAccount: list of str
        :param _SubBizType: 知识引擎子业务类型:  FileParse(文档解析)、Embedding、Rewrite(多轮改写)、 Concurrency(并发)、KnowledgeSummary(知识总结)   KnowledgeQA(知识问答)、KnowledgeCapacity(知识库容量)、SearchEngine(搜索引擎)
        :type SubBizType: str
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(废弃)
        :type EndTime: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _AppType: 应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :type AppType: str
        :param _SubScenes: 筛选子场景
        :type SubScenes: list of str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._UinAccount = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._AppType = None
        self._SubScenes = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def UinAccount(self):
        r"""腾讯云主账号
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def SubBizType(self):
        r"""知识引擎子业务类型:  FileParse(文档解析)、Embedding、Rewrite(多轮改写)、 Concurrency(并发)、KnowledgeSummary(知识总结)   KnowledgeQA(知识问答)、KnowledgeCapacity(知识库容量)、SearchEngine(搜索引擎)
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def AppType(self):
        r"""应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def SubScenes(self):
        r"""筛选子场景
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes

    @property
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._AppType = params.get("AppType")
        self._SubScenes = params.get("SubScenes")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenUsageGraphResponse(AbstractModel):
    r"""DescribeTokenUsageGraph返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: Token消耗总量
        :type Total: list of Stat
        :param _Input: 输入Token消耗量
        :type Input: list of Stat
        :param _Output: 输出Token消耗量
        :type Output: list of Stat
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Input = None
        self._Output = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Token消耗总量
        :rtype: list of Stat
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Input(self):
        r"""输入Token消耗量
        :rtype: list of Stat
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""输出Token消耗量
        :rtype: list of Stat
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

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
        if params.get("Total") is not None:
            self._Total = []
            for item in params.get("Total"):
                obj = Stat()
                obj._deserialize(item)
                self._Total.append(obj)
        if params.get("Input") is not None:
            self._Input = []
            for item in params.get("Input"):
                obj = Stat()
                obj._deserialize(item)
                self._Input.append(obj)
        if params.get("Output") is not None:
            self._Output = []
            for item in params.get("Output"):
                obj = Stat()
                obj._deserialize(item)
                self._Output.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTokenUsageRequest(AbstractModel):
    r"""DescribeTokenUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UinAccount: 腾讯云主账号
        :type UinAccount: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _SubBizType: 知识引擎子业务类型:  FileParse(文档解析)、Embedding、Rewrite(多轮改写)、 Concurrency(并发)、KnowledgeSummary(知识总结)   KnowledgeQA(知识问答)、KnowledgeCapacity(知识库容量)、SearchEngine(搜索引擎)
        :type SubBizType: str
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _StartTime: 开始时间戳, 单位为秒(默认值0)(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间戳, 单位为秒(默认值0， 必须大于开始时间戳)(废弃)
        :type EndTime: str
        :param _AppBizIds: 应用id列表
        :type AppBizIds: list of str
        :param _SubScenes: 筛选子场景(文档解析场景使用)
        :type SubScenes: list of str
        :param _AppType: 应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :type AppType: str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 结束时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SubScenes = None
        self._AppType = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def UinAccount(self):
        r"""腾讯云主账号
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        r"""知识引擎子业务类型:  FileParse(文档解析)、Embedding、Rewrite(多轮改写)、 Concurrency(并发)、KnowledgeSummary(知识总结)   KnowledgeQA(知识问答)、KnowledgeCapacity(知识库容量)、SearchEngine(搜索引擎)
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        r"""开始时间戳, 单位为秒(默认值0)(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳, 单位为秒(默认值0， 必须大于开始时间戳)(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        r"""应用id列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SubScenes(self):
        r"""筛选子场景(文档解析场景使用)
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes

    @property
    def AppType(self):
        r"""应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""结束时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SubScenes = params.get("SubScenes")
        self._AppType = params.get("AppType")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenUsageResponse(AbstractModel):
    r"""DescribeTokenUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalTokenUsage: 总token消耗量
        :type TotalTokenUsage: float
        :param _InputTokenUsage: 输入token消耗
        :type InputTokenUsage: float
        :param _OutputTokenUsage: 输出token消耗
        :type OutputTokenUsage: float
        :param _ApiCallStats: 接口调用次数
        :type ApiCallStats: int
        :param _SearchUsage: 搜索服务调用次数
        :type SearchUsage: float
        :param _PageUsage: 文档解析消耗页数
        :type PageUsage: int
        :param _SplitTokenUsage: 拆分token消耗量
        :type SplitTokenUsage: float
        :param _RagSearchUsage: Rag检索次数
        :type RagSearchUsage: float
        :param _InternetSearchUsage: 联网搜索次数
        :type InternetSearchUsage: float
        :param _DosageTypeLimit: dosage配额限制
        :type DosageTypeLimit: float
        :param _DosageTypeCurr: dosage当前用量	
        :type DosageTypeCurr: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalTokenUsage = None
        self._InputTokenUsage = None
        self._OutputTokenUsage = None
        self._ApiCallStats = None
        self._SearchUsage = None
        self._PageUsage = None
        self._SplitTokenUsage = None
        self._RagSearchUsage = None
        self._InternetSearchUsage = None
        self._DosageTypeLimit = None
        self._DosageTypeCurr = None
        self._RequestId = None

    @property
    def TotalTokenUsage(self):
        r"""总token消耗量
        :rtype: float
        """
        return self._TotalTokenUsage

    @TotalTokenUsage.setter
    def TotalTokenUsage(self, TotalTokenUsage):
        self._TotalTokenUsage = TotalTokenUsage

    @property
    def InputTokenUsage(self):
        r"""输入token消耗
        :rtype: float
        """
        return self._InputTokenUsage

    @InputTokenUsage.setter
    def InputTokenUsage(self, InputTokenUsage):
        self._InputTokenUsage = InputTokenUsage

    @property
    def OutputTokenUsage(self):
        r"""输出token消耗
        :rtype: float
        """
        return self._OutputTokenUsage

    @OutputTokenUsage.setter
    def OutputTokenUsage(self, OutputTokenUsage):
        self._OutputTokenUsage = OutputTokenUsage

    @property
    def ApiCallStats(self):
        r"""接口调用次数
        :rtype: int
        """
        return self._ApiCallStats

    @ApiCallStats.setter
    def ApiCallStats(self, ApiCallStats):
        self._ApiCallStats = ApiCallStats

    @property
    def SearchUsage(self):
        r"""搜索服务调用次数
        :rtype: float
        """
        return self._SearchUsage

    @SearchUsage.setter
    def SearchUsage(self, SearchUsage):
        self._SearchUsage = SearchUsage

    @property
    def PageUsage(self):
        r"""文档解析消耗页数
        :rtype: int
        """
        return self._PageUsage

    @PageUsage.setter
    def PageUsage(self, PageUsage):
        self._PageUsage = PageUsage

    @property
    def SplitTokenUsage(self):
        r"""拆分token消耗量
        :rtype: float
        """
        return self._SplitTokenUsage

    @SplitTokenUsage.setter
    def SplitTokenUsage(self, SplitTokenUsage):
        self._SplitTokenUsage = SplitTokenUsage

    @property
    def RagSearchUsage(self):
        r"""Rag检索次数
        :rtype: float
        """
        return self._RagSearchUsage

    @RagSearchUsage.setter
    def RagSearchUsage(self, RagSearchUsage):
        self._RagSearchUsage = RagSearchUsage

    @property
    def InternetSearchUsage(self):
        r"""联网搜索次数
        :rtype: float
        """
        return self._InternetSearchUsage

    @InternetSearchUsage.setter
    def InternetSearchUsage(self, InternetSearchUsage):
        self._InternetSearchUsage = InternetSearchUsage

    @property
    def DosageTypeLimit(self):
        r"""dosage配额限制
        :rtype: float
        """
        return self._DosageTypeLimit

    @DosageTypeLimit.setter
    def DosageTypeLimit(self, DosageTypeLimit):
        self._DosageTypeLimit = DosageTypeLimit

    @property
    def DosageTypeCurr(self):
        r"""dosage当前用量	
        :rtype: float
        """
        return self._DosageTypeCurr

    @DosageTypeCurr.setter
    def DosageTypeCurr(self, DosageTypeCurr):
        self._DosageTypeCurr = DosageTypeCurr

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
        self._TotalTokenUsage = params.get("TotalTokenUsage")
        self._InputTokenUsage = params.get("InputTokenUsage")
        self._OutputTokenUsage = params.get("OutputTokenUsage")
        self._ApiCallStats = params.get("ApiCallStats")
        self._SearchUsage = params.get("SearchUsage")
        self._PageUsage = params.get("PageUsage")
        self._SplitTokenUsage = params.get("SplitTokenUsage")
        self._RagSearchUsage = params.get("RagSearchUsage")
        self._InternetSearchUsage = params.get("InternetSearchUsage")
        self._DosageTypeLimit = params.get("DosageTypeLimit")
        self._DosageTypeCurr = params.get("DosageTypeCurr")
        self._RequestId = params.get("RequestId")


class DescribeUnsatisfiedReplyContextRequest(AbstractModel):
    r"""DescribeUnsatisfiedReplyContext请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _ReplyBizId: 回复ID，调用这个接口获得：[ListUnsatisfiedReply](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListUnsatisfiedReply) 
        :type ReplyBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizId(self):
        r"""回复ID，调用这个接口获得：[ListUnsatisfiedReply](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListUnsatisfiedReply) 
        :rtype: str
        """
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizId = params.get("ReplyBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnsatisfiedReplyContextResponse(AbstractModel):
    r"""DescribeUnsatisfiedReplyContext返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 不满意回复上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Context
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""不满意回复上下文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Context
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Context()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkflowRunRequest(AbstractModel):
    r"""DescribeWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID, 获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :type AppBizId: str
        :param _WorkflowRunId: 工作流运行实例ID
        :type WorkflowRunId: str
        :param _SubWorkflowNodePath: 指定的子工作流对应的NodePath。
格式：`[<node_id>[<index>].]*<node_id>[<index>]`
- 此路径用于定位一个具体的工作流实例（Workflow Run），可以是主工作流实例或某个子工作流节点产生的子实例。
- 路径由点号（.）分隔的节点标识符组成，每个节点标识符格式为 `节点ID[实例索引]`。
- **节点ID (node_id)**：子工作流所属的节点的ID。
- **实例索引 (index)**：“实例索引” 在工作流节点的时候为空，循环、批处理节点非空，从1开始。
示例：
- "" 或 不设置 -> 查询主工作流实例 (父工作流)
- "node_id_a" -> 查询由主工作流中工作流节点`node_id_a`对应的子工作流实例
- "node_id_a.node_id_b[1]" -> 查询工作流节点`node_id_a`对应的子工作流的循环节点node_id_b的第1轮循环的子工作流运行状态
        :type SubWorkflowNodePath: str
        :param _IncludeWorkflowGraph: 是否需要返回工作流的流程图配置
        :type IncludeWorkflowGraph: bool
        """
        self._AppBizId = None
        self._WorkflowRunId = None
        self._SubWorkflowNodePath = None
        self._IncludeWorkflowGraph = None

    @property
    def AppBizId(self):
        r"""应用ID, 获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def SubWorkflowNodePath(self):
        r"""指定的子工作流对应的NodePath。
格式：`[<node_id>[<index>].]*<node_id>[<index>]`
- 此路径用于定位一个具体的工作流实例（Workflow Run），可以是主工作流实例或某个子工作流节点产生的子实例。
- 路径由点号（.）分隔的节点标识符组成，每个节点标识符格式为 `节点ID[实例索引]`。
- **节点ID (node_id)**：子工作流所属的节点的ID。
- **实例索引 (index)**：“实例索引” 在工作流节点的时候为空，循环、批处理节点非空，从1开始。
示例：
- "" 或 不设置 -> 查询主工作流实例 (父工作流)
- "node_id_a" -> 查询由主工作流中工作流节点`node_id_a`对应的子工作流实例
- "node_id_a.node_id_b[1]" -> 查询工作流节点`node_id_a`对应的子工作流的循环节点node_id_b的第1轮循环的子工作流运行状态
        :rtype: str
        """
        return self._SubWorkflowNodePath

    @SubWorkflowNodePath.setter
    def SubWorkflowNodePath(self, SubWorkflowNodePath):
        self._SubWorkflowNodePath = SubWorkflowNodePath

    @property
    def IncludeWorkflowGraph(self):
        r"""是否需要返回工作流的流程图配置
        :rtype: bool
        """
        return self._IncludeWorkflowGraph

    @IncludeWorkflowGraph.setter
    def IncludeWorkflowGraph(self, IncludeWorkflowGraph):
        self._IncludeWorkflowGraph = IncludeWorkflowGraph


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._SubWorkflowNodePath = params.get("SubWorkflowNodePath")
        self._IncludeWorkflowGraph = params.get("IncludeWorkflowGraph")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkflowRunResponse(AbstractModel):
    r"""DescribeWorkflowRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkflowRun: 工作流运行实例详情
        :type WorkflowRun: :class:`tencentcloud.lke.v20231130.models.WorkflowRunDetail`
        :param _NodeRuns: 节点列表
        :type NodeRuns: list of NodeRunBase
        :param _SubWorkflowNodePath: 子工作流对应的NodePath
        :type SubWorkflowNodePath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkflowRun = None
        self._NodeRuns = None
        self._SubWorkflowNodePath = None
        self._RequestId = None

    @property
    def WorkflowRun(self):
        r"""工作流运行实例详情
        :rtype: :class:`tencentcloud.lke.v20231130.models.WorkflowRunDetail`
        """
        return self._WorkflowRun

    @WorkflowRun.setter
    def WorkflowRun(self, WorkflowRun):
        self._WorkflowRun = WorkflowRun

    @property
    def NodeRuns(self):
        r"""节点列表
        :rtype: list of NodeRunBase
        """
        return self._NodeRuns

    @NodeRuns.setter
    def NodeRuns(self, NodeRuns):
        self._NodeRuns = NodeRuns

    @property
    def SubWorkflowNodePath(self):
        r"""子工作流对应的NodePath
        :rtype: str
        """
        return self._SubWorkflowNodePath

    @SubWorkflowNodePath.setter
    def SubWorkflowNodePath(self, SubWorkflowNodePath):
        self._SubWorkflowNodePath = SubWorkflowNodePath

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
        if params.get("WorkflowRun") is not None:
            self._WorkflowRun = WorkflowRunDetail()
            self._WorkflowRun._deserialize(params.get("WorkflowRun"))
        if params.get("NodeRuns") is not None:
            self._NodeRuns = []
            for item in params.get("NodeRuns"):
                obj = NodeRunBase()
                obj._deserialize(item)
                self._NodeRuns.append(obj)
        self._SubWorkflowNodePath = params.get("SubWorkflowNodePath")
        self._RequestId = params.get("RequestId")


class DigitalHumanConfig(AbstractModel):
    r"""数智人配置

    """

    def __init__(self):
        r"""
        :param _AssetKey: 数智人资产key
        :type AssetKey: str
        :param _Name: 数智人名称
        :type Name: str
        :param _Avatar: 图像
        :type Avatar: str
        :param _PreviewUrl: 预览图
        :type PreviewUrl: str
        """
        self._AssetKey = None
        self._Name = None
        self._Avatar = None
        self._PreviewUrl = None

    @property
    def AssetKey(self):
        r"""数智人资产key
        :rtype: str
        """
        return self._AssetKey

    @AssetKey.setter
    def AssetKey(self, AssetKey):
        self._AssetKey = AssetKey

    @property
    def Name(self):
        r"""数智人名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        r"""图像
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def PreviewUrl(self):
        r"""预览图
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl


    def _deserialize(self, params):
        self._AssetKey = params.get("AssetKey")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._PreviewUrl = params.get("PreviewUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocFilterFlag(AbstractModel):
    r"""文档列表筛选标识位

    """

    def __init__(self):
        r"""
        :param _Flag: 标识位
        :type Flag: str
        :param _Value: 标识值
        :type Value: bool
        """
        self._Flag = None
        self._Value = None

    @property
    def Flag(self):
        r"""标识位
        :rtype: str
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Value(self):
        r"""标识值
        :rtype: bool
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Flag = params.get("Flag")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocSegment(AbstractModel):
    r"""文档片段

    """

    def __init__(self):
        r"""
        :param _Id: 片段ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _BusinessId: 业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _FileType: 文件类型(markdown,word,txt)
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _SegmentType: 文档切片类型(segment-文档切片 table-表格)
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentType: str
        :param _Title: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _PageContent: 段落内容
注意：此字段可能返回 null，表示取不到有效值。
        :type PageContent: str
        :param _OrgData: 段落原文
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgData: str
        :param _DocId: 文章ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        :param _DocBizId: 文档业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocBizId: str
        :param _DocUrl: 文档链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DocUrl: str
        :param _WebUrl: 文档的自定义链接
        :type WebUrl: str
        :param _PageInfos: 页码信息
        :type PageInfos: list of int non-negative
        """
        self._Id = None
        self._BusinessId = None
        self._FileType = None
        self._SegmentType = None
        self._Title = None
        self._PageContent = None
        self._OrgData = None
        self._DocId = None
        self._DocBizId = None
        self._DocUrl = None
        self._WebUrl = None
        self._PageInfos = None

    @property
    def Id(self):
        r"""片段ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BusinessId(self):
        r"""业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileType(self):
        r"""文件类型(markdown,word,txt)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SegmentType(self):
        r"""文档切片类型(segment-文档切片 table-表格)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SegmentType

    @SegmentType.setter
    def SegmentType(self, SegmentType):
        self._SegmentType = SegmentType

    @property
    def Title(self):
        r"""标题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def PageContent(self):
        r"""段落内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def OrgData(self):
        r"""段落原文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def DocId(self):
        r"""文章ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def DocBizId(self):
        r"""文档业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def DocUrl(self):
        r"""文档链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl

    @property
    def WebUrl(self):
        r"""文档的自定义链接
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def PageInfos(self):
        r"""页码信息
        :rtype: list of int non-negative
        """
        return self._PageInfos

    @PageInfos.setter
    def PageInfos(self, PageInfos):
        self._PageInfos = PageInfos


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BusinessId = params.get("BusinessId")
        self._FileType = params.get("FileType")
        self._SegmentType = params.get("SegmentType")
        self._Title = params.get("Title")
        self._PageContent = params.get("PageContent")
        self._OrgData = params.get("OrgData")
        self._DocId = params.get("DocId")
        self._DocBizId = params.get("DocBizId")
        self._DocUrl = params.get("DocUrl")
        self._WebUrl = params.get("WebUrl")
        self._PageInfos = params.get("PageInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateFileHandle(AbstractModel):
    r"""重复文档处理方式

    """

    def __init__(self):
        r"""
        :param _CheckType: 重复文档判断方式，1：按文档内容，即cos_hash字段判断是否重复
        :type CheckType: int
        :param _HandleType: 重复文档处理方式，1：返回报错，2：跳过，返回重复的文档业务ID
        :type HandleType: int
        """
        self._CheckType = None
        self._HandleType = None

    @property
    def CheckType(self):
        r"""重复文档判断方式，1：按文档内容，即cos_hash字段判断是否重复
        :rtype: int
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def HandleType(self):
        r"""重复文档处理方式，1：返回报错，2：跳过，返回重复的文档业务ID
        :rtype: int
        """
        return self._HandleType

    @HandleType.setter
    def HandleType(self, HandleType):
        self._HandleType = HandleType


    def _deserialize(self, params):
        self._CheckType = params.get("CheckType")
        self._HandleType = params.get("HandleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelRequest(AbstractModel):
    r"""ExportAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _AttributeBizIds: 标签ID
        :type AttributeBizIds: list of str
        :param _Filters: 根据筛选数据导出
        :type Filters: :class:`tencentcloud.lke.v20231130.models.AttributeFilters`
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttributeBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttributeBizIds(self):
        r"""标签ID
        :rtype: list of str
        """
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def Filters(self):
        r"""根据筛选数据导出
        :rtype: :class:`tencentcloud.lke.v20231130.models.AttributeFilters`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._AttributeBizIds = params.get("AttributeBizIds")
        if params.get("Filters") is not None:
            self._Filters = AttributeFilters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelResponse(AbstractModel):
    r"""ExportAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 导出任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""导出任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportQAListRequest(AbstractModel):
    r"""ExportQAList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: QA业务ID
        :type QaBizIds: list of str
        :param _Filters: 查询参数
        :type Filters: :class:`tencentcloud.lke.v20231130.models.QAQuery`
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        r"""QA业务ID
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def Filters(self):
        r"""查询参数
        :rtype: :class:`tencentcloud.lke.v20231130.models.QAQuery`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        if params.get("Filters") is not None:
            self._Filters = QAQuery()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportQAListResponse(AbstractModel):
    r"""ExportQAList返回参数结构体

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


class ExportUnsatisfiedReplyRequest(AbstractModel):
    r"""ExportUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReplyBizIds: 勾选导出ID列表
        :type ReplyBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Filters: 检索过滤器
        :type Filters: :class:`tencentcloud.lke.v20231130.models.Filters`
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Filters = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        r"""勾选导出ID列表
        :rtype: list of str
        """
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Filters(self):
        r"""检索过滤器
        :rtype: :class:`tencentcloud.lke.v20231130.models.Filters`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("Filters") is not None:
            self._Filters = Filters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportUnsatisfiedReplyResponse(AbstractModel):
    r"""ExportUnsatisfiedReply返回参数结构体

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


class ExtraInfo(AbstractModel):
    r"""扩展信息

    """

    def __init__(self):
        r"""
        :param _EChartsInfo: ECharts信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EChartsInfo: list of str
        """
        self._EChartsInfo = None

    @property
    def EChartsInfo(self):
        r"""ECharts信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._EChartsInfo

    @EChartsInfo.setter
    def EChartsInfo(self, EChartsInfo):
        self._EChartsInfo = EChartsInfo


    def _deserialize(self, params):
        self._EChartsInfo = params.get("EChartsInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    r"""实时上传的文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _FileUrl: 文件的URL地址，COS地址
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _DocId: 解析后返回的DocID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None
        self._CreatedAt = None

    @property
    def FileName(self):
        r"""文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        r"""文件的URL地址，COS地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        r"""文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        r"""解析后返回的DocID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def CreatedAt(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    r"""不满意回复检索过滤

    """

    def __init__(self):
        r"""
        :param _Query: 检索，用户问题或答案
        :type Query: str
        :param _Reasons: 错误类型检索

        :type Reasons: list of str
        :param _HandlingStatuses: 处理状态 0-待处理 1-已拒答 2-已忽略 3-已添加为新问答 4-已添加为相似问
        :type HandlingStatuses: list of int non-negative
        """
        self._Query = None
        self._Reasons = None
        self._HandlingStatuses = None

    @property
    def Query(self):
        r"""检索，用户问题或答案
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        r"""错误类型检索

        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def HandlingStatuses(self):
        r"""处理状态 0-待处理 1-已拒答 2-已忽略 3-已添加为新问答 4-已添加为相似问
        :rtype: list of int non-negative
        """
        return self._HandlingStatuses

    @HandlingStatuses.setter
    def HandlingStatuses(self, HandlingStatuses):
        self._HandlingStatuses = HandlingStatuses


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        self._HandlingStatuses = params.get("HandlingStatuses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQARequest(AbstractModel):
    r"""GenerateQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _DocBizIds: 文档ID
        :type DocBizIds: list of str
        """
        self._BotBizId = None
        self._DocBizIds = None

    @property
    def BotBizId(self):
        r"""应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        r"""文档ID
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQAResponse(AbstractModel):
    r"""GenerateQA返回参数结构体

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


class GetAnswerTypeDataCountRequest(AbstractModel):
    r"""GetAnswerTypeDataCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始日期
        :type StartTime: int
        :param _EndTime: 结束日期
        :type EndTime: int
        :param _AppBizId: 应用id
        :type AppBizId: list of str
        :param _Type: 消息来源(1、分享用户端  2、对话API  3、对话测试  4、应用评测)
        :type Type: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        r"""开始日期
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束日期
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        r"""应用id
        :rtype: list of str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        r"""消息来源(1、分享用户端  2、对话API  3、对话测试  4、应用评测)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAnswerTypeDataCountResponse(AbstractModel):
    r"""GetAnswerTypeDataCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总消息数
        :type Total: int
        :param _ModelReplyCount: 大模型直接回复总数
        :type ModelReplyCount: int
        :param _KnowledgeCount: 知识型回复总数
        :type KnowledgeCount: int
        :param _TaskFlowCount: 任务流回复总数
        :type TaskFlowCount: int
        :param _SearchEngineCount: 搜索引擎回复总数
        :type SearchEngineCount: int
        :param _ImageUnderstandingCount: 图片理解回复总数
        :type ImageUnderstandingCount: int
        :param _RejectCount: 拒答回复总数
        :type RejectCount: int
        :param _SensitiveCount: 敏感回复总数
        :type SensitiveCount: int
        :param _ConcurrentLimitCount: 并发超限回复总数
        :type ConcurrentLimitCount: int
        :param _UnknownIssuesCount: 未知问题回复总数
        :type UnknownIssuesCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ModelReplyCount = None
        self._KnowledgeCount = None
        self._TaskFlowCount = None
        self._SearchEngineCount = None
        self._ImageUnderstandingCount = None
        self._RejectCount = None
        self._SensitiveCount = None
        self._ConcurrentLimitCount = None
        self._UnknownIssuesCount = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总消息数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ModelReplyCount(self):
        r"""大模型直接回复总数
        :rtype: int
        """
        return self._ModelReplyCount

    @ModelReplyCount.setter
    def ModelReplyCount(self, ModelReplyCount):
        self._ModelReplyCount = ModelReplyCount

    @property
    def KnowledgeCount(self):
        r"""知识型回复总数
        :rtype: int
        """
        return self._KnowledgeCount

    @KnowledgeCount.setter
    def KnowledgeCount(self, KnowledgeCount):
        self._KnowledgeCount = KnowledgeCount

    @property
    def TaskFlowCount(self):
        r"""任务流回复总数
        :rtype: int
        """
        return self._TaskFlowCount

    @TaskFlowCount.setter
    def TaskFlowCount(self, TaskFlowCount):
        self._TaskFlowCount = TaskFlowCount

    @property
    def SearchEngineCount(self):
        r"""搜索引擎回复总数
        :rtype: int
        """
        return self._SearchEngineCount

    @SearchEngineCount.setter
    def SearchEngineCount(self, SearchEngineCount):
        self._SearchEngineCount = SearchEngineCount

    @property
    def ImageUnderstandingCount(self):
        r"""图片理解回复总数
        :rtype: int
        """
        return self._ImageUnderstandingCount

    @ImageUnderstandingCount.setter
    def ImageUnderstandingCount(self, ImageUnderstandingCount):
        self._ImageUnderstandingCount = ImageUnderstandingCount

    @property
    def RejectCount(self):
        r"""拒答回复总数
        :rtype: int
        """
        return self._RejectCount

    @RejectCount.setter
    def RejectCount(self, RejectCount):
        self._RejectCount = RejectCount

    @property
    def SensitiveCount(self):
        r"""敏感回复总数
        :rtype: int
        """
        return self._SensitiveCount

    @SensitiveCount.setter
    def SensitiveCount(self, SensitiveCount):
        self._SensitiveCount = SensitiveCount

    @property
    def ConcurrentLimitCount(self):
        r"""并发超限回复总数
        :rtype: int
        """
        return self._ConcurrentLimitCount

    @ConcurrentLimitCount.setter
    def ConcurrentLimitCount(self, ConcurrentLimitCount):
        self._ConcurrentLimitCount = ConcurrentLimitCount

    @property
    def UnknownIssuesCount(self):
        r"""未知问题回复总数
        :rtype: int
        """
        return self._UnknownIssuesCount

    @UnknownIssuesCount.setter
    def UnknownIssuesCount(self, UnknownIssuesCount):
        self._UnknownIssuesCount = UnknownIssuesCount

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
        self._ModelReplyCount = params.get("ModelReplyCount")
        self._KnowledgeCount = params.get("KnowledgeCount")
        self._TaskFlowCount = params.get("TaskFlowCount")
        self._SearchEngineCount = params.get("SearchEngineCount")
        self._ImageUnderstandingCount = params.get("ImageUnderstandingCount")
        self._RejectCount = params.get("RejectCount")
        self._SensitiveCount = params.get("SensitiveCount")
        self._ConcurrentLimitCount = params.get("ConcurrentLimitCount")
        self._UnknownIssuesCount = params.get("UnknownIssuesCount")
        self._RequestId = params.get("RequestId")


class GetAppKnowledgeCountRequest(AbstractModel):
    r"""GetAppKnowledgeCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 类型：doc-文档；qa-问答对
        :type Type: str
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)	
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._Type = None
        self._AppBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def Type(self):
        r"""类型：doc-文档；qa-问答对
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppBizId = params.get("AppBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppKnowledgeCountResponse(AbstractModel):
    r"""GetAppKnowledgeCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._RequestId = params.get("RequestId")


class GetAppSecretRequest(AbstractModel):
    r"""GetAppSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        """
        self._AppBizId = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppSecretResponse(AbstractModel):
    r"""GetAppSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppKey: 应用密钥
        :type AppKey: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsRelease: 是否发布
        :type IsRelease: bool
        :param _HasPermission: 是否有查看权限
        :type HasPermission: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppKey = None
        self._CreateTime = None
        self._IsRelease = None
        self._HasPermission = None
        self._RequestId = None

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

    @property
    def IsRelease(self):
        r"""是否发布
        :rtype: bool
        """
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease

    @property
    def HasPermission(self):
        r"""是否有查看权限
        :rtype: bool
        """
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

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
        self._AppKey = params.get("AppKey")
        self._CreateTime = params.get("CreateTime")
        self._IsRelease = params.get("IsRelease")
        self._HasPermission = params.get("HasPermission")
        self._RequestId = params.get("RequestId")


class GetDocPreviewRequest(AbstractModel):
    r"""GetDocPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档BizID
        :type DocBizId: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _TypeKey: 存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :type TypeKey: str
        """
        self._DocBizId = None
        self._BotBizId = None
        self._TypeKey = None

    @property
    def DocBizId(self):
        r"""文档BizID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def TypeKey(self):
        r"""存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._BotBizId = params.get("BotBizId")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocPreviewResponse(AbstractModel):
    r"""GetDocPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名, 发布端固定使用这个名称
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _CosUrl: cos路径

        :type CosUrl: str
        :param _Url: cos临时地址

        :type Url: str
        :param _Bucket: cos桶

        :type Bucket: str
        :param _NewName: 存在文档重命名情况下的新名称, 评测端优先使用这个名称
        :type NewName: str
        :param _ParseResultCosUrl: 文件md结果cos临时地址
        :type ParseResultCosUrl: str
        :param _IsDownload: 是否可下载
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDownload: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._Url = None
        self._Bucket = None
        self._NewName = None
        self._ParseResultCosUrl = None
        self._IsDownload = None
        self._RequestId = None

    @property
    def FileName(self):
        r"""文件名, 发布端固定使用这个名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        r"""cos路径

        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def Url(self):
        r"""cos临时地址

        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Bucket(self):
        r"""cos桶

        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def NewName(self):
        r"""存在文档重命名情况下的新名称, 评测端优先使用这个名称
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def ParseResultCosUrl(self):
        r"""文件md结果cos临时地址
        :rtype: str
        """
        return self._ParseResultCosUrl

    @ParseResultCosUrl.setter
    def ParseResultCosUrl(self, ParseResultCosUrl):
        self._ParseResultCosUrl = ParseResultCosUrl

    @property
    def IsDownload(self):
        r"""是否可下载
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDownload

    @IsDownload.setter
    def IsDownload(self, IsDownload):
        self._IsDownload = IsDownload

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
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._Url = params.get("Url")
        self._Bucket = params.get("Bucket")
        self._NewName = params.get("NewName")
        self._ParseResultCosUrl = params.get("ParseResultCosUrl")
        self._IsDownload = params.get("IsDownload")
        self._RequestId = params.get("RequestId")


class GetLikeDataCountRequest(AbstractModel):
    r"""GetLikeDataCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始日期
        :type StartTime: int
        :param _EndTime: 结束日期
        :type EndTime: int
        :param _AppBizId: 应用id
        :type AppBizId: list of str
        :param _Type: 消息来源(1、分享用户端  2、对话API)
        :type Type: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        r"""开始日期
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束日期
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        r"""应用id
        :rtype: list of str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        r"""消息来源(1、分享用户端  2、对话API)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLikeDataCountResponse(AbstractModel):
    r"""GetLikeDataCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 可评价消息数
        :type Total: int
        :param _AppraisalTotal: 评价数
        :type AppraisalTotal: int
        :param _ParticipationRate: 参评率
        :type ParticipationRate: float
        :param _LikeTotal: 点赞数
        :type LikeTotal: int
        :param _LikeRate: 点赞率
        :type LikeRate: float
        :param _DislikeTotal: 点踩数
        :type DislikeTotal: int
        :param _DislikeRate: 点踩率
        :type DislikeRate: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AppraisalTotal = None
        self._ParticipationRate = None
        self._LikeTotal = None
        self._LikeRate = None
        self._DislikeTotal = None
        self._DislikeRate = None
        self._RequestId = None

    @property
    def Total(self):
        r"""可评价消息数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AppraisalTotal(self):
        r"""评价数
        :rtype: int
        """
        return self._AppraisalTotal

    @AppraisalTotal.setter
    def AppraisalTotal(self, AppraisalTotal):
        self._AppraisalTotal = AppraisalTotal

    @property
    def ParticipationRate(self):
        r"""参评率
        :rtype: float
        """
        return self._ParticipationRate

    @ParticipationRate.setter
    def ParticipationRate(self, ParticipationRate):
        self._ParticipationRate = ParticipationRate

    @property
    def LikeTotal(self):
        r"""点赞数
        :rtype: int
        """
        return self._LikeTotal

    @LikeTotal.setter
    def LikeTotal(self, LikeTotal):
        self._LikeTotal = LikeTotal

    @property
    def LikeRate(self):
        r"""点赞率
        :rtype: float
        """
        return self._LikeRate

    @LikeRate.setter
    def LikeRate(self, LikeRate):
        self._LikeRate = LikeRate

    @property
    def DislikeTotal(self):
        r"""点踩数
        :rtype: int
        """
        return self._DislikeTotal

    @DislikeTotal.setter
    def DislikeTotal(self, DislikeTotal):
        self._DislikeTotal = DislikeTotal

    @property
    def DislikeRate(self):
        r"""点踩率
        :rtype: float
        """
        return self._DislikeRate

    @DislikeRate.setter
    def DislikeRate(self, DislikeRate):
        self._DislikeRate = DislikeRate

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
        self._AppraisalTotal = params.get("AppraisalTotal")
        self._ParticipationRate = params.get("ParticipationRate")
        self._LikeTotal = params.get("LikeTotal")
        self._LikeRate = params.get("LikeRate")
        self._DislikeTotal = params.get("DislikeTotal")
        self._DislikeRate = params.get("DislikeRate")
        self._RequestId = params.get("RequestId")


class GetMsgRecordRequest(AbstractModel):
    r"""GetMsgRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: int
        :param _Count: 数量,  数量需大于2, 最大1000
        :type Count: int
        :param _SessionId: 会话sessionid
        :type SessionId: str
        :param _BotAppKey: 应用AppKey, 当Type=5[API访客]时, 该字段必填  :</br>  获取方式:</br>   1、应用发布后在应用页面[发布管理]-[调用信息]-[API管理]处获取</br>   2、参考 https://cloud.tencent.com/document/product/1759/109469 第二项
        :type BotAppKey: str
        :param _Scene: 场景, 体验: 1; 正式: 2
        :type Scene: int
        :param _LastRecordId: 最后一条记录ID， 消息从后往前获取

MidRecordId与LastRecordId只能选择一个

        :type LastRecordId: str
        :param _MidRecordId: 传该值，代表拉取该记录id的前后总共count条消息记录

MidRecordId与LastRecordId只能选择一个

        :type MidRecordId: str
        """
        self._Type = None
        self._Count = None
        self._SessionId = None
        self._BotAppKey = None
        self._Scene = None
        self._LastRecordId = None
        self._MidRecordId = None

    @property
    def Type(self):
        r"""类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""数量,  数量需大于2, 最大1000
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SessionId(self):
        r"""会话sessionid
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def BotAppKey(self):
        r"""应用AppKey, 当Type=5[API访客]时, 该字段必填  :</br>  获取方式:</br>   1、应用发布后在应用页面[发布管理]-[调用信息]-[API管理]处获取</br>   2、参考 https://cloud.tencent.com/document/product/1759/109469 第二项
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def Scene(self):
        r"""场景, 体验: 1; 正式: 2
        :rtype: int
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LastRecordId(self):
        r"""最后一条记录ID， 消息从后往前获取

MidRecordId与LastRecordId只能选择一个

        :rtype: str
        """
        return self._LastRecordId

    @LastRecordId.setter
    def LastRecordId(self, LastRecordId):
        self._LastRecordId = LastRecordId

    @property
    def MidRecordId(self):
        r"""传该值，代表拉取该记录id的前后总共count条消息记录

MidRecordId与LastRecordId只能选择一个

        :rtype: str
        """
        return self._MidRecordId

    @MidRecordId.setter
    def MidRecordId(self, MidRecordId):
        self._MidRecordId = MidRecordId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._SessionId = params.get("SessionId")
        self._BotAppKey = params.get("BotAppKey")
        self._Scene = params.get("Scene")
        self._LastRecordId = params.get("LastRecordId")
        self._MidRecordId = params.get("MidRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMsgRecordResponse(AbstractModel):
    r"""GetMsgRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 会话记录
        :type Records: list of MsgRecord
        :param _SessionDisassociatedTimestamp: session 清除关联上下文时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionDisassociatedTimestamp: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._SessionDisassociatedTimestamp = None
        self._RequestId = None

    @property
    def Records(self):
        r"""会话记录
        :rtype: list of MsgRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def SessionDisassociatedTimestamp(self):
        r"""session 清除关联上下文时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionDisassociatedTimestamp

    @SessionDisassociatedTimestamp.setter
    def SessionDisassociatedTimestamp(self, SessionDisassociatedTimestamp):
        self._SessionDisassociatedTimestamp = SessionDisassociatedTimestamp

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = MsgRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._SessionDisassociatedTimestamp = params.get("SessionDisassociatedTimestamp")
        self._RequestId = params.get("RequestId")


class GetTaskStatusRequest(AbstractModel):
    r"""GetTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._BotBizId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStatusResponse(AbstractModel):
    r"""GetTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Message: 任务消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Params: 任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: :class:`tencentcloud.lke.v20231130.models.TaskParams`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._Status = None
        self._Message = None
        self._Params = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        r"""任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        r"""任务消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Params(self):
        r"""任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskParams`
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

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
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        if params.get("Params") is not None:
            self._Params = TaskParams()
            self._Params._deserialize(params.get("Params"))
        self._RequestId = params.get("RequestId")


class GetVarListRequest(AbstractModel):
    r"""GetVarList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _VarIds: 变量ID数组
        :type VarIds: list of str
        :param _Keyword: 按变量名称关键词搜索
        :type Keyword: str
        :param _Offset: 起始偏移量（默认0）
        :type Offset: int
        :param _Limit: 限定数量（默认15）
        :type Limit: int
        :param _VarType: 按变量类型过滤，默认查询所有类型(STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO)
        :type VarType: str
        :param _NeedInternalVar: 是否需要内部变量(默认false)
        :type NeedInternalVar: bool
        :param _VarModuleType: 变量类型
        :type VarModuleType: int
        """
        self._AppBizId = None
        self._VarIds = None
        self._Keyword = None
        self._Offset = None
        self._Limit = None
        self._VarType = None
        self._NeedInternalVar = None
        self._VarModuleType = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def VarIds(self):
        r"""变量ID数组
        :rtype: list of str
        """
        return self._VarIds

    @VarIds.setter
    def VarIds(self, VarIds):
        self._VarIds = VarIds

    @property
    def Keyword(self):
        r"""按变量名称关键词搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Offset(self):
        r"""起始偏移量（默认0）
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限定数量（默认15）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def VarType(self):
        r"""按变量类型过滤，默认查询所有类型(STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO)
        :rtype: str
        """
        return self._VarType

    @VarType.setter
    def VarType(self, VarType):
        self._VarType = VarType

    @property
    def NeedInternalVar(self):
        r"""是否需要内部变量(默认false)
        :rtype: bool
        """
        return self._NeedInternalVar

    @NeedInternalVar.setter
    def NeedInternalVar(self, NeedInternalVar):
        self._NeedInternalVar = NeedInternalVar

    @property
    def VarModuleType(self):
        r"""变量类型
        :rtype: int
        """
        return self._VarModuleType

    @VarModuleType.setter
    def VarModuleType(self, VarModuleType):
        self._VarModuleType = VarModuleType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._VarIds = params.get("VarIds")
        self._Keyword = params.get("Keyword")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VarType = params.get("VarType")
        self._NeedInternalVar = params.get("NeedInternalVar")
        self._VarModuleType = params.get("VarModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVarListResponse(AbstractModel):
    r"""GetVarList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 变量总数
        :type Total: int
        :param _List: 变量信息列表
        :type List: list of TaskFLowVar
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""变量总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""变量信息列表
        :rtype: list of TaskFLowVar
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TaskFLowVar()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class GetWsTokenReq_Label(AbstractModel):
    r"""获取ws token label

    """

    def __init__(self):
        r"""
        :param _Name: 标签名
        :type Name: str
        :param _Values: 标签值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""标签名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""标签值
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
        


class GetWsTokenRequest(AbstractModel):
    r"""GetWsToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 接入类型， 5-API 访客，目前仅支持传5
        :type Type: int
        :param _BotAppKey:   应用AppKey </br>   获取方式:</br>   1、应用发布后在应用页面[发布管理]-[调用信息]-[API管理]处获取</br>   2、参考 https://cloud.tencent.com/document/product/1759/109469 第二项
        :type BotAppKey: str
        :param _VisitorBizId: 访客ID（外部输入，建议唯一，标识当前接入会话的用户）
长度限制： string(64)
        :type VisitorBizId: str
        :param _VisitorLabels: 知识标签，用于知识库中知识的检索过滤。该字段即将下线，请使用对话端接口中的 custom_variables 字段替代该字段。
        :type VisitorLabels: list of GetWsTokenReq_Label
        """
        self._Type = None
        self._BotAppKey = None
        self._VisitorBizId = None
        self._VisitorLabels = None

    @property
    def Type(self):
        r"""接入类型， 5-API 访客，目前仅支持传5
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BotAppKey(self):
        r"""  应用AppKey </br>   获取方式:</br>   1、应用发布后在应用页面[发布管理]-[调用信息]-[API管理]处获取</br>   2、参考 https://cloud.tencent.com/document/product/1759/109469 第二项
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def VisitorBizId(self):
        r"""访客ID（外部输入，建议唯一，标识当前接入会话的用户）
长度限制： string(64)
        :rtype: str
        """
        return self._VisitorBizId

    @VisitorBizId.setter
    def VisitorBizId(self, VisitorBizId):
        self._VisitorBizId = VisitorBizId

    @property
    def VisitorLabels(self):
        r"""知识标签，用于知识库中知识的检索过滤。该字段即将下线，请使用对话端接口中的 custom_variables 字段替代该字段。
        :rtype: list of GetWsTokenReq_Label
        """
        return self._VisitorLabels

    @VisitorLabels.setter
    def VisitorLabels(self, VisitorLabels):
        self._VisitorLabels = VisitorLabels


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._BotAppKey = params.get("BotAppKey")
        self._VisitorBizId = params.get("VisitorBizId")
        if params.get("VisitorLabels") is not None:
            self._VisitorLabels = []
            for item in params.get("VisitorLabels"):
                obj = GetWsTokenReq_Label()
                obj._deserialize(item)
                self._VisitorLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWsTokenResponse(AbstractModel):
    r"""GetWsToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: token值（有效期60s，仅一次有效，多次校验会报错）
        :type Token: str
        :param _Balance: 余额; 余额大于 0 时表示有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Balance: float
        :param _InputLenLimit: 对话窗输入字符限制
        :type InputLenLimit: int
        :param _Pattern: 应用模式，standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :type Pattern: str
        :param _SingleWorkflow: SingleWorkflow
        :type SingleWorkflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        :param _VisionModelInputLimit: 使用视觉模型时对话窗口输入字符限制
注意：此字段可能返回 null，表示取不到有效值。
        :type VisionModelInputLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._Balance = None
        self._InputLenLimit = None
        self._Pattern = None
        self._SingleWorkflow = None
        self._VisionModelInputLimit = None
        self._RequestId = None

    @property
    def Token(self):
        r"""token值（有效期60s，仅一次有效，多次校验会报错）
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Balance(self):
        r"""余额; 余额大于 0 时表示有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def InputLenLimit(self):
        r"""对话窗输入字符限制
        :rtype: int
        """
        return self._InputLenLimit

    @InputLenLimit.setter
    def InputLenLimit(self, InputLenLimit):
        self._InputLenLimit = InputLenLimit

    @property
    def Pattern(self):
        r"""应用模式，standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def SingleWorkflow(self):
        r"""SingleWorkflow
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        """
        return self._SingleWorkflow

    @SingleWorkflow.setter
    def SingleWorkflow(self, SingleWorkflow):
        self._SingleWorkflow = SingleWorkflow

    @property
    def VisionModelInputLimit(self):
        r"""使用视觉模型时对话窗口输入字符限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VisionModelInputLimit

    @VisionModelInputLimit.setter
    def VisionModelInputLimit(self, VisionModelInputLimit):
        self._VisionModelInputLimit = VisionModelInputLimit

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
        self._Token = params.get("Token")
        self._Balance = params.get("Balance")
        self._InputLenLimit = params.get("InputLenLimit")
        self._Pattern = params.get("Pattern")
        if params.get("SingleWorkflow") is not None:
            self._SingleWorkflow = KnowledgeQaSingleWorkflow()
            self._SingleWorkflow._deserialize(params.get("SingleWorkflow"))
        self._VisionModelInputLimit = params.get("VisionModelInputLimit")
        self._RequestId = params.get("RequestId")


class GroupDocRequest(AbstractModel):
    r"""GroupDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _BizIds: 操作对象的业务ID列表
        :type BizIds: list of str
        :param _CateBizId: 分组 ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._BizIds = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def BizIds(self):
        r"""操作对象的业务ID列表
        :rtype: list of str
        """
        return self._BizIds

    @BizIds.setter
    def BizIds(self, BizIds):
        self._BizIds = BizIds

    @property
    def CateBizId(self):
        r"""分组 ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._BizIds = params.get("BizIds")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupDocResponse(AbstractModel):
    r"""GroupDoc返回参数结构体

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


class GroupQARequest(AbstractModel):
    r"""GroupQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: QaBizID列表
        :type QaBizIds: list of str
        :param _CateBizId: 分组 ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        r"""QaBizID列表
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def CateBizId(self):
        r"""分组 ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupQAResponse(AbstractModel):
    r"""GroupQA返回参数结构体

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


class Highlight(AbstractModel):
    r"""分片高亮内容

    """

    def __init__(self):
        r"""
        :param _StartPos: 高亮起始位置

注意：此字段可能返回 null，表示取不到有效值。
        :type StartPos: str
        :param _EndPos: 高亮结束位置

注意：此字段可能返回 null，表示取不到有效值。
        :type EndPos: str
        :param _Text: 高亮子文本

注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self._StartPos = None
        self._EndPos = None
        self._Text = None

    @property
    def StartPos(self):
        r"""高亮起始位置

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartPos

    @StartPos.setter
    def StartPos(self, StartPos):
        self._StartPos = StartPos

    @property
    def EndPos(self):
        r"""高亮结束位置

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndPos

    @EndPos.setter
    def EndPos(self, EndPos):
        self._EndPos = EndPos

    @property
    def Text(self):
        r"""高亮子文本

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._StartPos = params.get("StartPos")
        self._EndPos = params.get("EndPos")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistorySummary(AbstractModel):
    r"""多轮历史信息

    """

    def __init__(self):
        r"""
        :param _Assistant: 助手
注意：此字段可能返回 null，表示取不到有效值。
        :type Assistant: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        """
        self._Assistant = None
        self._User = None

    @property
    def Assistant(self):
        r"""助手
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Assistant

    @Assistant.setter
    def Assistant(self, Assistant):
        self._Assistant = Assistant

    @property
    def User(self):
        r"""用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._Assistant = params.get("Assistant")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyRequest(AbstractModel):
    r"""IgnoreUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReplyBizIds: 不满意回复ID
        :type ReplyBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        r"""不满意回复ID
        :rtype: list of str
        """
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyResponse(AbstractModel):
    r"""IgnoreUnsatisfiedReply返回参数结构体

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


class InputBoxConfig(AbstractModel):
    r"""输入框配置

    """

    def __init__(self):
        r"""
        :param _InputBoxButtons: 输入框按钮，1：上传图片、2：上传文档，3：腾讯文档，4：联网搜索
        :type InputBoxButtons: list of int non-negative
        """
        self._InputBoxButtons = None

    @property
    def InputBoxButtons(self):
        r"""输入框按钮，1：上传图片、2：上传文档，3：腾讯文档，4：联网搜索
        :rtype: list of int non-negative
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
        


class IntentAchievement(AbstractModel):
    r"""意图达成方式

    """

    def __init__(self):
        r"""
        :param _Name: 意图达成方式，qa:问答回复、doc：文档回复、workflow：工作流回复，llm：大模型回复
        :type Name: str
        :param _Desc: 意图达成方式描述
        :type Desc: str
        """
        self._Name = None
        self._Desc = None

    @property
    def Name(self):
        r"""意图达成方式，qa:问答回复、doc：文档回复、workflow：工作流回复，llm：大模型回复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""意图达成方式描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeAPI(AbstractModel):
    r"""请求的API信息

    """

    def __init__(self):
        r"""
        :param _Method: 请求方法，如GET/POST等
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Url: 请求地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _HeaderValues: header参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderValues: list of StrValue
        :param _QueryValues: 入参Query
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryValues: list of StrValue
        :param _RequestPostBody: Post请求的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestPostBody: str
        :param _ResponseBody: 返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseBody: str
        :param _ResponseValues: 出参
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseValues: list of ValueInfo
        :param _FailMessage: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMessage: str
        """
        self._Method = None
        self._Url = None
        self._HeaderValues = None
        self._QueryValues = None
        self._RequestPostBody = None
        self._ResponseBody = None
        self._ResponseValues = None
        self._FailMessage = None

    @property
    def Method(self):
        r"""请求方法，如GET/POST等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Url(self):
        r"""请求地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def HeaderValues(self):
        r"""header参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StrValue
        """
        return self._HeaderValues

    @HeaderValues.setter
    def HeaderValues(self, HeaderValues):
        self._HeaderValues = HeaderValues

    @property
    def QueryValues(self):
        r"""入参Query
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StrValue
        """
        return self._QueryValues

    @QueryValues.setter
    def QueryValues(self, QueryValues):
        self._QueryValues = QueryValues

    @property
    def RequestPostBody(self):
        r"""Post请求的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestPostBody

    @RequestPostBody.setter
    def RequestPostBody(self, RequestPostBody):
        self._RequestPostBody = RequestPostBody

    @property
    def ResponseBody(self):
        r"""返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResponseBody

    @ResponseBody.setter
    def ResponseBody(self, ResponseBody):
        self._ResponseBody = ResponseBody

    @property
    def ResponseValues(self):
        r"""出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ValueInfo
        """
        return self._ResponseValues

    @ResponseValues.setter
    def ResponseValues(self, ResponseValues):
        self._ResponseValues = ResponseValues

    @property
    def FailMessage(self):
        r"""异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Url = params.get("Url")
        if params.get("HeaderValues") is not None:
            self._HeaderValues = []
            for item in params.get("HeaderValues"):
                obj = StrValue()
                obj._deserialize(item)
                self._HeaderValues.append(obj)
        if params.get("QueryValues") is not None:
            self._QueryValues = []
            for item in params.get("QueryValues"):
                obj = StrValue()
                obj._deserialize(item)
                self._QueryValues.append(obj)
        self._RequestPostBody = params.get("RequestPostBody")
        self._ResponseBody = params.get("ResponseBody")
        if params.get("ResponseValues") is not None:
            self._ResponseValues = []
            for item in params.get("ResponseValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._ResponseValues.append(obj)
        self._FailMessage = params.get("FailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsTransferIntentRequest(AbstractModel):
    r"""IsTransferIntent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _BotAppKey: 应用appKey
        :type BotAppKey: str
        """
        self._Content = None
        self._BotAppKey = None

    @property
    def Content(self):
        r"""内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def BotAppKey(self):
        r"""应用appKey
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._BotAppKey = params.get("BotAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsTransferIntentResponse(AbstractModel):
    r"""IsTransferIntent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Hit: 是否意图转人工
        :type Hit: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Hit = None
        self._RequestId = None

    @property
    def Hit(self):
        r"""是否意图转人工
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

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
        self._Hit = params.get("Hit")
        self._RequestId = params.get("RequestId")


class KnowledgeAdvancedConfig(AbstractModel):
    r"""知识库高级设置

    """

    def __init__(self):
        r"""
        :param _RerankModel: 重排序模型
注意：此字段可能返回 null，表示取不到有效值。
        :type RerankModel: str
        :param _RerankRecallNum: 召回数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RerankRecallNum: int
        """
        self._RerankModel = None
        self._RerankRecallNum = None

    @property
    def RerankModel(self):
        r"""重排序模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RerankModel

    @RerankModel.setter
    def RerankModel(self, RerankModel):
        self._RerankModel = RerankModel

    @property
    def RerankRecallNum(self):
        r"""召回数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RerankRecallNum

    @RerankRecallNum.setter
    def RerankRecallNum(self, RerankRecallNum):
        self._RerankRecallNum = RerankRecallNum


    def _deserialize(self, params):
        self._RerankModel = params.get("RerankModel")
        self._RerankRecallNum = params.get("RerankRecallNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeBaseInfo(AbstractModel):
    r"""共享知识库基础信息

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        :param _KnowledgeName: 共享知识库名称
        :type KnowledgeName: str
        :param _KnowledgeDescription: 共享知识库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeDescription: str
        :param _EmbeddingModel: Embedding模型
注意：此字段可能返回 null，表示取不到有效值。
        :type EmbeddingModel: str
        :param _QaExtractModel: 问答提取模型
注意：此字段可能返回 null，表示取不到有效值。
        :type QaExtractModel: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _KnowledgeType: 共享知识库类型，0普通，1公众号
        :type KnowledgeType: int
        :param _OwnerStaffId: 拥有者id
        :type OwnerStaffId: str
        :param _DocTotal: 知识库文档数量,当前仅支持公众号知识库
注意：此字段可能返回 null，表示取不到有效值。
        :type DocTotal: int
        :param _ProcessingFlags: 知识库处理中状态标记，1：向量embedding变更中
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessingFlags: list of int
        :param _OwnerStaffName: 知识库拥有者的名字
        :type OwnerStaffName: str
        """
        self._KnowledgeBizId = None
        self._KnowledgeName = None
        self._KnowledgeDescription = None
        self._EmbeddingModel = None
        self._QaExtractModel = None
        self._UpdateTime = None
        self._KnowledgeType = None
        self._OwnerStaffId = None
        self._DocTotal = None
        self._ProcessingFlags = None
        self._OwnerStaffName = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def KnowledgeName(self):
        r"""共享知识库名称
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName

    @property
    def KnowledgeDescription(self):
        r"""共享知识库描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeDescription

    @KnowledgeDescription.setter
    def KnowledgeDescription(self, KnowledgeDescription):
        self._KnowledgeDescription = KnowledgeDescription

    @property
    def EmbeddingModel(self):
        r"""Embedding模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EmbeddingModel

    @EmbeddingModel.setter
    def EmbeddingModel(self, EmbeddingModel):
        self._EmbeddingModel = EmbeddingModel

    @property
    def QaExtractModel(self):
        r"""问答提取模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QaExtractModel

    @QaExtractModel.setter
    def QaExtractModel(self, QaExtractModel):
        self._QaExtractModel = QaExtractModel

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
    def KnowledgeType(self):
        r"""共享知识库类型，0普通，1公众号
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType

    @property
    def OwnerStaffId(self):
        r"""拥有者id
        :rtype: str
        """
        return self._OwnerStaffId

    @OwnerStaffId.setter
    def OwnerStaffId(self, OwnerStaffId):
        self._OwnerStaffId = OwnerStaffId

    @property
    def DocTotal(self):
        r"""知识库文档数量,当前仅支持公众号知识库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DocTotal

    @DocTotal.setter
    def DocTotal(self, DocTotal):
        self._DocTotal = DocTotal

    @property
    def ProcessingFlags(self):
        r"""知识库处理中状态标记，1：向量embedding变更中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._ProcessingFlags

    @ProcessingFlags.setter
    def ProcessingFlags(self, ProcessingFlags):
        self._ProcessingFlags = ProcessingFlags

    @property
    def OwnerStaffName(self):
        r"""知识库拥有者的名字
        :rtype: str
        """
        return self._OwnerStaffName

    @OwnerStaffName.setter
    def OwnerStaffName(self, OwnerStaffName):
        self._OwnerStaffName = OwnerStaffName


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._KnowledgeName = params.get("KnowledgeName")
        self._KnowledgeDescription = params.get("KnowledgeDescription")
        self._EmbeddingModel = params.get("EmbeddingModel")
        self._QaExtractModel = params.get("QaExtractModel")
        self._UpdateTime = params.get("UpdateTime")
        self._KnowledgeType = params.get("KnowledgeType")
        self._OwnerStaffId = params.get("OwnerStaffId")
        self._DocTotal = params.get("DocTotal")
        self._ProcessingFlags = params.get("ProcessingFlags")
        self._OwnerStaffName = params.get("OwnerStaffName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeCapacityPieGraphDetail(AbstractModel):
    r"""知识库容量饼图详情

    """

    def __init__(self):
        r"""
        :param _AppName: 当前应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _UsedCharSize: 当前应用使用的字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCharSize: str
        :param _Proportion: 当前应用对于总用量的占比
注意：此字段可能返回 null，表示取不到有效值。
        :type Proportion: float
        :param _KnowledgeType: 知识库类型:0默认1共享
        :type KnowledgeType: int
        """
        self._AppName = None
        self._UsedCharSize = None
        self._Proportion = None
        self._KnowledgeType = None

    @property
    def AppName(self):
        r"""当前应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UsedCharSize(self):
        r"""当前应用使用的字符数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

    @property
    def Proportion(self):
        r"""当前应用对于总用量的占比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Proportion

    @Proportion.setter
    def Proportion(self, Proportion):
        self._Proportion = Proportion

    @property
    def KnowledgeType(self):
        r"""知识库类型:0默认1共享
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UsedCharSize = params.get("UsedCharSize")
        self._Proportion = params.get("Proportion")
        self._KnowledgeType = params.get("KnowledgeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeDetail(AbstractModel):
    r"""应用使用知识库容量详情

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _UsedCharSize: 已用字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCharSize: str
        :param _Proportion: 使用占比
注意：此字段可能返回 null，表示取不到有效值。
        :type Proportion: float
        :param _ExceedCharSize: 超量字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceedCharSize: str
        :param _IsSharedKnowledge: 废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSharedKnowledge: bool
        :param _KnowledgeType: 知识库类型:0默认1共享
        :type KnowledgeType: int
        """
        self._AppName = None
        self._UsedCharSize = None
        self._Proportion = None
        self._ExceedCharSize = None
        self._IsSharedKnowledge = None
        self._KnowledgeType = None

    @property
    def AppName(self):
        r"""应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UsedCharSize(self):
        r"""已用字符数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

    @property
    def Proportion(self):
        r"""使用占比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Proportion

    @Proportion.setter
    def Proportion(self, Proportion):
        self._Proportion = Proportion

    @property
    def ExceedCharSize(self):
        r"""超量字符数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExceedCharSize

    @ExceedCharSize.setter
    def ExceedCharSize(self, ExceedCharSize):
        self._ExceedCharSize = ExceedCharSize

    @property
    def IsSharedKnowledge(self):
        r"""废弃
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsSharedKnowledge

    @IsSharedKnowledge.setter
    def IsSharedKnowledge(self, IsSharedKnowledge):
        self._IsSharedKnowledge = IsSharedKnowledge

    @property
    def KnowledgeType(self):
        r"""知识库类型:0默认1共享
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UsedCharSize = params.get("UsedCharSize")
        self._Proportion = params.get("Proportion")
        self._ExceedCharSize = params.get("ExceedCharSize")
        self._IsSharedKnowledge = params.get("IsSharedKnowledge")
        self._KnowledgeType = params.get("KnowledgeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeDetailInfo(AbstractModel):
    r"""知识库详情信息

    """

    def __init__(self):
        r"""
        :param _Knowledge: 知识库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Knowledge: :class:`tencentcloud.lke.v20231130.models.KnowledgeBaseInfo`
        :param _AppList: 应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppList: list of AppBaseInfo
        :param _User: 用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type User: :class:`tencentcloud.lke.v20231130.models.UserBaseInfo`
        :param _PermissionIds: 权限位信息
        :type PermissionIds: list of str
        """
        self._Knowledge = None
        self._AppList = None
        self._User = None
        self._PermissionIds = None

    @property
    def Knowledge(self):
        r"""知识库信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeBaseInfo`
        """
        return self._Knowledge

    @Knowledge.setter
    def Knowledge(self, Knowledge):
        self._Knowledge = Knowledge

    @property
    def AppList(self):
        r"""应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AppBaseInfo
        """
        return self._AppList

    @AppList.setter
    def AppList(self, AppList):
        self._AppList = AppList

    @property
    def User(self):
        r"""用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.UserBaseInfo`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def PermissionIds(self):
        r"""权限位信息
        :rtype: list of str
        """
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds


    def _deserialize(self, params):
        if params.get("Knowledge") is not None:
            self._Knowledge = KnowledgeBaseInfo()
            self._Knowledge._deserialize(params.get("Knowledge"))
        if params.get("AppList") is not None:
            self._AppList = []
            for item in params.get("AppList"):
                obj = AppBaseInfo()
                obj._deserialize(item)
                self._AppList.append(obj)
        if params.get("User") is not None:
            self._User = UserBaseInfo()
            self._User._deserialize(params.get("User"))
        self._PermissionIds = params.get("PermissionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeModelConfig(AbstractModel):
    r"""知识库模型设置

    """

    def __init__(self):
        r"""
        :param _EmbeddingModel: 向量模型，该字段只有共享知识库有，应用知识库没有
注意：此字段可能返回 null，表示取不到有效值。
        :type EmbeddingModel: str
        :param _QaExtractModel: 问答对生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :type QaExtractModel: str
        :param _SchemaModel: schema生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaModel: str
        """
        self._EmbeddingModel = None
        self._QaExtractModel = None
        self._SchemaModel = None

    @property
    def EmbeddingModel(self):
        r"""向量模型，该字段只有共享知识库有，应用知识库没有
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EmbeddingModel

    @EmbeddingModel.setter
    def EmbeddingModel(self, EmbeddingModel):
        self._EmbeddingModel = EmbeddingModel

    @property
    def QaExtractModel(self):
        r"""问答对生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QaExtractModel

    @QaExtractModel.setter
    def QaExtractModel(self, QaExtractModel):
        self._QaExtractModel = QaExtractModel

    @property
    def SchemaModel(self):
        r"""schema生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchemaModel

    @SchemaModel.setter
    def SchemaModel(self, SchemaModel):
        self._SchemaModel = SchemaModel


    def _deserialize(self, params):
        self._EmbeddingModel = params.get("EmbeddingModel")
        self._QaExtractModel = params.get("QaExtractModel")
        self._SchemaModel = params.get("SchemaModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaAgent(AbstractModel):
    r"""应用配置关联的agent信息

    """

    def __init__(self):
        r"""
        :param _AgentCollaboration: 协同方式，1：自由转交，2：工作流编排，3：Plan-and-Execute
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCollaboration: int
        :param _Workflow: 应用配置agent关联的工作流
注意：此字段可能返回 null，表示取不到有效值。
        :type Workflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaWorkflowInfo`
        """
        self._AgentCollaboration = None
        self._Workflow = None

    @property
    def AgentCollaboration(self):
        r"""协同方式，1：自由转交，2：工作流编排，3：Plan-and-Execute
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AgentCollaboration

    @AgentCollaboration.setter
    def AgentCollaboration(self, AgentCollaboration):
        self._AgentCollaboration = AgentCollaboration

    @property
    def Workflow(self):
        r"""应用配置agent关联的工作流
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaWorkflowInfo`
        """
        return self._Workflow

    @Workflow.setter
    def Workflow(self, Workflow):
        self._Workflow = Workflow


    def _deserialize(self, params):
        self._AgentCollaboration = params.get("AgentCollaboration")
        if params.get("Workflow") is not None:
            self._Workflow = KnowledgeQaWorkflowInfo()
            self._Workflow._deserialize(params.get("Workflow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaConfig(AbstractModel):
    r"""知识问答配置

    """

    def __init__(self):
        r"""
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        :param _RoleDescription: 角色描述，4000字符以内。通过填写描述，设定应用的 #角色名称、 #风格特点 及可达成的#意图。建议按照下面的模板填写，且自定义意图建议不超过5个。

#角色名称：
#风格特点：
#输出要求：
#能力限制：

能够达成以下用户意图
##意图名称：
##意图描述：
##意图示例：
##意图实现：

注意：此字段可能返回 null，表示取不到有效值。
        :type RoleDescription: str
        :param _Model: 生成模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Search: 知识搜索配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Search: list of KnowledgeQaSearch
        :param _Output: 知识管理输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaOutput`
        :param _Workflow: 工作流程配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Workflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeWorkflow`
        :param _SearchRange: 检索范围
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchRange: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        :param _Pattern: 应用模式，standard:标准模式, agent: agent模式，single_workflow：单工作流模式
注意：此字段可能返回 null，表示取不到有效值。
        :type Pattern: str
        :param _SearchStrategy: 检索策略
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchStrategy: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        :param _SingleWorkflow: 单工作流ID，Pattern为single_workflow时传入
注意：此字段可能返回 null，表示取不到有效值。
        :type SingleWorkflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        :param _Plugins: 应用关联插件
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of KnowledgeQaPlugin
        :param _ThoughtModel: 思考模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ThoughtModel: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _IntentAchievements: 意图达成方式优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentAchievements: list of IntentAchievement
        :param _ImageTextRetrieval: 是否开启图文检索
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTextRetrieval: bool
        :param _AiCall: 配置语音通话参数
注意：此字段可能返回 null，表示取不到有效值。
        :type AiCall: :class:`tencentcloud.lke.v20231130.models.AICallConfig`
        :param _ShareKnowledgeBases: 共享知识库关联配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareKnowledgeBases: list of ShareKnowledgeBase
        :param _BackgroundImage: 背景图相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BackgroundImage: :class:`tencentcloud.lke.v20231130.models.BackgroundImageConfig`
        :param _OpeningQuestions: 开场问题
注意：此字段可能返回 null，表示取不到有效值。
        :type OpeningQuestions: list of str
        :param _LongMemoryOpen: 长期记忆开关
        :type LongMemoryOpen: bool
        :param _LongMemoryDay: 长期记忆时效
        :type LongMemoryDay: int
        :param _Agent: agent配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Agent: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaAgent`
        :param _KnowledgeModelConfig: 知识库模型
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeModelConfig: :class:`tencentcloud.lke.v20231130.models.KnowledgeModelConfig`
        :param _KnowledgeAdvancedConfig: 知识库高级设置
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeAdvancedConfig: :class:`tencentcloud.lke.v20231130.models.KnowledgeAdvancedConfig`
        """
        self._Greeting = None
        self._RoleDescription = None
        self._Model = None
        self._Search = None
        self._Output = None
        self._Workflow = None
        self._SearchRange = None
        self._Pattern = None
        self._SearchStrategy = None
        self._SingleWorkflow = None
        self._Plugins = None
        self._ThoughtModel = None
        self._IntentAchievements = None
        self._ImageTextRetrieval = None
        self._AiCall = None
        self._ShareKnowledgeBases = None
        self._BackgroundImage = None
        self._OpeningQuestions = None
        self._LongMemoryOpen = None
        self._LongMemoryDay = None
        self._Agent = None
        self._KnowledgeModelConfig = None
        self._KnowledgeAdvancedConfig = None

    @property
    def Greeting(self):
        r"""欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def RoleDescription(self):
        r"""角色描述，4000字符以内。通过填写描述，设定应用的 #角色名称、 #风格特点 及可达成的#意图。建议按照下面的模板填写，且自定义意图建议不超过5个。

#角色名称：
#风格特点：
#输出要求：
#能力限制：

能够达成以下用户意图
##意图名称：
##意图描述：
##意图示例：
##意图实现：

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleDescription

    @RoleDescription.setter
    def RoleDescription(self, RoleDescription):
        self._RoleDescription = RoleDescription

    @property
    def Model(self):
        r"""生成模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Search(self):
        r"""知识搜索配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KnowledgeQaSearch
        """
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def Output(self):
        r"""知识管理输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Workflow(self):
        r"""工作流程配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeWorkflow`
        """
        return self._Workflow

    @Workflow.setter
    def Workflow(self, Workflow):
        self._Workflow = Workflow

    @property
    def SearchRange(self):
        r"""检索范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        """
        return self._SearchRange

    @SearchRange.setter
    def SearchRange(self, SearchRange):
        self._SearchRange = SearchRange

    @property
    def Pattern(self):
        r"""应用模式，standard:标准模式, agent: agent模式，single_workflow：单工作流模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def SearchStrategy(self):
        r"""检索策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        """
        return self._SearchStrategy

    @SearchStrategy.setter
    def SearchStrategy(self, SearchStrategy):
        self._SearchStrategy = SearchStrategy

    @property
    def SingleWorkflow(self):
        r"""单工作流ID，Pattern为single_workflow时传入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        """
        return self._SingleWorkflow

    @SingleWorkflow.setter
    def SingleWorkflow(self, SingleWorkflow):
        self._SingleWorkflow = SingleWorkflow

    @property
    def Plugins(self):
        r"""应用关联插件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KnowledgeQaPlugin
        """
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def ThoughtModel(self):
        r"""思考模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._ThoughtModel

    @ThoughtModel.setter
    def ThoughtModel(self, ThoughtModel):
        self._ThoughtModel = ThoughtModel

    @property
    def IntentAchievements(self):
        r"""意图达成方式优先级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IntentAchievement
        """
        return self._IntentAchievements

    @IntentAchievements.setter
    def IntentAchievements(self, IntentAchievements):
        self._IntentAchievements = IntentAchievements

    @property
    def ImageTextRetrieval(self):
        r"""是否开启图文检索
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ImageTextRetrieval

    @ImageTextRetrieval.setter
    def ImageTextRetrieval(self, ImageTextRetrieval):
        self._ImageTextRetrieval = ImageTextRetrieval

    @property
    def AiCall(self):
        r"""配置语音通话参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AICallConfig`
        """
        return self._AiCall

    @AiCall.setter
    def AiCall(self, AiCall):
        self._AiCall = AiCall

    @property
    def ShareKnowledgeBases(self):
        r"""共享知识库关联配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ShareKnowledgeBase
        """
        return self._ShareKnowledgeBases

    @ShareKnowledgeBases.setter
    def ShareKnowledgeBases(self, ShareKnowledgeBases):
        self._ShareKnowledgeBases = ShareKnowledgeBases

    @property
    def BackgroundImage(self):
        r"""背景图相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.BackgroundImageConfig`
        """
        return self._BackgroundImage

    @BackgroundImage.setter
    def BackgroundImage(self, BackgroundImage):
        self._BackgroundImage = BackgroundImage

    @property
    def OpeningQuestions(self):
        r"""开场问题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OpeningQuestions

    @OpeningQuestions.setter
    def OpeningQuestions(self, OpeningQuestions):
        self._OpeningQuestions = OpeningQuestions

    @property
    def LongMemoryOpen(self):
        r"""长期记忆开关
        :rtype: bool
        """
        return self._LongMemoryOpen

    @LongMemoryOpen.setter
    def LongMemoryOpen(self, LongMemoryOpen):
        self._LongMemoryOpen = LongMemoryOpen

    @property
    def LongMemoryDay(self):
        r"""长期记忆时效
        :rtype: int
        """
        return self._LongMemoryDay

    @LongMemoryDay.setter
    def LongMemoryDay(self, LongMemoryDay):
        self._LongMemoryDay = LongMemoryDay

    @property
    def Agent(self):
        r"""agent配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaAgent`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def KnowledgeModelConfig(self):
        r"""知识库模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeModelConfig`
        """
        return self._KnowledgeModelConfig

    @KnowledgeModelConfig.setter
    def KnowledgeModelConfig(self, KnowledgeModelConfig):
        self._KnowledgeModelConfig = KnowledgeModelConfig

    @property
    def KnowledgeAdvancedConfig(self):
        r"""知识库高级设置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeAdvancedConfig`
        """
        return self._KnowledgeAdvancedConfig

    @KnowledgeAdvancedConfig.setter
    def KnowledgeAdvancedConfig(self, KnowledgeAdvancedConfig):
        self._KnowledgeAdvancedConfig = KnowledgeAdvancedConfig


    def _deserialize(self, params):
        self._Greeting = params.get("Greeting")
        self._RoleDescription = params.get("RoleDescription")
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = KnowledgeQaSearch()
                obj._deserialize(item)
                self._Search.append(obj)
        if params.get("Output") is not None:
            self._Output = KnowledgeQaOutput()
            self._Output._deserialize(params.get("Output"))
        if params.get("Workflow") is not None:
            self._Workflow = KnowledgeWorkflow()
            self._Workflow._deserialize(params.get("Workflow"))
        if params.get("SearchRange") is not None:
            self._SearchRange = SearchRange()
            self._SearchRange._deserialize(params.get("SearchRange"))
        self._Pattern = params.get("Pattern")
        if params.get("SearchStrategy") is not None:
            self._SearchStrategy = SearchStrategy()
            self._SearchStrategy._deserialize(params.get("SearchStrategy"))
        if params.get("SingleWorkflow") is not None:
            self._SingleWorkflow = KnowledgeQaSingleWorkflow()
            self._SingleWorkflow._deserialize(params.get("SingleWorkflow"))
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = KnowledgeQaPlugin()
                obj._deserialize(item)
                self._Plugins.append(obj)
        if params.get("ThoughtModel") is not None:
            self._ThoughtModel = AppModel()
            self._ThoughtModel._deserialize(params.get("ThoughtModel"))
        if params.get("IntentAchievements") is not None:
            self._IntentAchievements = []
            for item in params.get("IntentAchievements"):
                obj = IntentAchievement()
                obj._deserialize(item)
                self._IntentAchievements.append(obj)
        self._ImageTextRetrieval = params.get("ImageTextRetrieval")
        if params.get("AiCall") is not None:
            self._AiCall = AICallConfig()
            self._AiCall._deserialize(params.get("AiCall"))
        if params.get("ShareKnowledgeBases") is not None:
            self._ShareKnowledgeBases = []
            for item in params.get("ShareKnowledgeBases"):
                obj = ShareKnowledgeBase()
                obj._deserialize(item)
                self._ShareKnowledgeBases.append(obj)
        if params.get("BackgroundImage") is not None:
            self._BackgroundImage = BackgroundImageConfig()
            self._BackgroundImage._deserialize(params.get("BackgroundImage"))
        self._OpeningQuestions = params.get("OpeningQuestions")
        self._LongMemoryOpen = params.get("LongMemoryOpen")
        self._LongMemoryDay = params.get("LongMemoryDay")
        if params.get("Agent") is not None:
            self._Agent = KnowledgeQaAgent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("KnowledgeModelConfig") is not None:
            self._KnowledgeModelConfig = KnowledgeModelConfig()
            self._KnowledgeModelConfig._deserialize(params.get("KnowledgeModelConfig"))
        if params.get("KnowledgeAdvancedConfig") is not None:
            self._KnowledgeAdvancedConfig = KnowledgeAdvancedConfig()
            self._KnowledgeAdvancedConfig._deserialize(params.get("KnowledgeAdvancedConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaOutput(AbstractModel):
    r"""应用管理输出配置

    """

    def __init__(self):
        r"""
        :param _Method: 输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: int
        :param _UseGeneralKnowledge: 通用模型回复
注意：此字段可能返回 null，表示取不到有效值。
        :type UseGeneralKnowledge: bool
        :param _BareAnswer: 未知回复语，300字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type BareAnswer: str
        :param _ShowQuestionClarify: 是否展示问题澄清开关
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowQuestionClarify: bool
        :param _UseQuestionClarify: 是否打开问题澄清
注意：此字段可能返回 null，表示取不到有效值。
        :type UseQuestionClarify: bool
        :param _QuestionClarifyKeywords: 问题澄清关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QuestionClarifyKeywords: list of str
        :param _UseRecommended: 是否打开推荐问题开关
注意：此字段可能返回 null，表示取不到有效值。
        :type UseRecommended: bool
        :param _RecommendedPromptMode: 推荐问模式，0.结合知识库&对话历史推荐问题Prompt(默认) 1.仅结合知识库输出推荐问的prompt
注意：此字段可能返回 null，表示取不到有效值。
        :type RecommendedPromptMode: int
        :param _InputBoxConfig: 输入框按钮配置
        :type InputBoxConfig: :class:`tencentcloud.lke.v20231130.models.InputBoxConfig`
        """
        self._Method = None
        self._UseGeneralKnowledge = None
        self._BareAnswer = None
        self._ShowQuestionClarify = None
        self._UseQuestionClarify = None
        self._QuestionClarifyKeywords = None
        self._UseRecommended = None
        self._RecommendedPromptMode = None
        self._InputBoxConfig = None

    @property
    def Method(self):
        r"""输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UseGeneralKnowledge(self):
        r"""通用模型回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UseGeneralKnowledge

    @UseGeneralKnowledge.setter
    def UseGeneralKnowledge(self, UseGeneralKnowledge):
        self._UseGeneralKnowledge = UseGeneralKnowledge

    @property
    def BareAnswer(self):
        r"""未知回复语，300字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BareAnswer

    @BareAnswer.setter
    def BareAnswer(self, BareAnswer):
        self._BareAnswer = BareAnswer

    @property
    def ShowQuestionClarify(self):
        r"""是否展示问题澄清开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ShowQuestionClarify

    @ShowQuestionClarify.setter
    def ShowQuestionClarify(self, ShowQuestionClarify):
        self._ShowQuestionClarify = ShowQuestionClarify

    @property
    def UseQuestionClarify(self):
        r"""是否打开问题澄清
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UseQuestionClarify

    @UseQuestionClarify.setter
    def UseQuestionClarify(self, UseQuestionClarify):
        self._UseQuestionClarify = UseQuestionClarify

    @property
    def QuestionClarifyKeywords(self):
        r"""问题澄清关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._QuestionClarifyKeywords

    @QuestionClarifyKeywords.setter
    def QuestionClarifyKeywords(self, QuestionClarifyKeywords):
        self._QuestionClarifyKeywords = QuestionClarifyKeywords

    @property
    def UseRecommended(self):
        r"""是否打开推荐问题开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UseRecommended

    @UseRecommended.setter
    def UseRecommended(self, UseRecommended):
        self._UseRecommended = UseRecommended

    @property
    def RecommendedPromptMode(self):
        r"""推荐问模式，0.结合知识库&对话历史推荐问题Prompt(默认) 1.仅结合知识库输出推荐问的prompt
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RecommendedPromptMode

    @RecommendedPromptMode.setter
    def RecommendedPromptMode(self, RecommendedPromptMode):
        self._RecommendedPromptMode = RecommendedPromptMode

    @property
    def InputBoxConfig(self):
        r"""输入框按钮配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.InputBoxConfig`
        """
        return self._InputBoxConfig

    @InputBoxConfig.setter
    def InputBoxConfig(self, InputBoxConfig):
        self._InputBoxConfig = InputBoxConfig


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._UseGeneralKnowledge = params.get("UseGeneralKnowledge")
        self._BareAnswer = params.get("BareAnswer")
        self._ShowQuestionClarify = params.get("ShowQuestionClarify")
        self._UseQuestionClarify = params.get("UseQuestionClarify")
        self._QuestionClarifyKeywords = params.get("QuestionClarifyKeywords")
        self._UseRecommended = params.get("UseRecommended")
        self._RecommendedPromptMode = params.get("RecommendedPromptMode")
        if params.get("InputBoxConfig") is not None:
            self._InputBoxConfig = InputBoxConfig()
            self._InputBoxConfig._deserialize(params.get("InputBoxConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaPlugin(AbstractModel):
    r"""应用关联插件信息

    """

    def __init__(self):
        r"""
        :param _PluginId: 插件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginId: str
        :param _PluginName: 插件名称
        :type PluginName: str
        :param _PluginIcon: 插件图标
        :type PluginIcon: str
        :param _ToolId: 工具ID
        :type ToolId: str
        :param _ToolName: 工具名称
        :type ToolName: str
        :param _ToolDesc: 工具描述
        :type ToolDesc: str
        :param _Inputs: 工具输入参数
        :type Inputs: list of PluginToolReqParam
        :param _IsBindingKnowledge: 插件是否和知识库绑定
        :type IsBindingKnowledge: bool
        """
        self._PluginId = None
        self._PluginName = None
        self._PluginIcon = None
        self._ToolId = None
        self._ToolName = None
        self._ToolDesc = None
        self._Inputs = None
        self._IsBindingKnowledge = None

    @property
    def PluginId(self):
        r"""插件ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        r"""插件名称
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginIcon(self):
        r"""插件图标
        :rtype: str
        """
        return self._PluginIcon

    @PluginIcon.setter
    def PluginIcon(self, PluginIcon):
        self._PluginIcon = PluginIcon

    @property
    def ToolId(self):
        r"""工具ID
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""工具名称
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolDesc(self):
        r"""工具描述
        :rtype: str
        """
        return self._ToolDesc

    @ToolDesc.setter
    def ToolDesc(self, ToolDesc):
        self._ToolDesc = ToolDesc

    @property
    def Inputs(self):
        r"""工具输入参数
        :rtype: list of PluginToolReqParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def IsBindingKnowledge(self):
        r"""插件是否和知识库绑定
        :rtype: bool
        """
        return self._IsBindingKnowledge

    @IsBindingKnowledge.setter
    def IsBindingKnowledge(self, IsBindingKnowledge):
        self._IsBindingKnowledge = IsBindingKnowledge


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._PluginIcon = params.get("PluginIcon")
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ToolDesc = params.get("ToolDesc")
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        self._IsBindingKnowledge = params.get("IsBindingKnowledge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaSearch(AbstractModel):
    r"""检索配置

    """

    def __init__(self):
        r"""
        :param _Type: 知识来源 doc：文档，qa：问答  taskflow：业务流程，search：搜索增强，database:数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ReplyFlexibility: 问答-回复灵活度 1：已采纳答案直接回复 2：已采纳润色后回复
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyFlexibility: int
        :param _UseSearchEngine: 搜索增强-搜索引擎状态
注意：此字段可能返回 null，表示取不到有效值。
        :type UseSearchEngine: bool
        :param _ShowSearchEngine: 是否显示搜索引擎检索状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowSearchEngine: bool
        :param _IsEnabled: 知识来源，是否选择
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnabled: bool
        :param _QaTopN: 问答最大召回数量, 默认2，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :type QaTopN: int
        :param _DocTopN: 文档最大召回数量, 默认3，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :type DocTopN: int
        :param _Confidence: 检索置信度，针对文档和问答有效，最小0.01，最大0.99
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _ResourceStatus: 资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        """
        self._Type = None
        self._ReplyFlexibility = None
        self._UseSearchEngine = None
        self._ShowSearchEngine = None
        self._IsEnabled = None
        self._QaTopN = None
        self._DocTopN = None
        self._Confidence = None
        self._ResourceStatus = None

    @property
    def Type(self):
        r"""知识来源 doc：文档，qa：问答  taskflow：业务流程，search：搜索增强，database:数据库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ReplyFlexibility(self):
        r"""问答-回复灵活度 1：已采纳答案直接回复 2：已采纳润色后回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def UseSearchEngine(self):
        r"""搜索增强-搜索引擎状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UseSearchEngine

    @UseSearchEngine.setter
    def UseSearchEngine(self, UseSearchEngine):
        self._UseSearchEngine = UseSearchEngine

    @property
    def ShowSearchEngine(self):
        r"""是否显示搜索引擎检索状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ShowSearchEngine

    @ShowSearchEngine.setter
    def ShowSearchEngine(self, ShowSearchEngine):
        self._ShowSearchEngine = ShowSearchEngine

    @property
    def IsEnabled(self):
        r"""知识来源，是否选择
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def QaTopN(self):
        r"""问答最大召回数量, 默认2，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QaTopN

    @QaTopN.setter
    def QaTopN(self, QaTopN):
        self._QaTopN = QaTopN

    @property
    def DocTopN(self):
        r"""文档最大召回数量, 默认3，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DocTopN

    @DocTopN.setter
    def DocTopN(self, DocTopN):
        self._DocTopN = DocTopN

    @property
    def Confidence(self):
        r"""检索置信度，针对文档和问答有效，最小0.01，最大0.99
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ResourceStatus(self):
        r"""资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ReplyFlexibility = params.get("ReplyFlexibility")
        self._UseSearchEngine = params.get("UseSearchEngine")
        self._ShowSearchEngine = params.get("ShowSearchEngine")
        self._IsEnabled = params.get("IsEnabled")
        self._QaTopN = params.get("QaTopN")
        self._DocTopN = params.get("DocTopN")
        self._Confidence = params.get("Confidence")
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaSingleWorkflow(AbstractModel):
    r"""问答知识库单工作流模式下指定单工作流配置

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _WorkflowDesc: 工作流描述
        :type WorkflowDesc: str
        :param _Status: 工作流状态，发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 FAIL:发布失败)
        :type Status: str
        :param _IsEnable: 工作流是否启用
        :type IsEnable: bool
        :param _AsyncWorkflow: 是否开启异步调用工作流
        :type AsyncWorkflow: bool
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowDesc = None
        self._Status = None
        self._IsEnable = None
        self._AsyncWorkflow = None

    @property
    def WorkflowId(self):
        r"""工作流ID
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

    @property
    def WorkflowDesc(self):
        r"""工作流描述
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def Status(self):
        r"""工作流状态，发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 FAIL:发布失败)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsEnable(self):
        r"""工作流是否启用
        :rtype: bool
        """
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable

    @property
    def AsyncWorkflow(self):
        r"""是否开启异步调用工作流
        :rtype: bool
        """
        return self._AsyncWorkflow

    @AsyncWorkflow.setter
    def AsyncWorkflow(self, AsyncWorkflow):
        self._AsyncWorkflow = AsyncWorkflow


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._Status = params.get("Status")
        self._IsEnable = params.get("IsEnable")
        self._AsyncWorkflow = params.get("AsyncWorkflow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaWorkflowInfo(AbstractModel):
    r"""应用配置关联的工作流信息

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _WorkflowDesc: 工作流描述
        :type WorkflowDesc: str
        :param _Status: 工作流状态，发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 FAIL:发布失败)
        :type Status: str
        :param _IsEnable: 工作流是否启用
        :type IsEnable: bool
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowDesc = None
        self._Status = None
        self._IsEnable = None

    @property
    def WorkflowId(self):
        r"""工作流ID
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

    @property
    def WorkflowDesc(self):
        r"""工作流描述
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def Status(self):
        r"""工作流状态，发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 FAIL:发布失败)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsEnable(self):
        r"""工作流是否启用
        :rtype: bool
        """
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._Status = params.get("Status")
        self._IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSummary(AbstractModel):
    r"""检索知识

    """

    def __init__(self):
        r"""
        :param _Type: 1是问答 2是文档片段
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Content: 知识内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Type = None
        self._Content = None

    @property
    def Type(self):
        r"""1是问答 2是文档片段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        r"""知识内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeUpdateInfo(AbstractModel):
    r"""共享知识库更新信息

    """

    def __init__(self):
        r"""
        :param _KnowledgeName: 共享知识库名称
        :type KnowledgeName: str
        :param _KnowledgeDescription: 共享知识库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeDescription: str
        :param _EmbeddingModel: Embedding模型
注意：此字段可能返回 null，表示取不到有效值。
        :type EmbeddingModel: str
        :param _QaExtractModel: 问答提取模型
注意：此字段可能返回 null，表示取不到有效值。
        :type QaExtractModel: str
        :param _OwnerStaffId: 拥有者id
        :type OwnerStaffId: str
        """
        self._KnowledgeName = None
        self._KnowledgeDescription = None
        self._EmbeddingModel = None
        self._QaExtractModel = None
        self._OwnerStaffId = None

    @property
    def KnowledgeName(self):
        r"""共享知识库名称
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName

    @property
    def KnowledgeDescription(self):
        r"""共享知识库描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeDescription

    @KnowledgeDescription.setter
    def KnowledgeDescription(self, KnowledgeDescription):
        self._KnowledgeDescription = KnowledgeDescription

    @property
    def EmbeddingModel(self):
        warnings.warn("parameter `EmbeddingModel` is deprecated", DeprecationWarning) 

        r"""Embedding模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EmbeddingModel

    @EmbeddingModel.setter
    def EmbeddingModel(self, EmbeddingModel):
        warnings.warn("parameter `EmbeddingModel` is deprecated", DeprecationWarning) 

        self._EmbeddingModel = EmbeddingModel

    @property
    def QaExtractModel(self):
        warnings.warn("parameter `QaExtractModel` is deprecated", DeprecationWarning) 

        r"""问答提取模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QaExtractModel

    @QaExtractModel.setter
    def QaExtractModel(self, QaExtractModel):
        warnings.warn("parameter `QaExtractModel` is deprecated", DeprecationWarning) 

        self._QaExtractModel = QaExtractModel

    @property
    def OwnerStaffId(self):
        r"""拥有者id
        :rtype: str
        """
        return self._OwnerStaffId

    @OwnerStaffId.setter
    def OwnerStaffId(self, OwnerStaffId):
        self._OwnerStaffId = OwnerStaffId


    def _deserialize(self, params):
        self._KnowledgeName = params.get("KnowledgeName")
        self._KnowledgeDescription = params.get("KnowledgeDescription")
        self._EmbeddingModel = params.get("EmbeddingModel")
        self._QaExtractModel = params.get("QaExtractModel")
        self._OwnerStaffId = params.get("OwnerStaffId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeWorkflow(AbstractModel):
    r"""问答知识库工作流配置

    """

    def __init__(self):
        r"""
        :param _IsEnabled: 是否启用工作流
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnabled: bool
        :param _UsePdl: 是否启用PDL
注意：此字段可能返回 null，表示取不到有效值。
        :type UsePdl: bool
        """
        self._IsEnabled = None
        self._UsePdl = None

    @property
    def IsEnabled(self):
        r"""是否启用工作流
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def UsePdl(self):
        r"""是否启用PDL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UsePdl

    @UsePdl.setter
    def UsePdl(self, UsePdl):
        self._UsePdl = UsePdl


    def _deserialize(self, params):
        self._IsEnabled = params.get("IsEnabled")
        self._UsePdl = params.get("UsePdl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    r"""标签ID

    """

    def __init__(self):
        r"""
        :param _LabelBizId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelBizId: str
        :param _LabelName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        """
        self._LabelBizId = None
        self._LabelName = None

    @property
    def LabelBizId(self):
        r"""标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppKnowledgeDetailRequest(AbstractModel):
    r"""ListAppKnowledgeDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页面大小
        :type PageSize: int
        :param _AppBizIds: 应用ID列表
        :type AppBizIds: list of str
        :param _SpaceId: 空间列表
        :type SpaceId: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._AppBizIds = None
        self._SpaceId = None

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""页面大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AppBizIds(self):
        r"""应用ID列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SpaceId(self):
        r"""空间列表
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._AppBizIds = params.get("AppBizIds")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppKnowledgeDetailResponse(AbstractModel):
    r"""ListAppKnowledgeDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 列表总数
        :type Total: int
        :param _List: 应用使用知识库容量详情
        :type List: list of KnowledgeDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""应用使用知识库容量详情
        :rtype: list of KnowledgeDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = KnowledgeDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAppRequest(AbstractModel):
    r"""ListApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa - 知识问答管理 
        :type AppType: str
        :param _PageSize: 每页数目，整型
        :type PageSize: int
        :param _PageNumber: 页码，整型
        :type PageNumber: int
        :param _Keyword: 关键词：应用/修改人
        :type Keyword: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        :param _AgentType: 智能体类型 dialogue：对话智能体，wechat：公众号智能体
        :type AgentType: str
        :param _AppStatus: 应用状态 1:未上线   2：运行中
        :type AppStatus: str
        """
        self._AppType = None
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None
        self._LoginSubAccountUin = None
        self._AgentType = None
        self._AppStatus = None

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa - 知识问答管理 
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def PageSize(self):
        r"""每页数目，整型
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""页码，整型
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        r"""关键词：应用/修改人
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AgentType(self):
        r"""智能体类型 dialogue：对话智能体，wechat：公众号智能体
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def AppStatus(self):
        r"""应用状态 1:未上线   2：运行中
        :rtype: str
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._AgentType = params.get("AgentType")
        self._AppStatus = params.get("AppStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppResponse(AbstractModel):
    r"""ListApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数量
        :type Total: str
        :param _List: 应用列表
        :type List: list of AppInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""应用列表
        :rtype: list of AppInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AppInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttributeLabelRequest(AbstractModel):
    r"""ListAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _PageNumber: 页码，取值范围：大于0
        :type PageNumber: int
        :param _PageSize: 每页数量，取值范围：大于0
        :type PageSize: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 查询内容，同时匹配标签内容和标签值内容
        :type Query: str
        :param _LabelSize: 每个标签同步拉取的标签值数量。即在展示标签列表时，为每一个标签加载多少个具体的标签值。
        :type LabelSize: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._LabelSize = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码，取值范围：大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量，取值范围：大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        r"""查询内容，同时匹配标签内容和标签值内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LabelSize(self):
        r"""每个标签同步拉取的标签值数量。即在展示标签列表时，为每一个标签加载多少个具体的标签值。
        :rtype: int
        """
        return self._LabelSize

    @LabelSize.setter
    def LabelSize(self, LabelSize):
        self._LabelSize = LabelSize


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._LabelSize = params.get("LabelSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttributeLabelResponse(AbstractModel):
    r"""ListAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 列表
        :type List: list of AttrLabelDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""列表
        :rtype: list of AttrLabelDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttrLabelDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListChannelRequest(AbstractModel):
    r"""ListChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :type AppBizId: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 分页数量（取值范围为1-200）
        :type PageSize: int
        :param _ChannelType: 渠道类型, 10000: 微信订阅号，10001: 微信服务号，10002：企微应用，10004：微信客服，10005：小程序，10009：企微智能机器人 。（默认为[]）
        :type ChannelType: list of int non-negative
        :param _ChannelStatus: 渠道状态 1未发布 2运行中 3已下线 （默认为[]）
        :type ChannelStatus: list of int non-negative
        """
        self._AppBizId = None
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._ChannelType = None
        self._ChannelStatus = None

    @property
    def AppBizId(self):
        r"""应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def BotBizId(self):
        warnings.warn("parameter `BotBizId` is deprecated", DeprecationWarning) 

        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        warnings.warn("parameter `BotBizId` is deprecated", DeprecationWarning) 

        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页数量（取值范围为1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ChannelType(self):
        r"""渠道类型, 10000: 微信订阅号，10001: 微信服务号，10002：企微应用，10004：微信客服，10005：小程序，10009：企微智能机器人 。（默认为[]）
        :rtype: list of int non-negative
        """
        return self._ChannelType

    @ChannelType.setter
    def ChannelType(self, ChannelType):
        self._ChannelType = ChannelType

    @property
    def ChannelStatus(self):
        r"""渠道状态 1未发布 2运行中 3已下线 （默认为[]）
        :rtype: list of int non-negative
        """
        return self._ChannelStatus

    @ChannelStatus.setter
    def ChannelStatus(self, ChannelStatus):
        self._ChannelStatus = ChannelStatus


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ChannelType = params.get("ChannelType")
        self._ChannelStatus = params.get("ChannelStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListChannelResponse(AbstractModel):
    r"""ListChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回总数
        :type Total: int
        :param _ListChannel: 渠道信息列表
        :type ListChannel: list of ChannelListInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ListChannel = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ListChannel(self):
        r"""渠道信息列表
        :rtype: list of ChannelListInfo
        """
        return self._ListChannel

    @ListChannel.setter
    def ListChannel(self, ListChannel):
        self._ListChannel = ListChannel

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
        if params.get("ListChannel") is not None:
            self._ListChannel = []
            for item in params.get("ListChannel"):
                obj = ChannelListInfo()
                obj._deserialize(item)
                self._ListChannel.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocCateRequest(AbstractModel):
    r"""ListDocCate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QueryType: 分类查询类型：0-全量查询整棵标签树，1-根据父节点BizId分页查询子节点，2-关键词检索所有匹配的分类链路
        :type QueryType: int
        :param _ParentCateBizId: QueryType=1时，父节点分类ID
        :type ParentCateBizId: str
        :param _PageNumber: QueryType=1时，页码（从1开始）
        :type PageNumber: int
        :param _PageSize: 每页数量（默认10）
        :type PageSize: int
        :param _Query: QueryType=2时，搜索内容
        :type Query: str
        """
        self._BotBizId = None
        self._QueryType = None
        self._ParentCateBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QueryType(self):
        r"""分类查询类型：0-全量查询整棵标签树，1-根据父节点BizId分页查询子节点，2-关键词检索所有匹配的分类链路
        :rtype: int
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ParentCateBizId(self):
        r"""QueryType=1时，父节点分类ID
        :rtype: str
        """
        return self._ParentCateBizId

    @ParentCateBizId.setter
    def ParentCateBizId(self, ParentCateBizId):
        self._ParentCateBizId = ParentCateBizId

    @property
    def PageNumber(self):
        r"""QueryType=1时，页码（从1开始）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（默认10）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""QueryType=2时，搜索内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QueryType = params.get("QueryType")
        self._ParentCateBizId = params.get("ParentCateBizId")
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
        


class ListDocCateResponse(AbstractModel):
    r"""ListDocCate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表
        :type List: list of CateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""列表
        :rtype: list of CateInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CateInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocItem(AbstractModel):
    r"""文档列表详情描述

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocBizId: str
        :param _FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _NewName: 重命名的新文档名称，在重命名提交之后，文档发布之前都是这个名称
        :type NewName: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _CosUrl: cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Status: 文档状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 文档状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _IsRefer: 答案中是否引用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRefer: bool
        :param _QaNum: 问答对数量
注意：此字段可能返回 null，表示取不到有效值。
        :type QaNum: int
        :param _IsDeleted: 是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeleted: bool
        :param _Source: 文档来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _SourceDesc: 文档来源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceDesc: str
        :param _IsAllowRestart: 是否允许重新生成
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowRestart: bool
        :param _IsDeletedQa: qa是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeletedQa: bool
        :param _IsCreatingQa: 问答是否生成中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCreatingQa: bool
        :param _IsAllowDelete: 是否允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowDelete: bool
        :param _IsAllowRefer: 是否允许操作引用开关
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowRefer: bool
        :param _IsCreatedQa: 问答是否生成过
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCreatedQa: bool
        :param _DocCharSize: 文档字符量
注意：此字段可能返回 null，表示取不到有效值。
        :type DocCharSize: str
        :param _AttrRange: 属性标签适用范围
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrRange: int
        :param _AttrLabels: 属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrLabels: list of AttrLabel
        :param _IsAllowEdit: 是否允许编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowEdit: bool
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferUrlType: int
        :param _WebUrl: 网页(或自定义链接)地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebUrl: str
        :param _ExpireStart: 有效开始时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireEnd: str
        :param _IsAllowRetry: 是否允许重试，0：否，1：是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowRetry: bool
        :param _Processing: 0:文档比对处理 1:文档生成问答
注意：此字段可能返回 null，表示取不到有效值。
        :type Processing: list of int
        :param _CreateTime: 文档创建落库时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CateBizId: 文档所属分类ID
        :type CateBizId: str
        :param _CustomerKnowledgeId: 文档的用户自定义ID
        :type CustomerKnowledgeId: str
        :param _AttributeFlags: 文档的属性标记，0: 不做用户外部权限校验
        :type AttributeFlags: list of int non-negative
        :param _IsDisabled: false:未停用，ture:已停用
        :type IsDisabled: bool
        :param _StaffName: 员工名称
        :type StaffName: str
        :param _EnableScope: 文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableScope: int
        """
        self._DocBizId = None
        self._FileName = None
        self._NewName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._AttrRange = None
        self._AttrLabels = None
        self._IsAllowEdit = None
        self._ReferUrlType = None
        self._WebUrl = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._IsAllowRetry = None
        self._Processing = None
        self._CreateTime = None
        self._CateBizId = None
        self._CustomerKnowledgeId = None
        self._AttributeFlags = None
        self._IsDisabled = None
        self._StaffName = None
        self._EnableScope = None

    @property
    def DocBizId(self):
        r"""文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        r"""文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewName(self):
        r"""重命名的新文档名称，在重命名提交之后，文档发布之前都是这个名称
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def FileType(self):
        r"""文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        r"""cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

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
    def Status(self):
        r"""文档状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""文档状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        r"""原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        r"""答案中是否引用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        r"""问答对数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        r"""是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        r"""文档来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        r"""文档来源描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        r"""是否允许重新生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        r"""qa是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        r"""问答是否生成中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        r"""是否允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        r"""是否允许操作引用开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        r"""问答是否生成过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        r"""文档字符量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def AttrRange(self):
        r"""属性标签适用范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def IsAllowEdit(self):
        r"""是否允许编辑
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def ReferUrlType(self):
        r"""外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def WebUrl(self):
        r"""网页(或自定义链接)地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ExpireStart(self):
        r"""有效开始时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，unix时间戳，0代表永久有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def IsAllowRetry(self):
        r"""是否允许重试，0：否，1：是
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowRetry

    @IsAllowRetry.setter
    def IsAllowRetry(self, IsAllowRetry):
        self._IsAllowRetry = IsAllowRetry

    @property
    def Processing(self):
        r"""0:文档比对处理 1:文档生成问答
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Processing

    @Processing.setter
    def Processing(self, Processing):
        self._Processing = Processing

    @property
    def CreateTime(self):
        r"""文档创建落库时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CateBizId(self):
        r"""文档所属分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def CustomerKnowledgeId(self):
        r"""文档的用户自定义ID
        :rtype: str
        """
        return self._CustomerKnowledgeId

    @CustomerKnowledgeId.setter
    def CustomerKnowledgeId(self, CustomerKnowledgeId):
        self._CustomerKnowledgeId = CustomerKnowledgeId

    @property
    def AttributeFlags(self):
        r"""文档的属性标记，0: 不做用户外部权限校验
        :rtype: list of int non-negative
        """
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags

    @property
    def IsDisabled(self):
        r"""false:未停用，ture:已停用
        :rtype: bool
        """
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled

    @property
    def StaffName(self):
        r"""员工名称
        :rtype: str
        """
        return self._StaffName

    @StaffName.setter
    def StaffName(self, StaffName):
        self._StaffName = StaffName

    @property
    def EnableScope(self):
        r"""文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._NewName = params.get("NewName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._ReferUrlType = params.get("ReferUrlType")
        self._WebUrl = params.get("WebUrl")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._IsAllowRetry = params.get("IsAllowRetry")
        self._Processing = params.get("Processing")
        self._CreateTime = params.get("CreateTime")
        self._CateBizId = params.get("CateBizId")
        self._CustomerKnowledgeId = params.get("CustomerKnowledgeId")
        self._AttributeFlags = params.get("AttributeFlags")
        self._IsDisabled = params.get("IsDisabled")
        self._StaffName = params.get("StaffName")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocRequest(AbstractModel):
    r"""ListDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID, 获取方式参看 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _PageNumber: 页码(必须大于0)
        :type PageNumber: int
        :param _PageSize: 每页数量(取值范围1-200)
        :type PageSize: int
        :param _Query: 查询内容

输入特定标识 lke:system:untagged  将查询所有未关联标签的文档
        :type Query: str
        :param _Status: 文档状态： 1-未生成 2-生成中 3-生成成功 4-生成失败 5-删除中 6-删除成功  7-审核中  8-审核失败 9-审核成功  10-待发布  11-发布中  12-已发布  13-学习中  14-学习失败  15-更新中  16-更新失败  17-解析中  18-解析失败  19-导入失败   20-已过期 21-超量失效 22-超量失效恢复
        :type Status: list of int
        :param _QueryType: 查询类型 filename 文档、 attribute 标签
        :type QueryType: str
        :param _CateBizId: 分类ID, 调用接口[ListDocCate](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListDocCate)获取
        :type CateBizId: str
        :param _FileTypes: 文件类型分类筛选
        :type FileTypes: list of str
        :param _FilterFlag: 文档列表筛选标识位
        :type FilterFlag: list of DocFilterFlag
        :param _ShowCurrCate: 是否只展示当前分类的数据 0不是，1是
        :type ShowCurrCate: int
        :param _EnableScope: 文档生效域；不检索默认为0
        :type EnableScope: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._Status = None
        self._QueryType = None
        self._CateBizId = None
        self._FileTypes = None
        self._FilterFlag = None
        self._ShowCurrCate = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID, 获取方式参看 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码(必须大于0)
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量(取值范围1-200)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容

输入特定标识 lke:system:untagged  将查询所有未关联标签的文档
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Status(self):
        r"""文档状态： 1-未生成 2-生成中 3-生成成功 4-生成失败 5-删除中 6-删除成功  7-审核中  8-审核失败 9-审核成功  10-待发布  11-发布中  12-已发布  13-学习中  14-学习失败  15-更新中  16-更新失败  17-解析中  18-解析失败  19-导入失败   20-已过期 21-超量失效 22-超量失效恢复
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def QueryType(self):
        r"""查询类型 filename 文档、 attribute 标签
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def CateBizId(self):
        r"""分类ID, 调用接口[ListDocCate](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListDocCate)获取
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def FileTypes(self):
        r"""文件类型分类筛选
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def FilterFlag(self):
        r"""文档列表筛选标识位
        :rtype: list of DocFilterFlag
        """
        return self._FilterFlag

    @FilterFlag.setter
    def FilterFlag(self, FilterFlag):
        self._FilterFlag = FilterFlag

    @property
    def ShowCurrCate(self):
        r"""是否只展示当前分类的数据 0不是，1是
        :rtype: int
        """
        return self._ShowCurrCate

    @ShowCurrCate.setter
    def ShowCurrCate(self, ShowCurrCate):
        self._ShowCurrCate = ShowCurrCate

    @property
    def EnableScope(self):
        r"""文档生效域；不检索默认为0
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._Status = params.get("Status")
        self._QueryType = params.get("QueryType")
        self._CateBizId = params.get("CateBizId")
        self._FileTypes = params.get("FileTypes")
        if params.get("FilterFlag") is not None:
            self._FilterFlag = []
            for item in params.get("FilterFlag"):
                obj = DocFilterFlag()
                obj._deserialize(item)
                self._FilterFlag.append(obj)
        self._ShowCurrCate = params.get("ShowCurrCate")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocResponse(AbstractModel):
    r"""ListDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ListDocItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""文档数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""文档列表
        :rtype: list of ListDocItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListDocItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListModelRequest(AbstractModel):
    r"""ListModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _Pattern: 应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :type Pattern: str
        :param _ModelCategory: 模型类别 generate：生成模型，thought：思考模型,embedding模型，rerank：rerank模型
        :type ModelCategory: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)	
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._AppType = None
        self._Pattern = None
        self._ModelCategory = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def Pattern(self):
        r"""应用模式 standard:标准模式, agent: agent模式，single_workflow：单工作流模式
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ModelCategory(self):
        r"""模型类别 generate：生成模型，thought：思考模型,embedding模型，rerank：rerank模型
        :rtype: str
        """
        return self._ModelCategory

    @ModelCategory.setter
    def ModelCategory(self, ModelCategory):
        self._ModelCategory = ModelCategory

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._Pattern = params.get("Pattern")
        self._ModelCategory = params.get("ModelCategory")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListModelResponse(AbstractModel):
    r"""ListModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 模型列表
        :type List: list of ModelInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""模型列表
        :rtype: list of ModelInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ModelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQACateRequest(AbstractModel):
    r"""ListQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QueryType: 分类查询类型：0-全量查询整棵标签树，1-根据父节点BizId分页查询子节点，2-关键词检索所有匹配的分类链路
        :type QueryType: int
        :param _ParentCateBizId: QueryType=1时，父节点分类ID
        :type ParentCateBizId: str
        :param _PageNumber: QueryType=1时，页码（从1开始）
        :type PageNumber: int
        :param _PageSize: 每页数量（默认10）
        :type PageSize: int
        :param _Query: QueryType=2时，搜索内容
        :type Query: str
        """
        self._BotBizId = None
        self._QueryType = None
        self._ParentCateBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QueryType(self):
        r"""分类查询类型：0-全量查询整棵标签树，1-根据父节点BizId分页查询子节点，2-关键词检索所有匹配的分类链路
        :rtype: int
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ParentCateBizId(self):
        r"""QueryType=1时，父节点分类ID
        :rtype: str
        """
        return self._ParentCateBizId

    @ParentCateBizId.setter
    def ParentCateBizId(self, ParentCateBizId):
        self._ParentCateBizId = ParentCateBizId

    @property
    def PageNumber(self):
        r"""QueryType=1时，页码（从1开始）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（默认10）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""QueryType=2时，搜索内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QueryType = params.get("QueryType")
        self._ParentCateBizId = params.get("ParentCateBizId")
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
        


class ListQACateResponse(AbstractModel):
    r"""ListQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表
        :type List: list of QACate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""列表
        :rtype: list of QACate
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QACate()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQARequest(AbstractModel):
    r"""ListQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
若要操作共享知识库，传KnowledgeBizId
        :type BotBizId: str
        :param _PageNumber: 页码（取值范围>0）
        :type PageNumber: int
        :param _PageSize: 每页大小(取值范围1-200)
        :type PageSize: int
        :param _Query: 查询问题

输入特定标识 lke:system:untagged  将查询所有未关联标签的问答
        :type Query: str
        :param _AcceptStatus: 校验状态(1未校验2采纳3不采纳)
如果不填默认值为空数组，表示不筛选，返回所有状态
        :type AcceptStatus: list of int
        :param _ReleaseStatus: 发布状态(2待发布 3发布中 4已发布 7审核中 8审核失败 9人工申述中 11人工申述失败 12已过期 13超量失效 14超量失效恢复)
如果不填默认值为空数组，表示不筛选返回所有状态
        :type ReleaseStatus: list of int
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _Source: 来源(1 文档生成 2 批量导入 3 手动添加)
不填默认值为0，表示不过滤，返回所有状态
        :type Source: int
        :param _QueryAnswer: 查询答案
        :type QueryAnswer: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _QaBizIds: QA业务ID列表
        :type QaBizIds: list of str
        :param _QueryType: 查询类型 filename 名称、 attribute 标签
如果不填默认值为"filename"
        :type QueryType: str
        :param _ShowCurrCate: 是否只展示当前分类的数据 0不是，1是
        :type ShowCurrCate: int
        :param _EnableScope: // 知识生效作用域枚举值 enum RetrievalEnableScope {   ENABLE_SCOPE_TYPE_UNKNOWN = 0; // 未知类型   ENABLE_SCOPE_TYPE_NONE = 1; // 停用   ENABLE_SCOPE_TYPE_DEV = 2; // 仅开发域   ENABLE_SCOPE_TYPE_RELEASE = 3; // 仅发布域   ENABLE_SCOPE_TYPE_ALL = 4; // 全域 }  问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._Source = None
        self._QueryAnswer = None
        self._CateBizId = None
        self._QaBizIds = None
        self._QueryType = None
        self._ShowCurrCate = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID
若要操作共享知识库，传KnowledgeBizId
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（取值范围>0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小(取值范围1-200)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询问题

输入特定标识 lke:system:untagged  将查询所有未关联标签的问答
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def AcceptStatus(self):
        r"""校验状态(1未校验2采纳3不采纳)
如果不填默认值为空数组，表示不筛选，返回所有状态
        :rtype: list of int
        """
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        r"""发布状态(2待发布 3发布中 4已发布 7审核中 8审核失败 9人工申述中 11人工申述失败 12已过期 13超量失效 14超量失效恢复)
如果不填默认值为空数组，表示不筛选返回所有状态
        :rtype: list of int
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def Source(self):
        r"""来源(1 文档生成 2 批量导入 3 手动添加)
不填默认值为0，表示不过滤，返回所有状态
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        r"""查询答案
        :rtype: str
        """
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def QaBizIds(self):
        r"""QA业务ID列表
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def QueryType(self):
        r"""查询类型 filename 名称、 attribute 标签
如果不填默认值为"filename"
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ShowCurrCate(self):
        r"""是否只展示当前分类的数据 0不是，1是
        :rtype: int
        """
        return self._ShowCurrCate

    @ShowCurrCate.setter
    def ShowCurrCate(self, ShowCurrCate):
        self._ShowCurrCate = ShowCurrCate

    @property
    def EnableScope(self):
        r"""// 知识生效作用域枚举值 enum RetrievalEnableScope {   ENABLE_SCOPE_TYPE_UNKNOWN = 0; // 未知类型   ENABLE_SCOPE_TYPE_NONE = 1; // 停用   ENABLE_SCOPE_TYPE_DEV = 2; // 仅开发域   ENABLE_SCOPE_TYPE_RELEASE = 3; // 仅发布域   ENABLE_SCOPE_TYPE_ALL = 4; // 全域 }  问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        self._CateBizId = params.get("CateBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._QueryType = params.get("QueryType")
        self._ShowCurrCate = params.get("ShowCurrCate")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQAResponse(AbstractModel):
    r"""ListQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 问答数量
        :type Total: str
        :param _WaitVerifyTotal: 待校验问答数量
        :type WaitVerifyTotal: str
        :param _NotAcceptedTotal: 未采纳问答数量
        :type NotAcceptedTotal: str
        :param _AcceptedTotal: 已采纳问答数量
        :type AcceptedTotal: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _List: 问答详情
        :type List: list of ListQaItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._WaitVerifyTotal = None
        self._NotAcceptedTotal = None
        self._AcceptedTotal = None
        self._PageNumber = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""问答数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def WaitVerifyTotal(self):
        r"""待校验问答数量
        :rtype: str
        """
        return self._WaitVerifyTotal

    @WaitVerifyTotal.setter
    def WaitVerifyTotal(self, WaitVerifyTotal):
        self._WaitVerifyTotal = WaitVerifyTotal

    @property
    def NotAcceptedTotal(self):
        r"""未采纳问答数量
        :rtype: str
        """
        return self._NotAcceptedTotal

    @NotAcceptedTotal.setter
    def NotAcceptedTotal(self, NotAcceptedTotal):
        self._NotAcceptedTotal = NotAcceptedTotal

    @property
    def AcceptedTotal(self):
        r"""已采纳问答数量
        :rtype: str
        """
        return self._AcceptedTotal

    @AcceptedTotal.setter
    def AcceptedTotal(self, AcceptedTotal):
        self._AcceptedTotal = AcceptedTotal

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def List(self):
        r"""问答详情
        :rtype: list of ListQaItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._WaitVerifyTotal = params.get("WaitVerifyTotal")
        self._NotAcceptedTotal = params.get("NotAcceptedTotal")
        self._AcceptedTotal = params.get("AcceptedTotal")
        self._PageNumber = params.get("PageNumber")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListQaItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQaItem(AbstractModel):
    r"""问答详情数据

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _Source: 来源
        :type Source: int
        :param _SourceDesc: 来源描述
        :type SourceDesc: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 状态
        :type Status: int
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsAllowEdit: 是否允许编辑
        :type IsAllowEdit: bool
        :param _IsAllowDelete: 是否允许删除
        :type IsAllowDelete: bool
        :param _IsAllowAccept: 是否允许校验
        :type IsAllowAccept: bool
        :param _FileName: 文档名称
        :type FileName: str
        :param _FileType: 文档类型
        :type FileType: str
        :param _QaCharSize: 问答字符数
        :type QaCharSize: str
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签
        :type AttrLabels: list of AttrLabel
        :param _SimilarQuestionNum: 相似问个数
        :type SimilarQuestionNum: int
        :param _SimilarQuestionTips: 返回问答关联的相似问,联动搜索,仅展示一条
        :type SimilarQuestionTips: str
        :param _IsDisabled: 问答是否停用，false:未停用，ture:已停用
        :type IsDisabled: bool
        :param _StaffName: 员工名称
        :type StaffName: str
        :param _EnableScope: 问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableScope: int
        :param _DocEnableScope: 问答关联的文档生效域
        :type DocEnableScope: int
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._DocBizId = None
        self._CreateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None
        self._IsAllowAccept = None
        self._FileName = None
        self._FileType = None
        self._QaCharSize = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._AttrRange = None
        self._AttrLabels = None
        self._SimilarQuestionNum = None
        self._SimilarQuestionTips = None
        self._IsDisabled = None
        self._StaffName = None
        self._EnableScope = None
        self._DocEnableScope = None

    @property
    def QaBizId(self):
        r"""问答ID
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

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
    def Answer(self):
        r"""答案
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Source(self):
        r"""来源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        r"""来源描述
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

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
    def IsAllowEdit(self):
        r"""是否允许编辑
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        r"""是否允许删除
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowAccept(self):
        r"""是否允许校验
        :rtype: bool
        """
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def FileName(self):
        r"""文档名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文档类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def QaCharSize(self):
        r"""问答字符数
        :rtype: str
        """
        return self._QaCharSize

    @QaCharSize.setter
    def QaCharSize(self, QaCharSize):
        self._QaCharSize = QaCharSize

    @property
    def ExpireStart(self):
        r"""有效开始时间，unix时间戳
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，unix时间戳，0代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def AttrRange(self):
        r"""属性标签适用范围 1：全部，2：按条件
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""属性标签
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def SimilarQuestionNum(self):
        r"""相似问个数
        :rtype: int
        """
        return self._SimilarQuestionNum

    @SimilarQuestionNum.setter
    def SimilarQuestionNum(self, SimilarQuestionNum):
        self._SimilarQuestionNum = SimilarQuestionNum

    @property
    def SimilarQuestionTips(self):
        r"""返回问答关联的相似问,联动搜索,仅展示一条
        :rtype: str
        """
        return self._SimilarQuestionTips

    @SimilarQuestionTips.setter
    def SimilarQuestionTips(self, SimilarQuestionTips):
        self._SimilarQuestionTips = SimilarQuestionTips

    @property
    def IsDisabled(self):
        r"""问答是否停用，false:未停用，ture:已停用
        :rtype: bool
        """
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled

    @property
    def StaffName(self):
        r"""员工名称
        :rtype: str
        """
        return self._StaffName

    @StaffName.setter
    def StaffName(self, StaffName):
        self._StaffName = StaffName

    @property
    def EnableScope(self):
        r"""问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope

    @property
    def DocEnableScope(self):
        r"""问答关联的文档生效域
        :rtype: int
        """
        return self._DocEnableScope

    @DocEnableScope.setter
    def DocEnableScope(self, DocEnableScope):
        self._DocEnableScope = DocEnableScope


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DocBizId = params.get("DocBizId")
        self._CreateTime = params.get("CreateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._QaCharSize = params.get("QaCharSize")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._SimilarQuestionNum = params.get("SimilarQuestionNum")
        self._SimilarQuestionTips = params.get("SimilarQuestionTips")
        self._IsDisabled = params.get("IsDisabled")
        self._StaffName = params.get("StaffName")
        self._EnableScope = params.get("EnableScope")
        self._DocEnableScope = params.get("DocEnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReferShareKnowledgeRequest(AbstractModel):
    r"""ListReferShareKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用业务id
        :type AppBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._AppBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppBizId(self):
        r"""应用业务id
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReferShareKnowledgeResponse(AbstractModel):
    r"""ListReferShareKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 共享知识库信息列表
        :type List: list of KnowledgeBaseInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""共享知识库信息列表
        :rtype: list of KnowledgeBaseInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = KnowledgeBaseInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListRejectedQuestionPreviewRequest(AbstractModel):
    r"""ListRejectedQuestionPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 每页数量（取值范围为1-200）
        :type PageSize: int
        :param _Query: 查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :type Query: str
        :param _ReleaseBizId: 发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :type ReleaseBizId: str
        :param _Actions: 状态(1新增2更新3删除)
        :type Actions: list of int non-negative
        :param _StartTime: 开始时间。Unix 时间戳，单位是秒，默认为空。
        :type StartTime: str
        :param _EndTime: 结束时间。Unix 时间戳，单位是秒，默认为空。
        :type EndTime: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None

    @property
    def BotBizId(self):
        r"""应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（取值范围为1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        r"""发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        r"""状态(1新增2更新3删除)
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        r"""开始时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionPreviewResponse(AbstractModel):
    r"""ListRejectedQuestionPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseRejectedQuestion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""文档数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""文档列表
        :rtype: list of ReleaseRejectedQuestion
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseRejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListRejectedQuestionRequest(AbstractModel):
    r"""ListRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID, 获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 每页数量（取值范围1-200）
        :type PageSize: int
        :param _Query: 查询内容

        :type Query: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def BotBizId(self):
        r"""应用ID, 获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)。
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（取值范围1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容

        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
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
        


class ListRejectedQuestionResponse(AbstractModel):
    r"""ListRejectedQuestion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 拒答问题列表
        :type List: list of RejectedQuestion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""拒答问题列表
        :rtype: list of RejectedQuestion
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseConfigPreviewRequest(AbstractModel):
    r"""ListReleaseConfigPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 每页数量（取值范围为1-200）
        :type PageSize: int
        :param _Query: 查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :type Query: str
        :param _ReleaseBizId: 发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :type ReleaseBizId: str
        :param _Actions: 状态(1新增2更新3删除)
        :type Actions: list of int non-negative
        :param _StartTime: 开始时间。Unix 时间戳，单位是秒，默认为空。
        :type StartTime: str
        :param _EndTime: 结束时间。Unix 时间戳，单位是秒，默认为空。
        :type EndTime: str
        :param _ReleaseStatus: 发布状态(2 待发布 3 发布中 4 已发布 5 发布失败)，默认为空
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        r"""应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（取值范围为1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        r"""发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        r"""状态(1新增2更新3删除)
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        r"""开始时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReleaseStatus(self):
        r"""发布状态(2 待发布 3 发布中 4 已发布 5 发布失败)，默认为空
        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseConfigPreviewResponse(AbstractModel):
    r"""ListReleaseConfigPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数量
        :type Total: str
        :param _List: 配置项列表
        :type List: list of ReleaseConfigs
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""配置项列表
        :rtype: list of ReleaseConfigs
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseConfigs()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseDocPreviewRequest(AbstractModel):
    r"""ListReleaseDocPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 每页数量（取值范围为1-200）
        :type PageSize: int
        :param _Query: 查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :type Query: str
        :param _ReleaseBizId: 发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :type ReleaseBizId: str
        :param _StartTime: 开始时间。Unix 时间戳，单位是秒，默认为空。
        :type StartTime: str
        :param _EndTime: 结束时间。Unix 时间戳，单位是秒，默认为空。
        :type EndTime: str
        :param _Actions: 状态(1新增2修改3删除)，其和ReleaseStatus的区别为： Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据 / 内容本身的发布状态
        :type Actions: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None

    @property
    def BotBizId(self):
        r"""应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（取值范围为1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        r"""发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        r"""开始时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        r"""状态(1新增2修改3删除)，其和ReleaseStatus的区别为： Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据 / 内容本身的发布状态
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseDocPreviewResponse(AbstractModel):
    r"""ListReleaseDocPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseDoc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""文档数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""文档列表
        :rtype: list of ReleaseDoc
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseDoc()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseItem(AbstractModel):
    r"""发布列表详情

    """

    def __init__(self):
        r"""
        :param _ReleaseBizId: 版本ID
        :type ReleaseBizId: str
        :param _Operator: 发布人
        :type Operator: str
        :param _Desc: 发布描述
        :type Desc: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 发布状态，1：待发布，2：发布中，3：发布成功，5：发布失败
        :type Status: int
        :param _StatusDesc: 发布状态描述
        :type StatusDesc: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _SuccessCount: 发布成功数
        :type SuccessCount: int
        :param _FailCount: 发布失败数
        :type FailCount: int
        """
        self._ReleaseBizId = None
        self._Operator = None
        self._Desc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._SuccessCount = None
        self._FailCount = None

    @property
    def ReleaseBizId(self):
        r"""版本ID
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Operator(self):
        r"""发布人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Desc(self):
        r"""发布描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""发布状态，1：待发布，2：发布中，3：发布成功，5：发布失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""发布状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

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
    def SuccessCount(self):
        r"""发布成功数
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        r"""发布失败数
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount


    def _deserialize(self, params):
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Operator = params.get("Operator")
        self._Desc = params.get("Desc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewRequest(AbstractModel):
    r"""ListReleaseQAPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :type BotBizId: str
        :param _PageNumber: 页码（必须大于0）
        :type PageNumber: int
        :param _PageSize: 每页数量（取值范围为1-200）
        :type PageSize: int
        :param _Query: 查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :type Query: str
        :param _ReleaseBizId: 发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :type ReleaseBizId: str
        :param _StartTime: 开始时间。Unix 时间戳，单位是秒，默认为空。
        :type StartTime: str
        :param _EndTime: 结束时间。Unix 时间戳，单位是秒，默认为空。
        :type EndTime: str
        :param _Actions: 状态(1新增2修改3删除)，其和ReleaseStatus的区别为：Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据/内容本身的发布状态
        :type Actions: list of int non-negative
        :param _ReleaseStatus: 发布状态(4发布成功5发布失败)。其和Actions的区别为：Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据/内容本身的发布状态
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        r"""应用ID（获取方法参看如何获取   [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)）
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码（必须大于0）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量（取值范围为1-200）
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容关键字，用于模糊查询，若未提供该参数，默认为查询全部。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        r"""发布单ID（可以通过[ListRelease](https://cloud.tencent.com/document/product/1759/105077)获得）
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        r"""开始时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。Unix 时间戳，单位是秒，默认为空。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        r"""状态(1新增2修改3删除)，其和ReleaseStatus的区别为：Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据/内容本身的发布状态
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def ReleaseStatus(self):
        r"""发布状态(4发布成功5发布失败)。其和Actions的区别为：Actions表示的是对数据/内容的操作状态，ReleaseStatus表示数据/内容本身的发布状态
        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewResponse(AbstractModel):
    r"""ListReleaseQAPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseQA
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""文档数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""文档列表
        :rtype: list of ReleaseQA
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseQA()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseRequest(AbstractModel):
    r"""ListRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseResponse(AbstractModel):
    r"""ListRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 发布列表数量
        :type Total: str
        :param _List: 发布列表
        :type List: list of ListReleaseItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""发布列表数量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""发布列表
        :rtype: list of ListReleaseItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListReleaseItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListSelectDocRequest(AbstractModel):
    r"""ListSelectDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _FileName: 文档名称。可通过文档名称检索支持生成问答的文档，不支持xlsx、xls、csv格式
        :type FileName: str
        :param _Status: 文档状态筛选。文档状态对应码为7 审核中、8 审核失败、10 待发布、11 发布中、12 已发布、13 学习中、14 学习失败 20 已过期。其中仅状态为10 待发布、12 已发布的文档支持生成问答（未填写时默认值为空数组）
        :type Status: list of int
        """
        self._BotBizId = None
        self._FileName = None
        self._Status = None

    @property
    def BotBizId(self):
        r"""应用ID,获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        r"""文档名称。可通过文档名称检索支持生成问答的文档，不支持xlsx、xls、csv格式
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Status(self):
        r"""文档状态筛选。文档状态对应码为7 审核中、8 审核失败、10 待发布、11 发布中、12 已发布、13 学习中、14 学习失败 20 已过期。其中仅状态为10 待发布、12 已发布的文档支持生成问答（未填写时默认值为空数组）
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSelectDocResponse(AbstractModel):
    r"""ListSelectDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 下拉框内容
        :type List: list of Option
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        r"""下拉框内容
        :rtype: list of Option
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Option()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListSharedKnowledgeRequest(AbstractModel):
    r"""ListSharedKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页序号，编码从1开始
        :type PageNumber: int
        :param _PageSize: 分页大小，有效范围为[1,200]
        :type PageSize: int
        :param _Keyword: 搜索关键字
        :type Keyword: str
        :param _KnowledgeTypes: 共享知识库类型，0普通，1公众号
        :type KnowledgeTypes: list of int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._KnowledgeTypes = None

    @property
    def PageNumber(self):
        r"""分页序号，编码从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小，有效范围为[1,200]
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""搜索关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def KnowledgeTypes(self):
        r"""共享知识库类型，0普通，1公众号
        :rtype: list of int
        """
        return self._KnowledgeTypes

    @KnowledgeTypes.setter
    def KnowledgeTypes(self, KnowledgeTypes):
        self._KnowledgeTypes = KnowledgeTypes


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._KnowledgeTypes = params.get("KnowledgeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSharedKnowledgeResponse(AbstractModel):
    r"""ListSharedKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 累计数量
        :type Total: int
        :param _KnowledgeList: 知识库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeList: list of KnowledgeDetailInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._KnowledgeList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""累计数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def KnowledgeList(self):
        r"""知识库列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KnowledgeDetailInfo
        """
        return self._KnowledgeList

    @KnowledgeList.setter
    def KnowledgeList(self, KnowledgeList):
        self._KnowledgeList = KnowledgeList

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
        if params.get("KnowledgeList") is not None:
            self._KnowledgeList = []
            for item in params.get("KnowledgeList"):
                obj = KnowledgeDetailInfo()
                obj._deserialize(item)
                self._KnowledgeList.append(obj)
        self._RequestId = params.get("RequestId")


class ListUnsatisfiedReplyRequest(AbstractModel):
    r"""ListUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _PageNumber: 页码，取值范围：大于0
        :type PageNumber: int
        :param _PageSize: 分页数量，取值范围：大于0
        :type PageSize: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 用户请求(问题或答案)，按关键词检索，可匹配用户问题或答案
        :type Query: str
        :param _Reasons: 按错误类型检索
        :type Reasons: list of str
        :param _Status: 按操作状态检索  0-全部 1-待处理  2-已处理【包括答案纠错，拒答，忽略】，不填时默认值为0
        :type Status: int
        :param _HandlingStatuses: 处理状态 0-待处理 1-已拒答 2-已忽略 3-已添加为新问答 4-已添加为相似问
        :type HandlingStatuses: list of int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._Reasons = None
        self._Status = None
        self._HandlingStatuses = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看如何获取[BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        r"""页码，取值范围：大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页数量，取值范围：大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        r"""用户请求(问题或答案)，按关键词检索，可匹配用户问题或答案
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        r"""按错误类型检索
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def Status(self):
        r"""按操作状态检索  0-全部 1-待处理  2-已处理【包括答案纠错，拒答，忽略】，不填时默认值为0
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def HandlingStatuses(self):
        r"""处理状态 0-待处理 1-已拒答 2-已忽略 3-已添加为新问答 4-已添加为相似问
        :rtype: list of int
        """
        return self._HandlingStatuses

    @HandlingStatuses.setter
    def HandlingStatuses(self, HandlingStatuses):
        self._HandlingStatuses = HandlingStatuses


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        self._Status = params.get("Status")
        self._HandlingStatuses = params.get("HandlingStatuses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUnsatisfiedReplyResponse(AbstractModel):
    r"""ListUnsatisfiedReply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 不满意回复列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of UnsatisfiedReply
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""不满意回复列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UnsatisfiedReply
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UnsatisfiedReply()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsageCallDetailRequest(AbstractModel):
    r"""ListUsageCallDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型标识
        :type ModelName: str
        :param _PageNumber: 页码（从1开始）
        :type PageNumber: int
        :param _PageSize: 分页数量(最大值1000)
        :type PageSize: int
        :param _StartTime: 开始时间(废弃)
        :type StartTime: str
        :param _EndTime: 结束时间(废弃)
        :type EndTime: str
        :param _UinAccount: uin列表
        :type UinAccount: list of str
        :param _AppBizIds: 应用ID列表
        :type AppBizIds: list of str
        :param _CallType: 调用类型列表
        :type CallType: str
        :param _SubScenes: 筛选子场景
        :type SubScenes: list of str
        :param _AppType: 应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :type AppType: str
        :param _BillingTag: 账单明细对应的自定义tag
        :type BillingTag: str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _StatStartTime: 开始时间戳, 单位为秒
        :type StatStartTime: int
        :param _StatEndTime: 开始时间戳, 单位为秒
        :type StatEndTime: int
        """
        self._ModelName = None
        self._PageNumber = None
        self._PageSize = None
        self._StartTime = None
        self._EndTime = None
        self._UinAccount = None
        self._AppBizIds = None
        self._CallType = None
        self._SubScenes = None
        self._AppType = None
        self._BillingTag = None
        self._SpaceId = None
        self._StatStartTime = None
        self._StatEndTime = None

    @property
    def ModelName(self):
        r"""模型标识
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PageNumber(self):
        r"""页码（从1开始）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页数量(最大值1000)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartTime(self):
        r"""开始时间(废弃)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间(废弃)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UinAccount(self):
        r"""uin列表
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def AppBizIds(self):
        r"""应用ID列表
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def CallType(self):
        r"""调用类型列表
        :rtype: str
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def SubScenes(self):
        r"""筛选子场景
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes

    @property
    def AppType(self):
        r"""应用类型(knowledge_qa应用管理， shared_knowlege 共享知识库)
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BillingTag(self):
        r"""账单明细对应的自定义tag
        :rtype: str
        """
        return self._BillingTag

    @BillingTag.setter
    def BillingTag(self, BillingTag):
        self._BillingTag = BillingTag

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
    def StatStartTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatStartTime

    @StatStartTime.setter
    def StatStartTime(self, StatStartTime):
        self._StatStartTime = StatStartTime

    @property
    def StatEndTime(self):
        r"""开始时间戳, 单位为秒
        :rtype: int
        """
        return self._StatEndTime

    @StatEndTime.setter
    def StatEndTime(self, StatEndTime):
        self._StatEndTime = StatEndTime


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UinAccount = params.get("UinAccount")
        self._AppBizIds = params.get("AppBizIds")
        self._CallType = params.get("CallType")
        self._SubScenes = params.get("SubScenes")
        self._AppType = params.get("AppType")
        self._BillingTag = params.get("BillingTag")
        self._SpaceId = params.get("SpaceId")
        self._StatStartTime = params.get("StatStartTime")
        self._StatEndTime = params.get("StatEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsageCallDetailResponse(AbstractModel):
    r"""ListUsageCallDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 列表总数
        :type Total: int
        :param _List: 列表
        :type List: list of CallDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        r"""列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""列表
        :rtype: list of CallDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CallDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListWorkflowRunsRequest(AbstractModel):
    r"""ListWorkflowRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type AppBizId: str
        :param _PageSize: 每页数量(取值范围1-200)
        :type PageSize: int
        :param _RunEnv: 运行环境。0: 测试环境； 1: 正式环境
        :type RunEnv: int
        :param _Page: 页码(必须大于0)
        :type Page: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._AppBizId = None
        self._PageSize = None
        self._RunEnv = None
        self._Page = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppBizId(self):
        r"""应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def PageSize(self):
        r"""每页数量(取值范围1-200)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def RunEnv(self):
        r"""运行环境。0: 测试环境； 1: 正式环境
        :rtype: int
        """
        return self._RunEnv

    @RunEnv.setter
    def RunEnv(self, RunEnv):
        self._RunEnv = RunEnv

    @property
    def Page(self):
        r"""页码(必须大于0)
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._PageSize = params.get("PageSize")
        self._RunEnv = params.get("RunEnv")
        self._Page = params.get("Page")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowRunsResponse(AbstractModel):
    r"""ListWorkflowRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _WorkflowRuns: 工作流运行列表
        :type WorkflowRuns: list of WorkflowRunBase
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._WorkflowRuns = None
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
    def WorkflowRuns(self):
        r"""工作流运行列表
        :rtype: list of WorkflowRunBase
        """
        return self._WorkflowRuns

    @WorkflowRuns.setter
    def WorkflowRuns(self, WorkflowRuns):
        self._WorkflowRuns = WorkflowRuns

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
        if params.get("WorkflowRuns") is not None:
            self._WorkflowRuns = []
            for item in params.get("WorkflowRuns"):
                obj = WorkflowRunBase()
                obj._deserialize(item)
                self._WorkflowRuns.append(obj)
        self._RequestId = params.get("RequestId")


class ModelInfo(AbstractModel):
    r"""模型信息

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _ModelDesc: 模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelDesc: str
        :param _AliasName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _ResourceStatus: 资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        :param _PromptWordsLimit: 提示词内容字符限制
注意：此字段可能返回 null，表示取不到有效值。
        :type PromptWordsLimit: str
        :param _TopP: 通过核心采样控制内容生成的多样性，较高的Top P值会导致生成更多样的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type TopP: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _Temperature: 温度控制随机性
注意：此字段可能返回 null，表示取不到有效值。
        :type Temperature: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _MaxTokens: 最多能生成的token数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTokens: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _Source: 模型来源 Hunyuan：腾讯混元大模型,Industry：腾讯云行业大模型,Experience：新模型体验,Custom自定义模型
        :type Source: str
        :param _Icon: 模型图标
        :type Icon: str
        :param _IsFree: 是否免费
        :type IsFree: bool
        :param _InputLenLimit: 模型对话框可输入的上限
注意：此字段可能返回 null，表示取不到有效值。
        :type InputLenLimit: int
        :param _SupportWorkflowStatus: 支持工作流的类型 0:模型不支持; 1: 模型支持工作流； 2： 模型支持效果不佳；
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportWorkflowStatus: int
        :param _ModelCategory: 模型类别 generate：生成模型，thought：思考模型
        :type ModelCategory: str
        :param _IsDefault: 是否默认模型
        :type IsDefault: bool
        :param _RoleLenLimit: 角色提示词输入长度限制
        :type RoleLenLimit: int
        :param _IsExclusive: 是否专属并发模型
        :type IsExclusive: bool
        :param _SupportAiCallStatus: 模型支持智能通话效果
        :type SupportAiCallStatus: int
        :param _Concurrency: 专属并发数
        :type Concurrency: int
        :param _ModelTags: 模型标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelTags: list of str
        :param _ModelParams: 模型超参定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelParams: list of ModelParameter
        :param _ProviderName: 提供商名称
        :type ProviderName: str
        :param _ProviderAliasName: 提供商别名
        :type ProviderAliasName: str
        :param _ProviderType: 提供商类型 Self:提供商，Custom：自定义模型提供商，Third：第三方模型提供商
        :type ProviderType: str
        :param _IsCloseModelParams: 是否关闭模型超参
        :type IsCloseModelParams: bool
        :param _IsDeepThinking: 是否支持深度思考
        :type IsDeepThinking: bool
        """
        self._ModelName = None
        self._ModelDesc = None
        self._AliasName = None
        self._ResourceStatus = None
        self._PromptWordsLimit = None
        self._TopP = None
        self._Temperature = None
        self._MaxTokens = None
        self._Source = None
        self._Icon = None
        self._IsFree = None
        self._InputLenLimit = None
        self._SupportWorkflowStatus = None
        self._ModelCategory = None
        self._IsDefault = None
        self._RoleLenLimit = None
        self._IsExclusive = None
        self._SupportAiCallStatus = None
        self._Concurrency = None
        self._ModelTags = None
        self._ModelParams = None
        self._ProviderName = None
        self._ProviderAliasName = None
        self._ProviderType = None
        self._IsCloseModelParams = None
        self._IsDeepThinking = None

    @property
    def ModelName(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelDesc(self):
        r"""模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelDesc

    @ModelDesc.setter
    def ModelDesc(self, ModelDesc):
        self._ModelDesc = ModelDesc

    @property
    def AliasName(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def ResourceStatus(self):
        r"""资源状态 1：资源可用；2：资源已用尽
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def PromptWordsLimit(self):
        r"""提示词内容字符限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PromptWordsLimit

    @PromptWordsLimit.setter
    def PromptWordsLimit(self, PromptWordsLimit):
        self._PromptWordsLimit = PromptWordsLimit

    @property
    def TopP(self):
        r"""通过核心采样控制内容生成的多样性，较高的Top P值会导致生成更多样的内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        r"""温度控制随机性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def MaxTokens(self):
        r"""最多能生成的token数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def Source(self):
        r"""模型来源 Hunyuan：腾讯混元大模型,Industry：腾讯云行业大模型,Experience：新模型体验,Custom自定义模型
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Icon(self):
        r"""模型图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def IsFree(self):
        r"""是否免费
        :rtype: bool
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def InputLenLimit(self):
        r"""模型对话框可输入的上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InputLenLimit

    @InputLenLimit.setter
    def InputLenLimit(self, InputLenLimit):
        self._InputLenLimit = InputLenLimit

    @property
    def SupportWorkflowStatus(self):
        r"""支持工作流的类型 0:模型不支持; 1: 模型支持工作流； 2： 模型支持效果不佳；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SupportWorkflowStatus

    @SupportWorkflowStatus.setter
    def SupportWorkflowStatus(self, SupportWorkflowStatus):
        self._SupportWorkflowStatus = SupportWorkflowStatus

    @property
    def ModelCategory(self):
        r"""模型类别 generate：生成模型，thought：思考模型
        :rtype: str
        """
        return self._ModelCategory

    @ModelCategory.setter
    def ModelCategory(self, ModelCategory):
        self._ModelCategory = ModelCategory

    @property
    def IsDefault(self):
        r"""是否默认模型
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def RoleLenLimit(self):
        r"""角色提示词输入长度限制
        :rtype: int
        """
        return self._RoleLenLimit

    @RoleLenLimit.setter
    def RoleLenLimit(self, RoleLenLimit):
        self._RoleLenLimit = RoleLenLimit

    @property
    def IsExclusive(self):
        r"""是否专属并发模型
        :rtype: bool
        """
        return self._IsExclusive

    @IsExclusive.setter
    def IsExclusive(self, IsExclusive):
        self._IsExclusive = IsExclusive

    @property
    def SupportAiCallStatus(self):
        r"""模型支持智能通话效果
        :rtype: int
        """
        return self._SupportAiCallStatus

    @SupportAiCallStatus.setter
    def SupportAiCallStatus(self, SupportAiCallStatus):
        self._SupportAiCallStatus = SupportAiCallStatus

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
    def ModelTags(self):
        r"""模型标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ModelTags

    @ModelTags.setter
    def ModelTags(self, ModelTags):
        self._ModelTags = ModelTags

    @property
    def ModelParams(self):
        r"""模型超参定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ModelParameter
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams

    @property
    def ProviderName(self):
        r"""提供商名称
        :rtype: str
        """
        return self._ProviderName

    @ProviderName.setter
    def ProviderName(self, ProviderName):
        self._ProviderName = ProviderName

    @property
    def ProviderAliasName(self):
        r"""提供商别名
        :rtype: str
        """
        return self._ProviderAliasName

    @ProviderAliasName.setter
    def ProviderAliasName(self, ProviderAliasName):
        self._ProviderAliasName = ProviderAliasName

    @property
    def ProviderType(self):
        r"""提供商类型 Self:提供商，Custom：自定义模型提供商，Third：第三方模型提供商
        :rtype: str
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IsCloseModelParams(self):
        r"""是否关闭模型超参
        :rtype: bool
        """
        return self._IsCloseModelParams

    @IsCloseModelParams.setter
    def IsCloseModelParams(self, IsCloseModelParams):
        self._IsCloseModelParams = IsCloseModelParams

    @property
    def IsDeepThinking(self):
        r"""是否支持深度思考
        :rtype: bool
        """
        return self._IsDeepThinking

    @IsDeepThinking.setter
    def IsDeepThinking(self, IsDeepThinking):
        self._IsDeepThinking = IsDeepThinking


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._ModelDesc = params.get("ModelDesc")
        self._AliasName = params.get("AliasName")
        self._ResourceStatus = params.get("ResourceStatus")
        self._PromptWordsLimit = params.get("PromptWordsLimit")
        if params.get("TopP") is not None:
            self._TopP = ModelParameter()
            self._TopP._deserialize(params.get("TopP"))
        if params.get("Temperature") is not None:
            self._Temperature = ModelParameter()
            self._Temperature._deserialize(params.get("Temperature"))
        if params.get("MaxTokens") is not None:
            self._MaxTokens = ModelParameter()
            self._MaxTokens._deserialize(params.get("MaxTokens"))
        self._Source = params.get("Source")
        self._Icon = params.get("Icon")
        self._IsFree = params.get("IsFree")
        self._InputLenLimit = params.get("InputLenLimit")
        self._SupportWorkflowStatus = params.get("SupportWorkflowStatus")
        self._ModelCategory = params.get("ModelCategory")
        self._IsDefault = params.get("IsDefault")
        self._RoleLenLimit = params.get("RoleLenLimit")
        self._IsExclusive = params.get("IsExclusive")
        self._SupportAiCallStatus = params.get("SupportAiCallStatus")
        self._Concurrency = params.get("Concurrency")
        self._ModelTags = params.get("ModelTags")
        if params.get("ModelParams") is not None:
            self._ModelParams = []
            for item in params.get("ModelParams"):
                obj = ModelParameter()
                obj._deserialize(item)
                self._ModelParams.append(obj)
        self._ProviderName = params.get("ProviderName")
        self._ProviderAliasName = params.get("ProviderAliasName")
        self._ProviderType = params.get("ProviderType")
        self._IsCloseModelParams = params.get("IsCloseModelParams")
        self._IsDeepThinking = params.get("IsDeepThinking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelParameter(AbstractModel):
    r"""模型参数范围

    """

    def __init__(self):
        r"""
        :param _Default: 默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: float
        :param _Min: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: float
        :param _Max: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: float
        :param _Name: 超参名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Default = None
        self._Min = None
        self._Max = None
        self._Name = None

    @property
    def Default(self):
        r"""默认值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Min(self):
        r"""最小值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""最大值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Name(self):
        r"""超参名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Name = params.get("Name")
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
        :param _Temperature: 温度
        :type Temperature: float
        :param _TopP: Top_P
        :type TopP: float
        :param _Seed: 随机种子
        :type Seed: int
        :param _PresencePenalty: 存在惩罚
        :type PresencePenalty: float
        :param _FrequencyPenalty: 频率惩罚
        :type FrequencyPenalty: float
        :param _RepetitionPenalty: 重复惩罚
        :type RepetitionPenalty: float
        :param _MaxTokens: 最大输出长度
        :type MaxTokens: int
        :param _StopSequences: 停止序列
        :type StopSequences: list of str
        :param _ReplyFormat: 输出格式
        :type ReplyFormat: str
        """
        self._Temperature = None
        self._TopP = None
        self._Seed = None
        self._PresencePenalty = None
        self._FrequencyPenalty = None
        self._RepetitionPenalty = None
        self._MaxTokens = None
        self._StopSequences = None
        self._ReplyFormat = None

    @property
    def Temperature(self):
        r"""温度
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        r"""Top_P
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Seed(self):
        r"""随机种子
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def PresencePenalty(self):
        r"""存在惩罚
        :rtype: float
        """
        return self._PresencePenalty

    @PresencePenalty.setter
    def PresencePenalty(self, PresencePenalty):
        self._PresencePenalty = PresencePenalty

    @property
    def FrequencyPenalty(self):
        r"""频率惩罚
        :rtype: float
        """
        return self._FrequencyPenalty

    @FrequencyPenalty.setter
    def FrequencyPenalty(self, FrequencyPenalty):
        self._FrequencyPenalty = FrequencyPenalty

    @property
    def RepetitionPenalty(self):
        r"""重复惩罚
        :rtype: float
        """
        return self._RepetitionPenalty

    @RepetitionPenalty.setter
    def RepetitionPenalty(self, RepetitionPenalty):
        self._RepetitionPenalty = RepetitionPenalty

    @property
    def MaxTokens(self):
        r"""最大输出长度
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def StopSequences(self):
        r"""停止序列
        :rtype: list of str
        """
        return self._StopSequences

    @StopSequences.setter
    def StopSequences(self, StopSequences):
        self._StopSequences = StopSequences

    @property
    def ReplyFormat(self):
        r"""输出格式
        :rtype: str
        """
        return self._ReplyFormat

    @ReplyFormat.setter
    def ReplyFormat(self, ReplyFormat):
        self._ReplyFormat = ReplyFormat


    def _deserialize(self, params):
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._Seed = params.get("Seed")
        self._PresencePenalty = params.get("PresencePenalty")
        self._FrequencyPenalty = params.get("FrequencyPenalty")
        self._RepetitionPenalty = params.get("RepetitionPenalty")
        self._MaxTokens = params.get("MaxTokens")
        self._StopSequences = params.get("StopSequences")
        self._ReplyFormat = params.get("ReplyFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    r"""ModifyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用 ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classify-知识标签提取
        :type AppType: str
        :param _BaseConfig: 应用基础配置
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._AppBizId = None
        self._AppType = None
        self._BaseConfig = None
        self._AppConfig = None
        self._LoginSubAccountUin = None

    @property
    def AppBizId(self):
        r"""应用 ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        r"""应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classify-知识标签提取
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        r"""应用基础配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def AppConfig(self):
        r"""应用配置
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        """
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
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
        :param _AppBizId: 应用App
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppBizId(self):
        r"""应用App
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def UpdateTime(self):
        r"""更新时间
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
        self._AppBizId = params.get("AppBizId")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ModifyAttributeLabelRequest(AbstractModel):
    r"""ModifyAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _AttributeBizId: 标签ID
        :type AttributeBizId: str
        :param _AttrName: 标签名称
        :type AttrName: str
        :param _AttrKey: 标签标识 （已作废）
        :type AttrKey: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _DeleteLabelBizIds: 删除的标签值
        :type DeleteLabelBizIds: list of str
        :param _Labels: 新增或编辑的标签
        :type Labels: list of AttributeLabel
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._AttrName = None
        self._AttrKey = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._DeleteLabelBizIds = None
        self._Labels = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        r"""标签ID
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrName(self):
        r"""标签名称
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def AttrKey(self):
        r"""标签标识 （已作废）
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def DeleteLabelBizIds(self):
        r"""删除的标签值
        :rtype: list of str
        """
        return self._DeleteLabelBizIds

    @DeleteLabelBizIds.setter
    def DeleteLabelBizIds(self, DeleteLabelBizIds):
        self._DeleteLabelBizIds = DeleteLabelBizIds

    @property
    def Labels(self):
        r"""新增或编辑的标签
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrName = params.get("AttrName")
        self._AttrKey = params.get("AttrKey")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._DeleteLabelBizIds = params.get("DeleteLabelBizIds")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAttributeLabelResponse(AbstractModel):
    r"""ModifyAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Labels: 标签ID与名称
        :type Labels: list of AttributeLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Labels = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Labels(self):
        r"""标签ID与名称
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

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
        self._TaskId = params.get("TaskId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyDocAttrRangeRequest(AbstractModel):
    r"""ModifyDocAttrRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizIds: 文档ID
        :type DocBizIds: list of str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._DocBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        r"""文档ID
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def AttrRange(self):
        r"""属性标签适用范围 1：全部，2：按条件
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""属性标签引用
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocAttrRangeResponse(AbstractModel):
    r"""ModifyDocAttrRange返回参数结构体

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


class ModifyDocCateRequest(AbstractModel):
    r"""ModifyDocCate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Name: 分类名称

        :type Name: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._Name = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Name(self):
        r"""分类名称

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Name = params.get("Name")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocCateResponse(AbstractModel):
    r"""ModifyDocCate返回参数结构体

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


class ModifyDocRequest(AbstractModel):
    r"""ModifyDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看[如何获取   BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _IsRefer: 是否引用链接
        :type IsRefer: bool
        :param _AttrRange: 标签适用范围，1:全部，2:按条件。默认为1。
        :type AttrRange: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _AttrLabels: 关联的标签
        :type AttrLabels: list of AttrLabelRefer
        :param _WebUrl: 网页(或自定义链接)地址
        :type WebUrl: str
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :type ReferUrlType: int
        :param _ExpireStart: 有效开始时间，单位为unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，单位为unix时间戳，默认值为0代表永久有效
        :type ExpireEnd: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _IsDownload: 是否可下载，IsRefer为true并且ReferUrlType为0时，该值才有意义
        :type IsDownload: bool
        :param _ModifyTypes: 需要修改的内容类型  0  无效 1 更新文档cos信息 2 更新文档引用信息 3 更新文档刷新频率 4 腾讯文档刷新
        :type ModifyTypes: list of int non-negative
        :param _UpdatePeriodInfo: 文档更新频率
        :type UpdatePeriodInfo: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        :param _SplitRule: 自定义切分规则
        :type SplitRule: str
        :param _EnableScope: 文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        """
        self._BotBizId = None
        self._DocBizId = None
        self._IsRefer = None
        self._AttrRange = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttrLabels = None
        self._WebUrl = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._CateBizId = None
        self._IsDownload = None
        self._ModifyTypes = None
        self._UpdatePeriodInfo = None
        self._SplitRule = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看[如何获取   BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def IsRefer(self):
        r"""是否引用链接
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def AttrRange(self):
        r"""标签适用范围，1:全部，2:按条件。默认为1。
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttrLabels(self):
        r"""关联的标签
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def WebUrl(self):
        r"""网页(或自定义链接)地址
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ReferUrlType(self):
        r"""外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        r"""有效开始时间，单位为unix时间戳
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，单位为unix时间戳，默认值为0代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsDownload(self):
        r"""是否可下载，IsRefer为true并且ReferUrlType为0时，该值才有意义
        :rtype: bool
        """
        return self._IsDownload

    @IsDownload.setter
    def IsDownload(self, IsDownload):
        self._IsDownload = IsDownload

    @property
    def ModifyTypes(self):
        r"""需要修改的内容类型  0  无效 1 更新文档cos信息 2 更新文档引用信息 3 更新文档刷新频率 4 腾讯文档刷新
        :rtype: list of int non-negative
        """
        return self._ModifyTypes

    @ModifyTypes.setter
    def ModifyTypes(self, ModifyTypes):
        self._ModifyTypes = ModifyTypes

    @property
    def UpdatePeriodInfo(self):
        r"""文档更新频率
        :rtype: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        """
        return self._UpdatePeriodInfo

    @UpdatePeriodInfo.setter
    def UpdatePeriodInfo(self, UpdatePeriodInfo):
        self._UpdatePeriodInfo = UpdatePeriodInfo

    @property
    def SplitRule(self):
        r"""自定义切分规则
        :rtype: str
        """
        return self._SplitRule

    @SplitRule.setter
    def SplitRule(self, SplitRule):
        self._SplitRule = SplitRule

    @property
    def EnableScope(self):
        r"""文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._IsRefer = params.get("IsRefer")
        self._AttrRange = params.get("AttrRange")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._WebUrl = params.get("WebUrl")
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._CateBizId = params.get("CateBizId")
        self._IsDownload = params.get("IsDownload")
        self._ModifyTypes = params.get("ModifyTypes")
        if params.get("UpdatePeriodInfo") is not None:
            self._UpdatePeriodInfo = UpdatePeriodInfo()
            self._UpdatePeriodInfo._deserialize(params.get("UpdatePeriodInfo"))
        self._SplitRule = params.get("SplitRule")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocResponse(AbstractModel):
    r"""ModifyDoc返回参数结构体

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


class ModifyQAAttrRangeRequest(AbstractModel):
    r"""ModifyQAAttrRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: 问答ID
        :type QaBizIds: list of str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        r"""问答ID
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def AttrRange(self):
        r"""属性标签适用范围 1：全部，2：按条件
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""属性标签引用
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAAttrRangeResponse(AbstractModel):
    r"""ModifyQAAttrRange返回参数结构体

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


class ModifyQACateRequest(AbstractModel):
    r"""ModifyQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Name: 分类名称

        :type Name: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._Name = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Name(self):
        r"""分类名称

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CateBizId(self):
        r"""分类业务ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Name = params.get("Name")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQACateResponse(AbstractModel):
    r"""ModifyQACate返回参数结构体

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


class ModifyQARequest(AbstractModel):
    r"""ModifyQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
若要操作共享知识库，传KnowledgeBizId
        :type BotBizId: str
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _AttrRange: 标签适用范围 1：全部，2：按条件
默认值：当没有属性标签，labelRefers为空时，默认值为1
有属性标签，labelRefers不为空，默认值为2
        :type AttrRange: int
        :param _AttrLabels: 标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _ExpireStart: 有效开始时间，单位是unix时间戳，默认值为0，代表永久有效
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，单位是unix时间戳，默认值为0，代表永久有效
        :type ExpireEnd: str
        :param _SimilarQuestionModify: 相似问修改信息(相似问没有修改则不传)
        :type SimilarQuestionModify: :class:`tencentcloud.lke.v20231130.models.SimilarQuestionModify`
        :param _QuestionDesc: 问题描述
        :type QuestionDesc: str
        :param _EnableScope: 问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        """
        self._BotBizId = None
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._AttrRange = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestionModify = None
        self._QuestionDesc = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID
若要操作共享知识库，传KnowledgeBizId
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizId(self):
        r"""问答ID
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

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
    def Answer(self):
        r"""答案
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        r"""自定义参数
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrRange(self):
        r"""标签适用范围 1：全部，2：按条件
默认值：当没有属性标签，labelRefers为空时，默认值为1
有属性标签，labelRefers不为空，默认值为2
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        r"""标签引用
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        r"""有效开始时间，单位是unix时间戳，默认值为0，代表永久有效
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，单位是unix时间戳，默认值为0，代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestionModify(self):
        r"""相似问修改信息(相似问没有修改则不传)
        :rtype: :class:`tencentcloud.lke.v20231130.models.SimilarQuestionModify`
        """
        return self._SimilarQuestionModify

    @SimilarQuestionModify.setter
    def SimilarQuestionModify(self, SimilarQuestionModify):
        self._SimilarQuestionModify = SimilarQuestionModify

    @property
    def QuestionDesc(self):
        r"""问题描述
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc

    @property
    def EnableScope(self):
        r"""问答生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        if params.get("SimilarQuestionModify") is not None:
            self._SimilarQuestionModify = SimilarQuestionModify()
            self._SimilarQuestionModify._deserialize(params.get("SimilarQuestionModify"))
        self._QuestionDesc = params.get("QuestionDesc")
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAResponse(AbstractModel):
    r"""ModifyQA返回参数结构体

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


class ModifyRejectedQuestionRequest(AbstractModel):
    r"""ModifyRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _Question: 拒答问题


        :type Question: str
        :param _RejectedBizId: 拒答问题来源的数据源唯一id, 通过[ListRejectedQuestion](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListRejectedQuestion)接口获取



        :type RejectedBizId: str
        """
        self._BotBizId = None
        self._Question = None
        self._RejectedBizId = None

    @property
    def BotBizId(self):
        r"""应用ID, 获取方法参看如何获取 [BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        r"""拒答问题


        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def RejectedBizId(self):
        r"""拒答问题来源的数据源唯一id, 通过[ListRejectedQuestion](https://capi.woa.com/api/detail?product=lke&version=2023-11-30&action=ListRejectedQuestion)接口获取



        :rtype: str
        """
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._RejectedBizId = params.get("RejectedBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRejectedQuestionResponse(AbstractModel):
    r"""ModifyRejectedQuestion返回参数结构体

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


class MsgFileInfo(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 文档大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _FileUrl: 文档URL
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param _FileType: 文档类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _DocId: 文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None

    @property
    def FileName(self):
        r"""文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""文档大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        r"""文档URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        r"""文档类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        r"""文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecord(AbstractModel):
    r"""消息详情

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _SessionId: 当前记录所对应的 Session ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _RelatedRecordId: 关联记录ID
        :type RelatedRecordId: str
        :param _IsFromSelf: 是否来自自己
        :type IsFromSelf: bool
        :param _FromName: 发送者名称
        :type FromName: str
        :param _FromAvatar: 发送者头像
        :type FromAvatar: str
        :param _Timestamp: 时间戳
        :type Timestamp: str
        :param _HasRead: 是否已读
        :type HasRead: bool
        :param _Score: 评价
        :type Score: int
        :param _CanRating: 是否评分
        :type CanRating: bool
        :param _CanFeedback: 是否展示反馈按钮
注意：此字段可能返回 null，表示取不到有效值。
        :type CanFeedback: bool
        :param _Type: 记录类型
        :type Type: int
        :param _References: 引用来源
        :type References: list of MsgRecordReference
        :param _Reasons: 评价原因
        :type Reasons: list of str
        :param _IsLlmGenerated: 是否大模型
        :type IsLlmGenerated: bool
        :param _ImageUrls: 图片链接，可公有读
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrls: list of str
        :param _TokenStat: 当次 token 统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenStat: :class:`tencentcloud.lke.v20231130.models.TokenStat`
        :param _ReplyMethod: 回复方式
1:大模型直接回复;
2:保守回复, 未知问题回复;
3:拒答问题回复;
4:敏感回复;
5:问答对直接回复, 已采纳问答对优先回复;
6:欢迎语回复;
7:并发超限回复;
8:全局干预知识;
9:任务流程过程回复, 当历史记录中 task_flow.type = 0 时, 为大模型回复;
10:任务流程答案回复;
11:搜索引擎回复;
12:知识润色后回复;
13:图片理解回复;
14:实时文档回复;
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyMethod: int
        :param _OptionCards: 选项卡, 用于多轮对话
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionCards: list of str
        :param _TaskFlow: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlow: :class:`tencentcloud.lke.v20231130.models.TaskFlowInfo`
        :param _FileInfos: 用户传入的文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of FileInfo
        :param _QuoteInfos: 参考来源引用位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type QuoteInfos: list of QuoteInfo
        :param _AgentThought: Agent的思考过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentThought: :class:`tencentcloud.lke.v20231130.models.AgentThought`
        :param _ExtraInfo: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.lke.v20231130.models.ExtraInfo`
        :param _WorkFlow: 工作流信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkFlow: :class:`tencentcloud.lke.v20231130.models.WorkflowInfo`
        """
        self._Content = None
        self._SessionId = None
        self._RecordId = None
        self._RelatedRecordId = None
        self._IsFromSelf = None
        self._FromName = None
        self._FromAvatar = None
        self._Timestamp = None
        self._HasRead = None
        self._Score = None
        self._CanRating = None
        self._CanFeedback = None
        self._Type = None
        self._References = None
        self._Reasons = None
        self._IsLlmGenerated = None
        self._ImageUrls = None
        self._TokenStat = None
        self._ReplyMethod = None
        self._OptionCards = None
        self._TaskFlow = None
        self._FileInfos = None
        self._QuoteInfos = None
        self._AgentThought = None
        self._ExtraInfo = None
        self._WorkFlow = None

    @property
    def Content(self):
        r"""内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SessionId(self):
        r"""当前记录所对应的 Session ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
    def RelatedRecordId(self):
        r"""关联记录ID
        :rtype: str
        """
        return self._RelatedRecordId

    @RelatedRecordId.setter
    def RelatedRecordId(self, RelatedRecordId):
        self._RelatedRecordId = RelatedRecordId

    @property
    def IsFromSelf(self):
        r"""是否来自自己
        :rtype: bool
        """
        return self._IsFromSelf

    @IsFromSelf.setter
    def IsFromSelf(self, IsFromSelf):
        self._IsFromSelf = IsFromSelf

    @property
    def FromName(self):
        r"""发送者名称
        :rtype: str
        """
        return self._FromName

    @FromName.setter
    def FromName(self, FromName):
        self._FromName = FromName

    @property
    def FromAvatar(self):
        r"""发送者头像
        :rtype: str
        """
        return self._FromAvatar

    @FromAvatar.setter
    def FromAvatar(self, FromAvatar):
        self._FromAvatar = FromAvatar

    @property
    def Timestamp(self):
        r"""时间戳
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def HasRead(self):
        r"""是否已读
        :rtype: bool
        """
        return self._HasRead

    @HasRead.setter
    def HasRead(self, HasRead):
        self._HasRead = HasRead

    @property
    def Score(self):
        r"""评价
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def CanRating(self):
        r"""是否评分
        :rtype: bool
        """
        return self._CanRating

    @CanRating.setter
    def CanRating(self, CanRating):
        self._CanRating = CanRating

    @property
    def CanFeedback(self):
        r"""是否展示反馈按钮
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanFeedback

    @CanFeedback.setter
    def CanFeedback(self, CanFeedback):
        self._CanFeedback = CanFeedback

    @property
    def Type(self):
        r"""记录类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def References(self):
        r"""引用来源
        :rtype: list of MsgRecordReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Reasons(self):
        r"""评价原因
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def IsLlmGenerated(self):
        r"""是否大模型
        :rtype: bool
        """
        return self._IsLlmGenerated

    @IsLlmGenerated.setter
    def IsLlmGenerated(self, IsLlmGenerated):
        self._IsLlmGenerated = IsLlmGenerated

    @property
    def ImageUrls(self):
        r"""图片链接，可公有读
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls

    @property
    def TokenStat(self):
        r"""当次 token 统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.TokenStat`
        """
        return self._TokenStat

    @TokenStat.setter
    def TokenStat(self, TokenStat):
        self._TokenStat = TokenStat

    @property
    def ReplyMethod(self):
        r"""回复方式
1:大模型直接回复;
2:保守回复, 未知问题回复;
3:拒答问题回复;
4:敏感回复;
5:问答对直接回复, 已采纳问答对优先回复;
6:欢迎语回复;
7:并发超限回复;
8:全局干预知识;
9:任务流程过程回复, 当历史记录中 task_flow.type = 0 时, 为大模型回复;
10:任务流程答案回复;
11:搜索引擎回复;
12:知识润色后回复;
13:图片理解回复;
14:实时文档回复;
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod

    @property
    def OptionCards(self):
        r"""选项卡, 用于多轮对话
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def TaskFlow(self):
        r"""任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskFlowInfo`
        """
        return self._TaskFlow

    @TaskFlow.setter
    def TaskFlow(self, TaskFlow):
        self._TaskFlow = TaskFlow

    @property
    def FileInfos(self):
        r"""用户传入的文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FileInfo
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def QuoteInfos(self):
        r"""参考来源引用位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QuoteInfo
        """
        return self._QuoteInfos

    @QuoteInfos.setter
    def QuoteInfos(self, QuoteInfos):
        self._QuoteInfos = QuoteInfos

    @property
    def AgentThought(self):
        r"""Agent的思考过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentThought`
        """
        return self._AgentThought

    @AgentThought.setter
    def AgentThought(self, AgentThought):
        self._AgentThought = AgentThought

    @property
    def ExtraInfo(self):
        r"""扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def WorkFlow(self):
        r"""工作流信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.WorkflowInfo`
        """
        return self._WorkFlow

    @WorkFlow.setter
    def WorkFlow(self, WorkFlow):
        self._WorkFlow = WorkFlow


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._SessionId = params.get("SessionId")
        self._RecordId = params.get("RecordId")
        self._RelatedRecordId = params.get("RelatedRecordId")
        self._IsFromSelf = params.get("IsFromSelf")
        self._FromName = params.get("FromName")
        self._FromAvatar = params.get("FromAvatar")
        self._Timestamp = params.get("Timestamp")
        self._HasRead = params.get("HasRead")
        self._Score = params.get("Score")
        self._CanRating = params.get("CanRating")
        self._CanFeedback = params.get("CanFeedback")
        self._Type = params.get("Type")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = MsgRecordReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._Reasons = params.get("Reasons")
        self._IsLlmGenerated = params.get("IsLlmGenerated")
        self._ImageUrls = params.get("ImageUrls")
        if params.get("TokenStat") is not None:
            self._TokenStat = TokenStat()
            self._TokenStat._deserialize(params.get("TokenStat"))
        self._ReplyMethod = params.get("ReplyMethod")
        self._OptionCards = params.get("OptionCards")
        if params.get("TaskFlow") is not None:
            self._TaskFlow = TaskFlowInfo()
            self._TaskFlow._deserialize(params.get("TaskFlow"))
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        if params.get("QuoteInfos") is not None:
            self._QuoteInfos = []
            for item in params.get("QuoteInfos"):
                obj = QuoteInfo()
                obj._deserialize(item)
                self._QuoteInfos.append(obj)
        if params.get("AgentThought") is not None:
            self._AgentThought = AgentThought()
            self._AgentThought._deserialize(params.get("AgentThought"))
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        if params.get("WorkFlow") is not None:
            self._WorkFlow = WorkflowInfo()
            self._WorkFlow._deserialize(params.get("WorkFlow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordReference(AbstractModel):
    r"""聊天详情Refer

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: str
        :param _Url: 链接
        :type Url: str
        :param _Type: 类型
        :type Type: int
        :param _Name: 名称
        :type Name: str
        :param _DocId: 来源文档ID
        :type DocId: str
        :param _KnowledgeName: 知识库名称
        :type KnowledgeName: str
        :param _KnowledgeBizId: 知识库业务id
        :type KnowledgeBizId: str
        :param _DocBizId: 文档业务id
        :type DocBizId: str
        :param _QaBizId: 问答业务id
        :type QaBizId: str
        :param _Index: 文档索引id
        :type Index: int
        """
        self._Id = None
        self._Url = None
        self._Type = None
        self._Name = None
        self._DocId = None
        self._KnowledgeName = None
        self._KnowledgeBizId = None
        self._DocBizId = None
        self._QaBizId = None
        self._Index = None

    @property
    def Id(self):
        r"""id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        r"""链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        r"""类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DocId(self):
        r"""来源文档ID
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def KnowledgeName(self):
        r"""知识库名称
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName

    @property
    def KnowledgeBizId(self):
        r"""知识库业务id
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def DocBizId(self):
        r"""文档业务id
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def QaBizId(self):
        r"""问答业务id
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Index(self):
        r"""文档索引id
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._DocId = params.get("DocId")
        self._KnowledgeName = params.get("KnowledgeName")
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._DocBizId = params.get("DocBizId")
        self._QaBizId = params.get("QaBizId")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NL2SQLModelConfig(AbstractModel):
    r"""Nl2Sql模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeRunBase(AbstractModel):
    r"""节点运行的基本信息

    """

    def __init__(self):
        r"""
        :param _NodeRunId: 节点运行的ID
        :type NodeRunId: str
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _WorkflowRunId: 工作流运行实例的ID
        :type WorkflowRunId: str
        :param _NodeName: 节点名称
        :type NodeName: str
        :param _NodeType: 节点类型。
1： 开始节点
2：参数提取节点
3：大模型节点
4：知识问答节点
5：知识检索节点
6：标签提取节点
7：代码执行节点
8：工具节点
9：逻辑判断节点
10：回复节点
11：选项卡节点
12：循环节点
13：意图识别节点
14：工作流节点
15：插件节点
16：结束节点
17: 变量聚合节点数据
18: 批处理节点
19: 消息队列节点
        :type NodeType: int
        :param _State: 运行状态。0: 初始状态；1: 运行中；2: 运行成功； 3: 运行失败； 4: 已取消
        :type State: int
        :param _FailCode: 错误码
        :type FailCode: str
        :param _FailMessage: 错误信息
        :type FailMessage: str
        :param _CostMilliseconds: 消耗时间（毫秒）
        :type CostMilliseconds: int
        :param _TotalTokens: 消耗的token总数
        :type TotalTokens: int
        """
        self._NodeRunId = None
        self._NodeId = None
        self._WorkflowRunId = None
        self._NodeName = None
        self._NodeType = None
        self._State = None
        self._FailCode = None
        self._FailMessage = None
        self._CostMilliseconds = None
        self._TotalTokens = None

    @property
    def NodeRunId(self):
        r"""节点运行的ID
        :rtype: str
        """
        return self._NodeRunId

    @NodeRunId.setter
    def NodeRunId(self, NodeRunId):
        self._NodeRunId = NodeRunId

    @property
    def NodeId(self):
        r"""节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例的ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def NodeName(self):
        r"""节点名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeType(self):
        r"""节点类型。
1： 开始节点
2：参数提取节点
3：大模型节点
4：知识问答节点
5：知识检索节点
6：标签提取节点
7：代码执行节点
8：工具节点
9：逻辑判断节点
10：回复节点
11：选项卡节点
12：循环节点
13：意图识别节点
14：工作流节点
15：插件节点
16：结束节点
17: 变量聚合节点数据
18: 批处理节点
19: 消息队列节点
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def State(self):
        r"""运行状态。0: 初始状态；1: 运行中；2: 运行成功； 3: 运行失败； 4: 已取消
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FailCode(self):
        r"""错误码
        :rtype: str
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def FailMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def CostMilliseconds(self):
        r"""消耗时间（毫秒）
        :rtype: int
        """
        return self._CostMilliseconds

    @CostMilliseconds.setter
    def CostMilliseconds(self, CostMilliseconds):
        self._CostMilliseconds = CostMilliseconds

    @property
    def TotalTokens(self):
        r"""消耗的token总数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._NodeRunId = params.get("NodeRunId")
        self._NodeId = params.get("NodeId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._NodeName = params.get("NodeName")
        self._NodeType = params.get("NodeType")
        self._State = params.get("State")
        self._FailCode = params.get("FailCode")
        self._FailMessage = params.get("FailMessage")
        self._CostMilliseconds = params.get("CostMilliseconds")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeRunDetail(AbstractModel):
    r"""工作流节点运行详情

    """

    def __init__(self):
        r"""
        :param _NodeRunId: 节点运行的ID
        :type NodeRunId: str
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _WorkflowRunId: 工作流运行实例的ID
        :type WorkflowRunId: str
        :param _NodeName: 节点名称
        :type NodeName: str
        :param _NodeType: 节点类型。
1： 开始节点
2：参数提取节点
3：大模型节点
4：知识问答节点
5：知识检索节点
6：标签提取节点
7：代码执行节点
8：工具节点
9：逻辑判断节点
10：回复节点
11：选项卡节点
12：循环节点
13：意图识别节点
14：工作流节点
15：插件节点
16：结束节点
17: 变量聚合节点数据
18: 批处理节点
19: 消息队列节点
        :type NodeType: int
        :param _State: 运行状态。0: 初始状态；1: 运行中；2: 运行成功； 3: 运行失败； 4: 已取消
        :type State: int
        :param _FailCode: 错误码
        :type FailCode: str
        :param _FailMessage: 错误信息
        :type FailMessage: str
        :param _CostMilliseconds: 消耗时间（毫秒）
        :type CostMilliseconds: int
        :param _TotalTokens: 消耗的token总数
        :type TotalTokens: int
        :param _Input: 输入变量信息
        :type Input: str
        :param _InputRef: 节点的输入的完整内容的链接。（当Input内容超过限制的时候此字段才有值）
        :type InputRef: str
        :param _Output: 输出变量信息
        :type Output: str
        :param _OutputRef: 节点的输出的完整内容的链接。（当Output内容超过限制的时候此字段才有值）
        :type OutputRef: str
        :param _TaskOutput: 原始输出信息。部分节点才有值，如工具节点、代码节点
        :type TaskOutput: str
        :param _TaskOutputRef: 任务的原始输出的完整内容的链接。（当TaskOutput内容超过限制的时候此字段才有值）
        :type TaskOutputRef: str
        :param _Log: 节点的日志
        :type Log: str
        :param _LogRef: 节点的日志的完整内容的链接志（当Log内容超过限制的时候才有值）
        :type LogRef: str
        :param _StartTime: 开始时间戳（毫秒）
        :type StartTime: str
        :param _EndTime: 结束时间戳（毫秒）
        :type EndTime: str
        :param _StatisticInfos: LLM统计信息。
        :type StatisticInfos: list of StatisticInfo
        """
        self._NodeRunId = None
        self._NodeId = None
        self._WorkflowRunId = None
        self._NodeName = None
        self._NodeType = None
        self._State = None
        self._FailCode = None
        self._FailMessage = None
        self._CostMilliseconds = None
        self._TotalTokens = None
        self._Input = None
        self._InputRef = None
        self._Output = None
        self._OutputRef = None
        self._TaskOutput = None
        self._TaskOutputRef = None
        self._Log = None
        self._LogRef = None
        self._StartTime = None
        self._EndTime = None
        self._StatisticInfos = None

    @property
    def NodeRunId(self):
        r"""节点运行的ID
        :rtype: str
        """
        return self._NodeRunId

    @NodeRunId.setter
    def NodeRunId(self, NodeRunId):
        self._NodeRunId = NodeRunId

    @property
    def NodeId(self):
        r"""节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例的ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def NodeName(self):
        r"""节点名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeType(self):
        r"""节点类型。
1： 开始节点
2：参数提取节点
3：大模型节点
4：知识问答节点
5：知识检索节点
6：标签提取节点
7：代码执行节点
8：工具节点
9：逻辑判断节点
10：回复节点
11：选项卡节点
12：循环节点
13：意图识别节点
14：工作流节点
15：插件节点
16：结束节点
17: 变量聚合节点数据
18: 批处理节点
19: 消息队列节点
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def State(self):
        r"""运行状态。0: 初始状态；1: 运行中；2: 运行成功； 3: 运行失败； 4: 已取消
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FailCode(self):
        r"""错误码
        :rtype: str
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def FailMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def CostMilliseconds(self):
        r"""消耗时间（毫秒）
        :rtype: int
        """
        return self._CostMilliseconds

    @CostMilliseconds.setter
    def CostMilliseconds(self, CostMilliseconds):
        self._CostMilliseconds = CostMilliseconds

    @property
    def TotalTokens(self):
        r"""消耗的token总数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def Input(self):
        r"""输入变量信息
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def InputRef(self):
        r"""节点的输入的完整内容的链接。（当Input内容超过限制的时候此字段才有值）
        :rtype: str
        """
        return self._InputRef

    @InputRef.setter
    def InputRef(self, InputRef):
        self._InputRef = InputRef

    @property
    def Output(self):
        r"""输出变量信息
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def OutputRef(self):
        r"""节点的输出的完整内容的链接。（当Output内容超过限制的时候此字段才有值）
        :rtype: str
        """
        return self._OutputRef

    @OutputRef.setter
    def OutputRef(self, OutputRef):
        self._OutputRef = OutputRef

    @property
    def TaskOutput(self):
        r"""原始输出信息。部分节点才有值，如工具节点、代码节点
        :rtype: str
        """
        return self._TaskOutput

    @TaskOutput.setter
    def TaskOutput(self, TaskOutput):
        self._TaskOutput = TaskOutput

    @property
    def TaskOutputRef(self):
        r"""任务的原始输出的完整内容的链接。（当TaskOutput内容超过限制的时候此字段才有值）
        :rtype: str
        """
        return self._TaskOutputRef

    @TaskOutputRef.setter
    def TaskOutputRef(self, TaskOutputRef):
        self._TaskOutputRef = TaskOutputRef

    @property
    def Log(self):
        r"""节点的日志
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def LogRef(self):
        r"""节点的日志的完整内容的链接志（当Log内容超过限制的时候才有值）
        :rtype: str
        """
        return self._LogRef

    @LogRef.setter
    def LogRef(self, LogRef):
        self._LogRef = LogRef

    @property
    def StartTime(self):
        r"""开始时间戳（毫秒）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间戳（毫秒）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StatisticInfos(self):
        r"""LLM统计信息。
        :rtype: list of StatisticInfo
        """
        return self._StatisticInfos

    @StatisticInfos.setter
    def StatisticInfos(self, StatisticInfos):
        self._StatisticInfos = StatisticInfos


    def _deserialize(self, params):
        self._NodeRunId = params.get("NodeRunId")
        self._NodeId = params.get("NodeId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._NodeName = params.get("NodeName")
        self._NodeType = params.get("NodeType")
        self._State = params.get("State")
        self._FailCode = params.get("FailCode")
        self._FailMessage = params.get("FailMessage")
        self._CostMilliseconds = params.get("CostMilliseconds")
        self._TotalTokens = params.get("TotalTokens")
        self._Input = params.get("Input")
        self._InputRef = params.get("InputRef")
        self._Output = params.get("Output")
        self._OutputRef = params.get("OutputRef")
        self._TaskOutput = params.get("TaskOutput")
        self._TaskOutputRef = params.get("TaskOutputRef")
        self._Log = params.get("Log")
        self._LogRef = params.get("LogRef")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("StatisticInfos") is not None:
            self._StatisticInfos = []
            for item in params.get("StatisticInfos"):
                obj = StatisticInfo()
                obj._deserialize(item)
                self._StatisticInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    r"""下拉框选项

    """

    def __init__(self):
        r"""
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _CharSize: 文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type CharSize: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self._Text = None
        self._Value = None
        self._CharSize = None
        self._FileType = None

    @property
    def Text(self):
        r"""文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def CharSize(self):
        r"""文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CharSize

    @CharSize.setter
    def CharSize(self, CharSize):
        self._CharSize = CharSize

    @property
    def FileType(self):
        r"""文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        self._CharSize = params.get("CharSize")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionCardIndex(AbstractModel):
    r"""选项卡索引

    """

    def __init__(self):
        r"""
        :param _RecordId: 唯一标识
        :type RecordId: str
        :param _Index: 选项卡索引
        :type Index: int
        """
        self._RecordId = None
        self._Index = None

    @property
    def RecordId(self):
        r"""唯一标识
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Index(self):
        r"""选项卡索引
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterConfig(AbstractModel):
    r"""参数配置列表

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Description: 字段描述
        :type Description: str
        :param _Type: 字段类型
        :type Type: int
        :param _IsRequired: 是否必填
        :type IsRequired: bool
        :param _SubParams: 子参数
        :type SubParams: list of ParameterConfig
        :param _OneOf: OneOf类型的参数
        :type OneOf: list of ParameterConfig
        :param _AnyOf: AnyOf类型的参数
        :type AnyOf: list of ParameterConfig
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._IsRequired = None
        self._SubParams = None
        self._OneOf = None
        self._AnyOf = None

    @property
    def Name(self):
        r"""字段名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""字段描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""字段类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsRequired(self):
        r"""是否必填
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def SubParams(self):
        r"""子参数
        :rtype: list of ParameterConfig
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def OneOf(self):
        r"""OneOf类型的参数
        :rtype: list of ParameterConfig
        """
        return self._OneOf

    @OneOf.setter
    def OneOf(self, OneOf):
        self._OneOf = OneOf

    @property
    def AnyOf(self):
        r"""AnyOf类型的参数
        :rtype: list of ParameterConfig
        """
        return self._AnyOf

    @AnyOf.setter
    def AnyOf(self, AnyOf):
        self._AnyOf = AnyOf


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._IsRequired = params.get("IsRequired")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = ParameterConfig()
                obj._deserialize(item)
                self._SubParams.append(obj)
        if params.get("OneOf") is not None:
            self._OneOf = []
            for item in params.get("OneOf"):
                obj = ParameterConfig()
                obj._deserialize(item)
                self._OneOf.append(obj)
        if params.get("AnyOf") is not None:
            self._AnyOf = []
            for item in params.get("AnyOf"):
                obj = ParameterConfig()
                obj._deserialize(item)
                self._AnyOf.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginToolReqParam(AbstractModel):
    r"""插件参数请求结构

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _Desc: 参数描述
        :type Desc: str
        :param _Type: 参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object, 99:null, 100:upspecified
        :type Type: int
        :param _IsRequired: 参数是否必填
        :type IsRequired: bool
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _SubParams: 子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :type SubParams: list of PluginToolReqParam
        :param _GlobalHidden: 插件参数配置是否隐藏不可见，true-隐藏不可见，false-可见
        :type GlobalHidden: bool
        :param _OneOf: OneOf类型参数
        :type OneOf: list of PluginToolReqParam
        :param _AnyOf: AnyOf类型参数
        :type AnyOf: list of PluginToolReqParam
        """
        self._Name = None
        self._Desc = None
        self._Type = None
        self._IsRequired = None
        self._DefaultValue = None
        self._SubParams = None
        self._GlobalHidden = None
        self._OneOf = None
        self._AnyOf = None

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
    def Desc(self):
        r"""参数描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Type(self):
        r"""参数类型，0:string, 1:int, 2:float，3:bool 4:object 5:array_string, 6:array_int, 7:array_float, 8:array_bool, 9:array_object, 99:null, 100:upspecified
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def DefaultValue(self):
        r"""参数默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def SubParams(self):
        r"""子参数,ParamType 是OBJECT 或 ARRAY<>类型有用
        :rtype: list of PluginToolReqParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def GlobalHidden(self):
        r"""插件参数配置是否隐藏不可见，true-隐藏不可见，false-可见
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def OneOf(self):
        r"""OneOf类型参数
        :rtype: list of PluginToolReqParam
        """
        return self._OneOf

    @OneOf.setter
    def OneOf(self, OneOf):
        self._OneOf = OneOf

    @property
    def AnyOf(self):
        r"""AnyOf类型参数
        :rtype: list of PluginToolReqParam
        """
        return self._AnyOf

    @AnyOf.setter
    def AnyOf(self, AnyOf):
        self._AnyOf = AnyOf


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Type = params.get("Type")
        self._IsRequired = params.get("IsRequired")
        self._DefaultValue = params.get("DefaultValue")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._GlobalHidden = params.get("GlobalHidden")
        if params.get("OneOf") is not None:
            self._OneOf = []
            for item in params.get("OneOf"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._OneOf.append(obj)
        if params.get("AnyOf") is not None:
            self._AnyOf = []
            for item in params.get("AnyOf"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._AnyOf.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Procedure(AbstractModel):
    r"""执行过程信息记录

    """

    def __init__(self):
        r"""
        :param _Name: 执行过程英语名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Title: 中文名, 用于展示
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Status: 状态常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Count: 消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Debugging: 调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Debugging: :class:`tencentcloud.lke.v20231130.models.ProcedureDebugging`
        :param _ResourceStatus: 计费资源状态，1：可用，2：不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        :param _InputCount: 输入消耗 token 数
        :type InputCount: int
        :param _OutputCount: 输出消耗 token 数
        :type OutputCount: int
        """
        self._Name = None
        self._Title = None
        self._Status = None
        self._Count = None
        self._Debugging = None
        self._ResourceStatus = None
        self._InputCount = None
        self._OutputCount = None

    @property
    def Name(self):
        r"""执行过程英语名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""中文名, 用于展示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        r"""状态常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        r"""消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Debugging(self):
        r"""调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.ProcedureDebugging`
        """
        return self._Debugging

    @Debugging.setter
    def Debugging(self, Debugging):
        self._Debugging = Debugging

    @property
    def ResourceStatus(self):
        r"""计费资源状态，1：可用，2：不可用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def InputCount(self):
        r"""输入消耗 token 数
        :rtype: int
        """
        return self._InputCount

    @InputCount.setter
    def InputCount(self, InputCount):
        self._InputCount = InputCount

    @property
    def OutputCount(self):
        r"""输出消耗 token 数
        :rtype: int
        """
        return self._OutputCount

    @OutputCount.setter
    def OutputCount(self, OutputCount):
        self._OutputCount = OutputCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        if params.get("Debugging") is not None:
            self._Debugging = ProcedureDebugging()
            self._Debugging._deserialize(params.get("Debugging"))
        self._ResourceStatus = params.get("ResourceStatus")
        self._InputCount = params.get("InputCount")
        self._OutputCount = params.get("OutputCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedureDebugging(AbstractModel):
    r"""调试信息

    """

    def __init__(self):
        r"""
        :param _Content: 检索query
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _System: 系统prompt
注意：此字段可能返回 null，表示取不到有效值。
        :type System: str
        :param _Histories: 多轮历史信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Histories: list of HistorySummary
        :param _Knowledge: 检索知识
注意：此字段可能返回 null，表示取不到有效值。
        :type Knowledge: list of KnowledgeSummary
        :param _TaskFlow: 任务流程
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlow: :class:`tencentcloud.lke.v20231130.models.TaskFlowSummary`
        :param _WorkFlow: 工作流调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkFlow: :class:`tencentcloud.lke.v20231130.models.WorkFlowSummary`
        :param _Agent: Agent调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Agent: :class:`tencentcloud.lke.v20231130.models.AgentDebugInfo`
        :param _CustomVariables: 自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomVariables: list of str
        """
        self._Content = None
        self._System = None
        self._Histories = None
        self._Knowledge = None
        self._TaskFlow = None
        self._WorkFlow = None
        self._Agent = None
        self._CustomVariables = None

    @property
    def Content(self):
        r"""检索query
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def System(self):
        r"""系统prompt
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._System

    @System.setter
    def System(self, System):
        self._System = System

    @property
    def Histories(self):
        r"""多轮历史信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HistorySummary
        """
        return self._Histories

    @Histories.setter
    def Histories(self, Histories):
        self._Histories = Histories

    @property
    def Knowledge(self):
        r"""检索知识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KnowledgeSummary
        """
        return self._Knowledge

    @Knowledge.setter
    def Knowledge(self, Knowledge):
        self._Knowledge = Knowledge

    @property
    def TaskFlow(self):
        r"""任务流程
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskFlowSummary`
        """
        return self._TaskFlow

    @TaskFlow.setter
    def TaskFlow(self, TaskFlow):
        self._TaskFlow = TaskFlow

    @property
    def WorkFlow(self):
        r"""工作流调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.WorkFlowSummary`
        """
        return self._WorkFlow

    @WorkFlow.setter
    def WorkFlow(self, WorkFlow):
        self._WorkFlow = WorkFlow

    @property
    def Agent(self):
        r"""Agent调试信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentDebugInfo`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def CustomVariables(self):
        r"""自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomVariables

    @CustomVariables.setter
    def CustomVariables(self, CustomVariables):
        self._CustomVariables = CustomVariables


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._System = params.get("System")
        if params.get("Histories") is not None:
            self._Histories = []
            for item in params.get("Histories"):
                obj = HistorySummary()
                obj._deserialize(item)
                self._Histories.append(obj)
        if params.get("Knowledge") is not None:
            self._Knowledge = []
            for item in params.get("Knowledge"):
                obj = KnowledgeSummary()
                obj._deserialize(item)
                self._Knowledge.append(obj)
        if params.get("TaskFlow") is not None:
            self._TaskFlow = TaskFlowSummary()
            self._TaskFlow._deserialize(params.get("TaskFlow"))
        if params.get("WorkFlow") is not None:
            self._WorkFlow = WorkFlowSummary()
            self._WorkFlow._deserialize(params.get("WorkFlow"))
        if params.get("Agent") is not None:
            self._Agent = AgentDebugInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._CustomVariables = params.get("CustomVariables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QACate(AbstractModel):
    r"""获取QA分类分组

    """

    def __init__(self):
        r"""
        :param _CateBizId: QA分类的业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateBizId: str
        :param _Name: 分类名称

注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Total: 分类下QA数量

注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _CanAdd: 是否可新增

注意：此字段可能返回 null，表示取不到有效值。
        :type CanAdd: bool
        :param _CanEdit: 是否可编辑

注意：此字段可能返回 null，表示取不到有效值。
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

注意：此字段可能返回 null，表示取不到有效值。
        :type CanDelete: bool
        :param _Children: 子分类
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of QACate
        :param _IsLeaf: 是否是叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLeaf: bool
        """
        self._CateBizId = None
        self._Name = None
        self._Total = None
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._Children = None
        self._IsLeaf = None

    @property
    def CateBizId(self):
        r"""QA分类的业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Name(self):
        r"""分类名称

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        r"""分类下QA数量

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CanAdd(self):
        r"""是否可新增

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        r"""是否可编辑

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        r"""是否可删除

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Children(self):
        r"""子分类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QACate
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def IsLeaf(self):
        r"""是否是叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf


    def _deserialize(self, params):
        self._CateBizId = params.get("CateBizId")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = QACate()
                obj._deserialize(item)
                self._Children.append(obj)
        self._IsLeaf = params.get("IsLeaf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAList(AbstractModel):
    r"""问答列表

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _IsAccepted: 是否采纳
        :type IsAccepted: bool
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        """
        self._QaBizId = None
        self._IsAccepted = None
        self._CateBizId = None
        self._Question = None
        self._Answer = None

    @property
    def QaBizId(self):
        r"""问答ID
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def IsAccepted(self):
        r"""是否采纳
        :rtype: bool
        """
        return self._IsAccepted

    @IsAccepted.setter
    def IsAccepted(self, IsAccepted):
        self._IsAccepted = IsAccepted

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
    def Answer(self):
        r"""答案
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._IsAccepted = params.get("IsAccepted")
        self._CateBizId = params.get("CateBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAQuery(AbstractModel):
    r"""QA查询参数

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码


        :type PageNumber: int
        :param _PageSize: 每页数量

        :type PageSize: int
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Query: 查询内容

        :type Query: str
        :param _CateBizId: 分类ID

        :type CateBizId: str
        :param _AcceptStatus: 校验状态

        :type AcceptStatus: list of int non-negative
        :param _ReleaseStatus: 发布状态

        :type ReleaseStatus: list of int non-negative
        :param _DocBizId: 文档ID

        :type DocBizId: str
        :param _QaBizId: QAID

        :type QaBizId: str
        :param _Source: 来源

        :type Source: int
        :param _QueryAnswer: 查询答案

        :type QueryAnswer: str
        :param _QueryType: 查询类型 filename 名称、 attribute 标签
        :type QueryType: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._BotBizId = None
        self._Query = None
        self._CateBizId = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._QaBizId = None
        self._Source = None
        self._QueryAnswer = None
        self._QueryType = None

    @property
    def PageNumber(self):
        r"""页码


        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Query(self):
        r"""查询内容

        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def CateBizId(self):
        r"""分类ID

        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def AcceptStatus(self):
        r"""校验状态

        :rtype: list of int non-negative
        """
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        r"""发布状态

        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        r"""文档ID

        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def QaBizId(self):
        r"""QAID

        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Source(self):
        r"""来源

        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        r"""查询答案

        :rtype: str
        """
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer

    @property
    def QueryType(self):
        r"""查询类型 filename 名称、 attribute 标签
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._BotBizId = params.get("BotBizId")
        self._Query = params.get("Query")
        self._CateBizId = params.get("CateBizId")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._QaBizId = params.get("QaBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        self._QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuoteInfo(AbstractModel):
    r"""搜索引擎参考来源索引

    """

    def __init__(self):
        r"""
        :param _Position: 参考来源位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        :param _Index: 参考来源索引顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        """
        self._Position = None
        self._Index = None

    @property
    def Position(self):
        r"""参考来源位置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Index(self):
        r"""参考来源索引顺序
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Position = params.get("Position")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateMsgRecordRequest(AbstractModel):
    r"""RateMsgRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotAppKey: 应用appKey
        :type BotAppKey: str
        :param _RecordId: 消息ID 【大模型回复答案的RecordID】可以通过[GetMsgRecord](https://cloud.tencent.com/document/product/1759/105090)接口获取
        :type RecordId: str
        :param _Score: 0: 取消前置状态 ; 1: 点赞;   2: 点踩;   
注：
(1) 评测端不支持点赞、点踩
(2) 消息回复类型为欢迎语、并发超限、实时文档，不支持点赞、点踩
(3) 点赞或者点踩之后，如果想要取消状态，传值为0即可
        :type Score: int
        :param _Reasons: 支持通过API自定义，字符上限值为20字符；通过API 自定义标签，可以支持平台端用户在不满意问题错误类型中筛选、查看
        :type Reasons: list of str
        :param _FeedbackContent: 用户自定义反馈内容
        :type FeedbackContent: str
        """
        self._BotAppKey = None
        self._RecordId = None
        self._Score = None
        self._Reasons = None
        self._FeedbackContent = None

    @property
    def BotAppKey(self):
        r"""应用appKey
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def RecordId(self):
        r"""消息ID 【大模型回复答案的RecordID】可以通过[GetMsgRecord](https://cloud.tencent.com/document/product/1759/105090)接口获取
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Score(self):
        r"""0: 取消前置状态 ; 1: 点赞;   2: 点踩;   
注：
(1) 评测端不支持点赞、点踩
(2) 消息回复类型为欢迎语、并发超限、实时文档，不支持点赞、点踩
(3) 点赞或者点踩之后，如果想要取消状态，传值为0即可
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Reasons(self):
        r"""支持通过API自定义，字符上限值为20字符；通过API 自定义标签，可以支持平台端用户在不满意问题错误类型中筛选、查看
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def FeedbackContent(self):
        r"""用户自定义反馈内容
        :rtype: str
        """
        return self._FeedbackContent

    @FeedbackContent.setter
    def FeedbackContent(self, FeedbackContent):
        self._FeedbackContent = FeedbackContent


    def _deserialize(self, params):
        self._BotAppKey = params.get("BotAppKey")
        self._RecordId = params.get("RecordId")
        self._Score = params.get("Score")
        self._Reasons = params.get("Reasons")
        self._FeedbackContent = params.get("FeedbackContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateMsgRecordResponse(AbstractModel):
    r"""RateMsgRecord返回参数结构体

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


class ReferDetail(AbstractModel):
    r"""引用来源详情

    """

    def __init__(self):
        r"""
        :param _ReferBizId: 引用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferBizId: str
        :param _DocType: 文档类型 (1 QA, 2 文档段)
注意：此字段可能返回 null，表示取不到有效值。
        :type DocType: int
        :param _DocName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DocName: str
        :param _PageContent: 分片内容
注意：此字段可能返回 null，表示取不到有效值。
        :type PageContent: str
        :param _Question: 问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Answer: 答案
注意：此字段可能返回 null，表示取不到有效值。
        :type Answer: str
        :param _Confidence: 置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Mark: 标记
注意：此字段可能返回 null，表示取不到有效值。
        :type Mark: int
        :param _Highlights: 分片高亮内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Highlights: list of Highlight
        :param _OrgData: 原始内容
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgData: str
        :param _PageInfos: 页码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PageInfos: list of int non-negative
        :param _SheetInfos: sheet信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SheetInfos: list of str
        :param _DocBizId: 文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocBizId: str
        :param _KnowledgeBizId: 知识库ID
        :type KnowledgeBizId: str
        """
        self._ReferBizId = None
        self._DocType = None
        self._DocName = None
        self._PageContent = None
        self._Question = None
        self._Answer = None
        self._Confidence = None
        self._Mark = None
        self._Highlights = None
        self._OrgData = None
        self._PageInfos = None
        self._SheetInfos = None
        self._DocBizId = None
        self._KnowledgeBizId = None

    @property
    def ReferBizId(self):
        r"""引用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReferBizId

    @ReferBizId.setter
    def ReferBizId(self, ReferBizId):
        self._ReferBizId = ReferBizId

    @property
    def DocType(self):
        r"""文档类型 (1 QA, 2 文档段)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DocType

    @DocType.setter
    def DocType(self, DocType):
        self._DocType = DocType

    @property
    def DocName(self):
        r"""文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def PageContent(self):
        r"""分片内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Question(self):
        r"""问题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        r"""答案
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Confidence(self):
        r"""置信度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Mark(self):
        r"""标记
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Highlights(self):
        r"""分片高亮内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Highlight
        """
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        r"""原始内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def PageInfos(self):
        r"""页码信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._PageInfos

    @PageInfos.setter
    def PageInfos(self, PageInfos):
        self._PageInfos = PageInfos

    @property
    def SheetInfos(self):
        r"""sheet信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SheetInfos

    @SheetInfos.setter
    def SheetInfos(self, SheetInfos):
        self._SheetInfos = SheetInfos

    @property
    def DocBizId(self):
        r"""文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def KnowledgeBizId(self):
        r"""知识库ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId


    def _deserialize(self, params):
        self._ReferBizId = params.get("ReferBizId")
        self._DocType = params.get("DocType")
        self._DocName = params.get("DocName")
        self._PageContent = params.get("PageContent")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Confidence = params.get("Confidence")
        self._Mark = params.get("Mark")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        self._PageInfos = params.get("PageInfos")
        self._SheetInfos = params.get("SheetInfos")
        self._DocBizId = params.get("DocBizId")
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferShareKnowledgeRequest(AbstractModel):
    r"""ReferShareKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用业务id
        :type AppBizId: str
        :param _KnowledgeBizId: 共享知识库业务id列表
        :type KnowledgeBizId: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._AppBizId = None
        self._KnowledgeBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppBizId(self):
        r"""应用业务id
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务id列表
        :rtype: list of str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferShareKnowledgeResponse(AbstractModel):
    r"""ReferShareKnowledge返回参数结构体

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


class RejectedQuestion(AbstractModel):
    r"""发布拒答

    """

    def __init__(self):
        r"""
        :param _RejectedBizId: 拒答问题ID


注意：此字段可能返回 null，表示取不到有效值。
        :type RejectedBizId: str
        :param _Question: 被拒答的问题

注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Status: 发布状态(1 待发布 2 发布中 3 已发布 4 发布失败)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _UpdateTime: 更新时间, 秒级时间戳

注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _IsAllowEdit: 是否允许编辑

注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowEdit: bool
        :param _IsAllowDelete: 是否允许删除

注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowDelete: bool
        :param _Operator: 操作人
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        """
        self._RejectedBizId = None
        self._Question = None
        self._Status = None
        self._StatusDesc = None
        self._UpdateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None
        self._Operator = None

    @property
    def RejectedBizId(self):
        r"""拒答问题ID


注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId

    @property
    def Question(self):
        r"""被拒答的问题

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Status(self):
        r"""发布状态(1 待发布 2 发布中 3 已发布 4 发布失败)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def UpdateTime(self):
        r"""更新时间, 秒级时间戳

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowEdit(self):
        r"""是否允许编辑

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        r"""是否允许删除

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def Operator(self):
        r"""操作人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._RejectedBizId = params.get("RejectedBizId")
        self._Question = params.get("Question")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseConfigs(AbstractModel):
    r"""发布配置项

    """

    def __init__(self):
        r"""
        :param _ConfigItem: 配置项描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigItem: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Action: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _Value: 变更后的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _LastValue: 变更前的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type LastValue: str
        :param _Content: 变更内容(优先级展示content内容,content为空取value内容)
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Message: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._ConfigItem = None
        self._UpdateTime = None
        self._Action = None
        self._Value = None
        self._LastValue = None
        self._Content = None
        self._Message = None

    @property
    def ConfigItem(self):
        r"""配置项描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigItem

    @ConfigItem.setter
    def ConfigItem(self, ConfigItem):
        self._ConfigItem = ConfigItem

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
    def Action(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        r"""变更后的内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def LastValue(self):
        r"""变更前的内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastValue

    @LastValue.setter
    def LastValue(self, LastValue):
        self._LastValue = LastValue

    @property
    def Content(self):
        r"""变更内容(优先级展示content内容,content为空取value内容)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Message(self):
        r"""失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._ConfigItem = params.get("ConfigItem")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        self._LastValue = params.get("LastValue")
        self._Content = params.get("Content")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseDoc(AbstractModel):
    r"""发布文档详情

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Action: 状态
        :type Action: int
        :param _ActionDesc: 状态描述
        :type ActionDesc: str
        :param _Message: 失败原因
        :type Message: str
        :param _DocBizId: 文档业务ID
        :type DocBizId: str
        """
        self._FileName = None
        self._FileType = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None
        self._DocBizId = None

    @property
    def FileName(self):
        r"""文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        r"""状态
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        r"""状态描述
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        r"""失败原因
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DocBizId(self):
        r"""文档业务ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseQA(AbstractModel):
    r"""发布问答

    """

    def __init__(self):
        r"""
        :param _Question: 问题
        :type Question: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Action: 状态
        :type Action: int
        :param _ActionDesc: 状态描述
        :type ActionDesc: str
        :param _Source: 来源1:文档生成，2：批量导入，3：手动添加
        :type Source: int
        :param _SourceDesc: 来源描述
        :type SourceDesc: str
        :param _FileName: 文件名字
        :type FileName: str
        :param _FileType: 文档类型
        :type FileType: str
        :param _Message: 失败原因
        :type Message: str
        :param _ReleaseStatus: 发布状态
        :type ReleaseStatus: int
        :param _QaBizId: QAID
        :type QaBizId: str
        :param _DocBizId: 文档业务ID
        :type DocBizId: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Source = None
        self._SourceDesc = None
        self._FileName = None
        self._FileType = None
        self._Message = None
        self._ReleaseStatus = None
        self._QaBizId = None
        self._DocBizId = None

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
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        r"""状态
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        r"""状态描述
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Source(self):
        r"""来源1:文档生成，2：批量导入，3：手动添加
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        r"""来源描述
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def FileName(self):
        r"""文件名字
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文档类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Message(self):
        r"""失败原因
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReleaseStatus(self):
        r"""发布状态
        :rtype: int
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def QaBizId(self):
        r"""QAID
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def DocBizId(self):
        r"""文档业务ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._Message = params.get("Message")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._QaBizId = params.get("QaBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseRejectedQuestion(AbstractModel):
    r"""发布拒答

    """

    def __init__(self):
        r"""
        :param _Question: 问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Action: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _ActionDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionDesc: str
        :param _Message: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None

    @property
    def Question(self):
        r"""问题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

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
    def Action(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        r"""状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        r"""失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameDocRequest(AbstractModel):
    r"""RenameDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginUin: 登录用户主账号(集成商模式必填)	
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _NewName: 新文档名，需要带上后缀
        :type NewName: str
        """
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._BotBizId = None
        self._DocBizId = None
        self._NewName = None

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def NewName(self):
        r"""新文档名，需要带上后缀
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameDocResponse(AbstractModel):
    r"""RenameDoc返回参数结构体

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


class RetryDocAuditRequest(AbstractModel):
    r"""RetryDocAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocAuditResponse(AbstractModel):
    r"""RetryDocAudit返回参数结构体

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


class RetryDocParseRequest(AbstractModel):
    r"""RetryDocParse请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 废弃
        :type DocBizId: str
        :param _DocBizIds: 集合最大上限50个，DocBizIds有值使用DocBizIds，为空时则使用DocBizId(兼容废弃字段)
        :type DocBizIds: list of str
        """
        self._BotBizId = None
        self._DocBizId = None
        self._DocBizIds = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""废弃
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def DocBizIds(self):
        r"""集合最大上限50个，DocBizIds有值使用DocBizIds，为空时则使用DocBizId(兼容废弃字段)
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._DocBizIds = params.get("DocBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocParseResponse(AbstractModel):
    r"""RetryDocParse返回参数结构体

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
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _ReleaseBizId: 发布业务ID
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        r"""机器人ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        r"""发布业务ID
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
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


class RunNodeInfo(AbstractModel):
    r"""节点信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型，0:未指定，1:开始节点，2:API节点，3:询问节点，4:答案节点
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: int
        :param _NodeId: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _InvokeApi: 请求的API
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeApi: :class:`tencentcloud.lke.v20231130.models.InvokeAPI`
        :param _SlotValues: 当前节点的所有槽位的值，key：SlotID。没有值的时候也要返回空。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotValues: list of ValueInfo
        """
        self._NodeType = None
        self._NodeId = None
        self._NodeName = None
        self._InvokeApi = None
        self._SlotValues = None

    @property
    def NodeType(self):
        r"""节点类型，0:未指定，1:开始节点，2:API节点，3:询问节点，4:答案节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        r"""节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def InvokeApi(self):
        r"""请求的API
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.InvokeAPI`
        """
        return self._InvokeApi

    @InvokeApi.setter
    def InvokeApi(self, InvokeApi):
        self._InvokeApi = InvokeApi

    @property
    def SlotValues(self):
        r"""当前节点的所有槽位的值，key：SlotID。没有值的时候也要返回空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ValueInfo
        """
        return self._SlotValues

    @SlotValues.setter
    def SlotValues(self, SlotValues):
        self._SlotValues = SlotValues


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        if params.get("InvokeApi") is not None:
            self._InvokeApi = InvokeAPI()
            self._InvokeApi._deserialize(params.get("InvokeApi"))
        if params.get("SlotValues") is not None:
            self._SlotValues = []
            for item in params.get("SlotValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._SlotValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDocRequest(AbstractModel):
    r"""SaveDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID，获取方法参看[如何获取   BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :type BotBizId: str
        :param _FileName: 文件名，需要包含文件扩展名
        :type FileName: str
        :param _FileType: 文档支持下面类型
pdf、doc、docx、ppt、mhtml、pptx、wps、ppsx，单个文件不超过200MB；
xlsx、xls、md、txt、csv、html，单个文件不超过20MB；

图片支持下面类型：
jpg、png、jpeg、tiff、bmp、gif，单个文件不超过50MB
        :type FileType: str
        :param _CosUrl: 平台cos路径，与DescribeStorageCredential接口查询UploadPath参数保持一致
        :type CosUrl: str
        :param _ETag: ETag 全称为 Entity Tag，是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化 成功上传cos后，从返回头中获取
        :type ETag: str
        :param _CosHash: cos_hash x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性  
成功上传cos后，从返回头中获取

请注意：
cos_hash为文档唯一性标识，与文件名无关 相同的cos_hash会被判定为重复文档
        :type CosHash: str
        :param _Size: 文件大小
        :type Size: str
        :param _AttrRange: 标签适用范围，1:全部，2:按条件。默认为1。
        :type AttrRange: int
        :param _Source: 来源（0 从本地文档导入），默认值为0
        :type Source: int
        :param _WebUrl: 自定义链接地址, IsRefer为true的时候，该值才有意义
        :type WebUrl: str
        :param _AttrLabels: 标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :type ReferUrlType: int
        :param _ExpireStart: 有效开始时间，unix秒级时间戳，默认为0
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix秒级时间戳，默认为0代表永久有效
        :type ExpireEnd: str
        :param _IsRefer: 是否显示引用的文档来源(false不显示 true显示）默认false
        :type IsRefer: bool
        :param _Opt: 文档操作类型：1：批量导入（批量导入问答对）；2:文档导入（正常导入单个文档） 默认为2 <br> 请注意，opt=1的时候请从腾讯云智能体开发平台页面下载excel模板
        :type Opt: int
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _IsDownload: 是否可下载，IsRefer为true并且ReferUrlType为0时，该值才有意义
        :type IsDownload: bool
        :param _DuplicateFileHandles: 重复文档处理方式，按顺序匹配第一个满足条件的方式处理
        :type DuplicateFileHandles: list of DuplicateFileHandle
        :param _SplitRule: 自定义切分规则

请求参数为一个 **JSON Object**，具体格式可参见接口示例值。包含以下主要字段：

| 字段名             | 类型      | 说明                                   |
|--------------------|--------|----------------------------------------|
| `xlsx_splitter`    | Object   | **Excel（xlsx）文件切分策略配置**，仅当处理 Excel 文件时有效 |
| `common_splitter`  | Object  | **通用文件（如 txt、pdf 等）切分策略配置**，按页或按标签切分 |
| `table_style`      | String | 表格内容的输出格式，如 HTML 或 Markdown |

---

## `xlsx_splitter`（Excel 切分策略）

用于配置 **表格文件的切分方式**。
**类型：Object**

```json
"xlsx_splitter": {
  "header_interval": [1, 2],
  "content_start": 10,
  "split_row": 2
}
```

### 字段说明：

| 字段名            | 类型   | 说明                                                                 |
|-------------------|--------|----------------------------------------------------------------------|
| `header_interval` | Array\<Number\>  | 表头所在的行区间，格式为 `[起始行, 结束行]`，**行号从 1 开始计数**。例如 `[1, 2]` 表示第 1~2 行为表头。 |
| `content_start`   | Number  | **表格内容的起始行号（从 1 开始）**。 |
| `split_row`       | Number   | **切分行数**。                   |

---
## `common_splitter`（通用文件切分策略）

用于配置 **非 Excel 文件（如 TXT、PDF、DOCX 等）的切分方式**，支持两种策略：**按页切分（page）** 或 **按标识符切分（tag）**。

**类型：Object**

```json
"common_splitter": {
  "splitter": "page",
  "page_splitter": {
    "chunk_length": 1000,
    "chunk_overlap_length": 100
  }
}
```

### 字段说明：

| 字段名            | 类型     | 说明                                                                 |
|-------------------|--------|---------------------------------------------------|
| `splitter`        | String  | 切分策略类型，可选值为：`"page"`（按页切分） 或 `"tag"`（按标识符切分）。 |
| `page_splitter`   | Object   | **按页切分的配置**。                                         |
| `page_splitter.chunk_length`   | 1000    | **切片最大长度**。              |
| `page_splitter.chunk_overlap_length`  | 100    | **切片重叠长度**。  |
| `tag_splitter`             | Object          | **自定义切分配置**。             |
| `tag_splitter.tag`         | Array\<String\>    | **切分标识符**。                             |
| `tag_splitter.chunk_length`| Number       | **切片最大长度**。                                                               |
| `tag_splitter.chunk_overlap_length` | Number    | **切块重叠长度**。                                                  |

🔹 **补充说明：**

- `splitter` 字段的值可以是：
  - `"page"`：只使用按页切分逻辑，此时只需要关心 `page_splitter` 相关字段。
  - `"tag"`：只使用按标识符（如分号、换行等）切分逻辑，此时关注 `tag_splitter`。
---

##  `table_style`（表格输出样式）

用于指定 **表格类内容（比如从 Excel 或 CSV 中提取的表格）最终以何种格式返回**，方便前端展示或后续处理。

**类型：String**

```json
"table_style": "md"
```

### 字段说明：

| 字段名       | 类型   | 说明                                                                 |
|--------------|--------|----------------------------------------------------------------------|
| `table_style` | String | 指定表格内容的输出格式。可用值：<br>• `"html"`：以 HTML 表格形式返回，适合网页展示。<br>• `"md"`：以 Markdown 表格语法返回，适合文档或 Markdown 渲染环境。|
        :type SplitRule: str
        :param _UpdatePeriodInfo: 文档更新频率，默认值为0不更新
        :type UpdatePeriodInfo: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        :param _EnableScope: 文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :type EnableScope: int
        """
        self._BotBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._ETag = None
        self._CosHash = None
        self._Size = None
        self._AttrRange = None
        self._Source = None
        self._WebUrl = None
        self._AttrLabels = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._IsRefer = None
        self._Opt = None
        self._CateBizId = None
        self._IsDownload = None
        self._DuplicateFileHandles = None
        self._SplitRule = None
        self._UpdatePeriodInfo = None
        self._EnableScope = None

    @property
    def BotBizId(self):
        r"""应用ID，获取方法参看[如何获取   BotBizId](https://cloud.tencent.com/document/product/1759/109469#4eecb8c1-6ce4-45f5-8fa2-b269449d8efa)
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        r"""文件名，需要包含文件扩展名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文档支持下面类型
pdf、doc、docx、ppt、mhtml、pptx、wps、ppsx，单个文件不超过200MB；
xlsx、xls、md、txt、csv、html，单个文件不超过20MB；

图片支持下面类型：
jpg、png、jpeg、tiff、bmp、gif，单个文件不超过50MB
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        r"""平台cos路径，与DescribeStorageCredential接口查询UploadPath参数保持一致
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def ETag(self):
        r"""ETag 全称为 Entity Tag，是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化 成功上传cos后，从返回头中获取
        :rtype: str
        """
        return self._ETag

    @ETag.setter
    def ETag(self, ETag):
        self._ETag = ETag

    @property
    def CosHash(self):
        r"""cos_hash x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性  
成功上传cos后，从返回头中获取

请注意：
cos_hash为文档唯一性标识，与文件名无关 相同的cos_hash会被判定为重复文档
        :rtype: str
        """
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        r"""文件大小
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AttrRange(self):
        r"""标签适用范围，1:全部，2:按条件。默认为1。
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def Source(self):
        r"""来源（0 从本地文档导入），默认值为0
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def WebUrl(self):
        r"""自定义链接地址, IsRefer为true的时候，该值才有意义
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def AttrLabels(self):
        r"""标签引用
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ReferUrlType(self):
        r"""外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        r"""有效开始时间，unix秒级时间戳，默认为0
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        r"""有效结束时间，unix秒级时间戳，默认为0代表永久有效
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def IsRefer(self):
        r"""是否显示引用的文档来源(false不显示 true显示）默认false
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def Opt(self):
        r"""文档操作类型：1：批量导入（批量导入问答对）；2:文档导入（正常导入单个文档） 默认为2 <br> 请注意，opt=1的时候请从腾讯云智能体开发平台页面下载excel模板
        :rtype: int
        """
        return self._Opt

    @Opt.setter
    def Opt(self, Opt):
        self._Opt = Opt

    @property
    def CateBizId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsDownload(self):
        r"""是否可下载，IsRefer为true并且ReferUrlType为0时，该值才有意义
        :rtype: bool
        """
        return self._IsDownload

    @IsDownload.setter
    def IsDownload(self, IsDownload):
        self._IsDownload = IsDownload

    @property
    def DuplicateFileHandles(self):
        r"""重复文档处理方式，按顺序匹配第一个满足条件的方式处理
        :rtype: list of DuplicateFileHandle
        """
        return self._DuplicateFileHandles

    @DuplicateFileHandles.setter
    def DuplicateFileHandles(self, DuplicateFileHandles):
        self._DuplicateFileHandles = DuplicateFileHandles

    @property
    def SplitRule(self):
        r"""自定义切分规则

请求参数为一个 **JSON Object**，具体格式可参见接口示例值。包含以下主要字段：

| 字段名             | 类型      | 说明                                   |
|--------------------|--------|----------------------------------------|
| `xlsx_splitter`    | Object   | **Excel（xlsx）文件切分策略配置**，仅当处理 Excel 文件时有效 |
| `common_splitter`  | Object  | **通用文件（如 txt、pdf 等）切分策略配置**，按页或按标签切分 |
| `table_style`      | String | 表格内容的输出格式，如 HTML 或 Markdown |

---

## `xlsx_splitter`（Excel 切分策略）

用于配置 **表格文件的切分方式**。
**类型：Object**

```json
"xlsx_splitter": {
  "header_interval": [1, 2],
  "content_start": 10,
  "split_row": 2
}
```

### 字段说明：

| 字段名            | 类型   | 说明                                                                 |
|-------------------|--------|----------------------------------------------------------------------|
| `header_interval` | Array\<Number\>  | 表头所在的行区间，格式为 `[起始行, 结束行]`，**行号从 1 开始计数**。例如 `[1, 2]` 表示第 1~2 行为表头。 |
| `content_start`   | Number  | **表格内容的起始行号（从 1 开始）**。 |
| `split_row`       | Number   | **切分行数**。                   |

---
## `common_splitter`（通用文件切分策略）

用于配置 **非 Excel 文件（如 TXT、PDF、DOCX 等）的切分方式**，支持两种策略：**按页切分（page）** 或 **按标识符切分（tag）**。

**类型：Object**

```json
"common_splitter": {
  "splitter": "page",
  "page_splitter": {
    "chunk_length": 1000,
    "chunk_overlap_length": 100
  }
}
```

### 字段说明：

| 字段名            | 类型     | 说明                                                                 |
|-------------------|--------|---------------------------------------------------|
| `splitter`        | String  | 切分策略类型，可选值为：`"page"`（按页切分） 或 `"tag"`（按标识符切分）。 |
| `page_splitter`   | Object   | **按页切分的配置**。                                         |
| `page_splitter.chunk_length`   | 1000    | **切片最大长度**。              |
| `page_splitter.chunk_overlap_length`  | 100    | **切片重叠长度**。  |
| `tag_splitter`             | Object          | **自定义切分配置**。             |
| `tag_splitter.tag`         | Array\<String\>    | **切分标识符**。                             |
| `tag_splitter.chunk_length`| Number       | **切片最大长度**。                                                               |
| `tag_splitter.chunk_overlap_length` | Number    | **切块重叠长度**。                                                  |

🔹 **补充说明：**

- `splitter` 字段的值可以是：
  - `"page"`：只使用按页切分逻辑，此时只需要关心 `page_splitter` 相关字段。
  - `"tag"`：只使用按标识符（如分号、换行等）切分逻辑，此时关注 `tag_splitter`。
---

##  `table_style`（表格输出样式）

用于指定 **表格类内容（比如从 Excel 或 CSV 中提取的表格）最终以何种格式返回**，方便前端展示或后续处理。

**类型：String**

```json
"table_style": "md"
```

### 字段说明：

| 字段名       | 类型   | 说明                                                                 |
|--------------|--------|----------------------------------------------------------------------|
| `table_style` | String | 指定表格内容的输出格式。可用值：<br>• `"html"`：以 HTML 表格形式返回，适合网页展示。<br>• `"md"`：以 Markdown 表格语法返回，适合文档或 Markdown 渲染环境。|
        :rtype: str
        """
        return self._SplitRule

    @SplitRule.setter
    def SplitRule(self, SplitRule):
        self._SplitRule = SplitRule

    @property
    def UpdatePeriodInfo(self):
        r"""文档更新频率，默认值为0不更新
        :rtype: :class:`tencentcloud.lke.v20231130.models.UpdatePeriodInfo`
        """
        return self._UpdatePeriodInfo

    @UpdatePeriodInfo.setter
    def UpdatePeriodInfo(self, UpdatePeriodInfo):
        self._UpdatePeriodInfo = UpdatePeriodInfo

    @property
    def EnableScope(self):
        r"""文档生效域: 1-停用；2-仅开发域；3-仅发布域；4-全域
        :rtype: int
        """
        return self._EnableScope

    @EnableScope.setter
    def EnableScope(self, EnableScope):
        self._EnableScope = EnableScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._ETag = params.get("ETag")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._AttrRange = params.get("AttrRange")
        self._Source = params.get("Source")
        self._WebUrl = params.get("WebUrl")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._IsRefer = params.get("IsRefer")
        self._Opt = params.get("Opt")
        self._CateBizId = params.get("CateBizId")
        self._IsDownload = params.get("IsDownload")
        if params.get("DuplicateFileHandles") is not None:
            self._DuplicateFileHandles = []
            for item in params.get("DuplicateFileHandles"):
                obj = DuplicateFileHandle()
                obj._deserialize(item)
                self._DuplicateFileHandles.append(obj)
        self._SplitRule = params.get("SplitRule")
        if params.get("UpdatePeriodInfo") is not None:
            self._UpdatePeriodInfo = UpdatePeriodInfo()
            self._UpdatePeriodInfo._deserialize(params.get("UpdatePeriodInfo"))
        self._EnableScope = params.get("EnableScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDocResponse(AbstractModel):
    r"""SaveDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _ErrorMsg: 导入错误信息
        :type ErrorMsg: str
        :param _ErrorLink: 错误链接
        :type ErrorLink: str
        :param _ErrorLinkText: 错误链接文本
        :type ErrorLinkText: str
        :param _DuplicateFileCheckType: 重复类型，0：未重复，其他取值请参考入参DuplicateFileHandle结构体的CheckType字段
        :type DuplicateFileCheckType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocBizId = None
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._DuplicateFileCheckType = None
        self._RequestId = None

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def ErrorMsg(self):
        r"""导入错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        r"""错误链接
        :rtype: str
        """
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        r"""错误链接文本
        :rtype: str
        """
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

    @property
    def DuplicateFileCheckType(self):
        r"""重复类型，0：未重复，其他取值请参考入参DuplicateFileHandle结构体的CheckType字段
        :rtype: int
        """
        return self._DuplicateFileCheckType

    @DuplicateFileCheckType.setter
    def DuplicateFileCheckType(self, DuplicateFileCheckType):
        self._DuplicateFileCheckType = DuplicateFileCheckType

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
        self._DocBizId = params.get("DocBizId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._DuplicateFileCheckType = params.get("DuplicateFileCheckType")
        self._RequestId = params.get("RequestId")


class SearchRange(AbstractModel):
    r"""检索范围配置

    """

    def __init__(self):
        r"""
        :param _Condition: 检索条件and/or
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: str
        :param _ApiVarAttrInfos: 自定义变量和标签关系数据	
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiVarAttrInfos: list of ApiVarAttrInfo
        """
        self._Condition = None
        self._ApiVarAttrInfos = None

    @property
    def Condition(self):
        r"""检索条件and/or
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ApiVarAttrInfos(self):
        r"""自定义变量和标签关系数据	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApiVarAttrInfo
        """
        return self._ApiVarAttrInfos

    @ApiVarAttrInfos.setter
    def ApiVarAttrInfos(self, ApiVarAttrInfos):
        self._ApiVarAttrInfos = ApiVarAttrInfos


    def _deserialize(self, params):
        self._Condition = params.get("Condition")
        if params.get("ApiVarAttrInfos") is not None:
            self._ApiVarAttrInfos = []
            for item in params.get("ApiVarAttrInfos"):
                obj = ApiVarAttrInfo()
                obj._deserialize(item)
                self._ApiVarAttrInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchStrategy(AbstractModel):
    r"""知识库检索策略

    """

    def __init__(self):
        r"""
        :param _StrategyType: 检索策略类型 0:混合检索，1：语义检索
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyType: int
        :param _TableEnhancement: Excel检索增强开关, false关闭，true打开
注意：此字段可能返回 null，表示取不到有效值。
        :type TableEnhancement: bool
        :param _EmbeddingModel: 向量模型
注意：此字段可能返回 null，表示取不到有效值。
        :type EmbeddingModel: str
        :param _RerankModelSwitch: 结果重排序开关， on打开，off关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type RerankModelSwitch: str
        :param _RerankModel: 结果重排序模型
注意：此字段可能返回 null，表示取不到有效值。
        :type RerankModel: str
        :param _NatureLanguageToSqlModelConfig: NL2SQL模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NatureLanguageToSqlModelConfig: :class:`tencentcloud.lke.v20231130.models.NL2SQLModelConfig`
        """
        self._StrategyType = None
        self._TableEnhancement = None
        self._EmbeddingModel = None
        self._RerankModelSwitch = None
        self._RerankModel = None
        self._NatureLanguageToSqlModelConfig = None

    @property
    def StrategyType(self):
        r"""检索策略类型 0:混合检索，1：语义检索
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def TableEnhancement(self):
        r"""Excel检索增强开关, false关闭，true打开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._TableEnhancement

    @TableEnhancement.setter
    def TableEnhancement(self, TableEnhancement):
        self._TableEnhancement = TableEnhancement

    @property
    def EmbeddingModel(self):
        r"""向量模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EmbeddingModel

    @EmbeddingModel.setter
    def EmbeddingModel(self, EmbeddingModel):
        self._EmbeddingModel = EmbeddingModel

    @property
    def RerankModelSwitch(self):
        r"""结果重排序开关， on打开，off关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RerankModelSwitch

    @RerankModelSwitch.setter
    def RerankModelSwitch(self, RerankModelSwitch):
        self._RerankModelSwitch = RerankModelSwitch

    @property
    def RerankModel(self):
        r"""结果重排序模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RerankModel

    @RerankModel.setter
    def RerankModel(self, RerankModel):
        self._RerankModel = RerankModel

    @property
    def NatureLanguageToSqlModelConfig(self):
        r"""NL2SQL模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.NL2SQLModelConfig`
        """
        return self._NatureLanguageToSqlModelConfig

    @NatureLanguageToSqlModelConfig.setter
    def NatureLanguageToSqlModelConfig(self, NatureLanguageToSqlModelConfig):
        self._NatureLanguageToSqlModelConfig = NatureLanguageToSqlModelConfig


    def _deserialize(self, params):
        self._StrategyType = params.get("StrategyType")
        self._TableEnhancement = params.get("TableEnhancement")
        self._EmbeddingModel = params.get("EmbeddingModel")
        self._RerankModelSwitch = params.get("RerankModelSwitch")
        self._RerankModel = params.get("RerankModel")
        if params.get("NatureLanguageToSqlModelConfig") is not None:
            self._NatureLanguageToSqlModelConfig = NL2SQLModelConfig()
            self._NatureLanguageToSqlModelConfig._deserialize(params.get("NatureLanguageToSqlModelConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareKnowledgeBase(AbstractModel):
    r"""共享知识库配置

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeBizId: str
        :param _SearchRange: 检索范围
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchRange: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        :param _KnowledgeModelConfig: 知识库模型设置
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeModelConfig: :class:`tencentcloud.lke.v20231130.models.KnowledgeModelConfig`
        :param _SearchStrategy: 检索策略配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchStrategy: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        :param _Search: 检索配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Search: list of KnowledgeQaSearch
        :param _ReplyFlexibility: // 问答-回复灵活度 1：已采纳答案直接回复 2：已采纳润色后回复
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyFlexibility: int
        :param _KnowledgeName: 共享知识库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeName: str
        """
        self._KnowledgeBizId = None
        self._SearchRange = None
        self._KnowledgeModelConfig = None
        self._SearchStrategy = None
        self._Search = None
        self._ReplyFlexibility = None
        self._KnowledgeName = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def SearchRange(self):
        r"""检索范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        """
        return self._SearchRange

    @SearchRange.setter
    def SearchRange(self, SearchRange):
        self._SearchRange = SearchRange

    @property
    def KnowledgeModelConfig(self):
        r"""知识库模型设置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeModelConfig`
        """
        return self._KnowledgeModelConfig

    @KnowledgeModelConfig.setter
    def KnowledgeModelConfig(self, KnowledgeModelConfig):
        self._KnowledgeModelConfig = KnowledgeModelConfig

    @property
    def SearchStrategy(self):
        r"""检索策略配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        """
        return self._SearchStrategy

    @SearchStrategy.setter
    def SearchStrategy(self, SearchStrategy):
        self._SearchStrategy = SearchStrategy

    @property
    def Search(self):
        r"""检索配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KnowledgeQaSearch
        """
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def ReplyFlexibility(self):
        r"""// 问答-回复灵活度 1：已采纳答案直接回复 2：已采纳润色后回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def KnowledgeName(self):
        r"""共享知识库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KnowledgeName

    @KnowledgeName.setter
    def KnowledgeName(self, KnowledgeName):
        self._KnowledgeName = KnowledgeName


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        if params.get("SearchRange") is not None:
            self._SearchRange = SearchRange()
            self._SearchRange._deserialize(params.get("SearchRange"))
        if params.get("KnowledgeModelConfig") is not None:
            self._KnowledgeModelConfig = KnowledgeModelConfig()
            self._KnowledgeModelConfig._deserialize(params.get("KnowledgeModelConfig"))
        if params.get("SearchStrategy") is not None:
            self._SearchStrategy = SearchStrategy()
            self._SearchStrategy._deserialize(params.get("SearchStrategy"))
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = KnowledgeQaSearch()
                obj._deserialize(item)
                self._Search.append(obj)
        self._ReplyFlexibility = params.get("ReplyFlexibility")
        self._KnowledgeName = params.get("KnowledgeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarQuestion(AbstractModel):
    r"""相似问信息

    """

    def __init__(self):
        r"""
        :param _SimBizId: 相似问ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SimBizId: str
        :param _Question: 相似问内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _AuditStatus: 相似问审核状态，1审核失败
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditStatus: int
        """
        self._SimBizId = None
        self._Question = None
        self._AuditStatus = None

    @property
    def SimBizId(self):
        r"""相似问ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SimBizId

    @SimBizId.setter
    def SimBizId(self, SimBizId):
        self._SimBizId = SimBizId

    @property
    def Question(self):
        r"""相似问内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def AuditStatus(self):
        r"""相似问审核状态，1审核失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus


    def _deserialize(self, params):
        self._SimBizId = params.get("SimBizId")
        self._Question = params.get("Question")
        self._AuditStatus = params.get("AuditStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarQuestionModify(AbstractModel):
    r"""相似问修改(更新)信息

    """

    def __init__(self):
        r"""
        :param _AddQuestions: 需要添加的相似问(内容)列表
        :type AddQuestions: list of str
        :param _UpdateQuestions: 需要更新的相似问列表
        :type UpdateQuestions: list of SimilarQuestion
        :param _DeleteQuestions: 需要删除的相似问列表
        :type DeleteQuestions: list of SimilarQuestion
        """
        self._AddQuestions = None
        self._UpdateQuestions = None
        self._DeleteQuestions = None

    @property
    def AddQuestions(self):
        r"""需要添加的相似问(内容)列表
        :rtype: list of str
        """
        return self._AddQuestions

    @AddQuestions.setter
    def AddQuestions(self, AddQuestions):
        self._AddQuestions = AddQuestions

    @property
    def UpdateQuestions(self):
        r"""需要更新的相似问列表
        :rtype: list of SimilarQuestion
        """
        return self._UpdateQuestions

    @UpdateQuestions.setter
    def UpdateQuestions(self, UpdateQuestions):
        self._UpdateQuestions = UpdateQuestions

    @property
    def DeleteQuestions(self):
        r"""需要删除的相似问列表
        :rtype: list of SimilarQuestion
        """
        return self._DeleteQuestions

    @DeleteQuestions.setter
    def DeleteQuestions(self, DeleteQuestions):
        self._DeleteQuestions = DeleteQuestions


    def _deserialize(self, params):
        self._AddQuestions = params.get("AddQuestions")
        if params.get("UpdateQuestions") is not None:
            self._UpdateQuestions = []
            for item in params.get("UpdateQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._UpdateQuestions.append(obj)
        if params.get("DeleteQuestions") is not None:
            self._DeleteQuestions = []
            for item in params.get("DeleteQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._DeleteQuestions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Stat(AbstractModel):
    r"""计费统计信息

    """

    def __init__(self):
        r"""
        :param _X: X轴: 时间区域；根据查询条件的粒度返回“分/小时/日”三种区间范围
注意：此字段可能返回 null，表示取不到有效值。
        :type X: str
        :param _Y: Y轴: 该时间区域内的统计值，如token消耗量，调用次数或使用量等信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""X轴: 时间区域；根据查询条件的粒度返回“分/小时/日”三种区间范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y轴: 该时间区域内的统计值，如token消耗量，调用次数或使用量等信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticInfo(AbstractModel):
    r"""大模型token统计信息

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _FirstTokenCost: 首Token耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTokenCost: int
        :param _TotalCost: 总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: int
        :param _InputTokens: 输入Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InputTokens: int
        :param _OutputTokens: 输出Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputTokens: int
        :param _TotalTokens: 总Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTokens: int
        """
        self._ModelName = None
        self._FirstTokenCost = None
        self._TotalCost = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def ModelName(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def FirstTokenCost(self):
        r"""首Token耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstTokenCost

    @FirstTokenCost.setter
    def FirstTokenCost(self, FirstTokenCost):
        self._FirstTokenCost = FirstTokenCost

    @property
    def TotalCost(self):
        r"""总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def InputTokens(self):
        r"""输入Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        r"""输出Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        r"""总Token数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._FirstTokenCost = params.get("FirstTokenCost")
        self._TotalCost = params.get("TotalCost")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDocParseRequest(AbstractModel):
    r"""StopDocParse请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        r"""文档ID
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDocParseResponse(AbstractModel):
    r"""StopDocParse返回参数结构体

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


class StopWorkflowRunRequest(AbstractModel):
    r"""StopWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _WorkflowRunId: 工作流运行实例ID
        :type WorkflowRunId: str
        """
        self._AppBizId = None
        self._WorkflowRunId = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWorkflowRunResponse(AbstractModel):
    r"""StopWorkflowRun返回参数结构体

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


class StrValue(AbstractModel):
    r"""字符串KV信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class StructuredOutputConfig(AbstractModel):
    r"""结构化输出的配置项

    """

    def __init__(self):
        r"""
        :param _StructuredOutputParams: 参数列表
        :type StructuredOutputParams: list of ParameterConfig
        """
        self._StructuredOutputParams = None

    @property
    def StructuredOutputParams(self):
        r"""参数列表
        :rtype: list of ParameterConfig
        """
        return self._StructuredOutputParams

    @StructuredOutputParams.setter
    def StructuredOutputParams(self, StructuredOutputParams):
        self._StructuredOutputParams = StructuredOutputParams


    def _deserialize(self, params):
        if params.get("StructuredOutputParams") is not None:
            self._StructuredOutputParams = []
            for item in params.get("StructuredOutputParams"):
                obj = ParameterConfig()
                obj._deserialize(item)
                self._StructuredOutputParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryConfig(AbstractModel):
    r"""知识摘要应用配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Output: 知识摘要输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.lke.v20231130.models.SummaryOutput`
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        """
        self._Model = None
        self._Output = None
        self._Greeting = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Output(self):
        r"""知识摘要输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lke.v20231130.models.SummaryOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Greeting(self):
        r"""欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Output") is not None:
            self._Output = SummaryOutput()
            self._Output._deserialize(params.get("Output"))
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryOutput(AbstractModel):
    r"""知识摘要输出配置

    """

    def __init__(self):
        r"""
        :param _Method: 输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: int
        :param _Requirement: 输出要求 1：文本总结 2：自定义要求
注意：此字段可能返回 null，表示取不到有效值。
        :type Requirement: int
        :param _RequireCommand: 自定义要求指令
注意：此字段可能返回 null，表示取不到有效值。
        :type RequireCommand: str
        """
        self._Method = None
        self._Requirement = None
        self._RequireCommand = None

    @property
    def Method(self):
        r"""输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Requirement(self):
        r"""输出要求 1：文本总结 2：自定义要求
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def RequireCommand(self):
        r"""自定义要求指令
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequireCommand

    @RequireCommand.setter
    def RequireCommand(self, RequireCommand):
        self._RequireCommand = RequireCommand


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Requirement = params.get("Requirement")
        self._RequireCommand = params.get("RequireCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFLowVar(AbstractModel):
    r"""变量详情

    """

    def __init__(self):
        r"""
        :param _VarId: 变量ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VarId: str
        :param _VarName: 变量名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VarName: str
        :param _VarDesc: 变量描述（默认为"-"）
        :type VarDesc: str
        :param _VarType: 变量类型 (STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO)

        :type VarType: str
        :param _VarDefaultValue: 自定义变量默认值
        :type VarDefaultValue: str
        :param _VarDefaultFileName: 自定义变量文件默认名称
        :type VarDefaultFileName: str
        :param _VarModuleType: 变量类型
        :type VarModuleType: int
        """
        self._VarId = None
        self._VarName = None
        self._VarDesc = None
        self._VarType = None
        self._VarDefaultValue = None
        self._VarDefaultFileName = None
        self._VarModuleType = None

    @property
    def VarId(self):
        r"""变量ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VarId

    @VarId.setter
    def VarId(self, VarId):
        self._VarId = VarId

    @property
    def VarName(self):
        r"""变量名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VarName

    @VarName.setter
    def VarName(self, VarName):
        self._VarName = VarName

    @property
    def VarDesc(self):
        r"""变量描述（默认为"-"）
        :rtype: str
        """
        return self._VarDesc

    @VarDesc.setter
    def VarDesc(self, VarDesc):
        self._VarDesc = VarDesc

    @property
    def VarType(self):
        r"""变量类型 (STRING,INT,FLOAT,BOOL,OBJECT,ARRAY_STRING,ARRAY_INT,ARRAY_FLOAT,ARRAY_BOOL,ARRAY_OBJECT,FILE,DOCUMENT,IMAGE,AUDIO)

        :rtype: str
        """
        return self._VarType

    @VarType.setter
    def VarType(self, VarType):
        self._VarType = VarType

    @property
    def VarDefaultValue(self):
        r"""自定义变量默认值
        :rtype: str
        """
        return self._VarDefaultValue

    @VarDefaultValue.setter
    def VarDefaultValue(self, VarDefaultValue):
        self._VarDefaultValue = VarDefaultValue

    @property
    def VarDefaultFileName(self):
        r"""自定义变量文件默认名称
        :rtype: str
        """
        return self._VarDefaultFileName

    @VarDefaultFileName.setter
    def VarDefaultFileName(self, VarDefaultFileName):
        self._VarDefaultFileName = VarDefaultFileName

    @property
    def VarModuleType(self):
        r"""变量类型
        :rtype: int
        """
        return self._VarModuleType

    @VarModuleType.setter
    def VarModuleType(self, VarModuleType):
        self._VarModuleType = VarModuleType


    def _deserialize(self, params):
        self._VarId = params.get("VarId")
        self._VarName = params.get("VarName")
        self._VarDesc = params.get("VarDesc")
        self._VarType = params.get("VarType")
        self._VarDefaultValue = params.get("VarDefaultValue")
        self._VarDefaultFileName = params.get("VarDefaultFileName")
        self._VarModuleType = params.get("VarModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowInfo(AbstractModel):
    r"""任务流程信息

    """

    def __init__(self):
        r"""
        :param _TaskFlowId: 任务流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlowId: str
        :param _TaskFlowName: 任务流程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlowName: str
        :param _QueryRewrite: Query 重写结果
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryRewrite: str
        :param _HitIntent: 命中意图
注意：此字段可能返回 null，表示取不到有效值。
        :type HitIntent: str
        :param _Type: 任务流程回复类型
0: 任务流回复
1: 任务流静默
2: 任务流拉回话术
3: 任务流自定义回复
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        """
        self._TaskFlowId = None
        self._TaskFlowName = None
        self._QueryRewrite = None
        self._HitIntent = None
        self._Type = None

    @property
    def TaskFlowId(self):
        r"""任务流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskFlowId

    @TaskFlowId.setter
    def TaskFlowId(self, TaskFlowId):
        self._TaskFlowId = TaskFlowId

    @property
    def TaskFlowName(self):
        r"""任务流程名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskFlowName

    @TaskFlowName.setter
    def TaskFlowName(self, TaskFlowName):
        self._TaskFlowName = TaskFlowName

    @property
    def QueryRewrite(self):
        r"""Query 重写结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueryRewrite

    @QueryRewrite.setter
    def QueryRewrite(self, QueryRewrite):
        self._QueryRewrite = QueryRewrite

    @property
    def HitIntent(self):
        r"""命中意图
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HitIntent

    @HitIntent.setter
    def HitIntent(self, HitIntent):
        self._HitIntent = HitIntent

    @property
    def Type(self):
        r"""任务流程回复类型
0: 任务流回复
1: 任务流静默
2: 任务流拉回话术
3: 任务流自定义回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TaskFlowId = params.get("TaskFlowId")
        self._TaskFlowName = params.get("TaskFlowName")
        self._QueryRewrite = params.get("QueryRewrite")
        self._HitIntent = params.get("HitIntent")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowSummary(AbstractModel):
    r"""任务流程调试信息

    """

    def __init__(self):
        r"""
        :param _IntentName: 任务流程名
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param _UpdatedSlotValues: 实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedSlotValues: list of ValueInfo
        :param _RunNodes: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RunNodes: list of RunNodeInfo
        :param _Purposes: 意图判断
注意：此字段可能返回 null，表示取不到有效值。
        :type Purposes: list of str
        """
        self._IntentName = None
        self._UpdatedSlotValues = None
        self._RunNodes = None
        self._Purposes = None

    @property
    def IntentName(self):
        r"""任务流程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IntentName

    @IntentName.setter
    def IntentName(self, IntentName):
        self._IntentName = IntentName

    @property
    def UpdatedSlotValues(self):
        r"""实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ValueInfo
        """
        return self._UpdatedSlotValues

    @UpdatedSlotValues.setter
    def UpdatedSlotValues(self, UpdatedSlotValues):
        self._UpdatedSlotValues = UpdatedSlotValues

    @property
    def RunNodes(self):
        r"""节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RunNodeInfo
        """
        return self._RunNodes

    @RunNodes.setter
    def RunNodes(self, RunNodes):
        self._RunNodes = RunNodes

    @property
    def Purposes(self):
        r"""意图判断
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Purposes

    @Purposes.setter
    def Purposes(self, Purposes):
        self._Purposes = Purposes


    def _deserialize(self, params):
        self._IntentName = params.get("IntentName")
        if params.get("UpdatedSlotValues") is not None:
            self._UpdatedSlotValues = []
            for item in params.get("UpdatedSlotValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._UpdatedSlotValues.append(obj)
        if params.get("RunNodes") is not None:
            self._RunNodes = []
            for item in params.get("RunNodes"):
                obj = RunNodeInfo()
                obj._deserialize(item)
                self._RunNodes.append(obj)
        self._Purposes = params.get("Purposes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskParams(AbstractModel):
    r"""任务参数

    """

    def __init__(self):
        r"""
        :param _CosPath: 下载地址,需要通过cos桶临时密钥去下载
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPath: str
        """
        self._CosPath = None

    @property
    def CosPath(self):
        r"""下载地址,需要通过cos桶临时密钥去下载
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath


    def _deserialize(self, params):
        self._CosPath = params.get("CosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenStat(AbstractModel):
    r"""当前执行的 token 统计信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _RequestId: 请求 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _RecordId: 对应哪条会话, 会话 ID, 用于回答的消息存储使用, 可提前生成, 保存消息时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _UsedCount: token 已使用数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCount: int
        :param _FreeCount: 免费 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeCount: int
        :param _OrderCount: 订单总 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderCount: int
        :param _StatusSummary: 当前执行状态汇总, 常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusSummary: str
        :param _StatusSummaryTitle: 当前执行状态汇总后中文展示
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusSummaryTitle: str
        :param _Elapsed: 当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Elapsed: int
        :param _TokenCount: 当前请求消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenCount: int
        :param _Procedures: 执行过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of Procedure
        :param _TraceId: 执行过程信息TraceId
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        """
        self._SessionId = None
        self._RequestId = None
        self._RecordId = None
        self._UsedCount = None
        self._FreeCount = None
        self._OrderCount = None
        self._StatusSummary = None
        self._StatusSummaryTitle = None
        self._Elapsed = None
        self._TokenCount = None
        self._Procedures = None
        self._TraceId = None

    @property
    def SessionId(self):
        r"""会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        r"""请求 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RecordId(self):
        r"""对应哪条会话, 会话 ID, 用于回答的消息存储使用, 可提前生成, 保存消息时使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def UsedCount(self):
        r"""token 已使用数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedCount

    @UsedCount.setter
    def UsedCount(self, UsedCount):
        self._UsedCount = UsedCount

    @property
    def FreeCount(self):
        r"""免费 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FreeCount

    @FreeCount.setter
    def FreeCount(self, FreeCount):
        self._FreeCount = FreeCount

    @property
    def OrderCount(self):
        r"""订单总 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def StatusSummary(self):
        r"""当前执行状态汇总, 常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusSummary

    @StatusSummary.setter
    def StatusSummary(self, StatusSummary):
        self._StatusSummary = StatusSummary

    @property
    def StatusSummaryTitle(self):
        r"""当前执行状态汇总后中文展示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusSummaryTitle

    @StatusSummaryTitle.setter
    def StatusSummaryTitle(self, StatusSummaryTitle):
        self._StatusSummaryTitle = StatusSummaryTitle

    @property
    def Elapsed(self):
        r"""当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def TokenCount(self):
        r"""当前请求消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TokenCount

    @TokenCount.setter
    def TokenCount(self, TokenCount):
        self._TokenCount = TokenCount

    @property
    def Procedures(self):
        r"""执行过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Procedure
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TraceId(self):
        r"""执行过程信息TraceId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")
        self._RecordId = params.get("RecordId")
        self._UsedCount = params.get("UsedCount")
        self._FreeCount = params.get("FreeCount")
        self._OrderCount = params.get("OrderCount")
        self._StatusSummary = params.get("StatusSummary")
        self._StatusSummaryTitle = params.get("StatusSummaryTitle")
        self._Elapsed = params.get("Elapsed")
        self._TokenCount = params.get("TokenCount")
        if params.get("Procedures") is not None:
            self._Procedures = []
            for item in params.get("Procedures"):
                obj = Procedure()
                obj._deserialize(item)
                self._Procedures.append(obj)
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnsatisfiedReply(AbstractModel):
    r"""不满意回复

    """

    def __init__(self):
        r"""
        :param _ReplyBizId: 不满意回复ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyBizId: str
        :param _RecordBizId: 消息记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordBizId: str
        :param _Question: 用户问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Answer: 问题回复
注意：此字段可能返回 null，表示取不到有效值。
        :type Answer: str
        :param _Reasons: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Reasons: list of str
        :param _Status: 处理状态，0：待处理，1：已拒答，2：已忽略，3：已纠错
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 创建时间，秒级时间戳
        :type CreateTime: str
        :param _UpdateTime: 更新时间,秒级时间戳
        :type UpdateTime: str
        :param _Operator: 操作人
        :type Operator: str
        :param _FeedbackContent: 自定义反馈
        :type FeedbackContent: str
        """
        self._ReplyBizId = None
        self._RecordBizId = None
        self._Question = None
        self._Answer = None
        self._Reasons = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Operator = None
        self._FeedbackContent = None

    @property
    def ReplyBizId(self):
        r"""不满意回复ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def RecordBizId(self):
        r"""消息记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def Question(self):
        r"""用户问题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        r"""问题回复
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Reasons(self):
        r"""错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def Status(self):
        r"""处理状态，0：待处理，1：已拒答，2：已忽略，3：已纠错
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间，秒级时间戳
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间,秒级时间戳
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        r"""操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FeedbackContent(self):
        r"""自定义反馈
        :rtype: str
        """
        return self._FeedbackContent

    @FeedbackContent.setter
    def FeedbackContent(self, FeedbackContent):
        self._FeedbackContent = FeedbackContent


    def _deserialize(self, params):
        self._ReplyBizId = params.get("ReplyBizId")
        self._RecordBizId = params.get("RecordBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Reasons = params.get("Reasons")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._FeedbackContent = params.get("FeedbackContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePeriodInfo(AbstractModel):
    r"""更新时间策略

    """

    def __init__(self):
        r"""
        :param _UpdatePeriodH: 文档更新频率类型：0不更新 -H 小时粒度,当前仅支持24(1天)，72(3天)，168(7天) 仅source=2 腾讯文档类型有效
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatePeriodH: int
        """
        self._UpdatePeriodH = None

    @property
    def UpdatePeriodH(self):
        r"""文档更新频率类型：0不更新 -H 小时粒度,当前仅支持24(1天)，72(3天)，168(7天) 仅source=2 腾讯文档类型有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdatePeriodH

    @UpdatePeriodH.setter
    def UpdatePeriodH(self, UpdatePeriodH):
        self._UpdatePeriodH = UpdatePeriodH


    def _deserialize(self, params):
        self._UpdatePeriodH = params.get("UpdatePeriodH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSharedKnowledgeRequest(AbstractModel):
    r"""UpdateSharedKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        :param _Info: 共享知识库更新信息
        :type Info: :class:`tencentcloud.lke.v20231130.models.KnowledgeUpdateInfo`
        """
        self._KnowledgeBizId = None
        self._Info = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

    @property
    def Info(self):
        r"""共享知识库更新信息
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeUpdateInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        if params.get("Info") is not None:
            self._Info = KnowledgeUpdateInfo()
            self._Info._deserialize(params.get("Info"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSharedKnowledgeResponse(AbstractModel):
    r"""UpdateSharedKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBizId: 共享知识库业务ID
        :type KnowledgeBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBizId = None
        self._RequestId = None

    @property
    def KnowledgeBizId(self):
        r"""共享知识库业务ID
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId

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
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        self._RequestId = params.get("RequestId")


class UpdateVarRequest(AbstractModel):
    r"""UpdateVar请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _VarId: 变量ID
        :type VarId: str
        :param _VarName: 变量名称，最大支持50个字符
        :type VarName: str
        :param _VarDesc: 参数描述
        :type VarDesc: str
        :param _VarType: 参数类型
        :type VarType: str
        :param _VarDefaultValue: 自定义变量默认值
        :type VarDefaultValue: str
        :param _VarDefaultFileName: 自定义变量文件默认名称
        :type VarDefaultFileName: str
        :param _VarModuleType: 变量类型
        :type VarModuleType: int
        """
        self._AppBizId = None
        self._VarId = None
        self._VarName = None
        self._VarDesc = None
        self._VarType = None
        self._VarDefaultValue = None
        self._VarDefaultFileName = None
        self._VarModuleType = None

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def VarId(self):
        r"""变量ID
        :rtype: str
        """
        return self._VarId

    @VarId.setter
    def VarId(self, VarId):
        self._VarId = VarId

    @property
    def VarName(self):
        r"""变量名称，最大支持50个字符
        :rtype: str
        """
        return self._VarName

    @VarName.setter
    def VarName(self, VarName):
        self._VarName = VarName

    @property
    def VarDesc(self):
        r"""参数描述
        :rtype: str
        """
        return self._VarDesc

    @VarDesc.setter
    def VarDesc(self, VarDesc):
        self._VarDesc = VarDesc

    @property
    def VarType(self):
        r"""参数类型
        :rtype: str
        """
        return self._VarType

    @VarType.setter
    def VarType(self, VarType):
        self._VarType = VarType

    @property
    def VarDefaultValue(self):
        r"""自定义变量默认值
        :rtype: str
        """
        return self._VarDefaultValue

    @VarDefaultValue.setter
    def VarDefaultValue(self, VarDefaultValue):
        self._VarDefaultValue = VarDefaultValue

    @property
    def VarDefaultFileName(self):
        r"""自定义变量文件默认名称
        :rtype: str
        """
        return self._VarDefaultFileName

    @VarDefaultFileName.setter
    def VarDefaultFileName(self, VarDefaultFileName):
        self._VarDefaultFileName = VarDefaultFileName

    @property
    def VarModuleType(self):
        r"""变量类型
        :rtype: int
        """
        return self._VarModuleType

    @VarModuleType.setter
    def VarModuleType(self, VarModuleType):
        self._VarModuleType = VarModuleType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._VarId = params.get("VarId")
        self._VarName = params.get("VarName")
        self._VarDesc = params.get("VarDesc")
        self._VarType = params.get("VarType")
        self._VarDefaultValue = params.get("VarDefaultValue")
        self._VarDefaultFileName = params.get("VarDefaultFileName")
        self._VarModuleType = params.get("VarModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateVarResponse(AbstractModel):
    r"""UpdateVar返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VarId: 变量ID
        :type VarId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VarId = None
        self._RequestId = None

    @property
    def VarId(self):
        r"""变量ID
        :rtype: str
        """
        return self._VarId

    @VarId.setter
    def VarId(self, VarId):
        self._VarId = VarId

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
        self._VarId = params.get("VarId")
        self._RequestId = params.get("RequestId")


class UploadAttributeLabelRequest(AbstractModel):
    r"""UploadAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _CosUrl: cos路径
        :type CosUrl: str
        :param _CosHash: x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性
        :type CosHash: str
        :param _Size: 文件大小
        :type Size: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._FileName = None
        self._CosUrl = None
        self._CosHash = None
        self._Size = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        r"""文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CosUrl(self):
        r"""cos路径
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def CosHash(self):
        r"""x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性
        :rtype: str
        """
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        r"""文件大小
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._CosUrl = params.get("CosUrl")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAttributeLabelResponse(AbstractModel):
    r"""UploadAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 导入错误
        :type ErrorMsg: str
        :param _ErrorLink: 错误链接
        :type ErrorLink: str
        :param _ErrorLinkText: 错误链接文本
        :type ErrorLinkText: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""导入错误
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        r"""错误链接
        :rtype: str
        """
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        r"""错误链接文本
        :rtype: str
        """
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._RequestId = params.get("RequestId")


class UserBaseInfo(AbstractModel):
    r"""用户基础信息

    """

    def __init__(self):
        r"""
        :param _UserBizId: 用户ID
        :type UserBizId: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._UserBizId = None
        self._UserName = None

    @property
    def UserBizId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserBizId

    @UserBizId.setter
    def UserBizId(self, UserBizId):
        self._UserBizId = UserBizId

    @property
    def UserName(self):
        r"""用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserBizId = params.get("UserBizId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueInfo(AbstractModel):
    r"""任务流程参数信息

    """

    def __init__(self):
        r"""
        :param _Id: 值ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ValueType: 值类型：0:未知或者空, 1:string, 2:int, 3:float, 4:bool, 5:array(字符串数组), 6: object_array(结构体数组), 7: object(结构体)
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueType: int
        :param _ValueStr: string
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueStr: str
        :param _ValueInt: int（避免精度丢失使用字符串返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueInt: str
        :param _ValueFloat: float
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueFloat: float
        :param _ValueBool: bool
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueBool: bool
        :param _ValueStrArray: array
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueStrArray: list of str
        """
        self._Id = None
        self._Name = None
        self._ValueType = None
        self._ValueStr = None
        self._ValueInt = None
        self._ValueFloat = None
        self._ValueBool = None
        self._ValueStrArray = None

    @property
    def Id(self):
        r"""值ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ValueType(self):
        r"""值类型：0:未知或者空, 1:string, 2:int, 3:float, 4:bool, 5:array(字符串数组), 6: object_array(结构体数组), 7: object(结构体)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ValueStr(self):
        r"""string
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValueStr

    @ValueStr.setter
    def ValueStr(self, ValueStr):
        self._ValueStr = ValueStr

    @property
    def ValueInt(self):
        r"""int（避免精度丢失使用字符串返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValueInt

    @ValueInt.setter
    def ValueInt(self, ValueInt):
        self._ValueInt = ValueInt

    @property
    def ValueFloat(self):
        r"""float
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._ValueFloat

    @ValueFloat.setter
    def ValueFloat(self, ValueFloat):
        self._ValueFloat = ValueFloat

    @property
    def ValueBool(self):
        r"""bool
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ValueBool

    @ValueBool.setter
    def ValueBool(self, ValueBool):
        self._ValueBool = ValueBool

    @property
    def ValueStrArray(self):
        r"""array
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ValueStrArray

    @ValueStrArray.setter
    def ValueStrArray(self, ValueStrArray):
        self._ValueStrArray = ValueStrArray


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ValueType = params.get("ValueType")
        self._ValueStr = params.get("ValueStr")
        self._ValueInt = params.get("ValueInt")
        self._ValueFloat = params.get("ValueFloat")
        self._ValueBool = params.get("ValueBool")
        self._ValueStrArray = params.get("ValueStrArray")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQARequest(AbstractModel):
    r"""VerifyQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 问答列表
        :type List: list of QAList
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _KnowledgeBizId: 用于操作共享知识库
        :type KnowledgeBizId: str
        """
        self._List = None
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._KnowledgeBizId = None

    @property
    def List(self):
        r"""问答列表
        :rtype: list of QAList
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def BotBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        r"""登录用户主账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""登录用户子账号(集成商模式必填)
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def KnowledgeBizId(self):
        r"""用于操作共享知识库
        :rtype: str
        """
        return self._KnowledgeBizId

    @KnowledgeBizId.setter
    def KnowledgeBizId(self, KnowledgeBizId):
        self._KnowledgeBizId = KnowledgeBizId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QAList()
                obj._deserialize(item)
                self._List.append(obj)
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._KnowledgeBizId = params.get("KnowledgeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQAResponse(AbstractModel):
    r"""VerifyQA返回参数结构体

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


class VoiceConfig(AbstractModel):
    r"""音色参数

    """

    def __init__(self):
        r"""
        :param _VoiceType: 公有云音色id
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceType: int
        :param _TimbreKey: 音色key
注意：此字段可能返回 null，表示取不到有效值。
        :type TimbreKey: str
        :param _VoiceName: 音色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceName: str
        """
        self._VoiceType = None
        self._TimbreKey = None
        self._VoiceName = None

    @property
    def VoiceType(self):
        r"""公有云音色id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def TimbreKey(self):
        r"""音色key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimbreKey

    @TimbreKey.setter
    def TimbreKey(self, TimbreKey):
        self._TimbreKey = TimbreKey

    @property
    def VoiceName(self):
        r"""音色名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName


    def _deserialize(self, params):
        self._VoiceType = params.get("VoiceType")
        self._TimbreKey = params.get("TimbreKey")
        self._VoiceName = params.get("VoiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkFlowSummary(AbstractModel):
    r"""工作流程调试信息

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowRunId: 工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _RunNodes: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RunNodes: list of WorkflowRunNodeInfo
        :param _OptionCards: 选项卡
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionCards: list of str
        :param _Outputs: 多气泡的输出结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Outputs: list of str
        :param _WorkflowReleaseTime: 工作流发布时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowReleaseTime: str
        :param _PendingMessages: 中间消息
        :type PendingMessages: list of str
        :param _OptionCardIndex: 选项卡索引
        :type OptionCardIndex: :class:`tencentcloud.lke.v20231130.models.OptionCardIndex`
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowRunId = None
        self._RunNodes = None
        self._OptionCards = None
        self._Outputs = None
        self._WorkflowReleaseTime = None
        self._PendingMessages = None
        self._OptionCardIndex = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowRunId(self):
        r"""工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def RunNodes(self):
        r"""节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowRunNodeInfo
        """
        return self._RunNodes

    @RunNodes.setter
    def RunNodes(self, RunNodes):
        self._RunNodes = RunNodes

    @property
    def OptionCards(self):
        r"""选项卡
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def Outputs(self):
        r"""多气泡的输出结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def WorkflowReleaseTime(self):
        r"""工作流发布时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowReleaseTime

    @WorkflowReleaseTime.setter
    def WorkflowReleaseTime(self, WorkflowReleaseTime):
        self._WorkflowReleaseTime = WorkflowReleaseTime

    @property
    def PendingMessages(self):
        r"""中间消息
        :rtype: list of str
        """
        return self._PendingMessages

    @PendingMessages.setter
    def PendingMessages(self, PendingMessages):
        self._PendingMessages = PendingMessages

    @property
    def OptionCardIndex(self):
        r"""选项卡索引
        :rtype: :class:`tencentcloud.lke.v20231130.models.OptionCardIndex`
        """
        return self._OptionCardIndex

    @OptionCardIndex.setter
    def OptionCardIndex(self, OptionCardIndex):
        self._OptionCardIndex = OptionCardIndex


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowRunId = params.get("WorkflowRunId")
        if params.get("RunNodes") is not None:
            self._RunNodes = []
            for item in params.get("RunNodes"):
                obj = WorkflowRunNodeInfo()
                obj._deserialize(item)
                self._RunNodes.append(obj)
        self._OptionCards = params.get("OptionCards")
        self._Outputs = params.get("Outputs")
        self._WorkflowReleaseTime = params.get("WorkflowReleaseTime")
        self._PendingMessages = params.get("PendingMessages")
        if params.get("OptionCardIndex") is not None:
            self._OptionCardIndex = OptionCardIndex()
            self._OptionCardIndex._deserialize(params.get("OptionCardIndex"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    r"""工作流信息

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowRunId: 工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _OptionCards: 选项卡
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionCards: list of str
        :param _Outputs: 多气泡的输出结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Outputs: list of str
        :param _WorkflowReleaseTime: 工作流发布时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowReleaseTime: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowRunId = None
        self._OptionCards = None
        self._Outputs = None
        self._WorkflowReleaseTime = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowRunId(self):
        r"""工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def OptionCards(self):
        r"""选项卡
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def Outputs(self):
        r"""多气泡的输出结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def WorkflowReleaseTime(self):
        r"""工作流发布时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowReleaseTime

    @WorkflowReleaseTime.setter
    def WorkflowReleaseTime(self, WorkflowReleaseTime):
        self._WorkflowReleaseTime = WorkflowReleaseTime


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._OptionCards = params.get("OptionCards")
        self._Outputs = params.get("Outputs")
        self._WorkflowReleaseTime = params.get("WorkflowReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRef(AbstractModel):
    r"""WorkflowRef详情

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 任务流ID
        :type WorkflowId: str
        :param _WorkflowName: 任务流名称
        :type WorkflowName: str
        :param _WorkflowDesc: 任务流描述
        :type WorkflowDesc: str
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowDesc = None
        self._AppBizId = None
        self._UpdateTime = None

    @property
    def WorkflowId(self):
        r"""任务流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""任务流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowDesc(self):
        r"""任务流描述
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._AppBizId = params.get("AppBizId")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRunBase(AbstractModel):
    r"""工作流运行实例的基本信息

    """

    def __init__(self):
        r"""
        :param _RunEnv: 运行环境。0: 测试环境； 1: 正式环境
        :type RunEnv: int
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _WorkflowRunId: 工作流运行实例的ID
        :type WorkflowRunId: str
        :param _WorkflowId: 所属工作流ID
        :type WorkflowId: str
        :param _Name: 名称
        :type Name: str
        :param _State: 运行状态。0: 排队中；1: 运行中；2: 运行成功；3: 运行失败； 4: 已取消
        :type State: int
        :param _FailMessage: 错误信息
        :type FailMessage: str
        :param _TotalTokens: 消耗的token总数
        :type TotalTokens: int
        :param _CreateTime: 创建时间（毫秒时间戳）
        :type CreateTime: str
        :param _StartTime: 开始时间（毫秒时间戳）
        :type StartTime: str
        :param _EndTime: 结束时间（毫秒时间戳）
        :type EndTime: str
        """
        self._RunEnv = None
        self._AppBizId = None
        self._WorkflowRunId = None
        self._WorkflowId = None
        self._Name = None
        self._State = None
        self._FailMessage = None
        self._TotalTokens = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None

    @property
    def RunEnv(self):
        r"""运行环境。0: 测试环境； 1: 正式环境
        :rtype: int
        """
        return self._RunEnv

    @RunEnv.setter
    def RunEnv(self, RunEnv):
        self._RunEnv = RunEnv

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例的ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def WorkflowId(self):
        r"""所属工作流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def State(self):
        r"""运行状态。0: 排队中；1: 运行中；2: 运行成功；3: 运行失败； 4: 已取消
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FailMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def TotalTokens(self):
        r"""消耗的token总数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def CreateTime(self):
        r"""创建时间（毫秒时间戳）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""开始时间（毫秒时间戳）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（毫秒时间戳）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._RunEnv = params.get("RunEnv")
        self._AppBizId = params.get("AppBizId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._WorkflowId = params.get("WorkflowId")
        self._Name = params.get("Name")
        self._State = params.get("State")
        self._FailMessage = params.get("FailMessage")
        self._TotalTokens = params.get("TotalTokens")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRunDetail(AbstractModel):
    r"""工作流运行实例详情

    """

    def __init__(self):
        r"""
        :param _RunEnv: 运行环境。0: 测试环境； 1: 正式环境
        :type RunEnv: int
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _WorkflowRunId: 工作流运行实例的ID
        :type WorkflowRunId: str
        :param _WorkflowId: 所属工作流ID
        :type WorkflowId: str
        :param _Name: 名称
        :type Name: str
        :param _Output: 工作流输出
        :type Output: str
        :param _State: 运行状态。0: 排队中；1: 运行中；2: 运行成功；3: 运行失败； 4: 已取消
        :type State: int
        :param _FailMessage: 错误信息
        :type FailMessage: str
        :param _TotalTokens: 消耗的token总数
        :type TotalTokens: int
        :param _CreateTime: 创建时间（毫秒时间戳）
        :type CreateTime: str
        :param _StartTime: 开始时间（毫秒时间戳）
        :type StartTime: str
        :param _EndTime: 结束时间（毫秒时间戳）
        :type EndTime: str
        :param _DialogJson: 工作流画布Json
        :type DialogJson: str
        :param _Query: 用户的输入
        :type Query: str
        :param _MainModelName: 主模型名称
        :type MainModelName: str
        :param _CustomVariables: API参数配置
        :type CustomVariables: list of CustomVariable
        :param _WorkflowGraph: 工作流的流程图
        :type WorkflowGraph: str
        """
        self._RunEnv = None
        self._AppBizId = None
        self._WorkflowRunId = None
        self._WorkflowId = None
        self._Name = None
        self._Output = None
        self._State = None
        self._FailMessage = None
        self._TotalTokens = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._DialogJson = None
        self._Query = None
        self._MainModelName = None
        self._CustomVariables = None
        self._WorkflowGraph = None

    @property
    def RunEnv(self):
        r"""运行环境。0: 测试环境； 1: 正式环境
        :rtype: int
        """
        return self._RunEnv

    @RunEnv.setter
    def RunEnv(self, RunEnv):
        self._RunEnv = RunEnv

    @property
    def AppBizId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def WorkflowRunId(self):
        r"""工作流运行实例的ID
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def WorkflowId(self):
        r"""所属工作流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Output(self):
        r"""工作流输出
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def State(self):
        r"""运行状态。0: 排队中；1: 运行中；2: 运行成功；3: 运行失败； 4: 已取消
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FailMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def TotalTokens(self):
        r"""消耗的token总数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def CreateTime(self):
        r"""创建时间（毫秒时间戳）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""开始时间（毫秒时间戳）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（毫秒时间戳）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DialogJson(self):
        warnings.warn("parameter `DialogJson` is deprecated", DeprecationWarning) 

        r"""工作流画布Json
        :rtype: str
        """
        return self._DialogJson

    @DialogJson.setter
    def DialogJson(self, DialogJson):
        warnings.warn("parameter `DialogJson` is deprecated", DeprecationWarning) 

        self._DialogJson = DialogJson

    @property
    def Query(self):
        r"""用户的输入
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def MainModelName(self):
        r"""主模型名称
        :rtype: str
        """
        return self._MainModelName

    @MainModelName.setter
    def MainModelName(self, MainModelName):
        self._MainModelName = MainModelName

    @property
    def CustomVariables(self):
        r"""API参数配置
        :rtype: list of CustomVariable
        """
        return self._CustomVariables

    @CustomVariables.setter
    def CustomVariables(self, CustomVariables):
        self._CustomVariables = CustomVariables

    @property
    def WorkflowGraph(self):
        r"""工作流的流程图
        :rtype: str
        """
        return self._WorkflowGraph

    @WorkflowGraph.setter
    def WorkflowGraph(self, WorkflowGraph):
        self._WorkflowGraph = WorkflowGraph


    def _deserialize(self, params):
        self._RunEnv = params.get("RunEnv")
        self._AppBizId = params.get("AppBizId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._WorkflowId = params.get("WorkflowId")
        self._Name = params.get("Name")
        self._Output = params.get("Output")
        self._State = params.get("State")
        self._FailMessage = params.get("FailMessage")
        self._TotalTokens = params.get("TotalTokens")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DialogJson = params.get("DialogJson")
        self._Query = params.get("Query")
        self._MainModelName = params.get("MainModelName")
        if params.get("CustomVariables") is not None:
            self._CustomVariables = []
            for item in params.get("CustomVariables"):
                obj = CustomVariable()
                obj._deserialize(item)
                self._CustomVariables.append(obj)
        self._WorkflowGraph = params.get("WorkflowGraph")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRunNodeInfo(AbstractModel):
    r"""工作流运行节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _NodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: int
        :param _NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Input: 输入
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param _Output: 输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _TaskOutput: 任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskOutput: str
        :param _FailMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMessage: str
        :param _CostMilliSeconds: 花费时长
注意：此字段可能返回 null，表示取不到有效值。
        :type CostMilliSeconds: int
        :param _StatisticInfos: 大模型输出信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticInfos: list of StatisticInfo
        :param _FailCode: 错误代码
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCode: str
        """
        self._NodeId = None
        self._NodeType = None
        self._NodeName = None
        self._Status = None
        self._Input = None
        self._Output = None
        self._TaskOutput = None
        self._FailMessage = None
        self._CostMilliSeconds = None
        self._StatisticInfos = None
        self._FailCode = None

    @property
    def NodeId(self):
        r"""节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeType(self):
        r"""节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeName(self):
        r"""节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        r"""输入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""输出
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def TaskOutput(self):
        r"""任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskOutput

    @TaskOutput.setter
    def TaskOutput(self, TaskOutput):
        self._TaskOutput = TaskOutput

    @property
    def FailMessage(self):
        r"""错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def CostMilliSeconds(self):
        r"""花费时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CostMilliSeconds

    @CostMilliSeconds.setter
    def CostMilliSeconds(self, CostMilliSeconds):
        self._CostMilliSeconds = CostMilliSeconds

    @property
    def StatisticInfos(self):
        r"""大模型输出信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StatisticInfo
        """
        return self._StatisticInfos

    @StatisticInfos.setter
    def StatisticInfos(self, StatisticInfos):
        self._StatisticInfos = StatisticInfos

    @property
    def FailCode(self):
        r"""错误代码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeType = params.get("NodeType")
        self._NodeName = params.get("NodeName")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._TaskOutput = params.get("TaskOutput")
        self._FailMessage = params.get("FailMessage")
        self._CostMilliSeconds = params.get("CostMilliSeconds")
        if params.get("StatisticInfos") is not None:
            self._StatisticInfos = []
            for item in params.get("StatisticInfos"):
                obj = StatisticInfo()
                obj._deserialize(item)
                self._StatisticInfos.append(obj)
        self._FailCode = params.get("FailCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class YuanQi(AbstractModel):
    r"""//智能体应用可见范围，public-所有人可见 private-仅自己可见 share-通过分享可见

    """

    def __init__(self):
        r"""
        :param _VisibleRange: public-所有人可见
        :type VisibleRange: str
        """
        self._VisibleRange = None

    @property
    def VisibleRange(self):
        r"""public-所有人可见
        :rtype: str
        """
        return self._VisibleRange

    @VisibleRange.setter
    def VisibleRange(self, VisibleRange):
        self._VisibleRange = VisibleRange


    def _deserialize(self, params):
        self._VisibleRange = params.get("VisibleRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        