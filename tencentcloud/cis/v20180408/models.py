# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class Container(AbstractModel):
    """容器实例中容器结构体

    """

    def __init__(self):
        """
        :param Command: 容器启动命令
        :type Command: str
        :param Args: 容器启动参数
        :type Args: list of str
        :param EnvironmentVars: 容器环境变量
        :type EnvironmentVars: list of EnvironmentVar
        :param Image: 镜像
        :type Image: str
        :param Name: 容器名，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 63个字符
        :type Name: str
        :param Cpu: CPU，单位：核
        :type Cpu: float
        :param Memory: 内存，单位：Gi
        :type Memory: float
        :param RestartCount: 重启次数
        :type RestartCount: int
        :param CurrentState: 当前状态
        :type CurrentState: :class:`tencentcloud.cis.v20180408.models.ContainerState`
        :param PreviousState: 上一次状态
        :type PreviousState: :class:`tencentcloud.cis.v20180408.models.ContainerState`
        :param WorkingDir: 容器工作目录
        :type WorkingDir: str
        :param ContainerId: 容器ID
        :type ContainerId: str
        """
        self.Command = None
        self.Args = None
        self.EnvironmentVars = None
        self.Image = None
        self.Name = None
        self.Cpu = None
        self.Memory = None
        self.RestartCount = None
        self.CurrentState = None
        self.PreviousState = None
        self.WorkingDir = None
        self.ContainerId = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        if params.get("EnvironmentVars") is not None:
            self.EnvironmentVars = []
            for item in params.get("EnvironmentVars"):
                obj = EnvironmentVar()
                obj._deserialize(item)
                self.EnvironmentVars.append(obj)
        self.Image = params.get("Image")
        self.Name = params.get("Name")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.RestartCount = params.get("RestartCount")
        if params.get("CurrentState") is not None:
            self.CurrentState = ContainerState()
            self.CurrentState._deserialize(params.get("CurrentState"))
        if params.get("PreviousState") is not None:
            self.PreviousState = ContainerState()
            self.PreviousState._deserialize(params.get("PreviousState"))
        self.WorkingDir = params.get("WorkingDir")
        self.ContainerId = params.get("ContainerId")


class ContainerInstance(AbstractModel):
    """容器实例的具体信息

    """

    def __init__(self):
        """
        :param InstanceId: 容器实例ID
        :type InstanceId: str
        :param InstanceName: 容器实例名称
        :type InstanceName: str
        :param VpcId: 容器实例所属VpcId
        :type VpcId: str
        :param SubnetId: 容器实例所属SubnetId
        :type SubnetId: str
        :param State: 容器实例状态
        :type State: str
        :param Containers: 容器列表
        :type Containers: list of Container
        :param RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param StartTime: 启动时间
        :type StartTime: str
        :param Zone: 可用区
        :type Zone: str
        :param VpcName: Vpc名称
        :type VpcName: str
        :param VpcCidr: VpcCidr
        :type VpcCidr: str
        :param SubnetName: SubnetName
        :type SubnetName: str
        :param SubnetCidr: 子网Cidr
        :type SubnetCidr: str
        :param LanIp: 内网IP
        :type LanIp: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.State = None
        self.Containers = None
        self.RestartPolicy = None
        self.CreateTime = None
        self.StartTime = None
        self.Zone = None
        self.VpcName = None
        self.VpcCidr = None
        self.SubnetName = None
        self.SubnetCidr = None
        self.LanIp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.State = params.get("State")
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        self.RestartPolicy = params.get("RestartPolicy")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.Zone = params.get("Zone")
        self.VpcName = params.get("VpcName")
        self.VpcCidr = params.get("VpcCidr")
        self.SubnetName = params.get("SubnetName")
        self.SubnetCidr = params.get("SubnetCidr")
        self.LanIp = params.get("LanIp")


class ContainerLog(AbstractModel):
    """容器日志

    """

    def __init__(self):
        """
        :param Name: 容器名称
        :type Name: str
        :param Log: 日志
        :type Log: str
        :param Time: 日志记录时间
        :type Time: str
        """
        self.Name = None
        self.Log = None
        self.Time = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Log = params.get("Log")
        self.Time = params.get("Time")


class ContainerState(AbstractModel):
    """容器状态

    """

    def __init__(self):
        """
        :param StartTime: 容器运行开始时间
        :type StartTime: str
        :param State: 容器状态
        :type State: str
        :param Reason: 状态详情
        :type Reason: str
        :param FinishTime: 容器运行结束时间
        :type FinishTime: str
        :param ExitCode: 容器运行退出码
        :type ExitCode: int
        """
        self.StartTime = None
        self.State = None
        self.Reason = None
        self.FinishTime = None
        self.ExitCode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.State = params.get("State")
        self.Reason = params.get("Reason")
        self.FinishTime = params.get("FinishTime")
        self.ExitCode = params.get("ExitCode")


class CreateContainerInstanceRequest(AbstractModel):
    """CreateContainerInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区
        :type Zone: str
        :param VpcId: vpcId
        :type VpcId: str
        :param SubnetId: subnetId
        :type SubnetId: str
        :param InstanceName: 容器实例名称，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 40个字符
        :type InstanceName: str
        :param RestartPolicy: 重启策略（Always,OnFailure,Never）
        :type RestartPolicy: str
        :param Containers: 容器列表
        :type Containers: list of Container
        """
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceName = None
        self.RestartPolicy = None
        self.Containers = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceName = params.get("InstanceName")
        self.RestartPolicy = params.get("RestartPolicy")
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)


class CreateContainerInstanceResponse(AbstractModel):
    """CreateContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 容器实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteContainerInstanceRequest(AbstractModel):
    """DeleteContainerInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")


class DeleteContainerInstanceResponse(AbstractModel):
    """DeleteContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Msg: 操作信息
        :type Msg: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeContainerInstanceEventsRequest(AbstractModel):
    """DescribeContainerInstanceEvents请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")


class DescribeContainerInstanceEventsResponse(AbstractModel):
    """DescribeContainerInstanceEvents返回参数结构体

    """

    def __init__(self):
        """
        :param EventList: 容器实例事件列表
        :type EventList: list of Event
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.EventList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContainerInstanceRequest(AbstractModel):
    """DescribeContainerInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")


class DescribeContainerInstanceResponse(AbstractModel):
    """DescribeContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerInstance: 容器实例详细信息
        :type ContainerInstance: :class:`tencentcloud.cis.v20180408.models.ContainerInstance`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ContainerInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContainerInstance") is not None:
            self.ContainerInstance = ContainerInstance()
            self.ContainerInstance._deserialize(params.get("ContainerInstance"))
        self.RequestId = params.get("RequestId")


class DescribeContainerInstancesRequest(AbstractModel):
    """DescribeContainerInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10
        :type Limit: int
        :param Filters: 过滤条件。
- Zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。
- VpcId - String - 是否必填：否 -（过滤条件）按照VpcId过滤。
- InstanceName - String - 是否必填：否 -（过滤条件）按照容器实例名称做模糊查询。
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


class DescribeContainerInstancesResponse(AbstractModel):
    """DescribeContainerInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerInstanceList: 容器实例列表
        :type ContainerInstanceList: list of ContainerInstance
        :param TotalCount: 容器实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ContainerInstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContainerInstanceList") is not None:
            self.ContainerInstanceList = []
            for item in params.get("ContainerInstanceList"):
                obj = ContainerInstance()
                obj._deserialize(item)
                self.ContainerInstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeContainerLogRequest(AbstractModel):
    """DescribeContainerLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 容器实例名称
        :type InstanceName: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param Tail: 日志显示尾部行数
        :type Tail: int
        :param SinceTime: 日志起始时间
        :type SinceTime: str
        """
        self.InstanceName = None
        self.ContainerName = None
        self.Tail = None
        self.SinceTime = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.ContainerName = params.get("ContainerName")
        self.Tail = params.get("Tail")
        self.SinceTime = params.get("SinceTime")


class DescribeContainerLogResponse(AbstractModel):
    """DescribeContainerLog返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerLogList: 容器日志数组
        :type ContainerLogList: list of ContainerLog
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ContainerLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContainerLogList") is not None:
            self.ContainerLogList = []
            for item in params.get("ContainerLogList"):
                obj = ContainerLog()
                obj._deserialize(item)
                self.ContainerLogList.append(obj)
        self.RequestId = params.get("RequestId")


class EnvironmentVar(AbstractModel):
    """容器环境变量

    """

    def __init__(self):
        """
        :param Name: 环境变量名
        :type Name: str
        :param Value: 环境变量值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class Event(AbstractModel):
    """容器实例事件

    """

    def __init__(self):
        """
        :param FirstSeen: 事件首次出现时间
        :type FirstSeen: str
        :param LastSeen: 事件上次出现时间
        :type LastSeen: str
        :param Level: 事件等级
        :type Level: str
        :param Count: 事件出现次数
        :type Count: str
        :param Reason: 事件出现原因
        :type Reason: str
        :param Message: 事件消息
        :type Message: str
        """
        self.FirstSeen = None
        self.LastSeen = None
        self.Level = None
        self.Count = None
        self.Reason = None
        self.Message = None


    def _deserialize(self, params):
        self.FirstSeen = params.get("FirstSeen")
        self.LastSeen = params.get("LastSeen")
        self.Level = params.get("Level")
        self.Count = params.get("Count")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        """
        :param Name: 过滤字段，可选值 - Zone，VpcId，InstanceName
        :type Name: str
        :param ValueList: 过滤值列表
        :type ValueList: list of str
        """
        self.Name = None
        self.ValueList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ValueList = params.get("ValueList")


class InquiryPriceCreateCisRequest(AbstractModel):
    """InquiryPriceCreateCis请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区
        :type Zone: str
        :param Cpu: CPU，单位：核
        :type Cpu: float
        :param Memory: 内存，单位：Gi
        :type Memory: float
        """
        self.Zone = None
        self.Cpu = None
        self.Memory = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")


class InquiryPriceCreateCisResponse(AbstractModel):
    """InquiryPriceCreateCis返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格
        :type Price: :class:`tencentcloud.cis.v20180408.models.Price`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        """
        :param DiscountPrice: 原价，单位：元
        :type DiscountPrice: float
        :param OriginalPrice: 折扣价，单位：元
        :type OriginalPrice: float
        """
        self.DiscountPrice = None
        self.OriginalPrice = None


    def _deserialize(self, params):
        self.DiscountPrice = params.get("DiscountPrice")
        self.OriginalPrice = params.get("OriginalPrice")