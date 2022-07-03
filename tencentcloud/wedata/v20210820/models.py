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
        