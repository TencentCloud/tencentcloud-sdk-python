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
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Value = None
        self.Properties = None


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
        