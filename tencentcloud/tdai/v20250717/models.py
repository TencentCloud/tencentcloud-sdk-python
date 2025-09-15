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
        


class AgentInstance(AbstractModel):
    r"""智能体实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 智能体实例ID
        :type InstanceId: str
        :param _InstanceName: 智能体实例名称
        :type InstanceName: str
        :param _AgentId: 智能体ID
        :type AgentId: str
        :param _AgentName: 智能体名称
        :type AgentName: str
        :param _AgentInternalName: 智能体类型
        :type AgentInternalName: str
        :param _AgentType: 智能体服务模式
        :type AgentType: str
        :param _AgentVersion: 智能体版本
        :type AgentVersion: str
        :param _Status: 智能体实例状态
        :type Status: str
        :param _Parameters: 智能体实例参数列表
        :type Parameters: list of Parameter
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _Tags: 资源绑定Tag列表
        :type Tags: list of TagItem
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
    def InstanceName(self):
        r"""智能体实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AgentId(self):
        r"""智能体ID
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
    def AgentType(self):
        r"""智能体服务模式
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def AgentVersion(self):
        r"""智能体版本
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def Status(self):
        r"""智能体实例状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Parameters(self):
        r"""智能体实例参数列表
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

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
    def UpdateTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Tags(self):
        r"""资源绑定Tag列表
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        :param _AgentId: 智能体ID
        :type AgentId: str
        :param _AgentVersion: 智能体版本
        :type AgentVersion: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _Parameters: 智能体实例的参数列表
        :type Parameters: list of Parameter
        :param _Tags: 资源的标签信息
        :type Tags: list of TagItem
        """
        self._AgentId = None
        self._AgentVersion = None
        self._InstanceName = None
        self._Parameters = None
        self._Tags = None

    @property
    def AgentId(self):
        r"""智能体ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentVersion(self):
        r"""智能体版本
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Parameters(self):
        r"""智能体实例的参数列表
        :rtype: list of Parameter
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Tags(self):
        r"""资源的标签信息
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        :param _InstanceId: 智能体实例ID
        :type InstanceId: str
        :param _InstanceName: 智能体实例名称
        :type InstanceName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._RequestId = None

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
    def InstanceName(self):
        r"""智能体实例名称
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
        :param _IsHidden: 是否隐藏
        :type IsHidden: bool
        """
        self._IsHidden = None

    @property
    def IsHidden(self):
        r"""是否隐藏
        :rtype: bool
        """
        return self._IsHidden

    @IsHidden.setter
    def IsHidden(self, IsHidden):
        self._IsHidden = IsHidden


    def _deserialize(self, params):
        self._IsHidden = params.get("IsHidden")
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


class DescribeAgentDutyTasksRequest(AbstractModel):
    r"""DescribeAgentDutyTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 列表查询数量
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
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
        :param _InstanceId: 实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :type InstanceId: str
        :param _InstanceName: 实例名，为空时查询所有，如果填写则会根据InstanceName筛选
        :type InstanceName: str
        :param _AgentId: 智能体ID，为空时查询所有，如果填写则会根据AgentId筛选
        :type AgentId: str
        :param _AgentName: 智能体名称，为空时查询所有，如果填写则会根据AgentName筛选
        :type AgentName: str
        :param _AgentInternalName: 智能体类型，为空时查询所有，如果填写则会根据AgentName筛选
        :type AgentInternalName: str
        :param _Status: 智能体实例状态，为空时查询所有，如果填写则会根据Status筛选
        :type Status: str
        :param _TagFilter: 标签过滤信息
        :type TagFilter: list of TagFilter
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
        r"""实例ID，为空时查询所有，如果填写则会根据InstanceId筛选
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名，为空时查询所有，如果填写则会根据InstanceName筛选
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def Status(self):
        r"""智能体实例状态，为空时查询所有，如果填写则会根据Status筛选
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagFilter(self):
        r"""标签过滤信息
        :rtype: list of TagFilter
        """
        return self._TagFilter

    @TagFilter.setter
    def TagFilter(self, TagFilter):
        self._TagFilter = TagFilter


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
        :param _Items: 智能体实例列表
        :type Items: list of AgentInstance
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
        r"""智能体实例列表
        :rtype: list of AgentInstance
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
                obj = AgentInstance()
                obj._deserialize(item)
                self._Items.append(obj)
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
        """
        self._Offset = None
        self._Limit = None
        self._AgentId = None
        self._AgentName = None
        self._AgentInternalName = None
        self._AgentStatus = None

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


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._AgentInternalName = params.get("AgentInternalName")
        self._AgentStatus = params.get("AgentStatus")
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
        :param _LastStreamingTokenId: 最后一条流式TokenID
        :type LastStreamingTokenId: int
        """
        self._InstanceId = None
        self._ChatId = None
        self._LastStreamingTokenId = None

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
    def LastStreamingTokenId(self):
        r"""最后一条流式TokenID
        :rtype: int
        """
        return self._LastStreamingTokenId

    @LastStreamingTokenId.setter
    def LastStreamingTokenId(self, LastStreamingTokenId):
        self._LastStreamingTokenId = LastStreamingTokenId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChatId = params.get("ChatId")
        self._LastStreamingTokenId = params.get("LastStreamingTokenId")
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
        