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
        r"""
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
        :param Analysis: 多维分析设置
注意：此字段可能返回 null，表示取不到有效值。
        :type Analysis: list of AnalysisDimensional
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
        self.Analysis = None


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
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
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
        r"""
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
        r"""
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
        r"""
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
        


class AnalysisDimensional(AbstractModel):
    """多维分析的分析维度

    """

    def __init__(self):
        r"""
        :param Name: 分析名称
        :type Name: str
        :param Type: 分析类型：query，field
        :type Type: str
        :param Content: 分析内容
        :type Content: str
        """
        self.Name = None
        self.Type = None
        self.Content = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupRequest(AbstractModel):
    """ApplyConfigToMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集配置ID
        :type ConfigId: str
        :param GroupId: 机器组ID
        :type GroupId: str
        """
        self.ConfigId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupResponse(AbstractModel):
    """ApplyConfigToMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AsyncContextTask(AbstractModel):
    """异步上下文任务

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param CreateTime: 创建时间，时间戳，精确到毫秒
        :type CreateTime: int
        :param Status: 状态，0表示待开始，1表示运行中，2表示已完成，-1表示失败
        :type Status: int
        :param AsyncContextTaskId: 异步上下文任务ID
        :type AsyncContextTaskId: str
        :param ErrorMessage: 任务失败的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param PkgId: 日志包序号
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgLogId: 日志包内一条日志的序号
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgLogId: str
        :param Time: 日志时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param FinishTime: 任务完成时间，时间戳，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: int
        :param AsyncSearchTaskId: 相关联的异步检索ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncSearchTaskId: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.CreateTime = None
        self.Status = None
        self.AsyncContextTaskId = None
        self.ErrorMessage = None
        self.PkgId = None
        self.PkgLogId = None
        self.Time = None
        self.FinishTime = None
        self.AsyncSearchTaskId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.AsyncContextTaskId = params.get("AsyncContextTaskId")
        self.ErrorMessage = params.get("ErrorMessage")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.Time = params.get("Time")
        self.FinishTime = params.get("FinishTime")
        self.AsyncSearchTaskId = params.get("AsyncSearchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncSearchTask(AbstractModel):
    """异步检索任务

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Status: 状态，0表示待开始，1表示运行中，2表示已完成，-1表示失败
        :type Status: int
        :param AsyncSearchTaskId: 异步检索任务ID
        :type AsyncSearchTaskId: str
        :param Query: 查询语句
        :type Query: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Sort: 日志扫描顺序，可选值：asc(升序)、desc(降序)
        :type Sort: str
        :param ErrorMessage: 任务失败的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param LogCount: 异步检索任务匹配的总日志条数
注意：此字段可能返回 null，表示取不到有效值。
        :type LogCount: int
        :param FinishTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.CreateTime = None
        self.Status = None
        self.AsyncSearchTaskId = None
        self.Query = None
        self.From = None
        self.To = None
        self.Sort = None
        self.ErrorMessage = None
        self.LogCount = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.AsyncSearchTaskId = params.get("AsyncSearchTaskId")
        self.Query = params.get("Query")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Sort = params.get("Sort")
        self.ErrorMessage = params.get("ErrorMessage")
        self.LogCount = params.get("LogCount")
        self.FinishTime = params.get("FinishTime")
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
        r"""
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
        


class Column(AbstractModel):
    """日志分析的列属性

    """

    def __init__(self):
        r"""
        :param Name: 列的名字
        :type Name: str
        :param Type: 列的属性
        :type Type: str
        """
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressInfo(AbstractModel):
    """投递日志的压缩配置

    """

    def __init__(self):
        r"""
        :param Format: 压缩格式，支持gzip、lzop和none不压缩
        :type Format: str
        """
        self.Format = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigInfo(AbstractModel):
    """采集规则配置信息

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集规则配置ID
        :type ConfigId: str
        :param LogFormat: 日志格式化方式
注意：此字段可能返回 null，表示取不到有效值。
        :type LogFormat: str
        :param Path: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        :param ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: 采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePaths: list of ExcludePathInfo
        :param Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ConfigId = None
        self.LogFormat = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None
        self.Output = None
        self.UpdateTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.LogFormat = params.get("LogFormat")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        self.Output = params.get("Output")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentInfo(AbstractModel):
    """投递日志的内容格式配置

    """

    def __init__(self):
        r"""
        :param Format: 内容格式，支持json、csv
        :type Format: str
        :param Csv: csv格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Csv: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        :param Json: json格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        """
        self.Format = None
        self.Csv = None
        self.Json = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("Csv") is not None:
            self.Csv = CsvInfo()
            self.Csv._deserialize(params.get("Csv"))
        if params.get("Json") is not None:
            self.Json = JsonInfo()
            self.Json._deserialize(params.get("Json"))
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
        r"""
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
        r"""
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
        r"""
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
        :param MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
        """
        self.Name = None
        self.AlarmTargets = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.Status = None
        self.MessageTemplate = None
        self.CallBack = None
        self.Analysis = None


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
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
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
        r"""
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


class CreateAsyncContextTaskRequest(AbstractModel):
    """CreateAsyncContextTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Time: 日志时间，单位ms
        :type Time: int
        :param PkgId: 日志包序号
        :type PkgId: str
        :param PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param AsyncSearchTaskId: 异步检索任务ID
        :type AsyncSearchTaskId: str
        """
        self.TopicId = None
        self.Time = None
        self.PkgId = None
        self.PkgLogId = None
        self.LogsetId = None
        self.AsyncSearchTaskId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Time = params.get("Time")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.LogsetId = params.get("LogsetId")
        self.AsyncSearchTaskId = params.get("AsyncSearchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAsyncContextTaskResponse(AbstractModel):
    """CreateAsyncContextTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncContextTaskId: 异步上下文任务ID
        :type AsyncContextTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncContextTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncContextTaskId = params.get("AsyncContextTaskId")
        self.RequestId = params.get("RequestId")


class CreateAsyncSearchTaskRequest(AbstractModel):
    """CreateAsyncSearchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID，目前仅支持StorageType为cold的日志主题
        :type TopicId: str
        :param Query: 查询语句，语句长度最大为1024
        :type Query: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Sort: 日志扫描顺序；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Query = None
        self.From = None
        self.To = None
        self.Sort = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Query = params.get("Query")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAsyncSearchTaskResponse(AbstractModel):
    """CreateAsyncSearchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 采集配置名称
        :type Name: str
        :param Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param Path: 日志采集路径,包含文件名
        :type Path: str
        :param LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        """
        self.Name = None
        self.Output = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Output = params.get("Output")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集配置ID
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class CreateExportRequest(AbstractModel):
    """CreateExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 日志主题
        :type TopicId: str
        :param Query: 日志导出检索语句
        :type Query: str
        :param Count: 日志导出数量,  最大值1000万
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLogsetRequest(AbstractModel):
    """CreateLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetName: 日志集名字，不能重名
        :type LogsetName: str
        :param Tags: 标签描述列表。最大支持10个标签键值对，并且不能有重复的键值对
        :type Tags: list of Tag
        """
        self.LogsetName = None
        self.Tags = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogsetResponse(AbstractModel):
    """CreateLogset返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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


class CreateShipperRequest(AbstractModel):
    """CreateShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 创建的投递规则所属的日志主题ID
        :type TopicId: str
        :param Bucket: 创建的投递规则投递的bucket
        :type Bucket: str
        :param Prefix: 创建的投递规则投递目录的前缀
        :type Prefix: str
        :param ShipperName: 投递规则的名字
        :type ShipperName: str
        :param Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 100-256
        :type MaxSize: int
        :param FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        self.TopicId = None
        self.Bucket = None
        self.Prefix = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShipperResponse(AbstractModel):
    """CreateShipper返回参数结构体

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ShipperId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param PartitionCount: 日志主题分区个数。默认创建1个，最大支持创建10个分区。
        :type PartitionCount: int
        :param Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param AutoSplit: 是否开启自动分裂，默认值为true
        :type AutoSplit: bool
        :param MaxSplitPartitions: 开启自动分裂后，每个主题能够允许的最大分区数，默认值为50
        :type MaxSplitPartitions: int
        :param StorageType: 日志主题的存储类型，可选值 hot（实时存储），cold（离线存储）；默认为hot。若传入cold，请先联系客服进行开白。
        :type StorageType: str
        :param Period: 生命周期，单位天；可取值范围1~366。默认30天
        :type Period: int
        """
        self.LogsetId = None
        self.TopicName = None
        self.PartitionCount = None
        self.Tags = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.StorageType = None
        self.Period = None


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
        self.Period = params.get("Period")
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
        r"""
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


class CsvInfo(AbstractModel):
    """csv内容描述

    """

    def __init__(self):
        r"""
        :param PrintKey: csv首行是否打印key
        :type PrintKey: bool
        :param Keys: 每列key的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param Delimiter: 各字段间的分隔符
        :type Delimiter: str
        :param EscapeChar: 若字段内容中包含分隔符，则使用该转义符包裹改字段，只能填写单引号、双引号、空字符串
        :type EscapeChar: str
        :param NonExistingField: 对于上面指定的不存在字段使用该内容填充
        :type NonExistingField: str
        """
        self.PrintKey = None
        self.Keys = None
        self.Delimiter = None
        self.EscapeChar = None
        self.NonExistingField = None


    def _deserialize(self, params):
        self.PrintKey = params.get("PrintKey")
        self.Keys = params.get("Keys")
        self.Delimiter = params.get("Delimiter")
        self.EscapeChar = params.get("EscapeChar")
        self.NonExistingField = params.get("NonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAsyncContextTaskRequest(AbstractModel):
    """DeleteAsyncContextTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param AsyncContextTaskId: 异步上下文任务ID
        :type AsyncContextTaskId: str
        """
        self.TopicId = None
        self.AsyncContextTaskId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.AsyncContextTaskId = params.get("AsyncContextTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAsyncContextTaskResponse(AbstractModel):
    """DeleteAsyncContextTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAsyncSearchTaskRequest(AbstractModel):
    """DeleteAsyncSearchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncSearchTaskId: 异步检索任务ID
        :type AsyncSearchTaskId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        """
        self.AsyncSearchTaskId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.AsyncSearchTaskId = params.get("AsyncSearchTaskId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAsyncSearchTaskResponse(AbstractModel):
    """DeleteAsyncSearchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConfigFromMachineGroupRequest(AbstractModel):
    """DeleteConfigFromMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 机器组ID
        :type GroupId: str
        :param ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self.GroupId = None
        self.ConfigId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFromMachineGroupResponse(AbstractModel):
    """DeleteConfigFromMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集规则配置ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogsetRequest(AbstractModel):
    """DeleteLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        """
        self.LogsetId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogsetResponse(AbstractModel):
    """DeleteLogset返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteShipperRequest(AbstractModel):
    """DeleteShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        """
        self.ShipperId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShipperResponse(AbstractModel):
    """DeleteShipper返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class DescribeAsyncContextResultRequest(AbstractModel):
    """DescribeAsyncContextResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncContextTaskId: 异步检索任务ID
        :type AsyncContextTaskId: str
        :param PkgId: 日志包序号
        :type PkgId: str
        :param PkgLogId: 日志在日志包内的序号
        :type PkgLogId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param PrevLogs: 上文日志条数，默认值10
        :type PrevLogs: int
        :param NextLogs: 下文日志条数，默认值10
        :type NextLogs: int
        """
        self.AsyncContextTaskId = None
        self.PkgId = None
        self.PkgLogId = None
        self.TopicId = None
        self.PrevLogs = None
        self.NextLogs = None


    def _deserialize(self, params):
        self.AsyncContextTaskId = params.get("AsyncContextTaskId")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.TopicId = params.get("TopicId")
        self.PrevLogs = params.get("PrevLogs")
        self.NextLogs = params.get("NextLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncContextResultResponse(AbstractModel):
    """DescribeAsyncContextResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param PrevOver: 上文日志是否已经返回
        :type PrevOver: bool
        :param NextOver: 下文日志是否已经返回
        :type NextOver: bool
        :param Results: 日志内容
        :type Results: list of LogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PrevOver = None
        self.NextOver = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PrevOver = params.get("PrevOver")
        self.NextOver = params.get("NextOver")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAsyncContextTasksRequest(AbstractModel):
    """DescribeAsyncContextTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        :param Filters: <br><li> topicId

按照【日志主题ID】进行过滤。
类型：String

必选：否

<br><li> logsetId

按照【日志集ID】进行过滤，可通过调用DescribeLogsets查询已创建的日志集列表或登录控制台进行查看；也可以调用CreateLogset创建新的日志集。

类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncContextTasksResponse(AbstractModel):
    """DescribeAsyncContextTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncContextTasks: 异步上下文任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncContextTasks: list of AsyncContextTask
        :param TotalCount: 异步上下文任务的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncContextTasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsyncContextTasks") is not None:
            self.AsyncContextTasks = []
            for item in params.get("AsyncContextTasks"):
                obj = AsyncContextTask()
                obj._deserialize(item)
                self.AsyncContextTasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAsyncSearchResultRequest(AbstractModel):
    """DescribeAsyncSearchResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncSearchTaskId: 异步检索任务ID
        :type AsyncSearchTaskId: str
        :param TopicId: 日志集ID
        :type TopicId: str
        :param Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容
        :type Context: str
        :param Limit: 单次调用返回的日志条数，默认为20，最大为500
        :type Limit: int
        """
        self.AsyncSearchTaskId = None
        self.TopicId = None
        self.Context = None
        self.Limit = None


    def _deserialize(self, params):
        self.AsyncSearchTaskId = params.get("AsyncSearchTaskId")
        self.TopicId = params.get("TopicId")
        self.Context = params.get("Context")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncSearchResultResponse(AbstractModel):
    """DescribeAsyncSearchResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 加载后续内容的Context
        :type Context: str
        :param ListOver: 日志查询结果是否全部返回
        :type ListOver: bool
        :param Results: 日志内容
        :type Results: list of LogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAsyncSearchTasksRequest(AbstractModel):
    """DescribeAsyncSearchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        :param Filters: <br><li> topicId

按照【日志主题ID】进行过滤。
类型：String

必选：否

<br><li> logsetId

按照【日志集ID】进行过滤，可通过调用DescribeLogsets查询已创建的日志集列表或登录控制台进行查看；也可以调用CreateLogset创建新的日志集。

类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncSearchTasksResponse(AbstractModel):
    """DescribeAsyncSearchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncSearchTasks: 异步检索任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncSearchTasks: list of AsyncSearchTask
        :param TotalCount: 异步检索任务的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncSearchTasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsyncSearchTasks") is not None:
            self.AsyncSearchTasks = []
            for item in params.get("AsyncSearchTasks"):
                obj = AsyncSearchTask()
                obj._deserialize(item)
                self.AsyncSearchTasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeConfigMachineGroupsRequest(AbstractModel):
    """DescribeConfigMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMachineGroupsResponse(AbstractModel):
    """DescribeConfigMachineGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param MachineGroups: 采集规则配置绑定的机器组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineGroups: list of MachineGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self.MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self.MachineGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> name

按照【采集配置名称】进行过滤。
类型：String

必选：否

<br><li> configId

按照【采集配置ID】进行过滤。
类型：String

必选：否

<br><li> topicId

按照【日志主题】进行过滤。

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
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Configs: 采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param TotalCount: 过滤到的总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Configs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class DescribeLogsetsRequest(AbstractModel):
    """DescribeLogsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> logsetName

按照【日志集名称】进行过滤。
类型：String

必选：否

<br><li> logsetId

按照【日志集ID】进行过滤。
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
        


class DescribeLogsetsResponse(AbstractModel):
    """DescribeLogsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 分页的总数目
        :type TotalCount: int
        :param Logsets: 日志集列表
        :type Logsets: list of LogsetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logsets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logsets") is not None:
            self.Logsets = []
            for item in params.get("Logsets"):
                obj = LogsetInfo()
                obj._deserialize(item)
                self.Logsets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineGroupConfigsRequest(AbstractModel):
    """DescribeMachineGroupConfigs请求参数结构体

    """

    def __init__(self):
        r"""
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
        


class DescribeMachineGroupConfigsResponse(AbstractModel):
    """DescribeMachineGroupConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Configs: 采集规则配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Configs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class DescribeShipperTasksRequest(AbstractModel):
    """DescribeShipperTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        :param StartTime: 查询的开始时间戳，支持最近3天的查询， 毫秒
        :type StartTime: int
        :param EndTime: 查询的结束时间戳， 毫秒
        :type EndTime: int
        """
        self.ShipperId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShipperTasksResponse(AbstractModel):
    """DescribeShipperTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 投递任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ShipperTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ShipperTaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShippersRequest(AbstractModel):
    """DescribeShippers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> shipperName

按照【投递规则名称】进行过滤。
类型：String

必选：否

<br><li> shipperId

按照【投递规则ID】进行过滤。
类型：String

必选：否

<br><li> topicId

按照【日志主题】进行过滤。

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
        


class DescribeShippersResponse(AbstractModel):
    """DescribeShippers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Shippers: 投递规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Shippers: list of ShipperInfo
        :param TotalCount: 本次查询获取到的总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Shippers = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Shippers") is not None:
            self.Shippers = []
            for item in params.get("Shippers"):
                obj = ShipperInfo()
                obj._deserialize(item)
                self.Shippers.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        r"""
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

<br><li> storageType

按照【日志主题的存储类型】进行过滤。可选值 hot（实时存储），cold（离线存储）
类型：String

必选：否


每次请求的Filters的上限为10，Filter.Values的上限为100。
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
        r"""
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


class ExcludePathInfo(AbstractModel):
    """黑名单path信息

    """

    def __init__(self):
        r"""
        :param Type: 类型，选填File或Path
        :type Type: str
        :param Value: Type对应的具体内容
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInfo(AbstractModel):
    """日志导出信息

    """

    def __init__(self):
        r"""
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
        


class ExtractRuleInfo(AbstractModel):
    """日志提取规则

    """

    def __init__(self):
        r"""
        :param TimeKey: 时间字段的key名字，time_key和time_format必须成对出现
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeKey: str
        :param TimeFormat: 时间字段的格式，参考c语言的strftime函数对于时间的格式说明输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param Delimiter: 分隔符类型日志的分隔符，只有log_type为delimiter_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Delimiter: str
        :param LogRegex: 整条日志匹配规则，只有log_type为fullregex_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegex: str
        :param BeginRegex: 行首匹配规则，只有log_type为multiline_log或fullregex_log时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginRegex: str
        :param Keys: 取的每个字段的key名字，为空的key代表丢弃这个字段，只有log_type为delimiter_log时有效，json_log的日志使用json本身的key
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param FilterKeyRegex: 需要过滤日志的key，及其对应的regex
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterKeyRegex: list of KeyRegexInfo
        :param UnMatchUpLoadSwitch: 解析失败日志是否上传，true表示上传，false表示不上传
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchUpLoadSwitch: bool
        :param UnMatchLogKey: 失败日志的key
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchLogKey: str
        :param Backtracking: 增量采集模式下的回溯数据量，默认-1（全量采集）
注意：此字段可能返回 null，表示取不到有效值。
        :type Backtracking: int
        """
        self.TimeKey = None
        self.TimeFormat = None
        self.Delimiter = None
        self.LogRegex = None
        self.BeginRegex = None
        self.Keys = None
        self.FilterKeyRegex = None
        self.UnMatchUpLoadSwitch = None
        self.UnMatchLogKey = None
        self.Backtracking = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.TimeFormat = params.get("TimeFormat")
        self.Delimiter = params.get("Delimiter")
        self.LogRegex = params.get("LogRegex")
        self.BeginRegex = params.get("BeginRegex")
        self.Keys = params.get("Keys")
        if params.get("FilterKeyRegex") is not None:
            self.FilterKeyRegex = []
            for item in params.get("FilterKeyRegex"):
                obj = KeyRegexInfo()
                obj._deserialize(item)
                self.FilterKeyRegex.append(obj)
        self.UnMatchUpLoadSwitch = params.get("UnMatchUpLoadSwitch")
        self.UnMatchLogKey = params.get("UnMatchLogKey")
        self.Backtracking = params.get("Backtracking")
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
        r"""
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
        


class FilterRuleInfo(AbstractModel):
    """投递日志的过滤规则

    """

    def __init__(self):
        r"""
        :param Key: 过滤规则Key
        :type Key: str
        :param Regex: 过滤规则
        :type Regex: str
        :param Value: 过滤规则Value
        :type Value: str
        """
        self.Key = None
        self.Regex = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Regex = params.get("Regex")
        self.Value = params.get("Value")
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
        r"""
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
        r"""
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
        r"""
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


class JsonInfo(AbstractModel):
    """JSON类型描述

    """

    def __init__(self):
        r"""
        :param EnableTag: 启用标志
        :type EnableTag: bool
        :param MetaFields: 元数据信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaFields: list of str
        """
        self.EnableTag = None
        self.MetaFields = None


    def _deserialize(self, params):
        self.EnableTag = params.get("EnableTag")
        self.MetaFields = params.get("MetaFields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRegexInfo(AbstractModel):
    """需要过滤日志的key，及其对应的regex

    """

    def __init__(self):
        r"""
        :param Key: 需要过滤日志的key
        :type Key: str
        :param Regex: key对应的过滤规则regex
        :type Regex: str
        """
        self.Key = None
        self.Regex = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueInfo(AbstractModel):
    """键值或者元字段索引的字段信息

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        


class LogsetInfo(AbstractModel):
    """日志集相关信息

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param LogsetName: 日志集名称
        :type LogsetName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Tags: 日志集绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param TopicCount: 日志集下日志主题的数目
        :type TopicCount: int
        :param RoleName: 若AssumerUin非空，则表示创建该日志集的服务方角色
        :type RoleName: str
        """
        self.LogsetId = None
        self.LogsetName = None
        self.CreateTime = None
        self.Tags = None
        self.TopicCount = None
        self.RoleName = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TopicCount = params.get("TopicCount")
        self.RoleName = params.get("RoleName")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
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
        self.MessageTemplate = None
        self.CallBack = None
        self.Analysis = None


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
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyConfigRequest(AbstractModel):
    """ModifyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigId: 采集规则配置ID
        :type ConfigId: str
        :param Name: 采集规则配置名称
        :type Name: str
        :param Path: 日志采集路径，包含文件名
        :type Path: str
        :param LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param Output: 采集配置关联的日志主题（TopicId）
        :type Output: str
        """
        self.ConfigId = None
        self.Name = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None
        self.Output = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.Name = params.get("Name")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        self.Output = params.get("Output")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigResponse(AbstractModel):
    """ModifyConfig返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLogsetRequest(AbstractModel):
    """ModifyLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param LogsetName: 日志集名称
        :type LogsetName: str
        :param Tags: 日志集的绑定的标签键值对。最大支持10个标签键值对，同一个资源只能同时绑定一个标签键。
        :type Tags: list of Tag
        """
        self.LogsetId = None
        self.LogsetName = None
        self.Tags = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogsetResponse(AbstractModel):
    """ModifyLogset返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyShipperRequest(AbstractModel):
    """ModifyShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        :param Bucket: 投递规则投递的新的bucket
        :type Bucket: str
        :param Prefix: 投递规则投递的新的目录前缀
        :type Prefix: str
        :param Status: 投递规则的开关状态
        :type Status: bool
        :param ShipperName: 投递规则的名字
        :type ShipperName: str
        :param Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 100-256
        :type MaxSize: int
        :param FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        self.ShipperId = None
        self.Bucket = None
        self.Prefix = None
        self.Status = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.Status = params.get("Status")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyShipperResponse(AbstractModel):
    """ModifyShipper返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param Period: 生命周期，单位天；可取值范围1~366
        :type Period: int
        """
        self.TopicId = None
        self.TopicName = None
        self.Tags = None
        self.Status = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.Period = None


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
        self.Period = params.get("Period")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        


class RetryShipperTaskRequest(AbstractModel):
    """RetryShipperTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        :param TaskId: 投递任务ID
        :type TaskId: str
        """
        self.ShipperId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskResponse(AbstractModel):
    """RetryShipperTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """索引规则，FullText、KeyValue、Tag参数必须输入一个有效参数

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param UseNewAnalysis: 为true代表使用新检索,响应参数AnalysisRecords和Columns有效， 为false时代表使用老检索方式, AnalysisResults和ColNames有效
        :type UseNewAnalysis: bool
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None
        self.UseNewAnalysis = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        self.UseNewAnalysis = params.get("UseNewAnalysis")
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
        r"""
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
        :param AnalysisRecords: 新的日志分析结果; UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param Columns: 日志分析的列属性; UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.ColNames = None
        self.Results = None
        self.AnalysisResults = None
        self.AnalysisRecords = None
        self.Columns = None
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
        self.AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.RequestId = params.get("RequestId")


class ShipperInfo(AbstractModel):
    """投递规则

    """

    def __init__(self):
        r"""
        :param ShipperId: 投递规则ID
        :type ShipperId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Bucket: 投递的bucket地址
        :type Bucket: str
        :param Prefix: 投递的前缀目录
        :type Prefix: str
        :param ShipperName: 投递规则的名字
        :type ShipperName: str
        :param Interval: 投递的时间间隔，单位 秒
        :type Interval: int
        :param MaxSize: 投递的文件的最大值，单位 MB
        :type MaxSize: int
        :param Status: 是否生效
        :type Status: bool
        :param FilterRules: 投递日志的过滤规则
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of FilterRuleInfo
        :param Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param Compress: 投递日志的压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: 投递日志的内容格式配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param CreateTime: 投递日志的创建时间
        :type CreateTime: str
        """
        self.ShipperId = None
        self.TopicId = None
        self.Bucket = None
        self.Prefix = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.Status = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.TopicId = params.get("TopicId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        self.Status = params.get("Status")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperTaskInfo(AbstractModel):
    """投递任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 投递任务ID
        :type TaskId: str
        :param ShipperId: 投递信息ID
        :type ShipperId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param RangeStart: 本批投递的日志的开始时间戳，毫秒
        :type RangeStart: int
        :param RangeEnd: 本批投递的日志的结束时间戳， 毫秒
        :type RangeEnd: int
        :param StartTime: 本次投递任务的开始时间戳， 毫秒
        :type StartTime: int
        :param EndTime: 本次投递任务的结束时间戳， 毫秒
        :type EndTime: int
        :param Status: 本次投递的结果，"success","running","failed"
        :type Status: str
        :param Message: 结果的详细信息
        :type Message: str
        """
        self.TaskId = None
        self.ShipperId = None
        self.TopicId = None
        self.RangeStart = None
        self.RangeEnd = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Message = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ShipperId = params.get("ShipperId")
        self.TopicId = params.get("TopicId")
        self.RangeStart = params.get("RangeStart")
        self.RangeEnd = params.get("RangeEnd")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionRequest(AbstractModel):
    """SplitPartition请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param Period: 生命周期，单位为天
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
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
        self.Period = None


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
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogRequest(AbstractModel):
    """UploadLog请求参数结构体

    """


class UploadLogResponse(AbstractModel):
    """UploadLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ValueInfo(AbstractModel):
    """需要开启键值索引的字段的索引描述信息

    """

    def __init__(self):
        r"""
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
        r"""
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
        