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


class Agent(AbstractModel):
    r"""智能体

    """

    def __init__(self):
        r"""
        :param _AgentId: 智能体Id
        :type AgentId: str
        :param _AgentName: 智能体名称
        :type AgentName: str
        :param _AgentInternalName: 智能体类型
        :type AgentInternalName: str
        :param _DeployPlace: 架构：共享版-intranet，企业版-userVpc
        :type DeployPlace: str
        :param _AgentStatus: 智能体状态
        :type AgentStatus: str
        :param _DefaultVersion: 默认版本
        :type DefaultVersion: str
        :param _AgentType: 智能体模式
        :type AgentType: str
        :param _Description: 描述
        :type Description: str
        :param _Creator: 创建者
        :type Creator: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Updater: 更新者
        :type Updater: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._AgentId = None
        self._AgentName = None
        self._AgentInternalName = None
        self._DeployPlace = None
        self._AgentStatus = None
        self._DefaultVersion = None
        self._AgentType = None
        self._Description = None
        self._Creator = None
        self._CreateTime = None
        self._Updater = None
        self._UpdateTime = None

    @property
    def AgentId(self):
        r"""智能体Id
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""智能体名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AgentInternalName(self):
        r"""智能体类型
        :rtype: str
        """
        return self._AgentInternalName

    @AgentInternalName.setter
    def AgentInternalName(self, AgentInternalName):
        self._AgentInternalName = AgentInternalName

    @property
    def DeployPlace(self):
        r"""架构：共享版-intranet，企业版-userVpc
        :rtype: str
        """
        return self._DeployPlace

    @DeployPlace.setter
    def DeployPlace(self, DeployPlace):
        self._DeployPlace = DeployPlace

    @property
    def AgentStatus(self):
        r"""智能体状态
        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def DefaultVersion(self):
        r"""默认版本
        :rtype: str
        """
        return self._DefaultVersion

    @DefaultVersion.setter
    def DefaultVersion(self, DefaultVersion):
        self._DefaultVersion = DefaultVersion

    @property
    def AgentType(self):
        r"""智能体模式
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

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
    def Creator(self):
        r"""创建者
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
    def Updater(self):
        r"""更新者
        :rtype: str
        """
        return self._Updater

    @Updater.setter
    def Updater(self, Updater):
        self._Updater = Updater

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._AgentInternalName = params.get("AgentInternalName")
        self._DeployPlace = params.get("DeployPlace")
        self._AgentStatus = params.get("AgentStatus")
        self._DefaultVersion = params.get("DefaultVersion")
        self._AgentType = params.get("AgentType")
        self._Description = params.get("Description")
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        self._Updater = params.get("Updater")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDutyTask(AbstractModel):
    r"""智能体值守任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _StartTime: 任务开始运行时间
        :type StartTime: str
        :param _FinishTime: 任务结束时间
        :type FinishTime: str
        :param _Status: 任务状态
        :type Status: str
        :param _ResultExtraKey: 对外展示的Extra信息
        :type ResultExtraKey: list of str
        :param _Extra: 业务的额外敏感信息
        :type Extra: list of ExtraInfo
        """
        self._TaskId = None
        self._CreateTime = None
        self._StartTime = None
        self._FinishTime = None
        self._Status = None
        self._ResultExtraKey = None
        self._Extra = None

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
    def CreateTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""任务开始运行时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        r"""任务结束时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Status(self):
        r"""任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultExtraKey(self):
        r"""对外展示的Extra信息
        :rtype: list of str
        """
        return self._ResultExtraKey

    @ResultExtraKey.setter
    def ResultExtraKey(self, ResultExtraKey):
        self._ResultExtraKey = ResultExtraKey

    @property
    def Extra(self):
        r"""业务的额外敏感信息
        :rtype: list of ExtraInfo
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._Status = params.get("Status")
        self._ResultExtraKey = params.get("ResultExtraKey")
        if params.get("Extra") is not None:
            self._Extra = []
            for item in params.get("Extra"):
                obj = ExtraInfo()
                obj._deserialize(item)
                self._Extra.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentInstance(AbstractModel):
    r"""智能体实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>智能体实例ID</p>
        :type InstanceId: str
        :param _InstanceName: <p>智能体实例名称</p>
        :type InstanceName: str
        :param _AgentId: <p>智能体ID</p>
        :type AgentId: str
        :param _AgentName: <p>智能体名称</p>
        :type AgentName: str
        :param _AgentInternalName: <p>智能体类型</p>
        :type AgentInternalName: str
        :param _AgentType: <p>智能体服务模式</p>
        :type AgentType: str
        :param _AgentVersion: <p>智能体版本</p>
        :type AgentVersion: str
        :param _Status: <p>智能体实例状态</p>
        :type Status: str
        :param _Parameters: <p>智能体实例参数列表</p>
        :type Parameters: list of Parameter
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _UpdateTime: <p>修改时间</p>
        :type UpdateTime: str
        :param _Tags: <p>资源绑定Tag列表</p>
        :type Tags: list of TagItem
        :param _DeployPlace: <p>部署位置,intranet-共享版，userVpc-专享版</p>
        :type DeployPlace: str
        :param _PolicyIds: <p>关联的告警策略ID。</p>
        :type PolicyIds: list of str
        :param _ClawConfig: <p>无</p>
        :type ClawConfig: :class:`tencentcloud.tdai.v20250717.models.ClawConfigInfo`
        :param _InstanceType: <p>无</p>
        :type InstanceType: str
        :param _AllowedActions: <p>无</p>
        :type AllowedActions: list of str
        :param _LastActiveTime: <p>无</p>
        :type LastActiveTime: str
        :param _Description: <p>无</p>
        :type Description: str
        :param _CreatingProgress: <p>发货进度详情</p>
        :type CreatingProgress: :class:`tencentcloud.tdai.v20250717.models.CreatingProgress`
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AgentId = None
        self._AgentName = None
        self._AgentInternalName = None
        self._AgentType = None
        self._AgentVersion = None
        self._Status = None
        self._Parameters = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Tags = None
        self._DeployPlace = None
        self._PolicyIds = None
        self._ClawConfig = None
        self._InstanceType = None
        self._AllowedActions = None
        self._LastActiveTime = None
        self._Description = None
        self._CreatingProgress = None

    @property
    def InstanceId(self):
        r"""<p>智能体实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>智能体实例名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AgentId(self):
        r"""<p>智能体ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""<p>智能体名称</p>
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AgentInternalName(self):
        r"""<p>智能体类型</p>
        :rtype: str
        """
        return self._AgentInternalName

    @AgentInternalName.setter
    def AgentInternalName(self, AgentInternalName):
        self._AgentInternalName = AgentInternalName

    @property
    def AgentType(self):
        r"""<p>智能体服务模式</p>
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def AgentVersion(self):
        r"""<p>智能体版本</p>
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def Status(self):
        r"""<p>智能体实例状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Parameters(self):
        r"""<p>智能体实例参数列表</p>
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

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
    def UpdateTime(self):
        r"""<p>修改时间</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Tags(self):
        r"""<p>资源绑定Tag列表</p>
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeployPlace(self):
        r"""<p>部署位置,intranet-共享版，userVpc-专享版</p>
        :rtype: str
        """
        return self._DeployPlace

    @DeployPlace.setter
    def DeployPlace(self, DeployPlace):
        self._DeployPlace = DeployPlace

    @property
    def PolicyIds(self):
        r"""<p>关联的告警策略ID。</p>
        :rtype: list of str
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ClawConfig(self):
        r"""<p>无</p>
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ClawConfigInfo`
        """
        return self._ClawConfig

    @ClawConfig.setter
    def ClawConfig(self, ClawConfig):
        self._ClawConfig = ClawConfig

    @property
    def InstanceType(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AllowedActions(self):
        r"""<p>无</p>
        :rtype: list of str
        """
        return self._AllowedActions

    @AllowedActions.setter
    def AllowedActions(self, AllowedActions):
        self._AllowedActions = AllowedActions

    @property
    def LastActiveTime(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._LastActiveTime

    @LastActiveTime.setter
    def LastActiveTime(self, LastActiveTime):
        self._LastActiveTime = LastActiveTime

    @property
    def Description(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatingProgress(self):
        r"""<p>发货进度详情</p>
        :rtype: :class:`tencentcloud.tdai.v20250717.models.CreatingProgress`
        """
        return self._CreatingProgress

    @CreatingProgress.setter
    def CreatingProgress(self, CreatingProgress):
        self._CreatingProgress = CreatingProgress


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._AgentInternalName = params.get("AgentInternalName")
        self._AgentType = params.get("AgentType")
        self._AgentVersion = params.get("AgentVersion")
        self._Status = params.get("Status")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = Parameter()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeployPlace = params.get("DeployPlace")
        self._PolicyIds = params.get("PolicyIds")
        if params.get("ClawConfig") is not None:
            self._ClawConfig = ClawConfigInfo()
            self._ClawConfig._deserialize(params.get("ClawConfig"))
        self._InstanceType = params.get("InstanceType")
        self._AllowedActions = params.get("AllowedActions")
        self._LastActiveTime = params.get("LastActiveTime")
        self._Description = params.get("Description")
        if params.get("CreatingProgress") is not None:
            self._CreatingProgress = CreatingProgress()
            self._CreatingProgress._deserialize(params.get("CreatingProgress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatBrief(AbstractModel):
    r"""会话信息

    """

    def __init__(self):
        r"""
        :param _AppId: 主账号Id
        :type AppId: int
        :param _Uin: 主账号uin
        :type Uin: str
        :param _OwnerUin: 子账号uin
        :type OwnerUin: str
        :param _InstanceId: 智能体实例ID
        :type InstanceId: str
        :param _ChatId: 会话ID
        :type ChatId: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _Title: 会话标题
        :type Title: str
        :param _Status: 会话状态
        :type Status: str
        :param _LastStreamingId: 最后一条流式ID
        :type LastStreamingId: str
        :param _LastStreamingTokenId: 最后一条流式TokenID
        :type LastStreamingTokenId: int
        """
        self._AppId = None
        self._Uin = None
        self._OwnerUin = None
        self._InstanceId = None
        self._ChatId = None
        self._CreateTime = None
        self._Title = None
        self._Status = None
        self._LastStreamingId = None
        self._LastStreamingTokenId = None

    @property
    def AppId(self):
        r"""主账号Id
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def OwnerUin(self):
        r"""子账号uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InstanceId(self):
        r"""智能体实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话ID
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Title(self):
        r"""会话标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        r"""会话状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastStreamingId(self):
        r"""最后一条流式ID
        :rtype: str
        """
        return self._LastStreamingId

    @LastStreamingId.setter
    def LastStreamingId(self, LastStreamingId):
        self._LastStreamingId = LastStreamingId

    @property
    def LastStreamingTokenId(self):
        r"""最后一条流式TokenID
        :rtype: int
        """
        return self._LastStreamingTokenId

    @LastStreamingTokenId.setter
    def LastStreamingTokenId(self, LastStreamingTokenId):
        self._LastStreamingTokenId = LastStreamingTokenId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._OwnerUin = params.get("OwnerUin")
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._CreateTime = params.get("CreateTime")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._LastStreamingId = params.get("LastStreamingId")
        self._LastStreamingTokenId = params.get("LastStreamingTokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatDetail(AbstractModel):
    r"""会话详情

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _UserMessage: 用户消息
        :type UserMessage: str
        :param _AssistantMessage: 助手消息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssistantMessage: list of CreateChatCompletionRes
        """
        self._Role = None
        self._UserMessage = None
        self._AssistantMessage = None

    @property
    def Role(self):
        r"""角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def UserMessage(self):
        r"""用户消息
        :rtype: str
        """
        return self._UserMessage

    @UserMessage.setter
    def UserMessage(self, UserMessage):
        self._UserMessage = UserMessage

    @property
    def AssistantMessage(self):
        r"""助手消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CreateChatCompletionRes
        """
        return self._AssistantMessage

    @AssistantMessage.setter
    def AssistantMessage(self, AssistantMessage):
        self._AssistantMessage = AssistantMessage


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._UserMessage = params.get("UserMessage")
        if params.get("AssistantMessage") is not None:
            self._AssistantMessage = []
            for item in params.get("AssistantMessage"):
                obj = CreateChatCompletionRes()
                obj._deserialize(item)
                self._AssistantMessage.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawConfigInfo(AbstractModel):
    r"""databaseClaw实例配置信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>无</p>
        :type TemplateId: int
        :param _DbTypes: <p>无</p>
        :type DbTypes: list of str
        :param _Deploy: <p>无</p>
        :type Deploy: :class:`tencentcloud.tdai.v20250717.models.ClawDeployInfo`
        """
        self._TemplateId = None
        self._DbTypes = None
        self._Deploy = None

    @property
    def TemplateId(self):
        r"""<p>无</p>
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DbTypes(self):
        r"""<p>无</p>
        :rtype: list of str
        """
        return self._DbTypes

    @DbTypes.setter
    def DbTypes(self, DbTypes):
        self._DbTypes = DbTypes

    @property
    def Deploy(self):
        r"""<p>无</p>
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ClawDeployInfo`
        """
        return self._Deploy

    @Deploy.setter
    def Deploy(self, Deploy):
        self._Deploy = Deploy


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._DbTypes = params.get("DbTypes")
        if params.get("Deploy") is not None:
            self._Deploy = ClawDeployInfo()
            self._Deploy._deserialize(params.get("Deploy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawDeployInfo(AbstractModel):
    r"""databaseClaw实例部署详情

    """

    def __init__(self):
        r"""
        :param _UserVpcId: <p>无</p>
        :type UserVpcId: str
        :param _UserSubnetId: <p>无</p>
        :type UserSubnetId: str
        :param _UserVpcRegion: <p>无</p>
        :type UserVpcRegion: str
        """
        self._UserVpcId = None
        self._UserSubnetId = None
        self._UserVpcRegion = None

    @property
    def UserVpcId(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._UserVpcId

    @UserVpcId.setter
    def UserVpcId(self, UserVpcId):
        self._UserVpcId = UserVpcId

    @property
    def UserSubnetId(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def UserVpcRegion(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._UserVpcRegion

    @UserVpcRegion.setter
    def UserVpcRegion(self, UserVpcRegion):
        self._UserVpcRegion = UserVpcRegion


    def _deserialize(self, params):
        self._UserVpcId = params.get("UserVpcId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._UserVpcRegion = params.get("UserVpcRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeRepo(AbstractModel):
    r"""仓库信息

    """

    def __init__(self):
        r"""
        :param _RepoUrl: 代码仓库地址
        :type RepoUrl: str
        :param _Branch: 分支名
        :type Branch: str
        :param _GitCommitPipelines: Commit信息
        :type GitCommitPipelines: list of str
        :param _GitORMType: 数据库ORM类型
        :type GitORMType: str
        :param _GitCodeLanguage: 代码编写语言
        :type GitCodeLanguage: str
        """
        self._RepoUrl = None
        self._Branch = None
        self._GitCommitPipelines = None
        self._GitORMType = None
        self._GitCodeLanguage = None

    @property
    def RepoUrl(self):
        r"""代码仓库地址
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def Branch(self):
        r"""分支名
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def GitCommitPipelines(self):
        r"""Commit信息
        :rtype: list of str
        """
        return self._GitCommitPipelines

    @GitCommitPipelines.setter
    def GitCommitPipelines(self, GitCommitPipelines):
        self._GitCommitPipelines = GitCommitPipelines

    @property
    def GitORMType(self):
        r"""数据库ORM类型
        :rtype: str
        """
        return self._GitORMType

    @GitORMType.setter
    def GitORMType(self, GitORMType):
        self._GitORMType = GitORMType

    @property
    def GitCodeLanguage(self):
        r"""代码编写语言
        :rtype: str
        """
        return self._GitCodeLanguage

    @GitCodeLanguage.setter
    def GitCodeLanguage(self, GitCodeLanguage):
        self._GitCodeLanguage = GitCodeLanguage


    def _deserialize(self, params):
        self._RepoUrl = params.get("RepoUrl")
        self._Branch = params.get("Branch")
        self._GitCommitPipelines = params.get("GitCommitPipelines")
        self._GitORMType = params.get("GitORMType")
        self._GitCodeLanguage = params.get("GitCodeLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueAgentWorkRequest(AbstractModel):
    r"""ContinueAgentWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        :param _AgentTaskType: Agent任务类型
        :type AgentTaskType: str
        """
        self._InstanceId = None
        self._AgentTaskType = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentTaskType(self):
        r"""Agent任务类型
        :rtype: str
        """
        return self._AgentTaskType

    @AgentTaskType.setter
    def AgentTaskType(self, AgentTaskType):
        self._AgentTaskType = AgentTaskType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentTaskType = params.get("AgentTaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueAgentWorkResponse(AbstractModel):
    r"""ContinueAgentWork返回参数结构体

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


class CreateAgentInstanceRequest(AbstractModel):
    r"""CreateAgentInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>智能体ID</p>
        :type AgentId: str
        :param _AgentVersion: <p>智能体版本</p>
        :type AgentVersion: str
        :param _InstanceName: <p>实例名</p>
        :type InstanceName: str
        :param _Parameters: <p>智能体实例的参数列表</p>
        :type Parameters: list of Parameter
        :param _Tags: <p>资源的标签信息</p>
        :type Tags: list of TagItem
        :param _InstanceType: <p>无</p>
        :type InstanceType: str
        :param _TemplateId: <p>无</p>
        :type TemplateId: int
        :param _Skills: <p>无</p>
        :type Skills: list of str
        :param _SoulId: <p>无</p>
        :type SoulId: int
        :param _Description: <p>无</p>
        :type Description: str
        """
        self._AgentId = None
        self._AgentVersion = None
        self._InstanceName = None
        self._Parameters = None
        self._Tags = None
        self._InstanceType = None
        self._TemplateId = None
        self._Skills = None
        self._SoulId = None
        self._Description = None

    @property
    def AgentId(self):
        r"""<p>智能体ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentVersion(self):
        r"""<p>智能体版本</p>
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def InstanceName(self):
        r"""<p>实例名</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Parameters(self):
        r"""<p>智能体实例的参数列表</p>
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Tags(self):
        r"""<p>资源的标签信息</p>
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceType(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def TemplateId(self):
        r"""<p>无</p>
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Skills(self):
        r"""<p>无</p>
        :rtype: list of str
        """
        return self._Skills

    @Skills.setter
    def Skills(self, Skills):
        self._Skills = Skills

    @property
    def SoulId(self):
        r"""<p>无</p>
        :rtype: int
        """
        return self._SoulId

    @SoulId.setter
    def SoulId(self, SoulId):
        self._SoulId = SoulId

    @property
    def Description(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentVersion = params.get("AgentVersion")
        self._InstanceName = params.get("InstanceName")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = Parameter()
                obj._deserialize(item)
                self._Parameters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._TemplateId = params.get("TemplateId")
        self._Skills = params.get("Skills")
        self._SoulId = params.get("SoulId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentInstanceResponse(AbstractModel):
    r"""CreateAgentInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>智能体实例ID</p>
        :type InstanceId: str
        :param _InstanceName: <p>智能体实例名称</p>
        :type InstanceName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>智能体实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>智能体实例名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
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
        self._InstanceName = params.get("InstanceName")
        self._RequestId = params.get("RequestId")


class CreateChatCompletionRequest(AbstractModel):
    r"""CreateChatCompletion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputContent: <p>输入内容</p>
        :type InputContent: str
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _ChatId: <p>对话窗口ID，空值表示新的会话</p>
        :type ChatId: str
        :param _IsHidden: <p>是否隐藏</p>
        :type IsHidden: bool
        :param _IsChatHidden: <p>是否隐藏会话</p>
        :type IsChatHidden: bool
        """
        self._InputContent = None
        self._InstanceId = None
        self._ChatId = None
        self._IsHidden = None
        self._IsChatHidden = None

    @property
    def InputContent(self):
        r"""<p>输入内容</p>
        :rtype: str
        """
        return self._InputContent

    @InputContent.setter
    def InputContent(self, InputContent):
        self._InputContent = InputContent

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""<p>对话窗口ID，空值表示新的会话</p>
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def IsHidden(self):
        r"""<p>是否隐藏</p>
        :rtype: bool
        """
        return self._IsHidden

    @IsHidden.setter
    def IsHidden(self, IsHidden):
        self._IsHidden = IsHidden

    @property
    def IsChatHidden(self):
        r"""<p>是否隐藏会话</p>
        :rtype: bool
        """
        return self._IsChatHidden

    @IsChatHidden.setter
    def IsChatHidden(self, IsChatHidden):
        self._IsChatHidden = IsChatHidden


    def _deserialize(self, params):
        self._InputContent = params.get("InputContent")
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._IsHidden = params.get("IsHidden")
        self._IsChatHidden = params.get("IsChatHidden")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChatCompletionRes(AbstractModel):
    r"""对话接口出参

    """

    def __init__(self):
        r"""
        :param _Object: 枚举值，返回的数据类型
        :type Object: str
        :param _Created: 消息时间戳
        :type Created: int
        :param _Model: 输出模型
        :type Model: str
        :param _AppId: 用户标识
        :type AppId: int
        :param _OwnerUin: 主账户标识
        :type OwnerUin: str
        :param _Uin: 当前账户标识
        :type Uin: str
        :param _RequestId: Request ID

        :type RequestId: str
        :param _ChatId: 当前会话ID
        :type ChatId: str
        :param _StreamingId: 当前流ID
        :type StreamingId: str
        :param _TaskId: 当前任务ID
        :type TaskId: str
        :param _Choices: 消息的数据详情
        :type Choices: list of UploadChoice
        """
        self._Object = None
        self._Created = None
        self._Model = None
        self._AppId = None
        self._OwnerUin = None
        self._Uin = None
        self._RequestId = None
        self._ChatId = None
        self._StreamingId = None
        self._TaskId = None
        self._Choices = None

    @property
    def Object(self):
        r"""枚举值，返回的数据类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Created(self):
        r"""消息时间戳
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Model(self):
        r"""输出模型
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def AppId(self):
        r"""用户标识
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        r"""主账户标识
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Uin(self):
        r"""当前账户标识
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        r"""Request ID

        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def ChatId(self):
        r"""当前会话ID
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def StreamingId(self):
        r"""当前流ID
        :rtype: str
        """
        return self._StreamingId

    @StreamingId.setter
    def StreamingId(self, StreamingId):
        self._StreamingId = StreamingId

    @property
    def TaskId(self):
        r"""当前任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Choices(self):
        r"""消息的数据详情
        :rtype: list of UploadChoice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices


    def _deserialize(self, params):
        self._Object = params.get("Object")
        self._Created = params.get("Created")
        self._Model = params.get("Model")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")
        self._ChatId = params.get("ChatId")
        self._StreamingId = params.get("StreamingId")
        self._TaskId = params.get("TaskId")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = UploadChoice()
                obj._deserialize(item)
                self._Choices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChatCompletionResponse(AbstractModel):
    r"""CreateChatCompletion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateMemoryPlusSpaceRequest(AbstractModel):
    r"""CreateMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>Memory 实例的自定义名称，用于唯一标识和管理实例。支持 60 个字符内的中英文、数字、中划线（-）及下划线（_）。</p>
        :type Name: str
        :param _Description: <p>emory 实例的简要描述，包括使用场景、用途或背景信息，便于日常运维识别。长度限制为 0-200 个字符。</p>
        :type Description: str
        :param _ResourceTags: <p>以键值对（Key-Value）形式为 Memory 实例绑定的标签，用于项目管理、成本分摊、环境隔离等场景。</p>
        :type ResourceTags: list of ResourceTag
        :param _GoodsNum: <p>单次批量创建 Memory 实例的数量。取值范围为 1-50。</p>
        :type GoodsNum: int
        """
        self._Name = None
        self._Description = None
        self._ResourceTags = None
        self._GoodsNum = None

    @property
    def Name(self):
        r"""<p>Memory 实例的自定义名称，用于唯一标识和管理实例。支持 60 个字符内的中英文、数字、中划线（-）及下划线（_）。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>emory 实例的简要描述，包括使用场景、用途或背景信息，便于日常运维识别。长度限制为 0-200 个字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ResourceTags(self):
        r"""<p>以键值对（Key-Value）形式为 Memory 实例绑定的标签，用于项目管理、成本分摊、环境隔离等场景。</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def GoodsNum(self):
        r"""<p>单次批量创建 Memory 实例的数量。取值范围为 1-50。</p>
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMemoryPlusSpaceResponse(AbstractModel):
    r"""CreateMemoryPlusSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: <p>实例 ID 列表。</p>
        :type SpaceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceIds = None
        self._RequestId = None

    @property
    def SpaceIds(self):
        r"""<p>实例 ID 列表。</p>
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        self._RequestId = params.get("RequestId")


class CreatingProgress(AbstractModel):
    r"""发货步骤描述

    """

    def __init__(self):
        r"""
        :param _TotalSteps: <p>总步骤数</p>
        :type TotalSteps: int
        :param _CurrentStep: <p>当前步骤</p>
        :type CurrentStep: int
        :param _Steps: <p>步骤详情</p>
        :type Steps: list of CreatingStepInfo
        """
        self._TotalSteps = None
        self._CurrentStep = None
        self._Steps = None

    @property
    def TotalSteps(self):
        r"""<p>总步骤数</p>
        :rtype: int
        """
        return self._TotalSteps

    @TotalSteps.setter
    def TotalSteps(self, TotalSteps):
        self._TotalSteps = TotalSteps

    @property
    def CurrentStep(self):
        r"""<p>当前步骤</p>
        :rtype: int
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def Steps(self):
        r"""<p>步骤详情</p>
        :rtype: list of CreatingStepInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps


    def _deserialize(self, params):
        self._TotalSteps = params.get("TotalSteps")
        self._CurrentStep = params.get("CurrentStep")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = CreatingStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatingStepInfo(AbstractModel):
    r"""发货步骤详情

    """

    def __init__(self):
        r"""
        :param _StepName: <p>步骤名称</p>
        :type StepName: str
        :param _StepDesc: <p>步骤描述</p>
        :type StepDesc: str
        :param _Status: <p>步骤状态</p>
        :type Status: str
        :param _FinishTime: <p>完成时间</p>
        :type FinishTime: str
        :param _ErrMsg: <p>错误信息描述</p>
        :type ErrMsg: str
        """
        self._StepName = None
        self._StepDesc = None
        self._Status = None
        self._FinishTime = None
        self._ErrMsg = None

    @property
    def StepName(self):
        r"""<p>步骤名称</p>
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepDesc(self):
        r"""<p>步骤描述</p>
        :rtype: str
        """
        return self._StepDesc

    @StepDesc.setter
    def StepDesc(self, StepDesc):
        self._StepDesc = StepDesc

    @property
    def Status(self):
        r"""<p>步骤状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FinishTime(self):
        r"""<p>完成时间</p>
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ErrMsg(self):
        r"""<p>错误信息描述</p>
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._StepDesc = params.get("StepDesc")
        self._Status = params.get("Status")
        self._FinishTime = params.get("FinishTime")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDutyTaskDetailRequest(AbstractModel):
    r"""DescribeAgentDutyTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Parameters: 业务参数列表
        :type Parameters: list of Parameter
        """
        self._Parameters = None

    @property
    def Parameters(self):
        r"""业务参数列表
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = Parameter()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDutyTaskDetailResponse(AbstractModel):
    r"""DescribeAgentDutyTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentDutyTask: 任务详细信息
        :type AgentDutyTask: :class:`tencentcloud.tdai.v20250717.models.AgentDutyTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentDutyTask = None
        self._RequestId = None

    @property
    def AgentDutyTask(self):
        r"""任务详细信息
        :rtype: :class:`tencentcloud.tdai.v20250717.models.AgentDutyTask`
        """
        return self._AgentDutyTask

    @AgentDutyTask.setter
    def AgentDutyTask(self, AgentDutyTask):
        self._AgentDutyTask = AgentDutyTask

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AgentDutyTask") is not None:
            self._AgentDutyTask = AgentDutyTask()
            self._AgentDutyTask._deserialize(params.get("AgentDutyTask"))
        self._RequestId = params.get("RequestId")


class DescribeAgentDutyTasksRequest(AbstractModel):
    r"""DescribeAgentDutyTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: agent实例ID
        :type InstanceId: str
        :param _ChatId: 会话ID
        :type ChatId: str
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 列表查询数量
        :type Limit: int
        :param _StartTime: 任务启动时间
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _AgentTaskType: 任务类型
        :type AgentTaskType: str
        :param _Parameters: 业务参数
        :type Parameters: list of Parameter
        """
        self._InstanceId = None
        self._ChatId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._AgentTaskType = None
        self._Parameters = None

    @property
    def InstanceId(self):
        r"""agent实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话ID
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def Offset(self):
        r"""查询开始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""列表查询数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        r"""任务启动时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AgentTaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._AgentTaskType

    @AgentTaskType.setter
    def AgentTaskType(self, AgentTaskType):
        self._AgentTaskType = AgentTaskType

    @property
    def Parameters(self):
        r"""业务参数
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AgentTaskType = params.get("AgentTaskType")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = Parameter()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDutyTasksResponse(AbstractModel):
    r"""DescribeAgentDutyTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果总数量
        :type TotalCount: int
        :param _DutyTasks: 任务详细信息
        :type DutyTasks: list of AgentDutyTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DutyTasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询结果总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DutyTasks(self):
        r"""任务详细信息
        :rtype: list of AgentDutyTask
        """
        return self._DutyTasks

    @DutyTasks.setter
    def DutyTasks(self, DutyTasks):
        self._DutyTasks = DutyTasks

    @property
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
        if params.get("DutyTasks") is not None:
            self._DutyTasks = []
            for item in params.get("DutyTasks"):
                obj = AgentDutyTask()
                obj._deserialize(item)
                self._DutyTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentInstanceRequest(AbstractModel):
    r"""DescribeAgentInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
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
        


class DescribeAgentInstanceResponse(AbstractModel):
    r"""DescribeAgentInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentInstance: 智能体实例详情
        :type AgentInstance: :class:`tencentcloud.tdai.v20250717.models.AgentInstance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentInstance = None
        self._RequestId = None

    @property
    def AgentInstance(self):
        r"""智能体实例详情
        :rtype: :class:`tencentcloud.tdai.v20250717.models.AgentInstance`
        """
        return self._AgentInstance

    @AgentInstance.setter
    def AgentInstance(self, AgentInstance):
        self._AgentInstance = AgentInstance

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AgentInstance") is not None:
            self._AgentInstance = AgentInstance()
            self._AgentInstance._deserialize(params.get("AgentInstance"))
        self._RequestId = params.get("RequestId")


class DescribeAgentInstancesRequest(AbstractModel):
    r"""DescribeAgentInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 列表查询数量
        :type Limit: int
        :param _InstanceId: <p>实例ID，为空时查询所有，如果填写则会根据InstanceId筛选</p>
        :type InstanceId: str
        :param _InstanceName: <p>实例名，为空时查询所有，如果填写则会根据InstanceName筛选</p>
        :type InstanceName: str
        :param _AgentId: <p>智能体ID，为空时查询所有，如果填写则会根据AgentId筛选</p>
        :type AgentId: str
        :param _AgentName: <p>智能体名称，为空时查询所有，如果填写则会根据AgentName筛选</p>
        :type AgentName: str
        :param _AgentInternalName: <p>智能体类型，为空时查询所有，如果填写则会根据AgentName筛选</p>
        :type AgentInternalName: str
        :param _Status: <p>智能体实例状态，为空时查询所有，如果填写则会根据Status筛选</p>
        :type Status: str
        :param _TagFilter: <p>标签过滤信息</p>
        :type TagFilter: list of TagFilter
        :param _InstanceType: <p>实例类型</p>
        :type InstanceType: str
        """
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._InstanceName = None
        self._AgentId = None
        self._AgentName = None
        self._AgentInternalName = None
        self._Status = None
        self._TagFilter = None
        self._InstanceType = None

    @property
    def Offset(self):
        r"""查询开始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""列表查询数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        r"""<p>实例ID，为空时查询所有，如果填写则会根据InstanceId筛选</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>实例名，为空时查询所有，如果填写则会根据InstanceName筛选</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AgentId(self):
        r"""<p>智能体ID，为空时查询所有，如果填写则会根据AgentId筛选</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""<p>智能体名称，为空时查询所有，如果填写则会根据AgentName筛选</p>
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AgentInternalName(self):
        r"""<p>智能体类型，为空时查询所有，如果填写则会根据AgentName筛选</p>
        :rtype: str
        """
        return self._AgentInternalName

    @AgentInternalName.setter
    def AgentInternalName(self, AgentInternalName):
        self._AgentInternalName = AgentInternalName

    @property
    def Status(self):
        r"""<p>智能体实例状态，为空时查询所有，如果填写则会根据Status筛选</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagFilter(self):
        r"""<p>标签过滤信息</p>
        :rtype: list of TagFilter
        """
        return self._TagFilter

    @TagFilter.setter
    def TagFilter(self, TagFilter):
        self._TagFilter = TagFilter

    @property
    def InstanceType(self):
        r"""<p>实例类型</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._AgentInternalName = params.get("AgentInternalName")
        self._Status = params.get("Status")
        if params.get("TagFilter") is not None:
            self._TagFilter = []
            for item in params.get("TagFilter"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilter.append(obj)
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentInstancesResponse(AbstractModel):
    r"""DescribeAgentInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果总数量
        :type TotalCount: int
        :param _Items: <p>智能体实例列表</p>
        :type Items: list of AgentInstance
        :param _StatusCounts: <p>无</p>
        :type StatusCounts: list of StatusItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._StatusCounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询结果总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""<p>智能体实例列表</p>
        :rtype: list of AgentInstance
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def StatusCounts(self):
        r"""<p>无</p>
        :rtype: list of StatusItem
        """
        return self._StatusCounts

    @StatusCounts.setter
    def StatusCounts(self, StatusCounts):
        self._StatusCounts = StatusCounts

    @property
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AgentInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("StatusCounts") is not None:
            self._StatusCounts = []
            for item in params.get("StatusCounts"):
                obj = StatusItem()
                obj._deserialize(item)
                self._StatusCounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentsRequest(AbstractModel):
    r"""DescribeAgents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 列表查询数量
        :type Limit: int
        :param _AgentId: 智能体ID，为空时查询所有，如果填写则会根据AgentId筛选
        :type AgentId: str
        :param _AgentName: 智能体名称，为空时查询所有，如果填写则会根据AgentName筛选
        :type AgentName: str
        :param _AgentInternalName: 智能体类型，为空时查询所有，如果填写则会根据AgentName筛选
        :type AgentInternalName: str
        :param _AgentStatus: 智能体状态，为空时查询所有，如果填写则会根据AgentStatus筛选
        :type AgentStatus: str
        :param _DeployPlace: 架构，共享版-intranet，企业版-userVpc
        :type DeployPlace: str
        """
        self._Offset = None
        self._Limit = None
        self._AgentId = None
        self._AgentName = None
        self._AgentInternalName = None
        self._AgentStatus = None
        self._DeployPlace = None

    @property
    def Offset(self):
        r"""查询开始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""列表查询数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AgentId(self):
        r"""智能体ID，为空时查询所有，如果填写则会根据AgentId筛选
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""智能体名称，为空时查询所有，如果填写则会根据AgentName筛选
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def AgentInternalName(self):
        r"""智能体类型，为空时查询所有，如果填写则会根据AgentName筛选
        :rtype: str
        """
        return self._AgentInternalName

    @AgentInternalName.setter
    def AgentInternalName(self, AgentInternalName):
        self._AgentInternalName = AgentInternalName

    @property
    def AgentStatus(self):
        r"""智能体状态，为空时查询所有，如果填写则会根据AgentStatus筛选
        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def DeployPlace(self):
        r"""架构，共享版-intranet，企业版-userVpc
        :rtype: str
        """
        return self._DeployPlace

    @DeployPlace.setter
    def DeployPlace(self, DeployPlace):
        self._DeployPlace = DeployPlace


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._AgentInternalName = params.get("AgentInternalName")
        self._AgentStatus = params.get("AgentStatus")
        self._DeployPlace = params.get("DeployPlace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentsResponse(AbstractModel):
    r"""DescribeAgents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果总数量
        :type TotalCount: int
        :param _Items: 智能体列表
        :type Items: list of Agent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询结果总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""智能体列表
        :rtype: list of Agent
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Agent()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChatDetailRequest(AbstractModel):
    r"""DescribeChatDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 智能体ID
        :type InstanceId: str
        :param _ChatId: 会话Id
        :type ChatId: str
        :param _StreamingId: 流ID
        :type StreamingId: str
        :param _BeginStreamingTokenId: 开始拉取的流式TokenID。0表示从该流最早的TokenID开始获取
        :type BeginStreamingTokenId: int
        :param _TokenLimit: 单次获取的token数量，默认2000
        :type TokenLimit: int
        """
        self._InstanceId = None
        self._ChatId = None
        self._StreamingId = None
        self._BeginStreamingTokenId = None
        self._TokenLimit = None

    @property
    def InstanceId(self):
        r"""智能体ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话Id
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def StreamingId(self):
        r"""流ID
        :rtype: str
        """
        return self._StreamingId

    @StreamingId.setter
    def StreamingId(self, StreamingId):
        self._StreamingId = StreamingId

    @property
    def BeginStreamingTokenId(self):
        r"""开始拉取的流式TokenID。0表示从该流最早的TokenID开始获取
        :rtype: int
        """
        return self._BeginStreamingTokenId

    @BeginStreamingTokenId.setter
    def BeginStreamingTokenId(self, BeginStreamingTokenId):
        self._BeginStreamingTokenId = BeginStreamingTokenId

    @property
    def TokenLimit(self):
        r"""单次获取的token数量，默认2000
        :rtype: int
        """
        return self._TokenLimit

    @TokenLimit.setter
    def TokenLimit(self, TokenLimit):
        self._TokenLimit = TokenLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._StreamingId = params.get("StreamingId")
        self._BeginStreamingTokenId = params.get("BeginStreamingTokenId")
        self._TokenLimit = params.get("TokenLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChatDetailResponse(AbstractModel):
    r"""DescribeChatDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 主账号ID
        :type AppId: int
        :param _Uin: 主账号Uin
        :type Uin: str
        :param _OwnerUin: 子账号Uin
        :type OwnerUin: str
        :param _InstanceId: 智能体实例ID
        :type InstanceId: str
        :param _ChatId: 会话ID
        :type ChatId: str
        :param _LastStreamingTokenId: 最后一条流式TokenID
        :type LastStreamingTokenId: int
        :param _StreamingCount: Streaming数量
        :type StreamingCount: int
        :param _Streamings: 对话流列表
        :type Streamings: list of ChatDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._Uin = None
        self._OwnerUin = None
        self._InstanceId = None
        self._ChatId = None
        self._LastStreamingTokenId = None
        self._StreamingCount = None
        self._Streamings = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""主账号ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def OwnerUin(self):
        r"""子账号Uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InstanceId(self):
        r"""智能体实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话ID
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def LastStreamingTokenId(self):
        r"""最后一条流式TokenID
        :rtype: int
        """
        return self._LastStreamingTokenId

    @LastStreamingTokenId.setter
    def LastStreamingTokenId(self, LastStreamingTokenId):
        self._LastStreamingTokenId = LastStreamingTokenId

    @property
    def StreamingCount(self):
        r"""Streaming数量
        :rtype: int
        """
        return self._StreamingCount

    @StreamingCount.setter
    def StreamingCount(self, StreamingCount):
        self._StreamingCount = StreamingCount

    @property
    def Streamings(self):
        r"""对话流列表
        :rtype: list of ChatDetail
        """
        return self._Streamings

    @Streamings.setter
    def Streamings(self, Streamings):
        self._Streamings = Streamings

    @property
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
        self._Uin = params.get("Uin")
        self._OwnerUin = params.get("OwnerUin")
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._LastStreamingTokenId = params.get("LastStreamingTokenId")
        self._StreamingCount = params.get("StreamingCount")
        if params.get("Streamings") is not None:
            self._Streamings = []
            for item in params.get("Streamings"):
                obj = ChatDetail()
                obj._deserialize(item)
                self._Streamings.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChatsRequest(AbstractModel):
    r"""DescribeChats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 智能体ID
        :type InstanceId: str
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 列表查询数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""智能体ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""查询开始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""列表查询数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChatsResponse(AbstractModel):
    r"""DescribeChats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果总数量
        :type TotalCount: int
        :param _Chats: 对话流列表
        :type Chats: list of ChatBrief
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Chats = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询结果总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Chats(self):
        r"""对话流列表
        :rtype: list of ChatBrief
        """
        return self._Chats

    @Chats.setter
    def Chats(self, Chats):
        self._Chats = Chats

    @property
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
        if params.get("Chats") is not None:
            self._Chats = []
            for item in params.get("Chats"):
                obj = ChatBrief()
                obj._deserialize(item)
                self._Chats.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMemoryPlusRecordRequest(AbstractModel):
    r"""DescribeMemoryPlusRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>查询的 Memory 实例 ID。</p>
        :type SpaceId: str
        :param _Offset: <p>查询列表的起始位置（偏移量）。用于分页查询，指明从符合条件的第几条数据开始返回。</p>
        :type Offset: int
        :param _Limit: <p>单次查询返回的记录数量上限（分页大小）。</p>
        :type Limit: int
        :param _RecordType: <p>查询的记忆类型。</p><ul><li>conversation：L0 原始对话。</li><li>memory：L1 原子记忆。</li><li>scene：L2 场景记忆。</li><li>persona：L3 个性化画像。</li><li>memory/persona：L1 原子记忆-画像型。</li><li>memory/episodic：L1 原子记忆-事件型。</li><li>memory/instruction：L1 原子记忆-指令型。</li></ul>
        :type RecordType: str
        :param _Output: <p>指定返回记录中的特定字段。</p>
        :type Output: list of str
        :param _Filters: <p>过滤条件，当前仅支持 <strong>RecordType</strong> 为 <strong>conversation</strong> 的 <strong>session_id</strong> 过滤。</p>
        :type Filters: list of VDBFieldMap
        :param _OrderDirection: <p>查询结果列表的排序规则。</p><ul><li>ASC：升序。</li><li>DESC：降序。</li></ul>
        :type OrderDirection: str
        :param _StartTime: <p>查询时间范围的起始时间点。</p>
        :type StartTime: str
        :param _EndTime: <p>查询时间范围的结束时间点。</p>
        :type EndTime: str
        """
        self._SpaceId = None
        self._Offset = None
        self._Limit = None
        self._RecordType = None
        self._Output = None
        self._Filters = None
        self._OrderDirection = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SpaceId(self):
        r"""<p>查询的 Memory 实例 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Offset(self):
        r"""<p>查询列表的起始位置（偏移量）。用于分页查询，指明从符合条件的第几条数据开始返回。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>单次查询返回的记录数量上限（分页大小）。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RecordType(self):
        r"""<p>查询的记忆类型。</p><ul><li>conversation：L0 原始对话。</li><li>memory：L1 原子记忆。</li><li>scene：L2 场景记忆。</li><li>persona：L3 个性化画像。</li><li>memory/persona：L1 原子记忆-画像型。</li><li>memory/episodic：L1 原子记忆-事件型。</li><li>memory/instruction：L1 原子记忆-指令型。</li></ul>
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Output(self):
        r"""<p>指定返回记录中的特定字段。</p>
        :rtype: list of str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Filters(self):
        r"""<p>过滤条件，当前仅支持 <strong>RecordType</strong> 为 <strong>conversation</strong> 的 <strong>session_id</strong> 过滤。</p>
        :rtype: list of VDBFieldMap
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderDirection(self):
        r"""<p>查询结果列表的排序规则。</p><ul><li>ASC：升序。</li><li>DESC：降序。</li></ul>
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def StartTime(self):
        r"""<p>查询时间范围的起始时间点。</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>查询时间范围的结束时间点。</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RecordType = params.get("RecordType")
        self._Output = params.get("Output")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = VDBFieldMap()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderDirection = params.get("OrderDirection")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMemoryPlusRecordResponse(AbstractModel):
    r"""DescribeMemoryPlusRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>查询结果总数量。</p>
        :type TotalCount: int
        :param _Documents: <p>查询的记忆数据。</p>
        :type Documents: list of VDBDocument
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Documents = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>查询结果总数量。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Documents(self):
        r"""<p>查询的记忆数据。</p>
        :rtype: list of VDBDocument
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
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
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = VDBDocument()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMemoryPlusSpaceRequest(AbstractModel):
    r"""DescribeMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>指定查询的 Memory 实例 ID。</p>
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        r"""<p>指定查询的 Memory 实例 ID。</p>
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
        


class DescribeMemoryPlusSpaceResponse(AbstractModel):
    r"""DescribeMemoryPlusSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>Memory 实例 ID。</p>
        :type SpaceId: str
        :param _Name: <p>Memory 实例的自定义名称。</p>
        :type Name: str
        :param _Description: <p>Memory 实例的简要描述，包括使用场景、用途或背景信息，便于日常运维识别。</p>
        :type Description: str
        :param _AppId: <p>腾讯云账号的 APPID。</p>
        :type AppId: int
        :param _Region: <p>Memroy 实例所属地域。</p>
        :type Region: str
        :param _ResourceTags: <p>Memory 实例的标签信息。</p>
        :type ResourceTags: list of ResourceTag
        :param _Status: <p>Memory 实例当前运行状态。</p><ul><li>1：运行中。</li><li>2：创建中。</li><li>3：销毁中。</li><li>4：已销毁。</li><li>5：隔离中。</li><li>6：已隔离。</li><li>7：恢复中。</li></ul>
        :type Status: int
        :param _PayMode: <p>Memory 实例计费模式。</p><ul><li>-1：免费体验。</li><li>0：包年包月。</li><li>1：按量计费。</li></ul>
        :type PayMode: int
        :param _Version: <p>Memory 版本信息：v1。</p>
        :type Version: str
        :param _MemoryUsage: <p>Memory 当前已写入的记忆条数。</p>
        :type MemoryUsage: int
        :param _MemoryLimit: <p>Memory 实例记忆条数配额上限。</p>
        :type MemoryLimit: int
        :param _CreditUsage: <p>Memory 实例当前 Credit 的使用数量。</p>
        :type CreditUsage: float
        :param _CreditLimit: <p>Memory 实例 Credit 的最大使用数量。</p>
        :type CreditLimit: float
        :param _AccessUrl: <p>Memory 实例的内网访问地址。</p>
        :type AccessUrl: str
        :param _WanAccessUrl: <p>Memory 实例的外网访问地址。</p>
        :type WanAccessUrl: str
        :param _CreatedAt: <p>Memory 实例的创建时间。</p>
        :type CreatedAt: str
        :param _ExpiredAt: <p>Memory 实例的到期时间。</p>
        :type ExpiredAt: str
        :param _IsolatedAt: <p>Memory 实例的隔离时间。</p>
        :type IsolatedAt: str
        :param _DestroyAt: <p>到期销毁时间</p>
        :type DestroyAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None
        self._AppId = None
        self._Region = None
        self._ResourceTags = None
        self._Status = None
        self._PayMode = None
        self._Version = None
        self._MemoryUsage = None
        self._MemoryLimit = None
        self._CreditUsage = None
        self._CreditLimit = None
        self._AccessUrl = None
        self._WanAccessUrl = None
        self._CreatedAt = None
        self._ExpiredAt = None
        self._IsolatedAt = None
        self._DestroyAt = None
        self._RequestId = None

    @property
    def SpaceId(self):
        r"""<p>Memory 实例 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""<p>Memory 实例的自定义名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Memory 实例的简要描述，包括使用场景、用途或背景信息，便于日常运维识别。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AppId(self):
        r"""<p>腾讯云账号的 APPID。</p>
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        r"""<p>Memroy 实例所属地域。</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ResourceTags(self):
        r"""<p>Memory 实例的标签信息。</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Status(self):
        r"""<p>Memory 实例当前运行状态。</p><ul><li>1：运行中。</li><li>2：创建中。</li><li>3：销毁中。</li><li>4：已销毁。</li><li>5：隔离中。</li><li>6：已隔离。</li><li>7：恢复中。</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayMode(self):
        r"""<p>Memory 实例计费模式。</p><ul><li>-1：免费体验。</li><li>0：包年包月。</li><li>1：按量计费。</li></ul>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Version(self):
        r"""<p>Memory 版本信息：v1。</p>
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def MemoryUsage(self):
        r"""<p>Memory 当前已写入的记忆条数。</p>
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def MemoryLimit(self):
        r"""<p>Memory 实例记忆条数配额上限。</p>
        :rtype: int
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def CreditUsage(self):
        r"""<p>Memory 实例当前 Credit 的使用数量。</p>
        :rtype: float
        """
        return self._CreditUsage

    @CreditUsage.setter
    def CreditUsage(self, CreditUsage):
        self._CreditUsage = CreditUsage

    @property
    def CreditLimit(self):
        r"""<p>Memory 实例 Credit 的最大使用数量。</p>
        :rtype: float
        """
        return self._CreditLimit

    @CreditLimit.setter
    def CreditLimit(self, CreditLimit):
        self._CreditLimit = CreditLimit

    @property
    def AccessUrl(self):
        r"""<p>Memory 实例的内网访问地址。</p>
        :rtype: str
        """
        return self._AccessUrl

    @AccessUrl.setter
    def AccessUrl(self, AccessUrl):
        self._AccessUrl = AccessUrl

    @property
    def WanAccessUrl(self):
        r"""<p>Memory 实例的外网访问地址。</p>
        :rtype: str
        """
        return self._WanAccessUrl

    @WanAccessUrl.setter
    def WanAccessUrl(self, WanAccessUrl):
        self._WanAccessUrl = WanAccessUrl

    @property
    def CreatedAt(self):
        r"""<p>Memory 实例的创建时间。</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ExpiredAt(self):
        r"""<p>Memory 实例的到期时间。</p>
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def IsolatedAt(self):
        r"""<p>Memory 实例的隔离时间。</p>
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def DestroyAt(self):
        r"""<p>到期销毁时间</p>
        :rtype: str
        """
        return self._DestroyAt

    @DestroyAt.setter
    def DestroyAt(self, DestroyAt):
        self._DestroyAt = DestroyAt

    @property
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
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Status = params.get("Status")
        self._PayMode = params.get("PayMode")
        self._Version = params.get("Version")
        self._MemoryUsage = params.get("MemoryUsage")
        self._MemoryLimit = params.get("MemoryLimit")
        self._CreditUsage = params.get("CreditUsage")
        self._CreditLimit = params.get("CreditLimit")
        self._AccessUrl = params.get("AccessUrl")
        self._WanAccessUrl = params.get("WanAccessUrl")
        self._CreatedAt = params.get("CreatedAt")
        self._ExpiredAt = params.get("ExpiredAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._DestroyAt = params.get("DestroyAt")
        self._RequestId = params.get("RequestId")


class DescribeMemoryPlusSpacesRequest(AbstractModel):
    r"""DescribeMemoryPlusSpaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>查询列表的起始位置（偏移量）。用于分页查询，指明从符合条件的第几条数据开始返回。</p>
        :type Offset: int
        :param _Limit: <p>单次查询返回的记录数量上限（分页大小）。</p>
        :type Limit: int
        :param _SearchKeys: <p>查询实例名称或者实例id</p>
        :type SearchKeys: list of str
        :param _Status: <p>实例状态</p><p>枚举值：</p><ul><li>1： 运行中</li><li>2： 创建中</li><li>3： 删除中</li><li>4： 已删除</li><li>5： 隔离中</li><li>6： 已隔离（进入回收站）</li><li>7： 恢复中（从回收站恢复）</li></ul>
        :type Status: list of int
        :param _ResourceTags: <p>资源标签</p>
        :type ResourceTags: list of ResourceTag
        :param _Orderby: <p>排序字段</p>
        :type Orderby: str
        :param _OrderDirection: <p>排序方向</p><p>枚举值：</p><ul><li>ASC： 升序</li><li>DESC： 降序</li></ul>
        :type OrderDirection: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchKeys = None
        self._Status = None
        self._ResourceTags = None
        self._Orderby = None
        self._OrderDirection = None

    @property
    def Offset(self):
        r"""<p>查询列表的起始位置（偏移量）。用于分页查询，指明从符合条件的第几条数据开始返回。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>单次查询返回的记录数量上限（分页大小）。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKeys(self):
        r"""<p>查询实例名称或者实例id</p>
        :rtype: list of str
        """
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def Status(self):
        r"""<p>实例状态</p><p>枚举值：</p><ul><li>1： 运行中</li><li>2： 创建中</li><li>3： 删除中</li><li>4： 已删除</li><li>5： 隔离中</li><li>6： 已隔离（进入回收站）</li><li>7： 恢复中（从回收站恢复）</li></ul>
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceTags(self):
        r"""<p>资源标签</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Orderby(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

    @property
    def OrderDirection(self):
        r"""<p>排序方向</p><p>枚举值：</p><ul><li>ASC： 升序</li><li>DESC： 降序</li></ul>
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKeys = params.get("SearchKeys")
        self._Status = params.get("Status")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Orderby = params.get("Orderby")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMemoryPlusSpacesResponse(AbstractModel):
    r"""DescribeMemoryPlusSpaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>查询结果总数量。</p>
        :type TotalCount: int
        :param _Items: <p>实例列表信息</p>
        :type Items: list of MemoryPlusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>查询结果总数量。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""<p>实例列表信息</p>
        :rtype: list of MemoryPlusInfo
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = MemoryPlusInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReportUrlRequest(AbstractModel):
    r"""DescribeReportUrl请求参数结构体

    """


class DescribeReportUrlResponse(AbstractModel):
    r"""DescribeReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        r"""下载地址
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeServiceAccessKeyRequest(AbstractModel):
    r"""DescribeServiceAccessKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: <p>指定 Memroy 实例 ID。</p>
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        r"""<p>指定 Memroy 实例 ID。</p>
        :rtype: str
        """
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
        


class DescribeServiceAccessKeyResponse(AbstractModel):
    r"""DescribeServiceAccessKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthKey: <p>访问密钥。</p>
        :type AuthKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthKey = None
        self._RequestId = None

    @property
    def AuthKey(self):
        r"""<p>访问密钥。</p>
        :rtype: str
        """
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuthKey = params.get("AuthKey")
        self._RequestId = params.get("RequestId")


class DestroyMemoryPlusSpaceRequest(AbstractModel):
    r"""DestroyMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: <p>指定需要销毁的 Memory 实例 ID 列表。</p>
        :type SpaceIds: list of str
        """
        self._SpaceIds = None

    @property
    def SpaceIds(self):
        r"""<p>指定需要销毁的 Memory 实例 ID 列表。</p>
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyMemoryPlusSpaceResponse(AbstractModel):
    r"""DestroyMemoryPlusSpace返回参数结构体

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
    r"""智能体值守任务额外信息

    """

    def __init__(self):
        r"""
        :param _Key: 出参额外信息的Key
        :type Key: str
        :param _Description: 额外信息描述
        :type Description: str
        :param _Value: ExtraInfo的值
        :type Value: str
        :param _ValueType: 值的数据结构类型
        :type ValueType: str
        """
        self._Key = None
        self._Description = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        r"""出参额外信息的Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Description(self):
        r"""额外信息描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Value(self):
        r"""ExtraInfo的值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        r"""值的数据结构类型
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Description = params.get("Description")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfos(AbstractModel):
    r"""实例信息

    """

    def __init__(self):
        r"""
        :param _Region: 数据库地域
        :type Region: str
        :param _InstanceId: 数据库实例id
        :type InstanceId: str
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        :param _TableName: 表名称
        :type TableName: str
        """
        self._Region = None
        self._InstanceId = None
        self._DatabaseName = None
        self._TableName = None

    @property
    def Region(self):
        r"""数据库地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        r"""数据库实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DatabaseName(self):
        r"""数据库名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateAgentInstanceRequest(AbstractModel):
    r"""IsolateAgentInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
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
        


class IsolateAgentInstanceResponse(AbstractModel):
    r"""IsolateAgentInstance返回参数结构体

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


class IsolateMemoryPlusSpaceRequest(AbstractModel):
    r"""IsolateMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: <p>指定需要放入回收站的 Memory 实例 ID 列表。</p>
        :type SpaceIds: list of str
        """
        self._SpaceIds = None

    @property
    def SpaceIds(self):
        r"""<p>指定需要放入回收站的 Memory 实例 ID 列表。</p>
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMemoryPlusSpaceResponse(AbstractModel):
    r"""IsolateMemoryPlusSpace返回参数结构体

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


class MemoryPlusInfo(AbstractModel):
    r"""Memory正式版实例列表元素信息

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>实例id</p>
        :type SpaceId: str
        :param _Name: <p>实例名称</p>
        :type Name: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Status: <p>实例状态</p>
        :type Status: int
        :param _Region: <p>地域</p>
        :type Region: str
        :param _MemoryUsage: <p>记忆条数</p>
        :type MemoryUsage: int
        :param _CreditUsage: <p>当月积分数</p>
        :type CreditUsage: float
        :param _ResourceTags: <p>资源标签</p>
        :type ResourceTags: list of ResourceTag
        :param _CreatedAt: <p>创建时间</p>
        :type CreatedAt: str
        :param _IsolatedAt: <p>隔离时间</p>
        :type IsolatedAt: str
        :param _ExpiredAt: <p>到期时间</p>
        :type ExpiredAt: str
        :param _DestroyAt: <p>到期销毁时间</p>
        :type DestroyAt: str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Region = None
        self._MemoryUsage = None
        self._CreditUsage = None
        self._ResourceTags = None
        self._CreatedAt = None
        self._IsolatedAt = None
        self._ExpiredAt = None
        self._DestroyAt = None

    @property
    def SpaceId(self):
        r"""<p>实例id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""<p>实例名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Status(self):
        r"""<p>实例状态</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def MemoryUsage(self):
        r"""<p>记忆条数</p>
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def CreditUsage(self):
        r"""<p>当月积分数</p>
        :rtype: float
        """
        return self._CreditUsage

    @CreditUsage.setter
    def CreditUsage(self, CreditUsage):
        self._CreditUsage = CreditUsage

    @property
    def ResourceTags(self):
        r"""<p>资源标签</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CreatedAt(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def IsolatedAt(self):
        r"""<p>隔离时间</p>
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def ExpiredAt(self):
        r"""<p>到期时间</p>
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def DestroyAt(self):
        r"""<p>到期销毁时间</p>
        :rtype: str
        """
        return self._DestroyAt

    @DestroyAt.setter
    def DestroyAt(self, DestroyAt):
        self._DestroyAt = DestroyAt


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._MemoryUsage = params.get("MemoryUsage")
        self._CreditUsage = params.get("CreditUsage")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._ExpiredAt = params.get("ExpiredAt")
        self._DestroyAt = params.get("DestroyAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentInstanceParametersRequest(AbstractModel):
    r"""ModifyAgentInstanceParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _TaskType: 任务类型, 可选，默认default
        :type TaskType: str
        :param _Parameters: 更新的参数列表
        :type Parameters: :class:`tencentcloud.tdai.v20250717.models.Parameter`
        :param _SqlAgentParameter: 风险SQL智能体参数列表
        :type SqlAgentParameter: :class:`tencentcloud.tdai.v20250717.models.SqlAgentParameter`
        """
        self._InstanceId = None
        self._TaskType = None
        self._Parameters = None
        self._SqlAgentParameter = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskType(self):
        r"""任务类型, 可选，默认default
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Parameters(self):
        r"""更新的参数列表
        :rtype: :class:`tencentcloud.tdai.v20250717.models.Parameter`
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def SqlAgentParameter(self):
        r"""风险SQL智能体参数列表
        :rtype: :class:`tencentcloud.tdai.v20250717.models.SqlAgentParameter`
        """
        return self._SqlAgentParameter

    @SqlAgentParameter.setter
    def SqlAgentParameter(self, SqlAgentParameter):
        self._SqlAgentParameter = SqlAgentParameter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TaskType = params.get("TaskType")
        if params.get("Parameters") is not None:
            self._Parameters = Parameter()
            self._Parameters._deserialize(params.get("Parameters"))
        if params.get("SqlAgentParameter") is not None:
            self._SqlAgentParameter = SqlAgentParameter()
            self._SqlAgentParameter._deserialize(params.get("SqlAgentParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentInstanceParametersResponse(AbstractModel):
    r"""ModifyAgentInstanceParameters返回参数结构体

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


class ModifyChatTitleRequest(AbstractModel):
    r"""ModifyChatTitle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 智能体ID
        :type InstanceId: str
        :param _ChatId: 会话Id
        :type ChatId: str
        :param _Title: 标题
        :type Title: str
        """
        self._InstanceId = None
        self._ChatId = None
        self._Title = None

    @property
    def InstanceId(self):
        r"""智能体ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话Id
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def Title(self):
        r"""标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChatTitleResponse(AbstractModel):
    r"""ModifyChatTitle返回参数结构体

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


class ModifyMemoryPlusSpaceRequest(AbstractModel):
    r"""ModifyMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>指定需要修改的 Memory 实例 ID。</p>
        :type SpaceId: str
        :param _Name: <p>指定修改后的实例名称。支持 60 个字符内 的中英文、数字、中划线（-）及下划线（_）。</p>
        :type Name: str
        :param _Description: <p>指定修改后的实例描述。最多支持 200 个字符。</p>
        :type Description: str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None

    @property
    def SpaceId(self):
        r"""<p>指定需要修改的 Memory 实例 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""<p>指定修改后的实例名称。支持 60 个字符内 的中英文、数字、中划线（-）及下划线（_）。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>指定修改后的实例描述。最多支持 200 个字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMemoryPlusSpaceResponse(AbstractModel):
    r"""ModifyMemoryPlusSpace返回参数结构体

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


class Parameter(AbstractModel):
    r"""智能体实例的参数值

    """

    def __init__(self):
        r"""
        :param _Key: 参数键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _ValueType: 枚举值，可取值包括：string(字符串), int(整型), float(浮点型), bool(布尔型), struct(结构体), array(数组), 
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueType: str
        """
        self._Key = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        r"""参数键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        r"""枚举值，可取值包括：string(字符串), int(整型), float(浮点型), bool(布尔型), struct(结构体), array(数组), 
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseAgentWorkRequest(AbstractModel):
    r"""PauseAgentWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        :param _AgentTaskType: Agent任务类型
        :type AgentTaskType: str
        """
        self._InstanceId = None
        self._AgentTaskType = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentTaskType(self):
        r"""Agent任务类型
        :rtype: str
        """
        return self._AgentTaskType

    @AgentTaskType.setter
    def AgentTaskType(self, AgentTaskType):
        self._AgentTaskType = AgentTaskType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentTaskType = params.get("AgentTaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseAgentWorkResponse(AbstractModel):
    r"""PauseAgentWork返回参数结构体

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


class RecoverAgentInstanceRequest(AbstractModel):
    r"""RecoverAgentInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
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
        


class RecoverAgentInstanceResponse(AbstractModel):
    r"""RecoverAgentInstance返回参数结构体

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


class RecoverMemoryPlusSpaceRequest(AbstractModel):
    r"""RecoverMemoryPlusSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: <p>指定需要恢复的 Memory 实例 ID 列表。</p>
        :type SpaceIds: list of str
        """
        self._SpaceIds = None

    @property
    def SpaceIds(self):
        r"""<p>指定需要恢复的 Memory 实例 ID 列表。</p>
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMemoryPlusSpaceResponse(AbstractModel):
    r"""RecoverMemoryPlusSpace返回参数结构体

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


class RemoveChatRequest(AbstractModel):
    r"""RemoveChat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 智能体ID
        :type InstanceId: str
        :param _ChatId: 会话Id
        :type ChatId: str
        """
        self._InstanceId = None
        self._ChatId = None

    @property
    def InstanceId(self):
        r"""智能体ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChatId(self):
        r"""会话Id
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChatResponse(AbstractModel):
    r"""RemoveChat返回参数结构体

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


class ResourceTag(AbstractModel):
    r"""资源tag

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
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
        


class SqlAgentParameter(AbstractModel):
    r"""风险SQL智能体参数

    """

    def __init__(self):
        r"""
        :param _InstanceInfos: 数据库实例信息列表
        :type InstanceInfos: list of InstanceInfos
        :param _CodeRepo: 代码仓库信息
        :type CodeRepo: :class:`tencentcloud.tdai.v20250717.models.CodeRepo`
        """
        self._InstanceInfos = None
        self._CodeRepo = None

    @property
    def InstanceInfos(self):
        r"""数据库实例信息列表
        :rtype: list of InstanceInfos
        """
        return self._InstanceInfos

    @InstanceInfos.setter
    def InstanceInfos(self, InstanceInfos):
        self._InstanceInfos = InstanceInfos

    @property
    def CodeRepo(self):
        r"""代码仓库信息
        :rtype: :class:`tencentcloud.tdai.v20250717.models.CodeRepo`
        """
        return self._CodeRepo

    @CodeRepo.setter
    def CodeRepo(self, CodeRepo):
        self._CodeRepo = CodeRepo


    def _deserialize(self, params):
        if params.get("InstanceInfos") is not None:
            self._InstanceInfos = []
            for item in params.get("InstanceInfos"):
                obj = InstanceInfos()
                obj._deserialize(item)
                self._InstanceInfos.append(obj)
        if params.get("CodeRepo") is not None:
            self._CodeRepo = CodeRepo()
            self._CodeRepo._deserialize(params.get("CodeRepo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAgentTaskRequest(AbstractModel):
    r"""StartAgentTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceToken: 配置Token
        :type InstanceToken: str
        """
        self._InstanceId = None
        self._InstanceToken = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceToken(self):
        r"""配置Token
        :rtype: str
        """
        return self._InstanceToken

    @InstanceToken.setter
    def InstanceToken(self, InstanceToken):
        self._InstanceToken = InstanceToken


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceToken = params.get("InstanceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAgentTaskResponse(AbstractModel):
    r"""StartAgentTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
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


class StatusItem(AbstractModel):
    r"""实例状态描述

    """

    def __init__(self):
        r"""
        :param _Status: <p>无</p>
        :type Status: str
        :param _Count: <p>无</p>
        :type Count: int
        """
        self._Status = None
        self._Count = None

    @property
    def Status(self):
        r"""<p>无</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        r"""<p>无</p>
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    r"""通过标签对资源进行过滤

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: list of str
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
        


class TagItem(AbstractModel):
    r"""资源标签

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
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
        


class TerminateAgentInstanceRequest(AbstractModel):
    r"""TerminateAgentInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
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
        


class TerminateAgentInstanceResponse(AbstractModel):
    r"""TerminateAgentInstance返回参数结构体

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


class UploadChoice(AbstractModel):
    r"""流式输出消息数据体

    """

    def __init__(self):
        r"""
        :param _Index: 消息索引
        :type Index: int
        :param _StepNo: 当前消息步骤
        :type StepNo: int
        :param _CurrentStep: 当前步骤
        :type CurrentStep: str
        :param _Delta: 增量信息
        :type Delta: :class:`tencentcloud.tdai.v20250717.models.UploadDelta`
        :param _FinishReason: 结束原因
        :type FinishReason: str
        :param _ErrorMessage: 错误信息，FinishReason为error时有效
        :type ErrorMessage: str
        """
        self._Index = None
        self._StepNo = None
        self._CurrentStep = None
        self._Delta = None
        self._FinishReason = None
        self._ErrorMessage = None

    @property
    def Index(self):
        r"""消息索引
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def StepNo(self):
        r"""当前消息步骤
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def CurrentStep(self):
        r"""当前步骤
        :rtype: str
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def Delta(self):
        r"""增量信息
        :rtype: :class:`tencentcloud.tdai.v20250717.models.UploadDelta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def FinishReason(self):
        r"""结束原因
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def ErrorMessage(self):
        r"""错误信息，FinishReason为error时有效
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._StepNo = params.get("StepNo")
        self._CurrentStep = params.get("CurrentStep")
        if params.get("Delta") is not None:
            self._Delta = UploadDelta()
            self._Delta._deserialize(params.get("Delta"))
        self._FinishReason = params.get("FinishReason")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDelta(AbstractModel):
    r"""流式接口当前消息数据详细内容

    """

    def __init__(self):
        r"""
        :param _StepBrief: 步骤摘要
        :type StepBrief: str
        :param _Content: 步骤详情
        :type Content: str
        """
        self._StepBrief = None
        self._Content = None

    @property
    def StepBrief(self):
        r"""步骤摘要
        :rtype: str
        """
        return self._StepBrief

    @StepBrief.setter
    def StepBrief(self, StepBrief):
        self._StepBrief = StepBrief

    @property
    def Content(self):
        r"""步骤详情
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._StepBrief = params.get("StepBrief")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VDBDocument(AbstractModel):
    r"""vdb数据库文档结构

    """

    def __init__(self):
        r"""
        :param _Id: <p>vdb document数据id</p>
        :type Id: str
        :param _Fields: <p>vdb document数据标量字段</p>
        :type Fields: list of VDBFieldMap
        """
        self._Id = None
        self._Fields = None

    @property
    def Id(self):
        r"""<p>vdb document数据id</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Fields(self):
        r"""<p>vdb document数据标量字段</p>
        :rtype: list of VDBFieldMap
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = VDBFieldMap()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VDBFieldMap(AbstractModel):
    r"""vdb数据库文档中键值结构

    """

    def __init__(self):
        r"""
        :param _Name: <p>vdb document字段名</p>
        :type Name: str
        :param _Value: <p>vdb document字段值</p>
        :type Value: str
        :param _Type: <p>vdb document字段类型</p>
        :type Type: str
        :param _Description: <p>字段描述</p>
        :type Description: str
        """
        self._Name = None
        self._Value = None
        self._Type = None
        self._Description = None

    @property
    def Name(self):
        r"""<p>vdb document字段名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""<p>vdb document字段值</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        r"""<p>vdb document字段类型</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        r"""<p>字段描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        