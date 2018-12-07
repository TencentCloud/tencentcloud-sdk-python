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


class BindPsaTagRequest(AbstractModel):
    """BindPsaTag请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param TagKey: 需要绑定的标签key
        :type TagKey: str
        :param TagValue: 需要绑定的标签value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class BindPsaTagResponse(AbstractModel):
    """BindPsaTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePsaRegulationRequest(AbstractModel):
    """CreatePsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaName: 规则别名
        :type PsaName: str
        :param TaskTypeIds: 关联的故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        :param RepairLimit: 维修实例上限，默认为5
        :type RepairLimit: int
        :param PsaDescription: 规则备注
        :type PsaDescription: str
        """
        self.PsaName = None
        self.TaskTypeIds = None
        self.RepairLimit = None
        self.PsaDescription = None


    def _deserialize(self, params):
        self.PsaName = params.get("PsaName")
        self.TaskTypeIds = params.get("TaskTypeIds")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")


class CreatePsaRegulationResponse(AbstractModel):
    """CreatePsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 创建的预授权规则ID
        :type PsaId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PsaId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.RequestId = params.get("RequestId")


class CreateSpotDeviceRequest(AbstractModel):
    """CreateSpotDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区名称。如ap-guangzhou-bls-1, 通过DescribeRegions获取
        :type Zone: str
        :param ComputeType: 计算单元类型
        :type ComputeType: str
        :param OsTypeId: 操作系统类型ID
        :type OsTypeId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param GoodsNum: 购买的计算单元个数
        :type GoodsNum: int
        :param SpotStrategy: 出价策略。可取值为SpotWithPriceLimit和SpotAsPriceGo。SpotWithPriceLimit，用户设置价格上限，需要传SpotPriceLimit参数， 如果市场价高于用户的指定价格，则购买不成功;  SpotAsPriceGo 是随市场价的策略。
        :type SpotStrategy: str
        :param SpotPriceLimit: 用户设置的价格。当为SpotWithPriceLimit竞价策略时有效
        :type SpotPriceLimit: float
        :param Passwd: 设置竞价实例密码。可选参数，没有指定会生成随机密码
        :type Passwd: str
        """
        self.Zone = None
        self.ComputeType = None
        self.OsTypeId = None
        self.VpcId = None
        self.SubnetId = None
        self.GoodsNum = None
        self.SpotStrategy = None
        self.SpotPriceLimit = None
        self.Passwd = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ComputeType = params.get("ComputeType")
        self.OsTypeId = params.get("OsTypeId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.GoodsNum = params.get("GoodsNum")
        self.SpotStrategy = params.get("SpotStrategy")
        self.SpotPriceLimit = params.get("SpotPriceLimit")
        self.Passwd = params.get("Passwd")


class CreateSpotDeviceResponse(AbstractModel):
    """CreateSpotDevice返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 创建的服务器ID
        :type ResourceIds: list of str
        :param FlowId: 任务ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceIds = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateUserCmdRequest(AbstractModel):
    """CreateUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 用户自定义脚本的名称
        :type Alias: str
        :param OsType: 命令适用的操作系统类型，取值linux或xserver
        :type OsType: str
        :param Content: 脚本内容，必须经过base64编码
        :type Content: str
        """
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")


class CreateUserCmdResponse(AbstractModel):
    """CreateUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 脚本ID
        :type CmdId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CmdId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.RequestId = params.get("RequestId")


class DeletePsaRegulationRequest(AbstractModel):
    """DeletePsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        """
        self.PsaId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")


class DeletePsaRegulationResponse(AbstractModel):
    """DeletePsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserCmdsRequest(AbstractModel):
    """DeleteUserCmds请求参数结构体

    """

    def __init__(self):
        """
        :param CmdIds: 需要删除的脚本ID
        :type CmdIds: list of str
        """
        self.CmdIds = None


    def _deserialize(self, params):
        self.CmdIds = params.get("CmdIds")


class DeleteUserCmdsResponse(AbstractModel):
    """DeleteUserCmds返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDevicePriceInfoRequest(AbstractModel):
    """DescribeDevicePriceInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要查询的实例列表
        :type InstanceIds: list of str
        :param TimeUnit: 购买时长单位，当前只支持取值为m
        :type TimeUnit: str
        :param TimeSpan: 购买时长
        :type TimeSpan: int
        """
        self.InstanceIds = None
        self.TimeUnit = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")


class DescribeDevicePriceInfoResponse(AbstractModel):
    """DescribeDevicePriceInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DevicePriceInfoSet: 服务器价格信息列表
        :type DevicePriceInfoSet: list of DevicePriceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DevicePriceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevicePriceInfoSet") is not None:
            self.DevicePriceInfoSet = []
            for item in params.get("DevicePriceInfoSet"):
                obj = DevicePriceInfo()
                obj._deserialize(item)
                self.DevicePriceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param DeviceClassCode: 机型ID，通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/17602)查询
        :type DeviceClassCode: str
        :param InstanceIds: 设备ID数组
        :type InstanceIds: list of str
        :param WanIps: 外网IP数组
        :type WanIps: list of str
        :param LanIps: 内网IP数组
        :type LanIps: list of str
        :param Alias: 设备名称
        :type Alias: str
        :param VagueIp: 模糊IP查询
        :type VagueIp: str
        :param DeadlineStartTime: 设备到期时间查询的起始时间
        :type DeadlineStartTime: str
        :param DeadlineEndTime: 设备到期时间查询的结束时间
        :type DeadlineEndTime: str
        :param AutoRenewFlag: 自动续费标志 0:不自动续费，1:自动续费
        :type AutoRenewFlag: int
        :param VpcId: 私有网络唯一ID
        :type VpcId: str
        :param SubnetId: 子网唯一ID
        :type SubnetId: str
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param DeviceType: 设备类型，取值有: compute(计算型), standard(标准型), storage(存储型) 等
        :type DeviceType: str
        :param IsLuckyDevice: 竞价实例机器的过滤。如果未指定此参数，则不做过滤。0: 查询非竞价实例的机器; 1: 查询竞价实例的机器。
        :type IsLuckyDevice: int
        :param OrderField: 排序字段
        :type OrderField: str
        :param Order: 排序方式，取值：0:增序(默认)，1:降序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.DeviceClassCode = None
        self.InstanceIds = None
        self.WanIps = None
        self.LanIps = None
        self.Alias = None
        self.VagueIp = None
        self.DeadlineStartTime = None
        self.DeadlineEndTime = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.Tags = None
        self.DeviceType = None
        self.IsLuckyDevice = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.InstanceIds = params.get("InstanceIds")
        self.WanIps = params.get("WanIps")
        self.LanIps = params.get("LanIps")
        self.Alias = params.get("Alias")
        self.VagueIp = params.get("VagueIp")
        self.DeadlineStartTime = params.get("DeadlineStartTime")
        self.DeadlineEndTime = params.get("DeadlineEndTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.IsLuckyDevice = params.get("IsLuckyDevice")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param DeviceInfoSet: 物理机信息列表
        :type DeviceInfoSet: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceInfoSet") is not None:
            self.DeviceInfoSet = []
            for item in params.get("DeviceInfoSet"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.DeviceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePsaRegulationsRequest(AbstractModel):
    """DescribePsaRegulations请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 数量限制
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param PsaIds: 规则ID过滤，支持模糊查询
        :type PsaIds: list of str
        :param PsaNames: 规则别名过滤，支持模糊查询
        :type PsaNames: list of str
        :param Tags: 标签过滤
        :type Tags: list of Tag
        :param OrderField: 排序字段，取值支持：CreateTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self.Limit = None
        self.Offset = None
        self.PsaIds = None
        self.PsaNames = None
        self.Tags = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PsaIds = params.get("PsaIds")
        self.PsaNames = params.get("PsaNames")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribePsaRegulationsResponse(AbstractModel):
    """DescribePsaRegulations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回规则数量
        :type TotalCount: int
        :param PsaRegulations: 返回规则列表
        :type PsaRegulations: list of PsaRegulation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PsaRegulations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PsaRegulations") is not None:
            self.PsaRegulations = []
            for item in params.get("PsaRegulations"):
                obj = PsaRegulation()
                obj._deserialize(item)
                self.PsaRegulations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRepairTaskConstantRequest(AbstractModel):
    """DescribeRepairTaskConstant请求参数结构体

    """


class DescribeRepairTaskConstantResponse(AbstractModel):
    """DescribeRepairTaskConstant返回参数结构体

    """

    def __init__(self):
        """
        :param TaskTypeSet: 故障类型ID与对应中文名列表
        :type TaskTypeSet: list of TaskType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskTypeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTypeSet") is not None:
            self.TaskTypeSet = []
            for item in params.get("TaskTypeSet"):
                obj = TaskType()
                obj._deserialize(item)
                self.TaskTypeSet.append(obj)
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeUserCmdTaskInfoRequest(AbstractModel):
    """DescribeUserCmdTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： RunBeginTime,RunEndTime,Status
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")


class DescribeUserCmdTaskInfoResponse(AbstractModel):
    """DescribeUserCmdTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param UserCmdTaskInfoSet: 自定义脚本任务详细信息列表
        :type UserCmdTaskInfoSet: list of UserCmdTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTaskInfoSet") is not None:
            self.UserCmdTaskInfoSet = []
            for item in params.get("UserCmdTaskInfoSet"):
                obj = UserCmdTaskInfo()
                obj._deserialize(item)
                self.UserCmdTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdTasksRequest(AbstractModel):
    """DescribeUserCmdTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： RunBeginTime,RunEndTime,InstanceCount,SuccessCount,FailureCount
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeUserCmdTasksResponse(AbstractModel):
    """DescribeUserCmdTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 脚本任务信息数量
        :type TotalCount: int
        :param UserCmdTasks: 脚本任务信息列表
        :type UserCmdTasks: list of UserCmdTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTasks") is not None:
            self.UserCmdTasks = []
            for item in params.get("UserCmdTasks"):
                obj = UserCmdTask()
                obj._deserialize(item)
                self.UserCmdTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdsRequest(AbstractModel):
    """DescribeUserCmds请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： OsType,CreateTime,ModifyTime
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        :param CmdId: 查询的脚本ID
        :type CmdId: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None
        self.CmdId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")
        self.CmdId = params.get("CmdId")


class DescribeUserCmdsResponse(AbstractModel):
    """DescribeUserCmds返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param UserCmds: 脚本信息列表
        :type UserCmds: list of UserCmd
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmds") is not None:
            self.UserCmds = []
            for item in params.get("UserCmds"):
                obj = UserCmd()
                obj._deserialize(item)
                self.UserCmds.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceAlias(AbstractModel):
    """设备ID与别名

    """

    def __init__(self):
        """
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param Alias: 设备别名
        :type Alias: str
        """
        self.InstanceId = None
        self.Alias = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")


class DeviceInfo(AbstractModel):
    """物理机信息

    """

    def __init__(self):
        """
        :param InstanceId: 设备唯一ID
        :type InstanceId: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param DeviceStatus: 设备状态ID
        :type DeviceStatus: int
        :param OperateStatus: 设备操作状态
        :type OperateStatus: int
        :param OsTypeId: 操作系统ID
        :type OsTypeId: int
        :param RaidId: RAID类型ID
        :type RaidId: int
        :param Alias: 设备别名
        :type Alias: str
        :param AppId: AppId
        :type AppId: int
        :param Zone: 可用区
        :type Zone: str
        :param WanIp: 外网IP
        :type WanIp: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param DeliverTime: 设备交付时间
        :type DeliverTime: str
        :param Deadline: 设备到期时间
        :type Deadline: str
        :param AutoRenewFlag: 自动续费标识。0: 不自动续费; 1:自动续费
        :type AutoRenewFlag: int
        :param DeviceClassCode: 设备类型
        :type DeviceClassCode: str
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param CpmPayMode: 计费模式。1: 预付费; 2: 后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param DhcpIp: 带外IP
        :type DhcpIp: str
        :param VpcName: 所在私有网络别名
        :type VpcName: str
        :param SubnetName: 所在子网别名
        :type SubnetName: str
        :param VpcCidrBlock: 所在私有网络CIDR
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: 所在子网CIDR
        :type SubnetCidrBlock: str
        :param IsLuckyDevice: 标识是否是竞价实例。0: 普通设备; 1: 竞价实例设备
        :type IsLuckyDevice: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.OsTypeId = None
        self.RaidId = None
        self.Alias = None
        self.AppId = None
        self.Zone = None
        self.WanIp = None
        self.LanIp = None
        self.DeliverTime = None
        self.Deadline = None
        self.AutoRenewFlag = None
        self.DeviceClassCode = None
        self.Tags = None
        self.CpmPayMode = None
        self.DhcpIp = None
        self.VpcName = None
        self.SubnetName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.IsLuckyDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.Zone = params.get("Zone")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.DeliverTime = params.get("DeliverTime")
        self.Deadline = params.get("Deadline")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeviceClassCode = params.get("DeviceClassCode")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CpmPayMode = params.get("CpmPayMode")
        self.DhcpIp = params.get("DhcpIp")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.IsLuckyDevice = params.get("IsLuckyDevice")


class DevicePriceInfo(AbstractModel):
    """服务器价格信息

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param DeviceClassCode: 设备型号
        :type DeviceClassCode: str
        :param IsElastic: 是否是弹性机型，1：是，0：否
        :type IsElastic: int
        :param CpmPayMode: 付费模式ID, 1:预付费; 2:后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param CpuDescription: Cpu信息描述
        :type CpuDescription: str
        :param MemDescription: 内存信息描述
        :type MemDescription: str
        :param DiskDescription: 硬盘信息描述
        :type DiskDescription: str
        :param NicDescription: 网卡信息描述
        :type NicDescription: str
        :param GpuDescription: Gpu信息描述
        :type GpuDescription: str
        :param RaidDescription: Raid信息描述
        :type RaidDescription: str
        :param Price: 客户的单价
        :type Price: int
        :param NormalPrice: 刊例单价
        :type NormalPrice: int
        :param TotalCost: 原价
        :type TotalCost: int
        :param RealTotalCost: 折扣价
        :type RealTotalCost: int
        :param TimeSpan: 计费时长
        :type TimeSpan: int
        :param TimeUnit: 计费时长单位, m:按月计费; d:按天计费
        :type TimeUnit: str
        :param GoodsCount: 商品数量
        :type GoodsCount: int
        """
        self.InstanceId = None
        self.DeviceClassCode = None
        self.IsElastic = None
        self.CpmPayMode = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.NicDescription = None
        self.GpuDescription = None
        self.RaidDescription = None
        self.Price = None
        self.NormalPrice = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.GoodsCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.IsElastic = params.get("IsElastic")
        self.CpmPayMode = params.get("CpmPayMode")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.NicDescription = params.get("NicDescription")
        self.GpuDescription = params.get("GpuDescription")
        self.RaidDescription = params.get("RaidDescription")
        self.Price = params.get("Price")
        self.NormalPrice = params.get("NormalPrice")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.GoodsCount = params.get("GoodsCount")


class FailedTaskInfo(AbstractModel):
    """运行失败的自定义脚本信息

    """

    def __init__(self):
        """
        :param InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param ErrorMsg: 失败原因
        :type ErrorMsg: str
        """
        self.InstanceId = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")


class ModifyDeviceAliasesRequest(AbstractModel):
    """ModifyDeviceAliases请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceAliases: 需要改名的设备与别名列表
        :type DeviceAliases: list of DeviceAlias
        """
        self.DeviceAliases = None


    def _deserialize(self, params):
        if params.get("DeviceAliases") is not None:
            self.DeviceAliases = []
            for item in params.get("DeviceAliases"):
                obj = DeviceAlias()
                obj._deserialize(item)
                self.DeviceAliases.append(obj)


class ModifyDeviceAliasesResponse(AbstractModel):
    """ModifyDeviceAliases返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPayModePre2PostRequest(AbstractModel):
    """ModifyPayModePre2Post请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要修改的设备ID列表
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class ModifyPayModePre2PostResponse(AbstractModel):
    """ModifyPayModePre2Post返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPsaRegulationRequest(AbstractModel):
    """ModifyPsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param PsaName: 预授权规则别名
        :type PsaName: str
        :param RepairLimit: 维修中的实例上限
        :type RepairLimit: int
        :param PsaDescription: 预授权规则备注
        :type PsaDescription: str
        :param TaskTypeIds: 预授权规则关联故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.RepairLimit = None
        self.PsaDescription = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")
        self.TaskTypeIds = params.get("TaskTypeIds")


class ModifyPsaRegulationResponse(AbstractModel):
    """ModifyPsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserCmdRequest(AbstractModel):
    """ModifyUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 待修改的脚本ID
        :type CmdId: str
        :param Alias: 待修改的脚本名称
        :type Alias: str
        :param OsType: 脚本适用的操作系统类型
        :type OsType: str
        :param Content: 待修改的脚本内容，必须经过base64编码
        :type Content: str
        """
        self.CmdId = None
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")


class ModifyUserCmdResponse(AbstractModel):
    """ModifyUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PsaRegulation(AbstractModel):
    """一条预授权规则

    """

    def __init__(self):
        """
        :param PsaId: 规则ID
        :type PsaId: str
        :param PsaName: 规则别名
        :type PsaName: str
        :param TagCount: 关联标签数量
        :type TagCount: int
        :param InstanceCount: 关联实例数量
        :type InstanceCount: int
        :param RepairCount: 故障实例数量
        :type RepairCount: int
        :param RepairLimit: 故障实例上限
        :type RepairLimit: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PsaDescription: 规则备注
        :type PsaDescription: str
        :param Tags: 关联标签
        :type Tags: list of Tag
        :param TaskTypeIds: 关联故障类型id
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.TagCount = None
        self.InstanceCount = None
        self.RepairCount = None
        self.RepairLimit = None
        self.CreateTime = None
        self.PsaDescription = None
        self.Tags = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.TagCount = params.get("TagCount")
        self.InstanceCount = params.get("InstanceCount")
        self.RepairCount = params.get("RepairCount")
        self.RepairLimit = params.get("RepairLimit")
        self.CreateTime = params.get("CreateTime")
        self.PsaDescription = params.get("PsaDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TaskTypeIds = params.get("TaskTypeIds")


class RebootDevicesRequest(AbstractModel):
    """RebootDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重启的设备ID列表
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RebootDevicesResponse(AbstractModel):
    """RebootDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetDevicePasswordRequest(AbstractModel):
    """ResetDevicePassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重置密码的服务器ID列表
        :type InstanceIds: list of str
        :param Password: 新密码
        :type Password: str
        """
        self.InstanceIds = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")


class ResetDevicePasswordResponse(AbstractModel):
    """ResetDevicePassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RunUserCmdRequest(AbstractModel):
    """RunUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 自定义脚本ID
        :type CmdId: str
        :param UserName: 执行脚本机器的用户名
        :type UserName: str
        :param Password: 执行脚本机器的用户名的密码
        :type Password: str
        :param InstanceIds: 执行脚本的服务器实例
        :type InstanceIds: list of str
        :param CmdParam: 执行脚本的参数，必须经过base64编码
        :type CmdParam: str
        """
        self.CmdId = None
        self.UserName = None
        self.Password = None
        self.InstanceIds = None
        self.CmdParam = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.InstanceIds = params.get("InstanceIds")
        self.CmdParam = params.get("CmdParam")


class RunUserCmdResponse(AbstractModel):
    """RunUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTaskInfoSet: 运行成功的任务信息列表
        :type SuccessTaskInfoSet: list of SuccessTaskInfo
        :param FailedTaskInfoSet: 运行失败的任务信息列表
        :type FailedTaskInfoSet: list of FailedTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessTaskInfoSet = None
        self.FailedTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SuccessTaskInfoSet") is not None:
            self.SuccessTaskInfoSet = []
            for item in params.get("SuccessTaskInfoSet"):
                obj = SuccessTaskInfo()
                obj._deserialize(item)
                self.SuccessTaskInfoSet.append(obj)
        if params.get("FailedTaskInfoSet") is not None:
            self.FailedTaskInfoSet = []
            for item in params.get("FailedTaskInfoSet"):
                obj = FailedTaskInfo()
                obj._deserialize(item)
                self.FailedTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SuccessTaskInfo(AbstractModel):
    """成功运行的自定义脚本信息

    """

    def __init__(self):
        """
        :param InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        """
        self.InstanceId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TaskId = params.get("TaskId")


class Tag(AbstractModel):
    """标签键与值

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValues: 标签键对应的值
        :type TagValues: list of str
        """
        self.TagKey = None
        self.TagValues = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValues = params.get("TagValues")


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


class UnbindPsaTagRequest(AbstractModel):
    """UnbindPsaTag请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param TagKey: 需要解绑的标签key
        :type TagKey: str
        :param TagValue: 需要解绑的标签value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class UnbindPsaTagResponse(AbstractModel):
    """UnbindPsaTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserCmd(AbstractModel):
    """脚本信息

    """

    def __init__(self):
        """
        :param Alias: 用户自定义脚本名
        :type Alias: str
        :param AppId: AppId
        :type AppId: int
        :param AutoId: 脚本自增ID
        :type AutoId: int
        :param CmdId: 脚本ID
        :type CmdId: str
        :param Content: 脚本内容
        :type Content: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param OsType: 命令适用的操作系统类型
        :type OsType: str
        """
        self.Alias = None
        self.AppId = None
        self.AutoId = None
        self.CmdId = None
        self.Content = None
        self.CreateTime = None
        self.ModifyTime = None
        self.OsType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.AutoId = params.get("AutoId")
        self.CmdId = params.get("CmdId")
        self.Content = params.get("Content")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.OsType = params.get("OsType")


class UserCmdTask(AbstractModel):
    """自定义脚本任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param Status: 任务状态ID，取值: -1(进行中) 0(结束)
        :type Status: int
        :param Alias: 脚本名称
        :type Alias: str
        :param CmdId: 脚本ID
        :type CmdId: str
        :param InstanceCount: 运行实例数量
        :type InstanceCount: int
        :param SuccessCount: 运行成功数量
        :type SuccessCount: int
        :param FailureCount: 运行失败数量
        :type FailureCount: int
        :param RunBeginTime: 执行开始时间
        :type RunBeginTime: str
        :param RunEndTime: 执行结束时间
        :type RunEndTime: str
        """
        self.TaskId = None
        self.Status = None
        self.Alias = None
        self.CmdId = None
        self.InstanceCount = None
        self.SuccessCount = None
        self.FailureCount = None
        self.RunBeginTime = None
        self.RunEndTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Alias = params.get("Alias")
        self.CmdId = params.get("CmdId")
        self.InstanceCount = params.get("InstanceCount")
        self.SuccessCount = params.get("SuccessCount")
        self.FailureCount = params.get("FailureCount")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")


class UserCmdTaskInfo(AbstractModel):
    """自定义脚本任务详细信息

    """

    def __init__(self):
        """
        :param AutoId: 自动编号，可忽略
        :type AutoId: int
        :param TaskId: 任务ID
        :type TaskId: str
        :param RunBeginTime: 任务开始时间
        :type RunBeginTime: str
        :param RunEndTime: 任务结束时间
        :type RunEndTime: str
        :param Status: 任务状态ID，取值为 -1：进行中；0：成功；>0：失败错误码
        :type Status: int
        :param InstanceName: 设备别名
        :type InstanceName: str
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param VpcName: 私有网络名
        :type VpcName: str
        :param VpcId: 私有网络整型ID
        :type VpcId: str
        :param VpcCidrBlock: 私有网络Cidr
        :type VpcCidrBlock: str
        :param SubnetName: 子网名
        :type SubnetName: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param SubnetCidrBlock: 子网Cidr
        :type SubnetCidrBlock: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param CmdContent: 脚本内容，base64编码后的值
        :type CmdContent: str
        :param CmdParam: 脚本参数，base64编码后的值
        :type CmdParam: str
        :param CmdResult: 脚本执行结果，base64编码后的值
        :type CmdResult: str
        :param AppId: 用户AppId
        :type AppId: int
        :param LastShellExit: 用户执行脚本结束退出的返回值，没有返回值为-1
        :type LastShellExit: int
        """
        self.AutoId = None
        self.TaskId = None
        self.RunBeginTime = None
        self.RunEndTime = None
        self.Status = None
        self.InstanceName = None
        self.InstanceId = None
        self.VpcName = None
        self.VpcId = None
        self.VpcCidrBlock = None
        self.SubnetName = None
        self.SubnetId = None
        self.SubnetCidrBlock = None
        self.LanIp = None
        self.CmdContent = None
        self.CmdParam = None
        self.CmdResult = None
        self.AppId = None
        self.LastShellExit = None


    def _deserialize(self, params):
        self.AutoId = params.get("AutoId")
        self.TaskId = params.get("TaskId")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.LanIp = params.get("LanIp")
        self.CmdContent = params.get("CmdContent")
        self.CmdParam = params.get("CmdParam")
        self.CmdResult = params.get("CmdResult")
        self.AppId = params.get("AppId")
        self.LastShellExit = params.get("LastShellExit")