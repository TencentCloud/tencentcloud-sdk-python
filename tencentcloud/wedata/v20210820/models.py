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


class AlarmEventInfo(AbstractModel):
    """告警事件详情

    """

    def __init__(self):
        r"""
        :param AlarmId: 告警ID
        :type AlarmId: str
        :param AlarmTime: 告警时间
        :type AlarmTime: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param RegularName: 规则名称
        :type RegularName: str
        :param AlarmLevel: 告警级别,0表示普通，1表示重要，2表示紧急
        :type AlarmLevel: int
        :param AlarmIndicator: 告警指标,0表示任务失败，1表示任务运行超时，2表示任务停止，3表示任务暂停
        :type AlarmIndicator: int
        :param AlarmWay: 告警方式,多个用逗号隔开（1:邮件，2:短信，3:微信，4:语音，5:代表企业微信，6:http）
        :type AlarmWay: int
        :param AlarmRecipientId: 告警接收人Id，多个用逗号隔开
        :type AlarmRecipientId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param AlarmIndicatorDesc: 告警指标描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmIndicatorDesc: str
        :param TriggerType: 指标阈值，1表示离线任务第一次运行失败，2表示离线任务所有重试完成后失败
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: int
        :param EstimatedTime: 预计的超时时间，分钟级别
注意：此字段可能返回 null，表示取不到有效值。
        :type EstimatedTime: int
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param IsSendSuccess: 0：部分成功，1：全部成功，2：全部失败
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSendSuccess: int
        :param MessageId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param Operator: 阈值计算算子，1 : 大于 2 ：小于
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: int
        """
        self.AlarmId = None
        self.AlarmTime = None
        self.TaskId = None
        self.RegularName = None
        self.AlarmLevel = None
        self.AlarmIndicator = None
        self.AlarmWay = None
        self.AlarmRecipientId = None
        self.ProjectId = None
        self.AlarmIndicatorDesc = None
        self.TriggerType = None
        self.EstimatedTime = None
        self.InstanceId = None
        self.TaskName = None
        self.IsSendSuccess = None
        self.MessageId = None
        self.Operator = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.AlarmTime = params.get("AlarmTime")
        self.TaskId = params.get("TaskId")
        self.RegularName = params.get("RegularName")
        self.AlarmLevel = params.get("AlarmLevel")
        self.AlarmIndicator = params.get("AlarmIndicator")
        self.AlarmWay = params.get("AlarmWay")
        self.AlarmRecipientId = params.get("AlarmRecipientId")
        self.ProjectId = params.get("ProjectId")
        self.AlarmIndicatorDesc = params.get("AlarmIndicatorDesc")
        self.TriggerType = params.get("TriggerType")
        self.EstimatedTime = params.get("EstimatedTime")
        self.InstanceId = params.get("InstanceId")
        self.TaskName = params.get("TaskName")
        self.IsSendSuccess = params.get("IsSendSuccess")
        self.MessageId = params.get("MessageId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmInfo(AbstractModel):
    """任务告警信息

    """

    def __init__(self):
        r"""
        :param TaskIds: 关联任务id
        :type TaskIds: str
        :param AlarmType: 告警类别；failure表示失败告警；overtime表示超时告警
        :type AlarmType: str
        :param AlarmWay: 告警方式；SMS表示短信；Email表示邮件；HTTP 表示接口方式；Wechat表示微信方式
        :type AlarmWay: str
        :param AlarmRecipient: 告警接收人，多个告警接收人以;分割
        :type AlarmRecipient: str
        :param AlarmRecipientId: 告警接收人id，多个告警接收人id以;分割
        :type AlarmRecipientId: str
        :param Hours: 预计运行的小时，取值范围0-23
        :type Hours: int
        :param Minutes: 预计运行分钟，取值范围0-59
        :type Minutes: int
        :param TriggerType: 告警出发时机；1表示第一次运行失败；2表示所有重试完成后失败；
        :type TriggerType: int
        :param AlarmId: 告警信息id
        :type AlarmId: str
        :param Status: 告警状态设置；1表示可用；0表示不可用，默认可用
        :type Status: int
        """
        self.TaskIds = None
        self.AlarmType = None
        self.AlarmWay = None
        self.AlarmRecipient = None
        self.AlarmRecipientId = None
        self.Hours = None
        self.Minutes = None
        self.TriggerType = None
        self.AlarmId = None
        self.Status = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.AlarmType = params.get("AlarmType")
        self.AlarmWay = params.get("AlarmWay")
        self.AlarmRecipient = params.get("AlarmRecipient")
        self.AlarmRecipientId = params.get("AlarmRecipientId")
        self.Hours = params.get("Hours")
        self.Minutes = params.get("Minutes")
        self.TriggerType = params.get("TriggerType")
        self.AlarmId = params.get("AlarmId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmReceiverInfo(AbstractModel):
    """告警接收人详情

    """

    def __init__(self):
        r"""
        :param AlarmId: 告警ID
        :type AlarmId: str
        :param AlarmReceiver: 告警接收人ID
        :type AlarmReceiver: str
        :param Email: 邮件，0：未设置，1：成功，2：失败
        :type Email: int
        :param Sms: 短信，0：未设置，1：成功，2：失败
        :type Sms: int
        :param Wechat: 微信，0：未设置，1：成功，2：失败
        :type Wechat: int
        :param Voice: 电话，0：未设置，1：成功，2：失败
        :type Voice: int
        :param Wecom: 企业微信，0：未设置，1：成功，2：失败
        :type Wecom: int
        :param Http: http，0：未设置，1：成功，2：失败
        :type Http: int
        """
        self.AlarmId = None
        self.AlarmReceiver = None
        self.Email = None
        self.Sms = None
        self.Wechat = None
        self.Voice = None
        self.Wecom = None
        self.Http = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.AlarmReceiver = params.get("AlarmReceiver")
        self.Email = params.get("Email")
        self.Sms = params.get("Sms")
        self.Wechat = params.get("Wechat")
        self.Voice = params.get("Voice")
        self.Wecom = params.get("Wecom")
        self.Http = params.get("Http")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateIntegrationTaskAlarmsRequest(AbstractModel):
    """BatchCreateIntegrationTaskAlarms请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskAlarmInfo: 告警配置信息
        :type TaskAlarmInfo: :class:`tencentcloud.wedata.v20210820.models.TaskAlarmInfo`
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskAlarmInfo = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        if params.get("TaskAlarmInfo") is not None:
            self.TaskAlarmInfo = TaskAlarmInfo()
            self.TaskAlarmInfo._deserialize(params.get("TaskAlarmInfo"))
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateIntegrationTaskAlarmsResponse(AbstractModel):
    """BatchCreateIntegrationTaskAlarms返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param TotalCount: 任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchDeleteIntegrationTasksRequest(AbstractModel):
    """BatchDeleteIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteIntegrationTasksResponse(AbstractModel):
    """BatchDeleteIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param TotalCount: 任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchDeleteTasksNewRequest(AbstractModel):
    """BatchDeleteTasksNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIdList: 批量删除的任务TaskId
        :type TaskIdList: list of str
        :param DeleteMode: true : 删除后下游任务可正常运行
false：删除后下游任务不可运行
        :type DeleteMode: bool
        :param EnableNotify: true：通知下游任务责任人
false:  不通知下游任务责任人
        :type EnableNotify: bool
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.TaskIdList = None
        self.DeleteMode = None
        self.EnableNotify = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIdList = params.get("TaskIdList")
        self.DeleteMode = params.get("DeleteMode")
        self.EnableNotify = params.get("EnableNotify")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteTasksNewResponse(AbstractModel):
    """BatchDeleteTasksNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回批量操作成功个数、失败个数、操作总数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class BatchForceSuccessIntegrationTaskInstancesRequest(AbstractModel):
    """BatchForceSuccessIntegrationTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 实例信息
        :type Instances: list of SchedulerTaskInstanceInfo
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.Instances = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = SchedulerTaskInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchForceSuccessIntegrationTaskInstancesResponse(AbstractModel):
    """BatchForceSuccessIntegrationTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchKillIntegrationTaskInstancesRequest(AbstractModel):
    """BatchKillIntegrationTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 实例信息
        :type Instances: list of SchedulerTaskInstanceInfo
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.Instances = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = SchedulerTaskInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchKillIntegrationTaskInstancesResponse(AbstractModel):
    """BatchKillIntegrationTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchMakeUpIntegrationTasksRequest(AbstractModel):
    """BatchMakeUpIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param StartTime: 补数据开始时间
        :type StartTime: str
        :param EndTime: 补数据结束时间
        :type EndTime: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.StartTime = None
        self.EndTime = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchMakeUpIntegrationTasksResponse(AbstractModel):
    """BatchMakeUpIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchModifyOwnersNewRequest(AbstractModel):
    """BatchModifyOwnersNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIdList: 需要更新责任人的TaskId数组
        :type TaskIdList: list of str
        :param Owners: 需要更新的责任人
        :type Owners: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.TaskIdList = None
        self.Owners = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIdList = params.get("TaskIdList")
        self.Owners = params.get("Owners")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyOwnersNewResponse(AbstractModel):
    """BatchModifyOwnersNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回批量操作成功个数、失败个数、操作总数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class BatchOperateResult(AbstractModel):
    """批量操作的结果返回

    """

    def __init__(self):
        r"""
        :param SuccessCount: 批量操作成功数
        :type SuccessCount: int
        :param FailedCount: 批量操作失败数
        :type FailedCount: int
        :param TotalCount: 批量操作的总数
        :type TotalCount: int
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRerunIntegrationTaskInstancesRequest(AbstractModel):
    """BatchRerunIntegrationTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 实例信息
        :type Instances: list of SchedulerTaskInstanceInfo
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.Instances = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = SchedulerTaskInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRerunIntegrationTaskInstancesResponse(AbstractModel):
    """BatchRerunIntegrationTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchResult(AbstractModel):
    """批量操作结果

    """

    def __init__(self):
        r"""
        :param Running: 正在运行的任务数
        :type Running: int
        :param Success: 执行成功的任务数
        :type Success: int
        :param Failed: 执行失败的任务数
        :type Failed: int
        :param Total: 总任务数
        :type Total: int
        """
        self.Running = None
        self.Success = None
        self.Failed = None
        self.Total = None


    def _deserialize(self, params):
        self.Running = params.get("Running")
        self.Success = params.get("Success")
        self.Failed = params.get("Failed")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchResumeIntegrationTasksRequest(AbstractModel):
    """BatchResumeIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchResumeIntegrationTasksResponse(AbstractModel):
    """BatchResumeIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchReturn(AbstractModel):
    """操作结果

    """

    def __init__(self):
        r"""
        :param Result: 执行结果
        :type Result: bool
        :param ErrorDesc: 执行情况备注
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDesc: str
        :param ErrorId: 执行情况id
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorId: str
        """
        self.Result = None
        self.ErrorDesc = None
        self.ErrorId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ErrorDesc = params.get("ErrorDesc")
        self.ErrorId = params.get("ErrorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchStartIntegrationTasksRequest(AbstractModel):
    """BatchStartIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchStartIntegrationTasksResponse(AbstractModel):
    """BatchStartIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchStopIntegrationTasksRequest(AbstractModel):
    """BatchStopIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchStopIntegrationTasksResponse(AbstractModel):
    """BatchStopIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchStopTasksNewRequest(AbstractModel):
    """BatchStopTasksNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIdList: 批量停止任务的TaskId
        :type TaskIdList: list of str
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.TaskIdList = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIdList = params.get("TaskIdList")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchStopTasksNewResponse(AbstractModel):
    """BatchStopTasksNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回批量操作成功个数、失败个数、操作总数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class BatchSuspendIntegrationTasksRequest(AbstractModel):
    """BatchSuspendIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSuspendIntegrationTasksResponse(AbstractModel):
    """BatchSuspendIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BatchUpdateIntegrationTasksRequest(AbstractModel):
    """BatchUpdateIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务id
        :type TaskIds: list of str
        :param Incharge: 责任人（多个责任人用小写分号隔开；离线任务传入的是账号名，实时任务传入的是账号id）
        :type Incharge: str
        :param TaskType: 任务类型
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskIds = None
        self.Incharge = None
        self.TaskType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.Incharge = params.get("Incharge")
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateIntegrationTasksResponse(AbstractModel):
    """BatchUpdateIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCount: 操作成功的任务数
        :type SuccessCount: int
        :param FailedCount: 操作失败的任务数
        :type FailedCount: int
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.FailedCount = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        self.FailedCount = params.get("FailedCount")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class BytesSpeed(AbstractModel):
    """实时任务同步速度 字节/s

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param Values: 速度值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of SpeedValue
        """
        self.NodeType = None
        self.NodeName = None
        self.Values = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeName = params.get("NodeName")
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = SpeedValue()
                obj._deserialize(item)
                self.Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CanvasInfo(AbstractModel):
    """画布所需的信息

    """

    def __init__(self):
        r"""
        :param TasksList: 画布任务信息
        :type TasksList: list of TaskCanvasInfo
        :param LinksList: 画布任务链接信息
        :type LinksList: list of TaskLinkInfo
        """
        self.TasksList = None
        self.LinksList = None


    def _deserialize(self, params):
        if params.get("TasksList") is not None:
            self.TasksList = []
            for item in params.get("TasksList"):
                obj = TaskCanvasInfo()
                obj._deserialize(item)
                self.TasksList.append(obj)
        if params.get("LinksList") is not None:
            self.LinksList = []
            for item in params.get("LinksList"):
                obj = TaskLinkInfo()
                obj._deserialize(item)
                self.LinksList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAlarmRegularNameExistRequest(AbstractModel):
    """CheckAlarmRegularNameExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目名称
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param AlarmRegularName: 规则名称
        :type AlarmRegularName: str
        :param Id: 主键ID
        :type Id: str
        """
        self.ProjectId = None
        self.TaskId = None
        self.AlarmRegularName = None
        self.Id = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.AlarmRegularName = params.get("AlarmRegularName")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAlarmRegularNameExistResponse(AbstractModel):
    """CheckAlarmRegularNameExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否重名
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CheckDuplicateRuleNameRequest(AbstractModel):
    """CheckDuplicateRuleName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param RuleGroupId: 规则组Id
        :type RuleGroupId: int
        :param Name: 规则名称
        :type Name: str
        :param RuleId: 规则Id
        :type RuleId: int
        """
        self.ProjectId = None
        self.RuleGroupId = None
        self.Name = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.Name = params.get("Name")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDuplicateRuleNameResponse(AbstractModel):
    """CheckDuplicateRuleName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则名称是否重复
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CheckDuplicateTemplateNameRequest(AbstractModel):
    """CheckDuplicateTemplateName请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 规则模板ID
        :type TemplateId: int
        :param Name: 模板名称
        :type Name: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.TemplateId = None
        self.Name = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDuplicateTemplateNameResponse(AbstractModel):
    """CheckDuplicateTemplateName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否重名
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CheckIntegrationNodeNameExistsRequest(AbstractModel):
    """CheckIntegrationNodeNameExists请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param Name: 节点名称
        :type Name: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Id: 节点ID
        :type Id: int
        """
        self.TaskId = None
        self.Name = None
        self.ProjectId = None
        self.Id = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntegrationNodeNameExistsResponse(AbstractModel):
    """CheckIntegrationNodeNameExists返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回true代表存在，返回false代表不存在
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CheckIntegrationTaskNameExistsRequest(AbstractModel):
    """CheckIntegrationTaskNameExists请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskName: 任务名称
        :type TaskName: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param SyncType: 同步类型1.单表同步，2.解决方案
        :type SyncType: int
        """
        self.TaskName = None
        self.ProjectId = None
        self.TaskId = None
        self.SyncType = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.SyncType = params.get("SyncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntegrationTaskNameExistsResponse(AbstractModel):
    """CheckIntegrationTaskNameExists返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: true表示存在，false表示不存在
        :type Data: bool
        :param ExistsType: 任务名重复类型（0:未重复, 1:开发态重复, 2:生产态重复）
        :type ExistsType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.ExistsType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.ExistsType = params.get("ExistsType")
        self.RequestId = params.get("RequestId")


class CheckTaskNameExistRequest(AbstractModel):
    """CheckTaskNameExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id/工作空间id
        :type ProjectId: str
        :param TypeId: 任务类型（跟调度传参保持一致27）
        :type TypeId: int
        :param TaskName: 任务名
        :type TaskName: str
        """
        self.ProjectId = None
        self.TypeId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TypeId = params.get("TypeId")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTaskNameExistResponse(AbstractModel):
    """CheckTaskNameExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CommitExportTaskRequest(AbstractModel):
    """CommitExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleExecId: 规则执行Id
        :type RuleExecId: int
        :param ExportType: 导出类型(1.全部,2.触发行,3.通过行)
        :type ExportType: int
        :param ExecutorGroupId: 执行资源组id
        :type ExecutorGroupId: str
        :param QueueName: 计算资源队列
        :type QueueName: str
        """
        self.ProjectId = None
        self.RuleExecId = None
        self.ExportType = None
        self.ExecutorGroupId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleExecId = params.get("RuleExecId")
        self.ExportType = params.get("ExportType")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitExportTaskResponse(AbstractModel):
    """CommitExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 提交结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CommitIntegrationTaskRequest(AbstractModel):
    """CommitIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param CommitType: 0.仅提交，1.立即启动，2.停止线上作业，丢弃作业状态数据，重新启动运行，3.暂停线上作业，保留作业状态数据，继续运行，4.保留作业状态数据，继续运行
        :type CommitType: int
        :param TaskType: 实时任务 201   离线任务 202  默认实时任务
        :type TaskType: int
        """
        self.TaskId = None
        self.ProjectId = None
        self.CommitType = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.CommitType = params.get("CommitType")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitIntegrationTaskResponse(AbstractModel):
    """CommitIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CommitRuleGroupExecResultRequest(AbstractModel):
    """CommitRuleGroupExecResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: preject id
        :type ProjectId: str
        :param RuleGroupExecId: rule group exec id
        :type RuleGroupExecId: int
        :param RuleGroupState: group exec state
        :type RuleGroupState: str
        :param RuleExecResults: runner rule exec result list
        :type RuleExecResults: list of RunnerRuleExecResult
        """
        self.ProjectId = None
        self.RuleGroupExecId = None
        self.RuleGroupState = None
        self.RuleExecResults = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        self.RuleGroupState = params.get("RuleGroupState")
        if params.get("RuleExecResults") is not None:
            self.RuleExecResults = []
            for item in params.get("RuleExecResults"):
                obj = RunnerRuleExecResult()
                obj._deserialize(item)
                self.RuleExecResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitRuleGroupExecResultResponse(AbstractModel):
    """CommitRuleGroupExecResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CommitRuleGroupTaskRequest(AbstractModel):
    """CommitRuleGroupTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param TriggerType: 触发类型 1.手动触发 2.调度事中触发 3.周期调度触发
        :type TriggerType: int
        :param ExecRuleConfig: 规则配置列表
        :type ExecRuleConfig: list of RuleConfig
        :param ExecConfig: 执行配置
        :type ExecConfig: :class:`tencentcloud.wedata.v20210820.models.RuleExecConfig`
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.RuleGroupId = None
        self.TriggerType = None
        self.ExecRuleConfig = None
        self.ExecConfig = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.TriggerType = params.get("TriggerType")
        if params.get("ExecRuleConfig") is not None:
            self.ExecRuleConfig = []
            for item in params.get("ExecRuleConfig"):
                obj = RuleConfig()
                obj._deserialize(item)
                self.ExecRuleConfig.append(obj)
        if params.get("ExecConfig") is not None:
            self.ExecConfig = RuleExecConfig()
            self.ExecConfig._deserialize(params.get("ExecConfig"))
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitRuleGroupTaskResponse(AbstractModel):
    """CommitRuleGroupTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组执行id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupExecResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupExecResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CommonContent(AbstractModel):
    """内容详情

    """

    def __init__(self):
        r"""
        :param Content: 详情内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonId(AbstractModel):
    """Id包装对象

    """

    def __init__(self):
        r"""
        :param Id: Id值
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareResult(AbstractModel):
    """质量检查对比结果

    """

    def __init__(self):
        r"""
        :param Items: 对比结果项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of CompareResultItem
        :param TotalRows: 检测总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRows: int
        :param PassRows: 检测通过行数
注意：此字段可能返回 null，表示取不到有效值。
        :type PassRows: int
        :param TriggerRows: 检测不通过行数
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerRows: int
        """
        self.Items = None
        self.TotalRows = None
        self.PassRows = None
        self.TriggerRows = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CompareResultItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalRows = params.get("TotalRows")
        self.PassRows = params.get("PassRows")
        self.TriggerRows = params.get("TriggerRows")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareResultItem(AbstractModel):
    """对比结果项

    """

    def __init__(self):
        r"""
        :param FixResult: 对比结果， 1为真 2为假
注意：此字段可能返回 null，表示取不到有效值。
        :type FixResult: int
        :param ResultValue: 质量sql执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultValue: str
        :param Values: 阈值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of ThresholdValue
        :param Operator: 比较操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param CompareType: 比较类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareType: int
        :param ValueComputeType: 值比较类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueComputeType: int
        """
        self.FixResult = None
        self.ResultValue = None
        self.Values = None
        self.Operator = None
        self.CompareType = None
        self.ValueComputeType = None


    def _deserialize(self, params):
        self.FixResult = params.get("FixResult")
        self.ResultValue = params.get("ResultValue")
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = ThresholdValue()
                obj._deserialize(item)
                self.Values.append(obj)
        self.Operator = params.get("Operator")
        self.CompareType = params.get("CompareType")
        self.ValueComputeType = params.get("ValueComputeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareRule(AbstractModel):
    """对比规则

    """

    def __init__(self):
        r"""
        :param Items: 比较条件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of CompareRuleItem
        :param CycleStep: 周期性模板默认周期，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStep: int
        """
        self.Items = None
        self.CycleStep = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CompareRuleItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.CycleStep = params.get("CycleStep")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareRuleItem(AbstractModel):
    """比较条件

    """

    def __init__(self):
        r"""
        :param CompareType: 比较类型 1.固定值  2.波动值  3.数值范围比较  4.枚举范围比较  5.不用比较
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareType: int
        :param Operator: 比较操作类型 <  <=  ==  =>  >
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param ValueComputeType: 质量统计值类型 1.绝对值  2.上升 3. 下降  4._C包含   5. N_C不包含
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueComputeType: int
        :param ValueList: 比较阈值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueList: list of ThresholdValue
        """
        self.CompareType = None
        self.Operator = None
        self.ValueComputeType = None
        self.ValueList = None


    def _deserialize(self, params):
        self.CompareType = params.get("CompareType")
        self.Operator = params.get("Operator")
        self.ValueComputeType = params.get("ValueComputeType")
        if params.get("ValueList") is not None:
            self.ValueList = []
            for item in params.get("ValueList"):
                obj = ThresholdValue()
                obj._deserialize(item)
                self.ValueList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomFunctionRequest(AbstractModel):
    """CreateCustomFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 类型：HIVE、SPARK
        :type Type: str
        :param Kind: 分类：窗口函数、聚合函数、日期函数......
        :type Kind: str
        :param Name: 函数名称
        :type Name: str
        :param ClusterIdentifier: 集群实例引擎 ID
        :type ClusterIdentifier: str
        :param DbName: 数据库名称
        :type DbName: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.Type = None
        self.Kind = None
        self.Name = None
        self.ClusterIdentifier = None
        self.DbName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        self.ClusterIdentifier = params.get("ClusterIdentifier")
        self.DbName = params.get("DbName")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomFunctionResponse(AbstractModel):
    """CreateCustomFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionId: str
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionId = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class CreateDataSourceRequest(AbstractModel):
    """CreateDataSource请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 数据源名称，在相同SpaceName下，数据源名称不能为空
        :type Name: str
        :param Category: 数据源类别：绑定引擎、绑定数据库
        :type Category: str
        :param Type: 数据源类型:枚举值
        :type Type: str
        :param OwnerProjectId: 归属项目ID
        :type OwnerProjectId: str
        :param OwnerProjectName: 归属项目Name
        :type OwnerProjectName: str
        :param OwnerProjectIdent: 归属项目Name中文
        :type OwnerProjectIdent: str
        :param BizParams: 业务侧数据源的配置信息扩展
        :type BizParams: str
        :param Params: 数据源的配置信息，以JSON KV存储，根据每个数据源类型不同，而KV存储信息不同
        :type Params: str
        :param Description: 数据源描述信息
        :type Description: str
        :param Display: 数据源展示名，为了可视化查看
        :type Display: str
        :param DatabaseName: 若数据源列表为绑定数据库，则为db名称
        :type DatabaseName: str
        :param Instance: 数据源引擎的实例ID，如CDB实例ID
        :type Instance: str
        :param Status: 数据源数据源的可见性，1为可见、0为不可见。默认为1
        :type Status: int
        :param ClusterId: 数据源所属的业务空间名称
        :type ClusterId: str
        :param Collect: 是否采集
        :type Collect: str
        :param COSBucket: cos桶信息
        :type COSBucket: str
        :param COSRegion: cos region
        :type COSRegion: str
        """
        self.Name = None
        self.Category = None
        self.Type = None
        self.OwnerProjectId = None
        self.OwnerProjectName = None
        self.OwnerProjectIdent = None
        self.BizParams = None
        self.Params = None
        self.Description = None
        self.Display = None
        self.DatabaseName = None
        self.Instance = None
        self.Status = None
        self.ClusterId = None
        self.Collect = None
        self.COSBucket = None
        self.COSRegion = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Category = params.get("Category")
        self.Type = params.get("Type")
        self.OwnerProjectId = params.get("OwnerProjectId")
        self.OwnerProjectName = params.get("OwnerProjectName")
        self.OwnerProjectIdent = params.get("OwnerProjectIdent")
        self.BizParams = params.get("BizParams")
        self.Params = params.get("Params")
        self.Description = params.get("Description")
        self.Display = params.get("Display")
        self.DatabaseName = params.get("DatabaseName")
        self.Instance = params.get("Instance")
        self.Status = params.get("Status")
        self.ClusterId = params.get("ClusterId")
        self.Collect = params.get("Collect")
        self.COSBucket = params.get("COSBucket")
        self.COSRegion = params.get("COSRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataSourceResponse(AbstractModel):
    """CreateDataSource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 主键ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateFolderRequest(AbstractModel):
    """CreateFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param FolderName: 文件夹名称
        :type FolderName: str
        :param ParentsFolderId: 父文件夹ID
        :type ParentsFolderId: str
        """
        self.ProjectId = None
        self.FolderName = None
        self.ParentsFolderId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.FolderName = params.get("FolderName")
        self.ParentsFolderId = params.get("ParentsFolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFolderResponse(AbstractModel):
    """CreateFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 文件夹Id，null则创建失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.CommonId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CommonId()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateHiveTableByDDLRequest(AbstractModel):
    """CreateHiveTableByDDL请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceId: 数据源ID
        :type DatasourceId: str
        :param Database: 数据库
        :type Database: str
        :param DDLSql: 建hive表ddl
        :type DDLSql: str
        :param Privilege: 表权限 ，默认为0:项目共享;1:仅个人与管理员
        :type Privilege: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Type: 目标表类型(HIVE或GBASE)
        :type Type: str
        :param Incharge: 责任人
        :type Incharge: str
        """
        self.DatasourceId = None
        self.Database = None
        self.DDLSql = None
        self.Privilege = None
        self.ProjectId = None
        self.Type = None
        self.Incharge = None


    def _deserialize(self, params):
        self.DatasourceId = params.get("DatasourceId")
        self.Database = params.get("Database")
        self.DDLSql = params.get("DDLSql")
        self.Privilege = params.get("Privilege")
        self.ProjectId = params.get("ProjectId")
        self.Type = params.get("Type")
        self.Incharge = params.get("Incharge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHiveTableByDDLResponse(AbstractModel):
    """CreateHiveTableByDDL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 表名称
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateHiveTableRequest(AbstractModel):
    """CreateHiveTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceId: 数据源id
        :type DatasourceId: str
        :param Database: 数据库
        :type Database: str
        :param DDLSql: 建hive表ddl
        :type DDLSql: str
        :param Privilege: 表权限 ，默认为0:项目共享;1:仅个人与管理员
        :type Privilege: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Incharge: 责任人
        :type Incharge: str
        """
        self.DatasourceId = None
        self.Database = None
        self.DDLSql = None
        self.Privilege = None
        self.ProjectId = None
        self.Incharge = None


    def _deserialize(self, params):
        self.DatasourceId = params.get("DatasourceId")
        self.Database = params.get("Database")
        self.DDLSql = params.get("DDLSql")
        self.Privilege = params.get("Privilege")
        self.ProjectId = params.get("ProjectId")
        self.Incharge = params.get("Incharge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHiveTableResponse(AbstractModel):
    """CreateHiveTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsSuccess: 建表是否成功
        :type IsSuccess: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class CreateInLongAgentRequest(AbstractModel):
    """CreateInLongAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentType: 采集器类型，1：TKE Agent，2：BOSS SDK，默认：1
        :type AgentType: int
        :param AgentName: 采集器名称
        :type AgentName: str
        :param ExecutorGroupId: 集成资源组id
        :type ExecutorGroupId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param TkeRegion: TKE集群的地域
        :type TkeRegion: str
        :param ClusterId: 当AgentType为1时，必填。当AgentType为2时，不用填
        :type ClusterId: str
        """
        self.AgentType = None
        self.AgentName = None
        self.ExecutorGroupId = None
        self.ProjectId = None
        self.TkeRegion = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.AgentType = params.get("AgentType")
        self.AgentName = params.get("AgentName")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.ProjectId = params.get("ProjectId")
        self.TkeRegion = params.get("TkeRegion")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInLongAgentResponse(AbstractModel):
    """CreateInLongAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 采集器ID
        :type AgentId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AgentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.RequestId = params.get("RequestId")


class CreateIntegrationNodeRequest(AbstractModel):
    """CreateIntegrationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeInfo: 集成节点信息
        :type NodeInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationNodeInfo`
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型
        :type TaskType: int
        """
        self.NodeInfo = None
        self.ProjectId = None
        self.TaskType = None


    def _deserialize(self, params):
        if params.get("NodeInfo") is not None:
            self.NodeInfo = IntegrationNodeInfo()
            self.NodeInfo._deserialize(params.get("NodeInfo"))
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntegrationNodeResponse(AbstractModel):
    """CreateIntegrationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 节点
        :type Id: str
        :param TaskId: 当前任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateIntegrationTaskRequest(AbstractModel):
    """CreateIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationTaskInfo`
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskInfo = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = IntegrationTaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntegrationTaskResponse(AbstractModel):
    """CreateIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateOfflineTaskRequest(AbstractModel):
    """CreateOfflineTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目/工作
        :type ProjectId: str
        :param CycleStep: 1
        :type CycleStep: int
        :param DelayTime: 0
        :type DelayTime: int
        :param EndTime: 2099-12-31 00:00:00
        :type EndTime: str
        :param Notes: 备注
        :type Notes: str
        :param StartTime: 当前日期
        :type StartTime: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param TypeId: 跟之前调用调度接口保持一致27
        :type TypeId: int
        :param TaskAction: 默认 ""
        :type TaskAction: str
        :param TaskMode: 区分画布和表单
        :type TaskMode: str
        """
        self.ProjectId = None
        self.CycleStep = None
        self.DelayTime = None
        self.EndTime = None
        self.Notes = None
        self.StartTime = None
        self.TaskName = None
        self.TypeId = None
        self.TaskAction = None
        self.TaskMode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CycleStep = params.get("CycleStep")
        self.DelayTime = params.get("DelayTime")
        self.EndTime = params.get("EndTime")
        self.Notes = params.get("Notes")
        self.StartTime = params.get("StartTime")
        self.TaskName = params.get("TaskName")
        self.TypeId = params.get("TypeId")
        self.TaskAction = params.get("TaskAction")
        self.TaskMode = params.get("TaskMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineTaskResponse(AbstractModel):
    """CreateOfflineTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateOrUpdateResourceRequest(AbstractModel):
    """CreateOrUpdateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Files: 文件名
        :type Files: list of str
        :param FilePath: 文件所属路径，资源管理根路径为 /datastudio/resouce
        :type FilePath: str
        :param CosBucketName: cos存储桶名字
        :type CosBucketName: str
        :param CosRegion: cos所属地域
        :type CosRegion: str
        :param NewFile: 是否为新文件，新增为 true，更新为 false
        :type NewFile: bool
        :param FilesSize: 文件大小
        :type FilesSize: list of str
        """
        self.ProjectId = None
        self.Files = None
        self.FilePath = None
        self.CosBucketName = None
        self.CosRegion = None
        self.NewFile = None
        self.FilesSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Files = params.get("Files")
        self.FilePath = params.get("FilePath")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.NewFile = params.get("NewFile")
        self.FilesSize = params.get("FilesSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrUpdateResourceResponse(AbstractModel):
    """CreateOrUpdateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of UserFileDTO
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = UserFileDTO()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateResourcePathRequest(AbstractModel):
    """CreateResourcePath请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 文件夹名称，如 aaa
        :type Name: str
        :param FilePath: 文件夹所属父目录，请注意，根目录为 /datastudio/resource
        :type FilePath: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.Name = None
        self.FilePath = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FilePath = params.get("FilePath")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourcePathResponse(AbstractModel):
    """CreateResourcePath返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 新建成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleGroupId: 规则组Id
        :type RuleGroupId: int
        :param Name: 规则名称
        :type Name: str
        :param TableId: 数据表ID
        :type TableId: str
        :param RuleTemplateId: 规则模板列表
        :type RuleTemplateId: int
        :param Type: 规则类型 1.系统模版, 2.自定义模版, 3.自定义SQL
        :type Type: int
        :param QualityDim: 规则所属质量维度（1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
        :type QualityDim: int
        :param SourceObjectDataTypeName: 源字段详细类型，int、string
        :type SourceObjectDataTypeName: str
        :param SourceObjectValue: 源字段名称
        :type SourceObjectValue: str
        :param ConditionType: 检测范围 1.全表   2.条件扫描
        :type ConditionType: int
        :param ConditionExpression: 条件扫描WHERE条件表达式
        :type ConditionExpression: str
        :param CustomSql: 自定义SQL
        :type CustomSql: str
        :param CompareRule: 报警触发条件
        :type CompareRule: :class:`tencentcloud.wedata.v20210820.models.CompareRule`
        :param AlarmLevel: 报警触发级别 1.低, 2.中, 3.高
        :type AlarmLevel: int
        :param Description: 规则描述
        :type Description: str
        :param DatasourceId: 数据源Id
        :type DatasourceId: str
        :param DatabaseId: 数据库Id
        :type DatabaseId: str
        :param TargetDatabaseId: 目标库Id
        :type TargetDatabaseId: str
        :param TargetTableId: 目标表Id
        :type TargetTableId: str
        :param TargetConditionExpr: 目标过滤条件表达式
        :type TargetConditionExpr: str
        :param RelConditionExpr: 源字段与目标字段关联条件on表达式
        :type RelConditionExpr: str
        :param FieldConfig: 自定义模版sql表达式字段替换参数
        :type FieldConfig: :class:`tencentcloud.wedata.v20210820.models.RuleFieldConfig`
        :param TargetObjectValue: 目标字段名称  CITY
        :type TargetObjectValue: str
        """
        self.ProjectId = None
        self.RuleGroupId = None
        self.Name = None
        self.TableId = None
        self.RuleTemplateId = None
        self.Type = None
        self.QualityDim = None
        self.SourceObjectDataTypeName = None
        self.SourceObjectValue = None
        self.ConditionType = None
        self.ConditionExpression = None
        self.CustomSql = None
        self.CompareRule = None
        self.AlarmLevel = None
        self.Description = None
        self.DatasourceId = None
        self.DatabaseId = None
        self.TargetDatabaseId = None
        self.TargetTableId = None
        self.TargetConditionExpr = None
        self.RelConditionExpr = None
        self.FieldConfig = None
        self.TargetObjectValue = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.Name = params.get("Name")
        self.TableId = params.get("TableId")
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.Type = params.get("Type")
        self.QualityDim = params.get("QualityDim")
        self.SourceObjectDataTypeName = params.get("SourceObjectDataTypeName")
        self.SourceObjectValue = params.get("SourceObjectValue")
        self.ConditionType = params.get("ConditionType")
        self.ConditionExpression = params.get("ConditionExpression")
        self.CustomSql = params.get("CustomSql")
        if params.get("CompareRule") is not None:
            self.CompareRule = CompareRule()
            self.CompareRule._deserialize(params.get("CompareRule"))
        self.AlarmLevel = params.get("AlarmLevel")
        self.Description = params.get("Description")
        self.DatasourceId = params.get("DatasourceId")
        self.DatabaseId = params.get("DatabaseId")
        self.TargetDatabaseId = params.get("TargetDatabaseId")
        self.TargetTableId = params.get("TargetTableId")
        self.TargetConditionExpr = params.get("TargetConditionExpr")
        self.RelConditionExpr = params.get("RelConditionExpr")
        if params.get("FieldConfig") is not None:
            self.FieldConfig = RuleFieldConfig()
            self.FieldConfig._deserialize(params.get("FieldConfig"))
        self.TargetObjectValue = params.get("TargetObjectValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Rule()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateRuleTemplateRequest(AbstractModel):
    """CreateRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 模版类型  1.系统模版   2.自定义模版
        :type Type: int
        :param Name: 模版名称
        :type Name: str
        :param QualityDim: 质量检测维度 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性
        :type QualityDim: int
        :param SourceObjectType: 源端数据对象类型 1.常量  2.离线表级   2.离线字段级
        :type SourceObjectType: int
        :param Description: 模板描述
        :type Description: str
        :param SourceEngineTypes: 源端对应的引擎类型
        :type SourceEngineTypes: list of int non-negative
        :param MultiSourceFlag: 是否关联其它库表
        :type MultiSourceFlag: bool
        :param SqlExpression: SQL 表达式
        :type SqlExpression: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WhereFlag: 是否添加where参数
        :type WhereFlag: bool
        """
        self.Type = None
        self.Name = None
        self.QualityDim = None
        self.SourceObjectType = None
        self.Description = None
        self.SourceEngineTypes = None
        self.MultiSourceFlag = None
        self.SqlExpression = None
        self.ProjectId = None
        self.WhereFlag = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.QualityDim = params.get("QualityDim")
        self.SourceObjectType = params.get("SourceObjectType")
        self.Description = params.get("Description")
        self.SourceEngineTypes = params.get("SourceEngineTypes")
        self.MultiSourceFlag = params.get("MultiSourceFlag")
        self.SqlExpression = params.get("SqlExpression")
        self.ProjectId = params.get("ProjectId")
        self.WhereFlag = params.get("WhereFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleTemplateResponse(AbstractModel):
    """CreateRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 模板Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateTaskAlarmRegularRequest(AbstractModel):
    """CreateTaskAlarmRegular请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskAlarmInfo: 告警配置信息
        :type TaskAlarmInfo: :class:`tencentcloud.wedata.v20210820.models.TaskAlarmInfo`
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.TaskAlarmInfo = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("TaskAlarmInfo") is not None:
            self.TaskAlarmInfo = TaskAlarmInfo()
            self.TaskAlarmInfo._deserialize(params.get("TaskAlarmInfo"))
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskAlarmRegularResponse(AbstractModel):
    """CreateTaskAlarmRegular返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmId: 告警ID
        :type AlarmId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param TaskName: 任务名
        :type TaskName: str
        :param TaskType: 26离线同步，30Python，31PySpark，32DLC，33Impala，34Hive SQL，35Shell，36Spark SQL，39Spark，40CDW PG，92MapReduce
        :type TaskType: int
        :param TaskExt: 扩展属性
        :type TaskExt: list of TaskExtInfo
        """
        self.ProjectId = None
        self.WorkflowId = None
        self.TaskName = None
        self.TaskType = None
        self.TaskExt = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        self.TaskName = params.get("TaskName")
        self.TaskType = params.get("TaskType")
        if params.get("TaskExt") is not None:
            self.TaskExt = []
            for item in params.get("TaskExt"):
                obj = TaskExtInfo()
                obj._deserialize(item)
                self.TaskExt.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.CommonId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CommonId()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowName: 工作流名称
        :type WorkflowName: str
        :param FolderId: 所属文件夹id
        :type FolderId: str
        """
        self.ProjectId = None
        self.WorkflowName = None
        self.FolderId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowName = params.get("WorkflowName")
        self.FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回工作流Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.CommonId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CommonId()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CvmAgentStatus(AbstractModel):
    """采集器状态统计

    """

    def __init__(self):
        r"""
        :param Status: agent状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Count: 对应状态的agent总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.Status = None
        self.Count = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DailyScoreInfo(AbstractModel):
    """日评分信息

    """

    def __init__(self):
        r"""
        :param StatisticsDate: 统计日期 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticsDate: int
        :param Score: 评分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.StatisticsDate = None
        self.Score = None


    def _deserialize(self, params):
        self.StatisticsDate = params.get("StatisticsDate")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCheckStat(AbstractModel):
    """数据监测情况结果

    """

    def __init__(self):
        r"""
        :param TableTotal: 表总数
        :type TableTotal: int
        :param ColumnTotal: 字段总数
        :type ColumnTotal: int
        :param TableConfig: 表配置检测数
        :type TableConfig: int
        :param ColumnConfig: 字段配置检测数
        :type ColumnConfig: int
        :param TableExec: 表实际检测数
        :type TableExec: int
        :param ColumnExec: 字段实际检测数
        :type ColumnExec: int
        """
        self.TableTotal = None
        self.ColumnTotal = None
        self.TableConfig = None
        self.ColumnConfig = None
        self.TableExec = None
        self.ColumnExec = None


    def _deserialize(self, params):
        self.TableTotal = params.get("TableTotal")
        self.ColumnTotal = params.get("ColumnTotal")
        self.TableConfig = params.get("TableConfig")
        self.ColumnConfig = params.get("ColumnConfig")
        self.TableExec = params.get("TableExec")
        self.ColumnExec = params.get("ColumnExec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceInfo(AbstractModel):
    """数据源对象

    """

    def __init__(self):
        r"""
        :param DatabaseName: 若数据源列表为绑定数据库，则为db名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param Description: 数据源描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param ID: 数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Instance: 数据源引擎的实例ID，如CDB实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: str
        :param Name: 数据源名称，在相同SpaceName下，数据源名称不能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Region: 数据源引擎所属区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Type: 数据源类型:枚举值
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ClusterId: 数据源所属的集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param AppId: 应用ID AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param BizParams: 业务侧数据源的配置信息扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type BizParams: str
        :param Category: 数据源类别：绑定引擎、绑定数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param Display: 数据源展示名，为了可视化查看
注意：此字段可能返回 null，表示取不到有效值。
        :type Display: str
        :param OwnerAccount: 数据源责任人账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerAccount: str
        :param Params: 数据源的配置信息，以JSON KV存储，根据每个数据源类型不同，而KV存储信息不同
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param Status: 数据源数据源的可见性，1为可见、0为不可见。默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param OwnerAccountName: 数据源责任人账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerAccountName: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param OwnerProjectId: 归属项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerProjectId: str
        :param OwnerProjectName: 归属项目Name
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerProjectName: str
        :param OwnerProjectIdent: 归属项目标识
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerProjectIdent: str
        :param AuthorityProjectName: 授权项目
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorityProjectName: str
        :param AuthorityUserName: 授权用户
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorityUserName: str
        :param Edit: 是否有编辑权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Edit: bool
        :param Author: 是否有授权权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Author: bool
        :param Deliver: 是否有转交权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Deliver: bool
        :param DataSourceStatus: 数据源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceStatus: str
        :param CreateTime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param ParamsString: Params json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamsString: str
        :param BizParamsString: BizParams json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type BizParamsString: str
        """
        self.DatabaseName = None
        self.Description = None
        self.ID = None
        self.Instance = None
        self.Name = None
        self.Region = None
        self.Type = None
        self.ClusterId = None
        self.AppId = None
        self.BizParams = None
        self.Category = None
        self.Display = None
        self.OwnerAccount = None
        self.Params = None
        self.Status = None
        self.OwnerAccountName = None
        self.ClusterName = None
        self.OwnerProjectId = None
        self.OwnerProjectName = None
        self.OwnerProjectIdent = None
        self.AuthorityProjectName = None
        self.AuthorityUserName = None
        self.Edit = None
        self.Author = None
        self.Deliver = None
        self.DataSourceStatus = None
        self.CreateTime = None
        self.ParamsString = None
        self.BizParamsString = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Description = params.get("Description")
        self.ID = params.get("ID")
        self.Instance = params.get("Instance")
        self.Name = params.get("Name")
        self.Region = params.get("Region")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")
        self.AppId = params.get("AppId")
        self.BizParams = params.get("BizParams")
        self.Category = params.get("Category")
        self.Display = params.get("Display")
        self.OwnerAccount = params.get("OwnerAccount")
        self.Params = params.get("Params")
        self.Status = params.get("Status")
        self.OwnerAccountName = params.get("OwnerAccountName")
        self.ClusterName = params.get("ClusterName")
        self.OwnerProjectId = params.get("OwnerProjectId")
        self.OwnerProjectName = params.get("OwnerProjectName")
        self.OwnerProjectIdent = params.get("OwnerProjectIdent")
        self.AuthorityProjectName = params.get("AuthorityProjectName")
        self.AuthorityUserName = params.get("AuthorityUserName")
        self.Edit = params.get("Edit")
        self.Author = params.get("Author")
        self.Deliver = params.get("Deliver")
        self.DataSourceStatus = params.get("DataSourceStatus")
        self.CreateTime = params.get("CreateTime")
        self.ParamsString = params.get("ParamsString")
        self.BizParamsString = params.get("BizParamsString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceInfoPage(AbstractModel):
    """查询数据源分页列表

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param PageSize: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Rows: 数据源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rows: list of DataSourceInfo
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param TotalPageNumber: 总分页页码
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        """
        self.PageNumber = None
        self.PageSize = None
        self.Rows = None
        self.TotalCount = None
        self.TotalPageNumber = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = DataSourceInfo()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseInfo(AbstractModel):
    """数据质量数据来源数据库

    """

    def __init__(self):
        r"""
        :param DatasourceName: 数据源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceName: str
        :param DatasourceId: 数据源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param DatabaseId: 数据库id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param DatasourceType: 数据源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceType: int
        :param OriginDatabaseName: 数据库原始名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginDatabaseName: str
        :param OriginSchemaName: schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginSchemaName: str
        """
        self.DatasourceName = None
        self.DatasourceId = None
        self.DatabaseName = None
        self.DatabaseId = None
        self.InstanceId = None
        self.DatasourceType = None
        self.OriginDatabaseName = None
        self.OriginSchemaName = None


    def _deserialize(self, params):
        self.DatasourceName = params.get("DatasourceName")
        self.DatasourceId = params.get("DatasourceId")
        self.DatabaseName = params.get("DatabaseName")
        self.DatabaseId = params.get("DatabaseId")
        self.InstanceId = params.get("InstanceId")
        self.DatasourceType = params.get("DatasourceType")
        self.OriginDatabaseName = params.get("OriginDatabaseName")
        self.OriginSchemaName = params.get("OriginSchemaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceBaseInfo(AbstractModel):
    """数据源对象

    """

    def __init__(self):
        r"""
        :param DatabaseNames: 若数据源列表为绑定数据库，则为db名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNames: list of str
        :param Description: 数据源描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param ID: 数据源ID
        :type ID: int
        :param Instance: 数据源引擎的实例ID，如CDB实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: str
        :param Name: 数据源名称，在相同SpaceName下，数据源名称不能为空
        :type Name: str
        :param Region: 数据源引擎所属区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Type: 数据源类型:枚举值
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ClusterId: 数据源所属的集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self.DatabaseNames = None
        self.Description = None
        self.ID = None
        self.Instance = None
        self.Name = None
        self.Region = None
        self.Type = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.DatabaseNames = params.get("DatabaseNames")
        self.Description = params.get("Description")
        self.ID = params.get("ID")
        self.Instance = params.get("Instance")
        self.Name = params.get("Name")
        self.Region = params.get("Region")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomFunctionRequest(AbstractModel):
    """DeleteCustomFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIdentifier: 集群实例 ID
        :type ClusterIdentifier: str
        :param FunctionId: 函数 ID
        :type FunctionId: str
        :param ProjectId: 项目ID，必须填
        :type ProjectId: str
        """
        self.ClusterIdentifier = None
        self.FunctionId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ClusterIdentifier = params.get("ClusterIdentifier")
        self.FunctionId = params.get("FunctionId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomFunctionResponse(AbstractModel):
    """DeleteCustomFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionId: str
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionId = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DeleteDataSourcesRequest(AbstractModel):
    """DeleteDataSources请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: id列表
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDataSourcesResponse(AbstractModel):
    """DeleteDataSources返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否删除成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteFolderRequest(AbstractModel):
    """DeleteFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param FolderId: 文件夹ID
        :type FolderId: str
        """
        self.ProjectId = None
        self.FolderId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFolderResponse(AbstractModel):
    """DeleteFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: true代表删除成功，false代表删除失败
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteInLongAgentRequest(AbstractModel):
    """DeleteInLongAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 采集器ID
        :type AgentId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        """
        self.AgentId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInLongAgentResponse(AbstractModel):
    """DeleteInLongAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIntegrationNodeRequest(AbstractModel):
    """DeleteIntegrationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 节点id
        :type Id: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.Id = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntegrationNodeResponse(AbstractModel):
    """DeleteIntegrationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 删除返回是否成功标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteIntegrationTaskRequest(AbstractModel):
    """DeleteIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntegrationTaskResponse(AbstractModel):
    """DeleteIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 任务删除成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteOfflineTaskRequest(AbstractModel):
    """DeleteOfflineTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param OperatorName: 操作者name
        :type OperatorName: str
        :param ProjectId: 项目/工作空间id
        :type ProjectId: str
        :param TaskId: 任务id
        :type TaskId: str
        :param VirtualFlag: 虚拟任务标记(跟之前调度接口保持一致默认false)
        :type VirtualFlag: bool
        """
        self.OperatorName = None
        self.ProjectId = None
        self.TaskId = None
        self.VirtualFlag = None


    def _deserialize(self, params):
        self.OperatorName = params.get("OperatorName")
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.VirtualFlag = params.get("VirtualFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineTaskResponse(AbstractModel):
    """DeleteOfflineTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteResourceRequest(AbstractModel):
    """DeleteResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ResourceId: 资源ID
        :type ResourceId: str
        """
        self.ProjectId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceResponse(AbstractModel):
    """DeleteResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 质量规则ID
        :type RuleId: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.RuleId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否删除成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteRuleTemplateRequest(AbstractModel):
    """DeleteRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Ids: 模版Id列表
        :type Ids: list of int non-negative
        """
        self.ProjectId = None
        self.Ids = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleTemplateResponse(AbstractModel):
    """DeleteRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 删除成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteTaskAlarmRegularRequest(AbstractModel):
    """DeleteTaskAlarmRegular请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 主键ID
        :type Id: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskType: 任务类型(201表示实时任务，202表示离线任务)
        :type TaskType: int
        """
        self.Id = None
        self.ProjectId = None
        self.TaskId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskAlarmRegularResponse(AbstractModel):
    """DeleteTaskAlarmRegular返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 删除结果(true表示删除成功，false表示删除失败)
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteWorkflowNewRequest(AbstractModel):
    """DeleteWorkflowNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkFlowId: 工作流id
        :type WorkFlowId: str
        :param DeleteMode: true : 删除后下游任务可正常运行
false：删除后下游任务不可运行
        :type DeleteMode: bool
        :param EnableNotify: true：通知下游任务责任人
false:  不通知下游任务责任人
        :type EnableNotify: bool
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.WorkFlowId = None
        self.DeleteMode = None
        self.EnableNotify = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.WorkFlowId = params.get("WorkFlowId")
        self.DeleteMode = params.get("DeleteMode")
        self.EnableNotify = params.get("EnableNotify")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowNewResponse(AbstractModel):
    """DeleteWorkflowNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回删除结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DependencyConfig(AbstractModel):
    """依赖配置

    """

    def __init__(self):
        r"""
        :param DependConfType: 仅五种周期运行依赖配置： HOUR,DAY,WEEK,MONTH,YEAR,CRONTAB,MINUTE
        :type DependConfType: str
        :param SubordinateCyclicType: 依赖配置从属周期类型，CURRENT_HOUR，PREVIOUS_HOUR，CURRENT_DAY，PREVIOUS_DAY，PREVIOUS_WEEK，PREVIOUS_FRIDAY，PREVIOUS_WEEKEND，CURRENT_MONTH，PREVIOUS_MONTH，PREVIOUS_END_OF_MONTH
     * PREVIOUS_BEGIN_OF_MONTH，ALL_MONTH_OF_YEAR，ALL_DAY_OF_YEAR，CURRENT_YEAR，CURRENT，CURRENT_MINUTE，PREVIOUS_MINUTE_CYCLE，PREVIOUS_HOUR_CYCLE
        :type SubordinateCyclicType: str
        :param DependencyStrategy: WAITING，等待（默认策略）EXECUTING:执行
        :type DependencyStrategy: str
        :param ParentTask: 父任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentTask: :class:`tencentcloud.wedata.v20210820.models.TaskInnerInfo`
        :param SonTask: 子任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SonTask: :class:`tencentcloud.wedata.v20210820.models.TaskInnerInfo`
        """
        self.DependConfType = None
        self.SubordinateCyclicType = None
        self.DependencyStrategy = None
        self.ParentTask = None
        self.SonTask = None


    def _deserialize(self, params):
        self.DependConfType = params.get("DependConfType")
        self.SubordinateCyclicType = params.get("SubordinateCyclicType")
        self.DependencyStrategy = params.get("DependencyStrategy")
        if params.get("ParentTask") is not None:
            self.ParentTask = TaskInnerInfo()
            self.ParentTask._deserialize(params.get("ParentTask"))
        if params.get("SonTask") is not None:
            self.SonTask = TaskInnerInfo()
            self.SonTask._deserialize(params.get("SonTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmEventsRequest(AbstractModel):
    """DescribeAlarmEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件(key可以是：AlarmLevel,AlarmIndicator,KeyWord)
        :type Filters: list of Filter
        :param OrderFields: 排序字段（AlarmTime）
        :type OrderFields: list of OrderField
        :param TaskType: 类型(201表示实时，202表示离线)
        :type TaskType: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param PageNumber: 当前页
        :type PageNumber: int
        :param PageSize: 每页记录数
        :type PageSize: int
        """
        self.Filters = None
        self.OrderFields = None
        self.TaskType = None
        self.StartTime = None
        self.EndTime = None
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.TaskType = params.get("TaskType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmEventsResponse(AbstractModel):
    """DescribeAlarmEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmEventInfoList: 告警事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmEventInfoList: list of AlarmEventInfo
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmEventInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmEventInfoList") is not None:
            self.AlarmEventInfoList = []
            for item in params.get("AlarmEventInfoList"):
                obj = AlarmEventInfo()
                obj._deserialize(item)
                self.AlarmEventInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAlarmReceiverRequest(AbstractModel):
    """DescribeAlarmReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmId: 告警ID
        :type AlarmId: str
        :param PageNumber: 当前页
        :type PageNumber: int
        :param PageSize: 每页记录数
        :type PageSize: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param MessageId: 消息ID
        :type MessageId: str
        :param TaskType: 类型
        :type TaskType: int
        :param AlarmRecipient: 告警接收人ID(逗号分隔)
        :type AlarmRecipient: str
        :param AlarmRecipientName: 告警接收人姓名(逗号分隔)
        :type AlarmRecipientName: str
        :param AlarmTime: 告警时间
        :type AlarmTime: str
        """
        self.AlarmId = None
        self.PageNumber = None
        self.PageSize = None
        self.ProjectId = None
        self.MessageId = None
        self.TaskType = None
        self.AlarmRecipient = None
        self.AlarmRecipientName = None
        self.AlarmTime = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        self.MessageId = params.get("MessageId")
        self.TaskType = params.get("TaskType")
        self.AlarmRecipient = params.get("AlarmRecipient")
        self.AlarmRecipientName = params.get("AlarmRecipientName")
        self.AlarmTime = params.get("AlarmTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmReceiverResponse(AbstractModel):
    """DescribeAlarmReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmReceiverInfoList: 告警接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmReceiverInfoList: list of AlarmReceiverInfo
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmReceiverInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmReceiverInfoList") is not None:
            self.AlarmReceiverInfoList = []
            for item in params.get("AlarmReceiverInfoList"):
                obj = AlarmReceiverInfo()
                obj._deserialize(item)
                self.AlarmReceiverInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterNamespaceListRequest(AbstractModel):
    """DescribeClusterNamespaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        """
        self.ClusterId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNamespaceListResponse(AbstractModel):
    """DescribeClusterNamespaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Namespaces: 命名空间
        :type Namespaces: list of Namespace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Namespaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataBasesRequest(AbstractModel):
    """DescribeDataBases请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param DatasourceId: 数据源id
        :type DatasourceId: str
        :param DsTypes: 数据源类型
        :type DsTypes: list of int non-negative
        """
        self.ProjectId = None
        self.DatasourceId = None
        self.DsTypes = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DatasourceId = params.get("DatasourceId")
        self.DsTypes = params.get("DsTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBasesResponse(AbstractModel):
    """DescribeDataBases返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据来源数据数据库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DatabaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DatabaseInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataCheckStatRequest(AbstractModel):
    """DescribeDataCheckStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: Project id
        :type ProjectId: str
        :param BeginDate: 开始时间，时间戳到秒
        :type BeginDate: str
        :param EndDate: 结束时间，时间戳到秒
        :type EndDate: str
        """
        self.ProjectId = None
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCheckStatResponse(AbstractModel):
    """DescribeDataCheckStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DataCheckStat`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataCheckStat()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDataObjectsRequest(AbstractModel):
    """DescribeDataObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceId: 数据来源ID
        :type DatasourceId: str
        :param TableId: 数据表ID
        :type TableId: str
        :param RuleGroupId: 质量规则组ID
        :type RuleGroupId: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.DatasourceId = None
        self.TableId = None
        self.RuleGroupId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DatasourceId = params.get("DatasourceId")
        self.TableId = params.get("TableId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataObjectsResponse(AbstractModel):
    """DescribeDataObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SourceObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceObject()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataSourceInfoListRequest(AbstractModel):
    """DescribeDataSourceInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 工作空间id
        :type ProjectId: str
        :param PageNumber: 页码
        :type PageNumber: int
        :param PageSize: 页数
        :type PageSize: int
        :param Filters: 可选过滤条件，Filter可选配置(参考): "Name": { "type": "string", "description": "数据源名称" }, "Type": { "type": "string", "description": "类型" }, "ClusterId": { "type": "string", "description": "集群id" }, "CategoryId": { "type": "string", "description": "分类，项目或空间id" }
        :type Filters: :class:`tencentcloud.wedata.v20210820.models.Filter`
        :param OrderFields: 排序配置
        :type OrderFields: :class:`tencentcloud.wedata.v20210820.models.OrderField`
        :param Type: 数据源类型
        :type Type: str
        :param DatasourceName: 数据源名称过滤用
        :type DatasourceName: str
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.Type = None
        self.DatasourceName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))
        if params.get("OrderFields") is not None:
            self.OrderFields = OrderField()
            self.OrderFields._deserialize(params.get("OrderFields"))
        self.Type = params.get("Type")
        self.DatasourceName = params.get("DatasourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSourceInfoListResponse(AbstractModel):
    """DescribeDataSourceInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数。
        :type TotalCount: int
        :param DatasourceSet: 数据源信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceSet: list of DatasourceBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DatasourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DatasourceSet") is not None:
            self.DatasourceSet = []
            for item in params.get("DatasourceSet"):
                obj = DatasourceBaseInfo()
                obj._deserialize(item)
                self.DatasourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataSourceListRequest(AbstractModel):
    """DescribeDataSourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 页码
        :type PageNumber: int
        :param PageSize: 返回数量
        :type PageSize: int
        :param OrderFields: 排序配置
        :type OrderFields: list of OrderField
        :param Filters: 可选过滤条件，Filter可选配置(参考): "Name": { "type": "string", "description": "数据源名称" }, "Type": { "type": "string", "description": "类型" }, "ClusterId": { "type": "string", "description": "集群id" }, "CategoryId": { "type": "string", "description": "分类，项目或空间id" }
        :type Filters: list of Filter
        """
        self.PageNumber = None
        self.PageSize = None
        self.OrderFields = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
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
        


class DescribeDataSourceListResponse(AbstractModel):
    """DescribeDataSourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DataSourceInfoPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataSourceInfoPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDataSourceWithoutInfoRequest(AbstractModel):
    """DescribeDataSourceWithoutInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrderFields: 1
        :type OrderFields: list of OrderField
        :param Filters: 1
        :type Filters: list of Filter
        """
        self.OrderFields = None
        self.Filters = None


    def _deserialize(self, params):
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
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
        


class DescribeDataSourceWithoutInfoResponse(AbstractModel):
    """DescribeDataSourceWithoutInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DataSourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataSourceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataTypesRequest(AbstractModel):
    """DescribeDataTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceType: 数据源类型，MYSQL|KAFKA等
        :type DatasourceType: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        """
        self.DatasourceType = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DatasourceType = params.get("DatasourceType")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataTypesResponse(AbstractModel):
    """DescribeDataTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param TypeInfoSet: 字段类型列表。
        :type TypeInfoSet: list of Label
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TypeInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TypeInfoSet") is not None:
            self.TypeInfoSet = []
            for item in params.get("TypeInfoSet"):
                obj = Label()
                obj._deserialize(item)
                self.TypeInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseInfoListRequest(AbstractModel):
    """DescribeDatabaseInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConnectionType: 如果是hive这里写rpc，如果是其他类型不传
        :type ConnectionType: str
        """
        self.ConnectionType = None


    def _deserialize(self, params):
        self.ConnectionType = params.get("ConnectionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseInfoListResponse(AbstractModel):
    """DescribeDatabaseInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDatasourceRequest(AbstractModel):
    """DescribeDatasource请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 对象唯一ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasourceResponse(AbstractModel):
    """DescribeDatasource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据源对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DataSourceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataSourceInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDependTasksNewRequest(AbstractModel):
    """DescribeDependTasksNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param Deep: 上游/下游层级1-6级
        :type Deep: int
        :param Up: 1: 表示查询上游节点；0:表示查询下游节点；2：表示查询上游和下游节点
        :type Up: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param WorkflowId: 任务工作流id
        :type WorkflowId: str
        """
        self.TaskId = None
        self.Deep = None
        self.Up = None
        self.ProjectId = None
        self.WorkflowId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Deep = params.get("Deep")
        self.Up = params.get("Up")
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDependTasksNewResponse(AbstractModel):
    """DescribeDependTasksNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 画布任务和链接信息
        :type Data: :class:`tencentcloud.wedata.v20210820.models.CanvasInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CanvasInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDimensionScoreRequest(AbstractModel):
    """DescribeDimensionScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsDate: 统计日期 时间戳
        :type StatisticsDate: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param DatasourceId: 数据来源id
        :type DatasourceId: str
        """
        self.StatisticsDate = None
        self.ProjectId = None
        self.DatasourceId = None


    def _deserialize(self, params):
        self.StatisticsDate = params.get("StatisticsDate")
        self.ProjectId = params.get("ProjectId")
        self.DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDimensionScoreResponse(AbstractModel):
    """DescribeDimensionScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 维度评分
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DimensionScore`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DimensionScore()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeExecStrategyRequest(AbstractModel):
    """DescribeExecStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组Id
        :type RuleGroupId: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.RuleGroupId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExecStrategyResponse(AbstractModel):
    """DescribeExecStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupExecStrategy`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupExecStrategy()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFolderListData(AbstractModel):
    """文件夹分页信息

    """

    def __init__(self):
        r"""
        :param Items: 文件夹信息列表
        :type Items: list of Folder
        :param TotalCount: 总条数
        :type TotalCount: int
        :param PageNumber: 页号
        :type PageNumber: int
        :param PageSize: 页大小
        :type PageSize: int
        """
        self.Items = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Folder()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFolderListRequest(AbstractModel):
    """DescribeFolderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param ParentsFolderId: 文件夹ID
        :type ParentsFolderId: str
        :param KeyWords: 关键字
        :type KeyWords: str
        :param PageNumber: 页码，默认1
        :type PageNumber: int
        :param PageSize: 页大小，默认10
        :type PageSize: int
        """
        self.ProjectId = None
        self.ParentsFolderId = None
        self.KeyWords = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ParentsFolderId = params.get("ParentsFolderId")
        self.KeyWords = params.get("KeyWords")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFolderListResponse(AbstractModel):
    """DescribeFolderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeFolderListData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFolderWorkflowListData(AbstractModel):
    """文件夹分页信息

    """

    def __init__(self):
        r"""
        :param Items: 工作流信息列表
        :type Items: list of Workflow
        :param TotalCount: 总条数
        :type TotalCount: int
        :param PageNumber: 页号
        :type PageNumber: int
        :param PageSize: 页大小
        :type PageSize: int
        """
        self.Items = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Workflow()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFolderWorkflowListRequest(AbstractModel):
    """DescribeFolderWorkflowList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param ParentsFolderId: 父文件夹ID
        :type ParentsFolderId: str
        :param KeyWords: 关键字
        :type KeyWords: str
        :param PageNumber: 页码，默认1
        :type PageNumber: int
        :param PageSize: 页大小，默认10
        :type PageSize: int
        """
        self.ProjectId = None
        self.ParentsFolderId = None
        self.KeyWords = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ParentsFolderId = params.get("ParentsFolderId")
        self.KeyWords = params.get("KeyWords")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFolderWorkflowListResponse(AbstractModel):
    """DescribeFolderWorkflowList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeFolderWorkflowListData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFunctionKindsRequest(AbstractModel):
    """DescribeFunctionKinds请求参数结构体

    """


class DescribeFunctionKindsResponse(AbstractModel):
    """DescribeFunctionKinds返回参数结构体

    """

    def __init__(self):
        r"""
        :param Kinds: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Kinds: list of FunctionTypeOrKind
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Kinds = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Kinds") is not None:
            self.Kinds = []
            for item in params.get("Kinds"):
                obj = FunctionTypeOrKind()
                obj._deserialize(item)
                self.Kinds.append(obj)
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DescribeFunctionTypesRequest(AbstractModel):
    """DescribeFunctionTypes请求参数结构体

    """


class DescribeFunctionTypesResponse(AbstractModel):
    """DescribeFunctionTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Types: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Types: list of FunctionTypeOrKind
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Types = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Types") is not None:
            self.Types = []
            for item in params.get("Types"):
                obj = FunctionTypeOrKind()
                obj._deserialize(item)
                self.Types.append(obj)
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DescribeInLongAgentListRequest(AbstractModel):
    """DescribeInLongAgentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param AgentId: 采集器ID
        :type AgentId: str
        :param AgentName: Agent Name
        :type AgentName: str
        :param AgentType: 集群类型，1：TKE Agent，2：BOSS SDK，默认：1，3：CVM，4：自建服务器 【传多个用逗号分割】
        :type AgentType: int
        :param Status: Agent状态(running运行中，initializing 操作中，failed心跳异常)
        :type Status: str
        :param VpcId: Vpc Id
        :type VpcId: str
        :param PageIndex: 分页页码，从1开始，默认：1
        :type PageIndex: int
        :param PageSize: 分页每页记录数，默认10
        :type PageSize: int
        :param Like: 名称搜索是否开启模糊匹配，1：开启，0：不开启（精确匹配）
        :type Like: int
        :param AgentTypes: agent类型【多个用逗号分隔】
        :type AgentTypes: str
        """
        self.ProjectId = None
        self.AgentId = None
        self.AgentName = None
        self.AgentType = None
        self.Status = None
        self.VpcId = None
        self.PageIndex = None
        self.PageSize = None
        self.Like = None
        self.AgentTypes = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.AgentType = params.get("AgentType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.Like = params.get("Like")
        self.AgentTypes = params.get("AgentTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInLongAgentListResponse(AbstractModel):
    """DescribeInLongAgentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 采集器信息列表
        :type Items: list of InLongAgentDetail
        :param PageIndex: 页码
        :type PageIndex: int
        :param PageSize: 每页记录数
        :type PageSize: int
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param TotalPage: 总页数
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.PageIndex = None
        self.PageSize = None
        self.TotalCount = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InLongAgentDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeInLongAgentTaskListRequest(AbstractModel):
    """DescribeInLongAgentTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 采集器ID
        :type AgentId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        """
        self.AgentId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInLongAgentTaskListResponse(AbstractModel):
    """DescribeInLongAgentTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 采集器关联的集成任务列表
        :type Items: list of InLongAgentTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InLongAgentTask()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInLongAgentVpcListRequest(AbstractModel):
    """DescribeInLongAgentVpcList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInLongAgentVpcListResponse(AbstractModel):
    """DescribeInLongAgentVpcList返回参数结构体

    """

    def __init__(self):
        r"""
        :param VpcList: VPC列表
        :type VpcList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VpcList = params.get("VpcList")
        self.RequestId = params.get("RequestId")


class DescribeInLongTkeClusterListRequest(AbstractModel):
    """DescribeInLongTkeClusterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param TkeRegion: TKE集群地域
        :type TkeRegion: str
        :param ClusterName: 集群名称。
多个名称用逗号连接。
        :type ClusterName: str
        :param Status: TKE集群状态 (Running 运行中 Creating 创建中 Initializing 创建中 Idling 闲置中 Abnormal 异常 Failed 异常 Terminating 删除中 Deleting 删除中 Scaling 规模调整中 Upgrading 升级中 Isolated 欠费隔离中 NodeUpgrading 节点升级中 Recovering 唤醒中 Activating 激活中 MasterScaling Master扩缩容中 Waiting 等待注册 ClusterLevelUpgrading 调整规格中 ResourceIsolate 隔离中 ResourceIsolated 已隔离 ResourceReverse 冲正中 Trading 集群开通中 ResourceReversal 集群冲正 ClusterLevelTrading 集群变配交易中)
多个状态用逗号连接。
        :type Status: str
        :param HasAgent: 是否安装Agent，true: 是，false: 否
        :type HasAgent: bool
        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。
多个集群用逗号连接。
        :type ClusterType: str
        :param PageIndex: 分页页码，从1开始，默认：1
        :type PageIndex: int
        :param PageSize: 分页每页记录数，默认10
        :type PageSize: int
        """
        self.ProjectId = None
        self.TkeRegion = None
        self.ClusterName = None
        self.Status = None
        self.HasAgent = None
        self.ClusterType = None
        self.PageIndex = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TkeRegion = params.get("TkeRegion")
        self.ClusterName = params.get("ClusterName")
        self.Status = params.get("Status")
        self.HasAgent = params.get("HasAgent")
        self.ClusterType = params.get("ClusterType")
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInLongTkeClusterListResponse(AbstractModel):
    """DescribeInLongTkeClusterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: TKE集群信息
        :type Items: list of InLongTkeDetail
        :param PageIndex: 页码
        :type PageIndex: int
        :param PageSize: 每页记录数
        :type PageSize: int
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param TotalPage: 总页数
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.PageIndex = None
        self.PageSize = None
        self.TotalCount = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InLongTkeDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeInstanceLastLogRequest(AbstractModel):
    """DescribeInstanceLastLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        """
        self.TaskId = None
        self.CurRunDate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLastLogResponse(AbstractModel):
    """DescribeInstanceLastLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 日志
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目/工作空间id
        :type ProjectId: str
        :param PageIndex: 页码
        :type PageIndex: int
        :param PageSize: 页大小
        :type PageSize: int
        :param CycleList: 周期列表（如天，一次性），可选
        :type CycleList: list of str
        :param OwnerList: 责任人
        :type OwnerList: list of str
        :param InstanceType: 跟之前保持一致
        :type InstanceType: str
        :param Sort: 排序顺序（asc，desc）
        :type Sort: str
        :param SortCol: 排序列（costTime 运行耗时，startTime 开始时间，state 实例状态，curRunDate 数据时间）
        :type SortCol: str
        :param TaskTypeList: 类型列表（如35 shell任务），可选
        :type TaskTypeList: list of int
        :param StateList: 状态列表（如成功 2，正在执行 1），可选
        :type StateList: list of int
        :param Keyword: 任务名称
        :type Keyword: str
        """
        self.ProjectId = None
        self.PageIndex = None
        self.PageSize = None
        self.CycleList = None
        self.OwnerList = None
        self.InstanceType = None
        self.Sort = None
        self.SortCol = None
        self.TaskTypeList = None
        self.StateList = None
        self.Keyword = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.CycleList = params.get("CycleList")
        self.OwnerList = params.get("OwnerList")
        self.InstanceType = params.get("InstanceType")
        self.Sort = params.get("Sort")
        self.SortCol = params.get("SortCol")
        self.TaskTypeList = params.get("TaskTypeList")
        self.StateList = params.get("StateList")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogListRequest(AbstractModel):
    """DescribeInstanceLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        """
        self.TaskId = None
        self.CurRunDate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogListResponse(AbstractModel):
    """DescribeInstanceLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 日志列表
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogRequest(AbstractModel):
    """DescribeInstanceLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        :param BrokerIp: 服务器Ip
        :type BrokerIp: str
        :param OriginFileName: 文件Name
        :type OriginFileName: str
        """
        self.TaskId = None
        self.CurRunDate = None
        self.BrokerIp = None
        self.OriginFileName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.BrokerIp = params.get("BrokerIp")
        self.OriginFileName = params.get("OriginFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogResponse(AbstractModel):
    """DescribeInstanceLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回结果
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        """
        self.ProjectId = None
        self.TaskId = None
        self.CurRunDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of InstanceLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param PageNumber: 页数
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
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
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: Json 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationNodeRequest(AbstractModel):
    """DescribeIntegrationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 节点id
        :type Id: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型
        :type TaskType: int
        """
        self.Id = None
        self.ProjectId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationNodeResponse(AbstractModel):
    """DescribeIntegrationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeInfo: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationNodeInfo`
        :param SourceCheckFlag: 上游节点是否已经修改。true 已修改，需要提示；false 没有修改
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCheckFlag: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeInfo = None
        self.SourceCheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeInfo") is not None:
            self.NodeInfo = IntegrationNodeInfo()
            self.NodeInfo._deserialize(params.get("NodeInfo"))
        self.SourceCheckFlag = params.get("SourceCheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsAgentStatusRequest(AbstractModel):
    """DescribeIntegrationStatisticsAgentStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        :param ExecutorGroupId: 资源组id
        :type ExecutorGroupId: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsAgentStatusResponse(AbstractModel):
    """DescribeIntegrationStatisticsAgentStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatusData: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatusData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StatusData = params.get("StatusData")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsInstanceTrendRequest(AbstractModel):
    """DescribeIntegrationStatisticsInstanceTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        :param ExecutorGroupId: 资源组id
        :type ExecutorGroupId: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsInstanceTrendResponse(AbstractModel):
    """DescribeIntegrationStatisticsInstanceTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrendsData: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TrendsData: list of IntegrationStatisticsTrendResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrendsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrendsData") is not None:
            self.TrendsData = []
            for item in params.get("TrendsData"):
                obj = IntegrationStatisticsTrendResult()
                obj._deserialize(item)
                self.TrendsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsRecordsTrendRequest(AbstractModel):
    """DescribeIntegrationStatisticsRecordsTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsRecordsTrendResponse(AbstractModel):
    """DescribeIntegrationStatisticsRecordsTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrendsData: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TrendsData: list of IntegrationStatisticsTrendResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrendsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrendsData") is not None:
            self.TrendsData = []
            for item in params.get("TrendsData"):
                obj = IntegrationStatisticsTrendResult()
                obj._deserialize(item)
                self.TrendsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsRequest(AbstractModel):
    """DescribeIntegrationStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsResponse(AbstractModel):
    """DescribeIntegrationStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalTask: 总任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTask: int
        :param ProdTask: 生产态任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProdTask: int
        :param DevTask: 开发态任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type DevTask: int
        :param TotalReadRecords: 总读取条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalReadRecords: int
        :param TotalWriteRecords: 总写入条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalWriteRecords: int
        :param TotalErrorRecords: 总脏数据条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalErrorRecords: int
        :param TotalAlarmEvent: 总告警事件数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAlarmEvent: int
        :param IncreaseReadRecords: 当天读取增长条数
注意：此字段可能返回 null，表示取不到有效值。
        :type IncreaseReadRecords: int
        :param IncreaseWriteRecords: 当天写入增长条数
注意：此字段可能返回 null，表示取不到有效值。
        :type IncreaseWriteRecords: int
        :param IncreaseErrorRecords: 当天脏数据增长条数
注意：此字段可能返回 null，表示取不到有效值。
        :type IncreaseErrorRecords: int
        :param IncreaseAlarmEvent: 当天告警事件增长数
注意：此字段可能返回 null，表示取不到有效值。
        :type IncreaseAlarmEvent: int
        :param AlarmEvent: 告警事件统计
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmEvent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalTask = None
        self.ProdTask = None
        self.DevTask = None
        self.TotalReadRecords = None
        self.TotalWriteRecords = None
        self.TotalErrorRecords = None
        self.TotalAlarmEvent = None
        self.IncreaseReadRecords = None
        self.IncreaseWriteRecords = None
        self.IncreaseErrorRecords = None
        self.IncreaseAlarmEvent = None
        self.AlarmEvent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalTask = params.get("TotalTask")
        self.ProdTask = params.get("ProdTask")
        self.DevTask = params.get("DevTask")
        self.TotalReadRecords = params.get("TotalReadRecords")
        self.TotalWriteRecords = params.get("TotalWriteRecords")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        self.TotalAlarmEvent = params.get("TotalAlarmEvent")
        self.IncreaseReadRecords = params.get("IncreaseReadRecords")
        self.IncreaseWriteRecords = params.get("IncreaseWriteRecords")
        self.IncreaseErrorRecords = params.get("IncreaseErrorRecords")
        self.IncreaseAlarmEvent = params.get("IncreaseAlarmEvent")
        self.AlarmEvent = params.get("AlarmEvent")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsTaskStatusRequest(AbstractModel):
    """DescribeIntegrationStatisticsTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        :param ExecutorGroupId: 资源组id
        :type ExecutorGroupId: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsTaskStatusResponse(AbstractModel):
    """DescribeIntegrationStatisticsTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatusData: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatusData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StatusData = params.get("StatusData")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationStatisticsTaskStatusTrendRequest(AbstractModel):
    """DescribeIntegrationStatisticsTaskStatusTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型（实时：201，离线：202）
        :type TaskType: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param QueryDate: 查询日期
        :type QueryDate: str
        :param ExecutorGroupId: 资源组id
        :type ExecutorGroupId: str
        """
        self.TaskType = None
        self.ProjectId = None
        self.QueryDate = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProjectId = params.get("ProjectId")
        self.QueryDate = params.get("QueryDate")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationStatisticsTaskStatusTrendResponse(AbstractModel):
    """DescribeIntegrationStatisticsTaskStatusTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrendsData: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TrendsData: list of IntegrationStatisticsTrendResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrendsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrendsData") is not None:
            self.TrendsData = []
            for item in params.get("TrendsData"):
                obj = IntegrationStatisticsTrendResult()
                obj._deserialize(item)
                self.TrendsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntegrationTaskRequest(AbstractModel):
    """DescribeIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型：201. stream,   202. offline
        :type TaskType: int
        """
        self.TaskId = None
        self.ProjectId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationTaskResponse(AbstractModel):
    """DescribeIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationTaskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = IntegrationTaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeIntegrationTasksRequest(AbstractModel):
    """DescribeIntegrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param PageNumber: 分页第n页
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 查询filter
        :type Filters: list of Filter
        :param OrderFields: 排序字段信息
        :type OrderFields: list of OrderField
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskType: 201. stream, 202. offline 默认实时
        :type TaskType: int
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.StartTime = None
        self.EndTime = None
        self.TaskType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationTasksResponse(AbstractModel):
    """DescribeIntegrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfoSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfoSet: list of IntegrationTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfoSet") is not None:
            self.TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = IntegrationTaskInfo()
                obj._deserialize(item)
                self.TaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntegrationVersionNodesInfoRequest(AbstractModel):
    """DescribeIntegrationVersionNodesInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskVersionPath: task version path
        :type TaskVersionPath: str
        :param TaskVersion: task version
        :type TaskVersion: str
        """
        self.TaskId = None
        self.ProjectId = None
        self.TaskVersionPath = None
        self.TaskVersion = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.TaskVersionPath = params.get("TaskVersionPath")
        self.TaskVersion = params.get("TaskVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationVersionNodesInfoResponse(AbstractModel):
    """DescribeIntegrationVersionNodesInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Nodes: 任务节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of IntegrationNodeInfo
        :param Mappings: 任务映射信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Mappings: list of IntegrationNodeMapping
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Nodes = None
        self.Mappings = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = IntegrationNodeInfo()
                obj._deserialize(item)
                self.Nodes.append(obj)
        if params.get("Mappings") is not None:
            self.Mappings = []
            for item in params.get("Mappings"):
                obj = IntegrationNodeMapping()
                obj._deserialize(item)
                self.Mappings.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeKafkaTopicInfoRequest(AbstractModel):
    """DescribeKafkaTopicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceId: 数据源id
        :type DatasourceId: str
        :param Type: 数据源类型
        :type Type: str
        """
        self.DatasourceId = None
        self.Type = None


    def _deserialize(self, params):
        self.DatasourceId = params.get("DatasourceId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaTopicInfoResponse(AbstractModel):
    """DescribeKafkaTopicInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMonitorsByPageRequest(AbstractModel):
    """DescribeMonitorsByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OrderFields: 排序条件
        :type OrderFields: list of OrderField
        :param PageNumber: 分页序号
        :type PageNumber: int
        """
        self.ProjectId = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorsByPageResponse(AbstractModel):
    """DescribeMonitorsByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 分页查询结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupMonitorPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupMonitorPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeOfflineTaskTokenRequest(AbstractModel):
    """DescribeOfflineTaskToken请求参数结构体

    """


class DescribeOfflineTaskTokenResponse(AbstractModel):
    """DescribeOfflineTaskToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Token: 长连接临时token
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationalFunctionsRequest(AbstractModel):
    """DescribeOrganizationalFunctions请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 场景类型：开发、使用
        :type Type: str
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param Name: 函数名称
        :type Name: str
        :param DisplayName: 展示名称
        :type DisplayName: str
        """
        self.Type = None
        self.ProjectId = None
        self.Name = None
        self.DisplayName = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.DisplayName = params.get("DisplayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationalFunctionsResponse(AbstractModel):
    """DescribeOrganizationalFunctions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of OrganizationalFunction
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = OrganizationalFunction()
                obj._deserialize(item)
                self.Content.append(obj)
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DescribeProdTasksRequest(AbstractModel):
    """DescribeProdTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param PageSize: 页面大小
        :type PageSize: int
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.PageSize = None
        self.PageNumber = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
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
        


class DescribeProdTasksResponse(AbstractModel):
    """DescribeProdTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 生产调度任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ProdSchedulerTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ProdSchedulerTask()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id。一般使用项目Id来查询，与projectName必须存在一个。
        :type ProjectId: str
        :param DescribeClusters: 是否展示关联集群信息
        :type DescribeClusters: bool
        :param DescribeExecutors: 是否展示关联执行组的信息，仅部分信息。
        :type DescribeExecutors: bool
        :param DescribeAdminUsers: 默认不展示项目管理员信息
        :type DescribeAdminUsers: bool
        :param DescribeMemberCount: 默认不统计项目人员数量
        :type DescribeMemberCount: bool
        :param DescribeCreator: 默认不查询创建者的信息
        :type DescribeCreator: bool
        :param ProjectName: 项目名只在租户内唯一，一般用来转化为项目ID。
        :type ProjectName: str
        """
        self.ProjectId = None
        self.DescribeClusters = None
        self.DescribeExecutors = None
        self.DescribeAdminUsers = None
        self.DescribeMemberCount = None
        self.DescribeCreator = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DescribeClusters = params.get("DescribeClusters")
        self.DescribeExecutors = params.get("DescribeExecutors")
        self.DescribeAdminUsers = params.get("DescribeAdminUsers")
        self.DescribeMemberCount = params.get("DescribeMemberCount")
        self.DescribeCreator = params.get("DescribeCreator")
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeQualityScoreRequest(AbstractModel):
    """DescribeQualityScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsDate: 统计日期
        :type StatisticsDate: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param DatasourceId: 数据来源id
        :type DatasourceId: str
        """
        self.StatisticsDate = None
        self.ProjectId = None
        self.DatasourceId = None


    def _deserialize(self, params):
        self.StatisticsDate = params.get("StatisticsDate")
        self.ProjectId = params.get("ProjectId")
        self.DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityScoreResponse(AbstractModel):
    """DescribeQualityScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 质量评分
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.QualityScore`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QualityScore()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeQualityScoreTrendRequest(AbstractModel):
    """DescribeQualityScoreTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsStartDate: 统计开始日期
        :type StatisticsStartDate: int
        :param StatisticsEndDate: 统计结束日期
        :type StatisticsEndDate: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param DatasourceId: 数据来源id
        :type DatasourceId: str
        """
        self.StatisticsStartDate = None
        self.StatisticsEndDate = None
        self.ProjectId = None
        self.DatasourceId = None


    def _deserialize(self, params):
        self.StatisticsStartDate = params.get("StatisticsStartDate")
        self.StatisticsEndDate = params.get("StatisticsEndDate")
        self.ProjectId = params.get("ProjectId")
        self.DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityScoreTrendResponse(AbstractModel):
    """DescribeQualityScoreTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 质量评分趋势视图
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.QualityScoreTrend`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QualityScoreTrend()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRealTimeTaskInstanceNodeInfoRequest(AbstractModel):
    """DescribeRealTimeTaskInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 实时任务id
        :type TaskId: str
        :param ProjectId: 工程id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealTimeTaskInstanceNodeInfoResponse(AbstractModel):
    """DescribeRealTimeTaskInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RealTimeTaskInstanceNodeInfo: 实时任务实例节点相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTimeTaskInstanceNodeInfo: :class:`tencentcloud.wedata.v20210820.models.RealTimeTaskInstanceNodeInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RealTimeTaskInstanceNodeInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealTimeTaskInstanceNodeInfo") is not None:
            self.RealTimeTaskInstanceNodeInfo = RealTimeTaskInstanceNodeInfo()
            self.RealTimeTaskInstanceNodeInfo._deserialize(params.get("RealTimeTaskInstanceNodeInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRealTimeTaskMetricOverviewRequest(AbstractModel):
    """DescribeRealTimeTaskMetricOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 无
        :type TaskId: str
        :param ProjectId: 无
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealTimeTaskMetricOverviewResponse(AbstractModel):
    """DescribeRealTimeTaskMetricOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalRecordNumOfRead: 总读取记录数
        :type TotalRecordNumOfRead: int
        :param TotalRecordByteNumOfRead: 总读取字节数
        :type TotalRecordByteNumOfRead: int
        :param TotalRecordNumOfWrite: 总写入记录数
        :type TotalRecordNumOfWrite: int
        :param TotalRecordByteNumOfWrite: 总写入字节数 单位字节
        :type TotalRecordByteNumOfWrite: int
        :param TotalDirtyRecordNum: 总的脏记录数据
        :type TotalDirtyRecordNum: int
        :param TotalDirtyRecordByte: 总的脏字节数 单位字节
        :type TotalDirtyRecordByte: int
        :param TotalDuration: 运行时长 单位s
        :type TotalDuration: int
        :param BeginRunTime: 开始运行时间
        :type BeginRunTime: str
        :param EndRunTime: 目前运行到的时间
        :type EndRunTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalRecordNumOfRead = None
        self.TotalRecordByteNumOfRead = None
        self.TotalRecordNumOfWrite = None
        self.TotalRecordByteNumOfWrite = None
        self.TotalDirtyRecordNum = None
        self.TotalDirtyRecordByte = None
        self.TotalDuration = None
        self.BeginRunTime = None
        self.EndRunTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalRecordNumOfRead = params.get("TotalRecordNumOfRead")
        self.TotalRecordByteNumOfRead = params.get("TotalRecordByteNumOfRead")
        self.TotalRecordNumOfWrite = params.get("TotalRecordNumOfWrite")
        self.TotalRecordByteNumOfWrite = params.get("TotalRecordByteNumOfWrite")
        self.TotalDirtyRecordNum = params.get("TotalDirtyRecordNum")
        self.TotalDirtyRecordByte = params.get("TotalDirtyRecordByte")
        self.TotalDuration = params.get("TotalDuration")
        self.BeginRunTime = params.get("BeginRunTime")
        self.EndRunTime = params.get("EndRunTime")
        self.RequestId = params.get("RequestId")


class DescribeRealTimeTaskSpeedRequest(AbstractModel):
    """DescribeRealTimeTaskSpeed请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 无
        :type TaskId: str
        :param StartTime: 带毫秒的时间戳
        :type StartTime: int
        :param EndTime: 带毫秒的时间戳
        :type EndTime: int
        :param Granularity: 粒度，1或者5
        :type Granularity: int
        :param ProjectId: 无
        :type ProjectId: str
        """
        self.TaskId = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealTimeTaskSpeedResponse(AbstractModel):
    """DescribeRealTimeTaskSpeed返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordsSpeedList: 同步速度条/s列表
        :type RecordsSpeedList: list of RecordsSpeed
        :param BytesSpeedList: 同步速度字节/s列表
        :type BytesSpeedList: list of BytesSpeed
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordsSpeedList = None
        self.BytesSpeedList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordsSpeedList") is not None:
            self.RecordsSpeedList = []
            for item in params.get("RecordsSpeedList"):
                obj = RecordsSpeed()
                obj._deserialize(item)
                self.RecordsSpeedList.append(obj)
        if params.get("BytesSpeedList") is not None:
            self.BytesSpeedList = []
            for item in params.get("BytesSpeedList"):
                obj = BytesSpeed()
                obj._deserialize(item)
                self.BytesSpeedList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRelatedInstancesRequest(AbstractModel):
    """DescribeRelatedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param CurRunDate: 数据时间，格式yyyy-MM-dd HH:mm:ss
        :type CurRunDate: str
        :param TaskId: 任务id
        :type TaskId: int
        :param Depth: 距离当前任务的层级距离，-1表示取父节点，1表示子节点
        :type Depth: int
        :param PageNumber: 页号，默认为1
        :type PageNumber: int
        :param PageSize: 页大小，默认为10，最大不超过200
        :type PageSize: int
        """
        self.ProjectId = None
        self.CurRunDate = None
        self.TaskId = None
        self.Depth = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CurRunDate = params.get("CurRunDate")
        self.TaskId = params.get("TaskId")
        self.Depth = params.get("Depth")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedInstancesResponse(AbstractModel):
    """DescribeRelatedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeTaskInstancesData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeResourceManagePathTreesRequest(AbstractModel):
    """DescribeResourceManagePathTrees请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Name: 名字，供搜索
        :type Name: str
        :param FileType: 文件类型
        :type FileType: str
        :param FilePath: 文件路径
        :type FilePath: str
        :param DirType: 文件夹类型
        :type DirType: str
        """
        self.ProjectId = None
        self.Name = None
        self.FileType = None
        self.FilePath = None
        self.DirType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.FileType = params.get("FileType")
        self.FilePath = params.get("FilePath")
        self.DirType = params.get("DirType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceManagePathTreesResponse(AbstractModel):
    """DescribeResourceManagePathTrees返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ResourcePathTree
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourcePathTree()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuleDataSourcesRequest(AbstractModel):
    """DescribeRuleDataSources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param DatasourceId: 数据来源Id
        :type DatasourceId: str
        :param DsTypes: 数据源类型
        :type DsTypes: list of int non-negative
        """
        self.ProjectId = None
        self.DatasourceId = None
        self.DsTypes = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DatasourceId = params.get("DatasourceId")
        self.DsTypes = params.get("DsTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleDataSourcesResponse(AbstractModel):
    """DescribeRuleDataSources返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DatabaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DatabaseInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuleDimStatRequest(AbstractModel):
    """DescribeRuleDimStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: Project Id
        :type ProjectId: str
        :param BeginDate: 开始时间，时间戳到秒
        :type BeginDate: str
        :param EndDate: 结束时间，时间戳到秒
        :type EndDate: str
        """
        self.ProjectId = None
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleDimStatResponse(AbstractModel):
    """DescribeRuleDimStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleDimStat`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleDimStat()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecDetailRequest(AbstractModel):
    """DescribeRuleExecDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleExecId: 规则执行id
        :type RuleExecId: int
        """
        self.ProjectId = None
        self.RuleExecId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleExecId = params.get("RuleExecId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecDetailResponse(AbstractModel):
    """DescribeRuleExecDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则执行结果详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecResultDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecResultDetail()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecExportResultRequest(AbstractModel):
    """DescribeRuleExecExportResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleExecId: 规则执行id
        :type RuleExecId: int
        """
        self.ProjectId = None
        self.RuleExecId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleExecId = params.get("RuleExecId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecExportResultResponse(AbstractModel):
    """DescribeRuleExecExportResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 导出结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecExportResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecExportResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecHistoryRequest(AbstractModel):
    """DescribeRuleExecHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则Id
        :type RuleId: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.RuleId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecHistoryResponse(AbstractModel):
    """DescribeRuleExecHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则执行结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RuleExecResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleExecResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuleExecLogRequest(AbstractModel):
    """DescribeRuleExecLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleExecId: 规则执行Id
        :type RuleExecId: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleGroupExecId: 规则组执行id
        :type RuleGroupExecId: int
        """
        self.RuleExecId = None
        self.ProjectId = None
        self.RuleGroupExecId = None


    def _deserialize(self, params):
        self.RuleExecId = params.get("RuleExecId")
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecLogResponse(AbstractModel):
    """DescribeRuleExecLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecLog`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecLog()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecResultsByPageRequest(AbstractModel):
    """DescribeRuleExecResultsByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupExecId: 执行规则组ID
        :type RuleGroupExecId: int
        :param PageNumber: page number
        :type PageNumber: int
        :param PageSize: page size
        :type PageSize: int
        """
        self.RuleGroupExecId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecResultsByPageResponse(AbstractModel):
    """DescribeRuleExecResultsByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: results
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecResultPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecResultPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecResultsRequest(AbstractModel):
    """DescribeRuleExecResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupExecId: 规则组执行Id
        :type RuleGroupExecId: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.RuleGroupExecId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecResultsResponse(AbstractModel):
    """DescribeRuleExecResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则执行结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecResultPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecResultPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleExecStatRequest(AbstractModel):
    """DescribeRuleExecStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: ProjectId 值
        :type ProjectId: str
        :param BeginDate: 开始时间，时间戳到秒
        :type BeginDate: str
        :param EndDate: 结束时间，时间戳到秒
        :type EndDate: str
        """
        self.ProjectId = None
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleExecStatResponse(AbstractModel):
    """DescribeRuleExecStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleExecStat`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleExecStat()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupExecResultsByPageRequest(AbstractModel):
    """DescribeRuleGroupExecResultsByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OrderFields: 排序字段
        :type OrderFields: list of OrderField
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupExecResultsByPageResponse(AbstractModel):
    """DescribeRuleGroupExecResultsByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组执行结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupExecResultPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupExecResultPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupExecResultsByPageWithoutAuthRequest(AbstractModel):
    """DescribeRuleGroupExecResultsByPageWithoutAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件，指定表ID过滤字段为 TableIds
        :type Filters: list of Filter
        :param OrderFields: 排序字段
        :type OrderFields: list of OrderField
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupExecResultsByPageWithoutAuthResponse(AbstractModel):
    """DescribeRuleGroupExecResultsByPageWithoutAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组执行结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupExecResultPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupExecResultPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupRequest(AbstractModel):
    """DescribeRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param DatasourceId: 数据来源ID
        :type DatasourceId: str
        :param TableId: 数据表Id
        :type TableId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DatabaseId: 数据库ID
        :type DatabaseId: str
        """
        self.RuleGroupId = None
        self.DatasourceId = None
        self.TableId = None
        self.ProjectId = None
        self.DatabaseId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.DatasourceId = params.get("DatasourceId")
        self.TableId = params.get("TableId")
        self.ProjectId = params.get("ProjectId")
        self.DatabaseId = params.get("DatabaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupResponse(AbstractModel):
    """DescribeRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据质量规则组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroup()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupSubscriptionRequest(AbstractModel):
    """DescribeRuleGroupSubscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.RuleGroupId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupSubscriptionResponse(AbstractModel):
    """DescribeRuleGroupSubscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组订阅信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupSubscribe`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupSubscribe()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupTableRequest(AbstractModel):
    """DescribeRuleGroupTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param TableId: 表ID
        :type TableId: str
        """
        self.TableId = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupTableResponse(AbstractModel):
    """DescribeRuleGroupTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupTable`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupTable()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleGroupsByPageRequest(AbstractModel):
    """DescribeRuleGroupsByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件,每次请求的Filters的上限为10，Filter.Values的上限为5
        :type Filters: list of Filter
        :param OrderFields: 排序方式
        :type OrderFields: list of OrderField
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleGroupsByPageResponse(AbstractModel):
    """DescribeRuleGroupsByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleHistoryByPageRequest(AbstractModel):
    """DescribeRuleHistoryByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
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
        


class DescribeRuleHistoryByPageResponse(AbstractModel):
    """DescribeRuleHistoryByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组操作历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleHistoryPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleHistoryPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 质量规则ID
        :type RuleId: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.RuleId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Rule()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleTablesByPageRequest(AbstractModel):
    """DescribeRuleTablesByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param PageSize: 分页序号
        :type PageSize: int
        :param PageNumber: 分页大小
        :type PageNumber: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OrderFields: 排序条件
        :type OrderFields: list of OrderField
        """
        self.ProjectId = None
        self.PageSize = None
        self.PageNumber = None
        self.Filters = None
        self.OrderFields = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleTablesByPageResponse(AbstractModel):
    """DescribeRuleTablesByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 表列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleGroupPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleGroupPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleTemplateRequest(AbstractModel):
    """DescribeRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TemplateId: 规则模板Id
        :type TemplateId: int
        """
        self.ProjectId = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleTemplateResponse(AbstractModel):
    """DescribeRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 模板详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleTemplate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleTemplate()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleTemplatesByPageRequest(AbstractModel):
    """DescribeRuleTemplatesByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 当前页
        :type PageNumber: int
        :param PageSize: 每页记录数
        :type PageSize: int
        :param ProjectId: 工作空间ID
        :type ProjectId: str
        :param OrderFields: 通用排序字段
        :type OrderFields: list of OrderField
        :param Filters: 通用过滤条件
        :type Filters: list of Filter
        """
        self.PageNumber = None
        self.PageSize = None
        self.ProjectId = None
        self.OrderFields = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
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
        


class DescribeRuleTemplatesByPageResponse(AbstractModel):
    """DescribeRuleTemplatesByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleTemplatePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleTemplatePage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRuleTemplatesRequest(AbstractModel):
    """DescribeRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 模版类型 1.系统模版 2.自定义模版
        :type Type: int
        :param SourceObjectType: 1.常量 2.离线表级 2.离线字段级
        :type SourceObjectType: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param SourceEngineTypes: 源端对应的引擎类型
        :type SourceEngineTypes: list of int non-negative
        """
        self.Type = None
        self.SourceObjectType = None
        self.ProjectId = None
        self.SourceEngineTypes = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SourceObjectType = params.get("SourceObjectType")
        self.ProjectId = params.get("ProjectId")
        self.SourceEngineTypes = params.get("SourceEngineTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleTemplatesResponse(AbstractModel):
    """DescribeRuleTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则模版列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RuleTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleTemplate()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesByPageRequest(AbstractModel):
    """DescribeRulesByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OrderFields: 排序字段
        :type OrderFields: list of OrderField
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesByPageResponse(AbstractModel):
    """DescribeRulesByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则质量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RulePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RulePage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RuleGroupId: 规则组id
        :type RuleGroupId: int
        """
        self.ProjectId = None
        self.RuleGroupId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupId = params.get("RuleGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of Rule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Rule()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStandardRuleDetailInfoListRequest(AbstractModel):
    """DescribeStandardRuleDetailInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 空间、项目id
        :type ProjectId: str
        :param Type: 标准分类11编码映射 12数据过滤 13字符串转换 14数据元定义 15正则表达 16术语词典
        :type Type: int
        """
        self.ProjectId = None
        self.Type = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStandardRuleDetailInfoListResponse(AbstractModel):
    """DescribeStandardRuleDetailInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param StandardRuleDetailList: 返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardRuleDetailList: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StandardRuleDetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StandardRuleDetailList = params.get("StandardRuleDetailList")
        self.RequestId = params.get("RequestId")


class DescribeStreamTaskLogListRequest(AbstractModel):
    """DescribeStreamTaskLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param JobId: 作业ID
        :type JobId: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param Container: container名字
        :type Container: str
        :param Limit: 条数
        :type Limit: int
        :param OrderType: 排序类型 desc asc
        :type OrderType: str
        :param RunningOrderId: 作业运行的实例ID
        :type RunningOrderId: int
        """
        self.ProjectId = None
        self.TaskId = None
        self.JobId = None
        self.EndTime = None
        self.StartTime = None
        self.Container = None
        self.Limit = None
        self.OrderType = None
        self.RunningOrderId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.JobId = params.get("JobId")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Container = params.get("Container")
        self.Limit = params.get("Limit")
        self.OrderType = params.get("OrderType")
        self.RunningOrderId = params.get("RunningOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamTaskLogListResponse(AbstractModel):
    """DescribeStreamTaskLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ListOver: 是否是全量
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param LogContentList: 日志集合
注意：此字段可能返回 null，表示取不到有效值。
        :type LogContentList: list of LogContentInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListOver = None
        self.LogContentList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListOver = params.get("ListOver")
        if params.get("LogContentList") is not None:
            self.LogContentList = []
            for item in params.get("LogContentList"):
                obj = LogContentInfo()
                obj._deserialize(item)
                self.LogContentList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableInfoListRequest(AbstractModel):
    """DescribeTableInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 表名
        :type Filters: list of Filter
        :param ConnectionType: 如果是hive这里写rpc，如果是其他类型不传
        :type ConnectionType: str
        :param Catalog: 数据库源类型
        :type Catalog: str
        """
        self.Filters = None
        self.ConnectionType = None
        self.Catalog = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ConnectionType = params.get("ConnectionType")
        self.Catalog = params.get("Catalog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableInfoListResponse(AbstractModel):
    """DescribeTableInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TableInfo: 表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInfo: list of TableInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TableInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TableInfo") is not None:
            self.TableInfo = []
            for item in params.get("TableInfo"):
                obj = TableInfo()
                obj._deserialize(item)
                self.TableInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableQualityDetailsRequest(AbstractModel):
    """DescribeTableQualityDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsDate: 统计日期
        :type StatisticsDate: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤参数TableName、DatabaseId 、DatabaseName、OwnerUserName
        :type Filters: list of Filter
        :param OrderFields: 排序参数 排序方式 DESC 或者 ASC，表得分排序 TableScore
        :type OrderFields: list of OrderField
        :param DatasourceId: 数据来源id
        :type DatasourceId: str
        """
        self.StatisticsDate = None
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None
        self.DatasourceId = None


    def _deserialize(self, params):
        self.StatisticsDate = params.get("StatisticsDate")
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        self.DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableQualityDetailsResponse(AbstractModel):
    """DescribeTableQualityDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 表质量分详情结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.TableQualityDetailPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TableQualityDetailPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTableSchemaInfoRequest(AbstractModel):
    """DescribeTableSchemaInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 表名称
        :type Name: str
        :param DatabaseName: 数据库名称
        :type DatabaseName: str
        :param MsType: 表类型
        :type MsType: str
        :param DatasourceId: 数据源id
        :type DatasourceId: str
        :param ConnectionType: HIVE传rpc
        :type ConnectionType: str
        :param SchemaName: 元数据Database下的Schema名称
        :type SchemaName: str
        """
        self.Name = None
        self.DatabaseName = None
        self.MsType = None
        self.DatasourceId = None
        self.ConnectionType = None
        self.SchemaName = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DatabaseName = params.get("DatabaseName")
        self.MsType = params.get("MsType")
        self.DatasourceId = params.get("DatasourceId")
        self.ConnectionType = params.get("ConnectionType")
        self.SchemaName = params.get("SchemaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableSchemaInfoResponse(AbstractModel):
    """DescribeTableSchemaInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param SchemaInfoList: 123
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaInfoList: list of SchemaDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SchemaInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SchemaInfoList") is not None:
            self.SchemaInfoList = []
            for item in params.get("SchemaInfoList"):
                obj = SchemaDetail()
                obj._deserialize(item)
                self.SchemaInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableScoreTrendRequest(AbstractModel):
    """DescribeTableScoreTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param StatisticsStartDate: 开始时间 秒级时间戳
        :type StatisticsStartDate: int
        :param StatisticsEndDate: 结束时间 秒级时间戳
        :type StatisticsEndDate: int
        :param TableId: 表id
        :type TableId: str
        """
        self.ProjectId = None
        self.StatisticsStartDate = None
        self.StatisticsEndDate = None
        self.TableId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.StatisticsStartDate = params.get("StatisticsStartDate")
        self.StatisticsEndDate = params.get("StatisticsEndDate")
        self.TableId = params.get("TableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableScoreTrendResponse(AbstractModel):
    """DescribeTableScoreTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 表得分趋势
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.QualityScoreTrend`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QualityScoreTrend()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTaskAlarmRegulationsRequest(AbstractModel):
    """DescribeTaskAlarmRegulations请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param TaskType: 任务类型(201代表实时任务，202代表离线任务)
        :type TaskType: int
        :param PageNumber: 当前页
        :type PageNumber: int
        :param PageSize: 每页记录数
        :type PageSize: int
        :param Filters: 过滤条件(name有RegularStatus、AlarmLevel、AlarmIndicator、RegularName)
        :type Filters: list of Filter
        :param OrderFields: 排序条件(RegularId)
        :type OrderFields: list of OrderField
        """
        self.TaskId = None
        self.ProjectId = None
        self.TaskType = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderFields = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskAlarmRegulationsResponse(AbstractModel):
    """DescribeTaskAlarmRegulations返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskAlarmInfos: 任务告警规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAlarmInfos: list of TaskAlarmInfo
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskAlarmInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskAlarmInfos") is not None:
            self.TaskAlarmInfos = []
            for item in params.get("TaskAlarmInfos"):
                obj = TaskAlarmInfo()
                obj._deserialize(item)
                self.TaskAlarmInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskAlarmStatus: 任务告警状态
        :type TaskAlarmStatus: int
        """
        self.ProjectId = None
        self.TaskId = None
        self.TaskAlarmStatus = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.TaskAlarmStatus = params.get("TaskAlarmStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 任务详情1
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.TaskInfoData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TaskInfoData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTaskInstanceReportDetailRequest(AbstractModel):
    """DescribeTaskInstanceReportDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param CurRunDate: 任务实例数据时间
        :type CurRunDate: str
        :param IssueDate: 任务实例运行时间
        :type IssueDate: str
        """
        self.ProjectId = None
        self.TaskId = None
        self.CurRunDate = None
        self.IssueDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.IssueDate = params.get("IssueDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInstanceReportDetailResponse(AbstractModel):
    """DescribeTaskInstanceReportDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Summary: 任务实例运行指标概览
        :type Summary: :class:`tencentcloud.wedata.v20210820.models.InstanceReportSummary`
        :param ReadNode: 任务实例读取节点运行指标
        :type ReadNode: :class:`tencentcloud.wedata.v20210820.models.InstanceReportReadNode`
        :param WriteNode: 任务实例写入节点运行指标
        :type WriteNode: :class:`tencentcloud.wedata.v20210820.models.InstanceReportWriteNode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Summary = None
        self.ReadNode = None
        self.WriteNode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self.Summary = InstanceReportSummary()
            self.Summary._deserialize(params.get("Summary"))
        if params.get("ReadNode") is not None:
            self.ReadNode = InstanceReportReadNode()
            self.ReadNode._deserialize(params.get("ReadNode"))
        if params.get("WriteNode") is not None:
            self.WriteNode = InstanceReportWriteNode()
            self.WriteNode._deserialize(params.get("WriteNode"))
        self.RequestId = params.get("RequestId")


class DescribeTaskInstanceRequest(AbstractModel):
    """DescribeTaskInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param CurRunDate: 任务实例数据时间
        :type CurRunDate: str
        :param IssueDate: 任务实例运行时间
        :type IssueDate: str
        """
        self.ProjectId = None
        self.TaskId = None
        self.CurRunDate = None
        self.IssueDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.IssueDate = params.get("IssueDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInstanceResponse(AbstractModel):
    """DescribeTaskInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInstanceDetail: 任务实例详情
        :type TaskInstanceDetail: :class:`tencentcloud.wedata.v20210820.models.TaskInstanceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInstanceDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInstanceDetail") is not None:
            self.TaskInstanceDetail = TaskInstanceDetail()
            self.TaskInstanceDetail._deserialize(params.get("TaskInstanceDetail"))
        self.RequestId = params.get("RequestId")


class DescribeTaskInstancesData(AbstractModel):
    """查询任务实例列表

    """

    def __init__(self):
        r"""
        :param Items: 实例列表
        :type Items: list of TaskInstanceInfo
        :param TotalCount: 总条数
        :type TotalCount: int
        :param PageNumber: 页号
        :type PageNumber: int
        :param PageSize: 页大小
        :type PageSize: int
        """
        self.Items = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TaskInstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInstancesRequest(AbstractModel):
    """DescribeTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param PageNumber: 页号，默认为1
        :type PageNumber: int
        :param PageSize: 页大小，默认为10，最大不超过200
        :type PageSize: int
        :param WorkflowIdList: 工作流id列表
        :type WorkflowIdList: list of str
        :param WorkflowNameList: 工作流名称列表，支持模糊搜索
        :type WorkflowNameList: list of str
        :param DateFrom: 起始数据时间，格式yyyy-MM-dd HH:mm:ss
        :type DateFrom: str
        :param DateTo: 结束数据时间，格式yyyy-MM-dd HH:mm:ss
        :type DateTo: str
        :param TaskIdList: 任务id列表
        :type TaskIdList: list of str
        :param TaskNameList: 任务名称列表，支持模糊搜索
        :type TaskNameList: list of str
        :param InChargeList: 责任人名称列表
        :type InChargeList: list of str
        :param TaskTypeIdList: 任务类型码列表，26离线同步，30Python，31PySpark，32DLC，33Impala，34Hive SQL，35Shell，36Spark SQL，39Spark，40CDW PG，92MapReduce
        :type TaskTypeIdList: list of int
        :param StateList: 实例状态列表，0等待事件，1等待上游，2等待运行，3运行中，4正在终止，5失败重试，6失败，7成功
        :type StateList: list of str
        :param TaskCycleUnitList: 周期类型列表，I分钟，H小时，D天，W周，M月，Y年，O一次性，C crontab
        :type TaskCycleUnitList: list of str
        :param InstanceType: 实例类型，0补录实例，1周期实例，2非周期实例
        :type InstanceType: int
        :param OrderFields: 排序字段信息列表，ScheduleDateTime / CostTime / StartTime / EndTime
        :type OrderFields: list of OrderField
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.WorkflowIdList = None
        self.WorkflowNameList = None
        self.DateFrom = None
        self.DateTo = None
        self.TaskIdList = None
        self.TaskNameList = None
        self.InChargeList = None
        self.TaskTypeIdList = None
        self.StateList = None
        self.TaskCycleUnitList = None
        self.InstanceType = None
        self.OrderFields = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.WorkflowIdList = params.get("WorkflowIdList")
        self.WorkflowNameList = params.get("WorkflowNameList")
        self.DateFrom = params.get("DateFrom")
        self.DateTo = params.get("DateTo")
        self.TaskIdList = params.get("TaskIdList")
        self.TaskNameList = params.get("TaskNameList")
        self.InChargeList = params.get("InChargeList")
        self.TaskTypeIdList = params.get("TaskTypeIdList")
        self.StateList = params.get("StateList")
        self.TaskCycleUnitList = params.get("TaskCycleUnitList")
        self.InstanceType = params.get("InstanceType")
        if params.get("OrderFields") is not None:
            self.OrderFields = []
            for item in params.get("OrderFields"):
                obj = OrderField()
                obj._deserialize(item)
                self.OrderFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInstancesResponse(AbstractModel):
    """DescribeTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
        :type Data: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeTaskInstancesData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTaskLockStatusRequest(AbstractModel):
    """DescribeTaskLockStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型：201. stream,   202. offline
        :type TaskType: int
        """
        self.TaskId = None
        self.ProjectId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLockStatusResponse(AbstractModel):
    """DescribeTaskLockStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskLockStatus: 任务锁状态信息
        :type TaskLockStatus: :class:`tencentcloud.wedata.v20210820.models.TaskLockStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskLockStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskLockStatus") is not None:
            self.TaskLockStatus = TaskLockStatus()
            self.TaskLockStatus._deserialize(params.get("TaskLockStatus"))
        self.RequestId = params.get("RequestId")


class DescribeTaskReportDetailListRequest(AbstractModel):
    """DescribeTaskReportDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: WeData项目id
        :type ProjectId: str
        :param TaskId: 任务Id
        :type TaskId: str
        :param BeginDate: 统计周期的开始日期，格式为 yyyy-MM-dd
        :type BeginDate: str
        :param EndDate: 统计周期的结束日期，格式为 yyyy-MM-dd
        :type EndDate: str
        :param StateList: 任务状态，多个状态用逗号连接
        :type StateList: str
        :param SortItem: 排序字段名
        :type SortItem: str
        :param SortType: 升序或降序，传ASC或DESC
        :type SortType: str
        :param PageIndex: 页数，从1开始
        :type PageIndex: int
        :param PageSize: 每页的记录条数，默认10条
        :type PageSize: int
        """
        self.ProjectId = None
        self.TaskId = None
        self.BeginDate = None
        self.EndDate = None
        self.StateList = None
        self.SortItem = None
        self.SortType = None
        self.PageIndex = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.StateList = params.get("StateList")
        self.SortItem = params.get("SortItem")
        self.SortType = params.get("SortType")
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskReportDetailListResponse(AbstractModel):
    """DescribeTaskReportDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param PageIndex: 页码，从1开始
        :type PageIndex: int
        :param PageSize: 每页的记录数
        :type PageSize: int
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param TotalPage: 总页数
        :type TotalPage: int
        :param Items: 任务运行指标
        :type Items: list of TaskReportDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageIndex = None
        self.PageSize = None
        self.TotalCount = None
        self.TotalPage = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.TotalPage = params.get("TotalPage")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TaskReportDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskReportRequest(AbstractModel):
    """DescribeTaskReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param BeginDate: 统计周期的开始日期，格式为 yyyy-MM-dd
        :type BeginDate: str
        :param EndDate: 统计周期的结束日期，格式为 yyyy-MM-dd
        :type EndDate: str
        :param ProjectId: WeData项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.BeginDate = None
        self.EndDate = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskReportResponse(AbstractModel):
    """DescribeTaskReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalReadRecords: 总读取条数
        :type TotalReadRecords: int
        :param TotalReadBytes: 总读取字节数，单位为Byte
        :type TotalReadBytes: int
        :param TotalWriteRecords: 总写入条数
        :type TotalWriteRecords: int
        :param TotalWriteBytes: 总写入字节数，单位为Byte
        :type TotalWriteBytes: int
        :param TotalErrorRecords: 总脏数据条数
        :type TotalErrorRecords: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalReadRecords = None
        self.TotalReadBytes = None
        self.TotalWriteRecords = None
        self.TotalWriteBytes = None
        self.TotalErrorRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalReadRecords = params.get("TotalReadRecords")
        self.TotalReadBytes = params.get("TotalReadBytes")
        self.TotalWriteRecords = params.get("TotalWriteRecords")
        self.TotalWriteBytes = params.get("TotalWriteBytes")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        self.RequestId = params.get("RequestId")


class DescribeTaskScriptRequest(AbstractModel):
    """DescribeTaskScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.ProjectId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskScriptResponse(AbstractModel):
    """DescribeTaskScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 任务脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.TaskScriptContent`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TaskScriptContent()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTasksByPageRequest(AbstractModel):
    """DescribeTasksByPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowId: 工作流ID
        :type WorkflowId: str
        :param PageNumber: 页码，默认1
        :type PageNumber: int
        :param PageSize: 页大小，默认10
        :type PageSize: int
        """
        self.ProjectId = None
        self.WorkflowId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksByPageResponse(AbstractModel):
    """DescribeTasksByPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无1
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.TaskInfoDataPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TaskInfoDataPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTemplateDimCountRequest(AbstractModel):
    """DescribeTemplateDimCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 模版类型
        :type Type: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.Type = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateDimCountResponse(AbstractModel):
    """DescribeTemplateDimCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 维度统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DimensionCount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DimensionCount()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateHistoryRequest(AbstractModel):
    """DescribeTemplateHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateHistoryResponse(AbstractModel):
    """DescribeTemplateHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 分页记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.RuleTemplateHistoryPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RuleTemplateHistoryPage()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTopTableStatRequest(AbstractModel):
    """DescribeTopTableStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: Project Id
        :type ProjectId: str
        :param BeginDate: 开始时间，时间戳到秒
        :type BeginDate: str
        :param EndDate: 结束时间，时间戳到秒
        :type EndDate: str
        """
        self.ProjectId = None
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopTableStatResponse(AbstractModel):
    """DescribeTopTableStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.TopTableStat`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TopTableStat()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTrendStatRequest(AbstractModel):
    """DescribeTrendStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: Project id
        :type ProjectId: str
        :param BeginDate: 开始时间，时间戳到秒
        :type BeginDate: str
        :param EndDate: 结束时间，时间戳到秒
        :type EndDate: str
        """
        self.ProjectId = None
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrendStatResponse(AbstractModel):
    """DescribeTrendStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: list of RuleExecDateStat
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleExecDateStat()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DimensionCount(AbstractModel):
    """维度统计业务视图

    """

    def __init__(self):
        r"""
        :param DimType: 维度类型1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
注意：此字段可能返回 null，表示取不到有效值。
        :type DimType: int
        :param Count: 统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.DimType = None
        self.Count = None


    def _deserialize(self, params):
        self.DimType = params.get("DimType")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionScore(AbstractModel):
    """维度评分

    """

    def __init__(self):
        r"""
        :param DimensionScoreList: 维度评分列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DimensionScoreList: list of DimensionScoreInfo
        """
        self.DimensionScoreList = None


    def _deserialize(self, params):
        if params.get("DimensionScoreList") is not None:
            self.DimensionScoreList = []
            for item in params.get("DimensionScoreList"):
                obj = DimensionScoreInfo()
                obj._deserialize(item)
                self.DimensionScoreList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionScoreInfo(AbstractModel):
    """维度评分信息

    """

    def __init__(self):
        r"""
        :param Name: 维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: float
        :param UserId: 设置人id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: int
        :param UserName: 设置人名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param UpdateTime: 更新时间 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param JoinTableNumber: 参与评估表数量
        :type JoinTableNumber: int
        :param Score: 评分
        :type Score: float
        """
        self.Name = None
        self.Weight = None
        self.UserId = None
        self.UserName = None
        self.UpdateTime = None
        self.JoinTableNumber = None
        self.Score = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Weight = params.get("Weight")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.UpdateTime = params.get("UpdateTime")
        self.JoinTableNumber = params.get("JoinTableNumber")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DryRunDIOfflineTaskRequest(AbstractModel):
    """DryRunDIOfflineTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param ResourceGroup: 资源组Id
        :type ResourceGroup: str
        :param TaskTypeId: 默认 27
        :type TaskTypeId: int
        """
        self.TaskId = None
        self.ProjectId = None
        self.ResourceGroup = None
        self.TaskTypeId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.ResourceGroup = params.get("ResourceGroup")
        self.TaskTypeId = params.get("TaskTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DryRunDIOfflineTaskResponse(AbstractModel):
    """DryRunDIOfflineTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param CurrentRunDate: 数据时间
        :type CurrentRunDate: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Status: 任务状态
        :type Status: str
        :param TaskId: 任务Id
        :type TaskId: str
        :param TaskInstanceKey: 任务实例唯一key
        :type TaskInstanceKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CurrentRunDate = None
        self.ProjectId = None
        self.Status = None
        self.TaskId = None
        self.TaskInstanceKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CurrentRunDate = params.get("CurrentRunDate")
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.TaskInstanceKey = params.get("TaskInstanceKey")
        self.RequestId = params.get("RequestId")


class ExportTaskInfo(AbstractModel):
    """数据导出任务详情

    """

    def __init__(self):
        r"""
        :param ExportTaskId: 导出任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportTaskId: int
        :param TaskType: 导出任务类型(1.全部,2.触发行,3.通过行)
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param OperatorId: 任务创建人 id
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorId: int
        :param OperatorName: 任务创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorName: str
        :param CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Status: 导出状态(1.已提交 2.导出中 3.导出成功 4.导出失败)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param SchedulerTaskId: 调度任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerTaskId: str
        :param SchedulerCurRunDate: 调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerCurRunDate: str
        :param FilePath: 文件相对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        """
        self.ExportTaskId = None
        self.TaskType = None
        self.OperatorId = None
        self.OperatorName = None
        self.CreateTime = None
        self.Status = None
        self.SchedulerTaskId = None
        self.SchedulerCurRunDate = None
        self.FilePath = None


    def _deserialize(self, params):
        self.ExportTaskId = params.get("ExportTaskId")
        self.TaskType = params.get("TaskType")
        self.OperatorId = params.get("OperatorId")
        self.OperatorName = params.get("OperatorName")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.SchedulerTaskId = params.get("SchedulerTaskId")
        self.SchedulerCurRunDate = params.get("SchedulerCurRunDate")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldConfig(AbstractModel):
    """字段变量

    """

    def __init__(self):
        r"""
        :param FieldKey: 字段key
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldKey: str
        :param FieldValue: 字段值
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldValue: str
        :param FieldDataType: 字段值类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldDataType: str
        """
        self.FieldKey = None
        self.FieldValue = None
        self.FieldDataType = None


    def _deserialize(self, params):
        self.FieldKey = params.get("FieldKey")
        self.FieldValue = params.get("FieldValue")
        self.FieldDataType = params.get("FieldDataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """通用过滤器

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名称
        :type Name: str
        :param Values: 过滤值列表
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Folder(AbstractModel):
    """文件夹信息

    """

    def __init__(self):
        r"""
        :param Id: 文件ID
        :type Id: str
        :param Name: 文件夹名称
        :type Name: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ProjectId: 所属项目id
        :type ProjectId: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.Name = None
        self.CreateTime = None
        self.ProjectId = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceSucInstancesRequest(AbstractModel):
    """ForceSucInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Instances: 实例嵌套集合
        :type Instances: list of InstanceInfo
        """
        self.ProjectId = None
        self.Instances = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceSucInstancesResponse(AbstractModel):
    """ForceSucInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回实例批量终止结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FreezeTasksByMultiWorkflowRequest(AbstractModel):
    """FreezeTasksByMultiWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkFlowIds: 工作流Id集合
        :type WorkFlowIds: list of str
        """
        self.WorkFlowIds = None


    def _deserialize(self, params):
        self.WorkFlowIds = params.get("WorkFlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeTasksByMultiWorkflowResponse(AbstractModel):
    """FreezeTasksByMultiWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FreezeTasksRequest(AbstractModel):
    """FreezeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 任务列表
        :type Tasks: list of SimpleTaskInfo
        :param OperateIsInform: 任务操作是否消息通知下游任务责任人
        :type OperateIsInform: bool
        """
        self.Tasks = None
        self.OperateIsInform = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = SimpleTaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.OperateIsInform = params.get("OperateIsInform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeTasksResponse(AbstractModel):
    """FreezeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FunctionResource(AbstractModel):
    """函数资源信息

    """

    def __init__(self):
        r"""
        :param Path: 资源路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Name: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Id: 资源唯一标识
        :type Id: str
        :param Md5: 资源 MD5 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param Type: 默认是 hdfs
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Path = None
        self.Name = None
        self.Id = None
        self.Md5 = None
        self.Type = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Md5 = params.get("Md5")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionTypeOrKind(AbstractModel):
    """函数类型或函数分类

    """

    def __init__(self):
        r"""
        :param Name: 无
        :type Name: str
        :param ZhName: 无
        :type ZhName: str
        :param EnName: 无
        :type EnName: str
        """
        self.Name = None
        self.ZhName = None
        self.EnName = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ZhName = params.get("ZhName")
        self.EnName = params.get("EnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionVersion(AbstractModel):
    """函数提交版本信息

    """

    def __init__(self):
        r"""
        :param Tag: 版本号：V0 V1 V2
        :type Tag: str
        :param UserId: 提交人 ID
        :type UserId: str
        :param Type: 变更类型：ADD、MODIFY
        :type Type: str
        :param Comment: 备注
        :type Comment: str
        :param Timestamp: 提交时间: UTC 秒数
        :type Timestamp: str
        :param UserName: 提交人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param Content: 版本内容：json string 格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self.Tag = None
        self.UserId = None
        self.Type = None
        self.Comment = None
        self.Timestamp = None
        self.UserName = None
        self.Content = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Timestamp = params.get("Timestamp")
        self.UserName = params.get("UserName")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenHiveTableDDLSqlRequest(AbstractModel):
    """GenHiveTableDDLSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param SinkDatabase: 目标数据库
        :type SinkDatabase: str
        :param Id: 节点id
        :type Id: str
        :param MsType: 元数据类型(MYSQL、ORACLE)
        :type MsType: str
        :param DatasourceId: 数据源id
        :type DatasourceId: str
        :param SourceDatabase: 来源库
        :type SourceDatabase: str
        :param TableName: 来源表
        :type TableName: str
        :param SinkType: 目标表元数据类型(HIVE、GBASE)
        :type SinkType: str
        :param SchemaName: schema名称
        :type SchemaName: str
        :param SourceFieldInfoList: 上游节点的字段信息
        :type SourceFieldInfoList: list of SourceFieldInfo
        """
        self.ProjectId = None
        self.SinkDatabase = None
        self.Id = None
        self.MsType = None
        self.DatasourceId = None
        self.SourceDatabase = None
        self.TableName = None
        self.SinkType = None
        self.SchemaName = None
        self.SourceFieldInfoList = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SinkDatabase = params.get("SinkDatabase")
        self.Id = params.get("Id")
        self.MsType = params.get("MsType")
        self.DatasourceId = params.get("DatasourceId")
        self.SourceDatabase = params.get("SourceDatabase")
        self.TableName = params.get("TableName")
        self.SinkType = params.get("SinkType")
        self.SchemaName = params.get("SchemaName")
        if params.get("SourceFieldInfoList") is not None:
            self.SourceFieldInfoList = []
            for item in params.get("SourceFieldInfoList"):
                obj = SourceFieldInfo()
                obj._deserialize(item)
                self.SourceFieldInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenHiveTableDDLSqlResponse(AbstractModel):
    """GenHiveTableDDLSql返回参数结构体

    """

    def __init__(self):
        r"""
        :param DDLSql: 生成的ddl语句
        :type DDLSql: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DDLSql = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DDLSql = params.get("DDLSql")
        self.RequestId = params.get("RequestId")


class GeneralTaskParam(AbstractModel):
    """Spark SQL配置参数

    """

    def __init__(self):
        r"""
        :param Type: 通用任务参数类型,例：SPARK_SQL
        :type Type: str
        :param Value: 通用任务参数内容,直接作用于任务的参数。不同参数用;
分割
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
        


class GetIntegrationNodeColumnSchemaRequest(AbstractModel):
    """GetIntegrationNodeColumnSchema请求参数结构体

    """

    def __init__(self):
        r"""
        :param ColumnContent: 字段示例（json格式）
        :type ColumnContent: str
        :param DatasourceType: 数据源类型
        :type DatasourceType: str
        """
        self.ColumnContent = None
        self.DatasourceType = None


    def _deserialize(self, params):
        self.ColumnContent = params.get("ColumnContent")
        self.DatasourceType = params.get("DatasourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIntegrationNodeColumnSchemaResponse(AbstractModel):
    """GetIntegrationNodeColumnSchema返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schemas: 字段列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Schemas: list of IntegrationNodeSchema
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schemas = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Schemas") is not None:
            self.Schemas = []
            for item in params.get("Schemas"):
                obj = IntegrationNodeSchema()
                obj._deserialize(item)
                self.Schemas.append(obj)
        self.RequestId = params.get("RequestId")


class GetOfflineDIInstanceListRequest(AbstractModel):
    """GetOfflineDIInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageIndex: 第几页
        :type PageIndex: int
        :param PageSize: 每页几条
        :type PageSize: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param SearchCondition: 无
        :type SearchCondition: :class:`tencentcloud.wedata.v20210820.models.SearchConditionNew`
        """
        self.PageIndex = None
        self.PageSize = None
        self.ProjectId = None
        self.SearchCondition = None


    def _deserialize(self, params):
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = SearchConditionNew()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOfflineDIInstanceListResponse(AbstractModel):
    """GetOfflineDIInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总条数
        :type Total: int
        :param List: 实例详情
        :type List: list of OfflineInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = OfflineInstance()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class GetOfflineInstanceListRequest(AbstractModel):
    """GetOfflineInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageIndex: 第几页
        :type PageIndex: str
        :param PageSize: 每页几条
        :type PageSize: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param SearchCondition: 无
        :type SearchCondition: :class:`tencentcloud.wedata.v20210820.models.SearchCondition`
        """
        self.PageIndex = None
        self.PageSize = None
        self.ProjectId = None
        self.SearchCondition = None


    def _deserialize(self, params):
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = SearchCondition()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOfflineInstanceListResponse(AbstractModel):
    """GetOfflineInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总条数
        :type Total: int
        :param List: 实例详情
        :type List: list of OfflineInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = OfflineInstance()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class InLongAgentDetail(AbstractModel):
    """采集器详细信息

    """

    def __init__(self):
        r"""
        :param AgentId: Agent ID
        :type AgentId: str
        :param AgentName: Agent Name
        :type AgentName: str
        :param Status: Agent状态(running运行中，initializing 操作中，failed心跳异常)
        :type Status: str
        :param StatusDesc: Agent状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param AgentType: 集群类型，1：TKE Agent，2：BOSS SDK，默认：1
        :type AgentType: int
        :param Source: 采集来源
        :type Source: str
        :param VpcId: VPC
        :type VpcId: str
        :param ExecutorGroupId: 集成资源组Id
        :type ExecutorGroupId: str
        :param ExecutorGroupName: 集成资源组名称
        :type ExecutorGroupName: str
        :param TaskCount: 关联任务数
        :type TaskCount: int
        :param AgentGroupId: 采集器组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentGroupId: str
        :param CvmAgentStatusList: agent状态统计
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmAgentStatusList: list of CvmAgentStatus
        :param AgentTotal: agent数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentTotal: int
        """
        self.AgentId = None
        self.AgentName = None
        self.Status = None
        self.StatusDesc = None
        self.AgentType = None
        self.Source = None
        self.VpcId = None
        self.ExecutorGroupId = None
        self.ExecutorGroupName = None
        self.TaskCount = None
        self.AgentGroupId = None
        self.CvmAgentStatusList = None
        self.AgentTotal = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.AgentType = params.get("AgentType")
        self.Source = params.get("Source")
        self.VpcId = params.get("VpcId")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.ExecutorGroupName = params.get("ExecutorGroupName")
        self.TaskCount = params.get("TaskCount")
        self.AgentGroupId = params.get("AgentGroupId")
        if params.get("CvmAgentStatusList") is not None:
            self.CvmAgentStatusList = []
            for item in params.get("CvmAgentStatusList"):
                obj = CvmAgentStatus()
                obj._deserialize(item)
                self.CvmAgentStatusList.append(obj)
        self.AgentTotal = params.get("AgentTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InLongAgentTask(AbstractModel):
    """采集器关联的集成任务

    """

    def __init__(self):
        r"""
        :param TaskId: 集成任务ID
        :type TaskId: str
        :param TaskName: 集成任务名称
        :type TaskName: str
        :param TaskStatus: 集成任务状态
        :type TaskStatus: str
        """
        self.TaskId = None
        self.TaskName = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InLongTkeDetail(AbstractModel):
    """TKE集群信息详情

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Status: TKE集群状态 (Running 运行中 Creating 创建中 Idling 闲置中 Abnormal 异常)
        :type Status: str
        :param HasAgent: 是否安装Agent，true: 是，false: 否
        :type HasAgent: bool
        :param AgentId: 采集器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param TkeRegion: TKE集群区域ID
        :type TkeRegion: str
        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER
        :type ClusterType: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Status = None
        self.HasAgent = None
        self.AgentId = None
        self.VpcId = None
        self.TkeRegion = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Status = params.get("Status")
        self.HasAgent = params.get("HasAgent")
        self.AgentId = params.get("AgentId")
        self.VpcId = params.get("VpcId")
        self.TkeRegion = params.get("TkeRegion")
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例请求实体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        """
        self.TaskId = None
        self.CurRunDate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """实例日志实体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        :param Tries: 尝试运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tries: str
        :param LastUpdate: 日志更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdate: str
        :param BrokerIp: 日志所在节点
        :type BrokerIp: str
        :param OriginFileName: 文件名  含全路径
        :type OriginFileName: str
        :param CreateTime: 日志创建时间
        :type CreateTime: str
        :param InstanceLogType: 实例日志类型, run: 运行; kill: 终止
        :type InstanceLogType: str
        :param CostTime: 运行耗时
        :type CostTime: float
        """
        self.TaskId = None
        self.CurRunDate = None
        self.Tries = None
        self.LastUpdate = None
        self.BrokerIp = None
        self.OriginFileName = None
        self.CreateTime = None
        self.InstanceLogType = None
        self.CostTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.Tries = params.get("Tries")
        self.LastUpdate = params.get("LastUpdate")
        self.BrokerIp = params.get("BrokerIp")
        self.OriginFileName = params.get("OriginFileName")
        self.CreateTime = params.get("CreateTime")
        self.InstanceLogType = params.get("InstanceLogType")
        self.CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeInfo(AbstractModel):
    """查询实时任务实例当前的节点信息

    """

    def __init__(self):
        r"""
        :param NodeType: 读取节点SOURCE 写入节点SINK
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param NodeId: 节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        """
        self.NodeType = None
        self.NodeId = None
        self.NodeName = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReportReadNode(AbstractModel):
    """离线任务实例读取节点的运行指标

    """

    def __init__(self):
        r"""
        :param NodeName: 节点名称
        :type NodeName: str
        :param DataSource: 数据来源
        :type DataSource: str
        :param TotalReadRecords: 总条数
        :type TotalReadRecords: int
        :param TotalReadBytes: 总字节数
        :type TotalReadBytes: int
        :param RecordSpeed: 速度（条/秒）
        :type RecordSpeed: int
        :param ByteSpeed: 吞吐（Byte/秒）
        :type ByteSpeed: float
        :param TotalErrorRecords: 脏数据条数
        :type TotalErrorRecords: int
        """
        self.NodeName = None
        self.DataSource = None
        self.TotalReadRecords = None
        self.TotalReadBytes = None
        self.RecordSpeed = None
        self.ByteSpeed = None
        self.TotalErrorRecords = None


    def _deserialize(self, params):
        self.NodeName = params.get("NodeName")
        self.DataSource = params.get("DataSource")
        self.TotalReadRecords = params.get("TotalReadRecords")
        self.TotalReadBytes = params.get("TotalReadBytes")
        self.RecordSpeed = params.get("RecordSpeed")
        self.ByteSpeed = params.get("ByteSpeed")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReportSummary(AbstractModel):
    """离线任务实例运行指标概览

    """

    def __init__(self):
        r"""
        :param TotalReadRecords: 总读取记录数
        :type TotalReadRecords: int
        :param TotalReadBytes: 总读取字节数
        :type TotalReadBytes: int
        :param TotalWriteRecords: 总写入记录数
        :type TotalWriteRecords: int
        :param TotalWriteBytes: 总写入字节数
        :type TotalWriteBytes: int
        :param RecordSpeed: 速率（条/秒）
        :type RecordSpeed: int
        :param ByteSpeed: 流量（Byte/秒）
        :type ByteSpeed: float
        :param TotalErrorRecords: 脏数据记录数
        :type TotalErrorRecords: int
        :param TotalErrorBytes: 脏数据字节数
        :type TotalErrorBytes: int
        :param TotalRunDuration: 任务运行总时长
        :type TotalRunDuration: int
        :param BeginRunTime: 任务开始运行时间
        :type BeginRunTime: str
        :param EndRunTime: 任务结束运行时间
        :type EndRunTime: str
        """
        self.TotalReadRecords = None
        self.TotalReadBytes = None
        self.TotalWriteRecords = None
        self.TotalWriteBytes = None
        self.RecordSpeed = None
        self.ByteSpeed = None
        self.TotalErrorRecords = None
        self.TotalErrorBytes = None
        self.TotalRunDuration = None
        self.BeginRunTime = None
        self.EndRunTime = None


    def _deserialize(self, params):
        self.TotalReadRecords = params.get("TotalReadRecords")
        self.TotalReadBytes = params.get("TotalReadBytes")
        self.TotalWriteRecords = params.get("TotalWriteRecords")
        self.TotalWriteBytes = params.get("TotalWriteBytes")
        self.RecordSpeed = params.get("RecordSpeed")
        self.ByteSpeed = params.get("ByteSpeed")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        self.TotalErrorBytes = params.get("TotalErrorBytes")
        self.TotalRunDuration = params.get("TotalRunDuration")
        self.BeginRunTime = params.get("BeginRunTime")
        self.EndRunTime = params.get("EndRunTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReportWriteNode(AbstractModel):
    """离线任务实例写入节点的运行指标

    """

    def __init__(self):
        r"""
        :param NodeName: 节点名称
        :type NodeName: str
        :param DataSource: 数据来源
        :type DataSource: str
        :param TotalWriteRecords: 总条数
        :type TotalWriteRecords: int
        :param TotalWriteBytes: 总字节数
        :type TotalWriteBytes: int
        :param RecordSpeed: 速度（条/秒）
        :type RecordSpeed: int
        :param ByteSpeed: 吞吐（Byte/秒）
        :type ByteSpeed: float
        :param TotalErrorRecords: 脏数据条数
        :type TotalErrorRecords: int
        """
        self.NodeName = None
        self.DataSource = None
        self.TotalWriteRecords = None
        self.TotalWriteBytes = None
        self.RecordSpeed = None
        self.ByteSpeed = None
        self.TotalErrorRecords = None


    def _deserialize(self, params):
        self.NodeName = params.get("NodeName")
        self.DataSource = params.get("DataSource")
        self.TotalWriteRecords = params.get("TotalWriteRecords")
        self.TotalWriteBytes = params.get("TotalWriteBytes")
        self.RecordSpeed = params.get("RecordSpeed")
        self.ByteSpeed = params.get("ByteSpeed")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationNodeDetail(AbstractModel):
    """集成节点详情

    """

    def __init__(self):
        r"""
        :param Name: 集成节点名称
        :type Name: str
        :param NodeType: 集成节点类型
        :type NodeType: str
        :param DataSourceType: 节点数据源类型
        :type DataSourceType: str
        :param Description: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param DatasourceId: 数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param Config: 节点配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: list of RecordField
        :param ExtConfig: 节点扩展配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtConfig: list of RecordField
        :param Schema: 节点schema
注意：此字段可能返回 null，表示取不到有效值。
        :type Schema: list of IntegrationNodeSchema
        :param NodeMapping: 节点映射
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeMapping: :class:`tencentcloud.wedata.v20210820.models.IntegrationNodeMapping`
        :param OwnerUin: owner uin
        :type OwnerUin: str
        """
        self.Name = None
        self.NodeType = None
        self.DataSourceType = None
        self.Description = None
        self.DatasourceId = None
        self.Config = None
        self.ExtConfig = None
        self.Schema = None
        self.NodeMapping = None
        self.OwnerUin = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.NodeType = params.get("NodeType")
        self.DataSourceType = params.get("DataSourceType")
        self.Description = params.get("Description")
        self.DatasourceId = params.get("DatasourceId")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = RecordField()
                obj._deserialize(item)
                self.Config.append(obj)
        if params.get("ExtConfig") is not None:
            self.ExtConfig = []
            for item in params.get("ExtConfig"):
                obj = RecordField()
                obj._deserialize(item)
                self.ExtConfig.append(obj)
        if params.get("Schema") is not None:
            self.Schema = []
            for item in params.get("Schema"):
                obj = IntegrationNodeSchema()
                obj._deserialize(item)
                self.Schema.append(obj)
        if params.get("NodeMapping") is not None:
            self.NodeMapping = IntegrationNodeMapping()
            self.NodeMapping._deserialize(params.get("NodeMapping"))
        self.OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationNodeInfo(AbstractModel):
    """集成节点

    """

    def __init__(self):
        r"""
        :param Id: 集成节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param TaskId: 集成节点所属任务id
        :type TaskId: str
        :param Name: 集成节点名称
        :type Name: str
        :param NodeType: 集成节点类型
        :type NodeType: str
        :param DataSourceType: 节点数据源类型
        :type DataSourceType: str
        :param Description: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param DatasourceId: 数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param Config: 节点配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: list of RecordField
        :param ExtConfig: 节点扩展配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtConfig: list of RecordField
        :param Schema: 节点schema
注意：此字段可能返回 null，表示取不到有效值。
        :type Schema: list of IntegrationNodeSchema
        :param NodeMapping: 节点映射
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeMapping: :class:`tencentcloud.wedata.v20210820.models.IntegrationNodeMapping`
        :param AppId: 应用id
        :type AppId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param CreatorUin: 创建人uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param OperatorUin: 操作人uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUin: str
        :param OwnerUin: owner uin
        :type OwnerUin: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Id = None
        self.TaskId = None
        self.Name = None
        self.NodeType = None
        self.DataSourceType = None
        self.Description = None
        self.DatasourceId = None
        self.Config = None
        self.ExtConfig = None
        self.Schema = None
        self.NodeMapping = None
        self.AppId = None
        self.ProjectId = None
        self.CreatorUin = None
        self.OperatorUin = None
        self.OwnerUin = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TaskId = params.get("TaskId")
        self.Name = params.get("Name")
        self.NodeType = params.get("NodeType")
        self.DataSourceType = params.get("DataSourceType")
        self.Description = params.get("Description")
        self.DatasourceId = params.get("DatasourceId")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = RecordField()
                obj._deserialize(item)
                self.Config.append(obj)
        if params.get("ExtConfig") is not None:
            self.ExtConfig = []
            for item in params.get("ExtConfig"):
                obj = RecordField()
                obj._deserialize(item)
                self.ExtConfig.append(obj)
        if params.get("Schema") is not None:
            self.Schema = []
            for item in params.get("Schema"):
                obj = IntegrationNodeSchema()
                obj._deserialize(item)
                self.Schema.append(obj)
        if params.get("NodeMapping") is not None:
            self.NodeMapping = IntegrationNodeMapping()
            self.NodeMapping._deserialize(params.get("NodeMapping"))
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.CreatorUin = params.get("CreatorUin")
        self.OperatorUin = params.get("OperatorUin")
        self.OwnerUin = params.get("OwnerUin")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationNodeMapping(AbstractModel):
    """集成节点映射

    """

    def __init__(self):
        r"""
        :param SourceId: 源节点id
        :type SourceId: str
        :param SinkId: 目标节点id
        :type SinkId: str
        :param SourceSchema: 源节点schema
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceSchema: list of IntegrationNodeSchema
        :param SchemaMappings: 节点schema映射
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaMappings: list of IntegrationNodeSchemaMapping
        :param ExtConfig: 节点映射扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtConfig: list of RecordField
        """
        self.SourceId = None
        self.SinkId = None
        self.SourceSchema = None
        self.SchemaMappings = None
        self.ExtConfig = None


    def _deserialize(self, params):
        self.SourceId = params.get("SourceId")
        self.SinkId = params.get("SinkId")
        if params.get("SourceSchema") is not None:
            self.SourceSchema = []
            for item in params.get("SourceSchema"):
                obj = IntegrationNodeSchema()
                obj._deserialize(item)
                self.SourceSchema.append(obj)
        if params.get("SchemaMappings") is not None:
            self.SchemaMappings = []
            for item in params.get("SchemaMappings"):
                obj = IntegrationNodeSchemaMapping()
                obj._deserialize(item)
                self.SchemaMappings.append(obj)
        if params.get("ExtConfig") is not None:
            self.ExtConfig = []
            for item in params.get("ExtConfig"):
                obj = RecordField()
                obj._deserialize(item)
                self.ExtConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationNodeSchema(AbstractModel):
    """集成节点schema

    """

    def __init__(self):
        r"""
        :param Id: schema id
        :type Id: str
        :param Name: schema名称
        :type Name: str
        :param Type: schema类型
        :type Type: str
        :param Value: schema值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Properties: schema拓展属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of RecordField
        :param Alias: schema别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Value = None
        self.Properties = None
        self.Alias = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = RecordField()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationNodeSchemaMapping(AbstractModel):
    """集成节点schema映射

    """

    def __init__(self):
        r"""
        :param SourceSchemaId: 源schema id
        :type SourceSchemaId: str
        :param SinkSchemaId: 目标schema id
        :type SinkSchemaId: str
        """
        self.SourceSchemaId = None
        self.SinkSchemaId = None


    def _deserialize(self, params):
        self.SourceSchemaId = params.get("SourceSchemaId")
        self.SinkSchemaId = params.get("SinkSchemaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationStatisticsTrendResult(AbstractModel):
    """数据集成大屏趋势图统计结果

    """

    def __init__(self):
        r"""
        :param StatisticName: 统计属性名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticName: list of str
        :param StatisticValue: 统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticValue: list of int
        :param StatisticType: 统计项目
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticType: str
        """
        self.StatisticName = None
        self.StatisticValue = None
        self.StatisticType = None


    def _deserialize(self, params):
        self.StatisticName = params.get("StatisticName")
        self.StatisticValue = params.get("StatisticValue")
        self.StatisticType = params.get("StatisticType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationTaskInfo(AbstractModel):
    """集成任务

    """

    def __init__(self):
        r"""
        :param TaskName: 任务名称
        :type TaskName: str
        :param Description: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param SyncType: 同步类型1.解决方案(整库迁移),2.单表同步
        :type SyncType: int
        :param TaskType: 201.实时,202.离线
        :type TaskType: int
        :param WorkflowId: 任务所属工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param ScheduleTaskId: 任务调度id(oceanus or us等作业id)
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTaskId: str
        :param TaskGroupId: 任务组id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupId: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param CreatorUin: 创建人uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param OperatorUin: 操作人uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUin: str
        :param OwnerUin: owner uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param AppId: 应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param Status: 任务状态1.初始化,2.操作中,3.运行中,4.暂停,5.任务停止中,6.停止,7.执行失败,8.已删除,9.已锁定,10.配置过期,11.提交中,12.提交成功,13.提交失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Nodes: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of IntegrationNodeInfo
        :param ExecutorId: 执行资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorId: str
        :param Config: 任务配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: list of RecordField
        :param ExtConfig: 任务扩展配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtConfig: list of RecordField
        :param ExecuteContext: 任务执行context信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteContext: list of RecordField
        :param Mappings: 节点映射
注意：此字段可能返回 null，表示取不到有效值。
        :type Mappings: list of IntegrationNodeMapping
        :param TaskMode: 任务模式：1.画布模式，2.flink jar
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMode: str
        :param Incharge: 责任人
注意：此字段可能返回 null，表示取不到有效值。
        :type Incharge: str
        :param OfflineTaskAddEntity: 离线新增参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTaskAddEntity: :class:`tencentcloud.wedata.v20210820.models.OfflineTaskAddParam`
        :param ExecutorGroupName: group name
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupName: str
        :param InLongManagerUrl: url
注意：此字段可能返回 null，表示取不到有效值。
        :type InLongManagerUrl: str
        :param InLongStreamId: stream id
注意：此字段可能返回 null，表示取不到有效值。
        :type InLongStreamId: str
        :param InLongManagerVersion: version
注意：此字段可能返回 null，表示取不到有效值。
        :type InLongManagerVersion: str
        """
        self.TaskName = None
        self.Description = None
        self.SyncType = None
        self.TaskType = None
        self.WorkflowId = None
        self.TaskId = None
        self.ScheduleTaskId = None
        self.TaskGroupId = None
        self.ProjectId = None
        self.CreatorUin = None
        self.OperatorUin = None
        self.OwnerUin = None
        self.AppId = None
        self.Status = None
        self.Nodes = None
        self.ExecutorId = None
        self.Config = None
        self.ExtConfig = None
        self.ExecuteContext = None
        self.Mappings = None
        self.TaskMode = None
        self.Incharge = None
        self.OfflineTaskAddEntity = None
        self.ExecutorGroupName = None
        self.InLongManagerUrl = None
        self.InLongStreamId = None
        self.InLongManagerVersion = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.Description = params.get("Description")
        self.SyncType = params.get("SyncType")
        self.TaskType = params.get("TaskType")
        self.WorkflowId = params.get("WorkflowId")
        self.TaskId = params.get("TaskId")
        self.ScheduleTaskId = params.get("ScheduleTaskId")
        self.TaskGroupId = params.get("TaskGroupId")
        self.ProjectId = params.get("ProjectId")
        self.CreatorUin = params.get("CreatorUin")
        self.OperatorUin = params.get("OperatorUin")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.Status = params.get("Status")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = IntegrationNodeInfo()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.ExecutorId = params.get("ExecutorId")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = RecordField()
                obj._deserialize(item)
                self.Config.append(obj)
        if params.get("ExtConfig") is not None:
            self.ExtConfig = []
            for item in params.get("ExtConfig"):
                obj = RecordField()
                obj._deserialize(item)
                self.ExtConfig.append(obj)
        if params.get("ExecuteContext") is not None:
            self.ExecuteContext = []
            for item in params.get("ExecuteContext"):
                obj = RecordField()
                obj._deserialize(item)
                self.ExecuteContext.append(obj)
        if params.get("Mappings") is not None:
            self.Mappings = []
            for item in params.get("Mappings"):
                obj = IntegrationNodeMapping()
                obj._deserialize(item)
                self.Mappings.append(obj)
        self.TaskMode = params.get("TaskMode")
        self.Incharge = params.get("Incharge")
        if params.get("OfflineTaskAddEntity") is not None:
            self.OfflineTaskAddEntity = OfflineTaskAddParam()
            self.OfflineTaskAddEntity._deserialize(params.get("OfflineTaskAddEntity"))
        self.ExecutorGroupName = params.get("ExecutorGroupName")
        self.InLongManagerUrl = params.get("InLongManagerUrl")
        self.InLongStreamId = params.get("InLongStreamId")
        self.InLongManagerVersion = params.get("InLongManagerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillInstancesRequest(AbstractModel):
    """KillInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Instances: 实例嵌套集合
        :type Instances: list of InstanceInfo
        """
        self.ProjectId = None
        self.Instances = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillInstancesResponse(AbstractModel):
    """KillInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回实例批量终止结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class Label(AbstractModel):
    """标签类型

    """

    def __init__(self):
        r"""
        :param Value: 类型值。
        :type Value: str
        :param Text: 类型名称。
        :type Text: str
        """
        self.Value = None
        self.Text = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockIntegrationTaskRequest(AbstractModel):
    """LockIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockIntegrationTaskResponse(AbstractModel):
    """LockIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class LogContent(AbstractModel):
    """实时任务日志内容

    """

    def __init__(self):
        r"""
        :param Time: 日志时间戳，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param PkgId: 日志包id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param Log: 日志内容
        :type Log: str
        """
        self.Time = None
        self.PkgId = None
        self.Log = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.PkgId = params.get("PkgId")
        self.Log = params.get("Log")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContentInfo(AbstractModel):
    """日志内容实体

    """

    def __init__(self):
        r"""
        :param Log: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param PkgId: 日志组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgLogId: 日志Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgLogId: str
        :param Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param ContainerName: 日志所属的容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        """
        self.Log = None
        self.PkgId = None
        self.PkgLogId = None
        self.Time = None
        self.ContainerName = None


    def _deserialize(self, params):
        self.Log = params.get("Log")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.Time = params.get("Time")
        self.ContainerName = params.get("ContainerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MakeUpTasksNewRequest(AbstractModel):
    """MakeUpTasksNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIdList: 补录的当前任务的taskId数组
        :type TaskIdList: list of str
        :param StartTime: 补录开始时间
        :type StartTime: str
        :param EndTime: 补录结束时间
        :type EndTime: str
        :param MakeUpType: 补录选项标识，1表示当前任务；2表示当前及下游任务；3表示下游任务
        :type MakeUpType: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param CheckParent: true: 检查父任务实例状态；false: 不检查父任务实例状态
        :type CheckParent: bool
        """
        self.TaskIdList = None
        self.StartTime = None
        self.EndTime = None
        self.MakeUpType = None
        self.ProjectId = None
        self.CheckParent = None


    def _deserialize(self, params):
        self.TaskIdList = params.get("TaskIdList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MakeUpType = params.get("MakeUpType")
        self.ProjectId = params.get("ProjectId")
        self.CheckParent = params.get("CheckParent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MakeUpTasksNewResponse(AbstractModel):
    """MakeUpTasksNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回批量操作成功个数、失败个数、操作总数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class MakeUpWorkflowNewRequest(AbstractModel):
    """MakeUpWorkflowNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkFlowId: 工作流id
        :type WorkFlowId: str
        :param StartTime: 补录开始时间
        :type StartTime: str
        :param EndTime: 补录结束时间
        :type EndTime: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.WorkFlowId = None
        self.StartTime = None
        self.EndTime = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.WorkFlowId = params.get("WorkFlowId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MakeUpWorkflowNewResponse(AbstractModel):
    """MakeUpWorkflowNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回补录成功或失败的任务数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyDataSourceRequest(AbstractModel):
    """ModifyDataSource请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 数据源名称，在相同SpaceName下，数据源名称不能为空
        :type Name: str
        :param Category: 数据源类别：绑定引擎、绑定数据库
        :type Category: str
        :param Type: 数据源类型:枚举值
        :type Type: str
        :param ID: 数据源ID
        :type ID: int
        :param BizParams: 业务侧数据源的配置信息扩展
        :type BizParams: str
        :param Params: 数据源的配置信息，以JSON KV存储，根据每个数据源类型不同，而KV存储信息不同
        :type Params: str
        :param Description: 数据源描述信息
        :type Description: str
        :param Display: 数据源展示名，为了可视化查看
        :type Display: str
        :param DatabaseName: 若数据源列表为绑定数据库，则为db名称
        :type DatabaseName: str
        :param Instance: 数据源引擎的实例ID，如CDB实例ID
        :type Instance: str
        :param Status: 数据源数据源的可见性，1为可见、0为不可见。默认为1
        :type Status: int
        :param ClusterId: 数据源所属的业务空间名称
        :type ClusterId: str
        :param Collect: 是否采集
        :type Collect: str
        :param OwnerProjectId: 项目id
        :type OwnerProjectId: str
        :param OwnerProjectName: 项目名称
        :type OwnerProjectName: str
        :param OwnerProjectIdent: 项目中文名
        :type OwnerProjectIdent: str
        :param COSBucket: cos bucket
        :type COSBucket: str
        :param COSRegion: cos region
        :type COSRegion: str
        """
        self.Name = None
        self.Category = None
        self.Type = None
        self.ID = None
        self.BizParams = None
        self.Params = None
        self.Description = None
        self.Display = None
        self.DatabaseName = None
        self.Instance = None
        self.Status = None
        self.ClusterId = None
        self.Collect = None
        self.OwnerProjectId = None
        self.OwnerProjectName = None
        self.OwnerProjectIdent = None
        self.COSBucket = None
        self.COSRegion = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Category = params.get("Category")
        self.Type = params.get("Type")
        self.ID = params.get("ID")
        self.BizParams = params.get("BizParams")
        self.Params = params.get("Params")
        self.Description = params.get("Description")
        self.Display = params.get("Display")
        self.DatabaseName = params.get("DatabaseName")
        self.Instance = params.get("Instance")
        self.Status = params.get("Status")
        self.ClusterId = params.get("ClusterId")
        self.Collect = params.get("Collect")
        self.OwnerProjectId = params.get("OwnerProjectId")
        self.OwnerProjectName = params.get("OwnerProjectName")
        self.OwnerProjectIdent = params.get("OwnerProjectIdent")
        self.COSBucket = params.get("COSBucket")
        self.COSRegion = params.get("COSRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataSourceResponse(AbstractModel):
    """ModifyDataSource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyDimensionWeightRequest(AbstractModel):
    """ModifyDimensionWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param WeightInfoList: 权重信息列表
        :type WeightInfoList: list of WeightInfo
        :param ProjectId: 项目id
        :type ProjectId: str
        :param Refresh: 是否重刷历史数据
        :type Refresh: bool
        """
        self.WeightInfoList = None
        self.ProjectId = None
        self.Refresh = None


    def _deserialize(self, params):
        if params.get("WeightInfoList") is not None:
            self.WeightInfoList = []
            for item in params.get("WeightInfoList"):
                obj = WeightInfo()
                obj._deserialize(item)
                self.WeightInfoList.append(obj)
        self.ProjectId = params.get("ProjectId")
        self.Refresh = params.get("Refresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDimensionWeightResponse(AbstractModel):
    """ModifyDimensionWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 更新权重是否成功
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyExecStrategyRequest(AbstractModel):
    """ModifyExecStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param MonitorType: 监控类型 1.未配置, 2.关联生产调度, 3.离线周期检测
        :type MonitorType: int
        :param ExecQueue: 计算队列
        :type ExecQueue: str
        :param ExecutorGroupId: 执行资源组ID
        :type ExecutorGroupId: str
        :param ExecutorGroupName: 执行资源组名称
        :type ExecutorGroupName: str
        :param Tasks: 关联的生产调度任务列表
        :type Tasks: list of ProdSchedulerTask
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param StartTime: 离线周期模式下,生效日期-开始时间
        :type StartTime: str
        :param EndTime: 离线周期模式下,生效日期-结束时间
        :type EndTime: str
        :param CycleType: 离线周期模式下,调度周期 
MINUTE_CYCLE:I,
HOUR_CYCLE:H,
DAY_CYCLE:D,
WEEK_CYCLE:W,
MONTH_CYCLE:M
        :type CycleType: str
        :param CycleStep: 离线周期模式下,调度步长
        :type CycleStep: int
        :param TaskAction: 离线周期模式下,指定时间
        :type TaskAction: str
        :param DelayTime: 延时执行时间，单位分钟，可选: <0-1439
        :type DelayTime: int
        :param DatabaseId: 数据库Id
        :type DatabaseId: str
        :param DatasourceId: 数据源Id
        :type DatasourceId: str
        :param TableId: 数据表Id
        :type TableId: str
        """
        self.RuleGroupId = None
        self.MonitorType = None
        self.ExecQueue = None
        self.ExecutorGroupId = None
        self.ExecutorGroupName = None
        self.Tasks = None
        self.ProjectId = None
        self.StartTime = None
        self.EndTime = None
        self.CycleType = None
        self.CycleStep = None
        self.TaskAction = None
        self.DelayTime = None
        self.DatabaseId = None
        self.DatasourceId = None
        self.TableId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.MonitorType = params.get("MonitorType")
        self.ExecQueue = params.get("ExecQueue")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.ExecutorGroupName = params.get("ExecutorGroupName")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ProdSchedulerTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.ProjectId = params.get("ProjectId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.TaskAction = params.get("TaskAction")
        self.DelayTime = params.get("DelayTime")
        self.DatabaseId = params.get("DatabaseId")
        self.DatasourceId = params.get("DatasourceId")
        self.TableId = params.get("TableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExecStrategyResponse(AbstractModel):
    """ModifyExecStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyFolderRequest(AbstractModel):
    """ModifyFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param FolderName: 文件夹名称
        :type FolderName: str
        :param FolderId: 文件夹Id
        :type FolderId: str
        :param ParentsFolderId: 父文件夹ID
        :type ParentsFolderId: str
        """
        self.ProjectId = None
        self.FolderName = None
        self.FolderId = None
        self.ParentsFolderId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.FolderName = params.get("FolderName")
        self.FolderId = params.get("FolderId")
        self.ParentsFolderId = params.get("ParentsFolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFolderResponse(AbstractModel):
    """ModifyFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: true代表成功，false代表失败
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyIntegrationNodeRequest(AbstractModel):
    """ModifyIntegrationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeInfo: 集成节点信息
        :type NodeInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationNodeInfo`
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型
        :type TaskType: int
        :param TaskMode: 区分画布模式和表单模式
        :type TaskMode: int
        """
        self.NodeInfo = None
        self.ProjectId = None
        self.TaskType = None
        self.TaskMode = None


    def _deserialize(self, params):
        if params.get("NodeInfo") is not None:
            self.NodeInfo = IntegrationNodeInfo()
            self.NodeInfo._deserialize(params.get("NodeInfo"))
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        self.TaskMode = params.get("TaskMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIntegrationNodeResponse(AbstractModel):
    """ModifyIntegrationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 节点id
        :type Id: str
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyIntegrationTaskRequest(AbstractModel):
    """ModifyIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.wedata.v20210820.models.IntegrationTaskInfo`
        :param ProjectId: 项目id
        :type ProjectId: str
        :param RollbackFlag: 默认false . 为true时表示走回滚节点逻辑
        :type RollbackFlag: bool
        """
        self.TaskInfo = None
        self.ProjectId = None
        self.RollbackFlag = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = IntegrationTaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.ProjectId = params.get("ProjectId")
        self.RollbackFlag = params.get("RollbackFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIntegrationTaskResponse(AbstractModel):
    """ModifyIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyMonitorStatusRequest(AbstractModel):
    """ModifyMonitorStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param MonitorStatus: 监控开关状态
        :type MonitorStatus: bool
        """
        self.ProjectId = None
        self.RuleGroupId = None
        self.MonitorStatus = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.MonitorStatus = params.get("MonitorStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMonitorStatusResponse(AbstractModel):
    """ModifyMonitorStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 监控状态修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyRuleGroupSubscriptionRequest(AbstractModel):
    """ModifyRuleGroupSubscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param Receivers: 订阅人信息
        :type Receivers: list of SubscribeReceiver
        :param SubscribeType: 订阅类型
        :type SubscribeType: list of int non-negative
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DatabaseId: 数据库Id
        :type DatabaseId: str
        :param DatasourceId: 数据源Id
        :type DatasourceId: str
        :param TableId: 数据表Id
        :type TableId: str
        :param WebHooks: 群机器人webhook信息
        :type WebHooks: list of SubscribeWebHook
        """
        self.RuleGroupId = None
        self.Receivers = None
        self.SubscribeType = None
        self.ProjectId = None
        self.DatabaseId = None
        self.DatasourceId = None
        self.TableId = None
        self.WebHooks = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        if params.get("Receivers") is not None:
            self.Receivers = []
            for item in params.get("Receivers"):
                obj = SubscribeReceiver()
                obj._deserialize(item)
                self.Receivers.append(obj)
        self.SubscribeType = params.get("SubscribeType")
        self.ProjectId = params.get("ProjectId")
        self.DatabaseId = params.get("DatabaseId")
        self.DatasourceId = params.get("DatasourceId")
        self.TableId = params.get("TableId")
        if params.get("WebHooks") is not None:
            self.WebHooks = []
            for item in params.get("WebHooks"):
                obj = SubscribeWebHook()
                obj._deserialize(item)
                self.WebHooks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleGroupSubscriptionResponse(AbstractModel):
    """ModifyRuleGroupSubscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param RuleId: 规则ID
        :type RuleId: int
        :param RuleGroupId: 规则组ID
        :type RuleGroupId: int
        :param Name: 规则名称
        :type Name: str
        :param TableId: 数据表ID
        :type TableId: str
        :param RuleTemplateId: 规则模板ID
        :type RuleTemplateId: int
        :param Type: 规则类型 1.系统模版, 2.自定义模版, 3.自定义SQL
        :type Type: int
        :param QualityDim: 规则所属质量维度（1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
        :type QualityDim: int
        :param SourceObjectDataTypeName: 源字段详细类型，int、string
        :type SourceObjectDataTypeName: str
        :param SourceObjectValue: 源字段名称
        :type SourceObjectValue: str
        :param ConditionType: 检测范围 1.全表   2.条件扫描
        :type ConditionType: int
        :param ConditionExpression: 条件扫描WHERE条件表达式
        :type ConditionExpression: str
        :param CustomSql: 自定义SQL
        :type CustomSql: str
        :param CompareRule: 报警触发条件
        :type CompareRule: :class:`tencentcloud.wedata.v20210820.models.CompareRule`
        :param AlarmLevel: 报警触发级别 1.低, 2.中, 3.高
        :type AlarmLevel: int
        :param Description: 规则描述
        :type Description: str
        :param TargetDatabaseId: 目标库Id
        :type TargetDatabaseId: str
        :param TargetTableId: 目标表Id
        :type TargetTableId: str
        :param TargetConditionExpr: 目标过滤条件表达式
        :type TargetConditionExpr: str
        :param RelConditionExpr: 源字段与目标字段关联条件on表达式
        :type RelConditionExpr: str
        :param FieldConfig: 自定义模版sql表达式字段替换参数
        :type FieldConfig: :class:`tencentcloud.wedata.v20210820.models.RuleFieldConfig`
        :param TargetObjectValue: 目标字段名称  CITY
        :type TargetObjectValue: str
        """
        self.ProjectId = None
        self.RuleId = None
        self.RuleGroupId = None
        self.Name = None
        self.TableId = None
        self.RuleTemplateId = None
        self.Type = None
        self.QualityDim = None
        self.SourceObjectDataTypeName = None
        self.SourceObjectValue = None
        self.ConditionType = None
        self.ConditionExpression = None
        self.CustomSql = None
        self.CompareRule = None
        self.AlarmLevel = None
        self.Description = None
        self.TargetDatabaseId = None
        self.TargetTableId = None
        self.TargetConditionExpr = None
        self.RelConditionExpr = None
        self.FieldConfig = None
        self.TargetObjectValue = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RuleId = params.get("RuleId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.Name = params.get("Name")
        self.TableId = params.get("TableId")
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.Type = params.get("Type")
        self.QualityDim = params.get("QualityDim")
        self.SourceObjectDataTypeName = params.get("SourceObjectDataTypeName")
        self.SourceObjectValue = params.get("SourceObjectValue")
        self.ConditionType = params.get("ConditionType")
        self.ConditionExpression = params.get("ConditionExpression")
        self.CustomSql = params.get("CustomSql")
        if params.get("CompareRule") is not None:
            self.CompareRule = CompareRule()
            self.CompareRule._deserialize(params.get("CompareRule"))
        self.AlarmLevel = params.get("AlarmLevel")
        self.Description = params.get("Description")
        self.TargetDatabaseId = params.get("TargetDatabaseId")
        self.TargetTableId = params.get("TargetTableId")
        self.TargetConditionExpr = params.get("TargetConditionExpr")
        self.RelConditionExpr = params.get("RelConditionExpr")
        if params.get("FieldConfig") is not None:
            self.FieldConfig = RuleFieldConfig()
            self.FieldConfig._deserialize(params.get("FieldConfig"))
        self.TargetObjectValue = params.get("TargetObjectValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 是否更新成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyRuleTemplateRequest(AbstractModel):
    """ModifyRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模版ID
        :type TemplateId: int
        :param Type: 模版类型  1.系统模版   2.自定义模版
        :type Type: int
        :param Name: 模版名称
        :type Name: str
        :param QualityDim: 质量检测维度 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性
        :type QualityDim: int
        :param SourceObjectType: 源端数据对象类型 1.常量  2.离线表级   2.离线字段级
        :type SourceObjectType: int
        :param Description: 描述
        :type Description: str
        :param SourceEngineTypes: 源端对应的引擎类型
        :type SourceEngineTypes: list of int non-negative
        :param MultiSourceFlag: 是否关联其它库表
        :type MultiSourceFlag: bool
        :param SqlExpression: SQL 表达式
        :type SqlExpression: str
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WhereFlag: 是否添加where参数
        :type WhereFlag: bool
        """
        self.TemplateId = None
        self.Type = None
        self.Name = None
        self.QualityDim = None
        self.SourceObjectType = None
        self.Description = None
        self.SourceEngineTypes = None
        self.MultiSourceFlag = None
        self.SqlExpression = None
        self.ProjectId = None
        self.WhereFlag = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.QualityDim = params.get("QualityDim")
        self.SourceObjectType = params.get("SourceObjectType")
        self.Description = params.get("Description")
        self.SourceEngineTypes = params.get("SourceEngineTypes")
        self.MultiSourceFlag = params.get("MultiSourceFlag")
        self.SqlExpression = params.get("SqlExpression")
        self.ProjectId = params.get("ProjectId")
        self.WhereFlag = params.get("WhereFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleTemplateResponse(AbstractModel):
    """ModifyRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyTaskAlarmRegularRequest(AbstractModel):
    """ModifyTaskAlarmRegular请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 主键ID
        :type Id: str
        :param TaskAlarmInfo: 规则信息
        :type TaskAlarmInfo: :class:`tencentcloud.wedata.v20210820.models.TaskAlarmInfo`
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.Id = None
        self.TaskAlarmInfo = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("TaskAlarmInfo") is not None:
            self.TaskAlarmInfo = TaskAlarmInfo()
            self.TaskAlarmInfo._deserialize(params.get("TaskAlarmInfo"))
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskAlarmRegularResponse(AbstractModel):
    """ModifyTaskAlarmRegular返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 判断是否修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyTaskInfoRequest(AbstractModel):
    """ModifyTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param DelayTime: 执行时间，单位分钟，天/周/月/年调度才有。比如天调度，每天的02:00点执行一次，delayTime就是120分钟
        :type DelayTime: int
        :param StartupTime: 启动时间
        :type StartupTime: int
        :param SelfDepend: 自依赖类型  1:有序串行 一次一个 排队, 2: 无序串行 一次一个 不排队， 3:并行 一次多个
        :type SelfDepend: int
        :param StartTime: 生效开始时间，格式 yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 生效结束时间，格式 yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param TaskAction: 调度配置-弹性周期配置，小时/周/月/年调度才有，小时任务指定每天的0点3点4点跑，则为'0,3,4'。
        :type TaskAction: str
        :param CycleType: "周期类型  0:crontab类型, 1:分钟，2:小时，3:天，4:周，5:月，6:一次性，7:用户驱动，10:弹性周期 周,11:弹性周期 月,12:年,13:即时触发Instant类型，与正常周期调度任务逻辑隔离
        :type CycleType: int
        :param CycleStep: 步长，间隔时间，最小1
        :type CycleStep: int
        :param CrontabExpression: cron表达式  周期类型为crontab调度才需要
        :type CrontabExpression: str
        :param ExecutionStartTime: 执行时间左闭区间，格式：HH:mm  小时调度才有，例如小时任务, 每日固定区间生效
        :type ExecutionStartTime: str
        :param ExecutionEndTime: 执行时间右闭区间，格式：HH:mm  小时调度才有，例如小时任务, 每日固定区间生效
        :type ExecutionEndTime: str
        :param TaskName: 新的任务名
        :type TaskName: str
        :param RetryWait: 失败重试间隔,单位分钟，创建任务的时候已经给了默认值
        :type RetryWait: int
        :param TryLimit: 失败重试次数，创建任务的时候已经给了默认值
        :type TryLimit: int
        :param Retriable: 是否可重试，1代表可以重试
        :type Retriable: int
        :param RunPriority: 运行优先级，4高 5中 6低
        :type RunPriority: int
        :param TaskExt: 任务的扩展配置
        :type TaskExt: list of TaskExtInfo
        :param ResourceGroup: 执行资源组id，需要去资源管理服务上创建调度资源组，并且绑定cvm机器
        :type ResourceGroup: str
        :param YarnQueue: 资源池队列名称
        :type YarnQueue: str
        :param BrokerIp: 资源组下具体执行机，any 表示可以跑在任意一台。
        :type BrokerIp: str
        :param InCharge: 责任人
        :type InCharge: str
        :param Notes: 任务备注
        :type Notes: str
        :param TaskParamInfos: 任务参数
        :type TaskParamInfos: list of ParamInfo
        :param SourceServer: 源数据源
        :type SourceServer: str
        :param TargetServer: 目标数据源
        :type TargetServer: str
        :param DependencyWorkflow: 是否支持工作流依赖 yes / no 默认 no
        :type DependencyWorkflow: str
        :param DependencyConfigDTOs: 依赖配置
        :type DependencyConfigDTOs: list of DependencyConfig
        """
        self.ProjectId = None
        self.TaskId = None
        self.DelayTime = None
        self.StartupTime = None
        self.SelfDepend = None
        self.StartTime = None
        self.EndTime = None
        self.TaskAction = None
        self.CycleType = None
        self.CycleStep = None
        self.CrontabExpression = None
        self.ExecutionStartTime = None
        self.ExecutionEndTime = None
        self.TaskName = None
        self.RetryWait = None
        self.TryLimit = None
        self.Retriable = None
        self.RunPriority = None
        self.TaskExt = None
        self.ResourceGroup = None
        self.YarnQueue = None
        self.BrokerIp = None
        self.InCharge = None
        self.Notes = None
        self.TaskParamInfos = None
        self.SourceServer = None
        self.TargetServer = None
        self.DependencyWorkflow = None
        self.DependencyConfigDTOs = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.DelayTime = params.get("DelayTime")
        self.StartupTime = params.get("StartupTime")
        self.SelfDepend = params.get("SelfDepend")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskAction = params.get("TaskAction")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.CrontabExpression = params.get("CrontabExpression")
        self.ExecutionStartTime = params.get("ExecutionStartTime")
        self.ExecutionEndTime = params.get("ExecutionEndTime")
        self.TaskName = params.get("TaskName")
        self.RetryWait = params.get("RetryWait")
        self.TryLimit = params.get("TryLimit")
        self.Retriable = params.get("Retriable")
        self.RunPriority = params.get("RunPriority")
        if params.get("TaskExt") is not None:
            self.TaskExt = []
            for item in params.get("TaskExt"):
                obj = TaskExtInfo()
                obj._deserialize(item)
                self.TaskExt.append(obj)
        self.ResourceGroup = params.get("ResourceGroup")
        self.YarnQueue = params.get("YarnQueue")
        self.BrokerIp = params.get("BrokerIp")
        self.InCharge = params.get("InCharge")
        self.Notes = params.get("Notes")
        if params.get("TaskParamInfos") is not None:
            self.TaskParamInfos = []
            for item in params.get("TaskParamInfos"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.TaskParamInfos.append(obj)
        self.SourceServer = params.get("SourceServer")
        self.TargetServer = params.get("TargetServer")
        self.DependencyWorkflow = params.get("DependencyWorkflow")
        if params.get("DependencyConfigDTOs") is not None:
            self.DependencyConfigDTOs = []
            for item in params.get("DependencyConfigDTOs"):
                obj = DependencyConfig()
                obj._deserialize(item)
                self.DependencyConfigDTOs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskInfoResponse(AbstractModel):
    """ModifyTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 执行结果
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyTaskLinksRequest(AbstractModel):
    """ModifyTaskLinks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskFrom: 父任务ID
        :type TaskFrom: str
        :param TaskTo: 子任务ID
        :type TaskTo: str
        :param WorkflowId: 子任务工作流
        :type WorkflowId: str
        :param RealFromWorkflowId: 父任务工作流
        :type RealFromWorkflowId: str
        :param LinkDependencyType: 父子任务之间的依赖关系
        :type LinkDependencyType: str
        """
        self.ProjectId = None
        self.TaskFrom = None
        self.TaskTo = None
        self.WorkflowId = None
        self.RealFromWorkflowId = None
        self.LinkDependencyType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskFrom = params.get("TaskFrom")
        self.TaskTo = params.get("TaskTo")
        self.WorkflowId = params.get("WorkflowId")
        self.RealFromWorkflowId = params.get("RealFromWorkflowId")
        self.LinkDependencyType = params.get("LinkDependencyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskLinksResponse(AbstractModel):
    """ModifyTaskLinks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 成功或者失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyTaskNameRequest(AbstractModel):
    """ModifyTaskName请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskName: 名称
        :type TaskName: str
        :param TaskId: id
        :type TaskId: str
        :param ProjectId: 项目/工作空间id
        :type ProjectId: str
        :param Notes: 备注
        :type Notes: str
        """
        self.TaskName = None
        self.TaskId = None
        self.ProjectId = None
        self.Notes = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskNameResponse(AbstractModel):
    """ModifyTaskName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyTaskScriptRequest(AbstractModel):
    """ModifyTaskScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param ScriptContent: 脚本内容 base64编码
        :type ScriptContent: str
        :param IntegrationNodeDetails: 集成任务脚本配置
        :type IntegrationNodeDetails: list of IntegrationNodeDetail
        """
        self.ProjectId = None
        self.TaskId = None
        self.ScriptContent = None
        self.IntegrationNodeDetails = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.ScriptContent = params.get("ScriptContent")
        if params.get("IntegrationNodeDetails") is not None:
            self.IntegrationNodeDetails = []
            for item in params.get("IntegrationNodeDetails"):
                obj = IntegrationNodeDetail()
                obj._deserialize(item)
                self.IntegrationNodeDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskScriptResponse(AbstractModel):
    """ModifyTaskScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.CommonContent`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CommonContent()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyWorkflowInfoRequest(AbstractModel):
    """ModifyWorkflowInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param Owner: 责任人
        :type Owner: str
        :param OwnerId: 责任人id
        :type OwnerId: str
        :param WorkflowDesc: 备注
        :type WorkflowDesc: str
        :param WorkflowName: 工作流名称
        :type WorkflowName: str
        :param FolderId: 所属文件夹id
        :type FolderId: str
        :param UserGroupId: 工作流所属用户分组id  若有多个,分号隔开: a;b;c
        :type UserGroupId: str
        :param UserGroupName: 工作流所属用户分组名称  若有多个,分号隔开: a;b;c
        :type UserGroupName: str
        :param WorkflowParams: 工作流参数列表
        :type WorkflowParams: list of ParamInfo
        :param GeneralTaskParams: 用于配置优化参数（线程、内存、CPU核数等），仅作用于Spark SQL节点。多个参数用英文分号分隔。
        :type GeneralTaskParams: list of GeneralTaskParam
        """
        self.ProjectId = None
        self.WorkflowId = None
        self.Owner = None
        self.OwnerId = None
        self.WorkflowDesc = None
        self.WorkflowName = None
        self.FolderId = None
        self.UserGroupId = None
        self.UserGroupName = None
        self.WorkflowParams = None
        self.GeneralTaskParams = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        self.Owner = params.get("Owner")
        self.OwnerId = params.get("OwnerId")
        self.WorkflowDesc = params.get("WorkflowDesc")
        self.WorkflowName = params.get("WorkflowName")
        self.FolderId = params.get("FolderId")
        self.UserGroupId = params.get("UserGroupId")
        self.UserGroupName = params.get("UserGroupName")
        if params.get("WorkflowParams") is not None:
            self.WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.WorkflowParams.append(obj)
        if params.get("GeneralTaskParams") is not None:
            self.GeneralTaskParams = []
            for item in params.get("GeneralTaskParams"):
                obj = GeneralTaskParam()
                obj._deserialize(item)
                self.GeneralTaskParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkflowInfoResponse(AbstractModel):
    """ModifyWorkflowInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: true代表成功，false代表失败
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyWorkflowScheduleRequest(AbstractModel):
    """ModifyWorkflowSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param DelayTime: 延迟时间，单位分钟
        :type DelayTime: int
        :param StartupTime: 启动时间
        :type StartupTime: int
        :param SelfDepend: 自依赖类型  1:有序串行 一次一个 排队, 2: 无序串行 一次一个 不排队， 3:并行 一次多个
        :type SelfDepend: int
        :param CycleType: "周期类型  0:crontab类型, 1:分钟，2:小时，3:天，4:周，5:月，6:一次性，7:用户驱动，10:弹性周期 周,11:弹性周期 月,12:年,13:即时触发Instant类型，与正常周期调度任务逻辑隔离
        :type CycleType: int
        :param CycleStep: 步长，间隔时间，最小1
        :type CycleStep: int
        :param StartTime: 生效开始时间，格式 yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 生效结束时间，格式 yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param TaskAction: 调度配置-弹性周期配置，小时/周/月/年调度才有，小时任务指定每天的0点3点4点跑，则为'0,3,4'。
        :type TaskAction: str
        :param CrontabExpression: cron表达式  周期类型为crontab调度才需要
        :type CrontabExpression: str
        :param ExecutionStartTime: 执行时间左闭区间，格式：HH:mm  小时调度才有，例如小时任务, 每日固定区间生效
        :type ExecutionStartTime: str
        :param ExecutionEndTime: 执行时间右闭区间，格式：HH:mm  小时调度才有，例如小时任务, 每日固定区间生效
        :type ExecutionEndTime: str
        :param DependencyWorkflow: 工作流依赖 ,yes 或者no
        :type DependencyWorkflow: str
        """
        self.ProjectId = None
        self.WorkflowId = None
        self.DelayTime = None
        self.StartupTime = None
        self.SelfDepend = None
        self.CycleType = None
        self.CycleStep = None
        self.StartTime = None
        self.EndTime = None
        self.TaskAction = None
        self.CrontabExpression = None
        self.ExecutionStartTime = None
        self.ExecutionEndTime = None
        self.DependencyWorkflow = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        self.DelayTime = params.get("DelayTime")
        self.StartupTime = params.get("StartupTime")
        self.SelfDepend = params.get("SelfDepend")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskAction = params.get("TaskAction")
        self.CrontabExpression = params.get("CrontabExpression")
        self.ExecutionStartTime = params.get("ExecutionStartTime")
        self.ExecutionEndTime = params.get("ExecutionEndTime")
        self.DependencyWorkflow = params.get("DependencyWorkflow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkflowScheduleResponse(AbstractModel):
    """ModifyWorkflowSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Status: 当前状态
        :type Status: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        """
        self.Name = None
        self.Status = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstance(AbstractModel):
    """离线实例

    """

    def __init__(self):
        r"""
        :param CreateUin: 创建账号
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param OperatorUin: 操作账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUin: str
        :param OwnerUin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param AppId: 账号
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param WorkspaceId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param TaskId: 任务Id
        :type TaskId: str
        :param CurRunDate: 数据时间
        :type CurRunDate: str
        :param IssueId: 下发时间
        :type IssueId: str
        :param InlongTaskId: 资源组id
注意：此字段可能返回 null，表示取不到有效值。
        :type InlongTaskId: str
        :param ResourceGroup: 资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroup: str
        :param TaskRunType: 实例类型
        :type TaskRunType: int
        :param State: 实例状态
        :type State: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 最后更新时间
        :type UpdateTime: str
        :param InstanceKey: 唯一key
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        """
        self.CreateUin = None
        self.OperatorUin = None
        self.OwnerUin = None
        self.AppId = None
        self.WorkspaceId = None
        self.TaskId = None
        self.CurRunDate = None
        self.IssueId = None
        self.InlongTaskId = None
        self.ResourceGroup = None
        self.TaskRunType = None
        self.State = None
        self.StartTime = None
        self.EndTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.InstanceKey = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.OperatorUin = params.get("OperatorUin")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.WorkspaceId = params.get("WorkspaceId")
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.IssueId = params.get("IssueId")
        self.InlongTaskId = params.get("InlongTaskId")
        self.ResourceGroup = params.get("ResourceGroup")
        self.TaskRunType = params.get("TaskRunType")
        self.State = params.get("State")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.InstanceKey = params.get("InstanceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineTaskAddParam(AbstractModel):
    """离线任务新增参数

    """

    def __init__(self):
        r"""
        :param WorkflowName: 名称
        :type WorkflowName: str
        :param DependencyWorkflow: 依赖
        :type DependencyWorkflow: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param CycleType: 周期
        :type CycleType: int
        :param CycleStep: 周期间隔
        :type CycleStep: int
        :param DelayTime: 延迟时间
        :type DelayTime: int
        :param CrontabExpression: crontab
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        :param RetryWait: 重试等待
        :type RetryWait: int
        :param Retriable: 是否可以重试
        :type Retriable: int
        :param TryLimit: 重试限制
        :type TryLimit: int
        :param RunPriority: 优先级
        :type RunPriority: int
        :param ProductName: 产品名称
        :type ProductName: str
        :param SelfDepend: 1 有序串行 一次一个，排队 orderly 
2 无序串行 一次一个，不排队 serial  
3 并行 一次多个 parallel
        :type SelfDepend: int
        :param TaskAction: 周任务：1是周天，2是周1，7是周6 。
月任务：如具体1，3号则写 "1,3"，指定月末不可和具体号数一起输入，仅能为 "L"
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        :param ExecutionEndTime: 调度执行结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        :param ExecutionStartTime: 调度执行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        """
        self.WorkflowName = None
        self.DependencyWorkflow = None
        self.StartTime = None
        self.EndTime = None
        self.CycleType = None
        self.CycleStep = None
        self.DelayTime = None
        self.CrontabExpression = None
        self.RetryWait = None
        self.Retriable = None
        self.TryLimit = None
        self.RunPriority = None
        self.ProductName = None
        self.SelfDepend = None
        self.TaskAction = None
        self.ExecutionEndTime = None
        self.ExecutionStartTime = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        self.DependencyWorkflow = params.get("DependencyWorkflow")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.DelayTime = params.get("DelayTime")
        self.CrontabExpression = params.get("CrontabExpression")
        self.RetryWait = params.get("RetryWait")
        self.Retriable = params.get("Retriable")
        self.TryLimit = params.get("TryLimit")
        self.RunPriority = params.get("RunPriority")
        self.ProductName = params.get("ProductName")
        self.SelfDepend = params.get("SelfDepend")
        self.TaskAction = params.get("TaskAction")
        self.ExecutionEndTime = params.get("ExecutionEndTime")
        self.ExecutionStartTime = params.get("ExecutionStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateResult(AbstractModel):
    """操作结果

    """

    def __init__(self):
        r"""
        :param Result: 操作结果；true表示成功；false表示失败
        :type Result: bool
        :param ErrorId: 错误编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorId: str
        :param ErrorDesc: 操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDesc: str
        """
        self.Result = None
        self.ErrorId = None
        self.ErrorDesc = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ErrorId = params.get("ErrorId")
        self.ErrorDesc = params.get("ErrorDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderField(AbstractModel):
    """通用排序字段

    """

    def __init__(self):
        r"""
        :param Name: 排序字段名称
        :type Name: str
        :param Direction: 排序方向：ASC|DESC
        :type Direction: str
        """
        self.Name = None
        self.Direction = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationalFunction(AbstractModel):
    """包含层级信息的函数

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param DisplayName: 展示名称
        :type DisplayName: str
        :param LayerPath: 层级路径
        :type LayerPath: str
        :param ParentLayerPath: 上级层级路径
        :type ParentLayerPath: str
        :param Type: 函数类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Kind: 函数分类：窗口函数、聚合函数、日期函数......
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param Category: 函数种类：系统函数、自定义函数
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param Status: 函数状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Description: 函数说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Usage: 函数用法
注意：此字段可能返回 null，表示取不到有效值。
        :type Usage: str
        :param ParamDesc: 函数参数说明
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamDesc: str
        :param ReturnDesc: 函数返回值说明
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnDesc: str
        :param Example: 函数示例
注意：此字段可能返回 null，表示取不到有效值。
        :type Example: str
        :param ClusterIdentifier: 集群实例引擎 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIdentifier: str
        :param FuncId: 函数 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncId: str
        :param ClassName: 函数类名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassName: str
        :param ResourceList: 函数资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceList: list of FunctionVersion
        :param OperatorUserIds: 操作人 ID 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserIds: list of int
        :param OwnerUserIds: 公有云 Owner ID 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserIds: list of int
        :param DbName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param SubmitErrorMsg: 提交失败错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitErrorMsg: str
        """
        self.Name = None
        self.DisplayName = None
        self.LayerPath = None
        self.ParentLayerPath = None
        self.Type = None
        self.Kind = None
        self.Category = None
        self.Status = None
        self.Description = None
        self.Usage = None
        self.ParamDesc = None
        self.ReturnDesc = None
        self.Example = None
        self.ClusterIdentifier = None
        self.FuncId = None
        self.ClassName = None
        self.ResourceList = None
        self.OperatorUserIds = None
        self.OwnerUserIds = None
        self.DbName = None
        self.SubmitErrorMsg = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DisplayName = params.get("DisplayName")
        self.LayerPath = params.get("LayerPath")
        self.ParentLayerPath = params.get("ParentLayerPath")
        self.Type = params.get("Type")
        self.Kind = params.get("Kind")
        self.Category = params.get("Category")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Usage = params.get("Usage")
        self.ParamDesc = params.get("ParamDesc")
        self.ReturnDesc = params.get("ReturnDesc")
        self.Example = params.get("Example")
        self.ClusterIdentifier = params.get("ClusterIdentifier")
        self.FuncId = params.get("FuncId")
        self.ClassName = params.get("ClassName")
        if params.get("ResourceList") is not None:
            self.ResourceList = []
            for item in params.get("ResourceList"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self.ResourceList.append(obj)
        self.OperatorUserIds = params.get("OperatorUserIds")
        self.OwnerUserIds = params.get("OwnerUserIds")
        self.DbName = params.get("DbName")
        self.SubmitErrorMsg = params.get("SubmitErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """参数参数

    """

    def __init__(self):
        r"""
        :param ParamKey: 参数名
        :type ParamKey: str
        :param ParamValue: 参数值
        :type ParamValue: str
        """
        self.ParamKey = None
        self.ParamValue = None


    def _deserialize(self, params):
        self.ParamKey = params.get("ParamKey")
        self.ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProdSchedulerTask(AbstractModel):
    """数据质量生产调度任务业务实体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 生产调度任务工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param TaskId: 生产调度任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskName: 生产调度任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        """
        self.WorkflowId = None
        self.TaskId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityScore(AbstractModel):
    """质量评分

    """

    def __init__(self):
        r"""
        :param CompositeScore: 综合分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompositeScore: float
        :param ScoringDistribution: 评分分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ScoringDistribution: list of TableScoreStatisticsInfo
        :param TotalTableNumber: 总表数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTableNumber: int
        """
        self.CompositeScore = None
        self.ScoringDistribution = None
        self.TotalTableNumber = None


    def _deserialize(self, params):
        self.CompositeScore = params.get("CompositeScore")
        if params.get("ScoringDistribution") is not None:
            self.ScoringDistribution = []
            for item in params.get("ScoringDistribution"):
                obj = TableScoreStatisticsInfo()
                obj._deserialize(item)
                self.ScoringDistribution.append(obj)
        self.TotalTableNumber = params.get("TotalTableNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityScoreTrend(AbstractModel):
    """质量评分趋势

    """

    def __init__(self):
        r"""
        :param AverageScore: 周期平均分
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageScore: float
        :param DailyScoreList: 日评分列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyScoreList: list of DailyScoreInfo
        """
        self.AverageScore = None
        self.DailyScoreList = None


    def _deserialize(self, params):
        self.AverageScore = params.get("AverageScore")
        if params.get("DailyScoreList") is not None:
            self.DailyScoreList = []
            for item in params.get("DailyScoreList"):
                obj = DailyScoreInfo()
                obj._deserialize(item)
                self.DailyScoreList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealTimeTaskInstanceNodeInfo(AbstractModel):
    """实时任务实例当前的节点信息

    """

    def __init__(self):
        r"""
        :param TaskName: 任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param InstanceNodeInfoList: 实时任务实例节点信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNodeInfoList: list of InstanceNodeInfo
        """
        self.TaskName = None
        self.TaskId = None
        self.InstanceNodeInfoList = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskId = params.get("TaskId")
        if params.get("InstanceNodeInfoList") is not None:
            self.InstanceNodeInfoList = []
            for item in params.get("InstanceNodeInfoList"):
                obj = InstanceNodeInfo()
                obj._deserialize(item)
                self.InstanceNodeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordField(AbstractModel):
    """通用记录字段

    """

    def __init__(self):
        r"""
        :param Name: 字段名称
        :type Name: str
        :param Value: 字段值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordsSpeed(AbstractModel):
    """实时任务同步速度 条/s

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param Values: 速度值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of SpeedValue
        """
        self.NodeType = None
        self.NodeName = None
        self.Values = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeName = params.get("NodeName")
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = SpeedValue()
                obj._deserialize(item)
                self.Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterEventListenerRequest(AbstractModel):
    """RegisterEventListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param Key: 关键字，如果是任务，则传任务Id
        :type Key: str
        :param EventName: 事件名称
        :type EventName: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param Type: 事件类型，默认 REST_API
        :type Type: str
        :param Properties: 配置信息，比如最长等待时间1天配置json：{"maxWaitEventTime":1,"maxWaitEventTimeUnit":"DAYS"}
        :type Properties: str
        """
        self.Key = None
        self.EventName = None
        self.ProjectId = None
        self.Type = None
        self.Properties = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.EventName = params.get("EventName")
        self.ProjectId = params.get("ProjectId")
        self.Type = params.get("Type")
        self.Properties = params.get("Properties")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterEventListenerResponse(AbstractModel):
    """RegisterEventListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 成功或者失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchReturn`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchReturn()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RegisterEventRequest(AbstractModel):
    """RegisterEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Name: 事件名称，支持英文、数字和下划线，最长20个字符, 不能以数字下划线开头。
        :type Name: str
        :param EventSubType: 事件分割类型，周期类型: DAY，HOUR，MIN，SECOND
        :type EventSubType: str
        :param EventBroadcastType: 广播：BROADCAST,单播：SINGLE
        :type EventBroadcastType: str
        :param TimeUnit: 周期类型为天和小时为HOURS ，周期类型为分钟 ：MINUTES,周期类型为秒：SECONDS
        :type TimeUnit: str
        :param Owner: TBDS 事件所属人
        :type Owner: str
        :param EventType: 事件类型，默认值：TIME_SERIES
        :type EventType: str
        :param DimensionFormat: 对应day： yyyyMMdd，对应HOUR：yyyyMMddHH，对应MIN：yyyyMMddHHmm，对应SECOND：yyyyMMddHHmmss
        :type DimensionFormat: str
        :param TimeToLive: 存活时间
        :type TimeToLive: int
        :param Description: 事件描述
        :type Description: str
        """
        self.ProjectId = None
        self.Name = None
        self.EventSubType = None
        self.EventBroadcastType = None
        self.TimeUnit = None
        self.Owner = None
        self.EventType = None
        self.DimensionFormat = None
        self.TimeToLive = None
        self.Description = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.EventSubType = params.get("EventSubType")
        self.EventBroadcastType = params.get("EventBroadcastType")
        self.TimeUnit = params.get("TimeUnit")
        self.Owner = params.get("Owner")
        self.EventType = params.get("EventType")
        self.DimensionFormat = params.get("DimensionFormat")
        self.TimeToLive = params.get("TimeToLive")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterEventResponse(AbstractModel):
    """RegisterEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 成功或者失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchReturn`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchReturn()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RerunInstancesRequest(AbstractModel):
    """RerunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Instances: 实例嵌套集合
        :type Instances: list of InstanceInfo
        :param CheckFather: 检查父任务类型, true: 检查父任务; false: 不检查父任务
        :type CheckFather: bool
        :param RerunType: 重跑类型, 1: 自身; 3: 孩子; 2: 自身以及孩子
        :type RerunType: str
        :param DependentWay: 实例依赖方式, 1: 自依赖; 2: 任务依赖; 3: 自依赖及父子依赖
        :type DependentWay: str
        :param SkipEventListening: 重跑忽略事件监听与否
        :type SkipEventListening: bool
        :param SonInstanceType: 下游实例范围 1: 所在工作流 2: 所在项目 3: 所有跨工作流依赖的项目
        :type SonInstanceType: str
        """
        self.ProjectId = None
        self.Instances = None
        self.CheckFather = None
        self.RerunType = None
        self.DependentWay = None
        self.SkipEventListening = None
        self.SonInstanceType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.CheckFather = params.get("CheckFather")
        self.RerunType = params.get("RerunType")
        self.DependentWay = params.get("DependentWay")
        self.SkipEventListening = params.get("SkipEventListening")
        self.SonInstanceType = params.get("SonInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunInstancesResponse(AbstractModel):
    """RerunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回实例批量终止结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.OperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ResourcePathTree(AbstractModel):
    """资源管理目录树节点

    """

    def __init__(self):
        r"""
        :param Name: 资源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IsLeaf: 是否为叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLeaf: bool
        :param ResourceId: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param LocalPath: 本地路径
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalPath: str
        :param RemotePath: 远程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RemotePath: str
        :param FileExtensionType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtensionType: str
        :param Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Md5Value: 文件MD5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5Value: str
        :param OwnerName: 文件拥有者名字
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerName: str
        :param UpdateUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUser: str
        :param UpdateUserId: 文件更新人uin
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserId: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param CosBucket: Cos存储桶名
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucket: str
        :param CosRegion: Cos地域
注意：此字段可能返回 null，表示取不到有效值。
        :type CosRegion: str
        :param ExtraInfo: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: str
        """
        self.Name = None
        self.IsLeaf = None
        self.ResourceId = None
        self.LocalPath = None
        self.RemotePath = None
        self.FileExtensionType = None
        self.Size = None
        self.Md5Value = None
        self.OwnerName = None
        self.UpdateUser = None
        self.UpdateUserId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CosBucket = None
        self.CosRegion = None
        self.ExtraInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IsLeaf = params.get("IsLeaf")
        self.ResourceId = params.get("ResourceId")
        self.LocalPath = params.get("LocalPath")
        self.RemotePath = params.get("RemotePath")
        self.FileExtensionType = params.get("FileExtensionType")
        self.Size = params.get("Size")
        self.Md5Value = params.get("Md5Value")
        self.OwnerName = params.get("OwnerName")
        self.UpdateUser = params.get("UpdateUser")
        self.UpdateUserId = params.get("UpdateUserId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.ExtraInfo = params.get("ExtraInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInLongAgentRequest(AbstractModel):
    """RestartInLongAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 采集器ID
        :type AgentId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        """
        self.AgentId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInLongAgentResponse(AbstractModel):
    """RestartInLongAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeIntegrationTaskRequest(AbstractModel):
    """ResumeIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeIntegrationTaskResponse(AbstractModel):
    """ResumeIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class RobAndLockIntegrationTaskRequest(AbstractModel):
    """RobAndLockIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param TaskType: 任务类型：201. stream,   202. offline
        :type TaskType: int
        """
        self.TaskId = None
        self.ProjectId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RobAndLockIntegrationTaskResponse(AbstractModel):
    """RobAndLockIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RobLockState: 抢锁状态
        :type RobLockState: :class:`tencentcloud.wedata.v20210820.models.RobLockState`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RobLockState = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RobLockState") is not None:
            self.RobLockState = RobLockState()
            self.RobLockState._deserialize(params.get("RobLockState"))
        self.RequestId = params.get("RequestId")


class RobLockState(AbstractModel):
    """抢锁状态：是否可以抢锁和当前持锁人

    """

    def __init__(self):
        r"""
        :param IsRob: 是否可以抢锁
        :type IsRob: bool
        :param Locker: 当前持锁人
        :type Locker: str
        """
        self.IsRob = None
        self.Locker = None


    def _deserialize(self, params):
        self.IsRob = params.get("IsRob")
        self.Locker = params.get("Locker")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """数据质量规则

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RuleGroupId: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param TableId: 数据表Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param Name: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 规则类型 1.系统模版, 2.自定义模版, 3.自定义SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param RuleTemplateId: 规则模板Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateId: int
        :param RuleTemplateContent: 规则模板概述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateContent: str
        :param QualityDim: 规则所属质量维度 1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityDim: int
        :param SourceObjectType: 规则适用的源数据对象类型（1：常量，2：离线表级，3：离线字段级别）
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectType: int
        :param SourceObjectDataType: 规则适用的源数据对象类型（1：数值，2：字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectDataType: int
        :param SourceObjectDataTypeName: 源字段详细类型，INT、STRING
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectDataTypeName: str
        :param SourceObjectValue: 源字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectValue: str
        :param ConditionType: 检测范围 1.全表, 2.条件扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionType: int
        :param ConditionExpression: 条件扫描WHERE条件表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionExpression: str
        :param CustomSql: 自定义SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomSql: str
        :param CompareRule: 报警触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareRule: :class:`tencentcloud.wedata.v20210820.models.CompareRule`
        :param AlarmLevel: 报警触发级别 1.低, 2.中, 3.高
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: int
        :param Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Operator: 规则配置人
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param TargetDatabaseId: 目标库Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetDatabaseId: str
        :param TargetDatabaseName: 目标库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetDatabaseName: str
        :param TargetTableId: 目标表Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetTableId: str
        :param TargetTableName: 目标表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetTableName: str
        :param TargetConditionExpr: 目标字段过滤条件表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetConditionExpr: str
        :param RelConditionExpr: 源字段与目标字段关联条件on表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type RelConditionExpr: str
        :param FieldConfig: 自定义模版sql表达式参数
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldConfig: :class:`tencentcloud.wedata.v20210820.models.RuleFieldConfig`
        :param MultiSourceFlag: 是否关联多表
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiSourceFlag: bool
        :param WhereFlag: 是否where参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WhereFlag: bool
        """
        self.RuleId = None
        self.RuleGroupId = None
        self.TableId = None
        self.Name = None
        self.Type = None
        self.RuleTemplateId = None
        self.RuleTemplateContent = None
        self.QualityDim = None
        self.SourceObjectType = None
        self.SourceObjectDataType = None
        self.SourceObjectDataTypeName = None
        self.SourceObjectValue = None
        self.ConditionType = None
        self.ConditionExpression = None
        self.CustomSql = None
        self.CompareRule = None
        self.AlarmLevel = None
        self.Description = None
        self.Operator = None
        self.TargetDatabaseId = None
        self.TargetDatabaseName = None
        self.TargetTableId = None
        self.TargetTableName = None
        self.TargetConditionExpr = None
        self.RelConditionExpr = None
        self.FieldConfig = None
        self.MultiSourceFlag = None
        self.WhereFlag = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.TableId = params.get("TableId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.RuleTemplateContent = params.get("RuleTemplateContent")
        self.QualityDim = params.get("QualityDim")
        self.SourceObjectType = params.get("SourceObjectType")
        self.SourceObjectDataType = params.get("SourceObjectDataType")
        self.SourceObjectDataTypeName = params.get("SourceObjectDataTypeName")
        self.SourceObjectValue = params.get("SourceObjectValue")
        self.ConditionType = params.get("ConditionType")
        self.ConditionExpression = params.get("ConditionExpression")
        self.CustomSql = params.get("CustomSql")
        if params.get("CompareRule") is not None:
            self.CompareRule = CompareRule()
            self.CompareRule._deserialize(params.get("CompareRule"))
        self.AlarmLevel = params.get("AlarmLevel")
        self.Description = params.get("Description")
        self.Operator = params.get("Operator")
        self.TargetDatabaseId = params.get("TargetDatabaseId")
        self.TargetDatabaseName = params.get("TargetDatabaseName")
        self.TargetTableId = params.get("TargetTableId")
        self.TargetTableName = params.get("TargetTableName")
        self.TargetConditionExpr = params.get("TargetConditionExpr")
        self.RelConditionExpr = params.get("RelConditionExpr")
        if params.get("FieldConfig") is not None:
            self.FieldConfig = RuleFieldConfig()
            self.FieldConfig._deserialize(params.get("FieldConfig"))
        self.MultiSourceFlag = params.get("MultiSourceFlag")
        self.WhereFlag = params.get("WhereFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleConfig(AbstractModel):
    """规则配置

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param ConditionType: 规则检测范围类型 1.全表  2.条件扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionType: int
        :param Condition: 检测范围表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: str
        :param TargetCondition: 目标检测范围表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetCondition: str
        """
        self.RuleId = None
        self.ConditionType = None
        self.Condition = None
        self.TargetCondition = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ConditionType = params.get("ConditionType")
        self.Condition = params.get("Condition")
        self.TargetCondition = params.get("TargetCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDimCnt(AbstractModel):
    """RuleDimCnt 规则维度统计

    """

    def __init__(self):
        r"""
        :param Dim: 1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
        :type Dim: int
        :param Cnt: count 数
        :type Cnt: int
        """
        self.Dim = None
        self.Cnt = None


    def _deserialize(self, params):
        self.Dim = params.get("Dim")
        self.Cnt = params.get("Cnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDimStat(AbstractModel):
    """规则维度数统计

    """

    def __init__(self):
        r"""
        :param TotalCnt: 总数
        :type TotalCnt: int
        :param DimCntList: 维度统计数
        :type DimCntList: list of RuleDimCnt
        """
        self.TotalCnt = None
        self.DimCntList = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("DimCntList") is not None:
            self.DimCntList = []
            for item in params.get("DimCntList"):
                obj = RuleDimCnt()
                obj._deserialize(item)
                self.DimCntList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecConfig(AbstractModel):
    """规则执行配置

    """

    def __init__(self):
        r"""
        :param QueueName: 计算队列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        :param ExecutorGroupId: 执行资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        """
        self.QueueName = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecDateStat(AbstractModel):
    """概览趋势结果

    """

    def __init__(self):
        r"""
        :param StatDate: 统计日期
        :type StatDate: str
        :param AlarmCnt: 告警数
        :type AlarmCnt: int
        :param PipelineCnt: 阻塞数
        :type PipelineCnt: int
        """
        self.StatDate = None
        self.AlarmCnt = None
        self.PipelineCnt = None


    def _deserialize(self, params):
        self.StatDate = params.get("StatDate")
        self.AlarmCnt = params.get("AlarmCnt")
        self.PipelineCnt = params.get("PipelineCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecExportResult(AbstractModel):
    """规则执行结果导出结果

    """

    def __init__(self):
        r"""
        :param RuleExecId: 规则执行id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleExecId: int
        :param ExportTasks: 导出任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportTasks: list of ExportTaskInfo
        """
        self.RuleExecId = None
        self.ExportTasks = None


    def _deserialize(self, params):
        self.RuleExecId = params.get("RuleExecId")
        if params.get("ExportTasks") is not None:
            self.ExportTasks = []
            for item in params.get("ExportTasks"):
                obj = ExportTaskInfo()
                obj._deserialize(item)
                self.ExportTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecLog(AbstractModel):
    """规则执行日志

    """

    def __init__(self):
        r"""
        :param Finished: 是否完成
注意：此字段可能返回 null，表示取不到有效值。
        :type Finished: bool
        :param Log: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        """
        self.Finished = None
        self.Log = None


    def _deserialize(self, params):
        self.Finished = params.get("Finished")
        self.Log = params.get("Log")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecResult(AbstractModel):
    """规则执行结果

    """

    def __init__(self):
        r"""
        :param RuleExecId: 规则执行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleExecId: int
        :param RuleGroupExecId: 规则组执行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupExecId: int
        :param RuleGroupId: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param RuleType: 规则类型 1.系统模版, 2.自定义模版, 3.自定义SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: int
        :param SourceObjectDataTypeName: 源字段详细类型，int string
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectDataTypeName: str
        :param SourceObjectValue: 源字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectValue: str
        :param ConditionExpression: 条件扫描WHERE条件表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionExpression: str
        :param ExecResultStatus: 检测结果（1:检测通过，2：触发规则，3：检测失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecResultStatus: int
        :param TriggerResult: 触发结果，告警发送成功, 阻断任务成功
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerResult: str
        :param CompareResult: 对比结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareResult: :class:`tencentcloud.wedata.v20210820.models.CompareResult`
        :param TemplateName: 模版名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param QualityDim: 质量维度
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityDim: int
        :param TargetDBTableName: 目标表-库表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetDBTableName: str
        :param TargetObjectValue: 目标表-字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetObjectValue: str
        :param TargetObjectDataType: 目标表-字段类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetObjectDataType: str
        :param FieldConfig: 自定义模版sql表达式参数
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldConfig: :class:`tencentcloud.wedata.v20210820.models.RuleFieldConfig`
        :param RelConditionExpr: 源字段与目标字段关联条件on表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type RelConditionExpr: str
        """
        self.RuleExecId = None
        self.RuleGroupExecId = None
        self.RuleGroupId = None
        self.RuleId = None
        self.RuleName = None
        self.RuleType = None
        self.SourceObjectDataTypeName = None
        self.SourceObjectValue = None
        self.ConditionExpression = None
        self.ExecResultStatus = None
        self.TriggerResult = None
        self.CompareResult = None
        self.TemplateName = None
        self.QualityDim = None
        self.TargetDBTableName = None
        self.TargetObjectValue = None
        self.TargetObjectDataType = None
        self.FieldConfig = None
        self.RelConditionExpr = None


    def _deserialize(self, params):
        self.RuleExecId = params.get("RuleExecId")
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleType = params.get("RuleType")
        self.SourceObjectDataTypeName = params.get("SourceObjectDataTypeName")
        self.SourceObjectValue = params.get("SourceObjectValue")
        self.ConditionExpression = params.get("ConditionExpression")
        self.ExecResultStatus = params.get("ExecResultStatus")
        self.TriggerResult = params.get("TriggerResult")
        if params.get("CompareResult") is not None:
            self.CompareResult = CompareResult()
            self.CompareResult._deserialize(params.get("CompareResult"))
        self.TemplateName = params.get("TemplateName")
        self.QualityDim = params.get("QualityDim")
        self.TargetDBTableName = params.get("TargetDBTableName")
        self.TargetObjectValue = params.get("TargetObjectValue")
        self.TargetObjectDataType = params.get("TargetObjectDataType")
        if params.get("FieldConfig") is not None:
            self.FieldConfig = RuleFieldConfig()
            self.FieldConfig._deserialize(params.get("FieldConfig"))
        self.RelConditionExpr = params.get("RelConditionExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecResultDetail(AbstractModel):
    """规则执行结果详情

    """

    def __init__(self):
        r"""
        :param DatasourceId: 数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: int
        :param DatasourceName: 数据源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceName: str
        :param DatabaseId: 数据库guid
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param TableId: 表guid
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param RuleExecResult: 规则执行记录
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleExecResult: :class:`tencentcloud.wedata.v20210820.models.RuleExecResult`
        :param TableOwnerUserId: 表负责人userId
注意：此字段可能返回 null，表示取不到有效值。
        :type TableOwnerUserId: int
        """
        self.DatasourceId = None
        self.DatasourceName = None
        self.DatabaseId = None
        self.DatabaseName = None
        self.InstanceId = None
        self.TableId = None
        self.TableName = None
        self.RuleExecResult = None
        self.TableOwnerUserId = None


    def _deserialize(self, params):
        self.DatasourceId = params.get("DatasourceId")
        self.DatasourceName = params.get("DatasourceName")
        self.DatabaseId = params.get("DatabaseId")
        self.DatabaseName = params.get("DatabaseName")
        self.InstanceId = params.get("InstanceId")
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        if params.get("RuleExecResult") is not None:
            self.RuleExecResult = RuleExecResult()
            self.RuleExecResult._deserialize(params.get("RuleExecResult"))
        self.TableOwnerUserId = params.get("TableOwnerUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecResultPage(AbstractModel):
    """规则执行结果分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 规则执行结果
        :type Items: list of RuleExecResult
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleExecResult()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExecStat(AbstractModel):
    """规则运行情况结果

    """

    def __init__(self):
        r"""
        :param TotalCnt: 规则运行总数
        :type TotalCnt: int
        :param LastTotalCnt: 环比规则运行总数
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTotalCnt: int
        :param TotalCntRatio: 规则运行总数占比
        :type TotalCntRatio: float
        :param LastTotalCntRatio: 规则运行总数环比变化
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTotalCntRatio: float
        :param TriggerCnt: 规则触发数
        :type TriggerCnt: int
        :param LastTriggerCnt: 环比规则触发数
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerCnt: int
        :param TriggerCntRatio: 触发占总数占比
        :type TriggerCntRatio: float
        :param LastTriggerCntRatio: 环比规则触发数变化
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerCntRatio: float
        :param AlarmCnt: 规则报警数
        :type AlarmCnt: int
        :param LastAlarmCnt: 环比规则报警数
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAlarmCnt: int
        :param AlarmCntRatio: 报警占总数占比
        :type AlarmCntRatio: float
        :param LastAlarmCntRatio: 环比报警数变化
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAlarmCntRatio: float
        :param PipelineCnt: 阻塞发生数
        :type PipelineCnt: int
        :param LastPipelineCnt: 环比阻塞发生数
注意：此字段可能返回 null，表示取不到有效值。
        :type LastPipelineCnt: int
        :param PipelineCntRatio: 阻塞占总数占比
        :type PipelineCntRatio: float
        :param LastPipelineCntRatio: 环比阻塞发生数变化
注意：此字段可能返回 null，表示取不到有效值。
        :type LastPipelineCntRatio: float
        """
        self.TotalCnt = None
        self.LastTotalCnt = None
        self.TotalCntRatio = None
        self.LastTotalCntRatio = None
        self.TriggerCnt = None
        self.LastTriggerCnt = None
        self.TriggerCntRatio = None
        self.LastTriggerCntRatio = None
        self.AlarmCnt = None
        self.LastAlarmCnt = None
        self.AlarmCntRatio = None
        self.LastAlarmCntRatio = None
        self.PipelineCnt = None
        self.LastPipelineCnt = None
        self.PipelineCntRatio = None
        self.LastPipelineCntRatio = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        self.LastTotalCnt = params.get("LastTotalCnt")
        self.TotalCntRatio = params.get("TotalCntRatio")
        self.LastTotalCntRatio = params.get("LastTotalCntRatio")
        self.TriggerCnt = params.get("TriggerCnt")
        self.LastTriggerCnt = params.get("LastTriggerCnt")
        self.TriggerCntRatio = params.get("TriggerCntRatio")
        self.LastTriggerCntRatio = params.get("LastTriggerCntRatio")
        self.AlarmCnt = params.get("AlarmCnt")
        self.LastAlarmCnt = params.get("LastAlarmCnt")
        self.AlarmCntRatio = params.get("AlarmCntRatio")
        self.LastAlarmCntRatio = params.get("LastAlarmCntRatio")
        self.PipelineCnt = params.get("PipelineCnt")
        self.LastPipelineCnt = params.get("LastPipelineCnt")
        self.PipelineCntRatio = params.get("PipelineCntRatio")
        self.LastPipelineCntRatio = params.get("LastPipelineCntRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFieldConfig(AbstractModel):
    """规则变量替换

    """

    def __init__(self):
        r"""
        :param WhereConfig: where变量
注意：此字段可能返回 null，表示取不到有效值。
        :type WhereConfig: list of FieldConfig
        :param TableConfig: 库表变量
注意：此字段可能返回 null，表示取不到有效值。
        :type TableConfig: list of TableConfig
        """
        self.WhereConfig = None
        self.TableConfig = None


    def _deserialize(self, params):
        if params.get("WhereConfig") is not None:
            self.WhereConfig = []
            for item in params.get("WhereConfig"):
                obj = FieldConfig()
                obj._deserialize(item)
                self.WhereConfig.append(obj)
        if params.get("TableConfig") is not None:
            self.TableConfig = []
            for item in params.get("TableConfig"):
                obj = TableConfig()
                obj._deserialize(item)
                self.TableConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroup(AbstractModel):
    """数据质量规则组

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param DatasourceId: 数据源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param DatasourceName: 数据源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceName: str
        :param DatasourceType: 数据源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceType: int
        :param MonitorType: 监控类型 1.未配置, 2.关联生产调度, 3.离线周期检测
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TableName: 关联数据表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableId: 关联数据表Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableOwnerName: 关联数据表负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type TableOwnerName: str
        :param ExecStrategy: 执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecStrategy: :class:`tencentcloud.wedata.v20210820.models.RuleGroupExecStrategy`
        :param Subscription: 执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Subscription: :class:`tencentcloud.wedata.v20210820.models.RuleGroupSubscribe`
        :param DatabaseId: 数据库id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param Permission: 是否有权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: bool
        :param RuleCount: 已经配置的规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCount: int
        :param MonitorStatus: 监控状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorStatus: bool
        :param TableOwnerUserId: 表负责人UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type TableOwnerUserId: int
        """
        self.RuleGroupId = None
        self.DatasourceId = None
        self.DatasourceName = None
        self.DatasourceType = None
        self.MonitorType = None
        self.UpdateTime = None
        self.TableName = None
        self.TableId = None
        self.TableOwnerName = None
        self.ExecStrategy = None
        self.Subscription = None
        self.DatabaseId = None
        self.DatabaseName = None
        self.Permission = None
        self.RuleCount = None
        self.MonitorStatus = None
        self.TableOwnerUserId = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.DatasourceId = params.get("DatasourceId")
        self.DatasourceName = params.get("DatasourceName")
        self.DatasourceType = params.get("DatasourceType")
        self.MonitorType = params.get("MonitorType")
        self.UpdateTime = params.get("UpdateTime")
        self.TableName = params.get("TableName")
        self.TableId = params.get("TableId")
        self.TableOwnerName = params.get("TableOwnerName")
        if params.get("ExecStrategy") is not None:
            self.ExecStrategy = RuleGroupExecStrategy()
            self.ExecStrategy._deserialize(params.get("ExecStrategy"))
        if params.get("Subscription") is not None:
            self.Subscription = RuleGroupSubscribe()
            self.Subscription._deserialize(params.get("Subscription"))
        self.DatabaseId = params.get("DatabaseId")
        self.DatabaseName = params.get("DatabaseName")
        self.Permission = params.get("Permission")
        self.RuleCount = params.get("RuleCount")
        self.MonitorStatus = params.get("MonitorStatus")
        self.TableOwnerUserId = params.get("TableOwnerUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupExecResult(AbstractModel):
    """规则组执行结果

    """

    def __init__(self):
        r"""
        :param RuleGroupExecId: 规则组执行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupExecId: int
        :param RuleGroupId: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param TriggerType: 执行触发类型（1：手动触发， 2：调度事中触发，3：周期调度触发）
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: int
        :param ExecTime: 执行时间 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecTime: str
        :param Status: 执行状态（1.已提交 2.检测中 3.正常 4.异常）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param AlarmRuleCount: 异常规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmRuleCount: int
        :param TotalRuleCount: 总规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRuleCount: int
        :param TableOwnerName: 源表负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type TableOwnerName: str
        :param TableName: 源表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableId: 表id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param DatabaseId: 数据库id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatasourceId: 数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param Permission: 有无权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: bool
        :param ExecDetail: 执行详情，调度计划或者关联生产任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecDetail: str
        """
        self.RuleGroupExecId = None
        self.RuleGroupId = None
        self.TriggerType = None
        self.ExecTime = None
        self.Status = None
        self.AlarmRuleCount = None
        self.TotalRuleCount = None
        self.TableOwnerName = None
        self.TableName = None
        self.TableId = None
        self.DatabaseId = None
        self.DatasourceId = None
        self.Permission = None
        self.ExecDetail = None


    def _deserialize(self, params):
        self.RuleGroupExecId = params.get("RuleGroupExecId")
        self.RuleGroupId = params.get("RuleGroupId")
        self.TriggerType = params.get("TriggerType")
        self.ExecTime = params.get("ExecTime")
        self.Status = params.get("Status")
        self.AlarmRuleCount = params.get("AlarmRuleCount")
        self.TotalRuleCount = params.get("TotalRuleCount")
        self.TableOwnerName = params.get("TableOwnerName")
        self.TableName = params.get("TableName")
        self.TableId = params.get("TableId")
        self.DatabaseId = params.get("DatabaseId")
        self.DatasourceId = params.get("DatasourceId")
        self.Permission = params.get("Permission")
        self.ExecDetail = params.get("ExecDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupExecResultPage(AbstractModel):
    """规则组执行结果分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 规则组执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RuleGroupExecResult
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleGroupExecResult()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupExecStrategy(AbstractModel):
    """质量规则执行策略

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param MonitorType: 监控类型 1.未配置, 2.关联生产调度, 3.离线周期检测
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: int
        :param ExecQueue: 计算队列
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecQueue: str
        :param ExecutorGroupId: 执行资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        :param ExecutorGroupName: 执行资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupName: str
        :param Tasks: 关联的生产调度任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ProdSchedulerTask
        :param StartTime: 周期开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 周期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CycleType: 调度周期类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param DelayTime: 延迟调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: int
        :param CycleStep: 间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStep: int
        :param TaskAction: 时间指定
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        """
        self.RuleGroupId = None
        self.MonitorType = None
        self.ExecQueue = None
        self.ExecutorGroupId = None
        self.ExecutorGroupName = None
        self.Tasks = None
        self.StartTime = None
        self.EndTime = None
        self.CycleType = None
        self.DelayTime = None
        self.CycleStep = None
        self.TaskAction = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.MonitorType = params.get("MonitorType")
        self.ExecQueue = params.get("ExecQueue")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.ExecutorGroupName = params.get("ExecutorGroupName")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ProdSchedulerTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CycleType = params.get("CycleType")
        self.DelayTime = params.get("DelayTime")
        self.CycleStep = params.get("CycleStep")
        self.TaskAction = params.get("TaskAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupMonitor(AbstractModel):
    """规则组监控业务视图

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param TableId: 表guid
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param DatasourceId: 数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: int
        :param DatabaseId: 数据库guid
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param MonitorType: 监控类型 1.未配置, 2.关联生产调度, 3.离线周期检测
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: int
        :param MonitorStatus: 监控状态 0.false 1.true
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorStatus: int
        :param CreateUserId: 规则组创建人id
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param CreateUserName: 规则组创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserName: str
        :param CreateTime: 规则创建时间 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.RuleGroupId = None
        self.TableId = None
        self.DatasourceId = None
        self.DatabaseId = None
        self.MonitorType = None
        self.MonitorStatus = None
        self.CreateUserId = None
        self.CreateUserName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        self.TableId = params.get("TableId")
        self.DatasourceId = params.get("DatasourceId")
        self.DatabaseId = params.get("DatabaseId")
        self.MonitorType = params.get("MonitorType")
        self.MonitorStatus = params.get("MonitorStatus")
        self.CreateUserId = params.get("CreateUserId")
        self.CreateUserName = params.get("CreateUserName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupMonitorPage(AbstractModel):
    """规则组监控业务分页视图

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RuleGroupMonitor
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleGroupMonitor()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupPage(AbstractModel):
    """规则组分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 规则组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RuleGroup
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleGroup()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupSchedulerInfo(AbstractModel):
    """规则组调度信息

    """

    def __init__(self):
        r"""
        :param Id: 规则组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param MonitorType: 1:未配置 2:关联生产调度 3:离线周期检测
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: int
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CycleType: 循环类型简写
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param CycleStep: 循环步长
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStep: int
        :param CycleDesc: 循环类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleDesc: str
        :param TaskAction: 离线周期检测下指定时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        :param DelayTime: 离线周期检测下延迟时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: int
        :param CycleTaskId: 离线周期检测下注册到任务调度的任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleTaskId: str
        :param AssociateTaskIds: 关联生产调度下关联的任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateTaskIds: list of str
        """
        self.Id = None
        self.MonitorType = None
        self.StartTime = None
        self.EndTime = None
        self.CycleType = None
        self.CycleStep = None
        self.CycleDesc = None
        self.TaskAction = None
        self.DelayTime = None
        self.CycleTaskId = None
        self.AssociateTaskIds = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MonitorType = params.get("MonitorType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.CycleDesc = params.get("CycleDesc")
        self.TaskAction = params.get("TaskAction")
        self.DelayTime = params.get("DelayTime")
        self.CycleTaskId = params.get("CycleTaskId")
        self.AssociateTaskIds = params.get("AssociateTaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupSubscribe(AbstractModel):
    """数据质量规则组订阅信息

    """

    def __init__(self):
        r"""
        :param RuleGroupId: 规则组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroupId: int
        :param Receivers: 订阅接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Receivers: list of SubscribeReceiver
        :param SubscribeType: 订阅方式 1.邮件email  2.短信sms
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeType: list of int non-negative
        :param WebHooks: 群机器人配置的webhook信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WebHooks: list of SubscribeWebHook
        """
        self.RuleGroupId = None
        self.Receivers = None
        self.SubscribeType = None
        self.WebHooks = None


    def _deserialize(self, params):
        self.RuleGroupId = params.get("RuleGroupId")
        if params.get("Receivers") is not None:
            self.Receivers = []
            for item in params.get("Receivers"):
                obj = SubscribeReceiver()
                obj._deserialize(item)
                self.Receivers.append(obj)
        self.SubscribeType = params.get("SubscribeType")
        if params.get("WebHooks") is not None:
            self.WebHooks = []
            for item in params.get("WebHooks"):
                obj = SubscribeWebHook()
                obj._deserialize(item)
                self.WebHooks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupTable(AbstractModel):
    """表绑定规则组信息

    """

    def __init__(self):
        r"""
        :param TableInfo: 表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TableInfo: :class:`tencentcloud.wedata.v20210820.models.RuleGroupTableInnerInfo`
        :param RuleGroups: 规则组调度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleGroups: list of RuleGroupSchedulerInfo
        :param Subscriptions: 订阅者信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Subscriptions: list of RuleGroupSubscribe
        """
        self.TableInfo = None
        self.RuleGroups = None
        self.Subscriptions = None


    def _deserialize(self, params):
        if params.get("TableInfo") is not None:
            self.TableInfo = RuleGroupTableInnerInfo()
            self.TableInfo._deserialize(params.get("TableInfo"))
        if params.get("RuleGroups") is not None:
            self.RuleGroups = []
            for item in params.get("RuleGroups"):
                obj = RuleGroupSchedulerInfo()
                obj._deserialize(item)
                self.RuleGroups.append(obj)
        if params.get("Subscriptions") is not None:
            self.Subscriptions = []
            for item in params.get("Subscriptions"):
                obj = RuleGroupSubscribe()
                obj._deserialize(item)
                self.Subscriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleGroupTableInnerInfo(AbstractModel):
    """规则组关联表信息

    """

    def __init__(self):
        r"""
        :param TableId: 表ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param DatasourceId: 数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param DatasourceName: 数据源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceName: str
        :param DatasourceType: 数据源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceType: int
        :param DatabaseId: 数据库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param UserId: 责任人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: int
        """
        self.TableId = None
        self.TableName = None
        self.InstanceId = None
        self.DatasourceId = None
        self.DatasourceName = None
        self.DatasourceType = None
        self.DatabaseId = None
        self.DatabaseName = None
        self.ProjectId = None
        self.UserId = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        self.InstanceId = params.get("InstanceId")
        self.DatasourceId = params.get("DatasourceId")
        self.DatasourceName = params.get("DatasourceName")
        self.DatasourceType = params.get("DatasourceType")
        self.DatabaseId = params.get("DatabaseId")
        self.DatabaseName = params.get("DatabaseName")
        self.ProjectId = params.get("ProjectId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHistory(AbstractModel):
    """规则操作记录业务

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param AlterTime: 变更时间 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type AlterTime: str
        :param AlterContent: 变更内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AlterContent: str
        :param OperatorUserId: 操作账号UId
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserId: int
        :param OperatorName: 操作人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorName: str
        """
        self.RuleId = None
        self.AlterTime = None
        self.AlterContent = None
        self.OperatorUserId = None
        self.OperatorName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AlterTime = params.get("AlterTime")
        self.AlterContent = params.get("AlterContent")
        self.OperatorUserId = params.get("OperatorUserId")
        self.OperatorName = params.get("OperatorName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHistoryPage(AbstractModel):
    """数据质量规则操作历史分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 规则操作历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RuleHistory
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleHistory()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulePage(AbstractModel):
    """数据质量规则分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Rule
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Rule()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTemplate(AbstractModel):
    """规则模版

    """

    def __init__(self):
        r"""
        :param RuleTemplateId: 规则模版ID
        :type RuleTemplateId: int
        :param Name: 规则模版名称
        :type Name: str
        :param Description: 规则模版描述
        :type Description: str
        :param Type: 模版类型（1：系统模版，2：自定义）
        :type Type: int
        :param SourceObjectType: 规则适用的源数据对象类型（1：常量，2：离线表级，3：离线字段级别）
        :type SourceObjectType: int
        :param SourceObjectDataType: 规则适用的源数据对象类型（1：数值，2：字符串）
        :type SourceObjectDataType: int
        :param SourceContent: 规则模版源侧内容，区分引擎，JSON 结构
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceContent: str
        :param SourceEngineTypes: 源数据适用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceEngineTypes: list of int non-negative
        :param QualityDim: 规则所属质量维度（1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性）
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityDim: int
        :param CompareType: 规则支持的比较方式类型（1：固定值比较，大于、小于，大于等于等 2：波动值比较，绝对值、上升、下降）
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareType: int
        :param CitationCount: 引用次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CitationCount: int
        :param UserId: 创建人id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: int
        :param UserName: 创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param UpdateTime: 更新时间yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param WhereFlag: 是否添加where参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WhereFlag: bool
        :param MultiSourceFlag: 是否关联多个库表
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiSourceFlag: bool
        :param SqlExpression: 自定义模板SQL表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlExpression: str
        :param SubQualityDim: 模版子维度，0.父维度类型,1.一致性: 枚举范围一致性,2.一致性：数值范围一致性,3.一致性：字段数据相关性
注意：此字段可能返回 null，表示取不到有效值。
        :type SubQualityDim: int
        """
        self.RuleTemplateId = None
        self.Name = None
        self.Description = None
        self.Type = None
        self.SourceObjectType = None
        self.SourceObjectDataType = None
        self.SourceContent = None
        self.SourceEngineTypes = None
        self.QualityDim = None
        self.CompareType = None
        self.CitationCount = None
        self.UserId = None
        self.UserName = None
        self.UpdateTime = None
        self.WhereFlag = None
        self.MultiSourceFlag = None
        self.SqlExpression = None
        self.SubQualityDim = None


    def _deserialize(self, params):
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.SourceObjectType = params.get("SourceObjectType")
        self.SourceObjectDataType = params.get("SourceObjectDataType")
        self.SourceContent = params.get("SourceContent")
        self.SourceEngineTypes = params.get("SourceEngineTypes")
        self.QualityDim = params.get("QualityDim")
        self.CompareType = params.get("CompareType")
        self.CitationCount = params.get("CitationCount")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.UpdateTime = params.get("UpdateTime")
        self.WhereFlag = params.get("WhereFlag")
        self.MultiSourceFlag = params.get("MultiSourceFlag")
        self.SqlExpression = params.get("SqlExpression")
        self.SubQualityDim = params.get("SubQualityDim")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTemplateHistory(AbstractModel):
    """规则模版变更历史记录视图

    """

    def __init__(self):
        r"""
        :param TemplateId: 模版ID
        :type TemplateId: int
        :param Version: 版本
        :type Version: int
        :param UserId: 用户Id
        :type UserId: int
        :param UserName: 用户昵称
        :type UserName: str
        :param AlterType: 变更类型1.新增2.修改3.删除
        :type AlterType: int
        :param AlterContent: 变更内容
        :type AlterContent: str
        """
        self.TemplateId = None
        self.Version = None
        self.UserId = None
        self.UserName = None
        self.AlterType = None
        self.AlterContent = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Version = params.get("Version")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.AlterType = params.get("AlterType")
        self.AlterContent = params.get("AlterContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTemplateHistoryPage(AbstractModel):
    """规则模版分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RuleTemplateHistory
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleTemplateHistory()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTemplatePage(AbstractModel):
    """RuleTemplatePage 结果

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
        :type TotalCount: int
        :param Items: 模版列表
        :type Items: list of RuleTemplate
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RuleTemplate()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTaskRequest(AbstractModel):
    """RunTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.ProjectId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTaskResponse(AbstractModel):
    """RunTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 运行成功或者失败
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class RunnerRuleExecResult(AbstractModel):
    """规则执行结果

    """

    def __init__(self):
        r"""
        :param RuleId: rule id
        :type RuleId: int
        :param RuleExecId: rule exec id
        :type RuleExecId: int
        :param State: exec state
        :type State: str
        :param Data: 结果
        :type Data: list of str
        """
        self.RuleId = None
        self.RuleExecId = None
        self.State = None
        self.Data = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleExecId = params.get("RuleExecId")
        self.State = params.get("State")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveCustomFunctionRequest(AbstractModel):
    """SaveCustomFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数唯一标识
        :type FunctionId: str
        :param Kind: 分类：窗口函数、聚合函数、日期函数......
        :type Kind: str
        :param ClusterIdentifier: 集群引擎实例
        :type ClusterIdentifier: str
        :param ClassName: 类名
        :type ClassName: str
        :param ResourceList: 资源列表
        :type ResourceList: list of FunctionResource
        :param Description: 函数说明
        :type Description: str
        :param Usage: 用法
        :type Usage: str
        :param ParamDesc: 参数说明
        :type ParamDesc: str
        :param ReturnDesc: 返回值说明
        :type ReturnDesc: str
        :param Example: 示例
        :type Example: str
        """
        self.FunctionId = None
        self.Kind = None
        self.ClusterIdentifier = None
        self.ClassName = None
        self.ResourceList = None
        self.Description = None
        self.Usage = None
        self.ParamDesc = None
        self.ReturnDesc = None
        self.Example = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.Kind = params.get("Kind")
        self.ClusterIdentifier = params.get("ClusterIdentifier")
        self.ClassName = params.get("ClassName")
        if params.get("ResourceList") is not None:
            self.ResourceList = []
            for item in params.get("ResourceList"):
                obj = FunctionResource()
                obj._deserialize(item)
                self.ResourceList.append(obj)
        self.Description = params.get("Description")
        self.Usage = params.get("Usage")
        self.ParamDesc = params.get("ParamDesc")
        self.ReturnDesc = params.get("ReturnDesc")
        self.Example = params.get("Example")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveCustomFunctionResponse(AbstractModel):
    """SaveCustomFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionId: str
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionId = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class SchedulerTaskInstanceInfo(AbstractModel):
    """集成离线任务实例信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param CurRunDate: 实例运行时间
        :type CurRunDate: str
        """
        self.TaskId = None
        self.CurRunDate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaDetail(AbstractModel):
    """元数据字段信息

    """

    def __init__(self):
        r"""
        :param ColumnKey: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnKey: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.ColumnKey = None
        self.Description = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.ColumnKey = params.get("ColumnKey")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCondition(AbstractModel):
    """查询实例条件

    """

    def __init__(self):
        r"""
        :param Instance: 查询框架，必选
        :type Instance: :class:`tencentcloud.wedata.v20210820.models.SearchConditionInstance`
        :param Keyword: 查询关键字（任务Id精确匹配，任务名称模糊匹配），可选
        :type Keyword: str
        :param Sort: 排序顺序（asc，desc）
        :type Sort: str
        :param SortCol: 排序列（costTime 运行耗时，startTime 开始时间，state 实例状态，curRunDate 数据时间）
        :type SortCol: str
        """
        self.Instance = None
        self.Keyword = None
        self.Sort = None
        self.SortCol = None


    def _deserialize(self, params):
        if params.get("Instance") is not None:
            self.Instance = SearchConditionInstance()
            self.Instance._deserialize(params.get("Instance"))
        self.Keyword = params.get("Keyword")
        self.Sort = params.get("Sort")
        self.SortCol = params.get("SortCol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchConditionInstance(AbstractModel):
    """查询框架

    """

    def __init__(self):
        r"""
        :param ExecutionSpace: 执行空间 "DRY_RUN"
        :type ExecutionSpace: int
        :param ProductName: 产品名称，可选
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: int
        :param ResourceGroup: 资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroup: int
        """
        self.ExecutionSpace = None
        self.ProductName = None
        self.ResourceGroup = None


    def _deserialize(self, params):
        self.ExecutionSpace = params.get("ExecutionSpace")
        self.ProductName = params.get("ProductName")
        self.ResourceGroup = params.get("ResourceGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchConditionInstanceNew(AbstractModel):
    """搜索条件

    """

    def __init__(self):
        r"""
        :param ExecutionSpace: 执行空间 "DRY_RUN"
        :type ExecutionSpace: str
        :param ProductName: 产品名称，可选
        :type ProductName: str
        :param ResourceGroup: 资源组
        :type ResourceGroup: str
        """
        self.ExecutionSpace = None
        self.ProductName = None
        self.ResourceGroup = None


    def _deserialize(self, params):
        self.ExecutionSpace = params.get("ExecutionSpace")
        self.ProductName = params.get("ProductName")
        self.ResourceGroup = params.get("ResourceGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchConditionNew(AbstractModel):
    """查询实例条件(新)

    """

    def __init__(self):
        r"""
        :param Instance: 查询框架，必选
        :type Instance: :class:`tencentcloud.wedata.v20210820.models.SearchConditionInstanceNew`
        :param Keyword: 查询关键字（任务Id精确匹配，任务名称模糊匹配），可选
        :type Keyword: str
        :param Sort: 排序顺序（asc，desc）
        :type Sort: str
        :param SortCol: 排序列（costTime 运行耗时，startTime 开始时间，state 实例状态，curRunDate 数据时间）
        :type SortCol: str
        """
        self.Instance = None
        self.Keyword = None
        self.Sort = None
        self.SortCol = None


    def _deserialize(self, params):
        if params.get("Instance") is not None:
            self.Instance = SearchConditionInstanceNew()
            self.Instance._deserialize(params.get("Instance"))
        self.Keyword = params.get("Keyword")
        self.Sort = params.get("Sort")
        self.SortCol = params.get("SortCol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTaskAlarmNewRequest(AbstractModel):
    """SetTaskAlarmNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmInfoList: 设置任务超时告警和失败告警信息
        :type AlarmInfoList: list of AlarmInfo
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.AlarmInfoList = None
        self.ProjectId = None


    def _deserialize(self, params):
        if params.get("AlarmInfoList") is not None:
            self.AlarmInfoList = []
            for item in params.get("AlarmInfoList"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.AlarmInfoList.append(obj)
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTaskAlarmNewResponse(AbstractModel):
    """SetTaskAlarmNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回批量操作成功个数、失败个数、操作总数
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchOperateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchOperateResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SimpleTaskInfo(AbstractModel):
    """简单Task信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskName: 任务名
        :type TaskName: str
        """
        self.TaskId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceFieldInfo(AbstractModel):
    """上游节点字段信息

    """

    def __init__(self):
        r"""
        :param FieldName: 字段名称
        :type FieldName: str
        :param FieldType: 字段类型
        :type FieldType: str
        :param Alias: 字段别名
        :type Alias: str
        """
        self.FieldName = None
        self.FieldType = None
        self.Alias = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.FieldType = params.get("FieldType")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceObject(AbstractModel):
    """数据质量数据对象

    """

    def __init__(self):
        r"""
        :param SourceObjectDataTypeName: 源字段详细类型，int、string
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectDataTypeName: str
        :param SourceObjectValue: 源字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceObjectValue: str
        """
        self.SourceObjectDataTypeName = None
        self.SourceObjectValue = None


    def _deserialize(self, params):
        self.SourceObjectDataTypeName = params.get("SourceObjectDataTypeName")
        self.SourceObjectValue = params.get("SourceObjectValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedValue(AbstractModel):
    """速度值对象

    """

    def __init__(self):
        r"""
        :param Time: 带毫秒的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param Speed: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Speed: float
        """
        self.Time = None
        self.Speed = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Speed = params.get("Speed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartIntegrationTaskRequest(AbstractModel):
    """StartIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartIntegrationTaskResponse(AbstractModel):
    """StartIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class StopIntegrationTaskRequest(AbstractModel):
    """StopIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopIntegrationTaskResponse(AbstractModel):
    """StopIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class SubmitCustomFunctionRequest(AbstractModel):
    """SubmitCustomFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数唯一标识
        :type FunctionId: str
        :param ClusterIdentifier: 集群实例 ID
        :type ClusterIdentifier: str
        :param Comment: 备注信息
        :type Comment: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.FunctionId = None
        self.ClusterIdentifier = None
        self.Comment = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.ClusterIdentifier = params.get("ClusterIdentifier")
        self.Comment = params.get("Comment")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCustomFunctionResponse(AbstractModel):
    """SubmitCustomFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionId: 函数唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionId: str
        :param ErrorMessage: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionId = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionId = params.get("FunctionId")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class SubmitTaskRequest(AbstractModel):
    """SubmitTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param VersionRemark: 版本备注
        :type VersionRemark: str
        :param StartScheduling: 是否启动调度
        :type StartScheduling: bool
        """
        self.ProjectId = None
        self.TaskId = None
        self.VersionRemark = None
        self.StartScheduling = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.VersionRemark = params.get("VersionRemark")
        self.StartScheduling = params.get("StartScheduling")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTaskResponse(AbstractModel):
    """SubmitTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 成功或者失败
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class SubmitWorkflow(AbstractModel):
    """提交工作流实体

    """

    def __init__(self):
        r"""
        :param TaskIds: 被提交的任务id集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIds: list of str
        :param Result: 执行结果
        :type Result: bool
        :param ErrorDesc: 执行情况备注
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDesc: str
        :param ErrorId: 执行情况id
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorId: str
        """
        self.TaskIds = None
        self.Result = None
        self.ErrorDesc = None
        self.ErrorId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.Result = params.get("Result")
        self.ErrorDesc = params.get("ErrorDesc")
        self.ErrorId = params.get("ErrorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitWorkflowRequest(AbstractModel):
    """SubmitWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param VersionRemark: 提交的版本备注
        :type VersionRemark: str
        :param StartScheduling: 是否启动调度
        :type StartScheduling: bool
        """
        self.ProjectId = None
        self.WorkflowId = None
        self.VersionRemark = None
        self.StartScheduling = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.WorkflowId = params.get("WorkflowId")
        self.VersionRemark = params.get("VersionRemark")
        self.StartScheduling = params.get("StartScheduling")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitWorkflowResponse(AbstractModel):
    """SubmitWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflow`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SubmitWorkflow()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SubscribeReceiver(AbstractModel):
    """订阅接收人

    """

    def __init__(self):
        r"""
        :param ReceiverUserId: 接收人Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverUserId: int
        :param ReceiverName: 接收人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverName: str
        """
        self.ReceiverUserId = None
        self.ReceiverName = None


    def _deserialize(self, params):
        self.ReceiverUserId = params.get("ReceiverUserId")
        self.ReceiverName = params.get("ReceiverName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeWebHook(AbstractModel):
    """群机器人订阅配置

    """

    def __init__(self):
        r"""
        :param HookType: 群机器人类型，当前支持飞书
注意：此字段可能返回 null，表示取不到有效值。
        :type HookType: str
        :param HookAddress: 群机器人webhook地址，配置方式参考https://cloud.tencent.com/document/product/1254/70736
注意：此字段可能返回 null，表示取不到有效值。
        :type HookAddress: str
        """
        self.HookType = None
        self.HookAddress = None


    def _deserialize(self, params):
        self.HookType = params.get("HookType")
        self.HookAddress = params.get("HookAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendIntegrationTaskRequest(AbstractModel):
    """SuspendIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendIntegrationTaskResponse(AbstractModel):
    """SuspendIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TableConfig(AbstractModel):
    """规则表变量替换

    """

    def __init__(self):
        r"""
        :param DatabaseId: 数据库Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param TableId: 表Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableKey: 表Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TableKey: str
        :param FieldConfig: 字段变量
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldConfig: list of FieldConfig
        """
        self.DatabaseId = None
        self.DatabaseName = None
        self.TableId = None
        self.TableName = None
        self.TableKey = None
        self.FieldConfig = None


    def _deserialize(self, params):
        self.DatabaseId = params.get("DatabaseId")
        self.DatabaseName = params.get("DatabaseName")
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        self.TableKey = params.get("TableKey")
        if params.get("FieldConfig") is not None:
            self.FieldConfig = []
            for item in params.get("FieldConfig"):
                obj = FieldConfig()
                obj._deserialize(item)
                self.FieldConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfo(AbstractModel):
    """元数据表详细信息

    """

    def __init__(self):
        r"""
        :param TableId: 表Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        """
        self.TableId = None
        self.TableName = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableQualityDetail(AbstractModel):
    """表质量详情

    """

    def __init__(self):
        r"""
        :param DatabaseId: 数据库id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        :param DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param TableId: 表id
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param OwnerUserId: 表责任人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserId: int
        :param OwnerUserName: 表责任人名
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserName: str
        :param DatabaseScore: 库得分
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseScore: float
        :param TableScore: 表得分
注意：此字段可能返回 null，表示取不到有效值。
        :type TableScore: float
        :param LastPeriodRatio: 表环比
注意：此字段可能返回 null，表示取不到有效值。
        :type LastPeriodRatio: float
        """
        self.DatabaseId = None
        self.DatabaseName = None
        self.TableId = None
        self.TableName = None
        self.OwnerUserId = None
        self.OwnerUserName = None
        self.DatabaseScore = None
        self.TableScore = None
        self.LastPeriodRatio = None


    def _deserialize(self, params):
        self.DatabaseId = params.get("DatabaseId")
        self.DatabaseName = params.get("DatabaseName")
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        self.OwnerUserId = params.get("OwnerUserId")
        self.OwnerUserName = params.get("OwnerUserName")
        self.DatabaseScore = params.get("DatabaseScore")
        self.TableScore = params.get("TableScore")
        self.LastPeriodRatio = params.get("LastPeriodRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableQualityDetailPage(AbstractModel):
    """表质量分分页结果

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: 表质量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TableQualityDetail
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TableQualityDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableScoreStatisticsInfo(AbstractModel):
    """表评分统计信息

    """

    def __init__(self):
        r"""
        :param Level: 等级 1、2、3、4、5
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Scale: 占比
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param TableNumber: 表数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TableNumber: int
        """
        self.Level = None
        self.Scale = None
        self.TableNumber = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.Scale = params.get("Scale")
        self.TableNumber = params.get("TableNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAlarmInfo(AbstractModel):
    """任务告警信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param RegularName: 规则名称
        :type RegularName: str
        :param RegularStatus: 规则状态(0表示关闭，1表示打开)
        :type RegularStatus: int
        :param AlarmLevel: 告警级别(0表示普通，1表示重要，2表示紧急)
        :type AlarmLevel: int
        :param AlarmIndicator: 告警指标,0表示任务失败，1表示任务运行超时，2表示任务停止，3表示任务暂停
，4写入速度，5读取速度，6读取吞吐，7写入吞吐, 8脏数据字节数，9脏数据条数
        :type AlarmIndicator: int
        :param AlarmWay: 告警方式,多个用逗号隔开（1:邮件，2:短信，3:微信，4:语音，5:代表企业微信，6:http）
        :type AlarmWay: str
        :param AlarmRecipientId: 告警接收人ID，多个用逗号隔开
        :type AlarmRecipientId: str
        :param TaskType: 任务类型(201表示实时，202表示离线)
        :type TaskType: int
        :param AlarmRecipientName: 告警接收人昵称，多个用逗号隔开
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmRecipientName: str
        :param Id: 主键ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param RegularId: 规则ID
        :type RegularId: str
        :param TriggerType: 指标阈值(1表示离线任务第一次运行失败，2表示离线任务所有重试完成后失败)
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: int
        :param EstimatedTime: 预计的超时时间(分钟级别)
注意：此字段可能返回 null，表示取不到有效值。
        :type EstimatedTime: int
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param Creater: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creater: str
        :param AlarmIndicatorDesc: 告警指标描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmIndicatorDesc: str
        :param Operator: 实时任务告警需要的参数，1是大于2是小于
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: int
        :param NodeId: 节点id，多个逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param NodeName: 节点名称，多个逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        """
        self.TaskId = None
        self.RegularName = None
        self.RegularStatus = None
        self.AlarmLevel = None
        self.AlarmIndicator = None
        self.AlarmWay = None
        self.AlarmRecipientId = None
        self.TaskType = None
        self.AlarmRecipientName = None
        self.Id = None
        self.RegularId = None
        self.TriggerType = None
        self.EstimatedTime = None
        self.ProjectId = None
        self.Creater = None
        self.AlarmIndicatorDesc = None
        self.Operator = None
        self.NodeId = None
        self.NodeName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RegularName = params.get("RegularName")
        self.RegularStatus = params.get("RegularStatus")
        self.AlarmLevel = params.get("AlarmLevel")
        self.AlarmIndicator = params.get("AlarmIndicator")
        self.AlarmWay = params.get("AlarmWay")
        self.AlarmRecipientId = params.get("AlarmRecipientId")
        self.TaskType = params.get("TaskType")
        self.AlarmRecipientName = params.get("AlarmRecipientName")
        self.Id = params.get("Id")
        self.RegularId = params.get("RegularId")
        self.TriggerType = params.get("TriggerType")
        self.EstimatedTime = params.get("EstimatedTime")
        self.ProjectId = params.get("ProjectId")
        self.Creater = params.get("Creater")
        self.AlarmIndicatorDesc = params.get("AlarmIndicatorDesc")
        self.Operator = params.get("Operator")
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCanvasInfo(AbstractModel):
    """任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param WorkflowId: 工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectIdent: 项目标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectIdent: str
        :param Status: 任务状态，'Y','F','O','T','INVALID' 分别表示调度中、已停止、已暂停、停止中、已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param TaskTypeId: 任务类型id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param TaskTypeDesc: 任务类型描述，其中任务类型id和任务类型描述的对应的关系为
20	通用数据同步任务
21	JDBC SQL
22	Tbase
25	数据ETL
30	Python
31	PySpark
34	Hive SQL
35	Shell
36	Spark SQL
37	HDFS到HBase
38	SHELL
39	Spark
45	DATA_QUALITY
55	THIVE到MYSQL
56	THIVE到PG
66	HDFS到PG
67	HDFS到Oracle
68	HDFS到MYSQL
69	FTP到HDFS
70	HIVE SQL
72	HIVE到HDFS
75	HDFS到HIVE
81	PYTHONSQL脚本
82	SPARKSCALA计算
83	虫洞任务
84	校验对账文件
85	HDFS到THIVE
86	TDW到HDFS
87	HDFS到TDW
88	校验对账文件
91	FLINK任务
92	MapReduce
98	custom topology
99	kafkatoHDFS
100	kafkatoHbase
101	MYSQL导入至HIVE(DX)
104	MYSQL到HIVE
105	HIVE到MYSQL
106	SQL SERVER到HIVE
107	HIVE到SQL SERVER
108	ORACLE到HIVE
109	HIVE到ORACLE
111	HIVE到MYSQL(NEW)
112	HIVE到PG
113	HIVE到PHOENIX
118	MYSQL到HDFS
119	PG到HDFS
120	ORACLE到HDFS
121	数据质量
10000	自定义业务
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeDesc: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param FolderId: 文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param FirstSubmitTime: 最近提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstSubmitTime: str
        :param FirstRunTime: 首次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstRunTime: str
        :param ScheduleDesc: 调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleDesc: str
        :param InCharge: 负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type InCharge: str
        :param CycleUnit: 调度周期类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleUnit: str
        :param LeftCoordinate: 画布x轴坐标点
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftCoordinate: float
        :param TopCoordinate: 画布y轴坐标点
注意：此字段可能返回 null，表示取不到有效值。
        :type TopCoordinate: float
        :param VirtualFlag: 跨工作流虚拟任务标识；true标识跨工作流任务；false标识本工作流任务
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualFlag: bool
        :param TaskAction: 弹性周期配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        :param DelayTime: 延迟时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: int
        """
        self.TaskId = None
        self.TaskName = None
        self.WorkflowId = None
        self.WorkflowName = None
        self.ProjectName = None
        self.ProjectIdent = None
        self.Status = None
        self.TaskTypeId = None
        self.TaskTypeDesc = None
        self.ProjectId = None
        self.FolderName = None
        self.FolderId = None
        self.FirstSubmitTime = None
        self.FirstRunTime = None
        self.ScheduleDesc = None
        self.InCharge = None
        self.CycleUnit = None
        self.LeftCoordinate = None
        self.TopCoordinate = None
        self.VirtualFlag = None
        self.TaskAction = None
        self.DelayTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.ProjectName = params.get("ProjectName")
        self.ProjectIdent = params.get("ProjectIdent")
        self.Status = params.get("Status")
        self.TaskTypeId = params.get("TaskTypeId")
        self.TaskTypeDesc = params.get("TaskTypeDesc")
        self.ProjectId = params.get("ProjectId")
        self.FolderName = params.get("FolderName")
        self.FolderId = params.get("FolderId")
        self.FirstSubmitTime = params.get("FirstSubmitTime")
        self.FirstRunTime = params.get("FirstRunTime")
        self.ScheduleDesc = params.get("ScheduleDesc")
        self.InCharge = params.get("InCharge")
        self.CycleUnit = params.get("CycleUnit")
        self.LeftCoordinate = params.get("LeftCoordinate")
        self.TopCoordinate = params.get("TopCoordinate")
        self.VirtualFlag = params.get("VirtualFlag")
        self.TaskAction = params.get("TaskAction")
        self.DelayTime = params.get("DelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskExtInfo(AbstractModel):
    """任务扩展信息

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
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
        


class TaskInfoData(AbstractModel):
    """任务信息数据

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param WorkflowId: 工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectIdent: 项目标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectIdent: str
        :param Status: 任务状态，'Y','F','O','T','INVALID' 分别表示调度中、已停止、已暂停、停止中、已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param FolderId: 文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param InCharge: 负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type InCharge: str
        :param VirtualFlag: 跨工作流虚拟任务标识；true标识跨工作流任务；false标识本工作流任务
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualFlag: bool
        :param DelayTime: 延时实例生成时间(延时调度)，转换为分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: int
        :param CrontabExpression: crontab表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param LastUpdate: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdate: str
        :param StartTime: 生效日期
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束日期
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param ExecutionStartTime: 执行时间左闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        :param ExecutionEndTime: 执行时间右闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        :param CycleType: 周期类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: int
        :param CycleStep: 步长
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStep: int
        :param StartupTime: 延时执行时间（延时执行) 对应为 开始时间 状态为分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupTime: int
        :param RetryWait: 重试等待时间,单位分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryWait: int
        :param Retriable: 是否可重试
注意：此字段可能返回 null，表示取不到有效值。
        :type Retriable: int
        :param TaskAction: 调度扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        :param TryLimit: 运行次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TryLimit: int
        :param RunPriority: 运行优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type RunPriority: int
        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param BrokerIp: 指定的运行节点
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerIp: str
        :param ClusterId: 集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param MinDateTime: 最小数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MinDateTime: str
        :param MaxDateTime: 最大数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDateTime: str
        :param SelfDepend: 是否自身依赖 是1 否2 并行3
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfDepend: int
        :param TaskExt: 扩展属性
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskExt: list of TaskExtInfo
        :param Notes: 任务备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Notes: str
        :param YarnQueue: 队列
注意：此字段可能返回 null，表示取不到有效值。
        :type YarnQueue: str
        :param Submit: 任务版本是否已提交
注意：此字段可能返回 null，表示取不到有效值。
        :type Submit: bool
        :param LastSchedulerCommitTime: 最新调度计划变更时间 仅生产态
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSchedulerCommitTime: str
        :param NormalizedJobStartTime: 仅生产态存储于生产态序列化任务信息, 减少base CPU重复密集计算
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalizedJobStartTime: str
        :param SourceServer: 源数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceServer: str
        :param Creater: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creater: str
        :param DependencyRel: 分支，依赖关系，and/or, 默认and
注意：此字段可能返回 null，表示取不到有效值。
        :type DependencyRel: str
        :param DependencyWorkflow: 是否支持工作流依赖 yes / no 默认 no
注意：此字段可能返回 null，表示取不到有效值。
        :type DependencyWorkflow: str
        :param Params: 任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of ParamInfo
        :param UpdateUser: 最后修改的人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUser: str
        :param UpdateTime: 最后修改的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param UpdateUserId: 最后修改的人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserId: str
        :param SchedulerDesc: 调度计划
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerDesc: str
        :param ResourceGroup: 资源组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroup: str
        :param VersionDesc: 版本提交说明
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionDesc: str
        :param RealWorkflowId: 真实工作流Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RealWorkflowId: str
        :param TargetServer: 目标数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetServer: str
        :param DependencyConfigs: 依赖配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DependencyConfigs: list of DependencyConfig
        :param VirtualTaskStatus: 虚拟任务状态1
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualTaskStatus: str
        :param VirtualTaskId: 虚拟任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualTaskId: str
        """
        self.TaskId = None
        self.TaskName = None
        self.WorkflowId = None
        self.WorkflowName = None
        self.ProjectName = None
        self.ProjectIdent = None
        self.Status = None
        self.ProjectId = None
        self.FolderName = None
        self.FolderId = None
        self.InCharge = None
        self.VirtualFlag = None
        self.DelayTime = None
        self.CrontabExpression = None
        self.CreateTime = None
        self.LastUpdate = None
        self.StartTime = None
        self.EndTime = None
        self.ExecutionStartTime = None
        self.ExecutionEndTime = None
        self.CycleType = None
        self.CycleStep = None
        self.StartupTime = None
        self.RetryWait = None
        self.Retriable = None
        self.TaskAction = None
        self.TryLimit = None
        self.RunPriority = None
        self.TaskType = None
        self.BrokerIp = None
        self.ClusterId = None
        self.MinDateTime = None
        self.MaxDateTime = None
        self.SelfDepend = None
        self.TaskExt = None
        self.Notes = None
        self.YarnQueue = None
        self.Submit = None
        self.LastSchedulerCommitTime = None
        self.NormalizedJobStartTime = None
        self.SourceServer = None
        self.Creater = None
        self.DependencyRel = None
        self.DependencyWorkflow = None
        self.Params = None
        self.UpdateUser = None
        self.UpdateTime = None
        self.UpdateUserId = None
        self.SchedulerDesc = None
        self.ResourceGroup = None
        self.VersionDesc = None
        self.RealWorkflowId = None
        self.TargetServer = None
        self.DependencyConfigs = None
        self.VirtualTaskStatus = None
        self.VirtualTaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.ProjectName = params.get("ProjectName")
        self.ProjectIdent = params.get("ProjectIdent")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.FolderName = params.get("FolderName")
        self.FolderId = params.get("FolderId")
        self.InCharge = params.get("InCharge")
        self.VirtualFlag = params.get("VirtualFlag")
        self.DelayTime = params.get("DelayTime")
        self.CrontabExpression = params.get("CrontabExpression")
        self.CreateTime = params.get("CreateTime")
        self.LastUpdate = params.get("LastUpdate")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ExecutionStartTime = params.get("ExecutionStartTime")
        self.ExecutionEndTime = params.get("ExecutionEndTime")
        self.CycleType = params.get("CycleType")
        self.CycleStep = params.get("CycleStep")
        self.StartupTime = params.get("StartupTime")
        self.RetryWait = params.get("RetryWait")
        self.Retriable = params.get("Retriable")
        self.TaskAction = params.get("TaskAction")
        self.TryLimit = params.get("TryLimit")
        self.RunPriority = params.get("RunPriority")
        self.TaskType = params.get("TaskType")
        self.BrokerIp = params.get("BrokerIp")
        self.ClusterId = params.get("ClusterId")
        self.MinDateTime = params.get("MinDateTime")
        self.MaxDateTime = params.get("MaxDateTime")
        self.SelfDepend = params.get("SelfDepend")
        if params.get("TaskExt") is not None:
            self.TaskExt = []
            for item in params.get("TaskExt"):
                obj = TaskExtInfo()
                obj._deserialize(item)
                self.TaskExt.append(obj)
        self.Notes = params.get("Notes")
        self.YarnQueue = params.get("YarnQueue")
        self.Submit = params.get("Submit")
        self.LastSchedulerCommitTime = params.get("LastSchedulerCommitTime")
        self.NormalizedJobStartTime = params.get("NormalizedJobStartTime")
        self.SourceServer = params.get("SourceServer")
        self.Creater = params.get("Creater")
        self.DependencyRel = params.get("DependencyRel")
        self.DependencyWorkflow = params.get("DependencyWorkflow")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Params.append(obj)
        self.UpdateUser = params.get("UpdateUser")
        self.UpdateTime = params.get("UpdateTime")
        self.UpdateUserId = params.get("UpdateUserId")
        self.SchedulerDesc = params.get("SchedulerDesc")
        self.ResourceGroup = params.get("ResourceGroup")
        self.VersionDesc = params.get("VersionDesc")
        self.RealWorkflowId = params.get("RealWorkflowId")
        self.TargetServer = params.get("TargetServer")
        if params.get("DependencyConfigs") is not None:
            self.DependencyConfigs = []
            for item in params.get("DependencyConfigs"):
                obj = DependencyConfig()
                obj._deserialize(item)
                self.DependencyConfigs.append(obj)
        self.VirtualTaskStatus = params.get("VirtualTaskStatus")
        self.VirtualTaskId = params.get("VirtualTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfoDataPage(AbstractModel):
    """任务分页数据查询

    """

    def __init__(self):
        r"""
        :param PageNumber: 页号
        :type PageNumber: int
        :param PageSize: 页大小
        :type PageSize: int
        :param Items: 任务集合信息
        :type Items: list of TaskInfoData
        :param TotalCount: 总页数1
        :type TotalCount: int
        """
        self.PageNumber = None
        self.PageSize = None
        self.Items = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TaskInfoData()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInnerInfo(AbstractModel):
    """任务属性

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskName: 任务名
        :type TaskName: str
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param CycleType: 周期类型  0:crontab类型, 1:分钟，2:小时，3:天，4:周，5:月，6:一次性，7:用户驱动，10:弹性周期 周,11:弹性周期 月,12:年,13:即时触发Instant类型，与正常周期调度任务逻辑隔离
        :type CycleType: int
        :param VirtualTaskId: 虚拟任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualTaskId: str
        :param VirtualFlag: 虚拟任务标记
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualFlag: bool
        :param RealWorkflowId: 真实任务工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type RealWorkflowId: str
        """
        self.TaskId = None
        self.TaskName = None
        self.WorkflowId = None
        self.CycleType = None
        self.VirtualTaskId = None
        self.VirtualFlag = None
        self.RealWorkflowId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.WorkflowId = params.get("WorkflowId")
        self.CycleType = params.get("CycleType")
        self.VirtualTaskId = params.get("VirtualTaskId")
        self.VirtualFlag = params.get("VirtualFlag")
        self.RealWorkflowId = params.get("RealWorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceDetail(AbstractModel):
    """离线任务实例详情

    """

    def __init__(self):
        r"""
        :param TaskRunId: 实例id
        :type TaskRunId: str
        :param TaskId: 任务id
        :type TaskId: str
        :param CurRunDate: 实例数据运行时间
        :type CurRunDate: str
        :param IssueDate: 实例实际运行时间
        :type IssueDate: str
        :param InlongTaskId: InLong任务Id
        :type InlongTaskId: str
        :param ExecutorGroupId: 执行资源组id
        :type ExecutorGroupId: str
        :param TaskRunType: 任务类型(1 调试运行,2 调度执行)
        :type TaskRunType: int
        :param State: 任务状态(1 正在执行,2 成功,3 失败,4 等待终止,5 正在终止,6 已终止,7 终止失败,9 等待执行)
        :type State: int
        :param StartTime: 实例开始运行时间，格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 实例结束运行时间，格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param BrokerIp: Broker IP
        :type BrokerIp: str
        :param PodName: 运行实例的EKS Pod名称
        :type PodName: str
        :param NextRunDate: 下一个调度周期的数据运行时间
        :type NextRunDate: str
        :param CreateUin: 创建者的账号Id
        :type CreateUin: int
        :param OperatorUin: 操作者的账号Id
        :type OperatorUin: int
        :param OwnerUin: 拥有者的账号Id
        :type OwnerUin: int
        :param AppId: App Id
        :type AppId: int
        :param ProjectId: WeData项目id
        :type ProjectId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param TaskName: 任务名称
        :type TaskName: str
        """
        self.TaskRunId = None
        self.TaskId = None
        self.CurRunDate = None
        self.IssueDate = None
        self.InlongTaskId = None
        self.ExecutorGroupId = None
        self.TaskRunType = None
        self.State = None
        self.StartTime = None
        self.EndTime = None
        self.BrokerIp = None
        self.PodName = None
        self.NextRunDate = None
        self.CreateUin = None
        self.OperatorUin = None
        self.OwnerUin = None
        self.AppId = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.TaskName = None


    def _deserialize(self, params):
        self.TaskRunId = params.get("TaskRunId")
        self.TaskId = params.get("TaskId")
        self.CurRunDate = params.get("CurRunDate")
        self.IssueDate = params.get("IssueDate")
        self.InlongTaskId = params.get("InlongTaskId")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        self.TaskRunType = params.get("TaskRunType")
        self.State = params.get("State")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BrokerIp = params.get("BrokerIp")
        self.PodName = params.get("PodName")
        self.NextRunDate = params.get("NextRunDate")
        self.CreateUin = params.get("CreateUin")
        self.OperatorUin = params.get("OperatorUin")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceInfo(AbstractModel):
    """任务实例信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param WorkflowId: 工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectIdent: 项目标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectIdent: str
        :param State: 实例状态，0等待事件，1等待上游，2等待运行，3运行中，4正在终止，5失败重试，6失败，7成功
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param TaskTypeId: 任务类型id，26离线同步，30Python，31PySpark，32DLC，33Impala，34Hive SQL，35Shell，36Spark SQL，39Spark，40CDW PG，92MapReduce
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param TaskTypeDesc: 任务类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeDesc: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param FolderId: 文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param SchedulerDesc: 调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerDesc: str
        :param InCharge: 负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type InCharge: str
        :param CycleType: 调度周期类型，I分钟，H小时，D天，W周，M月，Y年，O一次性，C crontab
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param StartTime: 实例开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 实例结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param InstanceType: 实例类型，0补录实例，1周期实例，2非周期实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param TryLimit: 最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TryLimit: int
        :param Tries: 当前重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tries: int
        :param SchedulerDateTime: 计划调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerDateTime: str
        :param CostTime: 运行耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: str
        """
        self.TaskId = None
        self.TaskName = None
        self.WorkflowId = None
        self.WorkflowName = None
        self.ProjectName = None
        self.ProjectIdent = None
        self.State = None
        self.TaskTypeId = None
        self.TaskTypeDesc = None
        self.ProjectId = None
        self.FolderName = None
        self.FolderId = None
        self.SchedulerDesc = None
        self.InCharge = None
        self.CycleType = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceType = None
        self.TryLimit = None
        self.Tries = None
        self.SchedulerDateTime = None
        self.CostTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.ProjectName = params.get("ProjectName")
        self.ProjectIdent = params.get("ProjectIdent")
        self.State = params.get("State")
        self.TaskTypeId = params.get("TaskTypeId")
        self.TaskTypeDesc = params.get("TaskTypeDesc")
        self.ProjectId = params.get("ProjectId")
        self.FolderName = params.get("FolderName")
        self.FolderId = params.get("FolderId")
        self.SchedulerDesc = params.get("SchedulerDesc")
        self.InCharge = params.get("InCharge")
        self.CycleType = params.get("CycleType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceType = params.get("InstanceType")
        self.TryLimit = params.get("TryLimit")
        self.Tries = params.get("Tries")
        self.SchedulerDateTime = params.get("SchedulerDateTime")
        self.CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLinkInfo(AbstractModel):
    """任务依赖的边信息

    """

    def __init__(self):
        r"""
        :param TaskTo: 下游任务id
        :type TaskTo: str
        :param TaskFrom: 上游任务id
        :type TaskFrom: str
        :param LinkType: 依赖边类型 1、“real_real”表示任务->任务；2、"virtual_real" 跨工作流任务->任务
        :type LinkType: str
        :param LinkId: 依赖边id
        :type LinkId: str
        """
        self.TaskTo = None
        self.TaskFrom = None
        self.LinkType = None
        self.LinkId = None


    def _deserialize(self, params):
        self.TaskTo = params.get("TaskTo")
        self.TaskFrom = params.get("TaskFrom")
        self.LinkType = params.get("LinkType")
        self.LinkId = params.get("LinkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLockStatus(AbstractModel):
    """任务锁的状态

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param Locker: 持锁者
        :type Locker: str
        :param IsLocker: 当前操作用户是否为持锁者，1表示为持锁者，0表示为不为持锁者
        :type IsLocker: int
        :param IsRob: 是否可以抢锁，1表示可以抢锁，0表示不可以抢锁
        :type IsRob: int
        """
        self.TaskId = None
        self.Locker = None
        self.IsLocker = None
        self.IsRob = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Locker = params.get("Locker")
        self.IsLocker = params.get("IsLocker")
        self.IsRob = params.get("IsRob")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogRequest(AbstractModel):
    """TaskLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param StartTime: 起始时间戳，单位毫秒
        :type StartTime: int
        :param EndTime: 结束时间戳，单位毫秒
        :type EndTime: int
        :param ProjectId: 项目id
        :type ProjectId: str
        :param Limit: 拉取日志数量，默认100
        :type Limit: int
        :param OrderType: 日志排序 desc 倒序 asc 顺序
        :type OrderType: str
        :param TaskType: 实时任务 201   离线任务 202  默认实时任务
        :type TaskType: int
        """
        self.TaskId = None
        self.StartTime = None
        self.EndTime = None
        self.ProjectId = None
        self.Limit = None
        self.OrderType = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProjectId = params.get("ProjectId")
        self.Limit = params.get("Limit")
        self.OrderType = params.get("OrderType")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogResponse(AbstractModel):
    """TaskLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogContentList: 详细日志
        :type LogContentList: list of LogContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogContentList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogContentList") is not None:
            self.LogContentList = []
            for item in params.get("LogContentList"):
                obj = LogContent()
                obj._deserialize(item)
                self.LogContentList.append(obj)
        self.RequestId = params.get("RequestId")


class TaskReportDetail(AbstractModel):
    """离线任务统计指标明细

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param InstanceId: 任务实例ID
        :type InstanceId: str
        :param CurRunDate: 实例数据运行时间
        :type CurRunDate: str
        :param IssueDate: 实例实际下发时间
        :type IssueDate: str
        :param TaskState: 任务状态码。1 正在执行,2 成功,3 失败,4 等待终止,5 正在终止,6 已终止,7 终止失败,9 等待执行。
        :type TaskState: str
        :param TotalReadRecords: 总读取条数
        :type TotalReadRecords: int
        :param TotalReadBytes: 总读取字节数
        :type TotalReadBytes: int
        :param TotalWriteRecords: 总写入条数
        :type TotalWriteRecords: int
        :param TotalWriteBytes: 总写入字节数
        :type TotalWriteBytes: int
        :param RecordSpeed: 写入速度（条/秒）
        :type RecordSpeed: int
        :param ByteSpeed: 吞吐（Byte/秒）
        :type ByteSpeed: float
        :param TotalErrorRecords: 脏数据条数
        :type TotalErrorRecords: int
        """
        self.TaskId = None
        self.InstanceId = None
        self.CurRunDate = None
        self.IssueDate = None
        self.TaskState = None
        self.TotalReadRecords = None
        self.TotalReadBytes = None
        self.TotalWriteRecords = None
        self.TotalWriteBytes = None
        self.RecordSpeed = None
        self.ByteSpeed = None
        self.TotalErrorRecords = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.InstanceId = params.get("InstanceId")
        self.CurRunDate = params.get("CurRunDate")
        self.IssueDate = params.get("IssueDate")
        self.TaskState = params.get("TaskState")
        self.TotalReadRecords = params.get("TotalReadRecords")
        self.TotalReadBytes = params.get("TotalReadBytes")
        self.TotalWriteRecords = params.get("TotalWriteRecords")
        self.TotalWriteBytes = params.get("TotalWriteBytes")
        self.RecordSpeed = params.get("RecordSpeed")
        self.ByteSpeed = params.get("ByteSpeed")
        self.TotalErrorRecords = params.get("TotalErrorRecords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskScriptContent(AbstractModel):
    """任务执行脚本

    """

    def __init__(self):
        r"""
        :param ScriptContent: 脚本内容 base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContent: str
        """
        self.ScriptContent = None


    def _deserialize(self, params):
        self.ScriptContent = params.get("ScriptContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThresholdValue(AbstractModel):
    """数据质量阈值

    """

    def __init__(self):
        r"""
        :param ValueType: 阈值类型  1.低阈值  2.高阈值   3.普通阈值  4.枚举值
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueType: int
        :param Value: 阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.ValueType = None
        self.Value = None


    def _deserialize(self, params):
        self.ValueType = params.get("ValueType")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopTableStat(AbstractModel):
    """质量概览表排行结果

    """

    def __init__(self):
        r"""
        :param AlarmTables: 告警表列表
        :type AlarmTables: list of TopTableStatItem
        :param PipelineTables: 阻塞表列表
        :type PipelineTables: list of TopTableStatItem
        """
        self.AlarmTables = None
        self.PipelineTables = None


    def _deserialize(self, params):
        if params.get("AlarmTables") is not None:
            self.AlarmTables = []
            for item in params.get("AlarmTables"):
                obj = TopTableStatItem()
                obj._deserialize(item)
                self.AlarmTables.append(obj)
        if params.get("PipelineTables") is not None:
            self.PipelineTables = []
            for item in params.get("PipelineTables"):
                obj = TopTableStatItem()
                obj._deserialize(item)
                self.PipelineTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopTableStatItem(AbstractModel):
    """质量概览表排行元素

    """

    def __init__(self):
        r"""
        :param TableId: 表Id
        :type TableId: str
        :param TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param Cnt: 数
        :type Cnt: int
        """
        self.TableId = None
        self.TableName = None
        self.Cnt = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        self.TableName = params.get("TableName")
        self.Cnt = params.get("Cnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerEventRequest(AbstractModel):
    """TriggerEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Name: 案例名称
        :type Name: str
        :param Dimension: 时间格式：如果选择触发时间：2022年6月21，则设置为20220621
        :type Dimension: str
        :param Description: 描述信息
        :type Description: str
        """
        self.ProjectId = None
        self.Name = None
        self.Dimension = None
        self.Description = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.Dimension = params.get("Dimension")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerEventResponse(AbstractModel):
    """TriggerEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 成功或者失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20210820.models.BatchReturn`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BatchReturn()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class UnlockIntegrationTaskRequest(AbstractModel):
    """UnlockIntegrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockIntegrationTaskResponse(AbstractModel):
    """UnlockIntegrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 操作成功与否标识
        :type Data: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UpdateInLongAgentRequest(AbstractModel):
    """UpdateInLongAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 采集器ID
        :type AgentId: str
        :param ProjectId: WeData项目ID
        :type ProjectId: str
        :param AgentName: 采集器名称
        :type AgentName: str
        :param ExecutorGroupId: 集成资源组ID
        :type ExecutorGroupId: str
        """
        self.AgentId = None
        self.ProjectId = None
        self.AgentName = None
        self.ExecutorGroupId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.ProjectId = params.get("ProjectId")
        self.AgentName = params.get("AgentName")
        self.ExecutorGroupId = params.get("ExecutorGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInLongAgentResponse(AbstractModel):
    """UpdateInLongAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserFileDTO(AbstractModel):
    """用户文件信息

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileExtensionType: 文件类型，如 jar zip 等
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtensionType: str
        :param FileUploadType: 文件上传类型，资源管理为 resource
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUploadType: str
        :param Md5Value: 文件MD5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5Value: str
        :param CreateTime: 创建时间，秒级别的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间，秒级别的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Size: 文件大小，单位为字节
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param LocalPath: 本地路径
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalPath: str
        :param LocalTmpPath: 本地临时路径
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalTmpPath: str
        :param RemotePath: 远程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RemotePath: str
        :param OwnerName: 文件拥有者名字
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerName: str
        :param Owner: 文件拥有者uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param PathDepth: 文件深度
注意：此字段可能返回 null，表示取不到有效值。
        :type PathDepth: str
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param ExtraInfo: 附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: str
        :param ZipPath: 本地临时压缩文件绝对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ZipPath: str
        :param Bucket: 文件所属存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 文件所属存储桶的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.ResourceId = None
        self.FileName = None
        self.FileExtensionType = None
        self.FileUploadType = None
        self.Md5Value = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Size = None
        self.LocalPath = None
        self.LocalTmpPath = None
        self.RemotePath = None
        self.OwnerName = None
        self.Owner = None
        self.PathDepth = None
        self.ProjectId = None
        self.ExtraInfo = None
        self.ZipPath = None
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.FileName = params.get("FileName")
        self.FileExtensionType = params.get("FileExtensionType")
        self.FileUploadType = params.get("FileUploadType")
        self.Md5Value = params.get("Md5Value")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Size = params.get("Size")
        self.LocalPath = params.get("LocalPath")
        self.LocalTmpPath = params.get("LocalTmpPath")
        self.RemotePath = params.get("RemotePath")
        self.OwnerName = params.get("OwnerName")
        self.Owner = params.get("Owner")
        self.PathDepth = params.get("PathDepth")
        self.ProjectId = params.get("ProjectId")
        self.ExtraInfo = params.get("ExtraInfo")
        self.ZipPath = params.get("ZipPath")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeightInfo(AbstractModel):
    """权重信息

    """

    def __init__(self):
        r"""
        :param Weight: 权重
        :type Weight: int
        :param QualityDim: 维度类型 1：准确性，2：唯一性，3：完整性，4：一致性，5：及时性，6：有效性
        :type QualityDim: int
        """
        self.Weight = None
        self.QualityDim = None


    def _deserialize(self, params):
        self.Weight = params.get("Weight")
        self.QualityDim = params.get("QualityDim")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Workflow(AbstractModel):
    """工作流信息

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流id
        :type WorkflowId: str
        :param Owner: 责任人
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param OwnerId: 责任人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerId: str
        :param ProjectId: 项目id
        :type ProjectId: str
        :param ProjectIdent: 项目标识
        :type ProjectIdent: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param WorkflowDesc: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowDesc: str
        :param WorkflowName: 工作流名称
        :type WorkflowName: str
        :param FolderId: 所属文件夹id
        :type FolderId: str
        :param UserGroupId: 工作流所属用户分组id 若有多个,分号隔开: a;b;c
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param UserGroupName: 工作流所属用户分组名称  若有多个,分号隔开: a;b;c
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupName: str
        """
        self.WorkflowId = None
        self.Owner = None
        self.OwnerId = None
        self.ProjectId = None
        self.ProjectIdent = None
        self.ProjectName = None
        self.WorkflowDesc = None
        self.WorkflowName = None
        self.FolderId = None
        self.UserGroupId = None
        self.UserGroupName = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.Owner = params.get("Owner")
        self.OwnerId = params.get("OwnerId")
        self.ProjectId = params.get("ProjectId")
        self.ProjectIdent = params.get("ProjectIdent")
        self.ProjectName = params.get("ProjectName")
        self.WorkflowDesc = params.get("WorkflowDesc")
        self.WorkflowName = params.get("WorkflowName")
        self.FolderId = params.get("FolderId")
        self.UserGroupId = params.get("UserGroupId")
        self.UserGroupName = params.get("UserGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        