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
        


class CreateNoticeContentTmplRequest(AbstractModel):
    r"""CreateNoticeContentTmpl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplName: 模板名称
        :type TmplName: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _TmplContents: 模板内容
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _TmplLanguage: 模板语言 en/zh
        :type TmplLanguage: str
        """
        self._TmplName = None
        self._MonitorType = None
        self._TmplContents = None
        self._TmplLanguage = None

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
    def MonitorType(self):
        r"""监控类型
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

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
    def TmplLanguage(self):
        r"""模板语言 en/zh
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
        :param _TmplID: 自定义内容模板ID
        :type TmplID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TmplID = None
        self._RequestId = None

    @property
    def TmplID(self):
        r"""自定义内容模板ID
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


class DeleteNoticeContentTmplsRequest(AbstractModel):
    r"""DeleteNoticeContentTmpls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplIDs: 要删除的模板id
        :type TmplIDs: list of str
        """
        self._TmplIDs = None

    @property
    def TmplIDs(self):
        r"""要删除的模板id
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
        


class FeiShuRobotNoticeTmpl(AbstractModel):
    r"""飞书机器人内容模板配置

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
        :param _TmplID: 自定义通知内容模板id，唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplID: str
        :param _TmplName: 自定义通知内容模板名
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplName: str
        :param _TmplContents: 通知内容
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _CreateTime: Unix时间戳，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: Unix时间戳，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _LastModifier: 最后修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifier: str
        :param _Creator: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _TmplLanguage: 模板语言 en/zh
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
        r"""自定义通知内容模板id，唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmplID

    @TmplID.setter
    def TmplID(self, TmplID):
        self._TmplID = TmplID

    @property
    def TmplName(self):
        r"""自定义通知内容模板名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def TmplContents(self):
        r"""通知内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        """
        return self._TmplContents

    @TmplContents.setter
    def TmplContents(self, TmplContents):
        self._TmplContents = TmplContents

    @property
    def CreateTime(self):
        r"""Unix时间戳，秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Unix时间戳，秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastModifier(self):
        r"""最后修改人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastModifier

    @LastModifier.setter
    def LastModifier(self, LastModifier):
        self._LastModifier = LastModifier

    @property
    def Creator(self):
        r"""创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
    def TmplLanguage(self):
        r"""模板语言 en/zh
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
        