# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class DescribeRepairTaskConstantRequest(AbstractModel):
    """DescribeRepairTaskConstant请求参数结构体

    """


class DescribeRepairTaskConstantResponse(AbstractModel):
    """DescribeRepairTaskConstant返回参数结构体

    """

    def __init__(self):
        """
        :param TaskTypeList: 故障类型ID与对应中文名列表
        :type TaskTypeList: list of TaskType
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTypeList") is not None:
            self.TaskTypeList = []
            for item in params.get("TaskTypeList"):
                obj = TaskType()
                obj._deserialize(item)
                self.TaskTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 开始位置
        :type Offset: int
        :param Limit: 数据条数
        :type Limit: int
        :param StartDate: 时间过滤下限
        :type StartDate: str
        :param EndDate: 时间过滤上限
        :type EndDate: str
        :param TaskStatus: 任务状态ID过滤
        :type TaskStatus: list of int non-negative
        :param OrderField: 排序字段，目前支持：CreateTime，AuthTime，EndTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        :param TaskIds: 任务ID过滤
        :type TaskIds: list of str
        :param InstanceIds: 实例ID过滤
        :type InstanceIds: list of str
        :param Aliases: 实例别名过滤
        :type Aliases: list of str
        :param TaskTypeIds: 故障类型ID过滤
        :type TaskTypeIds: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.StartDate = None
        self.EndDate = None
        self.TaskStatus = None
        self.OrderField = None
        self.Order = None
        self.TaskIds = None
        self.InstanceIds = None
        self.Aliases = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.TaskStatus = params.get("TaskStatus")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.TaskIds = params.get("TaskIds")
        self.InstanceIds = params.get("InstanceIds")
        self.Aliases = params.get("Aliases")
        self.TaskTypeIds = params.get("TaskTypeIds")


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回任务总数量
        :type TotalCount: int
        :param TaskInfoSet: 任务信息列表
        :type TaskInfoSet: list of TaskInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self.TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.TaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskOperationLogRequest(AbstractModel):
    """DescribeTaskOperationLog请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 维修任务ID
        :type TaskId: str
        :param OrderField: 排序字段，目前支持：OperationTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self.TaskId = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeTaskOperationLogResponse(AbstractModel):
    """DescribeTaskOperationLog返回参数结构体

    """

    def __init__(self):
        """
        :param TaskOperationLogSet: 操作日志
        :type TaskOperationLogSet: list of TaskOperationLog
        :param TotalCount: 日志条数
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskOperationLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskOperationLogSet") is not None:
            self.TaskOperationLogSet = []
            for item in params.get("TaskOperationLogSet"):
                obj = TaskOperationLog()
                obj._deserialize(item)
                self.TaskOperationLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class RepairTaskControlRequest(AbstractModel):
    """RepairTaskControl请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 维修任务ID
        :type TaskId: str
        :param Operate: 操作
        :type Operate: str
        """
        self.TaskId = None
        self.Operate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operate = params.get("Operate")


class RepairTaskControlResponse(AbstractModel):
    """RepairTaskControl返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 出参TaskId是黑石异步任务ID，不同于入参TaskId字段。
此字段可作为DescriptionOperationResult查询异步任务状态接口的入参，查询异步任务执行结果。
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class TaskInfo(AbstractModel):
    """维护平台维修任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务id
        :type TaskId: str
        :param InstanceId: 主机id
        :type InstanceId: str
        :param Alias: 主机别名
        :type Alias: str
        :param TaskTypeId: 故障类型id
        :type TaskTypeId: int
        :param TaskStatus: 任务状态id
        :type TaskStatus: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param AuthTime: 授权时间
        :type AuthTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskDetail: 任务详情
        :type TaskDetail: str
        :param DeviceStatus: 设备状态
        :type DeviceStatus: int
        :param OperateStatus: 设备操作状态
        :type OperateStatus: int
        :param Zone: 可用区
        :type Zone: str
        :param Region: 地域
        :type Region: str
        :param VpcId: 所属网络
        :type VpcId: str
        :param SubnetId: 所在子网
        :type SubnetId: str
        :param SubnetName: 子网名
        :type SubnetName: str
        :param VpcName: VPC名
        :type VpcName: str
        :param VpcCidrBlock: VpcCidrBlock
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: SubnetCidrBlock
        :type SubnetCidrBlock: str
        :param WanIp: 公网ip
        :type WanIp: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param MgtIp: 管理IP
        :type MgtIp: str
        """
        self.TaskId = None
        self.InstanceId = None
        self.Alias = None
        self.TaskTypeId = None
        self.TaskStatus = None
        self.CreateTime = None
        self.AuthTime = None
        self.EndTime = None
        self.TaskDetail = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.Zone = None
        self.Region = None
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.WanIp = None
        self.LanIp = None
        self.MgtIp = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.TaskTypeId = params.get("TaskTypeId")
        self.TaskStatus = params.get("TaskStatus")
        self.CreateTime = params.get("CreateTime")
        self.AuthTime = params.get("AuthTime")
        self.EndTime = params.get("EndTime")
        self.TaskDetail = params.get("TaskDetail")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.Zone = params.get("Zone")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.MgtIp = params.get("MgtIp")


class TaskOperationLog(AbstractModel):
    """维修任务操作日志

    """

    def __init__(self):
        """
        :param TaskStep: 操作步骤
        :type TaskStep: str
        :param Operator: 操作人
        :type Operator: str
        :param OperationDetail: 操作描述
        :type OperationDetail: str
        :param OperationTime: 操作时间
        :type OperationTime: str
        """
        self.TaskStep = None
        self.Operator = None
        self.OperationDetail = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.TaskStep = params.get("TaskStep")
        self.Operator = params.get("Operator")
        self.OperationDetail = params.get("OperationDetail")
        self.OperationTime = params.get("OperationTime")


class TaskType(AbstractModel):
    """故障id对应故障名列表

    """

    def __init__(self):
        """
        :param TypeId: 故障类ID
        :type TypeId: int
        :param TypeName: 故障类中文名
        :type TypeName: str
        :param TaskSubType: 故障类型父类
        :type TaskSubType: str
        """
        self.TypeId = None
        self.TypeName = None
        self.TaskSubType = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.TypeName = params.get("TypeName")
        self.TaskSubType = params.get("TaskSubType")