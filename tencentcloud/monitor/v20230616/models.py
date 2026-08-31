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


class AIWorkbenchSREDigitalTwinTask(AbstractModel):
    r"""AI工作台SRE数字分身任务

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _TaskConfig: 任务配置
        :type TaskConfig: str
        :param _ID: 唯一标识
        :type ID: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _TwinID: 所属数字分身ID
        :type TwinID: int
        """
        self._Name = None
        self._TaskType = None
        self._TaskConfig = None
        self._ID = None
        self._CreatedAt = None
        self._TwinID = None

    @property
    def Name(self):
        r"""任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def TaskConfig(self):
        r"""任务配置
        :rtype: str
        """
        return self._TaskConfig

    @TaskConfig.setter
    def TaskConfig(self, TaskConfig):
        self._TaskConfig = TaskConfig

    @property
    def ID(self):
        r"""唯一标识
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def TwinID(self):
        r"""所属数字分身ID
        :rtype: int
        """
        return self._TwinID

    @TwinID.setter
    def TwinID(self, TwinID):
        self._TwinID = TwinID


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskType = params.get("TaskType")
        self._TaskConfig = params.get("TaskConfig")
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        self._TwinID = params.get("TwinID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIWorkbenchSREDigitalTwinTaskList(AbstractModel):
    r"""AI工作台SRE数字分身任务列表

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务列表
        :type Tasks: list of AIWorkbenchSREDigitalTwinTask
        :param _Total: 任务总数
        :type Total: int
        """
        self._Tasks = None
        self._Total = None

    @property
    def Tasks(self):
        r"""任务列表
        :rtype: list of AIWorkbenchSREDigitalTwinTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Total(self):
        r"""任务总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AIWorkbenchSREDigitalTwinTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIWorkbenchSREDigitalTwinWorkLog(AbstractModel):
    r"""AI工作台SRE数字分身工作日志

    """

    def __init__(self):
        r"""
        :param _ID: 唯一标识符
        :type ID: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _TwinID: 所属数字分身ID
        :type TwinID: int
        :param _TaskID: 所属数字分身任务ID
        :type TaskID: int
        :param _StartTime: 分析时间
        :type StartTime: str
        :param _Status: 分析状态
        :type Status: str
        :param _Result: 分析结果摘要
        :type Result: str
        :param _TaskName: 所属任务名称
        :type TaskName: str
        :param _TaskType: 所属任务类型
        :type TaskType: str
        """
        self._ID = None
        self._CreatedAt = None
        self._TwinID = None
        self._TaskID = None
        self._StartTime = None
        self._Status = None
        self._Result = None
        self._TaskName = None
        self._TaskType = None

    @property
    def ID(self):
        r"""唯一标识符
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def TwinID(self):
        r"""所属数字分身ID
        :rtype: int
        """
        return self._TwinID

    @TwinID.setter
    def TwinID(self, TwinID):
        self._TwinID = TwinID

    @property
    def TaskID(self):
        r"""所属数字分身任务ID
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def StartTime(self):
        r"""分析时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""分析状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        r"""分析结果摘要
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TaskName(self):
        r"""所属任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        r"""所属任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        self._TwinID = params.get("TwinID")
        self._TaskID = params.get("TaskID")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIWorkbenchSREDigitalTwinWorkLogDetail(AbstractModel):
    r"""AI工作台SRE数字分身工作日志详细信息

    """

    def __init__(self):
        r"""
        :param _Content: 工作日志详细内容
        :type Content: str
        :param _TaskType: 工作日志任务类型
        :type TaskType: str
        :param _DialogID: 工作日志相关对话ID
        :type DialogID: int
        """
        self._Content = None
        self._TaskType = None
        self._DialogID = None

    @property
    def Content(self):
        r"""工作日志详细内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def TaskType(self):
        r"""工作日志任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def DialogID(self):
        r"""工作日志相关对话ID
        :rtype: int
        """
        return self._DialogID

    @DialogID.setter
    def DialogID(self, DialogID):
        self._DialogID = DialogID


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._TaskType = params.get("TaskType")
        self._DialogID = params.get("DialogID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIWorkbenchSREDigitalTwinWorkLogList(AbstractModel):
    r"""AI工作台SRE数字分身工作日志列表

    """

    def __init__(self):
        r"""
        :param _WorkLogs: 工作日志列表
        :type WorkLogs: list of AIWorkbenchSREDigitalTwinWorkLog
        :param _Total: 总数
        :type Total: int
        """
        self._WorkLogs = None
        self._Total = None

    @property
    def WorkLogs(self):
        r"""工作日志列表
        :rtype: list of AIWorkbenchSREDigitalTwinWorkLog
        """
        return self._WorkLogs

    @WorkLogs.setter
    def WorkLogs(self, WorkLogs):
        self._WorkLogs = WorkLogs

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("WorkLogs") is not None:
            self._WorkLogs = []
            for item in params.get("WorkLogs"):
                obj = AIWorkbenchSREDigitalTwinWorkLog()
                obj._deserialize(item)
                self._WorkLogs.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentInfo(AbstractModel):
    r"""Agent 信息

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _Name: <p>Agent 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>Agent 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Category: <p>Agent 分类</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param _Status: <p>状态: draft/configured/running/standby/disabled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _SkillIds: <p>关联技能 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillIds: list of str
        :param _ResourceMapId: <p>关联的资源地图 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMapId: str
        :param _MCPIds: <p>关联的mcp id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCPIds: list of str
        :param _CamTags: <p>资源标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CamTags: list of Tag
        :param _EnvVars: <p>agent运行时所需环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVars: list of EnvVar
        """
        self._AgentId = None
        self._Name = None
        self._Description = None
        self._Category = None
        self._Status = None
        self._SkillIds = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._CamTags = None
        self._EnvVars = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        r"""<p>Agent 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Agent 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Category(self):
        r"""<p>Agent 分类</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Status(self):
        r"""<p>状态: draft/configured/running/standby/disabled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SkillIds(self):
        r"""<p>关联技能 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def ResourceMapId(self):
        r"""<p>关联的资源地图 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>关联的mcp id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def CamTags(self):
        r"""<p>资源标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._CamTags

    @CamTags.setter
    def CamTags(self, CamTags):
        self._CamTags = CamTags

    @property
    def EnvVars(self):
        r"""<p>agent运行时所需环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Status = params.get("Status")
        self._SkillIds = params.get("SkillIds")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("CamTags") is not None:
            self._CamTags = []
            for item in params.get("CamTags"):
                obj = Tag()
                obj._deserialize(item)
                self._CamTags.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmLable(AbstractModel):
    r"""告警中的Label

    """

    def __init__(self):
        r"""
        :param _Name: label name
        :type Name: str
        :param _Value: label value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""label name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""label value
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
        


class AlarmNotifyHistory(AbstractModel):
    r"""单个告警通知历史

    """

    def __init__(self):
        r"""
        :param _NotifyId: 通知的唯一ID
        :type NotifyId: str
        :param _PolicyId: 告警策略ID
        :type PolicyId: str
        :param _SessionId: 告警周期iD
        :type SessionId: str
        :param _NotifyTime: 通知时间 unix秒级时间戳
        :type NotifyTime: int
        :param _TriggerTime: 触发时间 unix秒级时间戳
        :type TriggerTime: int
        :param _TriggerLevel: 告警级别 None 非分级告警级别; Note 提示级别; Warn 严重级别; Serious 紧急级别
        :type TriggerLevel: str
        :param _AlarmContent: 告警内容
        :type AlarmContent: str
        :param _AlarmObject: 告警对象
        :type AlarmObject: str
        :param _ChannelSet: 本次告警通知涉及到的渠道合集
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSet: list of str
        :param _ChannelsReceivers: 渠道的接收人信息
        :type ChannelsReceivers: list of ChannelsReceivers
        :param _PolicyName: 告警策略名称
        :type PolicyName: str
        :param _PromeInstanceID: Prometheus实例ID, 仅当 MT_PROME 时有效
        :type PromeInstanceID: str
        :param _PromeInstanceRegion: Prometheus实例所在的地域, 仅当 MT_PROME 时有效
        :type PromeInstanceRegion: str
        :param _Notices: 通知模板相关的配置信息
        :type Notices: list of NotifyRelatedNotice
        :param _TriggerStatus: 告警触发状态  Trigger 告警状态触发; Recovery 告警状态恢复
        :type TriggerStatus: str
        :param _PromeConsoleURL: 与当前Prometheus通知历史相关控制台页面地址，仅当 MR_PROME 时有效
        :type PromeConsoleURL: str
        :param _Labels: 告警的lable
        :type Labels: list of AlarmLable
        """
        self._NotifyId = None
        self._PolicyId = None
        self._SessionId = None
        self._NotifyTime = None
        self._TriggerTime = None
        self._TriggerLevel = None
        self._AlarmContent = None
        self._AlarmObject = None
        self._ChannelSet = None
        self._ChannelsReceivers = None
        self._PolicyName = None
        self._PromeInstanceID = None
        self._PromeInstanceRegion = None
        self._Notices = None
        self._TriggerStatus = None
        self._PromeConsoleURL = None
        self._Labels = None

    @property
    def NotifyId(self):
        r"""通知的唯一ID
        :rtype: str
        """
        return self._NotifyId

    @NotifyId.setter
    def NotifyId(self, NotifyId):
        self._NotifyId = NotifyId

    @property
    def PolicyId(self):
        r"""告警策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def SessionId(self):
        r"""告警周期iD
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def NotifyTime(self):
        r"""通知时间 unix秒级时间戳
        :rtype: int
        """
        return self._NotifyTime

    @NotifyTime.setter
    def NotifyTime(self, NotifyTime):
        self._NotifyTime = NotifyTime

    @property
    def TriggerTime(self):
        r"""触发时间 unix秒级时间戳
        :rtype: int
        """
        return self._TriggerTime

    @TriggerTime.setter
    def TriggerTime(self, TriggerTime):
        self._TriggerTime = TriggerTime

    @property
    def TriggerLevel(self):
        r"""告警级别 None 非分级告警级别; Note 提示级别; Warn 严重级别; Serious 紧急级别
        :rtype: str
        """
        return self._TriggerLevel

    @TriggerLevel.setter
    def TriggerLevel(self, TriggerLevel):
        self._TriggerLevel = TriggerLevel

    @property
    def AlarmContent(self):
        r"""告警内容
        :rtype: str
        """
        return self._AlarmContent

    @AlarmContent.setter
    def AlarmContent(self, AlarmContent):
        self._AlarmContent = AlarmContent

    @property
    def AlarmObject(self):
        r"""告警对象
        :rtype: str
        """
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def ChannelSet(self):
        r"""本次告警通知涉及到的渠道合集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ChannelSet

    @ChannelSet.setter
    def ChannelSet(self, ChannelSet):
        self._ChannelSet = ChannelSet

    @property
    def ChannelsReceivers(self):
        r"""渠道的接收人信息
        :rtype: list of ChannelsReceivers
        """
        return self._ChannelsReceivers

    @ChannelsReceivers.setter
    def ChannelsReceivers(self, ChannelsReceivers):
        self._ChannelsReceivers = ChannelsReceivers

    @property
    def PolicyName(self):
        r"""告警策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PromeInstanceID(self):
        r"""Prometheus实例ID, 仅当 MT_PROME 时有效
        :rtype: str
        """
        return self._PromeInstanceID

    @PromeInstanceID.setter
    def PromeInstanceID(self, PromeInstanceID):
        self._PromeInstanceID = PromeInstanceID

    @property
    def PromeInstanceRegion(self):
        r"""Prometheus实例所在的地域, 仅当 MT_PROME 时有效
        :rtype: str
        """
        return self._PromeInstanceRegion

    @PromeInstanceRegion.setter
    def PromeInstanceRegion(self, PromeInstanceRegion):
        self._PromeInstanceRegion = PromeInstanceRegion

    @property
    def Notices(self):
        r"""通知模板相关的配置信息
        :rtype: list of NotifyRelatedNotice
        """
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def TriggerStatus(self):
        r"""告警触发状态  Trigger 告警状态触发; Recovery 告警状态恢复
        :rtype: str
        """
        return self._TriggerStatus

    @TriggerStatus.setter
    def TriggerStatus(self, TriggerStatus):
        self._TriggerStatus = TriggerStatus

    @property
    def PromeConsoleURL(self):
        r"""与当前Prometheus通知历史相关控制台页面地址，仅当 MR_PROME 时有效
        :rtype: str
        """
        return self._PromeConsoleURL

    @PromeConsoleURL.setter
    def PromeConsoleURL(self, PromeConsoleURL):
        self._PromeConsoleURL = PromeConsoleURL

    @property
    def Labels(self):
        r"""告警的lable
        :rtype: list of AlarmLable
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._NotifyId = params.get("NotifyId")
        self._PolicyId = params.get("PolicyId")
        self._SessionId = params.get("SessionId")
        self._NotifyTime = params.get("NotifyTime")
        self._TriggerTime = params.get("TriggerTime")
        self._TriggerLevel = params.get("TriggerLevel")
        self._AlarmContent = params.get("AlarmContent")
        self._AlarmObject = params.get("AlarmObject")
        self._ChannelSet = params.get("ChannelSet")
        if params.get("ChannelsReceivers") is not None:
            self._ChannelsReceivers = []
            for item in params.get("ChannelsReceivers"):
                obj = ChannelsReceivers()
                obj._deserialize(item)
                self._ChannelsReceivers.append(obj)
        self._PolicyName = params.get("PolicyName")
        self._PromeInstanceID = params.get("PromeInstanceID")
        self._PromeInstanceRegion = params.get("PromeInstanceRegion")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = NotifyRelatedNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._TriggerStatus = params.get("TriggerStatus")
        self._PromeConsoleURL = params.get("PromeConsoleURL")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AlarmLable()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArtifactInfo(AbstractModel):
    r"""产物实体

    """

    def __init__(self):
        r"""
        :param _ArtifactId: <p>产物 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ArtifactId: str
        :param _Name: <p>产物名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _MimeType: <p>物理类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MimeType: str
        :param _SizeBytes: <p>文件大小(字节)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SizeBytes: int
        :param _IsGlobal: <p>是否公共</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGlobal: bool
        :param _CreatedAt: <p>创建时间 Unix 秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: int
        :param _UpdatedAt: <p>修改时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: int
        :param _AgentId: <p>产生该制品的 Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _SkillId: <p>产生该制品的 Skill ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillId: str
        :param _StoragePath: <p>用于解析调用下载接口</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePath: str
        """
        self._ArtifactId = None
        self._Name = None
        self._MimeType = None
        self._SizeBytes = None
        self._IsGlobal = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._AgentId = None
        self._SkillId = None
        self._StoragePath = None

    @property
    def ArtifactId(self):
        r"""<p>产物 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId

    @property
    def Name(self):
        r"""<p>产物名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MimeType(self):
        r"""<p>物理类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MimeType

    @MimeType.setter
    def MimeType(self, MimeType):
        self._MimeType = MimeType

    @property
    def SizeBytes(self):
        r"""<p>文件大小(字节)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SizeBytes

    @SizeBytes.setter
    def SizeBytes(self, SizeBytes):
        self._SizeBytes = SizeBytes

    @property
    def IsGlobal(self):
        r"""<p>是否公共</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def CreatedAt(self):
        r"""<p>创建时间 Unix 秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>修改时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def AgentId(self):
        r"""<p>产生该制品的 Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def SkillId(self):
        r"""<p>产生该制品的 Skill ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def StoragePath(self):
        r"""<p>用于解析调用下载接口</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StoragePath

    @StoragePath.setter
    def StoragePath(self, StoragePath):
        self._StoragePath = StoragePath


    def _deserialize(self, params):
        self._ArtifactId = params.get("ArtifactId")
        self._Name = params.get("Name")
        self._MimeType = params.get("MimeType")
        self._SizeBytes = params.get("SizeBytes")
        self._IsGlobal = params.get("IsGlobal")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._AgentId = params.get("AgentId")
        self._SkillId = params.get("SkillId")
        self._StoragePath = params.get("StoragePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIWorkbenchChatRequest(AbstractModel):
    r"""CancelAIWorkbenchChat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话id</p>
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""<p>会话id</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIWorkbenchChatResponse(AbstractModel):
    r"""CancelAIWorkbenchChat返回参数结构体

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


class ChannelsReceivers(AbstractModel):
    r"""接受人详情信息

    """

    def __init__(self):
        r"""
        :param _ChannelName: 通知渠道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param _Receivers: 接收者
注意：此字段可能返回 null，表示取不到有效值。
        :type Receivers: list of str
        :param _SendStatus: 发送结果,0-无效,1-成功,2-失败,3-无需发送
注意：此字段可能返回 null，表示取不到有效值。
        :type SendStatus: str
        """
        self._ChannelName = None
        self._Receivers = None
        self._SendStatus = None

    @property
    def ChannelName(self):
        r"""通知渠道名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        r"""接收者
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def SendStatus(self):
        r"""发送结果,0-无效,1-成功,2-失败,3-无需发送
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._SendStatus = params.get("SendStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentBlockInfo(AbstractModel):
    r"""每个 ContentBlockInfo 对应下游 ContentBlock 转换而来的一个 AGUI 事件。

    """

    def __init__(self):
        r"""
        :param _Type: <p>类型</p>
        :type Type: str
        :param _Data: <p>数据内容</p>
        :type Data: str
        """
        self._Type = None
        self._Data = None

    @property
    def Type(self):
        r"""<p>类型</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        r"""<p>数据内容</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchAgentRequest(AbstractModel):
    r"""CreateAIWorkbenchAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>Agent 名称</p>
        :type Name: str
        :param _Description: <p>Agent 描述</p>
        :type Description: str
        :param _Category: <p>Agent 分类</p>
        :type Category: str
        :param _Tags: <p>Agent 标签</p>
        :type Tags: list of str
        :param _Instruction: <p>Agent 提示词</p>
        :type Instruction: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        :param _SkillIds: <p>关联技能 ID 列表</p>
        :type SkillIds: list of str
        :param _Source: <p>来源: builtin / custom</p>
        :type Source: str
        :param _ResourceMapId: <p>关联的资源地图 ID</p>
        :type ResourceMapId: str
        :param _MCPIds: <p>关联的mcp工具</p>
        :type MCPIds: list of str
        :param _CamTags: <p>资源标签</p>
        :type CamTags: list of Tag
        :param _EnvVars: <p>agent运行时环境变量</p>
        :type EnvVars: list of EnvVar
        """
        self._Name = None
        self._Description = None
        self._Category = None
        self._Tags = None
        self._Instruction = None
        self._SkillIds = None
        self._Source = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._CamTags = None
        self._EnvVars = None

    @property
    def Name(self):
        r"""<p>Agent 名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Category(self):
        r"""<p>Agent 分类</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Tags(self):
        r"""<p>Agent 标签</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Instruction(self):
        r"""<p>Agent 提示词</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        """
        return self._Instruction

    @Instruction.setter
    def Instruction(self, Instruction):
        self._Instruction = Instruction

    @property
    def SkillIds(self):
        r"""<p>关联技能 ID 列表</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def Source(self):
        r"""<p>来源: builtin / custom</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def ResourceMapId(self):
        r"""<p>关联的资源地图 ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>关联的mcp工具</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def CamTags(self):
        r"""<p>资源标签</p>
        :rtype: list of Tag
        """
        return self._CamTags

    @CamTags.setter
    def CamTags(self, CamTags):
        self._CamTags = CamTags

    @property
    def EnvVars(self):
        r"""<p>agent运行时环境变量</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Tags = params.get("Tags")
        if params.get("Instruction") is not None:
            self._Instruction = InstructionConfig()
            self._Instruction._deserialize(params.get("Instruction"))
        self._SkillIds = params.get("SkillIds")
        self._Source = params.get("Source")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("CamTags") is not None:
            self._CamTags = []
            for item in params.get("CamTags"):
                obj = Tag()
                obj._deserialize(item)
                self._CamTags.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchAgentResponse(AbstractModel):
    r"""CreateAIWorkbenchAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
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


class CreateAIWorkbenchTaskRequest(AbstractModel):
    r"""CreateAIWorkbenchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>任务名称</p>
        :type Name: str
        :param _Description: <p>任务描述</p>
        :type Description: str
        :param _AgentId: <p>关联 Agent ID</p>
        :type AgentId: str
        :param _PromptTemplate: <p>提示词模板</p>
        :type PromptTemplate: str
        :param _OutputFormat: <p>输出格式: markdown / json</p>
        :type OutputFormat: str
        :param _TriggerType: <p>触发类型: manual / cron / webhook</p>
        :type TriggerType: str
        :param _CronExpr: <p>Cron 表达式</p>
        :type CronExpr: str
        :param _CronTimezone: <p>Cron 时区</p>
        :type CronTimezone: str
        :param _ResourceMapId: <p>关联资源地图 ID</p>
        :type ResourceMapId: str
        :param _SkillIds: <p>技能 ID 列表</p>
        :type SkillIds: list of str
        :param _McpEndpointIds: <p>MCP 端点 ID 列表</p>
        :type McpEndpointIds: list of str
        :param _TimeoutSec: <p>超时时间(秒)</p>
        :type TimeoutSec: int
        :param _RetryCount: <p>重试次数</p>
        :type RetryCount: int
        :param _Enabled: <p>是否启用</p>
        :type Enabled: bool
        """
        self._Name = None
        self._Description = None
        self._AgentId = None
        self._PromptTemplate = None
        self._OutputFormat = None
        self._TriggerType = None
        self._CronExpr = None
        self._CronTimezone = None
        self._ResourceMapId = None
        self._SkillIds = None
        self._McpEndpointIds = None
        self._TimeoutSec = None
        self._RetryCount = None
        self._Enabled = None

    @property
    def Name(self):
        r"""<p>任务名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>任务描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AgentId(self):
        r"""<p>关联 Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def PromptTemplate(self):
        r"""<p>提示词模板</p>
        :rtype: str
        """
        return self._PromptTemplate

    @PromptTemplate.setter
    def PromptTemplate(self, PromptTemplate):
        self._PromptTemplate = PromptTemplate

    @property
    def OutputFormat(self):
        r"""<p>输出格式: markdown / json</p>
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def TriggerType(self):
        r"""<p>触发类型: manual / cron / webhook</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def CronExpr(self):
        r"""<p>Cron 表达式</p>
        :rtype: str
        """
        return self._CronExpr

    @CronExpr.setter
    def CronExpr(self, CronExpr):
        self._CronExpr = CronExpr

    @property
    def CronTimezone(self):
        r"""<p>Cron 时区</p>
        :rtype: str
        """
        return self._CronTimezone

    @CronTimezone.setter
    def CronTimezone(self, CronTimezone):
        self._CronTimezone = CronTimezone

    @property
    def ResourceMapId(self):
        r"""<p>关联资源地图 ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def SkillIds(self):
        r"""<p>技能 ID 列表</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def McpEndpointIds(self):
        r"""<p>MCP 端点 ID 列表</p>
        :rtype: list of str
        """
        return self._McpEndpointIds

    @McpEndpointIds.setter
    def McpEndpointIds(self, McpEndpointIds):
        self._McpEndpointIds = McpEndpointIds

    @property
    def TimeoutSec(self):
        r"""<p>超时时间(秒)</p>
        :rtype: int
        """
        return self._TimeoutSec

    @TimeoutSec.setter
    def TimeoutSec(self, TimeoutSec):
        self._TimeoutSec = TimeoutSec

    @property
    def RetryCount(self):
        r"""<p>重试次数</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AgentId = params.get("AgentId")
        self._PromptTemplate = params.get("PromptTemplate")
        self._OutputFormat = params.get("OutputFormat")
        self._TriggerType = params.get("TriggerType")
        self._CronExpr = params.get("CronExpr")
        self._CronTimezone = params.get("CronTimezone")
        self._ResourceMapId = params.get("ResourceMapId")
        self._SkillIds = params.get("SkillIds")
        self._McpEndpointIds = params.get("McpEndpointIds")
        self._TimeoutSec = params.get("TimeoutSec")
        self._RetryCount = params.get("RetryCount")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchTaskResponse(AbstractModel):
    r"""CreateAIWorkbenchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
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


class CreateDispenseExternalRuleRequest(AbstractModel):
    r"""CreateDispenseExternalRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _ExtNamespace: 云监控对外命名空间
        :type ExtNamespace: str
        :param _Producer: 转发目标消信息
        :type Producer: :class:`tencentcloud.monitor.v20230616.models.Producer`
        :param _DispenseRegions: 转发部署地域列表
        :type DispenseRegions: list of str
        :param _ExtMetrics: 云监控对外指标
        :type ExtMetrics: list of str
        :param _Period: 指标统计周期
        :type Period: list of int
        :param _DispenseConditions: 转发过滤条件信息
        :type DispenseConditions: list of DispenseCondition
        """
        self._Name = None
        self._ExtNamespace = None
        self._Producer = None
        self._DispenseRegions = None
        self._ExtMetrics = None
        self._Period = None
        self._DispenseConditions = None

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExtNamespace(self):
        r"""云监控对外命名空间
        :rtype: str
        """
        return self._ExtNamespace

    @ExtNamespace.setter
    def ExtNamespace(self, ExtNamespace):
        self._ExtNamespace = ExtNamespace

    @property
    def Producer(self):
        r"""转发目标消信息
        :rtype: :class:`tencentcloud.monitor.v20230616.models.Producer`
        """
        return self._Producer

    @Producer.setter
    def Producer(self, Producer):
        self._Producer = Producer

    @property
    def DispenseRegions(self):
        r"""转发部署地域列表
        :rtype: list of str
        """
        return self._DispenseRegions

    @DispenseRegions.setter
    def DispenseRegions(self, DispenseRegions):
        self._DispenseRegions = DispenseRegions

    @property
    def ExtMetrics(self):
        r"""云监控对外指标
        :rtype: list of str
        """
        return self._ExtMetrics

    @ExtMetrics.setter
    def ExtMetrics(self, ExtMetrics):
        self._ExtMetrics = ExtMetrics

    @property
    def Period(self):
        r"""指标统计周期
        :rtype: list of int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def DispenseConditions(self):
        r"""转发过滤条件信息
        :rtype: list of DispenseCondition
        """
        return self._DispenseConditions

    @DispenseConditions.setter
    def DispenseConditions(self, DispenseConditions):
        self._DispenseConditions = DispenseConditions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ExtNamespace = params.get("ExtNamespace")
        if params.get("Producer") is not None:
            self._Producer = Producer()
            self._Producer._deserialize(params.get("Producer"))
        self._DispenseRegions = params.get("DispenseRegions")
        self._ExtMetrics = params.get("ExtMetrics")
        self._Period = params.get("Period")
        if params.get("DispenseConditions") is not None:
            self._DispenseConditions = []
            for item in params.get("DispenseConditions"):
                obj = DispenseCondition()
                obj._deserialize(item)
                self._DispenseConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDispenseExternalRuleResponse(AbstractModel):
    r"""CreateDispenseExternalRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 转发规则Id
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        r"""转发规则Id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateNoticeContentTmplRequest(AbstractModel):
    r"""CreateNoticeContentTmpl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplName: <p>模板名称</p>
        :type TmplName: str
        :param _MonitorType: <p>监控类型</p>
        :type MonitorType: str
        :param _TmplContents: <p>模板内容</p>
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _TmplLanguage: <p>模板语言 en/zh</p>
        :type TmplLanguage: str
        """
        self._TmplName = None
        self._MonitorType = None
        self._TmplContents = None
        self._TmplLanguage = None

    @property
    def TmplName(self):
        r"""<p>模板名称</p>
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def MonitorType(self):
        r"""<p>监控类型</p>
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def TmplContents(self):
        r"""<p>模板内容</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        """
        return self._TmplContents

    @TmplContents.setter
    def TmplContents(self, TmplContents):
        self._TmplContents = TmplContents

    @property
    def TmplLanguage(self):
        r"""<p>模板语言 en/zh</p>
        :rtype: str
        """
        return self._TmplLanguage

    @TmplLanguage.setter
    def TmplLanguage(self, TmplLanguage):
        self._TmplLanguage = TmplLanguage


    def _deserialize(self, params):
        self._TmplName = params.get("TmplName")
        self._MonitorType = params.get("MonitorType")
        if params.get("TmplContents") is not None:
            self._TmplContents = NoticeContentTmplItem()
            self._TmplContents._deserialize(params.get("TmplContents"))
        self._TmplLanguage = params.get("TmplLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNoticeContentTmplResponse(AbstractModel):
    r"""CreateNoticeContentTmpl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplID: <p>自定义内容模板ID</p>
        :type TmplID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TmplID = None
        self._RequestId = None

    @property
    def TmplID(self):
        r"""<p>自定义内容模板ID</p>
        :rtype: str
        """
        return self._TmplID

    @TmplID.setter
    def TmplID(self, TmplID):
        self._TmplID = TmplID

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TmplID = params.get("TmplID")
        self._RequestId = params.get("RequestId")


class DeleteAIWorkbenchAgentRequest(AbstractModel):
    r"""DeleteAIWorkbenchAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIWorkbenchAgentResponse(AbstractModel):
    r"""DeleteAIWorkbenchAgent返回参数结构体

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


class DeleteAIWorkbenchTaskRequest(AbstractModel):
    r"""DeleteAIWorkbenchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务 ID</p>
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIWorkbenchTaskResponse(AbstractModel):
    r"""DeleteAIWorkbenchTask返回参数结构体

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


class DeleteDispenseExternalRuleRequest(AbstractModel):
    r"""DeleteDispenseExternalRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIdList: 需要删除的规则Id
        :type RuleIdList: list of int
        """
        self._RuleIdList = None

    @property
    def RuleIdList(self):
        r"""需要删除的规则Id
        :rtype: list of int
        """
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDispenseExternalRuleResponse(AbstractModel):
    r"""DeleteDispenseExternalRule返回参数结构体

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


class DeleteNoticeContentTmplsRequest(AbstractModel):
    r"""DeleteNoticeContentTmpls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplIDs: <p>要删除的模板id</p>
        :type TmplIDs: list of str
        """
        self._TmplIDs = None

    @property
    def TmplIDs(self):
        r"""<p>要删除的模板id</p>
        :rtype: list of str
        """
        return self._TmplIDs

    @TmplIDs.setter
    def TmplIDs(self, TmplIDs):
        self._TmplIDs = TmplIDs


    def _deserialize(self, params):
        self._TmplIDs = params.get("TmplIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNoticeContentTmplsResponse(AbstractModel):
    r"""DeleteNoticeContentTmpls返回参数结构体

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


class DescribeAIWorkbenchAgentRequest(AbstractModel):
    r"""DescribeAIWorkbenchAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchAgentResponse(AbstractModel):
    r"""DescribeAIWorkbenchAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: <p>Agent 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Agent: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Agent = None
        self._RequestId = None

    @property
    def Agent(self):
        r"""<p>Agent 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
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
            self._Agent = AgentInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchArtifactRequest(AbstractModel):
    r"""DescribeAIWorkbenchArtifact请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ArtifactId: <p>产物 ID</p>
        :type ArtifactId: str
        :param _NeedDownloadURL: <p>是否需要下载 URL</p><p><code>1</code> = 需要，<code>0</code> 或不传 = 不需要</p>
        :type NeedDownloadURL: int
        """
        self._ArtifactId = None
        self._NeedDownloadURL = None

    @property
    def ArtifactId(self):
        r"""<p>产物 ID</p>
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId

    @property
    def NeedDownloadURL(self):
        r"""<p>是否需要下载 URL</p><p><code>1</code> = 需要，<code>0</code> 或不传 = 不需要</p>
        :rtype: int
        """
        return self._NeedDownloadURL

    @NeedDownloadURL.setter
    def NeedDownloadURL(self, NeedDownloadURL):
        self._NeedDownloadURL = NeedDownloadURL


    def _deserialize(self, params):
        self._ArtifactId = params.get("ArtifactId")
        self._NeedDownloadURL = params.get("NeedDownloadURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchArtifactResponse(AbstractModel):
    r"""DescribeAIWorkbenchArtifact返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Artifact: <p>产物信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Artifact: :class:`tencentcloud.monitor.v20230616.models.ArtifactInfo`
        :param _DownloadURL: <p>COS 预签名下载 URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadURL: str
        :param _DownloadURLExpiredAt: <p>下载 URL 过期时间（RFC3339 格式）</p>
        :type DownloadURLExpiredAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Artifact = None
        self._DownloadURL = None
        self._DownloadURLExpiredAt = None
        self._RequestId = None

    @property
    def Artifact(self):
        r"""<p>产物信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ArtifactInfo`
        """
        return self._Artifact

    @Artifact.setter
    def Artifact(self, Artifact):
        self._Artifact = Artifact

    @property
    def DownloadURL(self):
        r"""<p>COS 预签名下载 URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def DownloadURLExpiredAt(self):
        r"""<p>下载 URL 过期时间（RFC3339 格式）</p>
        :rtype: str
        """
        return self._DownloadURLExpiredAt

    @DownloadURLExpiredAt.setter
    def DownloadURLExpiredAt(self, DownloadURLExpiredAt):
        self._DownloadURLExpiredAt = DownloadURLExpiredAt

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Artifact") is not None:
            self._Artifact = ArtifactInfo()
            self._Artifact._deserialize(params.get("Artifact"))
        self._DownloadURL = params.get("DownloadURL")
        self._DownloadURLExpiredAt = params.get("DownloadURLExpiredAt")
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchExecutionRequest(AbstractModel):
    r"""DescribeAIWorkbenchExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionId: <p>执行 ID</p>
        :type ExecutionId: str
        """
        self._ExecutionId = None

    @property
    def ExecutionId(self):
        r"""<p>执行 ID</p>
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId


    def _deserialize(self, params):
        self._ExecutionId = params.get("ExecutionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchExecutionResponse(AbstractModel):
    r"""DescribeAIWorkbenchExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Execution: <p>执行记录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Execution: :class:`tencentcloud.monitor.v20230616.models.ExecutionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        r"""<p>执行记录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ExecutionInfo`
        """
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self._Execution = ExecutionInfo()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSREDigitalTwinTaskListRequest(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TwinID: 数字分身ID
        :type TwinID: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        """
        self._TwinID = None
        self._Offset = None
        self._Limit = None

    @property
    def TwinID(self):
        r"""数字分身ID
        :rtype: int
        """
        return self._TwinID

    @TwinID.setter
    def TwinID(self, TwinID):
        self._TwinID = TwinID

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
    def Limit(self):
        r"""数量限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TwinID = params.get("TwinID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSREDigitalTwinTaskListResponse(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JSONStrPaths: Json序列化路径
        :type JSONStrPaths: list of str
        :param _Data: 数字分身任务列表
        :type Data: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinTaskList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JSONStrPaths = None
        self._Data = None
        self._RequestId = None

    @property
    def JSONStrPaths(self):
        r"""Json序列化路径
        :rtype: list of str
        """
        return self._JSONStrPaths

    @JSONStrPaths.setter
    def JSONStrPaths(self, JSONStrPaths):
        self._JSONStrPaths = JSONStrPaths

    @property
    def Data(self):
        r"""数字分身任务列表
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinTaskList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JSONStrPaths = params.get("JSONStrPaths")
        if params.get("Data") is not None:
            self._Data = AIWorkbenchSREDigitalTwinTaskList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSREDigitalTwinWorkLogDetailRequest(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinWorkLogDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkLogID: 工作日志ID
        :type WorkLogID: int
        """
        self._WorkLogID = None

    @property
    def WorkLogID(self):
        r"""工作日志ID
        :rtype: int
        """
        return self._WorkLogID

    @WorkLogID.setter
    def WorkLogID(self, WorkLogID):
        self._WorkLogID = WorkLogID


    def _deserialize(self, params):
        self._WorkLogID = params.get("WorkLogID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinWorkLogDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JSONStrPaths: Json序列化路径
        :type JSONStrPaths: list of str
        :param _Data: 数字分身详细信息
        :type Data: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinWorkLogDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JSONStrPaths = None
        self._Data = None
        self._RequestId = None

    @property
    def JSONStrPaths(self):
        r"""Json序列化路径
        :rtype: list of str
        """
        return self._JSONStrPaths

    @JSONStrPaths.setter
    def JSONStrPaths(self, JSONStrPaths):
        self._JSONStrPaths = JSONStrPaths

    @property
    def Data(self):
        r"""数字分身详细信息
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinWorkLogDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JSONStrPaths = params.get("JSONStrPaths")
        if params.get("Data") is not None:
            self._Data = AIWorkbenchSREDigitalTwinWorkLogDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSREDigitalTwinWorkLogListRequest(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinWorkLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TwinID: 数字分身ID
        :type TwinID: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页限制条数
        :type Limit: int
        """
        self._TwinID = None
        self._Offset = None
        self._Limit = None

    @property
    def TwinID(self):
        r"""数字分身ID
        :rtype: int
        """
        return self._TwinID

    @TwinID.setter
    def TwinID(self, TwinID):
        self._TwinID = TwinID

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TwinID = params.get("TwinID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse(AbstractModel):
    r"""DescribeAIWorkbenchSREDigitalTwinWorkLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JSONStrPaths: Json序列化路径
        :type JSONStrPaths: list of str
        :param _Data: 数字分身工作日志列表
        :type Data: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinWorkLogList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JSONStrPaths = None
        self._Data = None
        self._RequestId = None

    @property
    def JSONStrPaths(self):
        r"""Json序列化路径
        :rtype: list of str
        """
        return self._JSONStrPaths

    @JSONStrPaths.setter
    def JSONStrPaths(self, JSONStrPaths):
        self._JSONStrPaths = JSONStrPaths

    @property
    def Data(self):
        r"""数字分身工作日志列表
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AIWorkbenchSREDigitalTwinWorkLogList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JSONStrPaths = params.get("JSONStrPaths")
        if params.get("Data") is not None:
            self._Data = AIWorkbenchSREDigitalTwinWorkLogList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSessionRequest(AbstractModel):
    r"""DescribeAIWorkbenchSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID</p>
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSessionResponse(AbstractModel):
    r"""DescribeAIWorkbenchSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: <p>会话信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Session: :class:`tencentcloud.monitor.v20230616.models.SessionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        r"""<p>会话信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.SessionInfo`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self._Session = SessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSkillRequest(AbstractModel):
    r"""DescribeAIWorkbenchSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>技能 ID</p>
        :type SkillId: str
        """
        self._SkillId = None

    @property
    def SkillId(self):
        r"""<p>技能 ID</p>
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
        


class DescribeAIWorkbenchSkillResponse(AbstractModel):
    r"""DescribeAIWorkbenchSkill返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Skill: <p>技能信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Skill: :class:`tencentcloud.monitor.v20230616.models.SkillInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Skill = None
        self._RequestId = None

    @property
    def Skill(self):
        r"""<p>技能信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.SkillInfo`
        """
        return self._Skill

    @Skill.setter
    def Skill(self, Skill):
        self._Skill = Skill

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Skill") is not None:
            self._Skill = SkillInfo()
            self._Skill._deserialize(params.get("Skill"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmNotifyHistoriesRequest(AbstractModel):
    r"""DescribeAlarmNotifyHistories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _QueryBaseTime: 起始时间点，unix秒级时间戳
        :type QueryBaseTime: int
        :param _QueryBeforeSeconds: 从 QueryBaseTime 开始，需要查询往前多久的时间，单位秒
        :type QueryBeforeSeconds: int
        :param _PageParams: 分页参数
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        :param _Namespace: 当监控类型为 MT_QCE 时候需要填写，归属的命名空间
        :type Namespace: str
        :param _ModelName: 当监控类型为 MT_QCE 时候需要填写， 告警策略类型
        :type ModelName: str
        :param _PolicyId: 查询某个策略的通知历史
        :type PolicyId: str
        """
        self._MonitorType = None
        self._QueryBaseTime = None
        self._QueryBeforeSeconds = None
        self._PageParams = None
        self._Namespace = None
        self._ModelName = None
        self._PolicyId = None

    @property
    def MonitorType(self):
        r"""监控类型
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def QueryBaseTime(self):
        r"""起始时间点，unix秒级时间戳
        :rtype: int
        """
        return self._QueryBaseTime

    @QueryBaseTime.setter
    def QueryBaseTime(self, QueryBaseTime):
        self._QueryBaseTime = QueryBaseTime

    @property
    def QueryBeforeSeconds(self):
        r"""从 QueryBaseTime 开始，需要查询往前多久的时间，单位秒
        :rtype: int
        """
        return self._QueryBeforeSeconds

    @QueryBeforeSeconds.setter
    def QueryBeforeSeconds(self, QueryBeforeSeconds):
        self._QueryBeforeSeconds = QueryBeforeSeconds

    @property
    def PageParams(self):
        r"""分页参数
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams

    @property
    def Namespace(self):
        r"""当监控类型为 MT_QCE 时候需要填写，归属的命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ModelName(self):
        r"""当监控类型为 MT_QCE 时候需要填写， 告警策略类型
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PolicyId(self):
        r"""查询某个策略的通知历史
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._QueryBaseTime = params.get("QueryBaseTime")
        self._QueryBeforeSeconds = params.get("QueryBeforeSeconds")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNoParams()
            self._PageParams._deserialize(params.get("PageParams"))
        self._Namespace = params.get("Namespace")
        self._ModelName = params.get("ModelName")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNotifyHistoriesResponse(AbstractModel):
    r"""DescribeAlarmNotifyHistories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyHistoryList: 告警历史
        :type AlarmNotifyHistoryList: list of AlarmNotifyHistory
        :param _PageResult: 分页情况
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmNotifyHistoryList = None
        self._PageResult = None
        self._RequestId = None

    @property
    def AlarmNotifyHistoryList(self):
        r"""告警历史
        :rtype: list of AlarmNotifyHistory
        """
        return self._AlarmNotifyHistoryList

    @AlarmNotifyHistoryList.setter
    def AlarmNotifyHistoryList(self, AlarmNotifyHistoryList):
        self._AlarmNotifyHistoryList = AlarmNotifyHistoryList

    @property
    def PageResult(self):
        r"""分页情况
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlarmNotifyHistoryList") is not None:
            self._AlarmNotifyHistoryList = []
            for item in params.get("AlarmNotifyHistoryList"):
                obj = AlarmNotifyHistory()
                obj._deserialize(item)
                self._AlarmNotifyHistoryList.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNoResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class DescribeDispenseExternalRuleListRequest(AbstractModel):
    r"""DescribeDispenseExternalRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Page: 页数
        :type Page: int
        :param _PageSize: 页面大小
        :type PageSize: int
        :param _DispenseRegions: 转发部署地域
        :type DispenseRegions: list of str
        :param _Keyword: 关键字搜索规则名
        :type Keyword: str
        """
        self._Page = None
        self._PageSize = None
        self._DispenseRegions = None
        self._Keyword = None

    @property
    def Page(self):
        r"""页数
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

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
    def DispenseRegions(self):
        r"""转发部署地域
        :rtype: list of str
        """
        return self._DispenseRegions

    @DispenseRegions.setter
    def DispenseRegions(self, DispenseRegions):
        self._DispenseRegions = DispenseRegions

    @property
    def Keyword(self):
        r"""关键字搜索规则名
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._DispenseRegions = params.get("DispenseRegions")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDispenseExternalRuleListResponse(AbstractModel):
    r"""DescribeDispenseExternalRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleList: 指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleList: list of Rule
        :param _TotalCount: 列表大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RuleList(self):
        r"""指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Rule
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def TotalCount(self):
        r"""列表大小
注意：此字段可能返回 null，表示取不到有效值。
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
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = Rule()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDispenseExternalRuleRequest(AbstractModel):
    r"""DescribeDispenseExternalRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则id
        :type RuleId: int
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则id
        :rtype: int
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
        


class DescribeDispenseExternalRuleResponse(AbstractModel):
    r"""DescribeDispenseExternalRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.monitor.v20230616.models.Rule`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.monitor.v20230616.models.Rule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = Rule()
            self._Rule._deserialize(params.get("Rule"))
        self._RequestId = params.get("RequestId")


class DescribeDispenseRegionRequest(AbstractModel):
    r"""DescribeDispenseRegion请求参数结构体

    """


class DescribeDispenseRegionResponse(AbstractModel):
    r"""DescribeDispenseRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionList: 转发地域列表
        :type RegionList: list of DispenseRegion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        r"""转发地域列表
        :rtype: list of DispenseRegion
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = DispenseRegion()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtMetricRequest(AbstractModel):
    r"""DescribeExtMetric请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtNamespace: 对外命名空间
        :type ExtNamespace: str
        """
        self._ExtNamespace = None

    @property
    def ExtNamespace(self):
        r"""对外命名空间
        :rtype: str
        """
        return self._ExtNamespace

    @ExtNamespace.setter
    def ExtNamespace(self, ExtNamespace):
        self._ExtNamespace = ExtNamespace


    def _deserialize(self, params):
        self._ExtNamespace = params.get("ExtNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtMetricResponse(AbstractModel):
    r"""DescribeExtMetric返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtMetricList: 对外指标
        :type ExtMetricList: list of ExtMetric
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExtMetricList = None
        self._RequestId = None

    @property
    def ExtMetricList(self):
        r"""对外指标
        :rtype: list of ExtMetric
        """
        return self._ExtMetricList

    @ExtMetricList.setter
    def ExtMetricList(self, ExtMetricList):
        self._ExtMetricList = ExtMetricList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ExtMetricList") is not None:
            self._ExtMetricList = []
            for item in params.get("ExtMetricList"):
                obj = ExtMetric()
                obj._deserialize(item)
                self._ExtMetricList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtNamespaceRequest(AbstractModel):
    r"""DescribeExtNamespace请求参数结构体

    """


class DescribeExtNamespaceResponse(AbstractModel):
    r"""DescribeExtNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtNamespaceList: 对外命名空间列表
        :type ExtNamespaceList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExtNamespaceList = None
        self._RequestId = None

    @property
    def ExtNamespaceList(self):
        r"""对外命名空间列表
        :rtype: list of str
        """
        return self._ExtNamespaceList

    @ExtNamespaceList.setter
    def ExtNamespaceList(self, ExtNamespaceList):
        self._ExtNamespaceList = ExtNamespaceList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExtNamespaceList = params.get("ExtNamespaceList")
        self._RequestId = params.get("RequestId")


class DescribeKafkaRequest(AbstractModel):
    r"""DescribeKafka请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Brokers: kafka地址
        :type Brokers: str
        :param _DispenseRegions: 转发部署地域列表
        :type DispenseRegions: list of str
        """
        self._Brokers = None
        self._DispenseRegions = None

    @property
    def Brokers(self):
        r"""kafka地址
        :rtype: str
        """
        return self._Brokers

    @Brokers.setter
    def Brokers(self, Brokers):
        self._Brokers = Brokers

    @property
    def DispenseRegions(self):
        r"""转发部署地域列表
        :rtype: list of str
        """
        return self._DispenseRegions

    @DispenseRegions.setter
    def DispenseRegions(self, DispenseRegions):
        self._DispenseRegions = DispenseRegions


    def _deserialize(self, params):
        self._Brokers = params.get("Brokers")
        self._DispenseRegions = params.get("DispenseRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaResponse(AbstractModel):
    r"""DescribeKafka返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KafkaConnectivityList: 连通性列表
        :type KafkaConnectivityList: list of KafkaConnectivity
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KafkaConnectivityList = None
        self._RequestId = None

    @property
    def KafkaConnectivityList(self):
        r"""连通性列表
        :rtype: list of KafkaConnectivity
        """
        return self._KafkaConnectivityList

    @KafkaConnectivityList.setter
    def KafkaConnectivityList(self, KafkaConnectivityList):
        self._KafkaConnectivityList = KafkaConnectivityList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KafkaConnectivityList") is not None:
            self._KafkaConnectivityList = []
            for item in params.get("KafkaConnectivityList"):
                obj = KafkaConnectivity()
                obj._deserialize(item)
                self._KafkaConnectivityList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNoticeContentTmplRequest(AbstractModel):
    r"""DescribeNoticeContentTmpl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页数
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _TmplIDs: 指定模板ID查询，查询参数都为空则默认查询账号下所有模板
        :type TmplIDs: list of str
        :param _TmplName: 指定模板名称查询，查询参数都为空则默认查询账号下所有模板
        :type TmplName: str
        :param _NoticeID: 指定通知模板ID查询，查询参数都为空则默认查询账号下所有模板
        :type NoticeID: str
        :param _TmplLanguage: 模板语言 en/zh 缺省不过滤
        :type TmplLanguage: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._TmplIDs = None
        self._TmplName = None
        self._NoticeID = None
        self._TmplLanguage = None
        self._MonitorType = None

    @property
    def PageNumber(self):
        r"""分页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TmplIDs(self):
        r"""指定模板ID查询，查询参数都为空则默认查询账号下所有模板
        :rtype: list of str
        """
        return self._TmplIDs

    @TmplIDs.setter
    def TmplIDs(self, TmplIDs):
        self._TmplIDs = TmplIDs

    @property
    def TmplName(self):
        r"""指定模板名称查询，查询参数都为空则默认查询账号下所有模板
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def NoticeID(self):
        r"""指定通知模板ID查询，查询参数都为空则默认查询账号下所有模板
        :rtype: str
        """
        return self._NoticeID

    @NoticeID.setter
    def NoticeID(self, NoticeID):
        self._NoticeID = NoticeID

    @property
    def TmplLanguage(self):
        r"""模板语言 en/zh 缺省不过滤
        :rtype: str
        """
        return self._TmplLanguage

    @TmplLanguage.setter
    def TmplLanguage(self, TmplLanguage):
        self._TmplLanguage = TmplLanguage

    @property
    def MonitorType(self):
        r"""监控类型
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TmplIDs = params.get("TmplIDs")
        self._TmplName = params.get("TmplName")
        self._NoticeID = params.get("NoticeID")
        self._TmplLanguage = params.get("TmplLanguage")
        self._MonitorType = params.get("MonitorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNoticeContentTmplResponse(AbstractModel):
    r"""DescribeNoticeContentTmpl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeContentTmpls: 自定义通知内容模板
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeContentTmpls: list of NoticeContentTmpl
        :param _NoticeContentTmplBindPolicyCounts: 通知内容模板绑定的告警策略数量
        :type NoticeContentTmplBindPolicyCounts: list of NoticeContentTmplBindPolicyCount
        :param _PageNumber: 分页数
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoticeContentTmpls = None
        self._NoticeContentTmplBindPolicyCounts = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NoticeContentTmpls(self):
        r"""自定义通知内容模板
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NoticeContentTmpl
        """
        return self._NoticeContentTmpls

    @NoticeContentTmpls.setter
    def NoticeContentTmpls(self, NoticeContentTmpls):
        self._NoticeContentTmpls = NoticeContentTmpls

    @property
    def NoticeContentTmplBindPolicyCounts(self):
        r"""通知内容模板绑定的告警策略数量
        :rtype: list of NoticeContentTmplBindPolicyCount
        """
        return self._NoticeContentTmplBindPolicyCounts

    @NoticeContentTmplBindPolicyCounts.setter
    def NoticeContentTmplBindPolicyCounts(self, NoticeContentTmplBindPolicyCounts):
        self._NoticeContentTmplBindPolicyCounts = NoticeContentTmplBindPolicyCounts

    @property
    def PageNumber(self):
        r"""分页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""结果总数
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
        if params.get("NoticeContentTmpls") is not None:
            self._NoticeContentTmpls = []
            for item in params.get("NoticeContentTmpls"):
                obj = NoticeContentTmpl()
                obj._deserialize(item)
                self._NoticeContentTmpls.append(obj)
        if params.get("NoticeContentTmplBindPolicyCounts") is not None:
            self._NoticeContentTmplBindPolicyCounts = []
            for item in params.get("NoticeContentTmplBindPolicyCounts"):
                obj = NoticeContentTmplBindPolicyCount()
                obj._deserialize(item)
                self._NoticeContentTmplBindPolicyCounts.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DingDingRobotNoticeTmpl(AbstractModel):
    r"""钉钉机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        :param _TitleTmpl: 标题模板
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""标题模板
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DingDingRobotNoticeTmplMatcher(AbstractModel):
    r"""钉钉机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.DingDingRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DingDingRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = DingDingRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DispenseCondition(AbstractModel):
    r"""转发过滤条件信息

    """

    def __init__(self):
        r"""
        :param _ExtMetric: 对外指标名
        :type ExtMetric: str
        :param _DispenseFilters: 过滤条件表
        :type DispenseFilters: list of DispenseFilter
        :param _ConditionId: 过滤条件id
        :type ConditionId: int
        """
        self._ExtMetric = None
        self._DispenseFilters = None
        self._ConditionId = None

    @property
    def ExtMetric(self):
        r"""对外指标名
        :rtype: str
        """
        return self._ExtMetric

    @ExtMetric.setter
    def ExtMetric(self, ExtMetric):
        self._ExtMetric = ExtMetric

    @property
    def DispenseFilters(self):
        r"""过滤条件表
        :rtype: list of DispenseFilter
        """
        return self._DispenseFilters

    @DispenseFilters.setter
    def DispenseFilters(self, DispenseFilters):
        self._DispenseFilters = DispenseFilters

    @property
    def ConditionId(self):
        r"""过滤条件id
        :rtype: int
        """
        return self._ConditionId

    @ConditionId.setter
    def ConditionId(self, ConditionId):
        self._ConditionId = ConditionId


    def _deserialize(self, params):
        self._ExtMetric = params.get("ExtMetric")
        if params.get("DispenseFilters") is not None:
            self._DispenseFilters = []
            for item in params.get("DispenseFilters"):
                obj = DispenseFilter()
                obj._deserialize(item)
                self._DispenseFilters.append(obj)
        self._ConditionId = params.get("ConditionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DispenseFilter(AbstractModel):
    r"""过滤表

    """

    def __init__(self):
        r"""
        :param _Key: 维度名称
        :type Key: str
        :param _Values: 维度值列表
        :type Values: list of str
        :param _Expression: 表示式
        :type Expression: str
        """
        self._Key = None
        self._Values = None
        self._Expression = None

    @property
    def Key(self):
        r"""维度名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""维度值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Expression(self):
        r"""表示式
        :rtype: str
        """
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DispenseGlobalTag(AbstractModel):
    r"""全局维度

    """

    def __init__(self):
        r"""
        :param _Key: 维度key
        :type Key: str
        :param _Value: 维度值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""维度key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""维度值
        :rtype: str
        """
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
        


class DispenseRegion(AbstractModel):
    r"""转发地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域缩写
        :type Region: str
        :param _RegionCnName: 地域中文名
        :type RegionCnName: str
        :param _RegionEnName: 地域英文名
        :type RegionEnName: str
        :param _RuleNumber: 规则数量
        :type RuleNumber: int
        """
        self._Region = None
        self._RegionCnName = None
        self._RegionEnName = None
        self._RuleNumber = None

    @property
    def Region(self):
        r"""地域缩写
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionCnName(self):
        r"""地域中文名
        :rtype: str
        """
        return self._RegionCnName

    @RegionCnName.setter
    def RegionCnName(self, RegionCnName):
        self._RegionCnName = RegionCnName

    @property
    def RegionEnName(self):
        r"""地域英文名
        :rtype: str
        """
        return self._RegionEnName

    @RegionEnName.setter
    def RegionEnName(self, RegionEnName):
        self._RegionEnName = RegionEnName

    @property
    def RuleNumber(self):
        r"""规则数量
        :rtype: int
        """
        return self._RuleNumber

    @RuleNumber.setter
    def RuleNumber(self, RuleNumber):
        self._RuleNumber = RuleNumber


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionCnName = params.get("RegionCnName")
        self._RegionEnName = params.get("RegionEnName")
        self._RuleNumber = params.get("RuleNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvEntry(AbstractModel):
    r"""环境变量entry

    """

    def __init__(self):
        r"""
        :param _Value: <p>环境变量value</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Sensitive: <p>是否脱敏</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Sensitive: bool
        """
        self._Value = None
        self._Sensitive = None

    @property
    def Value(self):
        r"""<p>环境变量value</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Sensitive(self):
        r"""<p>是否脱敏</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Sensitive

    @Sensitive.setter
    def Sensitive(self, Sensitive):
        self._Sensitive = Sensitive


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Sensitive = params.get("Sensitive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    r"""agent运行时所需环境变量

    """

    def __init__(self):
        r"""
        :param _Key: <p>环境变量key</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: <p>环境变量value</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.monitor.v20230616.models.EnvEntry`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>环境变量key</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>环境变量value</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.EnvEntry`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = EnvEntry()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionInfo(AbstractModel):
    r"""执行记录实体

    """

    def __init__(self):
        r"""
        :param _Name: <p>任务名</p>
        :type Name: str
        :param _TaskId: <p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _ExecutionId: <p>执行 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionId: str
        :param _AgentId: <p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _SessionId: <p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _TriggerType: <p>触发类型: manual / cron / webhook</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param _Status: <p>状态: pending/running/completed/failed/timeout/cancelled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Summary: <p>执行摘要</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: str
        :param _DurationMs: <p>执行耗时(毫秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationMs: int
        """
        self._Name = None
        self._TaskId = None
        self._ExecutionId = None
        self._AgentId = None
        self._SessionId = None
        self._TriggerType = None
        self._Status = None
        self._Summary = None
        self._DurationMs = None

    @property
    def Name(self):
        r"""<p>任务名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ExecutionId(self):
        r"""<p>执行 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def TriggerType(self):
        r"""<p>触发类型: manual / cron / webhook</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Status(self):
        r"""<p>状态: pending/running/completed/failed/timeout/cancelled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Summary(self):
        r"""<p>执行摘要</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def DurationMs(self):
        r"""<p>执行耗时(毫秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._ExecutionId = params.get("ExecutionId")
        self._AgentId = params.get("AgentId")
        self._SessionId = params.get("SessionId")
        self._TriggerType = params.get("TriggerType")
        self._Status = params.get("Status")
        self._Summary = params.get("Summary")
        self._DurationMs = params.get("DurationMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtMetric(AbstractModel):
    r"""对外指标

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _MetricCName: 中文指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricCName: str
        :param _CNMeaning: 中文含义
注意：此字段可能返回 null，表示取不到有效值。
        :type CNMeaning: str
        :param _EnMeaning: 英文含义
注意：此字段可能返回 null，表示取不到有效值。
        :type EnMeaning: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _DimensionFlag: 是否配置对外维度
        :type DimensionFlag: bool
        """
        self._MetricName = None
        self._MetricCName = None
        self._CNMeaning = None
        self._EnMeaning = None
        self._Unit = None
        self._DimensionFlag = None

    @property
    def MetricName(self):
        r"""指标名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricCName(self):
        r"""中文指标名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricCName

    @MetricCName.setter
    def MetricCName(self, MetricCName):
        self._MetricCName = MetricCName

    @property
    def CNMeaning(self):
        r"""中文含义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CNMeaning

    @CNMeaning.setter
    def CNMeaning(self, CNMeaning):
        self._CNMeaning = CNMeaning

    @property
    def EnMeaning(self):
        r"""英文含义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnMeaning

    @EnMeaning.setter
    def EnMeaning(self, EnMeaning):
        self._EnMeaning = EnMeaning

    @property
    def Unit(self):
        r"""单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def DimensionFlag(self):
        r"""是否配置对外维度
        :rtype: bool
        """
        return self._DimensionFlag

    @DimensionFlag.setter
    def DimensionFlag(self, DimensionFlag):
        self._DimensionFlag = DimensionFlag


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._MetricCName = params.get("MetricCName")
        self._CNMeaning = params.get("CNMeaning")
        self._EnMeaning = params.get("EnMeaning")
        self._Unit = params.get("Unit")
        self._DimensionFlag = params.get("DimensionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeiShuRobotNoticeTmpl(AbstractModel):
    r"""飞书机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: <p>内容模板</p>
        :type ContentTmpl: str
        :param _TitleTmpl: <p>标题模板</p>
        :type TitleTmpl: str
        :param _TitleColor: <p>通知内容模版标题自定义颜色</p>
        :type TitleColor: :class:`tencentcloud.monitor.v20230616.models.RobotNoticeTitleColor`
        """
        self._ContentTmpl = None
        self._TitleTmpl = None
        self._TitleColor = None

    @property
    def ContentTmpl(self):
        r"""<p>内容模板</p>
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""<p>标题模板</p>
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl

    @property
    def TitleColor(self):
        r"""<p>通知内容模版标题自定义颜色</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.RobotNoticeTitleColor`
        """
        return self._TitleColor

    @TitleColor.setter
    def TitleColor(self, TitleColor):
        self._TitleColor = TitleColor


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        if params.get("TitleColor") is not None:
            self._TitleColor = RobotNoticeTitleColor()
            self._TitleColor._deserialize(params.get("TitleColor"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeiShuRobotNoticeTmplMatcher(AbstractModel):
    r"""飞书机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.FeiShuRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.FeiShuRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = FeiShuRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAIWorkbenchArtifactDownloadURLRequest(AbstractModel):
    r"""GetAIWorkbenchArtifactDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话ID</p>
        :type SessionId: str
        :param _ArtifactId: <p>制品ID</p>
        :type ArtifactId: str
        """
        self._SessionId = None
        self._ArtifactId = None

    @property
    def SessionId(self):
        r"""<p>会话ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ArtifactId(self):
        r"""<p>制品ID</p>
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._ArtifactId = params.get("ArtifactId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAIWorkbenchArtifactDownloadURLResponse(AbstractModel):
    r"""GetAIWorkbenchArtifactDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadURL: <p>COS 预签名 HTTPS 下载 URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadURL: str
        :param _ExpiredAt: <p>URL 过期时间（RFC3339 格式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadURL = None
        self._ExpiredAt = None
        self._RequestId = None

    @property
    def DownloadURL(self):
        r"""<p>COS 预签名 HTTPS 下载 URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def ExpiredAt(self):
        r"""<p>URL 过期时间（RFC3339 格式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadURL = params.get("DownloadURL")
        self._ExpiredAt = params.get("ExpiredAt")
        self._RequestId = params.get("RequestId")


class GoogleChatRobotNoticeTmpl(AbstractModel):
    r"""Google Chat 机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GoogleChatRobotNoticeTmplMatcher(AbstractModel):
    r"""Google Chat 机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.GoogleChatRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.GoogleChatRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = GoogleChatRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstructionConfig(AbstractModel):
    r"""分身提示词配置

    """

    def __init__(self):
        r"""
        :param _RolePosition: <p>角色定义</p>
        :type RolePosition: str
        :param _CoreDuty: <p>核心职责</p>
        :type CoreDuty: str
        :param _CoreTruths: <p>核心原则</p>
        :type CoreTruths: str
        :param _Vibe: <p>风格约束</p>
        :type Vibe: str
        :param _Boundaries: <p>注意事项</p>
        :type Boundaries: str
        """
        self._RolePosition = None
        self._CoreDuty = None
        self._CoreTruths = None
        self._Vibe = None
        self._Boundaries = None

    @property
    def RolePosition(self):
        r"""<p>角色定义</p>
        :rtype: str
        """
        return self._RolePosition

    @RolePosition.setter
    def RolePosition(self, RolePosition):
        self._RolePosition = RolePosition

    @property
    def CoreDuty(self):
        r"""<p>核心职责</p>
        :rtype: str
        """
        return self._CoreDuty

    @CoreDuty.setter
    def CoreDuty(self, CoreDuty):
        self._CoreDuty = CoreDuty

    @property
    def CoreTruths(self):
        r"""<p>核心原则</p>
        :rtype: str
        """
        return self._CoreTruths

    @CoreTruths.setter
    def CoreTruths(self, CoreTruths):
        self._CoreTruths = CoreTruths

    @property
    def Vibe(self):
        r"""<p>风格约束</p>
        :rtype: str
        """
        return self._Vibe

    @Vibe.setter
    def Vibe(self, Vibe):
        self._Vibe = Vibe

    @property
    def Boundaries(self):
        r"""<p>注意事项</p>
        :rtype: str
        """
        return self._Boundaries

    @Boundaries.setter
    def Boundaries(self, Boundaries):
        self._Boundaries = Boundaries


    def _deserialize(self, params):
        self._RolePosition = params.get("RolePosition")
        self._CoreDuty = params.get("CoreDuty")
        self._CoreTruths = params.get("CoreTruths")
        self._Vibe = params.get("Vibe")
        self._Boundaries = params.get("Boundaries")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaConnectivity(AbstractModel):
    r"""kafka连通性

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _Result: 连通
        :type Result: bool
        """
        self._Region = None
        self._Result = None

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Result(self):
        r"""连通
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchAgentsRequest(AbstractModel):
    r"""ListAIWorkbenchAgents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _Status: <p>状态筛选</p>
        :type Status: str
        :param _Category: <p>分类筛选</p>
        :type Category: str
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        :param _Source: <p>来源筛选</p>
        :type Source: str
        :param _AgentIds: <p>Agent ID 列表筛选</p>
        :type AgentIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._Status = None
        self._Category = None
        self._Keyword = None
        self._Source = None
        self._AgentIds = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Status(self):
        r"""<p>状态筛选</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Category(self):
        r"""<p>分类筛选</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Source(self):
        r"""<p>来源筛选</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AgentIds(self):
        r"""<p>Agent ID 列表筛选</p>
        :rtype: list of str
        """
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Status = params.get("Status")
        self._Category = params.get("Category")
        self._Keyword = params.get("Keyword")
        self._Source = params.get("Source")
        self._AgentIds = params.get("AgentIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchAgentsResponse(AbstractModel):
    r"""ListAIWorkbenchAgents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Agents: <p>Agent 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Agents: list of AgentInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Agents = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Agents(self):
        r"""<p>Agent 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentInfo
        """
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = AgentInfo()
                obj._deserialize(item)
                self._Agents.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchArtifactsRequest(AbstractModel):
    r"""ListAIWorkbenchArtifacts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _SessionIds: <p>会话ID</p>
        :type SessionIds: list of str
        :param _MimeTypes: <p>消息内容类型</p>
        :type MimeTypes: list of str
        :param _OrderDirection: <p>排序</p><p>枚举值：</p><ul><li>ASC： 正序</li><li>DESC： 倒序</li></ul>
        :type OrderDirection: str
        """
        self._PerPage = None
        self._PageNo = None
        self._SessionIds = None
        self._MimeTypes = None
        self._OrderDirection = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def SessionIds(self):
        r"""<p>会话ID</p>
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds

    @property
    def MimeTypes(self):
        r"""<p>消息内容类型</p>
        :rtype: list of str
        """
        return self._MimeTypes

    @MimeTypes.setter
    def MimeTypes(self, MimeTypes):
        self._MimeTypes = MimeTypes

    @property
    def OrderDirection(self):
        r"""<p>排序</p><p>枚举值：</p><ul><li>ASC： 正序</li><li>DESC： 倒序</li></ul>
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._SessionIds = params.get("SessionIds")
        self._MimeTypes = params.get("MimeTypes")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchArtifactsResponse(AbstractModel):
    r"""ListAIWorkbenchArtifacts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Artifacts: <p>产物列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Artifacts: list of ArtifactInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Artifacts = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Artifacts(self):
        r"""<p>产物列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ArtifactInfo
        """
        return self._Artifacts

    @Artifacts.setter
    def Artifacts(self, Artifacts):
        self._Artifacts = Artifacts

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Artifacts") is not None:
            self._Artifacts = []
            for item in params.get("Artifacts"):
                obj = ArtifactInfo()
                obj._deserialize(item)
                self._Artifacts.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchExecutionsRequest(AbstractModel):
    r"""ListAIWorkbenchExecutions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _AgentId: <p>按 Agent 筛选</p>
        :type AgentId: str
        :param _Status: <p>按状态筛选</p>
        :type Status: str
        :param _ExecutionIds: <p>执行 ID 列表筛选</p>
        :type ExecutionIds: list of str
        :param _TaskIds: <p>任务id</p>
        :type TaskIds: list of str
        :param _TriggerType: <p>触发方式</p>
        :type TriggerType: str
        :param _Keyword: <p>关键值</p>
        :type Keyword: str
        :param _Enabled: <p>是否启用</p>
        :type Enabled: bool
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._Status = None
        self._ExecutionIds = None
        self._TaskIds = None
        self._TriggerType = None
        self._Keyword = None
        self._Enabled = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>按 Agent 筛选</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Status(self):
        r"""<p>按状态筛选</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExecutionIds(self):
        r"""<p>执行 ID 列表筛选</p>
        :rtype: list of str
        """
        return self._ExecutionIds

    @ExecutionIds.setter
    def ExecutionIds(self, ExecutionIds):
        self._ExecutionIds = ExecutionIds

    @property
    def TaskIds(self):
        r"""<p>任务id</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def TriggerType(self):
        r"""<p>触发方式</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Keyword(self):
        r"""<p>关键值</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._Status = params.get("Status")
        self._ExecutionIds = params.get("ExecutionIds")
        self._TaskIds = params.get("TaskIds")
        self._TriggerType = params.get("TriggerType")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchExecutionsResponse(AbstractModel):
    r"""ListAIWorkbenchExecutions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Executions: <p>执行列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Executions: list of ExecutionInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Executions = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Executions(self):
        r"""<p>执行列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExecutionInfo
        """
        return self._Executions

    @Executions.setter
    def Executions(self, Executions):
        self._Executions = Executions

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Executions") is not None:
            self._Executions = []
            for item in params.get("Executions"):
                obj = ExecutionInfo()
                obj._deserialize(item)
                self._Executions.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchMCPsRequest(AbstractModel):
    r"""ListAIWorkbenchMCPs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _Transport: <p>按传输协议筛选</p>
        :type Transport: str
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        :param _Enabled: <p>是否启用筛选</p>
        :type Enabled: bool
        :param _MCPIds: <p>关联的mcp</p>
        :type MCPIds: list of str
        :param _Type: <p>MCP类型（内置/私有）</p><p>枚举值：</p><ul><li>builtin： 平台内置</li><li>private： 用户自定义</li></ul>
        :type Type: str
        """
        self._PerPage = None
        self._PageNo = None
        self._Transport = None
        self._Keyword = None
        self._Enabled = None
        self._MCPIds = None
        self._Type = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Transport(self):
        r"""<p>按传输协议筛选</p>
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>是否启用筛选</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MCPIds(self):
        r"""<p>关联的mcp</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def Type(self):
        r"""<p>MCP类型（内置/私有）</p><p>枚举值：</p><ul><li>builtin： 平台内置</li><li>private： 用户自定义</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Transport = params.get("Transport")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        self._MCPIds = params.get("MCPIds")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchMCPsResponse(AbstractModel):
    r"""ListAIWorkbenchMCPs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MCPs: <p>MCP 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCPs: list of MCPInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MCPs = None
        self._PageResult = None
        self._RequestId = None

    @property
    def MCPs(self):
        r"""<p>MCP 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MCPInfo
        """
        return self._MCPs

    @MCPs.setter
    def MCPs(self, MCPs):
        self._MCPs = MCPs

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MCPs") is not None:
            self._MCPs = []
            for item in params.get("MCPs"):
                obj = MCPInfo()
                obj._deserialize(item)
                self._MCPs.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchMessagesRequest(AbstractModel):
    r"""ListAIWorkbenchMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID</p>
        :type SessionId: str
        :param _Cursor: <p>游标分页的定位标记</p>
        :type Cursor: str
        :param _Limit: <p>窗口大小</p>
        :type Limit: int
        :param _Direction: <p>拉取顺序</p>
        :type Direction: str
        """
        self._SessionId = None
        self._Cursor = None
        self._Limit = None
        self._Direction = None

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Cursor(self):
        r"""<p>游标分页的定位标记</p>
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        r"""<p>窗口大小</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Direction(self):
        r"""<p>拉取顺序</p>
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchMessagesResponse(AbstractModel):
    r"""ListAIWorkbenchMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: <p>消息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Messages: list of MessageInfo
        :param _NextCursor: <p>下一个游标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _HasMore: <p>还有后续吗</p>
        :type HasMore: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Messages = None
        self._NextCursor = None
        self._HasMore = None
        self._RequestId = None

    @property
    def Messages(self):
        r"""<p>消息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MessageInfo
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def NextCursor(self):
        r"""<p>下一个游标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def HasMore(self):
        r"""<p>还有后续吗</p>
        :rtype: bool
        """
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageInfo()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchResourceInstancesRequest(AbstractModel):
    r"""ListAIWorkbenchResourceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceMapId: <p>资源地图 ID</p>
        :type ResourceMapId: str
        :param _PageParams: <p>分页参数</p>
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNumParams`
        """
        self._ResourceMapId = None
        self._PageParams = None

    @property
    def ResourceMapId(self):
        r"""<p>资源地图 ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def PageParams(self):
        r"""<p>分页参数</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams


    def _deserialize(self, params):
        self._ResourceMapId = params.get("ResourceMapId")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNumParams()
            self._PageParams._deserialize(params.get("PageParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchResourceInstancesResponse(AbstractModel):
    r"""ListAIWorkbenchResourceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: <p>资源实例列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of ResourceInstance
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""<p>资源实例列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ResourceInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchResourceMapsRequest(AbstractModel):
    r"""ListAIWorkbenchResourceMaps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _Keyword: <p>按名称搜索</p>
        :type Keyword: str
        """
        self._PerPage = None
        self._PageNo = None
        self._Keyword = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Keyword(self):
        r"""<p>按名称搜索</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchResourceMapsResponse(AbstractModel):
    r"""ListAIWorkbenchResourceMaps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceMaps: <p>资源地图列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMaps: list of ResourceMapInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceMaps = None
        self._PageResult = None
        self._RequestId = None

    @property
    def ResourceMaps(self):
        r"""<p>资源地图列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceMapInfo
        """
        return self._ResourceMaps

    @ResourceMaps.setter
    def ResourceMaps(self, ResourceMaps):
        self._ResourceMaps = ResourceMaps

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceMaps") is not None:
            self._ResourceMaps = []
            for item in params.get("ResourceMaps"):
                obj = ResourceMapInfo()
                obj._deserialize(item)
                self._ResourceMaps.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchSessionsRequest(AbstractModel):
    r"""ListAIWorkbenchSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _AgentId: <p>按 Agent 筛选</p>
        :type AgentId: str
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        :param _SessionIds: <p>会话 ID 列表筛选</p>
        :type SessionIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._Keyword = None
        self._SessionIds = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>按 Agent 筛选</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SessionIds(self):
        r"""<p>会话 ID 列表筛选</p>
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._Keyword = params.get("Keyword")
        self._SessionIds = params.get("SessionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchSessionsResponse(AbstractModel):
    r"""ListAIWorkbenchSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sessions: <p>会话列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Sessions: list of SessionInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sessions = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Sessions(self):
        r"""<p>会话列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SessionInfo
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = SessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchSkillsRequest(AbstractModel):
    r"""ListAIWorkbenchSkills请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _Type: <p>按类型筛选</p>
        :type Type: str
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        :param _Enabled: <p>是否启用筛选</p>
        :type Enabled: bool
        :param _SkillIds: <p>技能 ID 列表筛选</p>
        :type SkillIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._Type = None
        self._Keyword = None
        self._Enabled = None
        self._SkillIds = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Type(self):
        r"""<p>按类型筛选</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>是否启用筛选</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def SkillIds(self):
        r"""<p>技能 ID 列表筛选</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Type = params.get("Type")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        self._SkillIds = params.get("SkillIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchSkillsResponse(AbstractModel):
    r"""ListAIWorkbenchSkills返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Skills: <p>技能列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Skills: list of SkillInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Skills = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Skills(self):
        r"""<p>技能列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SkillInfo
        """
        return self._Skills

    @Skills.setter
    def Skills(self, Skills):
        self._Skills = Skills

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Skills") is not None:
            self._Skills = []
            for item in params.get("Skills"):
                obj = SkillInfo()
                obj._deserialize(item)
                self._Skills.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchTasksRequest(AbstractModel):
    r"""ListAIWorkbenchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每页数量</p>
        :type PerPage: int
        :param _PageNo: <p>页码</p>
        :type PageNo: int
        :param _AgentId: <p>按 Agent 筛选</p>
        :type AgentId: str
        :param _TriggerType: <p>按触发类型筛选</p>
        :type TriggerType: str
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        :param _TaskIds: <p>任务 ID 列表筛选</p>
        :type TaskIds: list of str
        :param _Enabled: <p>是否启用筛选</p>
        :type Enabled: bool
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._TriggerType = None
        self._Keyword = None
        self._TaskIds = None
        self._Enabled = None

    @property
    def PerPage(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>按 Agent 筛选</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def TriggerType(self):
        r"""<p>按触发类型筛选</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TaskIds(self):
        r"""<p>任务 ID 列表筛选</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Enabled(self):
        r"""<p>是否启用筛选</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._TriggerType = params.get("TriggerType")
        self._Keyword = params.get("Keyword")
        self._TaskIds = params.get("TaskIds")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchTasksResponse(AbstractModel):
    r"""ListAIWorkbenchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: <p>任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of TaskInfo
        :param _PageResult: <p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""<p>任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def PageResult(self):
        r"""<p>分页结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class MCPInfo(AbstractModel):
    r"""MCP 实体

    """

    def __init__(self):
        r"""
        :param _MCPId: <p>mcp的ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCPId: str
        :param _Name: <p>MCP 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>MCP 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Url: <p>MCP URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Transport: <p>传输协议: sse / streamable_http / stdio</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Transport: str
        :param _AuthType: <p>认证类型: none / bearer / basic / api_key</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _AuthSecret: <p>认证密钥(响应时脱敏)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthSecret: str
        :param _Timeout: <p>超时时间(秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _RetryCount: <p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryCount: int
        :param _Headers: <p>请求头 JSON</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: str
        :param _Enabled: <p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._MCPId = None
        self._Name = None
        self._Description = None
        self._Url = None
        self._Transport = None
        self._AuthType = None
        self._AuthSecret = None
        self._Timeout = None
        self._RetryCount = None
        self._Headers = None
        self._Enabled = None

    @property
    def MCPId(self):
        r"""<p>mcp的ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MCPId

    @MCPId.setter
    def MCPId(self, MCPId):
        self._MCPId = MCPId

    @property
    def Name(self):
        r"""<p>MCP 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>MCP 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Url(self):
        r"""<p>MCP URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Transport(self):
        r"""<p>传输协议: sse / streamable_http / stdio</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def AuthType(self):
        r"""<p>认证类型: none / bearer / basic / api_key</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AuthSecret(self):
        r"""<p>认证密钥(响应时脱敏)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AuthSecret

    @AuthSecret.setter
    def AuthSecret(self, AuthSecret):
        self._AuthSecret = AuthSecret

    @property
    def Timeout(self):
        r"""<p>超时时间(秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def RetryCount(self):
        r"""<p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def Headers(self):
        r"""<p>请求头 JSON</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._MCPId = params.get("MCPId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Url = params.get("Url")
        self._Transport = params.get("Transport")
        self._AuthType = params.get("AuthType")
        self._AuthSecret = params.get("AuthSecret")
        self._Timeout = params.get("Timeout")
        self._RetryCount = params.get("RetryCount")
        self._Headers = params.get("Headers")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageInfo(AbstractModel):
    r"""消息实体

    """

    def __init__(self):
        r"""
        :param _EntryId: <p>实体id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryId: str
        :param _SessionId: <p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _Role: <p>角色: user / assistant</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _Content: <p>消息内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Status: <p>状态</p>
        :type Status: str
        :param _ContentBlocks: <p>块内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentBlocks: list of ContentBlockInfo
        """
        self._EntryId = None
        self._SessionId = None
        self._Role = None
        self._Content = None
        self._Status = None
        self._ContentBlocks = None

    @property
    def EntryId(self):
        r"""<p>实体id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Role(self):
        r"""<p>角色: user / assistant</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""<p>消息内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Status(self):
        r"""<p>状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ContentBlocks(self):
        r"""<p>块内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ContentBlockInfo
        """
        return self._ContentBlocks

    @ContentBlocks.setter
    def ContentBlocks(self, ContentBlocks):
        self._ContentBlocks = ContentBlocks


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SessionId = params.get("SessionId")
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._Status = params.get("Status")
        if params.get("ContentBlocks") is not None:
            self._ContentBlocks = []
            for item in params.get("ContentBlocks"):
                obj = ContentBlockInfo()
                obj._deserialize(item)
                self._ContentBlocks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDispenseExternalRuleRequest(AbstractModel):
    r"""ModifyDispenseExternalRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _ExtNamespace: 云监控对外命名空间
        :type ExtNamespace: str
        :param _Producer: 转发目标消信息
        :type Producer: :class:`tencentcloud.monitor.v20230616.models.Producer`
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _DispenseRegions: 转发部署地域列表
        :type DispenseRegions: list of str
        :param _ExtMetrics: 云监控对外指标
        :type ExtMetrics: list of str
        :param _Period: 指标统计周期
        :type Period: list of int
        :param _DispenseConditions: 转发过滤信息
        :type DispenseConditions: list of DispenseCondition
        """
        self._Name = None
        self._ExtNamespace = None
        self._Producer = None
        self._RuleId = None
        self._DispenseRegions = None
        self._ExtMetrics = None
        self._Period = None
        self._DispenseConditions = None

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExtNamespace(self):
        r"""云监控对外命名空间
        :rtype: str
        """
        return self._ExtNamespace

    @ExtNamespace.setter
    def ExtNamespace(self, ExtNamespace):
        self._ExtNamespace = ExtNamespace

    @property
    def Producer(self):
        r"""转发目标消信息
        :rtype: :class:`tencentcloud.monitor.v20230616.models.Producer`
        """
        return self._Producer

    @Producer.setter
    def Producer(self, Producer):
        self._Producer = Producer

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def DispenseRegions(self):
        r"""转发部署地域列表
        :rtype: list of str
        """
        return self._DispenseRegions

    @DispenseRegions.setter
    def DispenseRegions(self, DispenseRegions):
        self._DispenseRegions = DispenseRegions

    @property
    def ExtMetrics(self):
        r"""云监控对外指标
        :rtype: list of str
        """
        return self._ExtMetrics

    @ExtMetrics.setter
    def ExtMetrics(self, ExtMetrics):
        self._ExtMetrics = ExtMetrics

    @property
    def Period(self):
        r"""指标统计周期
        :rtype: list of int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def DispenseConditions(self):
        r"""转发过滤信息
        :rtype: list of DispenseCondition
        """
        return self._DispenseConditions

    @DispenseConditions.setter
    def DispenseConditions(self, DispenseConditions):
        self._DispenseConditions = DispenseConditions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ExtNamespace = params.get("ExtNamespace")
        if params.get("Producer") is not None:
            self._Producer = Producer()
            self._Producer._deserialize(params.get("Producer"))
        self._RuleId = params.get("RuleId")
        self._DispenseRegions = params.get("DispenseRegions")
        self._ExtMetrics = params.get("ExtMetrics")
        self._Period = params.get("Period")
        if params.get("DispenseConditions") is not None:
            self._DispenseConditions = []
            for item in params.get("DispenseConditions"):
                obj = DispenseCondition()
                obj._deserialize(item)
                self._DispenseConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDispenseExternalRuleResponse(AbstractModel):
    r"""ModifyDispenseExternalRule返回参数结构体

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


class ModifyDispenseExternalRuleStatusRequest(AbstractModel):
    r"""ModifyDispenseExternalRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIdList: 规则id列表
        :type RuleIdList: list of int
        :param _Status: 状态
        :type Status: int
        """
        self._RuleIdList = None
        self._Status = None

    @property
    def RuleIdList(self):
        r"""规则id列表
        :rtype: list of int
        """
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleIdList = params.get("RuleIdList")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDispenseExternalRuleStatusResponse(AbstractModel):
    r"""ModifyDispenseExternalRuleStatus返回参数结构体

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


class ModifyNoticeContentTmplRequest(AbstractModel):
    r"""ModifyNoticeContentTmpl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplName: 模板名称
        :type TmplName: str
        :param _TmplContents: 模板内容
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _TmplID: 需要修改的模板ID
        :type TmplID: str
        """
        self._TmplName = None
        self._TmplContents = None
        self._TmplID = None

    @property
    def TmplName(self):
        r"""模板名称
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def TmplContents(self):
        r"""模板内容
        :rtype: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        """
        return self._TmplContents

    @TmplContents.setter
    def TmplContents(self, TmplContents):
        self._TmplContents = TmplContents

    @property
    def TmplID(self):
        r"""需要修改的模板ID
        :rtype: str
        """
        return self._TmplID

    @TmplID.setter
    def TmplID(self, TmplID):
        self._TmplID = TmplID


    def _deserialize(self, params):
        self._TmplName = params.get("TmplName")
        if params.get("TmplContents") is not None:
            self._TmplContents = NoticeContentTmplItem()
            self._TmplContents._deserialize(params.get("TmplContents"))
        self._TmplID = params.get("TmplID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNoticeContentTmplResponse(AbstractModel):
    r"""ModifyNoticeContentTmpl返回参数结构体

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


class NoticeContentTmpl(AbstractModel):
    r"""自定义通知内容模板

    """

    def __init__(self):
        r"""
        :param _TmplID: <p>自定义通知内容模板id，唯一id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplID: str
        :param _TmplName: <p>自定义通知内容模板名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplName: str
        :param _TmplContents: <p>通知内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _CreateTime: <p>Unix时间戳，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: <p>Unix时间戳，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _LastModifier: <p>最后修改人</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifier: str
        :param _Creator: <p>创建人</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _MonitorType: <p>监控类型</p>
        :type MonitorType: str
        :param _TmplLanguage: <p>模板语言 en/zh</p>
        :type TmplLanguage: str
        """
        self._TmplID = None
        self._TmplName = None
        self._TmplContents = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LastModifier = None
        self._Creator = None
        self._MonitorType = None
        self._TmplLanguage = None

    @property
    def TmplID(self):
        r"""<p>自定义通知内容模板id，唯一id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmplID

    @TmplID.setter
    def TmplID(self, TmplID):
        self._TmplID = TmplID

    @property
    def TmplName(self):
        r"""<p>自定义通知内容模板名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def TmplContents(self):
        r"""<p>通知内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        """
        return self._TmplContents

    @TmplContents.setter
    def TmplContents(self, TmplContents):
        self._TmplContents = TmplContents

    @property
    def CreateTime(self):
        r"""<p>Unix时间戳，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Unix时间戳，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastModifier(self):
        r"""<p>最后修改人</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastModifier

    @LastModifier.setter
    def LastModifier(self, LastModifier):
        self._LastModifier = LastModifier

    @property
    def Creator(self):
        r"""<p>创建人</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def MonitorType(self):
        r"""<p>监控类型</p>
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def TmplLanguage(self):
        r"""<p>模板语言 en/zh</p>
        :rtype: str
        """
        return self._TmplLanguage

    @TmplLanguage.setter
    def TmplLanguage(self, TmplLanguage):
        self._TmplLanguage = TmplLanguage


    def _deserialize(self, params):
        self._TmplID = params.get("TmplID")
        self._TmplName = params.get("TmplName")
        if params.get("TmplContents") is not None:
            self._TmplContents = NoticeContentTmplItem()
            self._TmplContents._deserialize(params.get("TmplContents"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastModifier = params.get("LastModifier")
        self._Creator = params.get("Creator")
        self._MonitorType = params.get("MonitorType")
        self._TmplLanguage = params.get("TmplLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContentTmplBindPolicyCount(AbstractModel):
    r"""通知内容模板绑定告警策略数量

    """

    def __init__(self):
        r"""
        :param _NoticeContentTmplID: 通知内容模板ID
        :type NoticeContentTmplID: str
        :param _BindCount: 绑定告警策略数量
        :type BindCount: int
        """
        self._NoticeContentTmplID = None
        self._BindCount = None

    @property
    def NoticeContentTmplID(self):
        r"""通知内容模板ID
        :rtype: str
        """
        return self._NoticeContentTmplID

    @NoticeContentTmplID.setter
    def NoticeContentTmplID(self, NoticeContentTmplID):
        self._NoticeContentTmplID = NoticeContentTmplID

    @property
    def BindCount(self):
        r"""绑定告警策略数量
        :rtype: int
        """
        return self._BindCount

    @BindCount.setter
    def BindCount(self, BindCount):
        self._BindCount = BindCount


    def _deserialize(self, params):
        self._NoticeContentTmplID = params.get("NoticeContentTmplID")
        self._BindCount = params.get("BindCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContentTmplItem(AbstractModel):
    r"""内容通知模板元素

    """

    def __init__(self):
        r"""
        :param _QCloudYehe: <p>官网通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type QCloudYehe: list of QCloudYeheNoticeTmplMatcher
        :param _WeWorkRobot: <p>企业微信机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WeWorkRobot: list of WeWorkRobotNoticeTmplMatcher
        :param _DingDingRobot: <p>钉钉机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DingDingRobot: list of DingDingRobotNoticeTmplMatcher
        :param _FeiShuRobot: <p>飞书机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FeiShuRobot: list of FeiShuRobotNoticeTmplMatcher
        :param _Webhook: <p>自定义Webhook通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Webhook: list of WebhookNoticeTmplMatcher
        :param _TeamsRobot: <p>Teams机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TeamsRobot: list of TeamsRobotNoticeTmplMatcher
        :param _PagerDutyRobot: <p>PagerDutyRobot机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PagerDutyRobot: list of PagerDutyRobotNoticeTmplMatcher
        :param _GoogleChatRobot: <p>GoogleChat</p>
        :type GoogleChatRobot: list of GoogleChatRobotNoticeTmplMatcher
        :param _SlackRobot: <p>Slack</p>
        :type SlackRobot: list of SlackRobotNoticeTmplMatcher
        :param _TeamsWorkflowRobot: <p>Teams 工作流渠道</p>
        :type TeamsWorkflowRobot: list of TeamsWorkflowRobotNoticeTmplMatcher
        """
        self._QCloudYehe = None
        self._WeWorkRobot = None
        self._DingDingRobot = None
        self._FeiShuRobot = None
        self._Webhook = None
        self._TeamsRobot = None
        self._PagerDutyRobot = None
        self._GoogleChatRobot = None
        self._SlackRobot = None
        self._TeamsWorkflowRobot = None

    @property
    def QCloudYehe(self):
        r"""<p>官网通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QCloudYeheNoticeTmplMatcher
        """
        return self._QCloudYehe

    @QCloudYehe.setter
    def QCloudYehe(self, QCloudYehe):
        self._QCloudYehe = QCloudYehe

    @property
    def WeWorkRobot(self):
        r"""<p>企业微信机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WeWorkRobotNoticeTmplMatcher
        """
        return self._WeWorkRobot

    @WeWorkRobot.setter
    def WeWorkRobot(self, WeWorkRobot):
        self._WeWorkRobot = WeWorkRobot

    @property
    def DingDingRobot(self):
        r"""<p>钉钉机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DingDingRobotNoticeTmplMatcher
        """
        return self._DingDingRobot

    @DingDingRobot.setter
    def DingDingRobot(self, DingDingRobot):
        self._DingDingRobot = DingDingRobot

    @property
    def FeiShuRobot(self):
        r"""<p>飞书机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FeiShuRobotNoticeTmplMatcher
        """
        return self._FeiShuRobot

    @FeiShuRobot.setter
    def FeiShuRobot(self, FeiShuRobot):
        self._FeiShuRobot = FeiShuRobot

    @property
    def Webhook(self):
        r"""<p>自定义Webhook通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebhookNoticeTmplMatcher
        """
        return self._Webhook

    @Webhook.setter
    def Webhook(self, Webhook):
        self._Webhook = Webhook

    @property
    def TeamsRobot(self):
        r"""<p>Teams机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TeamsRobotNoticeTmplMatcher
        """
        return self._TeamsRobot

    @TeamsRobot.setter
    def TeamsRobot(self, TeamsRobot):
        self._TeamsRobot = TeamsRobot

    @property
    def PagerDutyRobot(self):
        r"""<p>PagerDutyRobot机器人通知渠道配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PagerDutyRobotNoticeTmplMatcher
        """
        return self._PagerDutyRobot

    @PagerDutyRobot.setter
    def PagerDutyRobot(self, PagerDutyRobot):
        self._PagerDutyRobot = PagerDutyRobot

    @property
    def GoogleChatRobot(self):
        r"""<p>GoogleChat</p>
        :rtype: list of GoogleChatRobotNoticeTmplMatcher
        """
        return self._GoogleChatRobot

    @GoogleChatRobot.setter
    def GoogleChatRobot(self, GoogleChatRobot):
        self._GoogleChatRobot = GoogleChatRobot

    @property
    def SlackRobot(self):
        r"""<p>Slack</p>
        :rtype: list of SlackRobotNoticeTmplMatcher
        """
        return self._SlackRobot

    @SlackRobot.setter
    def SlackRobot(self, SlackRobot):
        self._SlackRobot = SlackRobot

    @property
    def TeamsWorkflowRobot(self):
        r"""<p>Teams 工作流渠道</p>
        :rtype: list of TeamsWorkflowRobotNoticeTmplMatcher
        """
        return self._TeamsWorkflowRobot

    @TeamsWorkflowRobot.setter
    def TeamsWorkflowRobot(self, TeamsWorkflowRobot):
        self._TeamsWorkflowRobot = TeamsWorkflowRobot


    def _deserialize(self, params):
        if params.get("QCloudYehe") is not None:
            self._QCloudYehe = []
            for item in params.get("QCloudYehe"):
                obj = QCloudYeheNoticeTmplMatcher()
                obj._deserialize(item)
                self._QCloudYehe.append(obj)
        if params.get("WeWorkRobot") is not None:
            self._WeWorkRobot = []
            for item in params.get("WeWorkRobot"):
                obj = WeWorkRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._WeWorkRobot.append(obj)
        if params.get("DingDingRobot") is not None:
            self._DingDingRobot = []
            for item in params.get("DingDingRobot"):
                obj = DingDingRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._DingDingRobot.append(obj)
        if params.get("FeiShuRobot") is not None:
            self._FeiShuRobot = []
            for item in params.get("FeiShuRobot"):
                obj = FeiShuRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._FeiShuRobot.append(obj)
        if params.get("Webhook") is not None:
            self._Webhook = []
            for item in params.get("Webhook"):
                obj = WebhookNoticeTmplMatcher()
                obj._deserialize(item)
                self._Webhook.append(obj)
        if params.get("TeamsRobot") is not None:
            self._TeamsRobot = []
            for item in params.get("TeamsRobot"):
                obj = TeamsRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._TeamsRobot.append(obj)
        if params.get("PagerDutyRobot") is not None:
            self._PagerDutyRobot = []
            for item in params.get("PagerDutyRobot"):
                obj = PagerDutyRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._PagerDutyRobot.append(obj)
        if params.get("GoogleChatRobot") is not None:
            self._GoogleChatRobot = []
            for item in params.get("GoogleChatRobot"):
                obj = GoogleChatRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._GoogleChatRobot.append(obj)
        if params.get("SlackRobot") is not None:
            self._SlackRobot = []
            for item in params.get("SlackRobot"):
                obj = SlackRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._SlackRobot.append(obj)
        if params.get("TeamsWorkflowRobot") is not None:
            self._TeamsWorkflowRobot = []
            for item in params.get("TeamsWorkflowRobot"):
                obj = TeamsWorkflowRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._TeamsWorkflowRobot.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyRelatedNotice(AbstractModel):
    r"""通知历史中关联的通知模板信息

    """

    def __init__(self):
        r"""
        :param _NoticeId: 通知模板ID
        :type NoticeId: str
        :param _NoticeName: 通知模板的名称
        :type NoticeName: str
        """
        self._NoticeId = None
        self._NoticeName = None

    @property
    def NoticeId(self):
        r"""通知模板ID
        :rtype: str
        """
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def NoticeName(self):
        r"""通知模板的名称
        :rtype: str
        """
        return self._NoticeName

    @NoticeName.setter
    def NoticeName(self, NoticeName):
        self._NoticeName = NoticeName


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._NoticeName = params.get("NoticeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoParams(AbstractModel):
    r"""分页请求参数

    """

    def __init__(self):
        r"""
        :param _PerPage: 每个分页的数量是多少
注意：此字段可能返回 null，表示取不到有效值。
        :type PerPage: int
        :param _PageNo: 第几个分页，从1开始
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: str
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""每个分页的数量是多少
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""第几个分页，从1开始
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoResult(AbstractModel):
    r"""分页结果参数

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总共有多少数据
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPage: 总共有多少个分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPage: int
        :param _CurrentPageNo: 当前的分页号
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentPageNo: int
        :param _IsEnd: 【已弃用】是否遍历到末尾
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnd: bool
        :param _End: 是否遍历到末尾
        :type End: bool
        """
        self._TotalCount = None
        self._TotalPage = None
        self._CurrentPageNo = None
        self._IsEnd = None
        self._End = None

    @property
    def TotalCount(self):
        r"""总共有多少数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPage(self):
        r"""总共有多少个分页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def CurrentPageNo(self):
        r"""当前的分页号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentPageNo

    @CurrentPageNo.setter
    def CurrentPageNo(self, CurrentPageNo):
        self._CurrentPageNo = CurrentPageNo

    @property
    def IsEnd(self):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        r"""【已弃用】是否遍历到末尾
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        self._IsEnd = IsEnd

    @property
    def End(self):
        r"""是否遍历到末尾
        :rtype: bool
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPage = params.get("TotalPage")
        self._CurrentPageNo = params.get("CurrentPageNo")
        self._IsEnd = params.get("IsEnd")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNumParams(AbstractModel):
    r"""按第几页进行分页的入参

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>每个分页的数量</p>
        :type PerPage: int
        :param _PageNo: <p>第几个分页，从1开始</p>
        :type PageNo: int
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""<p>每个分页的数量</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>第几个分页，从1开始</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNumResult(AbstractModel):
    r"""分页结果参数

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总共有多少数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPage: <p>总共有多少个分页</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPage: int
        :param _CurrentPageNo: <p>当前的分页号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentPageNo: int
        """
        self._TotalCount = None
        self._TotalPage = None
        self._CurrentPageNo = None

    @property
    def TotalCount(self):
        r"""<p>总共有多少数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPage(self):
        r"""<p>总共有多少个分页</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def CurrentPageNo(self):
        r"""<p>当前的分页号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentPageNo

    @CurrentPageNo.setter
    def CurrentPageNo(self, CurrentPageNo):
        self._CurrentPageNo = CurrentPageNo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPage = params.get("TotalPage")
        self._CurrentPageNo = params.get("CurrentPageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmpl(AbstractModel):
    r"""告警通知自定义PagerDutyRobot内容模板

    """

    def __init__(self):
        r"""
        :param _Body: 请求体模板 仅支持json
        :type Body: str
        :param _Headers: 请求头 暂时未支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of PagerDutyRobotNoticeTmplHeader
        :param _TitleTmpl: 标题模板
        :type TitleTmpl: str
        """
        self._Body = None
        self._Headers = None
        self._TitleTmpl = None

    @property
    def Body(self):
        r"""请求体模板 仅支持json
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        r"""请求头 暂时未支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PagerDutyRobotNoticeTmplHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def TitleTmpl(self):
        r"""标题模板
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._Body = params.get("Body")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = PagerDutyRobotNoticeTmplHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmplHeader(AbstractModel):
    r"""告警通知自定义PagerDutyRobot模板中的请求体头部描述

    """

    def __init__(self):
        r"""
        :param _Key: http请求中header的key
        :type Key: str
        :param _Values: http请求中header的value
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""http请求中header的key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""http请求中header的value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmplMatcher(AbstractModel):
    r"""告警通知自定义PagerDutyRobot的通知内容模板匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 自定义PagerDutyRobot内容模板
        :type Template: :class:`tencentcloud.monitor.v20230616.models.PagerDutyRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""自定义PagerDutyRobot内容模板
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PagerDutyRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = PagerDutyRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Producer(AbstractModel):
    r"""转发目标对象信息

    """

    def __init__(self):
        r"""
        :param _ProtocolType: 转发协议类型，0-stormRetPb, 1-tcbDispensePb, 2-stormRetJson, 3-ADPPb(废弃)，4-中台pb
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: int
        :param _Type: 目标类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Brokers: 转发kafka地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Brokers: str
        :param _Topic: 转发kafka topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _Merge: 是否合并指标,默认是1，合并
        :type Merge: int
        :param _GlobalTags: 全局维度组
        :type GlobalTags: list of DispenseGlobalTag
        :param _DefaultTags: 默认维度组，只提供维度即可
        :type DefaultTags: list of str
        :param _Username: Kafka用户名
        :type Username: str
        :param _Password: Kafka密码
        :type Password: str
        """
        self._ProtocolType = None
        self._Type = None
        self._Brokers = None
        self._Topic = None
        self._Merge = None
        self._GlobalTags = None
        self._DefaultTags = None
        self._Username = None
        self._Password = None

    @property
    def ProtocolType(self):
        r"""转发协议类型，0-stormRetPb, 1-tcbDispensePb, 2-stormRetJson, 3-ADPPb(废弃)，4-中台pb
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Type(self):
        r"""目标类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brokers(self):
        r"""转发kafka地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Brokers

    @Brokers.setter
    def Brokers(self, Brokers):
        self._Brokers = Brokers

    @property
    def Topic(self):
        r"""转发kafka topic
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Merge(self):
        r"""是否合并指标,默认是1，合并
        :rtype: int
        """
        return self._Merge

    @Merge.setter
    def Merge(self, Merge):
        self._Merge = Merge

    @property
    def GlobalTags(self):
        r"""全局维度组
        :rtype: list of DispenseGlobalTag
        """
        return self._GlobalTags

    @GlobalTags.setter
    def GlobalTags(self, GlobalTags):
        self._GlobalTags = GlobalTags

    @property
    def DefaultTags(self):
        r"""默认维度组，只提供维度即可
        :rtype: list of str
        """
        return self._DefaultTags

    @DefaultTags.setter
    def DefaultTags(self, DefaultTags):
        self._DefaultTags = DefaultTags

    @property
    def Username(self):
        r"""Kafka用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Kafka密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._ProtocolType = params.get("ProtocolType")
        self._Type = params.get("Type")
        self._Brokers = params.get("Brokers")
        self._Topic = params.get("Topic")
        self._Merge = params.get("Merge")
        if params.get("GlobalTags") is not None:
            self._GlobalTags = []
            for item in params.get("GlobalTags"):
                obj = DispenseGlobalTag()
                obj._deserialize(item)
                self._GlobalTags.append(obj)
        self._DefaultTags = params.get("DefaultTags")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmpl(AbstractModel):
    r"""官网通知内容模板

    """

    def __init__(self):
        r"""
        :param _Email: 邮件通知渠道
        :type Email: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _QYWX: 企业微信通知渠道
        :type QYWX: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _SMS: 短信通知渠道
        :type SMS: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _Voice: 语音通知渠道
        :type Voice: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _WeChat: 微信通知渠道
        :type WeChat: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheWeChatNoticeTmplItem`
        :param _Site: 站内信通知渠道
        :type Site: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _Andon: 安灯通知渠道
        :type Andon: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        self._Email = None
        self._QYWX = None
        self._SMS = None
        self._Voice = None
        self._WeChat = None
        self._Site = None
        self._Andon = None

    @property
    def Email(self):
        r"""邮件通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def QYWX(self):
        r"""企业微信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._QYWX

    @QYWX.setter
    def QYWX(self, QYWX):
        self._QYWX = QYWX

    @property
    def SMS(self):
        r"""短信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._SMS

    @SMS.setter
    def SMS(self, SMS):
        self._SMS = SMS

    @property
    def Voice(self):
        r"""语音通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def WeChat(self):
        r"""微信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheWeChatNoticeTmplItem`
        """
        return self._WeChat

    @WeChat.setter
    def WeChat(self, WeChat):
        self._WeChat = WeChat

    @property
    def Site(self):
        r"""站内信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def Andon(self):
        r"""安灯通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Andon

    @Andon.setter
    def Andon(self, Andon):
        self._Andon = Andon


    def _deserialize(self, params):
        if params.get("Email") is not None:
            self._Email = QCloudYeheNoticeTmplItem()
            self._Email._deserialize(params.get("Email"))
        if params.get("QYWX") is not None:
            self._QYWX = QCloudYeheNoticeTmplItem()
            self._QYWX._deserialize(params.get("QYWX"))
        if params.get("SMS") is not None:
            self._SMS = QCloudYeheNoticeTmplItem()
            self._SMS._deserialize(params.get("SMS"))
        if params.get("Voice") is not None:
            self._Voice = QCloudYeheNoticeTmplItem()
            self._Voice._deserialize(params.get("Voice"))
        if params.get("WeChat") is not None:
            self._WeChat = QCloudYeheWeChatNoticeTmplItem()
            self._WeChat._deserialize(params.get("WeChat"))
        if params.get("Site") is not None:
            self._Site = QCloudYeheNoticeTmplItem()
            self._Site._deserialize(params.get("Site"))
        if params.get("Andon") is not None:
            self._Andon = QCloudYeheNoticeTmplItem()
            self._Andon._deserialize(params.get("Andon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmplItem(AbstractModel):
    r"""官网通知内容模板元素

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        :param _TitleTmpl: 标题
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""标题
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmplMatcher(AbstractModel):
    r"""官网内容通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = QCloudYeheNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheWeChatNoticeTmplItem(AbstractModel):
    r"""官网通知内容模板元素

    """

    def __init__(self):
        r"""
        :param _AlarmContentTmpl: 告警内容模板
        :type AlarmContentTmpl: str
        :param _AlarmObjectTmpl: 告警对象模板
        :type AlarmObjectTmpl: str
        :param _AlarmRegionTmpl: 告警地域模板
        :type AlarmRegionTmpl: str
        :param _AlarmTimeTmpl: 告警时间模板
        :type AlarmTimeTmpl: str
        """
        self._AlarmContentTmpl = None
        self._AlarmObjectTmpl = None
        self._AlarmRegionTmpl = None
        self._AlarmTimeTmpl = None

    @property
    def AlarmContentTmpl(self):
        r"""告警内容模板
        :rtype: str
        """
        return self._AlarmContentTmpl

    @AlarmContentTmpl.setter
    def AlarmContentTmpl(self, AlarmContentTmpl):
        self._AlarmContentTmpl = AlarmContentTmpl

    @property
    def AlarmObjectTmpl(self):
        r"""告警对象模板
        :rtype: str
        """
        return self._AlarmObjectTmpl

    @AlarmObjectTmpl.setter
    def AlarmObjectTmpl(self, AlarmObjectTmpl):
        self._AlarmObjectTmpl = AlarmObjectTmpl

    @property
    def AlarmRegionTmpl(self):
        r"""告警地域模板
        :rtype: str
        """
        return self._AlarmRegionTmpl

    @AlarmRegionTmpl.setter
    def AlarmRegionTmpl(self, AlarmRegionTmpl):
        self._AlarmRegionTmpl = AlarmRegionTmpl

    @property
    def AlarmTimeTmpl(self):
        r"""告警时间模板
        :rtype: str
        """
        return self._AlarmTimeTmpl

    @AlarmTimeTmpl.setter
    def AlarmTimeTmpl(self, AlarmTimeTmpl):
        self._AlarmTimeTmpl = AlarmTimeTmpl


    def _deserialize(self, params):
        self._AlarmContentTmpl = params.get("AlarmContentTmpl")
        self._AlarmObjectTmpl = params.get("AlarmObjectTmpl")
        self._AlarmRegionTmpl = params.get("AlarmRegionTmpl")
        self._AlarmTimeTmpl = params.get("AlarmTimeTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInstance(AbstractModel):
    r"""资源实例

    """

    def __init__(self):
        r"""
        :param _Id: <p>实例 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Service: <p>服务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _Region: <p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _IsReady: <p>是否就绪</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReady: bool
        """
        self._Id = None
        self._Service = None
        self._Region = None
        self._IsReady = None

    @property
    def Id(self):
        r"""<p>实例 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Service(self):
        r"""<p>服务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Region(self):
        r"""<p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IsReady(self):
        r"""<p>是否就绪</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsReady

    @IsReady.setter
    def IsReady(self, IsReady):
        self._IsReady = IsReady


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Service = params.get("Service")
        self._Region = params.get("Region")
        self._IsReady = params.get("IsReady")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceMapInfo(AbstractModel):
    r"""资源地图实体

    """

    def __init__(self):
        r"""
        :param _ResourceMapId: <p>资源地图 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMapId: str
        :param _Name: <p>资源地图名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>资源地图描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _InstanceCount: <p>总实例数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        """
        self._ResourceMapId = None
        self._Name = None
        self._Description = None
        self._InstanceCount = None

    @property
    def ResourceMapId(self):
        r"""<p>资源地图 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def Name(self):
        r"""<p>资源地图名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>资源地图描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceCount(self):
        r"""<p>总实例数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._ResourceMapId = params.get("ResourceMapId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RobotNoticeTitleColor(AbstractModel):
    r"""告警通知内容模版自定义标题颜色

    """

    def __init__(self):
        r"""
        :param _Default: <p>通知内容模版自定义标题颜色默认颜色</p>
        :type Default: str
        :param _Rules: <p>通知内容模版自定义标题颜色规则，label 匹配设置颜色</p>
        :type Rules: list of RobotNoticeTitleColorRules
        """
        self._Default = None
        self._Rules = None

    @property
    def Default(self):
        r"""<p>通知内容模版自定义标题颜色默认颜色</p>
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Rules(self):
        r"""<p>通知内容模版自定义标题颜色规则，label 匹配设置颜色</p>
        :rtype: list of RobotNoticeTitleColorRules
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Default = params.get("Default")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RobotNoticeTitleColorRules()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RobotNoticeTitleColorRules(AbstractModel):
    r"""告警通知内容模版自定义标题颜色 key-value 匹配规则

    """

    def __init__(self):
        r"""
        :param _Key: <p>通知内容模版自定义颜色 Label 匹配的 Key</p>
        :type Key: str
        :param _Value: <p>通知内容模版自定义颜色 Label 匹配的 Value</p>
        :type Value: str
        :param _Color: <p>通知内容模版自定义颜色</p>
        :type Color: str
        """
        self._Key = None
        self._Value = None
        self._Color = None

    @property
    def Key(self):
        r"""<p>通知内容模版自定义颜色 Label 匹配的 Key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>通知内容模版自定义颜色 Label 匹配的 Value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Color(self):
        r"""<p>通知内容模版自定义颜色</p>
        :rtype: str
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    r"""转发规则

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: int
        :param _Name: 规则名称
        :type Name: str
        :param _ExtNamespace: 对外namespace
        :type ExtNamespace: str
        :param _ExtMetric: 对外指标列表
        :type ExtMetric: list of ExtMetric
        :param _Producer: 输出信息
        :type Producer: :class:`tencentcloud.monitor.v20230616.models.Producer`
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _Status: 规则触发状态
        :type Status: int
        :param _Period: 指标粒度周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: list of int
        :param _DispenseConditions: 转发过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type DispenseConditions: list of DispenseCondition
        :param _DispenseRegions: 转发地域列表
        :type DispenseRegions: list of str
        """
        self._RuleId = None
        self._Name = None
        self._ExtNamespace = None
        self._ExtMetric = None
        self._Producer = None
        self._UpdateTime = None
        self._Status = None
        self._Period = None
        self._DispenseConditions = None
        self._DispenseRegions = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExtNamespace(self):
        r"""对外namespace
        :rtype: str
        """
        return self._ExtNamespace

    @ExtNamespace.setter
    def ExtNamespace(self, ExtNamespace):
        self._ExtNamespace = ExtNamespace

    @property
    def ExtMetric(self):
        r"""对外指标列表
        :rtype: list of ExtMetric
        """
        return self._ExtMetric

    @ExtMetric.setter
    def ExtMetric(self, ExtMetric):
        self._ExtMetric = ExtMetric

    @property
    def Producer(self):
        r"""输出信息
        :rtype: :class:`tencentcloud.monitor.v20230616.models.Producer`
        """
        return self._Producer

    @Producer.setter
    def Producer(self, Producer):
        self._Producer = Producer

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""规则触发状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Period(self):
        r"""指标粒度周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def DispenseConditions(self):
        r"""转发过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DispenseCondition
        """
        return self._DispenseConditions

    @DispenseConditions.setter
    def DispenseConditions(self, DispenseConditions):
        self._DispenseConditions = DispenseConditions

    @property
    def DispenseRegions(self):
        r"""转发地域列表
        :rtype: list of str
        """
        return self._DispenseRegions

    @DispenseRegions.setter
    def DispenseRegions(self, DispenseRegions):
        self._DispenseRegions = DispenseRegions


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._ExtNamespace = params.get("ExtNamespace")
        if params.get("ExtMetric") is not None:
            self._ExtMetric = []
            for item in params.get("ExtMetric"):
                obj = ExtMetric()
                obj._deserialize(item)
                self._ExtMetric.append(obj)
        if params.get("Producer") is not None:
            self._Producer = Producer()
            self._Producer._deserialize(params.get("Producer"))
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Period = params.get("Period")
        if params.get("DispenseConditions") is not None:
            self._DispenseConditions = []
            for item in params.get("DispenseConditions"):
                obj = DispenseCondition()
                obj._deserialize(item)
                self._DispenseConditions.append(obj)
        self._DispenseRegions = params.get("DispenseRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    r"""会话实体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _AgentId: <p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _Title: <p>会话标题</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Status: <p>状态: active / archived / deleted</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskId: <p>如果该会话由任务触发，则携带触发其会话的任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._SessionId = None
        self._AgentId = None
        self._Title = None
        self._Status = None
        self._TaskId = None

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Title(self):
        r"""<p>会话标题</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        r"""<p>状态: active / archived / deleted</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""<p>如果该会话由任务触发，则携带触发其会话的任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillInfo(AbstractModel):
    r"""技能实体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>技能 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillId: str
        :param _Name: <p>技能名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>技能描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Enabled: <p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._SkillId = None
        self._Name = None
        self._Description = None
        self._Enabled = None

    @property
    def SkillId(self):
        r"""<p>技能 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def Name(self):
        r"""<p>技能名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>技能描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlackRobotNoticeTmpl(AbstractModel):
    r"""企业微信机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: <p>内容模板</p>
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""<p>内容模板</p>
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlackRobotNoticeTmplMatcher(AbstractModel):
    r"""企业微信机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: <p>匹配状态 Invalid;<br>Trigger 告警触发; Recovery 告警恢复</p>
        :type MatchingStatus: list of str
        :param _Template: <p>模板配置</p>
        :type Template: :class:`tencentcloud.monitor.v20230616.models.SlackRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""<p>匹配状态 Invalid;<br>Trigger 告警触发; Recovery 告警恢复</p>
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""<p>模板配置</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.SlackRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = SlackRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
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
        :param _Key: 标签key
        :type Key: str
        :param _Value: 标签value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签value
        :rtype: str
        """
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
        


class TaskInfo(AbstractModel):
    r"""任务实体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Name: <p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>任务描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _AgentId: <p>关联 Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _PromptTemplate: <p>提示词模板</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PromptTemplate: str
        :param _OutputFormat: <p>输出格式: markdown / json</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param _TriggerType: <p>触发类型: manual / cron / webhook</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param _CronExpr: <p>Cron 表达式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CronExpr: str
        :param _CronTimezone: <p>Cron 时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CronTimezone: str
        :param _SkillIds: <p>关联技能 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillIds: list of str
        :param _McpEndpointIds: <p>关联 MCP 端点 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type McpEndpointIds: list of str
        :param _TimeoutSec: <p>超时时间(秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutSec: int
        :param _RetryCount: <p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryCount: int
        :param _NotifyIds: <p>通知id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyIds: list of str
        :param _Enabled: <p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._TaskId = None
        self._Name = None
        self._Description = None
        self._AgentId = None
        self._PromptTemplate = None
        self._OutputFormat = None
        self._TriggerType = None
        self._CronExpr = None
        self._CronTimezone = None
        self._SkillIds = None
        self._McpEndpointIds = None
        self._TimeoutSec = None
        self._RetryCount = None
        self._NotifyIds = None
        self._Enabled = None

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        r"""<p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>任务描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AgentId(self):
        r"""<p>关联 Agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def PromptTemplate(self):
        r"""<p>提示词模板</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PromptTemplate

    @PromptTemplate.setter
    def PromptTemplate(self, PromptTemplate):
        self._PromptTemplate = PromptTemplate

    @property
    def OutputFormat(self):
        r"""<p>输出格式: markdown / json</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def TriggerType(self):
        r"""<p>触发类型: manual / cron / webhook</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def CronExpr(self):
        r"""<p>Cron 表达式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CronExpr

    @CronExpr.setter
    def CronExpr(self, CronExpr):
        self._CronExpr = CronExpr

    @property
    def CronTimezone(self):
        r"""<p>Cron 时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CronTimezone

    @CronTimezone.setter
    def CronTimezone(self, CronTimezone):
        self._CronTimezone = CronTimezone

    @property
    def SkillIds(self):
        r"""<p>关联技能 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def McpEndpointIds(self):
        r"""<p>关联 MCP 端点 ID 列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._McpEndpointIds

    @McpEndpointIds.setter
    def McpEndpointIds(self, McpEndpointIds):
        self._McpEndpointIds = McpEndpointIds

    @property
    def TimeoutSec(self):
        r"""<p>超时时间(秒)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeoutSec

    @TimeoutSec.setter
    def TimeoutSec(self, TimeoutSec):
        self._TimeoutSec = TimeoutSec

    @property
    def RetryCount(self):
        r"""<p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def NotifyIds(self):
        r"""<p>通知id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NotifyIds

    @NotifyIds.setter
    def NotifyIds(self, NotifyIds):
        self._NotifyIds = NotifyIds

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AgentId = params.get("AgentId")
        self._PromptTemplate = params.get("PromptTemplate")
        self._OutputFormat = params.get("OutputFormat")
        self._TriggerType = params.get("TriggerType")
        self._CronExpr = params.get("CronExpr")
        self._CronTimezone = params.get("CronTimezone")
        self._SkillIds = params.get("SkillIds")
        self._McpEndpointIds = params.get("McpEndpointIds")
        self._TimeoutSec = params.get("TimeoutSec")
        self._RetryCount = params.get("RetryCount")
        self._NotifyIds = params.get("NotifyIds")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsRobotNoticeTmpl(AbstractModel):
    r"""企业微信机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsRobotNoticeTmplMatcher(AbstractModel):
    r"""企业微信机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.TeamsRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TeamsRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = TeamsRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsWorkflowRobotNoticeTmpl(AbstractModel):
    r"""Microsoft Teams 工作流内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: <p>内容模板</p>
        :type ContentTmpl: str
        :param _Version: <p>区分 TeamsWorkflow 是自定义内容还是自定义 POST BODY</p><p>枚举值：</p><ul><li>WorkflowText： 自定义内容</li><li>WorkflowJson： 自定义 POST BODY</li></ul>
        :type Version: str
        :param _TitleTmpl: <p>标题模版</p>
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._Version = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""<p>内容模板</p>
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def Version(self):
        r"""<p>区分 TeamsWorkflow 是自定义内容还是自定义 POST BODY</p><p>枚举值：</p><ul><li>WorkflowText： 自定义内容</li><li>WorkflowJson： 自定义 POST BODY</li></ul>
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def TitleTmpl(self):
        r"""<p>标题模版</p>
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._Version = params.get("Version")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsWorkflowRobotNoticeTmplMatcher(AbstractModel):
    r"""Microsoft Teams 工作流通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: <p>匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复</p><p>枚举值：</p><ul><li>Trigger： 告警触发</li><li>Recovery： 告警恢复</li></ul>
        :type MatchingStatus: list of str
        :param _Template: <p>模板配置</p>
        :type Template: :class:`tencentcloud.monitor.v20230616.models.TeamsWorkflowRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""<p>匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复</p><p>枚举值：</p><ul><li>Trigger： 告警触发</li><li>Recovery： 告警恢复</li></ul>
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""<p>模板配置</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TeamsWorkflowRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = TeamsWorkflowRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAIWorkbenchSREDigitalTwinTaskRequest(AbstractModel):
    r"""TriggerAIWorkbenchSREDigitalTwinTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 数字分身任务ID
        :type TaskID: int
        """
        self._TaskID = None

    @property
    def TaskID(self):
        r"""数字分身任务ID
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAIWorkbenchSREDigitalTwinTaskResponse(AbstractModel):
    r"""TriggerAIWorkbenchSREDigitalTwinTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JSONStrPaths: Json序列化路径
        :type JSONStrPaths: list of str
        :param _Data: 数字分身任务信息
        :type Data: :class:`tencentcloud.monitor.v20230616.models.TriggerDigitalTwinTaskResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JSONStrPaths = None
        self._Data = None
        self._RequestId = None

    @property
    def JSONStrPaths(self):
        r"""Json序列化路径
        :rtype: list of str
        """
        return self._JSONStrPaths

    @JSONStrPaths.setter
    def JSONStrPaths(self, JSONStrPaths):
        self._JSONStrPaths = JSONStrPaths

    @property
    def Data(self):
        r"""数字分身任务信息
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TriggerDigitalTwinTaskResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JSONStrPaths = params.get("JSONStrPaths")
        if params.get("Data") is not None:
            self._Data = TriggerDigitalTwinTaskResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class TriggerAIWorkbenchTaskRequest(AbstractModel):
    r"""TriggerAIWorkbenchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务 ID</p>
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAIWorkbenchTaskResponse(AbstractModel):
    r"""TriggerAIWorkbenchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionId: <p>执行 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExecutionId = None
        self._RequestId = None

    @property
    def ExecutionId(self):
        r"""<p>执行 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExecutionId = params.get("ExecutionId")
        self._RequestId = params.get("RequestId")


class TriggerDigitalTwinTaskResp(AbstractModel):
    r"""触发数字分身任务响应

    """

    def __init__(self):
        r"""
        :param _TaskID: 数字分身任务ID
        :type TaskID: int
        """
        self._TaskID = None

    @property
    def TaskID(self):
        r"""数字分身任务ID
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIWorkbenchAgentRequest(AbstractModel):
    r"""UpdateAIWorkbenchAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Name: <p>Agent 名称</p>
        :type Name: str
        :param _Description: <p>Agent 描述</p>
        :type Description: str
        :param _Category: <p>Agent 分类</p>
        :type Category: str
        :param _Tags: <p>Agent 标签</p>
        :type Tags: list of str
        :param _Instruction: <p>Agent 提示词</p>
        :type Instruction: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        :param _SkillIds: <p>关联技能 ID 列表</p>
        :type SkillIds: list of str
        :param _Source: <p>来源</p>
        :type Source: str
        :param _Status: <p>状态</p>
        :type Status: str
        :param _ResourceMapId: <p>关联的资源地图 ID</p>
        :type ResourceMapId: str
        :param _MCPIds: <p>关联的mcp</p>
        :type MCPIds: list of str
        :param _EnvVars: <p>agent运行时环境变量</p>
        :type EnvVars: list of EnvVar
        """
        self._AgentId = None
        self._Name = None
        self._Description = None
        self._Category = None
        self._Tags = None
        self._Instruction = None
        self._SkillIds = None
        self._Source = None
        self._Status = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._EnvVars = None

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
    def Name(self):
        r"""<p>Agent 名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Category(self):
        r"""<p>Agent 分类</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Tags(self):
        r"""<p>Agent 标签</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Instruction(self):
        r"""<p>Agent 提示词</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        """
        return self._Instruction

    @Instruction.setter
    def Instruction(self, Instruction):
        self._Instruction = Instruction

    @property
    def SkillIds(self):
        r"""<p>关联技能 ID 列表</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def Source(self):
        r"""<p>来源</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Status(self):
        r"""<p>状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceMapId(self):
        r"""<p>关联的资源地图 ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>关联的mcp</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def EnvVars(self):
        r"""<p>agent运行时环境变量</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Tags = params.get("Tags")
        if params.get("Instruction") is not None:
            self._Instruction = InstructionConfig()
            self._Instruction._deserialize(params.get("Instruction"))
        self._SkillIds = params.get("SkillIds")
        self._Source = params.get("Source")
        self._Status = params.get("Status")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIWorkbenchAgentResponse(AbstractModel):
    r"""UpdateAIWorkbenchAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: <p>更新后的 Agent 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Agent: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Agent = None
        self._RequestId = None

    @property
    def Agent(self):
        r"""<p>更新后的 Agent 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
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
            self._Agent = AgentInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._RequestId = params.get("RequestId")


class WeWorkRobotNoticeTmpl(AbstractModel):
    r"""企业微信机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeWorkRobotNoticeTmplMatcher(AbstractModel):
    r"""企业微信机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.WeWorkRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.WeWorkRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = WeWorkRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmpl(AbstractModel):
    r"""告警通知自定义Webhook内容模板

    """

    def __init__(self):
        r"""
        :param _Body: 请求体
        :type Body: str
        :param _BodyContentType: 请求体的类型，非必填、默认为JSON
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyContentType: str
        :param _Headers: 请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of WebhookNoticeTmplHeader
        """
        self._Body = None
        self._BodyContentType = None
        self._Headers = None

    @property
    def Body(self):
        r"""请求体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def BodyContentType(self):
        r"""请求体的类型，非必填、默认为JSON
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BodyContentType

    @BodyContentType.setter
    def BodyContentType(self, BodyContentType):
        self._BodyContentType = BodyContentType

    @property
    def Headers(self):
        r"""请求头
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebhookNoticeTmplHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._BodyContentType = params.get("BodyContentType")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = WebhookNoticeTmplHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmplHeader(AbstractModel):
    r"""告警通知自定义Webhook模板中的请求体头部描述

    """

    def __init__(self):
        r"""
        :param _Key: http请求中header的key
        :type Key: str
        :param _Values: http请求中header的value
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""http请求中header的key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""http请求中header的value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmplMatcher(AbstractModel):
    r"""告警通知自定义Webhook的通知内容模板匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 自定义Webhook内容模板
        :type Template: :class:`tencentcloud.monitor.v20230616.models.WebhookNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""自定义Webhook内容模板
        :rtype: :class:`tencentcloud.monitor.v20230616.models.WebhookNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = WebhookNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        