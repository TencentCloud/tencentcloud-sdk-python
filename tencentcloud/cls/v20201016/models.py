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


class AlarmInfo(AbstractModel):
    """告警策略描述

    """

    def __init__(self):
        """
        :param Name: 告警策略名称。
        :type Name: str
        :param AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTargetInfo
        :param MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: 触发条件。
        :type Condition: str
        :param TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param AlarmPeriod: 告警重复的周期。单位是min。取值范围是0~1440。
        :type AlarmPeriod: int
        :param AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param Status: 开启状态。
        :type Status: bool
        :param AlarmId: 告警策略ID。
        :type AlarmId: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param UpdateTime: 最近更新时间。
        :type UpdateTime: str
        :param MessageTemplate: 自定义通知模板
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTemplate: str
        :param CallBack: 自定义回调模板
注意：此字段可能返回 null，表示取不到有效值。
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        """
        self.Name = None
        self.AlarmTargets = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.Status = None
        self.AlarmId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MessageTemplate = None
        self.CallBack = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTargetInfo()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        self.Status = params.get("Status")
        self.AlarmId = params.get("AlarmId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """告警通知模板类型

    """

    def __init__(self):
        """
        :param Name: 告警通知模板名称。
        :type Name: str
        :param Type: 告警模板的类型。可选值：
<br><li> Trigger - 告警触发
<br><li> Recovery - 告警恢复
<br><li> All - 告警触发和告警恢复
        :type Type: str
        :param NoticeReceivers: 告警通知模板接收者信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: 告警通知模板回调信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCallbacks: list of WebCallback
        :param AlarmNoticeId: 告警通知模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNoticeId: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 最近更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None
        self.AlarmNoticeId = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTarget(AbstractModel):
    """告警对象

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID。
        :type TopicId: str
        :param Query: 查询语句。
        :type Query: str
        :param Number: 告警对象序号；从1开始递增。
        :type Number: int
        :param StartTimeOffset: 查询范围起始时间相对当前的历史时间，单位非分钟，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param EndTimeOffset: 查询范围终止时间相对当前的历史时间，单位非分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        :param LogsetId: 日志集ID。
        :type LogsetId: str
        """
        self.TopicId = None
        self.Query = None
        self.Number = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.LogsetId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Query = params.get("Query")
        self.Number = params.get("Number")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTargetInfo(AbstractModel):
    """日志告警监控对线

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID。
        :type LogsetId: str
        :param LogsetName: 日志集名称。
        :type LogsetName: str
        :param TopicId: 日志主题ID。
        :type TopicId: str
        :param TopicName: 日志主题名称。
        :type TopicName: str
        :param Query: 查询语句。
        :type Query: str
        :param Number: 告警对象序号。
        :type Number: int
        :param StartTimeOffset: 查询范围起始时间相对当前的历史时间，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param EndTimeOffset: 查询范围终止时间相对当前的历史时间，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        """
        self.LogsetId = None
        self.LogsetName = None
        self.TopicId = None
        self.TopicName = None
        self.Query = None
        self.Number = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Query = params.get("Query")
        self.Number = params.get("Number")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallBackInfo(AbstractModel):
    """回调配置

    """

    def __init__(self):
        """
        :param Body: 回调时的Body
        :type Body: str
        :param Headers: 回调时的Headers
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of str
        """
        self.Body = None
        self.Headers = None


    def _deserialize(self, params):
        self.Body = params.get("Body")
        self.Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 告警模板名称。
        :type Name: str
        :param Type: 告警模板的类型。可选值：
<br><li> Trigger - 告警触发
<br><li> Recovery - 告警恢复
<br><li> All - 告警触发和告警恢复
        :type Type: str
        :param NoticeReceivers: 告警模板接收者信息。
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: 告警模板回调信息。
        :type WebCallbacks: list of WebCallback
        """
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param AlarmNoticeId: 告警模板ID
        :type AlarmNoticeId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmNoticeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.RequestId = params.get("RequestId")


class CreateAlarmRequest(AbstractModel):
    """CreateAlarm请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 告警策略名称
        :type Name: str
        :param AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: 触发条件。
        :type Condition: str
        :param TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param AlarmPeriod: 告警重复的周期。单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param Status: 是否开启告警策略。默认值为true
        :type Status: bool
        """
        self.Name = None
        self.AlarmTargets = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    """CreateAlarm返回参数结构体

    """

    def __init__(self):
        """
        :param AlarmId: 告警策略ID。
        :type AlarmId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.RequestId = params.get("RequestId")


class CreateExportRequest(AbstractModel):
    """CreateExport请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题
        :type TopicId: str
        :param Query: 日志导出检索语句
        :type Query: str
        :param Count: 日志导出数量
        :type Count: int
        :param From: 日志导出起始时间，毫秒时间戳
        :type From: int
        :param To: 日志导出结束时间，毫秒时间戳
        :type To: int
        :param Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        :param Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        """
        self.TopicId = None
        self.Query = None
        self.Count = None
        self.From = None
        self.To = None
        self.Order = None
        self.Format = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Query = params.get("Query")
        self.Count = params.get("Count")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportResponse(AbstractModel):
    """CreateExport返回参数结构体

    """

    def __init__(self):
        """
        :param ExportId: 日志导出ID。
        :type ExportId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExportId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        self.RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Rule: 索引规则
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param Status: 是否生效，默认为true
        :type Status: bool
        """
        self.TopicId = None
        self.Rule = None
        self.Status = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 机器组名字，不能重复
        :type GroupName: str
        :param MachineGroupType: 创建机器组类型，Type为ip，Values中为Ip字符串列表创建机器组，Type为label， Values中为标签字符串列表创建机器组
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的机器组。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: bool
        :param UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        """
        self.GroupName = None
        self.MachineGroupType = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMachineGroupResponse(AbstractModel):
    """CreateMachineGroup返回参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 机器组ID
        :type GroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param PartitionCount: 日志主题分区个数。默认创建1个，最大支持创建10个分区。
        :type PartitionCount: int
        :param Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param AutoSplit: 是否开启自动分裂，默认值为false
        :type AutoSplit: bool
        :param MaxSplitPartitions: 开启自动分裂后，每个主题能够允许的最大分区数，默认值为50
        :type MaxSplitPartitions: int
        :param StorageType: 日志主题的存储类型，可选值 hot（热存储），cold（冷存储）默认为hot
        :type StorageType: str
        """
        self.LogsetId = None
        self.TopicName = None
        self.PartitionCount = None
        self.Tags = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.StorageType = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        self.StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param AlarmNoticeId: 告警通知模板
        :type AlarmNoticeId: str
        """
        self.AlarmNoticeId = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeResponse(AbstractModel):
    """DeleteAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAlarmRequest(AbstractModel):
    """DeleteAlarm请求参数结构体

    """

    def __init__(self):
        """
        :param AlarmId: 告警策略ID。
        :type AlarmId: str
        """
        self.AlarmId = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    """DeleteAlarm返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteExportRequest(AbstractModel):
    """DeleteExport请求参数结构体

    """

    def __init__(self):
        """
        :param ExportId: 日志导出ID
        :type ExportId: str
        """
        self.ExportId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExportResponse(AbstractModel):
    """DeleteExport返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineGroupRequest(AbstractModel):
    """DeleteMachineGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 机器组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupResponse(AbstractModel):
    """DeleteMachineGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: <br><li> name

按照【告警通知模板名称】进行过滤。
类型：String

必选：否

<br><li> alarmNoticeId

按照【告警通知模板ID】进行过滤。
类型：String

必选：否

<br><li> uid

按照【接收用户ID】进行过滤。

类型：String

必选：否

<br><li> groupId

按照【用户组ID】进行过滤。

类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices返回参数结构体

    """

    def __init__(self):
        """
        :param AlarmNotices: 告警通知模板列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNotices: list of AlarmNotice
        :param TotalCount: 符合条件的告警通知模板总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmNotices = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmNotices") is not None:
            self.AlarmNotices = []
            for item in params.get("AlarmNotices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.AlarmNotices.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: <br><li> name

按照【告警策略名称】进行过滤。
类型：String

必选：否

<br><li> alarmId

按照【告警策略ID】进行过滤。
类型：String

必选：否

<br><li> topicId

按照【监控对象的日志主题ID】进行过滤。

类型：String

必选：否

<br><li> enable

按照【启用状态】进行过滤。

类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms返回参数结构体

    """

    def __init__(self):
        """
        :param Alarms: 告警策略列表。
        :type Alarms: list of AlarmInfo
        :param TotalCount: 符合查询条件的告警策略数目。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Alarms = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self.TopicId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportsResponse(AbstractModel):
    """DescribeExports返回参数结构体

    """

    def __init__(self):
        """
        :param Exports: 日志导出列表
        :type Exports: list of ExportInfo
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Exports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Exports") is not None:
            self.Exports = []
            for item in params.get("Exports"):
                obj = ExportInfo()
                obj._deserialize(item)
                self.Exports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIndexRequest(AbstractModel):
    """DescribeIndex请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexResponse(AbstractModel):
    """DescribeIndex返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Status: 是否生效
        :type Status: bool
        :param Rule: 索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param ModifyTime: 索引修改时间，初始值为索引创建时间。
        :type ModifyTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.Status = None
        self.Rule = None
        self.ModifyTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Status = params.get("Status")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.ModifyTime = params.get("ModifyTime")
        self.RequestId = params.get("RequestId")


class DescribeLogContextRequest(AbstractModel):
    """DescribeLogContext请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param BTime: 日志时间,  格式: YYYY-mm-dd HH:MM:SS
        :type BTime: str
        :param PkgId: 日志包序号
        :type PkgId: str
        :param PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: int
        :param PrevLogs: 上文日志条数,  默认值10
        :type PrevLogs: int
        :param NextLogs: 下文日志条数,  默认值10
        :type NextLogs: int
        """
        self.TopicId = None
        self.BTime = None
        self.PkgId = None
        self.PkgLogId = None
        self.PrevLogs = None
        self.NextLogs = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.BTime = params.get("BTime")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.PrevLogs = params.get("PrevLogs")
        self.NextLogs = params.get("NextLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogContextResponse(AbstractModel):
    """DescribeLogContext返回参数结构体

    """

    def __init__(self):
        """
        :param LogContextInfos: 日志上下文信息集合
        :type LogContextInfos: list of LogContextInfo
        :param PrevOver: 上文日志是否已经返回
        :type PrevOver: bool
        :param NextOver: 下文日志是否已经返回
        :type NextOver: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogContextInfos = None
        self.PrevOver = None
        self.NextOver = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogContextInfos") is not None:
            self.LogContextInfos = []
            for item in params.get("LogContextInfos"):
                obj = LogContextInfo()
                obj._deserialize(item)
                self.LogContextInfos.append(obj)
        self.PrevOver = params.get("PrevOver")
        self.NextOver = params.get("NextOver")
        self.RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: <br><li> machineGroupName

按照【机器组名称】进行过滤。
类型：String

必选：否

<br><li> machineGroupId

按照【机器组ID】进行过滤。
类型：String

必选：否

<br><li> tagKey

按照【标签键】进行过滤。

类型：String

必选：否

<br><li> tag:tagKey

按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
类型：String

必选：否


每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupsResponse(AbstractModel):
    """DescribeMachineGroups返回参数结构体

    """

    def __init__(self):
        """
        :param MachineGroups: 机器组信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineGroups: list of MachineGroupInfo
        :param TotalCount: 分页的总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineGroups = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self.MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self.MachineGroups.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 查询的机器组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        """
        :param Machines: 机器状态信息组
        :type Machines: list of MachineInfo
        :param AutoUpdate: 机器组是否开启自动升级功能
        :type AutoUpdate: int
        :param UpdateStartTime: 机器组自动升级功能预设开始时间
        :type UpdateStartTime: str
        :param UpdateEndTime: 机器组自动升级功能预设结束时间
        :type UpdateEndTime: str
        :param LatestAgentVersion: 当前用户可用最新的Loglistener版本
        :type LatestAgentVersion: str
        :param ServiceLogging: 是否开启服务日志
        :type ServiceLogging: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.LatestAgentVersion = None
        self.ServiceLogging = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.LatestAgentVersion = params.get("LatestAgentVersion")
        self.ServiceLogging = params.get("ServiceLogging")
        self.RequestId = params.get("RequestId")


class DescribePartitionsRequest(AbstractModel):
    """DescribePartitions请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePartitionsResponse(AbstractModel):
    """DescribePartitions返回参数结构体

    """

    def __init__(self):
        """
        :param Partitions: 分区列表
        :type Partitions: list of PartitionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: <br><li> topicName

按照【日志主题名称】进行过滤。
类型：String

必选：否

<br><li> topicId

按照【日志主题ID】进行过滤。
类型：String

必选：否

<br><li> logsetId

按照【日志集ID】进行过滤，可通过调用DescribeLogsets查询已创建的日志集列表或登录控制台进行查看；也可以调用CreateLogset创建新的日志集。

类型：String

必选：否

<br><li> tagKey

按照【标签键】进行过滤。

类型：String

必选：否

<br><li> tag:tagKey

按照【标签键值对】进行过滤。tag-key使用具体的标签键进行替换。使用请参考示例2。

类型：String

必选：否


每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        """
        :param Topics: 日志主题列表
        :type Topics: list of TopicInfo
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Topics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ExportInfo(AbstractModel):
    """日志导出信息

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param ExportId: 日志导出任务ID
        :type ExportId: str
        :param Query: 日志导出查询语句
        :type Query: str
        :param FileName: 日志导出文件名
        :type FileName: str
        :param FileSize: 日志文件大小
        :type FileSize: int
        :param Order: 日志导出时间排序
        :type Order: str
        :param Format: 日志导出格式
        :type Format: str
        :param Count: 日志导出数量
        :type Count: int
        :param Status: 日志下载状态。Processing:导出正在进行中，Complete:导出完成，Failed:导出失败，Expired:日志导出已过期（三天有效期）。
        :type Status: str
        :param From: 日志导出起始时间
        :type From: int
        :param To: 日志导出结束时间
        :type To: int
        :param CosPath: 日志导出路径
        :type CosPath: str
        :param CreateTime: 日志导出创建时间
        :type CreateTime: str
        """
        self.TopicId = None
        self.ExportId = None
        self.Query = None
        self.FileName = None
        self.FileSize = None
        self.Order = None
        self.Format = None
        self.Count = None
        self.Status = None
        self.From = None
        self.To = None
        self.CosPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ExportId = params.get("ExportId")
        self.Query = params.get("Query")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        self.Count = params.get("Count")
        self.Status = params.get("Status")
        self.From = params.get("From")
        self.To = params.get("To")
        self.CosPath = params.get("CosPath")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Key: 需要过滤的字段。
        :type Key: str
        :param Values: 需要过滤的值。
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullTextInfo(AbstractModel):
    """全文索引配置

    """

    def __init__(self):
        """
        :param CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param Tokenizer: 全文索引的分词符，字符串中每个字符代表一个分词符
        :type Tokenizer: str
        :param ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self.CaseSensitive = None
        self.Tokenizer = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        self.Tokenizer = params.get("Tokenizer")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogRequest(AbstractModel):
    """GetAlarmLog请求参数结构体

    """

    def __init__(self):
        """
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Query: 查询语句，语句长度最大为1024
        :type Query: str
        :param Limit: 单次查询返回的日志条数，最大值为100
        :type Limit: int
        :param Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容
        :type Context: str
        :param Sort: 日志接口是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        """
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogResponse(AbstractModel):
    """GetAlarmLog返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 加载后续内容的Context
        :type Context: str
        :param ListOver: 日志查询结果是否全部返回
        :type ListOver: bool
        :param Analysis: 返回的是否为分析结果
        :type Analysis: bool
        :param ColNames: 如果Analysis为True，则返回分析结果的列名，否则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param Results: 日志查询结果；当Analysis为True时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param AnalysisResults: 日志分析结果；当Analysis为False时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.ColNames = None
        self.Results = None
        self.AnalysisResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        self.Analysis = params.get("Analysis")
        self.ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self.AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self.AnalysisResults.append(obj)
        self.RequestId = params.get("RequestId")


class KeyValueInfo(AbstractModel):
    """键值或者元字段索引的字段信息

    """

    def __init__(self):
        """
        :param Key: 需要配置键值或者元字段索引的字段
        :type Key: str
        :param Value: 字段的索引描述信息
        :type Value: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = ValueInfo()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContextInfo(AbstractModel):
    """日志上下文信息

    """

    def __init__(self):
        """
        :param Source: 日志来源设备
        :type Source: str
        :param Filename: 采集路径
        :type Filename: str
        :param Content: 日志内容
        :type Content: str
        :param PkgId: 日志包序号
        :type PkgId: str
        :param PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: int
        :param BTime: 日志时间戳
        :type BTime: int
        """
        self.Source = None
        self.Filename = None
        self.Content = None
        self.PkgId = None
        self.PkgLogId = None
        self.BTime = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Filename = params.get("Filename")
        self.Content = params.get("Content")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.BTime = params.get("BTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """日志结果信息

    """

    def __init__(self):
        """
        :param Time: 日志时间，单位ms
        :type Time: int
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param Source: 日志来源IP
        :type Source: str
        :param FileName: 日志文件名称
        :type FileName: str
        :param PkgId: 日志上报请求包的ID
        :type PkgId: str
        :param PkgLogId: 请求包内日志的ID
        :type PkgLogId: str
        :param LogJson: 日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        """
        self.Time = None
        self.TopicId = None
        self.TopicName = None
        self.Source = None
        self.FileName = None
        self.PkgId = None
        self.PkgLogId = None
        self.LogJson = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Source = params.get("Source")
        self.FileName = params.get("FileName")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.LogJson = params.get("LogJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """日志中的KV对

    """

    def __init__(self):
        """
        :param Key: 日志Key
        :type Key: str
        :param Value: 日志Value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItems(AbstractModel):
    """LogItem的数组

    """

    def __init__(self):
        """
        :param Data: 分析结果返回的KV数据对
        :type Data: list of LogItem
        """
        self.Data = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupInfo(AbstractModel):
    """机器组信息

    """

    def __init__(self):
        """
        :param GroupId: 机器组ID
        :type GroupId: str
        :param GroupName: 机器组名称
        :type GroupName: str
        :param MachineGroupType: 机器组类型
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Tags: 机器组绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param AutoUpdate: 是否开启机器组自动更新
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpdate: str
        :param UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateStartTime: str
        :param UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateEndTime: str
        :param ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLogging: bool
        """
        self.GroupId = None
        self.GroupName = None
        self.MachineGroupType = None
        self.CreateTime = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        self.CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupTypeInfo(AbstractModel):
    """机器组类型描述

    """

    def __init__(self):
        """
        :param Type: 机器组类型，ip表示该机器组Values中存的是采集机器的IP地址，label表示该机器组Values中存储的是机器的标签
        :type Type: str
        :param Values: 机器描述列表
        :type Values: list of str
        """
        self.Type = None
        self.Values = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """机器状态信息

    """

    def __init__(self):
        """
        :param Ip: 机器的IP
        :type Ip: str
        :param Status: 机器状态，0:异常，1:正常
        :type Status: int
        :param OfflineTime: 机器离线时间，空为正常，异常返回具体时间
        :type OfflineTime: str
        :param AutoUpdate: 机器是否开启自动升级。0:关闭，1:开启
        :type AutoUpdate: int
        :param Version: 机器当前版本号。
        :type Version: str
        :param UpdateStatus: 机器升级功能状态。
        :type UpdateStatus: int
        :param ErrCode: 机器升级结果标识。
        :type ErrCode: int
        :param ErrMsg: 机器升级结果信息。
        :type ErrMsg: str
        """
        self.Ip = None
        self.Status = None
        self.OfflineTime = None
        self.AutoUpdate = None
        self.Version = None
        self.UpdateStatus = None
        self.ErrCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Status = params.get("Status")
        self.OfflineTime = params.get("OfflineTime")
        self.AutoUpdate = params.get("AutoUpdate")
        self.Version = params.get("Version")
        self.UpdateStatus = params.get("UpdateStatus")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionRequest(AbstractModel):
    """MergePartition请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param PartitionId: 合并的PartitionId
        :type PartitionId: int
        """
        self.TopicId = None
        self.PartitionId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionResponse(AbstractModel):
    """MergePartition返回参数结构体

    """

    def __init__(self):
        """
        :param Partitions: 合并结果集
        :type Partitions: list of PartitionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param AlarmNoticeId: 告警通知模板ID。
        :type AlarmNoticeId: str
        :param Name: 告警模板名称。
        :type Name: str
        :param Type: 告警模板的类型。可选值：
<br><li> Trigger - 告警触发
<br><li> Recovery - 告警恢复
<br><li> All - 告警触发和告警恢复
        :type Type: str
        :param NoticeReceivers: 告警模板接收者信息。
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: 告警模板回调信息。
        :type WebCallbacks: list of WebCallback
        """
        self.AlarmNoticeId = None
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmRequest(AbstractModel):
    """ModifyAlarm请求参数结构体

    """

    def __init__(self):
        """
        :param AlarmId: 告警策略ID。
        :type AlarmId: str
        :param Name: 告警策略名称
        :type Name: str
        :param MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: 触发条件。
        :type Condition: str
        :param TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param AlarmPeriod: 告警重复的周期。单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param Status: 是否开启告警策略。
        :type Status: bool
        """
        self.AlarmId = None
        self.Name = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.AlarmTargets = None
        self.Status = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.Name = params.get("Name")
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmResponse(AbstractModel):
    """ModifyAlarm返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIndexRequest(AbstractModel):
    """ModifyIndex请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Status: 默认不生效
        :type Status: bool
        :param Rule: 索引规则，Rule和Effective两个必须有一个参数存在
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        """
        self.TopicId = None
        self.Status = None
        self.Rule = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Status = params.get("Status")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIndexResponse(AbstractModel):
    """ModifyIndex返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMachineGroupRequest(AbstractModel):
    """ModifyMachineGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 机器组ID
        :type GroupId: str
        :param GroupName: 机器组名称
        :type GroupName: str
        :param MachineGroupType: 机器组类型
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: bool
        :param UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        """
        self.GroupId = None
        self.GroupName = None
        self.MachineGroupType = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMachineGroupResponse(AbstractModel):
    """ModifyMachineGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param Status: 该日志主题是否开始采集
        :type Status: bool
        :param AutoSplit: 是否开启自动分裂
        :type AutoSplit: bool
        :param MaxSplitPartitions: 若开启最大分裂，该主题能够能够允许的最大分区数
        :type MaxSplitPartitions: int
        """
        self.TopicId = None
        self.TopicName = None
        self.Tags = None
        self.Status = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Status = params.get("Status")
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorTime(AbstractModel):
    """告警策略中监控任务的执行时间点

    """

    def __init__(self):
        """
        :param Type: 可选值：
<br><li> Period - 周期执行
<br><li> Fixed - 定期执行
        :type Type: str
        :param Time: 执行的周期，或者定制执行的时间节点。单位为分钟，取值范围为1~1440。
        :type Time: int
        """
        self.Type = None
        self.Time = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeReceiver(AbstractModel):
    """告警通知接收者信息

    """

    def __init__(self):
        """
        :param ReceiverType: 接受者类型。可选值：
<br><li> Uin - 用户ID
<br><li> Group - 用户组ID
暂不支持其余接收者类型。
        :type ReceiverType: str
        :param ReceiverIds: 接收者。
        :type ReceiverIds: list of int
        :param ReceiverChannels: 通知接收渠道。
<br><li> Email - 邮件
<br><li> Sms - 短信
<br><li> WeChat - 微信
<br><li> Phone - 电话
        :type ReceiverChannels: list of str
        :param StartTime: 允许接收信息的开始时间。
        :type StartTime: str
        :param EndTime: 允许接收信息的结束时间。
        :type EndTime: str
        :param Index: 位序
        :type Index: int
        """
        self.ReceiverType = None
        self.ReceiverIds = None
        self.ReceiverChannels = None
        self.StartTime = None
        self.EndTime = None
        self.Index = None


    def _deserialize(self, params):
        self.ReceiverType = params.get("ReceiverType")
        self.ReceiverIds = params.get("ReceiverIds")
        self.ReceiverChannels = params.get("ReceiverChannels")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """日志主题分区信息

    """

    def __init__(self):
        """
        :param PartitionId: 分区ID
        :type PartitionId: int
        :param Status: 分区的状态（readwrite或者是readonly）
        :type Status: str
        :param InclusiveBeginKey: 分区哈希键起始key
        :type InclusiveBeginKey: str
        :param ExclusiveEndKey: 分区哈希键结束key
        :type ExclusiveEndKey: str
        :param CreateTime: 分区创建时间
        :type CreateTime: str
        :param LastWriteTime: 只读分区数据停止写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWriteTime: str
        """
        self.PartitionId = None
        self.Status = None
        self.InclusiveBeginKey = None
        self.ExclusiveEndKey = None
        self.CreateTime = None
        self.LastWriteTime = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")
        self.Status = params.get("Status")
        self.InclusiveBeginKey = params.get("InclusiveBeginKey")
        self.ExclusiveEndKey = params.get("ExclusiveEndKey")
        self.CreateTime = params.get("CreateTime")
        self.LastWriteTime = params.get("LastWriteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """索引规则，FullText、KeyValue、Tag参数必须输入一个有效参数

    """

    def __init__(self):
        """
        :param FullText: 全文索引配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FullText: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        :param KeyValue: 键值索引配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValue: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        :param Tag: 元字段索引配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        """
        self.FullText = None
        self.KeyValue = None
        self.Tag = None


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self.FullText = FullTextInfo()
            self.FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self.KeyValue = RuleKeyValueInfo()
            self.KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self.Tag = RuleTagInfo()
            self.Tag._deserialize(params.get("Tag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleKeyValueInfo(AbstractModel):
    """键值索引配置

    """

    def __init__(self):
        """
        :param CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param KeyValues: 需要建立索引的键值对信息；最大只能配置100个键值对
        :type KeyValues: list of KeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTagInfo(AbstractModel):
    """标签索引配置信息

    """

    def __init__(self):
        """
        :param CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param KeyValues: 标签索引配置中的字段信息
        :type KeyValues: list of KeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Query: 查询语句，语句长度最大为4096
        :type Query: str
        :param Limit: 单次查询返回的日志条数，最大值为100
        :type Limit: int
        :param Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容
        :type Context: str
        :param Sort: 日志接口是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 加载后续内容的Context
        :type Context: str
        :param ListOver: 日志查询结果是否全部返回
        :type ListOver: bool
        :param Analysis: 返回的是否为分析结果
        :type Analysis: bool
        :param ColNames: 如果Analysis为True，则返回分析结果的列名，否则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param Results: 日志查询结果；当Analysis为True时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param AnalysisResults: 日志分析结果；当Analysis为False时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.ColNames = None
        self.Results = None
        self.AnalysisResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        self.Analysis = params.get("Analysis")
        self.ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self.AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self.AnalysisResults.append(obj)
        self.RequestId = params.get("RequestId")


class SplitPartitionRequest(AbstractModel):
    """SplitPartition请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param PartitionId: 待分裂分区ID
        :type PartitionId: int
        :param SplitKey: 分区切分的哈希key的位置，只在Number=2时有意义
        :type SplitKey: str
        :param Number: 分区分裂个数(可选)，默认等于2
        :type Number: int
        """
        self.TopicId = None
        self.PartitionId = None
        self.SplitKey = None
        self.Number = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.PartitionId = params.get("PartitionId")
        self.SplitKey = params.get("SplitKey")
        self.Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionResponse(AbstractModel):
    """SplitPartition返回参数结构体

    """

    def __init__(self):
        """
        :param Partitions: 分裂结果集
        :type Partitions: list of PartitionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """创建资源实例时同时绑定的标签对说明

    """

    def __init__(self):
        """
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """日志主题信息

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param PartitionCount: 主题分区个数
        :type PartitionCount: int
        :param Index: 是否开启索引
        :type Index: bool
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Status: 日主主题是否开启采集
        :type Status: bool
        :param Tags: 日志主题绑定的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param AutoSplit: 该主题是否开启自动分裂
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSplit: bool
        :param MaxSplitPartitions: 若开启自动分裂的话，该主题能够允许的最大分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSplitPartitions: int
        :param StorageType: 日主题的存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.TopicName = None
        self.PartitionCount = None
        self.Index = None
        self.CreateTime = None
        self.Status = None
        self.Tags = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.StorageType = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        self.Index = params.get("Index")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        self.StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueInfo(AbstractModel):
    """需要开启键值索引的字段的索引描述信息

    """

    def __init__(self):
        """
        :param Type: 字段类型，目前支持的类型有：long、text、double
        :type Type: str
        :param Tokenizer: 字段的分词符，只有当字段类型为text时才有意义；输入字符串中的每个字符代表一个分词符
        :type Tokenizer: str
        :param SqlFlag: 字段是否开启分析功能
        :type SqlFlag: bool
        :param ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self.Type = None
        self.Tokenizer = None
        self.SqlFlag = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tokenizer = params.get("Tokenizer")
        self.SqlFlag = params.get("SqlFlag")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallback(AbstractModel):
    """回调地址

    """

    def __init__(self):
        """
        :param Url: 回调地址。
        :type Url: str
        :param CallbackType: 回调的类型。可选值：
<br><li> WeCom
<br><li> Http
        :type CallbackType: str
        :param Method: 回调方法。可选值：
<br><li> POST
<br><li> PUT
默认值为POST。CallbackType为Http时为必选。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param Headers: 请求头。
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of str
        :param Body: 请求内容。CallbackType为Http时为必选。
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        :param Index: 序号
        :type Index: int
        """
        self.Url = None
        self.CallbackType = None
        self.Method = None
        self.Headers = None
        self.Body = None
        self.Index = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CallbackType = params.get("CallbackType")
        self.Method = params.get("Method")
        self.Headers = params.get("Headers")
        self.Body = params.get("Body")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        