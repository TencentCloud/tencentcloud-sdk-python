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


class AddMachineGroupInfoRequest(AbstractModel):
    """AddMachineGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _MachineGroupType: 机器组类型
目前type支持 ip 和 label
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineGroupInfoResponse(AbstractModel):
    """AddMachineGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AlarmAnalysisConfig(AbstractModel):
    """告警多维分析一些配置信息

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class AlarmInfo(AbstractModel):
    """告警策略描述

    """

    def __init__(self):
        r"""
        :param _Name: 告警策略名称。
        :type Name: str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTargetInfo
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: 触发条件。
        :type Condition: str
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期。单位是min。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _Status: 开启状态。
        :type Status: bool
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间。
        :type UpdateTime: str
        :param _MessageTemplate: 自定义通知模板
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTemplate: str
        :param _CallBack: 自定义回调模板
注意：此字段可能返回 null，表示取不到有效值。
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析设置
注意：此字段可能返回 null，表示取不到有效值。
        :type Analysis: list of AnalysisDimensional
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Status = None
        self._AlarmId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTargetInfo()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Status = params.get("Status")
        self._AlarmId = params.get("AlarmId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """告警通知模板类型

    """

    def __init__(self):
        r"""
        :param _Name: 告警通知模板名称。
        :type Name: str
        :param _Type: 告警模板的类型。可选值：
<br><li> Trigger - 告警触发
<br><li> Recovery - 告警恢复
<br><li> All - 告警触发和告警恢复
        :type Type: str
        :param _NoticeReceivers: 告警通知模板接收者信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 告警通知模板回调信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCallbacks: list of WebCallback
        :param _AlarmNoticeId: 告警通知模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNoticeId: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._AlarmNoticeId = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTarget(AbstractModel):
    """告警对象

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _Query: 查询语句。
        :type Query: str
        :param _Number: 告警对象序号；从1开始递增。
        :type Number: int
        :param _StartTimeOffset: 查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param _EndTimeOffset: 查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        :param _LogsetId: 日志集ID。
        :type LogsetId: str
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        """
        self._TopicId = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._LogsetId = None
        self._SyntaxRule = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._LogsetId = params.get("LogsetId")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTargetInfo(AbstractModel):
    """告警对象

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID。
        :type LogsetId: str
        :param _LogsetName: 日志集名称。
        :type LogsetName: str
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _TopicName: 日志主题名称。
        :type TopicName: str
        :param _Query: 查询语句。
        :type Query: str
        :param _Number: 告警对象序号。
        :type Number: int
        :param _StartTimeOffset: 查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param _EndTimeOffset: 查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        """
        self._LogsetId = None
        self._LogsetName = None
        self._TopicId = None
        self._TopicName = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryNotice(AbstractModel):
    """告警通知渠道组详情

    """

    def __init__(self):
        r"""
        :param _Name: 通知渠道组名称
        :type Name: str
        :param _AlarmNoticeId: 通知渠道组ID
        :type AlarmNoticeId: str
        """
        self._Name = None
        self._AlarmNoticeId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryRecord(AbstractModel):
    """告警历史详情

    """

    def __init__(self):
        r"""
        :param _RecordId: 告警历史ID
        :type RecordId: str
        :param _AlarmId: 告警策略ID
        :type AlarmId: str
        :param _AlarmName: 告警策略名称
        :type AlarmName: str
        :param _TopicId: 监控对象ID
        :type TopicId: str
        :param _TopicName: 监控对象名称
        :type TopicName: str
        :param _Region: 监控对象所属地域
        :type Region: str
        :param _Trigger: 触发条件
        :type Trigger: str
        :param _TriggerCount: 持续周期，持续满足触发条件TriggerCount个周期后，再进行告警
        :type TriggerCount: int
        :param _AlarmPeriod: 告警通知发送频率，单位为分钟
        :type AlarmPeriod: int
        :param _Notices: 通知渠道组
        :type Notices: list of AlertHistoryNotice
        :param _Duration: 告警持续时间，单位为分钟
        :type Duration: int
        :param _Status: 告警状态，0代表未恢复，1代表已恢复，2代表已失效
        :type Status: int
        :param _CreateTime: 告警发生时间，毫秒级Unix时间戳
        :type CreateTime: int
        :param _GroupTriggerCondition: 告警分组触发时对应的分组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupTriggerCondition: list of GroupTriggerConditionInfo
        :param _AlarmLevel: 告警级别，0代表警告(Warn)，1代表提醒(Info)，2代表紧急 (Critical)
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: int
        :param _MonitorObjectType: 监控对象类型。
0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorObjectType: int
        """
        self._RecordId = None
        self._AlarmId = None
        self._AlarmName = None
        self._TopicId = None
        self._TopicName = None
        self._Region = None
        self._Trigger = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._Notices = None
        self._Duration = None
        self._Status = None
        self._CreateTime = None
        self._GroupTriggerCondition = None
        self._AlarmLevel = None
        self._MonitorObjectType = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def AlarmName(self):
        return self._AlarmName

    @AlarmName.setter
    def AlarmName(self, AlarmName):
        self._AlarmName = AlarmName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupTriggerCondition(self):
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def MonitorObjectType(self):
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._AlarmId = params.get("AlarmId")
        self._AlarmName = params.get("AlarmName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Region = params.get("Region")
        self._Trigger = params.get("Trigger")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlertHistoryNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._Duration = params.get("Duration")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        if params.get("GroupTriggerCondition") is not None:
            self._GroupTriggerCondition = []
            for item in params.get("GroupTriggerCondition"):
                obj = GroupTriggerConditionInfo()
                obj._deserialize(item)
                self._GroupTriggerCondition.append(obj)
        self._AlarmLevel = params.get("AlarmLevel")
        self._MonitorObjectType = params.get("MonitorObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisDimensional(AbstractModel):
    """多维分析的分析维度

    """

    def __init__(self):
        r"""
        :param _Name: 分析名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 分析类型：query，field ，original
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Content: 分析内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _ConfigInfo: 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigInfo: list of AlarmAnalysisConfig
        """
        self._Name = None
        self._Type = None
        self._Content = None
        self._ConfigInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ConfigInfo(self):
        return self._ConfigInfo

    @ConfigInfo.setter
    def ConfigInfo(self, ConfigInfo):
        self._ConfigInfo = ConfigInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        if params.get("ConfigInfo") is not None:
            self._ConfigInfo = []
            for item in params.get("ConfigInfo"):
                obj = AlarmAnalysisConfig()
                obj._deserialize(item)
                self._ConfigInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupRequest(AbstractModel):
    """ApplyConfigToMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._ConfigId = None
        self._GroupId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupResponse(AbstractModel):
    """ApplyConfigToMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CallBackInfo(AbstractModel):
    """回调配置

    """

    def __init__(self):
        r"""
        :param _Body: 回调时的Body
        :type Body: str
        :param _Headers: 回调时的Headers
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of str
        """
        self._Body = None
        self._Headers = None

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRechargeKafkaServerRequest(AbstractModel):
    """CheckRechargeKafkaServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRechargeKafkaServerResponse(AbstractModel):
    """CheckRechargeKafkaServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Kafka集群可访问状态，0：可正常访问 ...
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class Ckafka(AbstractModel):
    """CKafka的描述-需要投递到的kafka信息

    """

    def __init__(self):
        r"""
        :param _Vip: Ckafka 的 Vip
        :type Vip: str
        :param _Vport: Ckafka 的 Vport
        :type Vport: str
        :param _InstanceId: Ckafka 的 InstanceId
        :type InstanceId: str
        :param _InstanceName: Ckafka 的 InstanceName
        :type InstanceName: str
        :param _TopicId: Ckafka 的 TopicId
        :type TopicId: str
        :param _TopicName: Ckafka 的 TopicName
        :type TopicName: str
        """
        self._Vip = None
        self._Vport = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicId = None
        self._TopicName = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerRequest(AbstractModel):
    """CloseKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: CLS对应的topic标识
        :type FromTopicId: str
        """
        self._FromTopicId = None

    @property
    def FromTopicId(self):
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerResponse(AbstractModel):
    """CloseKafkaConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Column(AbstractModel):
    """日志分析的列属性

    """

    def __init__(self):
        r"""
        :param _Name: 列的名字
        :type Name: str
        :param _Type: 列的属性
        :type Type: str
        """
        self._Name = None
        self._Type = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressInfo(AbstractModel):
    """投递日志的压缩配置

    """

    def __init__(self):
        r"""
        :param _Format: 压缩格式，支持gzip、lzop、snappy和none不压缩
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigExtraInfo(AbstractModel):
    """特殊采集规则配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集规则扩展配置ID
        :type ConfigExtraId: str
        :param _Name: 采集规则名称
        :type Name: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Type: 类型：container_stdout、container_file、host_file
        :type Type: str
        :param _HostFile: 节点文件配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 容器文件路径信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogFormat: 日志格式化方式
注意：此字段可能返回 null，表示取不到有效值。
        :type LogFormat: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePaths: list of ExcludePathInfo
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UserDefineRule: 用户自定义解析字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefineRule: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigFlag: 自建采集配置标
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFlag: str
        :param _LogsetId: 日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param _LogsetName: 日志集name
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetName: str
        :param _TopicName: 日志主题name
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        """
        self._ConfigExtraId = None
        self._Name = None
        self._TopicId = None
        self._Type = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogFormat = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UserDefineRule = None
        self._GroupId = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None

    @property
    def ConfigExtraId(self):
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostFile(self):
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigFlag(self):
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        self._Type = params.get("Type")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogFormat = params.get("LogFormat")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UserDefineRule = params.get("UserDefineRule")
        self._GroupId = params.get("GroupId")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigInfo(AbstractModel):
    """采集规则配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID
        :type ConfigId: str
        :param _Name: 采集规则配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _LogFormat: 日志格式化方式
注意：此字段可能返回 null，表示取不到有效值。
        :type LogFormat: str
        :param _Path: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UserDefineRule: 用户自定义解析字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefineRule: str
        """
        self._ConfigId = None
        self._Name = None
        self._LogFormat = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UserDefineRule = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._LogFormat = params.get("LogFormat")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerContent(AbstractModel):
    """投递任务出入参 Content

    """

    def __init__(self):
        r"""
        :param _EnableTag: 是否投递 TAG 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTag: bool
        :param _MetaFields: 需要投递的元数据列表，目前仅支持：\_\_SOURCE\_\_，\_\_FILENAME\_\_，\_\_TIMESTAMP\_\_，\_\_HOSTNAME\_\_和\_\_PKGID\_\_
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaFields: list of str
        :param _TagJsonNotTiled: 当EnableTag为true时，必须填写TagJsonNotTiled字段，TagJsonNotTiled用于标识tag信息是否json平铺，TagJsonNotTiled为true时不平铺，false时平铺
注意：此字段可能返回 null，表示取不到有效值。
        :type TagJsonNotTiled: bool
        :param _TimestampAccuracy: 投递时间戳精度，可选项 [1:秒；2:毫秒] ，默认是秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimestampAccuracy: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._TagJsonNotTiled = None
        self._TimestampAccuracy = None

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagJsonNotTiled(self):
        return self._TagJsonNotTiled

    @TagJsonNotTiled.setter
    def TagJsonNotTiled(self, TagJsonNotTiled):
        self._TagJsonNotTiled = TagJsonNotTiled

    @property
    def TimestampAccuracy(self):
        return self._TimestampAccuracy

    @TimestampAccuracy.setter
    def TimestampAccuracy(self, TimestampAccuracy):
        self._TimestampAccuracy = TimestampAccuracy


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagJsonNotTiled = params.get("TagJsonNotTiled")
        self._TimestampAccuracy = params.get("TimestampAccuracy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerFileInfo(AbstractModel):
    """自建k8s-容器文件路径信息

    """

    def __init__(self):
        r"""
        :param _Namespace: namespace可以多个，用分隔号分割,例如A,B
        :type Namespace: str
        :param _Container: 容器名称
        :type Container: str
        :param _LogPath: 日志文件夹
        :type LogPath: str
        :param _FilePattern: 日志名称
        :type FilePattern: str
        :param _IncludeLabels: pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeLabels: list of str
        :param _WorkLoad: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkLoad: :class:`tencentcloud.cls.v20201016.models.ContainerWorkLoadInfo`
        :param _ExcludeNamespace: 需要排除的namespace可以多个，用分隔号分割,例如A,B
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeNamespace: str
        :param _ExcludeLabels: 需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeLabels: list of str
        """
        self._Namespace = None
        self._Container = None
        self._LogPath = None
        self._FilePattern = None
        self._IncludeLabels = None
        self._WorkLoad = None
        self._ExcludeNamespace = None
        self._ExcludeLabels = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Container(self):
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def IncludeLabels(self):
        return self._IncludeLabels

    @IncludeLabels.setter
    def IncludeLabels(self, IncludeLabels):
        self._IncludeLabels = IncludeLabels

    @property
    def WorkLoad(self):
        return self._WorkLoad

    @WorkLoad.setter
    def WorkLoad(self, WorkLoad):
        self._WorkLoad = WorkLoad

    @property
    def ExcludeNamespace(self):
        return self._ExcludeNamespace

    @ExcludeNamespace.setter
    def ExcludeNamespace(self, ExcludeNamespace):
        self._ExcludeNamespace = ExcludeNamespace

    @property
    def ExcludeLabels(self):
        return self._ExcludeLabels

    @ExcludeLabels.setter
    def ExcludeLabels(self, ExcludeLabels):
        self._ExcludeLabels = ExcludeLabels


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Container = params.get("Container")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        self._IncludeLabels = params.get("IncludeLabels")
        if params.get("WorkLoad") is not None:
            self._WorkLoad = ContainerWorkLoadInfo()
            self._WorkLoad._deserialize(params.get("WorkLoad"))
        self._ExcludeNamespace = params.get("ExcludeNamespace")
        self._ExcludeLabels = params.get("ExcludeLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStdoutInfo(AbstractModel):
    """自建k8s-容器标准输出信息

    """

    def __init__(self):
        r"""
        :param _AllContainers: 是否所有容器
        :type AllContainers: bool
        :param _Container: container为空表所有的，不为空采集指定的容器
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param _Namespace: namespace可以多个，用分隔号分割,例如A,B；为空或者没有这个字段，表示所有namespace
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _IncludeLabels: pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeLabels: list of str
        :param _WorkLoads: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkLoads: list of ContainerWorkLoadInfo
        :param _ExcludeNamespace: 需要排除的namespace可以多个，用分隔号分割,例如A,B
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeNamespace: str
        :param _ExcludeLabels: 需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeLabels: list of str
        """
        self._AllContainers = None
        self._Container = None
        self._Namespace = None
        self._IncludeLabels = None
        self._WorkLoads = None
        self._ExcludeNamespace = None
        self._ExcludeLabels = None

    @property
    def AllContainers(self):
        return self._AllContainers

    @AllContainers.setter
    def AllContainers(self, AllContainers):
        self._AllContainers = AllContainers

    @property
    def Container(self):
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def IncludeLabels(self):
        return self._IncludeLabels

    @IncludeLabels.setter
    def IncludeLabels(self, IncludeLabels):
        self._IncludeLabels = IncludeLabels

    @property
    def WorkLoads(self):
        return self._WorkLoads

    @WorkLoads.setter
    def WorkLoads(self, WorkLoads):
        self._WorkLoads = WorkLoads

    @property
    def ExcludeNamespace(self):
        return self._ExcludeNamespace

    @ExcludeNamespace.setter
    def ExcludeNamespace(self, ExcludeNamespace):
        self._ExcludeNamespace = ExcludeNamespace

    @property
    def ExcludeLabels(self):
        return self._ExcludeLabels

    @ExcludeLabels.setter
    def ExcludeLabels(self, ExcludeLabels):
        self._ExcludeLabels = ExcludeLabels


    def _deserialize(self, params):
        self._AllContainers = params.get("AllContainers")
        self._Container = params.get("Container")
        self._Namespace = params.get("Namespace")
        self._IncludeLabels = params.get("IncludeLabels")
        if params.get("WorkLoads") is not None:
            self._WorkLoads = []
            for item in params.get("WorkLoads"):
                obj = ContainerWorkLoadInfo()
                obj._deserialize(item)
                self._WorkLoads.append(obj)
        self._ExcludeNamespace = params.get("ExcludeNamespace")
        self._ExcludeLabels = params.get("ExcludeLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerWorkLoadInfo(AbstractModel):
    """自建k8s-工作负载信息

    """

    def __init__(self):
        r"""
        :param _Kind: 工作负载的类型
        :type Kind: str
        :param _Name: 工作负载的名称
        :type Name: str
        :param _Container: 容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        """
        self._Kind = None
        self._Name = None
        self._Container = None
        self._Namespace = None

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Container(self):
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Container = params.get("Container")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentInfo(AbstractModel):
    """投递日志的内容格式配置

    """

    def __init__(self):
        r"""
        :param _Format: 内容格式，支持json、csv
        :type Format: str
        :param _Csv: csv格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Csv: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        :param _Json: json格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        :param _Parquet: parquet格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Parquet: :class:`tencentcloud.cls.v20201016.models.ParquetInfo`
        """
        self._Format = None
        self._Csv = None
        self._Json = None
        self._Parquet = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Csv(self):
        return self._Csv

    @Csv.setter
    def Csv(self, Csv):
        self._Csv = Csv

    @property
    def Json(self):
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def Parquet(self):
        return self._Parquet

    @Parquet.setter
    def Parquet(self, Parquet):
        self._Parquet = Parquet


    def _deserialize(self, params):
        self._Format = params.get("Format")
        if params.get("Csv") is not None:
            self._Csv = CsvInfo()
            self._Csv._deserialize(params.get("Csv"))
        if params.get("Json") is not None:
            self._Json = JsonInfo()
            self._Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self._Parquet = ParquetInfo()
            self._Parquet._deserialize(params.get("Parquet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRechargeInfo(AbstractModel):
    """cos导入配置信息

    """

    def __init__(self):
        r"""
        :param _Id: COS导入配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _LogsetId: 日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param _Name: COS导入任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Bucket: COS存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketRegion: str
        :param _Prefix: COS文件所在文件夹的前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type Prefix: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        :param _Status: 状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Enable: 是否启用:   0： 未启用  ， 1：启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Progress: 进度条百分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _Compress: supported: "", "gzip", "lzop", "snappy”; 默认空
注意：此字段可能返回 null，表示取不到有效值。
        :type Compress: str
        :param _ExtractRuleInfo: 见： ExtractRuleInfo 结构描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        self._Id = None
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Status = None
        self._Enable = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Progress = None
        self._Compress = None
        self._ExtractRuleInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Progress = params.get("Progress")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 通知渠道组名称。
        :type Name: str
        :param _Type: 通知类型。可选值：
<li> Trigger - 告警触发
<li> Recovery - 告警恢复
<li> All - 告警触发和告警恢复
        :type Type: str
        :param _NoticeReceivers: 通知接收对象。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 接口回调信息（包括企业微信）。
        :type WebCallbacks: list of WebCallback
        """
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 告警模板ID
        :type AlarmNoticeId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmNoticeId = None
        self._RequestId = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._RequestId = params.get("RequestId")


class CreateAlarmRequest(AbstractModel):
    """CreateAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 告警策略名称
        :type Name: str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: 触发条件。
        :type Condition: str
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期。单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _Status: 是否开启告警策略。默认值为true
        :type Status: bool
        :param _MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param _CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Status = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Status = params.get("Status")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    """CreateAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmId = None
        self._RequestId = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._RequestId = params.get("RequestId")


class CreateConfigExtraRequest(AbstractModel):
    """CreateConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :type Name: str
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _Type: 类型：container_stdout、container_file、host_file
        :type Type: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param _ConfigFlag: 采集配置标
        :type ConfigFlag: str
        :param _LogsetId: 日志集id
        :type LogsetId: str
        :param _LogsetName: 日志集name
        :type LogsetName: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _HostFile: 节点文件配置信息
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 容器文件路径信息
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出信息
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogFormat: 日志格式化方式
        :type LogFormat: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 用户自定义采集规则，Json格式序列化的字符串
        :type UserDefineRule: str
        :param _GroupId: 绑定的机器组id
        :type GroupId: str
        :param _GroupIds: 绑定的机器组id列表
        :type GroupIds: list of str
        """
        self._Name = None
        self._TopicId = None
        self._Type = None
        self._LogType = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogFormat = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._GroupId = None
        self._GroupIds = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ConfigFlag(self):
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def HostFile(self):
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        self._Type = params.get("Type")
        self._LogType = params.get("LogType")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogFormat = params.get("LogFormat")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._GroupId = params.get("GroupId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigExtraResponse(AbstractModel):
    """CreateConfigExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集配置扩展信息ID
        :type ConfigExtraId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigExtraId = None
        self._RequestId = None

    @property
    def ConfigExtraId(self):
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 采集配置名称
        :type Name: str
        :param _Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param _Path: 日志采集路径,包含文件名
        :type Path: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 用户自定义采集规则，Json格式序列化的字符串
        :type UserDefineRule: str
        :param _AdvancedConfig: 高级采集配置
        :type AdvancedConfig: str
        """
        self._Name = None
        self._Output = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._AdvancedConfig = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def AdvancedConfig(self):
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Output = params.get("Output")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        :param _NeedContent: 是否投递日志的元数据信息，默认为 true
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 投递时压缩方式，取值0，2，3。[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        """
        self._TopicId = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCosRechargeRequest(AbstractModel):
    """CreateCosRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Name: 投递任务名称
        :type Name: str
        :param _Bucket: COS存储桶
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域
        :type BucketRegion: str
        :param _Prefix: COS文件所在文件夹的前缀
        :type Prefix: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
        :type LogType: str
        :param _Compress: supported: "", "gzip", "lzop", "snappy”; 默认空
        :type Compress: str
        :param _ExtractRuleInfo: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Compress = None
        self._ExtractRuleInfo = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosRechargeResponse(AbstractModel):
    """CreateCosRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: cos_recharge记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDataTransformRequest(AbstractModel):
    """CreateDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FuncType: 任务类型. 1: 指定主题；2:动态创建
        :type FuncType: int
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Name: 加工任务名称
        :type Name: str
        :param _EtlContent: 加工语句
        :type EtlContent: str
        :param _TaskType: 加工类型  1 使用源日志主题中的随机数据，进行加工预览 :2 使用用户自定义测试数据，进行加工预览 3 创建真实加工任务
        :type TaskType: int
        :param _EnableFlag: 任务启动状态.   默认为1:开启,  2:关闭
        :type EnableFlag: int
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        :param _PreviewLogStatistics: 用于预览加工结果的测试数据
        :type PreviewLogStatistics: list of PreviewLogStatistic
        """
        self._FuncType = None
        self._SrcTopicId = None
        self._Name = None
        self._EtlContent = None
        self._TaskType = None
        self._EnableFlag = None
        self._DstResources = None
        self._PreviewLogStatistics = None

    @property
    def FuncType(self):
        return self._FuncType

    @FuncType.setter
    def FuncType(self, FuncType):
        self._FuncType = FuncType

    @property
    def SrcTopicId(self):
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def PreviewLogStatistics(self):
        return self._PreviewLogStatistics

    @PreviewLogStatistics.setter
    def PreviewLogStatistics(self, PreviewLogStatistics):
        self._PreviewLogStatistics = PreviewLogStatistics


    def _deserialize(self, params):
        self._FuncType = params.get("FuncType")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._TaskType = params.get("TaskType")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        if params.get("PreviewLogStatistics") is not None:
            self._PreviewLogStatistics = []
            for item in params.get("PreviewLogStatistics"):
                obj = PreviewLogStatistic()
                obj._deserialize(item)
                self._PreviewLogStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataTransformResponse(AbstractModel):
    """CreateDataTransform返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateExportRequest(AbstractModel):
    """CreateExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Count: 日志导出数量,  最大值5000万
        :type Count: int
        :param _Query: 日志导出检索语句，不支持<a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>
        :type Query: str
        :param _From: 日志导出起始时间，毫秒时间戳
        :type From: int
        :param _To: 日志导出结束时间，毫秒时间戳
        :type To: int
        :param _Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        :param _Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        """
        self._TopicId = None
        self._Count = None
        self._Query = None
        self._From = None
        self._To = None
        self._Order = None
        self._Format = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Count = params.get("Count")
        self._Query = params.get("Query")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportResponse(AbstractModel):
    """CreateExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID。
        :type ExportId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportId = None
        self._RequestId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        self._RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Rule: 索引规则
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _Status: 是否生效，默认为true
        :type Status: bool
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Rule = None
        self._Status = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._Status = params.get("Status")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateKafkaRechargeRequest(AbstractModel):
    """CreateKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        :param _Name: Kafka导入配置名称
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _Offset: 导入数据位置，-2:最早（默认），-1：最晚
        :type Offset: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址，KafkaType为1时必填
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接，KafkaType为1时必填
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: 用户Kafka消费组名称
        :type ConsumerGroupName: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKafkaRechargeResponse(AbstractModel):
    """CreateKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateLogsetRequest(AbstractModel):
    """CreateLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetName: 日志集名字，不能重名
        :type LogsetName: str
        :param _Tags: 标签描述列表。最大支持10个标签键值对，并且不能有重复的键值对
        :type Tags: list of Tag
        """
        self._LogsetName = None
        self._Tags = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogsetResponse(AbstractModel):
    """CreateLogset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 机器组名字，不能重复
        :type GroupName: str
        :param _MachineGroupType: 创建机器组类型，Type为ip，Values中为Ip字符串列表创建机器组，Type为label， Values中为标签字符串列表创建机器组
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的机器组。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: bool
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMachineGroupResponse(AbstractModel):
    """CreateMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateScheduledSqlRequest(AbstractModel):
    """CreateScheduledSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Name: 任务名称
        :type Name: str
        :param _EnableFlag: 任务启动状态.  1正常开启,  2关闭
        :type EnableFlag: int
        :param _DstResource: 加工任务目的topic_id以及别名
        :type DstResource: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        :param _ScheduledSqlContent: ScheduledSQL语句
        :type ScheduledSqlContent: str
        :param _ProcessStartTime: 调度开始时间,Unix时间戳，单位ms
        :type ProcessStartTime: int
        :param _ProcessType: 调度类型，1:持续运行 2:指定调度结束时间
        :type ProcessType: int
        :param _ProcessPeriod: 调度周期(分钟)
        :type ProcessPeriod: int
        :param _ProcessTimeWindow: 调度时间窗口
        :type ProcessTimeWindow: str
        :param _ProcessDelay: 执行延迟(秒)
        :type ProcessDelay: int
        :param _SrcTopicRegion: 源topicId的地域信息
        :type SrcTopicRegion: str
        :param _ProcessEndTime: 调度结束时间，当ProcessType=2时为必传字段, Unix时间戳，单位ms
        :type ProcessEndTime: int
        :param _SyntaxRule: 语法规则。 默认值为0。0：Lucene语法，1：CQL语法  
        :type SyntaxRule: int
        """
        self._SrcTopicId = None
        self._Name = None
        self._EnableFlag = None
        self._DstResource = None
        self._ScheduledSqlContent = None
        self._ProcessStartTime = None
        self._ProcessType = None
        self._ProcessPeriod = None
        self._ProcessTimeWindow = None
        self._ProcessDelay = None
        self._SrcTopicRegion = None
        self._ProcessEndTime = None
        self._SyntaxRule = None

    @property
    def SrcTopicId(self):
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResource(self):
        return self._DstResource

    @DstResource.setter
    def DstResource(self, DstResource):
        self._DstResource = DstResource

    @property
    def ScheduledSqlContent(self):
        return self._ScheduledSqlContent

    @ScheduledSqlContent.setter
    def ScheduledSqlContent(self, ScheduledSqlContent):
        self._ScheduledSqlContent = ScheduledSqlContent

    @property
    def ProcessStartTime(self):
        return self._ProcessStartTime

    @ProcessStartTime.setter
    def ProcessStartTime(self, ProcessStartTime):
        self._ProcessStartTime = ProcessStartTime

    @property
    def ProcessType(self):
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def ProcessPeriod(self):
        return self._ProcessPeriod

    @ProcessPeriod.setter
    def ProcessPeriod(self, ProcessPeriod):
        self._ProcessPeriod = ProcessPeriod

    @property
    def ProcessTimeWindow(self):
        return self._ProcessTimeWindow

    @ProcessTimeWindow.setter
    def ProcessTimeWindow(self, ProcessTimeWindow):
        self._ProcessTimeWindow = ProcessTimeWindow

    @property
    def ProcessDelay(self):
        return self._ProcessDelay

    @ProcessDelay.setter
    def ProcessDelay(self, ProcessDelay):
        self._ProcessDelay = ProcessDelay

    @property
    def SrcTopicRegion(self):
        return self._SrcTopicRegion

    @SrcTopicRegion.setter
    def SrcTopicRegion(self, SrcTopicRegion):
        self._SrcTopicRegion = SrcTopicRegion

    @property
    def ProcessEndTime(self):
        return self._ProcessEndTime

    @ProcessEndTime.setter
    def ProcessEndTime(self, ProcessEndTime):
        self._ProcessEndTime = ProcessEndTime

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._SrcTopicId = params.get("SrcTopicId")
        self._Name = params.get("Name")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResource") is not None:
            self._DstResource = ScheduledSqlResouceInfo()
            self._DstResource._deserialize(params.get("DstResource"))
        self._ScheduledSqlContent = params.get("ScheduledSqlContent")
        self._ProcessStartTime = params.get("ProcessStartTime")
        self._ProcessType = params.get("ProcessType")
        self._ProcessPeriod = params.get("ProcessPeriod")
        self._ProcessTimeWindow = params.get("ProcessTimeWindow")
        self._ProcessDelay = params.get("ProcessDelay")
        self._SrcTopicRegion = params.get("SrcTopicRegion")
        self._ProcessEndTime = params.get("ProcessEndTime")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScheduledSqlResponse(AbstractModel):
    """CreateScheduledSql返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateShipperRequest(AbstractModel):
    """CreateShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 创建的投递规则所属的日志主题ID
        :type TopicId: str
        :param _Bucket: 创建的投递规则投递的bucket
        :type Bucket: str
        :param _Prefix: 创建的投递规则投递目录的前缀
        :type Prefix: str
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 5-256
        :type MaxSize: int
        :param _FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :type FilenameMode: int
        :param _StartTime: 投递数据范围的开始时间点，不能超出日志主题的生命周期起点。如果用户不填写，默认为用户新建投递任务的时间。
        :type StartTime: int
        :param _EndTime: 投递数据范围的结束时间点，不能填写未来时间。如果用户不填写，默认为持续投递，即无限。
        :type EndTime: int
        """
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShipperResponse(AbstractModel):
    """CreateShipper返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递任务ID
        :type ShipperId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ShipperId = None
        self._RequestId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _PartitionCount: 日志主题分区个数。默认创建1个，最大支持创建10个分区。
        :type PartitionCount: int
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param _AutoSplit: 是否开启自动分裂，默认值为true
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 开启自动分裂后，每个主题能够允许的最大分区数，默认值为50
        :type MaxSplitPartitions: int
        :param _StorageType: 日志主题的存储类型，可选值 hot（标准存储），cold（低频存储）；默认为hot。
        :type StorageType: str
        :param _Period: 生命周期，单位天，标准存储取值范围1\~3600，低频存储取值范围7\~3600天。取值为3640时代表永久保存
        :type Period: int
        :param _Describes: 日志主题描述
        :type Describes: str
        :param _HotPeriod: 0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数。HotPeriod需要大于等于7，且小于Period。仅在StorageType为 hot 时生效
        :type HotPeriod: int
        :param _IsWebTracking: webtracking开关； false: 关闭 true： 开启
        :type IsWebTracking: bool
        """
        self._LogsetId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._IsWebTracking = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def IsWebTracking(self):
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._IsWebTracking = params.get("IsWebTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CsvInfo(AbstractModel):
    """csv内容描述

    """

    def __init__(self):
        r"""
        :param _PrintKey: csv首行是否打印key
        :type PrintKey: bool
        :param _Keys: 每列key的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param _Delimiter: 各字段间的分隔符
        :type Delimiter: str
        :param _EscapeChar: 若字段内容中包含分隔符，则使用该转义符包裹改字段，只能填写单引号、双引号、空字符串
        :type EscapeChar: str
        :param _NonExistingField: 对于上面指定的不存在字段使用该内容填充
        :type NonExistingField: str
        """
        self._PrintKey = None
        self._Keys = None
        self._Delimiter = None
        self._EscapeChar = None
        self._NonExistingField = None

    @property
    def PrintKey(self):
        return self._PrintKey

    @PrintKey.setter
    def PrintKey(self, PrintKey):
        self._PrintKey = PrintKey

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def EscapeChar(self):
        return self._EscapeChar

    @EscapeChar.setter
    def EscapeChar(self, EscapeChar):
        self._EscapeChar = EscapeChar

    @property
    def NonExistingField(self):
        return self._NonExistingField

    @NonExistingField.setter
    def NonExistingField(self, NonExistingField):
        self._NonExistingField = NonExistingField


    def _deserialize(self, params):
        self._PrintKey = params.get("PrintKey")
        self._Keys = params.get("Keys")
        self._Delimiter = params.get("Delimiter")
        self._EscapeChar = params.get("EscapeChar")
        self._NonExistingField = params.get("NonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformResouceInfo(AbstractModel):
    """数据加工的资源信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 目标主题id
        :type TopicId: str
        :param _Alias: 别名
        :type Alias: str
        """
        self._TopicId = None
        self._Alias = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformTaskInfo(AbstractModel):
    """数据加工任务基本详情

    """

    def __init__(self):
        r"""
        :param _Name: 数据加工任务名称
        :type Name: str
        :param _TaskId: 数据加工任务id
        :type TaskId: str
        :param _EnableFlag: 任务启用状态，默认为1，正常开启,  2关闭
        :type EnableFlag: int
        :param _Type: 加工任务类型，1： DSL， 2：SQL
        :type Type: int
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Status: 当前加工任务状态（1准备中/2运行中/3停止中/4已停止）
        :type Status: int
        :param _CreateTime: 加工任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 最近修改时间
        :type UpdateTime: str
        :param _LastEnableTime: 最后启用时间，如果需要重建集群，修改该时间
        :type LastEnableTime: str
        :param _SrcTopicName: 日志主题名称
        :type SrcTopicName: str
        :param _LogsetId: 日志集id
        :type LogsetId: str
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        :param _EtlContent: 加工逻辑函数
        :type EtlContent: str
        """
        self._Name = None
        self._TaskId = None
        self._EnableFlag = None
        self._Type = None
        self._SrcTopicId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LastEnableTime = None
        self._SrcTopicName = None
        self._LogsetId = None
        self._DstResources = None
        self._EtlContent = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SrcTopicId(self):
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastEnableTime(self):
        return self._LastEnableTime

    @LastEnableTime.setter
    def LastEnableTime(self, LastEnableTime):
        self._LastEnableTime = LastEnableTime

    @property
    def SrcTopicName(self):
        return self._SrcTopicName

    @SrcTopicName.setter
    def SrcTopicName(self, SrcTopicName):
        self._SrcTopicName = SrcTopicName

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._EnableFlag = params.get("EnableFlag")
        self._Type = params.get("Type")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastEnableTime = params.get("LastEnableTime")
        self._SrcTopicName = params.get("SrcTopicName")
        self._LogsetId = params.get("LogsetId")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._EtlContent = params.get("EtlContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组ID
        :type AlarmNoticeId: str
        """
        self._AlarmNoticeId = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeResponse(AbstractModel):
    """DeleteAlarmNotice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAlarmRequest(AbstractModel):
    """DeleteAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        """
        self._AlarmId = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    """DeleteAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConfigExtraRequest(AbstractModel):
    """DeleteConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集规则扩展配置ID
        :type ConfigExtraId: str
        """
        self._ConfigExtraId = None

    @property
    def ConfigExtraId(self):
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigExtraResponse(AbstractModel):
    """DeleteConfigExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConfigFromMachineGroupRequest(AbstractModel):
    """DeleteConfigFromMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self._GroupId = None
        self._ConfigId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFromMachineGroupResponse(AbstractModel):
    """DeleteConfigFromMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConsumerRequest(AbstractModel):
    """DeleteConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerResponse(AbstractModel):
    """DeleteConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDataTransformRequest(AbstractModel):
    """DeleteDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 数据加工任务id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DeleteDataTransformResponse(AbstractModel):
    """DeleteDataTransform返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteExportRequest(AbstractModel):
    """DeleteExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID
        :type ExportId: str
        """
        self._ExportId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExportResponse(AbstractModel):
    """DeleteExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteKafkaRechargeRequest(AbstractModel):
    """DeleteKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        """
        self._Id = None
        self._TopicId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKafkaRechargeResponse(AbstractModel):
    """DeleteKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLogsetRequest(AbstractModel):
    """DeleteLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        """
        self._LogsetId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogsetResponse(AbstractModel):
    """DeleteLogset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMachineGroupInfoRequest(AbstractModel):
    """DeleteMachineGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _MachineGroupType: 机器组类型
目前type支持 ip 和 label
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupInfoResponse(AbstractModel):
    """DeleteMachineGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMachineGroupRequest(AbstractModel):
    """DeleteMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupResponse(AbstractModel):
    """DeleteMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteShipperRequest(AbstractModel):
    """DeleteShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        """
        self._ShipperId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShipperResponse(AbstractModel):
    """DeleteShipper返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li> name
按照【通知渠道组名称】进行过滤。
类型：String
必选：否
<li> alarmNoticeId
按照【通知渠道组ID】进行过滤。
类型：String
必选：否
<li> uid
按照【接收用户ID】进行过滤。
类型：String
必选：否
<li> groupId
按照【接收用户组ID】进行过滤。
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNotices: 告警通知模板列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNotices: list of AlarmNotice
        :param _TotalCount: 符合条件的告警通知模板总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmNotices = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AlarmNotices(self):
        return self._AlarmNotices

    @AlarmNotices.setter
    def AlarmNotices(self, AlarmNotices):
        self._AlarmNotices = AlarmNotices

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlarmNotices") is not None:
            self._AlarmNotices = []
            for item in params.get("AlarmNotices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._AlarmNotices.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: name
- 按照【告警策略名称】进行过滤。
- 类型：String
- 必选：否

alarmId
- 按照【告警策略ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【监控对象的日志主题ID】进行过滤。
- 类型：String
- 必选：否

enable
- 按照【启用状态】进行过滤。
- 类型：String
- 备注：enable参数值范围: 1, t, T, TRUE, true, True, 0, f, F, FALSE, false, False。 其它值将返回参数错误信息.
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alarms: 告警策略列表。
        :type Alarms: list of AlarmInfo
        :param _TotalCount: 符合查询条件的告警策略数目。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alarms = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self._Alarms = []
            for item in params.get("Alarms"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlertRecordHistoryRequest(AbstractModel):
    """DescribeAlertRecordHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 查询时间范围启始时间，毫秒级unix时间戳
        :type From: int
        :param _To: 查询时间范围结束时间，毫秒级unix时间戳
        :type To: int
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，最大值100。
        :type Limit: int
        :param _Filters: - alertId：按照告警策略ID进行过滤。类型：String 必选：否
- topicId：按照监控对象ID进行过滤。类型：String 必选：否
- status：按照告警状态进行过滤。类型：String 必选：否，0代表未恢复，1代表已恢复，2代表已失效
- alarmLevel：按照告警等级进行过滤。类型：String 必选：否，0代表警告，1代表提醒，2代表紧急

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        """
        self._From = None
        self._To = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRecordHistoryResponse(AbstractModel):
    """DescribeAlertRecordHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 告警历史总数
        :type TotalCount: int
        :param _Records: 告警历史详情
        :type Records: list of AlertHistoryRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Records = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = AlertHistoryRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigExtrasRequest(AbstractModel):
    """DescribeConfigExtras请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 支持的key： topicId,name, configExtraId, machineGroupId
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigExtrasResponse(AbstractModel):
    """DescribeConfigExtras返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigExtraInfo
        :param _TotalCount: 过滤到的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigExtraInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConfigMachineGroupsRequest(AbstractModel):
    """DescribeConfigMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMachineGroupsResponse(AbstractModel):
    """DescribeConfigMachineGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineGroups: 采集规则配置绑定的机器组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineGroups: list of MachineGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MachineGroups = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: configName
- 按照【采集配置名称】进行模糊匹配过滤。
- 类型：String
- 必选：否

configId
- 按照【采集配置ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【日志主题】进行过滤。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param _TotalCount: 过滤到的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConsumerRequest(AbstractModel):
    """DescribeConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerResponse(AbstractModel):
    """DescribeConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Effective: 投递任务是否生效
        :type Effective: bool
        :param _NeedContent: 是否投递日志的元数据信息
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None
        self._RequestId = None

    @property
    def Effective(self):
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        self._RequestId = params.get("RequestId")


class DescribeCosRechargesRequest(AbstractModel):
    """DescribeCosRecharges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _Status: 状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
        :type Status: int
        :param _Enable: 是否启用:   0： 未启用  ， 1：启用
        :type Enable: int
        """
        self._TopicId = None
        self._Status = None
        self._Enable = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosRechargesResponse(AbstractModel):
    """DescribeCosRecharges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 见: CosRechargeInfo 结构描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CosRechargeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CosRechargeInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataTransformInfoRequest(AbstractModel):
    """DescribeDataTransformInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <br><li> taskName

按照【加工任务名称】进行过滤。
类型：String

必选：否

<br><li> taskId

按照【加工任务id】进行过滤。
类型：String

必选：否

<br><li> srctopicId

按照【源topicId】进行过滤。
类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Type: 默认值为2.   1: 获取单个任务的详细信息 2：获取任务列表
        :type Type: int
        :param _TaskId: Type为1， 此参数必填
        :type TaskId: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Type = None
        self._TaskId = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Type = params.get("Type")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataTransformInfoResponse(AbstractModel):
    """DescribeDataTransformInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataTransformTaskInfos: 数据加工任务列表信息
        :type DataTransformTaskInfos: list of DataTransformTaskInfo
        :param _TotalCount: 任务总次数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataTransformTaskInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataTransformTaskInfos(self):
        return self._DataTransformTaskInfos

    @DataTransformTaskInfos.setter
    def DataTransformTaskInfos(self, DataTransformTaskInfos):
        self._DataTransformTaskInfos = DataTransformTaskInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataTransformTaskInfos") is not None:
            self._DataTransformTaskInfos = []
            for item in params.get("DataTransformTaskInfos"):
                obj = DataTransformTaskInfo()
                obj._deserialize(item)
                self._DataTransformTaskInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._TopicId = None
        self._Offset = None
        self._Limit = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportsResponse(AbstractModel):
    """DescribeExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Exports: 日志导出列表
        :type Exports: list of ExportInfo
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Exports = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Exports(self):
        return self._Exports

    @Exports.setter
    def Exports(self, Exports):
        self._Exports = Exports

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Exports") is not None:
            self._Exports = []
            for item in params.get("Exports"):
                obj = ExportInfo()
                obj._deserialize(item)
                self._Exports.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIndexRequest(AbstractModel):
    """DescribeIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexResponse(AbstractModel):
    """DescribeIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Status: 是否生效
        :type Status: bool
        :param _Rule: 索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _ModifyTime: 索引修改时间，初始值为索引创建时间。
        :type ModifyTime: str
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引
* false:不包含
* true:包含
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type MetadataFlag: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._ModifyTime = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._ModifyTime = params.get("ModifyTime")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        self._RequestId = params.get("RequestId")


class DescribeKafkaRechargesRequest(AbstractModel):
    """DescribeKafkaRecharges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _Id: 导入配置ID
        :type Id: str
        :param _Status: 状态   status 1: 运行中, 2: 暂停...
        :type Status: int
        """
        self._TopicId = None
        self._Id = None
        self._Status = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaRechargesResponse(AbstractModel):
    """DescribeKafkaRecharges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Infos: KafkaRechargeInfo 信息列表
        :type Infos: list of KafkaRechargeInfo
        :param _TotalCount: Kafka导入信息总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Infos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = KafkaRechargeInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLogContextRequest(AbstractModel):
    """DescribeLogContext请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param _BTime: 日志时间,  格式: YYYY-mm-dd HH:MM:SS.FFF
        :type BTime: str
        :param _PkgId: 日志包序号
        :type PkgId: str
        :param _PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: int
        :param _PrevLogs: 上文日志条数,  默认值10
        :type PrevLogs: int
        :param _NextLogs: 下文日志条数,  默认值10
        :type NextLogs: int
        """
        self._TopicId = None
        self._BTime = None
        self._PkgId = None
        self._PkgLogId = None
        self._PrevLogs = None
        self._NextLogs = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def PrevLogs(self):
        return self._PrevLogs

    @PrevLogs.setter
    def PrevLogs(self, PrevLogs):
        self._PrevLogs = PrevLogs

    @property
    def NextLogs(self):
        return self._NextLogs

    @NextLogs.setter
    def NextLogs(self, NextLogs):
        self._NextLogs = NextLogs


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._BTime = params.get("BTime")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._PrevLogs = params.get("PrevLogs")
        self._NextLogs = params.get("NextLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogContextResponse(AbstractModel):
    """DescribeLogContext返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogContextInfos: 日志上下文信息集合
        :type LogContextInfos: list of LogContextInfo
        :param _PrevOver: 上文日志是否已经返回
        :type PrevOver: bool
        :param _NextOver: 下文日志是否已经返回
        :type NextOver: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogContextInfos = None
        self._PrevOver = None
        self._NextOver = None
        self._RequestId = None

    @property
    def LogContextInfos(self):
        return self._LogContextInfos

    @LogContextInfos.setter
    def LogContextInfos(self, LogContextInfos):
        self._LogContextInfos = LogContextInfos

    @property
    def PrevOver(self):
        return self._PrevOver

    @PrevOver.setter
    def PrevOver(self, PrevOver):
        self._PrevOver = PrevOver

    @property
    def NextOver(self):
        return self._NextOver

    @NextOver.setter
    def NextOver(self, NextOver):
        self._NextOver = NextOver

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LogContextInfos") is not None:
            self._LogContextInfos = []
            for item in params.get("LogContextInfos"):
                obj = LogContextInfo()
                obj._deserialize(item)
                self._LogContextInfos.append(obj)
        self._PrevOver = params.get("PrevOver")
        self._NextOver = params.get("NextOver")
        self._RequestId = params.get("RequestId")


class DescribeLogHistogramRequest(AbstractModel):
    """DescribeLogHistogram请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句
        :type Query: str
        :param _TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param _Interval: 时间间隔: 单位ms  限制性条件：(To-From) / interval <= 200
        :type Interval: int
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        """
        self._From = None
        self._To = None
        self._Query = None
        self._TopicId = None
        self._Interval = None
        self._SyntaxRule = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Interval = params.get("Interval")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogHistogramResponse(AbstractModel):
    """DescribeLogHistogram返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 统计周期： 单位ms
        :type Interval: int
        :param _TotalCount: 命中关键字的日志总条数
        :type TotalCount: int
        :param _HistogramInfos: 周期内统计结果详情
        :type HistogramInfos: list of HistogramInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._TotalCount = None
        self._HistogramInfos = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistogramInfos(self):
        return self._HistogramInfos

    @HistogramInfos.setter
    def HistogramInfos(self, HistogramInfos):
        self._HistogramInfos = HistogramInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._TotalCount = params.get("TotalCount")
        if params.get("HistogramInfos") is not None:
            self._HistogramInfos = []
            for item in params.get("HistogramInfos"):
                obj = HistogramInfo()
                obj._deserialize(item)
                self._HistogramInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogsetsRequest(AbstractModel):
    """DescribeLogsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: logsetName
- 按照【日志集名称】进行过滤。
- 类型：String
- 必选：否

logsetId
- 按照【日志集ID】进行过滤。
- 类型：String
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogsetsResponse(AbstractModel):
    """DescribeLogsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 分页的总数目
        :type TotalCount: int
        :param _Logsets: 日志集列表
        :type Logsets: list of LogsetInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Logsets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Logsets(self):
        return self._Logsets

    @Logsets.setter
    def Logsets(self, Logsets):
        self._Logsets = Logsets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Logsets") is not None:
            self._Logsets = []
            for item in params.get("Logsets"):
                obj = LogsetInfo()
                obj._deserialize(item)
                self._Logsets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupConfigsRequest(AbstractModel):
    """DescribeMachineGroupConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupConfigsResponse(AbstractModel):
    """DescribeMachineGroupConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集规则配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._RequestId = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: machineGroupName
- 按照【机器组名称】进行过滤。
- 类型：String
- 必选：否

machineGroupId
- 按照【机器组ID】进行过滤。
- 类型：String
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupsResponse(AbstractModel):
    """DescribeMachineGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineGroups: 机器组信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineGroups: list of MachineGroupInfo
        :param _TotalCount: 分页的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MachineGroups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 查询的机器组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Machines: 机器状态信息组
        :type Machines: list of MachineInfo
        :param _AutoUpdate: 机器组是否开启自动升级功能
        :type AutoUpdate: int
        :param _UpdateStartTime: 机器组自动升级功能预设开始时间
        :type UpdateStartTime: str
        :param _UpdateEndTime: 机器组自动升级功能预设结束时间
        :type UpdateEndTime: str
        :param _LatestAgentVersion: 当前用户可用最新的Loglistener版本
        :type LatestAgentVersion: str
        :param _ServiceLogging: 是否开启服务日志
        :type ServiceLogging: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Machines = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._LatestAgentVersion = None
        self._ServiceLogging = None
        self._RequestId = None

    @property
    def Machines(self):
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def LatestAgentVersion(self):
        return self._LatestAgentVersion

    @LatestAgentVersion.setter
    def LatestAgentVersion(self, LatestAgentVersion):
        self._LatestAgentVersion = LatestAgentVersion

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._Machines.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._LatestAgentVersion = params.get("LatestAgentVersion")
        self._ServiceLogging = params.get("ServiceLogging")
        self._RequestId = params.get("RequestId")


class DescribePartitionsRequest(AbstractModel):
    """DescribePartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePartitionsResponse(AbstractModel):
    """DescribePartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分区列表
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShipperTasksRequest(AbstractModel):
    """DescribeShipperTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _StartTime: 查询的开始时间戳，支持最近3天的查询， 毫秒
        :type StartTime: int
        :param _EndTime: 查询的结束时间戳， 毫秒
        :type EndTime: int
        """
        self._ShipperId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShipperTasksResponse(AbstractModel):
    """DescribeShipperTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 投递任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ShipperTaskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ShipperTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShippersRequest(AbstractModel):
    """DescribeShippers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: - shipperName：按照【投递规则名称】进行过滤。类型：String。必选：否
- shipperId：按照【投递规则ID】进行过滤。类型：String。必选：否
- topicId：按照【日志主题】进行过滤。类型：String。必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShippersResponse(AbstractModel):
    """DescribeShippers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Shippers: 投递规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Shippers: list of ShipperInfo
        :param _TotalCount: 本次查询获取到的总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Shippers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Shippers(self):
        return self._Shippers

    @Shippers.setter
    def Shippers(self, Shippers):
        self._Shippers = Shippers

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Shippers") is not None:
            self._Shippers = []
            for item in params.get("Shippers"):
                obj = ShipperInfo()
                obj._deserialize(item)
                self._Shippers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li> topicName按照【日志主题名称】进行过滤，默认为模糊匹配，可使用PreciseSearch参数设置为精确匹配。类型：String必选：否<br><li> logsetName按照【日志集名称】进行过滤，默认为模糊匹配，可使用PreciseSearch参数设置为精确匹配。类型：String必选：否<br><li> topicId按照【日志主题ID】进行过滤。类型：String必选：否<br><li> logsetId按照【日志集ID】进行过滤，可通过调用DescribeLogsets查询已创建的日志集列表或登录控制台进行查看；也可以调用CreateLogset创建新的日志集。类型：String必选：否<br><li> tagKey按照【标签键】进行过滤。类型：String必选：否<br><li> tag:tagKey按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换，例如tag:exampleKey。类型：String必选：否<br><li> storageType按照【日志主题的存储类型】进行过滤。可选值 hot（标准存储），cold（低频存储）类型：String必选：否每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _PreciseSearch: 控制Filters相关字段是否为精确匹配。
- 0: 默认值，topicName和logsetName模糊匹配
- 1: topicName精确匹配
- 2: logsetName精确匹配
- 3: topicName和logsetName都精确匹配
        :type PreciseSearch: int
        :param _BizType: 主题类型
- 0:日志主题，默认值
- 1:指标主题

        :type BizType: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._PreciseSearch = None
        self._BizType = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PreciseSearch(self):
        return self._PreciseSearch

    @PreciseSearch.setter
    def PreciseSearch(self, PreciseSearch):
        self._PreciseSearch = PreciseSearch

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PreciseSearch = params.get("PreciseSearch")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: 日志主题列表
        :type Topics: list of TopicInfo
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DynamicIndex(AbstractModel):
    """动态更新索引配置

    注意：该功能尚处于内测阶段，如需使用请联系技术支持

    """

    def __init__(self):
        r"""
        :param _Status: 动态索引配置开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
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
        


class ExcludePathInfo(AbstractModel):
    """黑名单path信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型，选填File或Path
        :type Type: str
        :param _Value: Type对应的具体内容
        :type Value: str
        """
        self._Type = None
        self._Value = None

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
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInfo(AbstractModel):
    """日志导出信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _ExportId: 日志导出任务ID
        :type ExportId: str
        :param _Query: 日志导出查询语句
        :type Query: str
        :param _FileName: 日志导出文件名
        :type FileName: str
        :param _FileSize: 日志文件大小
        :type FileSize: int
        :param _Order: 日志导出时间排序
        :type Order: str
        :param _Format: 日志导出格式
        :type Format: str
        :param _Count: 日志导出数量
        :type Count: int
        :param _Status: 日志下载状态。Processing:导出正在进行中，Completed:导出完成，Failed:导出失败，Expired:日志导出已过期(三天有效期), Queuing 排队中
        :type Status: str
        :param _From: 日志导出起始时间
        :type From: int
        :param _To: 日志导出结束时间
        :type To: int
        :param _CosPath: 日志导出路径
        :type CosPath: str
        :param _CreateTime: 日志导出创建时间
        :type CreateTime: str
        """
        self._TopicId = None
        self._ExportId = None
        self._Query = None
        self._FileName = None
        self._FileSize = None
        self._Order = None
        self._Format = None
        self._Count = None
        self._Status = None
        self._From = None
        self._To = None
        self._CosPath = None
        self._CreateTime = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def CosPath(self):
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ExportId = params.get("ExportId")
        self._Query = params.get("Query")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._From = params.get("From")
        self._To = params.get("To")
        self._CosPath = params.get("CosPath")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractRuleInfo(AbstractModel):
    """日志提取规则

    """

    def __init__(self):
        r"""
        :param _TimeKey: 时间字段的key名字，time_key和time_format必须成对出现
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeKey: str
        :param _TimeFormat: 时间字段的格式，参考c语言的strftime函数对于时间的格式说明输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param _Delimiter: 分隔符类型日志的分隔符，只有log_type为delimiter_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Delimiter: str
        :param _LogRegex: 整条日志匹配规则，只有log_type为fullregex_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegex: str
        :param _BeginRegex: 行首匹配规则，只有log_type为multiline_log或fullregex_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginRegex: str
        :param _Keys: 取的每个字段的key名字，为空的key代表丢弃这个字段，只有log_type为delimiter_log时有效，json_log的日志使用json本身的key。限制100个。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param _FilterKeyRegex: 需要过滤日志的key，及其对应的regex
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterKeyRegex: list of KeyRegexInfo
        :param _UnMatchUpLoadSwitch: 解析失败日志是否上传，true表示上传，false表示不上传
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchUpLoadSwitch: bool
        :param _UnMatchLogKey: 失败日志的key
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchLogKey: str
        :param _Backtracking: 增量采集模式下的回溯数据量，默认-1（全量采集）
注意：此字段可能返回 null，表示取不到有效值。
        :type Backtracking: int
        :param _IsGBK: 是否为Gbk编码.   0: 否, 1: 是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGBK: int
        :param _JsonStandard: 是否为标准json.   0: 否, 1: 是
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonStandard: int
        :param _Protocol: syslog传输协议，取值为tcp或者udp。
该字段适用于：创建采集规则配置、修改采集规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Address: syslog系统日志采集指定采集器监听的地址和端口 ，形式：[ip]:[port]。举例：127.0.0.1:9000
该字段适用于：创建采集规则配置、修改采集规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _ParseProtocol: rfc3164：指定系统日志采集使用RFC3164协议解析日志。
rfc5424：指定系统日志采集使用RFC5424协议解析日志。
auto：自动匹配rfc3164或者rfc5424其中一种协议
该字段适用于：创建采集规则配置、修改采集规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ParseProtocol: str
        :param _MetadataType: 元数据类型，0: 不使用元数据信息，1:使用机器组元数据，2:使用用户自定义元数据，3:使用采集配置路径，
        :type MetadataType: int
        :param _PathRegex: 采集配置路径正则表达式，MetadataType为3时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type PathRegex: str
        :param _MetaTags: 用户自定义元数据信息，MetadataType为2时必填
        :type MetaTags: list of MetaTagInfo
        """
        self._TimeKey = None
        self._TimeFormat = None
        self._Delimiter = None
        self._LogRegex = None
        self._BeginRegex = None
        self._Keys = None
        self._FilterKeyRegex = None
        self._UnMatchUpLoadSwitch = None
        self._UnMatchLogKey = None
        self._Backtracking = None
        self._IsGBK = None
        self._JsonStandard = None
        self._Protocol = None
        self._Address = None
        self._ParseProtocol = None
        self._MetadataType = None
        self._PathRegex = None
        self._MetaTags = None

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def BeginRegex(self):
        return self._BeginRegex

    @BeginRegex.setter
    def BeginRegex(self, BeginRegex):
        self._BeginRegex = BeginRegex

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def FilterKeyRegex(self):
        return self._FilterKeyRegex

    @FilterKeyRegex.setter
    def FilterKeyRegex(self, FilterKeyRegex):
        self._FilterKeyRegex = FilterKeyRegex

    @property
    def UnMatchUpLoadSwitch(self):
        return self._UnMatchUpLoadSwitch

    @UnMatchUpLoadSwitch.setter
    def UnMatchUpLoadSwitch(self, UnMatchUpLoadSwitch):
        self._UnMatchUpLoadSwitch = UnMatchUpLoadSwitch

    @property
    def UnMatchLogKey(self):
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def Backtracking(self):
        return self._Backtracking

    @Backtracking.setter
    def Backtracking(self, Backtracking):
        self._Backtracking = Backtracking

    @property
    def IsGBK(self):
        return self._IsGBK

    @IsGBK.setter
    def IsGBK(self, IsGBK):
        self._IsGBK = IsGBK

    @property
    def JsonStandard(self):
        return self._JsonStandard

    @JsonStandard.setter
    def JsonStandard(self, JsonStandard):
        self._JsonStandard = JsonStandard

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ParseProtocol(self):
        return self._ParseProtocol

    @ParseProtocol.setter
    def ParseProtocol(self, ParseProtocol):
        self._ParseProtocol = ParseProtocol

    @property
    def MetadataType(self):
        return self._MetadataType

    @MetadataType.setter
    def MetadataType(self, MetadataType):
        self._MetadataType = MetadataType

    @property
    def PathRegex(self):
        return self._PathRegex

    @PathRegex.setter
    def PathRegex(self, PathRegex):
        self._PathRegex = PathRegex

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._TimeFormat = params.get("TimeFormat")
        self._Delimiter = params.get("Delimiter")
        self._LogRegex = params.get("LogRegex")
        self._BeginRegex = params.get("BeginRegex")
        self._Keys = params.get("Keys")
        if params.get("FilterKeyRegex") is not None:
            self._FilterKeyRegex = []
            for item in params.get("FilterKeyRegex"):
                obj = KeyRegexInfo()
                obj._deserialize(item)
                self._FilterKeyRegex.append(obj)
        self._UnMatchUpLoadSwitch = params.get("UnMatchUpLoadSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._Backtracking = params.get("Backtracking")
        self._IsGBK = params.get("IsGBK")
        self._JsonStandard = params.get("JsonStandard")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._ParseProtocol = params.get("ParseProtocol")
        self._MetadataType = params.get("MetadataType")
        self._PathRegex = params.get("PathRegex")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Key: 需要过滤的字段。
        :type Key: str
        :param _Values: 需要过滤的值。
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
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
        


class FilterRuleInfo(AbstractModel):
    """投递日志的过滤规则

    """

    def __init__(self):
        r"""
        :param _Key: 过滤规则Key
        :type Key: str
        :param _Regex: 过滤规则
        :type Regex: str
        :param _Value: 过滤规则Value
        :type Value: str
        """
        self._Key = None
        self._Regex = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullTextInfo(AbstractModel):
    """全文索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _Tokenizer: 全文索引的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :type Tokenizer: str
        :param _ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self._CaseSensitive = None
        self._Tokenizer = None
        self._ContainZH = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._Tokenizer = params.get("Tokenizer")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogRequest(AbstractModel):
    """GetAlarmLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句，语句长度最大为1024
        :type Query: str
        :param _Limit: 单次查询返回的日志条数，最大值为1000
        :type Limit: int
        :param _Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容
        :type Context: str
        :param _Sort: 日志接口是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        :param _UseNewAnalysis: 为true代表使用新检索,响应参数AnalysisRecords和Columns有效， 为false时代表使用老检索方式, AnalysisResults和ColNames有效
        :type UseNewAnalysis: bool
        """
        self._From = None
        self._To = None
        self._Query = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseNewAnalysis = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseNewAnalysis(self):
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogResponse(AbstractModel):
    """GetAlarmLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 加载后续内容的Context
        :type Context: str
        :param _ListOver: 日志查询结果是否全部返回
        :type ListOver: bool
        :param _Analysis: 返回的是否为分析结果
        :type Analysis: bool
        :param _ColNames: 如果Analysis为True，则返回分析结果的列名，否则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _Results: 日志查询结果；当Analysis为True时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param _AnalysisResults: 日志分析结果；当Analysis为False时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: 新的日志分析结果; UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param _Columns: 日志分析的列属性; UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._ColNames = None
        self._Results = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def ColNames(self):
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def AnalysisResults(self):
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        self._ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._RequestId = params.get("RequestId")


class GroupTriggerConditionInfo(AbstractModel):
    """分组触发条件

    """

    def __init__(self):
        r"""
        :param _Key: 分组触发字段名称
        :type Key: str
        :param _Value: 分组触发字段值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class HistogramInfo(AbstractModel):
    """直方图详细信息

    """

    def __init__(self):
        r"""
        :param _Count: 统计周期内的日志条数
        :type Count: int
        :param _BTime: 按 period 取整后的 unix timestamp： 单位毫秒
        :type BTime: int
        """
        self._Count = None
        self._BTime = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._BTime = params.get("BTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostFileInfo(AbstractModel):
    """自建k8s-节点文件配置信息

    """

    def __init__(self):
        r"""
        :param _LogPath: 日志文件夹
        :type LogPath: str
        :param _FilePattern: 日志文件名
        :type FilePattern: str
        :param _CustomLabels: metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLabels: list of str
        """
        self._LogPath = None
        self._FilePattern = None
        self._CustomLabels = None

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def CustomLabels(self):
        return self._CustomLabels

    @CustomLabels.setter
    def CustomLabels(self, CustomLabels):
        self._CustomLabels = CustomLabels


    def _deserialize(self, params):
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        self._CustomLabels = params.get("CustomLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonInfo(AbstractModel):
    """JSON类型描述

    """

    def __init__(self):
        r"""
        :param _EnableTag: 启用标志
        :type EnableTag: bool
        :param _MetaFields: 元数据信息列表, 可选值为 __SOURCE__、__FILENAME__、__TIMESTAMP__、__HOSTNAME__。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaFields: list of str
        :param _JsonType: 投递Json格式，0：字符串方式投递；1:以结构化方式投递
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonType: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._JsonType = None

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def JsonType(self):
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaConsumerContent(AbstractModel):
    """kafka协议消费内容

    """

    def __init__(self):
        r"""
        :param _Format: 消费格式 0:全文；1:json
        :type Format: int
        :param _EnableTag: 是否投递 TAG 信息
Format为0时，此字段不需要赋值
        :type EnableTag: bool
        :param _MetaFields: 元数据信息列表, 可选值为：\_\_SOURCE\_\_、\_\_FILENAME\_\_
、\_\_TIMESTAMP\_\_、\_\_HOSTNAME\_\_、\_\_PKGID\_\_
Format为0时，此字段不需要赋值
        :type MetaFields: list of str
        :param _TagTransaction: tag数据处理方式：
1:不平铺（默认值）
2:平铺
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTransaction: int
        :param _JsonType: 消费数据Json格式：
1：不转义（默认格式）
2：转义
        :type JsonType: int
        """
        self._Format = None
        self._EnableTag = None
        self._MetaFields = None
        self._TagTransaction = None
        self._JsonType = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagTransaction(self):
        return self._TagTransaction

    @TagTransaction.setter
    def TagTransaction(self, TagTransaction):
        self._TagTransaction = TagTransaction

    @property
    def JsonType(self):
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagTransaction = params.get("TagTransaction")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaProtocolInfo(AbstractModel):
    """Kafka访问协议

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议类型，支持的协议类型包括 plaintext、sasl_plaintext 或 sasl_ssl。建议使用 sasl_ssl，此协议会进行连接加密同时需要用户认证
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Mechanism: 加密类型，支持 PLAIN、SCRAM-SHA-256 或 SCRAM-SHA-512
注意：此字段可能返回 null，表示取不到有效值。
        :type Mechanism: str
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: 用户密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self._Protocol = None
        self._Mechanism = None
        self._UserName = None
        self._Password = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Mechanism(self):
        return self._Mechanism

    @Mechanism.setter
    def Mechanism(self, Mechanism):
        self._Mechanism = Mechanism

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Mechanism = params.get("Mechanism")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaRechargeInfo(AbstractModel):
    """Kafka导入配置信息

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _Name: Kafka导入任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接	
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
注意：此字段可能返回 null，表示取不到有效值。
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: 用户Kafka消费组名称	
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerGroupName: str
        :param _Status: 状态   status 1: 运行中, 2: 暂停 ...
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Offset: 导入数据位置，-1:最早（默认），-2：最晚，大于等于0: 指定offset
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _LogRechargeRule: 日志导入规则
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._Status = None
        self._Offset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LogRechargeRule = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRegexInfo(AbstractModel):
    """需要过滤日志的key，及其对应的regex

    """

    def __init__(self):
        r"""
        :param _Key: 需要过滤日志的key
        :type Key: str
        :param _Regex: key对应的过滤规则regex
        :type Regex: str
        """
        self._Key = None
        self._Regex = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueInfo(AbstractModel):
    """键值或者元字段索引的字段信息

    """

    def __init__(self):
        r"""
        :param _Key: 需要配置键值或者元字段索引的字段名称，仅支持字母、数字、下划线和-./@，且不能以下划线开头

注意：
1，元字段（tag）的Key无需额外添加`__TAG__.`前缀，与上传日志时对应的字段Key一致即可，腾讯云控制台展示时将自动添加`__TAG__.`前缀
2，键值索引（KeyValue）及元字段索引（Tag）中的Key总数不能超过300
3，Key的层级不能超过10层，例如a.b.c.d.e.f.g.h.j.k
4，不允许同时包含json父子级字段，例如a及a.b
        :type Key: str
        :param _Value: 字段的索引描述信息
        :type Value: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = ValueInfo()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContextInfo(AbstractModel):
    """日志上下文信息

    """

    def __init__(self):
        r"""
        :param _Source: 日志来源设备
        :type Source: str
        :param _Filename: 采集路径
        :type Filename: str
        :param _Content: 日志内容
        :type Content: str
        :param _PkgId: 日志包序号
        :type PkgId: str
        :param _PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: int
        :param _BTime: 日志时间戳
        :type BTime: int
        :param _HostName: 日志来源主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _RawLog: 原始日志(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type RawLog: str
        :param _IndexStatus: 日志创建索引异常原因(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        """
        self._Source = None
        self._Filename = None
        self._Content = None
        self._PkgId = None
        self._PkgLogId = None
        self._BTime = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Filename(self):
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Filename = params.get("Filename")
        self._Content = params.get("Content")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._BTime = params.get("BTime")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """日志结果信息

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间，单位ms
        :type Time: int
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _Source: 日志来源IP
        :type Source: str
        :param _FileName: 日志文件名称
        :type FileName: str
        :param _PkgId: 日志上报请求包的ID
        :type PkgId: str
        :param _PkgLogId: 请求包内日志的ID
        :type PkgLogId: str
        :param _LogJson: 日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        :param _HostName: 日志来源主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _RawLog: 原始日志(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type RawLog: str
        :param _IndexStatus: 日志创建索引异常原因(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._Source = None
        self._FileName = None
        self._PkgId = None
        self._PkgLogId = None
        self._LogJson = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def LogJson(self):
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Source = params.get("Source")
        self._FileName = params.get("FileName")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._LogJson = params.get("LogJson")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """日志中的KV对

    """

    def __init__(self):
        r"""
        :param _Key: 日志Key
        :type Key: str
        :param _Value: 日志Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class LogItems(AbstractModel):
    """LogItem的数组

    """

    def __init__(self):
        r"""
        :param _Data: 分析结果返回的KV数据对
        :type Data: list of LogItem
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogRechargeRuleInfo(AbstractModel):
    """日志导入规则

    """

    def __init__(self):
        r"""
        :param _RechargeType: 导入类型，支持json_log：json格式日志，minimalist_log: 单行全文，fullregex_log: 单行完全正则
        :type RechargeType: str
        :param _EncodingFormat: 解析编码格式，0: UTF-8（默认值），1: GBK
        :type EncodingFormat: int
        :param _DefaultTimeSwitch: 使用默认时间，true：开启（默认值）， flase：关闭
        :type DefaultTimeSwitch: bool
        :param _LogRegex: 整条日志匹配规则，只有RechargeType为fullregex_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegex: str
        :param _UnMatchLogSwitch: 解析失败日志是否上传，true表示上传，false表示不上传
        :type UnMatchLogSwitch: bool
        :param _UnMatchLogKey: 解析失败日志的键名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchLogKey: str
        :param _UnMatchLogTimeSrc: 解析失败日志时间来源，0: 系统当前时间，1: Kafka消息时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchLogTimeSrc: int
        :param _DefaultTimeSrc: 默认时间来源，0: 系统当前时间，1: Kafka消息时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultTimeSrc: int
        :param _TimeKey: 时间字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeKey: str
        :param _TimeRegex: 时间提取正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeRegex: str
        :param _TimeFormat: 时间字段格式
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param _TimeZone: 时间字段时区
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeZone: str
        :param _Metadata: 元数据信息，Kafka导入支持kafka_topic,kafka_partition,kafka_offset,kafka_timestamp
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: list of str
        :param _Keys: 日志Key列表，RechargeType为full_regex_log时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        """
        self._RechargeType = None
        self._EncodingFormat = None
        self._DefaultTimeSwitch = None
        self._LogRegex = None
        self._UnMatchLogSwitch = None
        self._UnMatchLogKey = None
        self._UnMatchLogTimeSrc = None
        self._DefaultTimeSrc = None
        self._TimeKey = None
        self._TimeRegex = None
        self._TimeFormat = None
        self._TimeZone = None
        self._Metadata = None
        self._Keys = None

    @property
    def RechargeType(self):
        return self._RechargeType

    @RechargeType.setter
    def RechargeType(self, RechargeType):
        self._RechargeType = RechargeType

    @property
    def EncodingFormat(self):
        return self._EncodingFormat

    @EncodingFormat.setter
    def EncodingFormat(self, EncodingFormat):
        self._EncodingFormat = EncodingFormat

    @property
    def DefaultTimeSwitch(self):
        return self._DefaultTimeSwitch

    @DefaultTimeSwitch.setter
    def DefaultTimeSwitch(self, DefaultTimeSwitch):
        self._DefaultTimeSwitch = DefaultTimeSwitch

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def UnMatchLogSwitch(self):
        return self._UnMatchLogSwitch

    @UnMatchLogSwitch.setter
    def UnMatchLogSwitch(self, UnMatchLogSwitch):
        self._UnMatchLogSwitch = UnMatchLogSwitch

    @property
    def UnMatchLogKey(self):
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def UnMatchLogTimeSrc(self):
        return self._UnMatchLogTimeSrc

    @UnMatchLogTimeSrc.setter
    def UnMatchLogTimeSrc(self, UnMatchLogTimeSrc):
        self._UnMatchLogTimeSrc = UnMatchLogTimeSrc

    @property
    def DefaultTimeSrc(self):
        return self._DefaultTimeSrc

    @DefaultTimeSrc.setter
    def DefaultTimeSrc(self, DefaultTimeSrc):
        self._DefaultTimeSrc = DefaultTimeSrc

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeRegex(self):
        return self._TimeRegex

    @TimeRegex.setter
    def TimeRegex(self, TimeRegex):
        self._TimeRegex = TimeRegex

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys


    def _deserialize(self, params):
        self._RechargeType = params.get("RechargeType")
        self._EncodingFormat = params.get("EncodingFormat")
        self._DefaultTimeSwitch = params.get("DefaultTimeSwitch")
        self._LogRegex = params.get("LogRegex")
        self._UnMatchLogSwitch = params.get("UnMatchLogSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._UnMatchLogTimeSrc = params.get("UnMatchLogTimeSrc")
        self._DefaultTimeSrc = params.get("DefaultTimeSrc")
        self._TimeKey = params.get("TimeKey")
        self._TimeRegex = params.get("TimeRegex")
        self._TimeFormat = params.get("TimeFormat")
        self._TimeZone = params.get("TimeZone")
        self._Metadata = params.get("Metadata")
        self._Keys = params.get("Keys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogsetInfo(AbstractModel):
    """日志集相关信息

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集名称
        :type LogsetName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AssumerName: 云产品标识，日志集由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
注意：此字段可能返回 null，表示取不到有效值。
        :type AssumerName: str
        :param _Tags: 日志集绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _TopicCount: 日志集下日志主题的数目
        :type TopicCount: int
        :param _RoleName: 若AssumerName非空，则表示创建该日志集的服务方角色
        :type RoleName: str
        """
        self._LogsetId = None
        self._LogsetName = None
        self._CreateTime = None
        self._AssumerName = None
        self._Tags = None
        self._TopicCount = None
        self._RoleName = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AssumerName(self):
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TopicCount(self):
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._CreateTime = params.get("CreateTime")
        self._AssumerName = params.get("AssumerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TopicCount = params.get("TopicCount")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupInfo(AbstractModel):
    """机器组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _GroupName: 机器组名称
        :type GroupName: str
        :param _MachineGroupType: 机器组类型
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Tags: 机器组绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpdate: str
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLogging: bool
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._CreateTime = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupTypeInfo(AbstractModel):
    """机器组类型描述

    """

    def __init__(self):
        r"""
        :param _Type: 机器组类型，ip表示该机器组Values中存的是采集机器的IP地址，label表示该机器组Values中存储的是机器的标签
        :type Type: str
        :param _Values: 机器描述列表
        :type Values: list of str
        """
        self._Type = None
        self._Values = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
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
        


class MachineInfo(AbstractModel):
    """机器状态信息

    """

    def __init__(self):
        r"""
        :param _Ip: 机器的IP
        :type Ip: str
        :param _Status: 机器状态，0:异常，1:正常
        :type Status: int
        :param _OfflineTime: 机器离线时间，空为正常，异常返回具体时间
        :type OfflineTime: str
        :param _AutoUpdate: 机器是否开启自动升级。0:关闭，1:开启
        :type AutoUpdate: int
        :param _Version: 机器当前版本号。
        :type Version: str
        :param _UpdateStatus: 机器升级功能状态。
        :type UpdateStatus: int
        :param _ErrCode: 机器升级结果标识。
        :type ErrCode: int
        :param _ErrMsg: 机器升级结果信息。
        :type ErrMsg: str
        """
        self._Ip = None
        self._Status = None
        self._OfflineTime = None
        self._AutoUpdate = None
        self._Version = None
        self._UpdateStatus = None
        self._ErrCode = None
        self._ErrMsg = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateStatus(self):
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoUpdate = params.get("AutoUpdate")
        self._Version = params.get("Version")
        self._UpdateStatus = params.get("UpdateStatus")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionRequest(AbstractModel):
    """MergePartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _PartitionId: 合并的PartitionId
        :type PartitionId: int
        """
        self._TopicId = None
        self._PartitionId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionResponse(AbstractModel):
    """MergePartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 合并结果集
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class MetaTagInfo(AbstractModel):
    """元数据信息

    """

    def __init__(self):
        r"""
        :param _Key: 元数据key
        :type Key: str
        :param _Value: 元数据value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组ID。
        :type AlarmNoticeId: str
        :param _Name: 通知渠道组名称。
        :type Name: str
        :param _Type: 通知类型。可选值：
<li> Trigger - 告警触发
<li> Recovery - 告警恢复
<li> All - 告警触发和告警恢复
        :type Type: str
        :param _NoticeReceivers: 通知接收对象。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 接口回调信息（包括企业微信）。
        :type WebCallbacks: list of WebCallback
        """
        self._AlarmNoticeId = None
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAlarmRequest(AbstractModel):
    """ModifyAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _Name: 告警策略名称
        :type Name: str
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: 触发条件。
        :type Condition: str
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期。单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param _Status: 是否开启告警策略。
        :type Status: bool
        :param _MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param _CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
        """
        self._AlarmId = None
        self._Name = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._AlarmTargets = None
        self._Status = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._Name = params.get("Name")
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        self._Status = params.get("Status")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmResponse(AbstractModel):
    """ModifyAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConfigExtraRequest(AbstractModel):
    """ModifyConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集配置扩展信息id
        :type ConfigExtraId: str
        :param _Name: 采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :type Name: str
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _HostFile: 节点文件配置信息
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 容器文件路径信息
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出信息
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param _LogFormat: 日志格式化方式
        :type LogFormat: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 用户自定义采集规则，Json格式序列化的字符串
        :type UserDefineRule: str
        :param _Type: 类型：container_stdout、container_file、host_file
        :type Type: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigFlag: 自建采集配置标
        :type ConfigFlag: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集name
        :type LogsetName: str
        :param _TopicName: 日志主题name
        :type TopicName: str
        """
        self._ConfigExtraId = None
        self._Name = None
        self._TopicId = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogType = None
        self._LogFormat = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._Type = None
        self._GroupId = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None

    @property
    def ConfigExtraId(self):
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def HostFile(self):
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigFlag(self):
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogType = params.get("LogType")
        self._LogFormat = params.get("LogFormat")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._Type = params.get("Type")
        self._GroupId = params.get("GroupId")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigExtraResponse(AbstractModel):
    """ModifyConfigExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConfigRequest(AbstractModel):
    """ModifyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID
        :type ConfigId: str
        :param _Name: 采集规则配置名称
        :type Name: str
        :param _Path: 日志采集路径，包含文件名
        :type Path: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: 采集配置关联的日志主题（TopicId）
        :type Output: str
        :param _UserDefineRule: 用户自定义解析字符串，Json格式序列化的字符串
        :type UserDefineRule: str
        """
        self._ConfigId = None
        self._Name = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UserDefineRule = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigResponse(AbstractModel):
    """ModifyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsumerRequest(AbstractModel):
    """ModifyConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        :param _Effective: 投递任务是否生效，默认不生效
        :type Effective: bool
        :param _NeedContent: 是否投递日志的元数据信息，默认为 false
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 投递时压缩方式，取值0，2，3。[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        """
        self._TopicId = None
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Effective(self):
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerResponse(AbstractModel):
    """ModifyConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCosRechargeRequest(AbstractModel):
    """ModifyCosRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: COS导入配置ID
        :type Id: str
        :param _TopicId: 日志主题Id
        :type TopicId: str
        :param _Name: COS导入任务名称
        :type Name: str
        :param _Enable: 是否启用:   0： 未启用  ， 1：启用
        :type Enable: int
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._Enable = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCosRechargeResponse(AbstractModel):
    """ModifyCosRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDataTransformRequest(AbstractModel):
    """ModifyDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 加工任务id
        :type TaskId: str
        :param _Name: 加工任务名称
        :type Name: str
        :param _EtlContent: 加工语句
        :type EtlContent: str
        :param _EnableFlag: 任务启动状态. 默认为1，开启,  2关闭
        :type EnableFlag: int
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        """
        self._TaskId = None
        self._Name = None
        self._EtlContent = None
        self._EnableFlag = None
        self._DstResources = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataTransformResponse(AbstractModel):
    """ModifyDataTransform返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyIndexRequest(AbstractModel):
    """ModifyIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Status: 默认不生效
        :type Status: bool
        :param _Rule: 索引规则
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIndexResponse(AbstractModel):
    """ModifyIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyKafkaRechargeRequest(AbstractModel):
    """ModifyKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        :param _Name: Kafka导入配置名称
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: 用户Kafka消费组名称
        :type ConsumerGroupName: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        :param _StatusControl: 导入控制，1：暂停，2：继续
        :type StatusControl: int
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None
        self._StatusControl = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule

    @property
    def StatusControl(self):
        return self._StatusControl

    @StatusControl.setter
    def StatusControl(self, StatusControl):
        self._StatusControl = StatusControl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        self._StatusControl = params.get("StatusControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKafkaRechargeResponse(AbstractModel):
    """ModifyKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLogsetRequest(AbstractModel):
    """ModifyLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集名称
        :type LogsetName: str
        :param _Tags: 日志集的绑定的标签键值对。最大支持10个标签键值对，同一个资源只能同时绑定一个标签键。
        :type Tags: list of Tag
        """
        self._LogsetId = None
        self._LogsetName = None
        self._Tags = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogsetResponse(AbstractModel):
    """ModifyLogset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMachineGroupRequest(AbstractModel):
    """ModifyMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _GroupName: 机器组名称
        :type GroupName: str
        :param _MachineGroupType: 机器组类型
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: bool
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMachineGroupResponse(AbstractModel):
    """ModifyMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyShipperRequest(AbstractModel):
    """ModifyShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _Bucket: 投递规则投递的新的bucket
        :type Bucket: str
        :param _Prefix: 投递规则投递的新的目录前缀
        :type Prefix: str
        :param _Status: 投递规则的开关状态
        :type Status: bool
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 5-256
        :type MaxSize: int
        :param _FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :type FilenameMode: int
        """
        self._ShipperId = None
        self._Bucket = None
        self._Prefix = None
        self._Status = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._Status = params.get("Status")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyShipperResponse(AbstractModel):
    """ModifyShipper返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _Status: 该日志主题是否开始采集
        :type Status: bool
        :param _AutoSplit: 是否开启自动分裂
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 若开启最大分裂，该主题能够能够允许的最大分区数
        :type MaxSplitPartitions: int
        :param _Period: 生命周期，单位天，标准存储取值范围1\~3600，低频存储取值范围7\~3600。取值为3640时代表永久保存
        :type Period: int
        :param _Describes: 日志主题描述
        :type Describes: str
        :param _HotPeriod: 0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数。HotPeriod需要大于等于7，且小于Period。仅在StorageType为 hot 时生效
        :type HotPeriod: int
        :param _IsWebTracking: webtracking开关； false: 关闭 true: 开启
        :type IsWebTracking: bool
        """
        self._TopicId = None
        self._TopicName = None
        self._Tags = None
        self._Status = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._IsWebTracking = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def IsWebTracking(self):
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._IsWebTracking = params.get("IsWebTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorTime(AbstractModel):
    """告警策略中监控任务的执行时间点

    """

    def __init__(self):
        r"""
        :param _Type: 可选值：
<br><li> Period - 周期执行
<br><li> Fixed - 定期执行
        :type Type: str
        :param _Time: 执行的周期，或者定制执行的时间节点。单位为分钟，取值范围为1~1440。
        :type Time: int
        """
        self._Type = None
        self._Time = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiTopicSearchInformation(AbstractModel):
    """多日志主题检索相关信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 要检索分析的日志主题ID
        :type TopicId: str
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
        :type Context: str
        """
        self._TopicId = None
        self._Context = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeReceiver(AbstractModel):
    """告警通知接收者信息

    """

    def __init__(self):
        r"""
        :param _ReceiverType: 接受者类型。可选值：
<br><li> Uin - 用户ID
<br><li> Group - 用户组ID
暂不支持其余接收者类型。
        :type ReceiverType: str
        :param _ReceiverIds: 接收者。
        :type ReceiverIds: list of int
        :param _ReceiverChannels: 通知接收渠道。
<br><li> Email - 邮件
<br><li> Sms - 短信
<br><li> WeChat - 微信
<br><li> Phone - 电话
        :type ReceiverChannels: list of str
        :param _StartTime: 允许接收信息的开始时间。
        :type StartTime: str
        :param _EndTime: 允许接收信息的结束时间。
        :type EndTime: str
        :param _Index: 位序
        :type Index: int
        """
        self._ReceiverType = None
        self._ReceiverIds = None
        self._ReceiverChannels = None
        self._StartTime = None
        self._EndTime = None
        self._Index = None

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def ReceiverIds(self):
        return self._ReceiverIds

    @ReceiverIds.setter
    def ReceiverIds(self, ReceiverIds):
        self._ReceiverIds = ReceiverIds

    @property
    def ReceiverChannels(self):
        return self._ReceiverChannels

    @ReceiverChannels.setter
    def ReceiverChannels(self, ReceiverChannels):
        self._ReceiverChannels = ReceiverChannels

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._ReceiverIds = params.get("ReceiverIds")
        self._ReceiverChannels = params.get("ReceiverChannels")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerRequest(AbstractModel):
    """OpenKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: CLS控制台创建的TopicId
        :type FromTopicId: str
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        :param _ConsumerContent: kafka协议消费数据格式
        :type ConsumerContent: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        self._FromTopicId = None
        self._Compression = None
        self._ConsumerContent = None

    @property
    def FromTopicId(self):
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def ConsumerContent(self):
        return self._ConsumerContent

    @ConsumerContent.setter
    def ConsumerContent(self, ConsumerContent):
        self._ConsumerContent = ConsumerContent


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        self._Compression = params.get("Compression")
        if params.get("ConsumerContent") is not None:
            self._ConsumerContent = KafkaConsumerContent()
            self._ConsumerContent._deserialize(params.get("ConsumerContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerResponse(AbstractModel):
    """OpenKafkaConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicID: 待消费TopicId
        :type TopicID: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicID = None
        self._RequestId = None

    @property
    def TopicID(self):
        return self._TopicID

    @TopicID.setter
    def TopicID(self, TopicID):
        self._TopicID = TopicID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicID = params.get("TopicID")
        self._RequestId = params.get("RequestId")


class ParquetInfo(AbstractModel):
    """Parquet内容

    """

    def __init__(self):
        r"""
        :param _ParquetKeyInfo: ParquetKeyInfo数组
        :type ParquetKeyInfo: list of ParquetKeyInfo
        """
        self._ParquetKeyInfo = None

    @property
    def ParquetKeyInfo(self):
        return self._ParquetKeyInfo

    @ParquetKeyInfo.setter
    def ParquetKeyInfo(self, ParquetKeyInfo):
        self._ParquetKeyInfo = ParquetKeyInfo


    def _deserialize(self, params):
        if params.get("ParquetKeyInfo") is not None:
            self._ParquetKeyInfo = []
            for item in params.get("ParquetKeyInfo"):
                obj = ParquetKeyInfo()
                obj._deserialize(item)
                self._ParquetKeyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParquetKeyInfo(AbstractModel):
    """Parquet内容描述

    """

    def __init__(self):
        r"""
        :param _KeyName: 键值名称
        :type KeyName: str
        :param _KeyType: 数据类型，目前支持6种类型：string、boolean、int32、int64、float、double
        :type KeyType: str
        :param _KeyNonExistingField: 解析失败赋值信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyNonExistingField: str
        """
        self._KeyName = None
        self._KeyType = None
        self._KeyNonExistingField = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def KeyType(self):
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def KeyNonExistingField(self):
        return self._KeyNonExistingField

    @KeyNonExistingField.setter
    def KeyNonExistingField(self, KeyNonExistingField):
        self._KeyNonExistingField = KeyNonExistingField


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._KeyType = params.get("KeyType")
        self._KeyNonExistingField = params.get("KeyNonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """日志主题分区信息

    """

    def __init__(self):
        r"""
        :param _PartitionId: 分区ID
        :type PartitionId: int
        :param _Status: 分区的状态（readwrite或者是readonly）
        :type Status: str
        :param _InclusiveBeginKey: 分区哈希键起始key
        :type InclusiveBeginKey: str
        :param _ExclusiveEndKey: 分区哈希键结束key
        :type ExclusiveEndKey: str
        :param _CreateTime: 分区创建时间
        :type CreateTime: str
        :param _LastWriteTime: 只读分区数据停止写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWriteTime: str
        """
        self._PartitionId = None
        self._Status = None
        self._InclusiveBeginKey = None
        self._ExclusiveEndKey = None
        self._CreateTime = None
        self._LastWriteTime = None

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InclusiveBeginKey(self):
        return self._InclusiveBeginKey

    @InclusiveBeginKey.setter
    def InclusiveBeginKey(self, InclusiveBeginKey):
        self._InclusiveBeginKey = InclusiveBeginKey

    @property
    def ExclusiveEndKey(self):
        return self._ExclusiveEndKey

    @ExclusiveEndKey.setter
    def ExclusiveEndKey(self, ExclusiveEndKey):
        self._ExclusiveEndKey = ExclusiveEndKey

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastWriteTime(self):
        return self._LastWriteTime

    @LastWriteTime.setter
    def LastWriteTime(self, LastWriteTime):
        self._LastWriteTime = LastWriteTime


    def _deserialize(self, params):
        self._PartitionId = params.get("PartitionId")
        self._Status = params.get("Status")
        self._InclusiveBeginKey = params.get("InclusiveBeginKey")
        self._ExclusiveEndKey = params.get("ExclusiveEndKey")
        self._CreateTime = params.get("CreateTime")
        self._LastWriteTime = params.get("LastWriteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeRequest(AbstractModel):
    """PreviewKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PreviewType: 预览类型，1:源数据预览，2:导出结果预览
        :type PreviewType: int
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _Offset: 导入数据位置，-2:最早（默认），-1：最晚
        :type Offset: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: 用户Kafka消费组
        :type ConsumerGroupName: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._PreviewType = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None

    @property
    def PreviewType(self):
        return self._PreviewType

    @PreviewType.setter
    def PreviewType(self, PreviewType):
        self._PreviewType = PreviewType

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._PreviewType = params.get("PreviewType")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeResponse(AbstractModel):
    """PreviewKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogSample: 日志样例，PreviewType为2时返回
        :type LogSample: str
        :param _LogData: 日志预览结果
注意：此字段可能返回 null，表示取不到有效值。
        :type LogData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogSample = None
        self._LogData = None
        self._RequestId = None

    @property
    def LogSample(self):
        return self._LogSample

    @LogSample.setter
    def LogSample(self, LogSample):
        self._LogSample = LogSample

    @property
    def LogData(self):
        return self._LogData

    @LogData.setter
    def LogData(self, LogData):
        self._LogData = LogData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogSample = params.get("LogSample")
        self._LogData = params.get("LogData")
        self._RequestId = params.get("RequestId")


class PreviewLogStatistic(AbstractModel):
    """预览数据详情

    """

    def __init__(self):
        r"""
        :param _LogContent: 日志内容
        :type LogContent: str
        :param _LineNum: 行号
        :type LineNum: int
        :param _DstTopicId: 目标日志主题
        :type DstTopicId: str
        :param _FailReason: 失败错误码， 空字符串""表示正常
        :type FailReason: str
        :param _Time: 日志时间戳
        :type Time: str
        :param _DstTopicName: 目标topic-name
注意：此字段可能返回 null，表示取不到有效值。
        :type DstTopicName: str
        """
        self._LogContent = None
        self._LineNum = None
        self._DstTopicId = None
        self._FailReason = None
        self._Time = None
        self._DstTopicName = None

    @property
    def LogContent(self):
        return self._LogContent

    @LogContent.setter
    def LogContent(self, LogContent):
        self._LogContent = LogContent

    @property
    def LineNum(self):
        return self._LineNum

    @LineNum.setter
    def LineNum(self, LineNum):
        self._LineNum = LineNum

    @property
    def DstTopicId(self):
        return self._DstTopicId

    @DstTopicId.setter
    def DstTopicId(self, DstTopicId):
        self._DstTopicId = DstTopicId

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DstTopicName(self):
        return self._DstTopicName

    @DstTopicName.setter
    def DstTopicName(self, DstTopicName):
        self._DstTopicName = DstTopicName


    def _deserialize(self, params):
        self._LogContent = params.get("LogContent")
        self._LineNum = params.get("LineNum")
        self._DstTopicId = params.get("DstTopicId")
        self._FailReason = params.get("FailReason")
        self._Time = params.get("Time")
        self._DstTopicName = params.get("DstTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskRequest(AbstractModel):
    """RetryShipperTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _TaskId: 投递任务ID
        :type TaskId: str
        """
        self._ShipperId = None
        self._TaskId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskResponse(AbstractModel):
    """RetryShipperTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """索引规则，FullText、KeyValue、Tag参数必须输入一个有效参数

    """

    def __init__(self):
        r"""
        :param _FullText: 全文索引配置, 如果为空时代表未开启全文索引
注意：此字段可能返回 null，表示取不到有效值。
        :type FullText: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        :param _KeyValue: 键值索引配置，如果为空时代表未开启键值索引
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValue: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        :param _Tag: 元字段索引配置，如果为空时代表未开启元字段索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        :param _DynamicIndex: 动态索引配置，如果为空时代表未开启动态段索引

注意：该功能尚处于内测阶段，如需使用请联系技术支持
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicIndex: :class:`tencentcloud.cls.v20201016.models.DynamicIndex`
        """
        self._FullText = None
        self._KeyValue = None
        self._Tag = None
        self._DynamicIndex = None

    @property
    def FullText(self):
        return self._FullText

    @FullText.setter
    def FullText(self, FullText):
        self._FullText = FullText

    @property
    def KeyValue(self):
        return self._KeyValue

    @KeyValue.setter
    def KeyValue(self, KeyValue):
        self._KeyValue = KeyValue

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DynamicIndex(self):
        return self._DynamicIndex

    @DynamicIndex.setter
    def DynamicIndex(self, DynamicIndex):
        self._DynamicIndex = DynamicIndex


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self._FullText = FullTextInfo()
            self._FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self._KeyValue = RuleKeyValueInfo()
            self._KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self._Tag = RuleTagInfo()
            self._Tag._deserialize(params.get("Tag"))
        if params.get("DynamicIndex") is not None:
            self._DynamicIndex = DynamicIndex()
            self._DynamicIndex._deserialize(params.get("DynamicIndex"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleKeyValueInfo(AbstractModel):
    """键值索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _KeyValues: 需要建立索引的键值对信息
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTagInfo(AbstractModel):
    """元字段索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _KeyValues: 元字段索引配置中的字段信息
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledSqlResouceInfo(AbstractModel):
    """ScheduledSql的资源信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 目标主题id
        :type TopicId: str
        :param _Region: topic的地域信息
        :type Region: str
        """
        self._TopicId = None
        self._Region = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要检索分析的日志的起始时间，Unix时间戳（毫秒）
        :type From: int
        :param _To: 要检索分析的日志的结束时间，Unix时间戳（毫秒）
        :type To: int
        :param _Query: 检索分析语句，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a> | <a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>构成，无需对日志进行统计分析时，可省略其中的管道符<code> | </code>及SQL语句
使用*或空字符串可查询所有日志
        :type Query: str
        :param _TopicId: - 要检索分析的日志主题ID，仅能指定一个日志主题。
- 如需同时检索多个日志主题，请使用Topics参数。
        :type TopicId: str
        :param _Limit: 表示单次查询返回的原始日志条数，最大值为1000，获取后续日志需使用Context参数
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果条数指定方式参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :type Limit: int
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :type Context: str
        :param _Sort: 原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :type Sort: str
        :param _UseNewAnalysis: 为true代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效
为false时代表使用老的检索结果返回方式, 输出AnalysisResults和ColNames有效
两种返回方式在编码格式上有少量区别，建议使用true
        :type UseNewAnalysis: bool
        :param _SamplingRate: 执行统计分析（Query中包含SQL）时，是否对原始日志先进行采样，再进行统计分析。
0：自动采样;
0～1：按指定采样率采样，例如0.02;
1：不采样，即精确分析
默认值为1
        :type SamplingRate: float
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        :param _Topics: - 要检索分析的日志主题列表，最大支持20个日志主题。
- 检索单个日志主题时请使用TopicId。
- 不能同时使用TopicId和Topics。
        :type Topics: list of MultiTopicSearchInformation
        """
        self._From = None
        self._To = None
        self._Query = None
        self._TopicId = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseNewAnalysis = None
        self._SamplingRate = None
        self._SyntaxRule = None
        self._Topics = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseNewAnalysis(self):
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis

    @property
    def SamplingRate(self):
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        self._SamplingRate = params.get("SamplingRate")
        self._SyntaxRule = params.get("SyntaxRule")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = MultiTopicSearchInformation()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时
        :type Context: str
        :param _ListOver: 符合检索条件的日志是否已全部返回，如未全部返回可使用Context参数获取后续更多日志
注意：仅当检索分析语句(Query)不包含SQL时有效
        :type ListOver: bool
        :param _Analysis: 返回的是否为统计分析（即SQL）结果
        :type Analysis: bool
        :param _Results: 匹配检索条件的原始日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param _ColNames: 日志统计分析结果的列名
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _AnalysisResults: 日志统计分析结果
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: 日志统计分析结果
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param _Columns: 日志统计分析结果的列属性
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _SamplingRate: 本次统计分析使用的采样率
注意：此字段可能返回 null，表示取不到有效值。
        :type SamplingRate: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._Results = None
        self._ColNames = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._SamplingRate = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ColNames(self):
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def AnalysisResults(self):
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def SamplingRate(self):
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        self._ColNames = params.get("ColNames")
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._SamplingRate = params.get("SamplingRate")
        self._RequestId = params.get("RequestId")


class ShipperInfo(AbstractModel):
    """投递规则

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Bucket: 投递的bucket地址
        :type Bucket: str
        :param _Prefix: 投递的前缀目录
        :type Prefix: str
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB
        :type MaxSize: int
        :param _Status: 是否生效
        :type Status: bool
        :param _FilterRules: 投递日志的过滤规则
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _CreateTime: 投递日志的创建时间
        :type CreateTime: str
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
注意：此字段可能返回 null，表示取不到有效值。
        :type FilenameMode: int
        :param _StartTime: 投递数据范围的开始时间点
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 投递数据范围的结束时间点
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _Progress: 历史数据投递的进度（仅当用户选择的数据内中历史数据时才有效）
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _RemainTime: 历史数据全部投递完成剩余的时间（仅当用户选择的数据中有历史数据时才有效）
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainTime: int
        :param _HistoryStatus: 历史任务状态：
0：实时任务
1：任务准备中
2：任务运行中
3：任务运行异常
4：任务运行结束
注意：此字段可能返回 null，表示取不到有效值。
        :type HistoryStatus: int
        """
        self._ShipperId = None
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._Status = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._CreateTime = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None
        self._Progress = None
        self._RemainTime = None
        self._HistoryStatus = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RemainTime(self):
        return self._RemainTime

    @RemainTime.setter
    def RemainTime(self, RemainTime):
        self._RemainTime = RemainTime

    @property
    def HistoryStatus(self):
        return self._HistoryStatus

    @HistoryStatus.setter
    def HistoryStatus(self, HistoryStatus):
        self._HistoryStatus = HistoryStatus


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        self._Status = params.get("Status")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._CreateTime = params.get("CreateTime")
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Progress = params.get("Progress")
        self._RemainTime = params.get("RemainTime")
        self._HistoryStatus = params.get("HistoryStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperTaskInfo(AbstractModel):
    """投递任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 投递任务ID
        :type TaskId: str
        :param _ShipperId: 投递信息ID
        :type ShipperId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _RangeStart: 本批投递的日志的开始时间戳，毫秒
        :type RangeStart: int
        :param _RangeEnd: 本批投递的日志的结束时间戳， 毫秒
        :type RangeEnd: int
        :param _StartTime: 本次投递任务的开始时间戳， 毫秒
        :type StartTime: int
        :param _EndTime: 本次投递任务的结束时间戳， 毫秒
        :type EndTime: int
        :param _Status: 本次投递的结果，"success","running","failed"
        :type Status: str
        :param _Message: 结果的详细信息
        :type Message: str
        """
        self._TaskId = None
        self._ShipperId = None
        self._TopicId = None
        self._RangeStart = None
        self._RangeEnd = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Message = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RangeStart(self):
        return self._RangeStart

    @RangeStart.setter
    def RangeStart(self, RangeStart):
        self._RangeStart = RangeStart

    @property
    def RangeEnd(self):
        return self._RangeEnd

    @RangeEnd.setter
    def RangeEnd(self, RangeEnd):
        self._RangeEnd = RangeEnd

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._RangeStart = params.get("RangeStart")
        self._RangeEnd = params.get("RangeEnd")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionRequest(AbstractModel):
    """SplitPartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _PartitionId: 待分裂分区ID
        :type PartitionId: int
        :param _SplitKey: 分区切分的哈希key的位置，只在Number=2时有意义
        :type SplitKey: str
        :param _Number: 分区分裂个数(可选)，默认等于2
        :type Number: int
        """
        self._TopicId = None
        self._PartitionId = None
        self._SplitKey = None
        self._Number = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def SplitKey(self):
        return self._SplitKey

    @SplitKey.setter
    def SplitKey(self, SplitKey):
        self._SplitKey = SplitKey

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        self._SplitKey = params.get("SplitKey")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionResponse(AbstractModel):
    """SplitPartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分裂结果集
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """创建资源实例时同时绑定的标签对说明

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TopicInfo(AbstractModel):
    """日志主题信息

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _PartitionCount: 主题分区个数
        :type PartitionCount: int
        :param _Index: 是否开启索引
        :type Index: bool
        :param _AssumerName: 云产品标识，日志主题由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
注意：此字段可能返回 null，表示取不到有效值。
        :type AssumerName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Status: 日主主题是否开启采集
        :type Status: bool
        :param _Tags: 日志主题绑定的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoSplit: 该主题是否开启自动分裂
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 若开启自动分裂的话，该主题能够允许的最大分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSplitPartitions: int
        :param _StorageType: 日主题的存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _Period: 生命周期，单位天，可取值范围1~3600。取值为3640时代表永久保存
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _SubAssumerName: 云产品二级标识，日志主题由其它云产品创建时，该字段会显示云产品名称及其日志类型的二级分类，例如TKE-Audit、TKE-Event。部分云产品仅有云产品标识(AssumerName)，无该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAssumerName: str
        :param _Describes: 日志主题描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describes: str
        :param _HotPeriod: 开启日志沉降，热存储的生命周期， hotPeriod < Period。
热存储为 hotPeriod, 冷存储则为 Period-hotPeriod。
注意：此字段可能返回 null，表示取不到有效值。
        :type HotPeriod: int
        """
        self._LogsetId = None
        self._TopicId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Index = None
        self._AssumerName = None
        self._CreateTime = None
        self._Status = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._SubAssumerName = None
        self._Describes = None
        self._HotPeriod = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AssumerName(self):
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SubAssumerName(self):
        return self._SubAssumerName

    @SubAssumerName.setter
    def SubAssumerName(self, SubAssumerName):
        self._SubAssumerName = SubAssumerName

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        self._Index = params.get("Index")
        self._AssumerName = params.get("AssumerName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._SubAssumerName = params.get("SubAssumerName")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogRequest(AbstractModel):
    """UploadLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题id
        :type TopicId: str
        :param _HashKey: 根据 hashkey 写入相应范围的主题分区
        :type HashKey: str
        :param _CompressType: 压缩方法
        :type CompressType: str
        """
        self._TopicId = None
        self._HashKey = None
        self._CompressType = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def HashKey(self):
        return self._HashKey

    @HashKey.setter
    def HashKey(self, HashKey):
        self._HashKey = HashKey

    @property
    def CompressType(self):
        return self._CompressType

    @CompressType.setter
    def CompressType(self, CompressType):
        self._CompressType = CompressType


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._HashKey = params.get("HashKey")
        self._CompressType = params.get("CompressType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogResponse(AbstractModel):
    """UploadLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ValueInfo(AbstractModel):
    """需要开启键值索引的字段的索引描述信息

    """

    def __init__(self):
        r"""
        :param _Type: 字段类型，目前支持的类型有：long、text、double
        :type Type: str
        :param _Tokenizer: 字段的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
long及double类型字段需为空；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :type Tokenizer: str
        :param _SqlFlag: 字段是否开启分析功能
        :type SqlFlag: bool
        :param _ContainZH: 是否包含中文，long及double类型字段需为false
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self._Type = None
        self._Tokenizer = None
        self._SqlFlag = None
        self._ContainZH = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def SqlFlag(self):
        return self._SqlFlag

    @SqlFlag.setter
    def SqlFlag(self, SqlFlag):
        self._SqlFlag = SqlFlag

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Tokenizer = params.get("Tokenizer")
        self._SqlFlag = params.get("SqlFlag")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallback(AbstractModel):
    """回调地址

    """

    def __init__(self):
        r"""
        :param _Url: 回调地址。
        :type Url: str
        :param _CallbackType: 回调的类型。可选值：
<li> WeCom
<li> Http
        :type CallbackType: str
        :param _Method: 回调方法。可选值：
<li> POST
<li> PUT
默认值为POST。CallbackType为Http时为必选。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Headers: 请求头。
注意：该参数已废弃，请在<a href="https://cloud.tencent.com/document/product/614/56466">创建告警策略</a>接口CallBack参数中指定请求头。
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of str
        :param _Body: 请求内容。
注意：该参数已废弃，请在<a href="https://cloud.tencent.com/document/product/614/56466">创建告警策略</a>接口CallBack参数中指定请求内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        :param _Index: 序号
        :type Index: int
        """
        self._Url = None
        self._CallbackType = None
        self._Method = None
        self._Headers = None
        self._Body = None
        self._Index = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackType(self):
        return self._CallbackType

    @CallbackType.setter
    def CallbackType(self, CallbackType):
        self._CallbackType = CallbackType

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._CallbackType = params.get("CallbackType")
        self._Method = params.get("Method")
        self._Headers = params.get("Headers")
        self._Body = params.get("Body")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        