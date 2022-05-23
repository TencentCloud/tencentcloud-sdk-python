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


class CreateTaskFromTemplateRequest(AbstractModel):
    """CreateTaskFromTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 从经验库中查询到的经验模版ID
        :type TemplateId: int
        :param TaskConfig: 演练的配置参数
        :type TaskConfig: :class:`tencentcloud.cfg.v20210820.models.TaskConfig`
        """
        self.TemplateId = None
        self.TaskConfig = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("TaskConfig") is not None:
            self.TaskConfig = TaskConfig()
            self.TaskConfig._deserialize(params.get("TaskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromTemplateResponse(AbstractModel):
    """CreateTaskFromTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 创建成功的演练ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribePolicy(AbstractModel):
    """查询-保护策略

    """

    def __init__(self):
        r"""
        :param TaskPolicyIdList: 保护策略ID列表
        :type TaskPolicyIdList: list of str
        :param TaskPolicyStatus: 保护策略状态
        :type TaskPolicyStatus: str
        :param TaskPolicyRule: 策略规则
        :type TaskPolicyRule: str
        :param TaskPolicyDealType: 护栏策略生效处理策略 1:顺序执行，2:暂停
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPolicyDealType: int
        """
        self.TaskPolicyIdList = None
        self.TaskPolicyStatus = None
        self.TaskPolicyRule = None
        self.TaskPolicyDealType = None


    def _deserialize(self, params):
        self.TaskPolicyIdList = params.get("TaskPolicyIdList")
        self.TaskPolicyStatus = params.get("TaskPolicyStatus")
        self.TaskPolicyRule = params.get("TaskPolicyRule")
        self.TaskPolicyDealType = params.get("TaskPolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsRequest(AbstractModel):
    """DescribeTaskExecuteLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param Limit: 返回的内容行数
        :type Limit: int
        :param Offset: 日志起始的行数。
        :type Offset: int
        """
        self.TaskId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsResponse(AbstractModel):
    """DescribeTaskExecuteLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogMessage: 日志数据
        :type LogMessage: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogMessage = params.get("LogMessage")
        self.RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: 分页Offset
        :type Offset: int
        :param TaskTitle: 演练名称
        :type TaskTitle: str
        :param TaskTag: 标签键
        :type TaskTag: list of str
        :param TaskStatus: 状态
        :type TaskStatus: int
        :param TaskStartTime: 开始时间，固定格式%Y-%m-%d %H:%M:%S
        :type TaskStartTime: str
        :param TaskEndTime: 结束时间，固定格式%Y-%m-%d %H:%M:%S
        :type TaskEndTime: str
        :param Tags: 标签对
        :type Tags: list of TagWithDescribe
        """
        self.Limit = None
        self.Offset = None
        self.TaskTitle = None
        self.TaskTag = None
        self.TaskStatus = None
        self.TaskStartTime = None
        self.TaskEndTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.TaskTitle = params.get("TaskTitle")
        self.TaskTag = params.get("TaskTag")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskStartTime = params.get("TaskStartTime")
        self.TaskEndTime = params.get("TaskEndTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskList: 无
        :type TaskList: list of TaskListItem
        :param Total: 列表数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = TaskListItem()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Task: 任务信息
        :type Task: :class:`tencentcloud.cfg.v20210820.models.Task`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class DescribeTemplateListRequest(AbstractModel):
    """DescribeTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页Limit, 最大值100
        :type Limit: int
        :param Offset: 分页Offset
        :type Offset: int
        :param Title: 演练名称
        :type Title: str
        :param Tag: 标签键
        :type Tag: list of str
        :param IsUsed: 状态，1---使用中， 2---停用
        :type IsUsed: int
        :param Tags: 标签对
        :type Tags: list of TagWithDescribe
        """
        self.Limit = None
        self.Offset = None
        self.Title = None
        self.Tag = None
        self.IsUsed = None
        self.Tags = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Title = params.get("Title")
        self.Tag = params.get("Tag")
        self.IsUsed = params.get("IsUsed")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateListResponse(AbstractModel):
    """DescribeTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateList: 经验库列表
        :type TemplateList: list of TemplateListItem
        :param Total: 列表数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateList") is not None:
            self.TemplateList = []
            for item in params.get("TemplateList"):
                obj = TemplateListItem()
                obj._deserialize(item)
                self.TemplateList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTemplateRequest(AbstractModel):
    """DescribeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 经验库ID
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateResponse(AbstractModel):
    """DescribeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Template: 经验库详情
        :type Template: :class:`tencentcloud.cfg.v20210820.models.Template`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class ExecuteTaskInstanceRequest(AbstractModel):
    """ExecuteTaskInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param TaskActionId: 任务动作ID
        :type TaskActionId: int
        :param TaskInstanceIds: 任务动作实例ID
        :type TaskInstanceIds: list of int non-negative
        :param IsOperateAll: 是否操作整个任务
        :type IsOperateAll: bool
        :param ActionType: 操作类型：（1--启动   2--执行  3--跳过   5--重试）
        :type ActionType: int
        :param TaskGroupId: 动作组ID
        :type TaskGroupId: int
        """
        self.TaskId = None
        self.TaskActionId = None
        self.TaskInstanceIds = None
        self.IsOperateAll = None
        self.ActionType = None
        self.TaskGroupId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskActionId = params.get("TaskActionId")
        self.TaskInstanceIds = params.get("TaskInstanceIds")
        self.IsOperateAll = params.get("IsOperateAll")
        self.ActionType = params.get("ActionType")
        self.TaskGroupId = params.get("TaskGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskInstanceResponse(AbstractModel):
    """ExecuteTaskInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExecuteTaskRequest(AbstractModel):
    """ExecuteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 需要执行的任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskResponse(AbstractModel):
    """ExecuteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskRunStatusRequest(AbstractModel):
    """ModifyTaskRunStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param Status: 任务状态, 1001--未开始 1002--进行中（执行）1003--进行中（暂停）1004--执行结束
        :type Status: int
        :param IsExpect: 执行结果是否符合预期（当前扭转状态为执行结束时，需要必传此字段）
        :type IsExpect: bool
        :param Summary: 演习结论（当演习状态转变为执行结束时，需要填写此字段）
        :type Summary: str
        """
        self.TaskId = None
        self.Status = None
        self.IsExpect = None
        self.Summary = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.IsExpect = params.get("IsExpect")
        self.Summary = params.get("Summary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskRunStatusResponse(AbstractModel):
    """ModifyTaskRunStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TagWithCreate(AbstractModel):
    """用于传入创建、编辑标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagWithDescribe(AbstractModel):
    """展示标签列表

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param TaskTitle: 任务标题
        :type TaskTitle: str
        :param TaskDescription: 任务描述
        :type TaskDescription: str
        :param TaskTag: 自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTag: str
        :param TaskStatus: 任务状态，1001--未开始  1002--进行中（执行）1003--进行中（暂停）1004--执行结束
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: int
        :param TaskStatusType: 任务结束状态，表明任务以何种状态结束: 0 -- 尚未结束，1 -- 成功，2-- 失败，3--终止
        :type TaskStatusType: int
        :param TaskProtectStrategy: 保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProtectStrategy: str
        :param TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param TaskUpdateTime: 任务更新时间
        :type TaskUpdateTime: str
        :param TaskGroups: 任务动作组
        :type TaskGroups: list of TaskGroup
        :param TaskStartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStartTime: str
        :param TaskEndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskEndTime: str
        :param TaskExpect: 是否符合预期。1：符合预期，2：不符合预期
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskExpect: int
        :param TaskSummary: 演习记录
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSummary: str
        :param TaskMode: 任务模式。1:手工执行，2:自动执行
        :type TaskMode: int
        :param TaskPauseDuration: 自动暂停时长。单位分钟
        :type TaskPauseDuration: int
        :param TaskOwnerUin: 演练创建者Uin
        :type TaskOwnerUin: str
        :param TaskRegionId: 地域ID
        :type TaskRegionId: int
        :param TaskMonitors: 监控指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMonitors: list of TaskMonitor
        :param TaskPolicy: 保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPolicy: :class:`tencentcloud.cfg.v20210820.models.DescribePolicy`
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagWithDescribe
        """
        self.TaskId = None
        self.TaskTitle = None
        self.TaskDescription = None
        self.TaskTag = None
        self.TaskStatus = None
        self.TaskStatusType = None
        self.TaskProtectStrategy = None
        self.TaskCreateTime = None
        self.TaskUpdateTime = None
        self.TaskGroups = None
        self.TaskStartTime = None
        self.TaskEndTime = None
        self.TaskExpect = None
        self.TaskSummary = None
        self.TaskMode = None
        self.TaskPauseDuration = None
        self.TaskOwnerUin = None
        self.TaskRegionId = None
        self.TaskMonitors = None
        self.TaskPolicy = None
        self.Tags = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskTitle = params.get("TaskTitle")
        self.TaskDescription = params.get("TaskDescription")
        self.TaskTag = params.get("TaskTag")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskStatusType = params.get("TaskStatusType")
        self.TaskProtectStrategy = params.get("TaskProtectStrategy")
        self.TaskCreateTime = params.get("TaskCreateTime")
        self.TaskUpdateTime = params.get("TaskUpdateTime")
        if params.get("TaskGroups") is not None:
            self.TaskGroups = []
            for item in params.get("TaskGroups"):
                obj = TaskGroup()
                obj._deserialize(item)
                self.TaskGroups.append(obj)
        self.TaskStartTime = params.get("TaskStartTime")
        self.TaskEndTime = params.get("TaskEndTime")
        self.TaskExpect = params.get("TaskExpect")
        self.TaskSummary = params.get("TaskSummary")
        self.TaskMode = params.get("TaskMode")
        self.TaskPauseDuration = params.get("TaskPauseDuration")
        self.TaskOwnerUin = params.get("TaskOwnerUin")
        self.TaskRegionId = params.get("TaskRegionId")
        if params.get("TaskMonitors") is not None:
            self.TaskMonitors = []
            for item in params.get("TaskMonitors"):
                obj = TaskMonitor()
                obj._deserialize(item)
                self.TaskMonitors.append(obj)
        if params.get("TaskPolicy") is not None:
            self.TaskPolicy = DescribePolicy()
            self.TaskPolicy._deserialize(params.get("TaskPolicy"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskConfig(AbstractModel):
    """从经验模版创建演练时需要配置的任务参数

    """

    def __init__(self):
        r"""
        :param TaskGroupsConfig: 动作组配置，需要保证配置个数和经验中的动作组个数一致
        :type TaskGroupsConfig: list of TaskGroupConfig
        :param TaskTitle: 更改后的演练名称，不填则默认取经验名称
        :type TaskTitle: str
        :param TaskDescription: 更改后的演练描述，不填则默认取经验描述
        :type TaskDescription: str
        :param TaskMode: 演练执行模式：1----手工执行/ 2 ---自动执行，不填则默认取经验执行模式
        :type TaskMode: int
        :param TaskPauseDuration: 演练自动暂停时间，单位分钟, 不填则默认取经验自动暂停时间
        :type TaskPauseDuration: int
        :param Tags: 演练标签信息，不填则默认取经验标签
        :type Tags: list of TagWithCreate
        """
        self.TaskGroupsConfig = None
        self.TaskTitle = None
        self.TaskDescription = None
        self.TaskMode = None
        self.TaskPauseDuration = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("TaskGroupsConfig") is not None:
            self.TaskGroupsConfig = []
            for item in params.get("TaskGroupsConfig"):
                obj = TaskGroupConfig()
                obj._deserialize(item)
                self.TaskGroupsConfig.append(obj)
        self.TaskTitle = params.get("TaskTitle")
        self.TaskDescription = params.get("TaskDescription")
        self.TaskMode = params.get("TaskMode")
        self.TaskPauseDuration = params.get("TaskPauseDuration")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithCreate()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroup(AbstractModel):
    """任务分组

    """

    def __init__(self):
        r"""
        :param TaskGroupId: 任务动作ID
        :type TaskGroupId: int
        :param TaskGroupTitle: 分组标题
        :type TaskGroupTitle: str
        :param TaskGroupDescription: 分组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupDescription: str
        :param TaskGroupOrder: 任务分组顺序
        :type TaskGroupOrder: int
        :param ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        :param TaskGroupCreateTime: 任务分组创建时间
        :type TaskGroupCreateTime: str
        :param TaskGroupUpdateTime: 任务分组更新时间
        :type TaskGroupUpdateTime: str
        :param TaskGroupActions: 动作分组动作列表
        :type TaskGroupActions: list of TaskGroupAction
        :param TaskGroupInstanceList: 实例列表
        :type TaskGroupInstanceList: list of str
        :param TaskGroupMode: 执行模式。1 --- 顺序执行，2 --- 阶段执行
        :type TaskGroupMode: int
        """
        self.TaskGroupId = None
        self.TaskGroupTitle = None
        self.TaskGroupDescription = None
        self.TaskGroupOrder = None
        self.ObjectTypeId = None
        self.TaskGroupCreateTime = None
        self.TaskGroupUpdateTime = None
        self.TaskGroupActions = None
        self.TaskGroupInstanceList = None
        self.TaskGroupMode = None


    def _deserialize(self, params):
        self.TaskGroupId = params.get("TaskGroupId")
        self.TaskGroupTitle = params.get("TaskGroupTitle")
        self.TaskGroupDescription = params.get("TaskGroupDescription")
        self.TaskGroupOrder = params.get("TaskGroupOrder")
        self.ObjectTypeId = params.get("ObjectTypeId")
        self.TaskGroupCreateTime = params.get("TaskGroupCreateTime")
        self.TaskGroupUpdateTime = params.get("TaskGroupUpdateTime")
        if params.get("TaskGroupActions") is not None:
            self.TaskGroupActions = []
            for item in params.get("TaskGroupActions"):
                obj = TaskGroupAction()
                obj._deserialize(item)
                self.TaskGroupActions.append(obj)
        self.TaskGroupInstanceList = params.get("TaskGroupInstanceList")
        self.TaskGroupMode = params.get("TaskGroupMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupAction(AbstractModel):
    """任务分组动作

    """

    def __init__(self):
        r"""
        :param TaskGroupActionId: 任务分组动作ID
        :type TaskGroupActionId: int
        :param TaskGroupInstances: 任务分组动作实例列表
        :type TaskGroupInstances: list of TaskGroupInstance
        :param ActionId: 动作ID
        :type ActionId: int
        :param TaskGroupActionOrder: 分组动作顺序
        :type TaskGroupActionOrder: int
        :param TaskGroupActionGeneralConfiguration: 分组动作通用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupActionGeneralConfiguration: str
        :param TaskGroupActionCustomConfiguration: 分组动作自定义配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupActionCustomConfiguration: str
        :param TaskGroupActionStatus: 分组动作状态
        :type TaskGroupActionStatus: int
        :param TaskGroupActionCreateTime: 动作分组创建时间
        :type TaskGroupActionCreateTime: str
        :param TaskGroupActionUpdateTime: 动作分组更新时间
        :type TaskGroupActionUpdateTime: str
        :param ActionTitle: 动作名称
        :type ActionTitle: str
        :param TaskGroupActionStatusType: 状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :type TaskGroupActionStatusType: int
        :param TaskGroupActionRandomId: RandomId
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupActionRandomId: int
        :param TaskGroupActionRecoverId: RecoverId
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupActionRecoverId: int
        :param TaskGroupActionExecuteId: ExecuteId
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupActionExecuteId: int
        :param ActionApiType: 调用api类型，0:tat, 1:云api
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionApiType: int
        :param ActionAttribute: 1:故障，2:恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionAttribute: int
        :param ActionType: 动作类型：平台、自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        """
        self.TaskGroupActionId = None
        self.TaskGroupInstances = None
        self.ActionId = None
        self.TaskGroupActionOrder = None
        self.TaskGroupActionGeneralConfiguration = None
        self.TaskGroupActionCustomConfiguration = None
        self.TaskGroupActionStatus = None
        self.TaskGroupActionCreateTime = None
        self.TaskGroupActionUpdateTime = None
        self.ActionTitle = None
        self.TaskGroupActionStatusType = None
        self.TaskGroupActionRandomId = None
        self.TaskGroupActionRecoverId = None
        self.TaskGroupActionExecuteId = None
        self.ActionApiType = None
        self.ActionAttribute = None
        self.ActionType = None


    def _deserialize(self, params):
        self.TaskGroupActionId = params.get("TaskGroupActionId")
        if params.get("TaskGroupInstances") is not None:
            self.TaskGroupInstances = []
            for item in params.get("TaskGroupInstances"):
                obj = TaskGroupInstance()
                obj._deserialize(item)
                self.TaskGroupInstances.append(obj)
        self.ActionId = params.get("ActionId")
        self.TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self.TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self.TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        self.TaskGroupActionStatus = params.get("TaskGroupActionStatus")
        self.TaskGroupActionCreateTime = params.get("TaskGroupActionCreateTime")
        self.TaskGroupActionUpdateTime = params.get("TaskGroupActionUpdateTime")
        self.ActionTitle = params.get("ActionTitle")
        self.TaskGroupActionStatusType = params.get("TaskGroupActionStatusType")
        self.TaskGroupActionRandomId = params.get("TaskGroupActionRandomId")
        self.TaskGroupActionRecoverId = params.get("TaskGroupActionRecoverId")
        self.TaskGroupActionExecuteId = params.get("TaskGroupActionExecuteId")
        self.ActionApiType = params.get("ActionApiType")
        self.ActionAttribute = params.get("ActionAttribute")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupActionConfig(AbstractModel):
    """动作组中的动作参数

    """

    def __init__(self):
        r"""
        :param TaskGroupActionOrder: 该动作在动作组中的顺序，从1开始，不填或填错将匹配不到经验中要修改参数的动作
        :type TaskGroupActionOrder: int
        :param TaskGroupActionGeneralConfiguration: 动作通用参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :type TaskGroupActionGeneralConfiguration: str
        :param TaskGroupActionCustomConfiguration: 动作自定义参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :type TaskGroupActionCustomConfiguration: str
        """
        self.TaskGroupActionOrder = None
        self.TaskGroupActionGeneralConfiguration = None
        self.TaskGroupActionCustomConfiguration = None


    def _deserialize(self, params):
        self.TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self.TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self.TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupConfig(AbstractModel):
    """动作组的配置项

    """

    def __init__(self):
        r"""
        :param TaskGroupInstances: 动作组所关联的实例对象
        :type TaskGroupInstances: list of str
        :param TaskGroupTitle: 动作组标题，不填默认取经验中的动作组名称
        :type TaskGroupTitle: str
        :param TaskGroupDescription: 动作组描述，不填默认取经验中的动作组描述
        :type TaskGroupDescription: str
        :param TaskGroupMode: 动作执行模式。1 --- 顺序执行，2 --- 阶段执行, 不填默认取经验中的动作组执行模式
        :type TaskGroupMode: int
        :param TaskGroupActionsConfig: 动作组中的动作参数，不填默认使用经验中的动作参数，配置时可以只指定想要修改参数的动作
        :type TaskGroupActionsConfig: list of TaskGroupActionConfig
        """
        self.TaskGroupInstances = None
        self.TaskGroupTitle = None
        self.TaskGroupDescription = None
        self.TaskGroupMode = None
        self.TaskGroupActionsConfig = None


    def _deserialize(self, params):
        self.TaskGroupInstances = params.get("TaskGroupInstances")
        self.TaskGroupTitle = params.get("TaskGroupTitle")
        self.TaskGroupDescription = params.get("TaskGroupDescription")
        self.TaskGroupMode = params.get("TaskGroupMode")
        if params.get("TaskGroupActionsConfig") is not None:
            self.TaskGroupActionsConfig = []
            for item in params.get("TaskGroupActionsConfig"):
                obj = TaskGroupActionConfig()
                obj._deserialize(item)
                self.TaskGroupActionsConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupInstance(AbstractModel):
    """任务分组动作实例

    """

    def __init__(self):
        r"""
        :param TaskGroupInstanceId: 实例ID
        :type TaskGroupInstanceId: int
        :param TaskGroupInstanceObjectId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupInstanceObjectId: str
        :param TaskGroupInstanceStatus: 实例动作执行状态
        :type TaskGroupInstanceStatus: int
        :param TaskGroupInstanceExecuteLog: 实例动作执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupInstanceExecuteLog: str
        :param TaskGroupInstanceCreateTime: 实例创建时间
        :type TaskGroupInstanceCreateTime: str
        :param TaskGroupInstanceUpdateTime: 实例更新时间
        :type TaskGroupInstanceUpdateTime: str
        :param TaskGroupInstanceStatusType: 状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :type TaskGroupInstanceStatusType: int
        :param TaskGroupInstanceStartTime: 执行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupInstanceStartTime: str
        :param TaskGroupInstanceEndTime: 执行结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupInstanceEndTime: str
        """
        self.TaskGroupInstanceId = None
        self.TaskGroupInstanceObjectId = None
        self.TaskGroupInstanceStatus = None
        self.TaskGroupInstanceExecuteLog = None
        self.TaskGroupInstanceCreateTime = None
        self.TaskGroupInstanceUpdateTime = None
        self.TaskGroupInstanceStatusType = None
        self.TaskGroupInstanceStartTime = None
        self.TaskGroupInstanceEndTime = None


    def _deserialize(self, params):
        self.TaskGroupInstanceId = params.get("TaskGroupInstanceId")
        self.TaskGroupInstanceObjectId = params.get("TaskGroupInstanceObjectId")
        self.TaskGroupInstanceStatus = params.get("TaskGroupInstanceStatus")
        self.TaskGroupInstanceExecuteLog = params.get("TaskGroupInstanceExecuteLog")
        self.TaskGroupInstanceCreateTime = params.get("TaskGroupInstanceCreateTime")
        self.TaskGroupInstanceUpdateTime = params.get("TaskGroupInstanceUpdateTime")
        self.TaskGroupInstanceStatusType = params.get("TaskGroupInstanceStatusType")
        self.TaskGroupInstanceStartTime = params.get("TaskGroupInstanceStartTime")
        self.TaskGroupInstanceEndTime = params.get("TaskGroupInstanceEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskListItem(AbstractModel):
    """任务列表信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param TaskTitle: 任务标题
        :type TaskTitle: str
        :param TaskDescription: 任务描述
        :type TaskDescription: str
        :param TaskTag: 任务标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTag: str
        :param TaskStatus: 任务状态(1001 -- 未开始   1002 -- 进行中  1003 -- 暂停中   1004 -- 任务结束)
        :type TaskStatus: int
        :param TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param TaskUpdateTime: 任务更新时间
        :type TaskUpdateTime: str
        """
        self.TaskId = None
        self.TaskTitle = None
        self.TaskDescription = None
        self.TaskTag = None
        self.TaskStatus = None
        self.TaskCreateTime = None
        self.TaskUpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskTitle = params.get("TaskTitle")
        self.TaskDescription = params.get("TaskDescription")
        self.TaskTag = params.get("TaskTag")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskCreateTime = params.get("TaskCreateTime")
        self.TaskUpdateTime = params.get("TaskUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMonitor(AbstractModel):
    """监控指标

    """

    def __init__(self):
        r"""
        :param TaskMonitorId: 监控指标ID
        :type TaskMonitorId: int
        :param TaskMonitorObjectTypeId: 监控指标对象类型ID
        :type TaskMonitorObjectTypeId: int
        :param MetricName: 指标名称
        :type MetricName: str
        :param InstancesIds: 实例ID列表
        :type InstancesIds: list of str
        :param MetricChineseName: 中文指标
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricChineseName: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
        self.TaskMonitorId = None
        self.TaskMonitorObjectTypeId = None
        self.MetricName = None
        self.InstancesIds = None
        self.MetricChineseName = None
        self.Unit = None


    def _deserialize(self, params):
        self.TaskMonitorId = params.get("TaskMonitorId")
        self.TaskMonitorObjectTypeId = params.get("TaskMonitorObjectTypeId")
        self.MetricName = params.get("MetricName")
        self.InstancesIds = params.get("InstancesIds")
        self.MetricChineseName = params.get("MetricChineseName")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """经验库

    """

    def __init__(self):
        r"""
        :param TemplateId: 经验库ID
        :type TemplateId: int
        :param TemplateTitle: 经验库标题
        :type TemplateTitle: str
        :param TemplateDescription: 经验库描述
        :type TemplateDescription: str
        :param TemplateTag: 自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateTag: str
        :param TemplateIsUsed: 使用状态。1 ---- 使用中，2 --- 停用
        :type TemplateIsUsed: int
        :param TemplateCreateTime: 经验库创建时间
        :type TemplateCreateTime: str
        :param TemplateUpdateTime: 经验库更新时间
        :type TemplateUpdateTime: str
        :param TemplateMode: 经验库模式。1:手工执行，2:自动执行
        :type TemplateMode: int
        :param TemplatePauseDuration: 自动暂停时长。单位分钟
        :type TemplatePauseDuration: int
        :param TemplateOwnerUin: 演练创建者Uin
        :type TemplateOwnerUin: str
        :param TemplateRegionId: 地域ID
        :type TemplateRegionId: int
        :param TemplateGroups: 动作组
        :type TemplateGroups: list of TemplateGroup
        :param TemplateMonitors: 监控指标
        :type TemplateMonitors: list of TemplateMonitor
        :param TemplatePolicy: 护栏监控
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplatePolicy: :class:`tencentcloud.cfg.v20210820.models.TemplatePolicy`
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagWithDescribe
        """
        self.TemplateId = None
        self.TemplateTitle = None
        self.TemplateDescription = None
        self.TemplateTag = None
        self.TemplateIsUsed = None
        self.TemplateCreateTime = None
        self.TemplateUpdateTime = None
        self.TemplateMode = None
        self.TemplatePauseDuration = None
        self.TemplateOwnerUin = None
        self.TemplateRegionId = None
        self.TemplateGroups = None
        self.TemplateMonitors = None
        self.TemplatePolicy = None
        self.Tags = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateTitle = params.get("TemplateTitle")
        self.TemplateDescription = params.get("TemplateDescription")
        self.TemplateTag = params.get("TemplateTag")
        self.TemplateIsUsed = params.get("TemplateIsUsed")
        self.TemplateCreateTime = params.get("TemplateCreateTime")
        self.TemplateUpdateTime = params.get("TemplateUpdateTime")
        self.TemplateMode = params.get("TemplateMode")
        self.TemplatePauseDuration = params.get("TemplatePauseDuration")
        self.TemplateOwnerUin = params.get("TemplateOwnerUin")
        self.TemplateRegionId = params.get("TemplateRegionId")
        if params.get("TemplateGroups") is not None:
            self.TemplateGroups = []
            for item in params.get("TemplateGroups"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self.TemplateGroups.append(obj)
        if params.get("TemplateMonitors") is not None:
            self.TemplateMonitors = []
            for item in params.get("TemplateMonitors"):
                obj = TemplateMonitor()
                obj._deserialize(item)
                self.TemplateMonitors.append(obj)
        if params.get("TemplatePolicy") is not None:
            self.TemplatePolicy = TemplatePolicy()
            self.TemplatePolicy._deserialize(params.get("TemplatePolicy"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """任务分组

    """

    def __init__(self):
        r"""
        :param TemplateGroupId: 经验库动作ID
        :type TemplateGroupId: int
        :param TemplateGroupActions: 经验库动作分组动作列表
        :type TemplateGroupActions: list of TemplateGroupAction
        :param Title: 分组标题
        :type Title: str
        :param Description: 分组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Order: 分组顺序
        :type Order: int
        :param Mode: 执行模式。1 --- 顺序执行，2 --- 阶段执行
        :type Mode: int
        :param ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        :param CreateTime: 分组创建时间
        :type CreateTime: str
        :param UpdateTime: 分组更新时间
        :type UpdateTime: str
        """
        self.TemplateGroupId = None
        self.TemplateGroupActions = None
        self.Title = None
        self.Description = None
        self.Order = None
        self.Mode = None
        self.ObjectTypeId = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TemplateGroupId = params.get("TemplateGroupId")
        if params.get("TemplateGroupActions") is not None:
            self.TemplateGroupActions = []
            for item in params.get("TemplateGroupActions"):
                obj = TemplateGroupAction()
                obj._deserialize(item)
                self.TemplateGroupActions.append(obj)
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.Order = params.get("Order")
        self.Mode = params.get("Mode")
        self.ObjectTypeId = params.get("ObjectTypeId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroupAction(AbstractModel):
    """任务分组动作

    """

    def __init__(self):
        r"""
        :param TemplateGroupActionId: 经验库分组动作ID
        :type TemplateGroupActionId: int
        :param ActionId: 动作ID
        :type ActionId: int
        :param Order: 分组动作顺序
        :type Order: int
        :param GeneralConfiguration: 分组动作通用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneralConfiguration: str
        :param CustomConfiguration: 分组动作自定义配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomConfiguration: str
        :param CreateTime: 动作分组创建时间
        :type CreateTime: str
        :param UpdateTime: 动作分组更新时间
        :type UpdateTime: str
        :param ActionTitle: 动作名称
        :type ActionTitle: str
        :param RandomId: 自身随机id
注意：此字段可能返回 null，表示取不到有效值。
        :type RandomId: int
        :param RecoverId: 恢复动作id
注意：此字段可能返回 null，表示取不到有效值。
        :type RecoverId: int
        :param ExecuteId: 执行动作id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteId: int
        :param ActionApiType: 调用api类型，0:tat, 1:云api
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionApiType: int
        :param ActionAttribute: 1:故障，2:恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionAttribute: int
        :param ActionType: 动作类型：平台和自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        """
        self.TemplateGroupActionId = None
        self.ActionId = None
        self.Order = None
        self.GeneralConfiguration = None
        self.CustomConfiguration = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ActionTitle = None
        self.RandomId = None
        self.RecoverId = None
        self.ExecuteId = None
        self.ActionApiType = None
        self.ActionAttribute = None
        self.ActionType = None


    def _deserialize(self, params):
        self.TemplateGroupActionId = params.get("TemplateGroupActionId")
        self.ActionId = params.get("ActionId")
        self.Order = params.get("Order")
        self.GeneralConfiguration = params.get("GeneralConfiguration")
        self.CustomConfiguration = params.get("CustomConfiguration")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ActionTitle = params.get("ActionTitle")
        self.RandomId = params.get("RandomId")
        self.RecoverId = params.get("RecoverId")
        self.ExecuteId = params.get("ExecuteId")
        self.ActionApiType = params.get("ActionApiType")
        self.ActionAttribute = params.get("ActionAttribute")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateListItem(AbstractModel):
    """经验库列表信息

    """

    def __init__(self):
        r"""
        :param TemplateId: 经验库ID
        :type TemplateId: int
        :param TemplateTitle: 经验库标题
        :type TemplateTitle: str
        :param TemplateDescription: 经验库描述
        :type TemplateDescription: str
        :param TemplateTag: 经验库标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateTag: str
        :param TemplateIsUsed: 经验库状态。1 -- 使用中，2 -- 停用
        :type TemplateIsUsed: int
        :param TemplateCreateTime: 经验库创建时间
        :type TemplateCreateTime: str
        :param TemplateUpdateTime: 经验库更新时间
        :type TemplateUpdateTime: str
        :param TemplateUsedNum: 经验库关联的任务数量
        :type TemplateUsedNum: int
        """
        self.TemplateId = None
        self.TemplateTitle = None
        self.TemplateDescription = None
        self.TemplateTag = None
        self.TemplateIsUsed = None
        self.TemplateCreateTime = None
        self.TemplateUpdateTime = None
        self.TemplateUsedNum = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateTitle = params.get("TemplateTitle")
        self.TemplateDescription = params.get("TemplateDescription")
        self.TemplateTag = params.get("TemplateTag")
        self.TemplateIsUsed = params.get("TemplateIsUsed")
        self.TemplateCreateTime = params.get("TemplateCreateTime")
        self.TemplateUpdateTime = params.get("TemplateUpdateTime")
        self.TemplateUsedNum = params.get("TemplateUsedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateMonitor(AbstractModel):
    """监控指标

    """

    def __init__(self):
        r"""
        :param MonitorId: 监控指标ID
        :type MonitorId: int
        :param ObjectTypeId: 监控指标对象类型ID
        :type ObjectTypeId: int
        :param MetricName: 指标名称
        :type MetricName: str
        :param MetricChineseName: 中文指标
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricChineseName: str
        """
        self.MonitorId = None
        self.ObjectTypeId = None
        self.MetricName = None
        self.MetricChineseName = None


    def _deserialize(self, params):
        self.MonitorId = params.get("MonitorId")
        self.ObjectTypeId = params.get("ObjectTypeId")
        self.MetricName = params.get("MetricName")
        self.MetricChineseName = params.get("MetricChineseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatePolicy(AbstractModel):
    """保护策略

    """

    def __init__(self):
        r"""
        :param TemplatePolicyIdList: 保护策略ID列表
        :type TemplatePolicyIdList: list of str
        :param TemplatePolicyRule: 策略规则
        :type TemplatePolicyRule: str
        :param TemplatePolicyDealType: 护栏策略生效处理策略 1:顺序执行，2:暂停
        :type TemplatePolicyDealType: int
        """
        self.TemplatePolicyIdList = None
        self.TemplatePolicyRule = None
        self.TemplatePolicyDealType = None


    def _deserialize(self, params):
        self.TemplatePolicyIdList = params.get("TemplatePolicyIdList")
        self.TemplatePolicyRule = params.get("TemplatePolicyRule")
        self.TemplatePolicyDealType = params.get("TemplatePolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        