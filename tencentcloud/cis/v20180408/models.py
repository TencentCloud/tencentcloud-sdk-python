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


class Container(AbstractModel):
    """容器实例中容器结构体

    """

    def __init__(self):
        """
        :param Command: 容器启动命令\n        :type Command: str\n        :param Args: 容器启动参数\n        :type Args: list of str\n        :param EnvironmentVars: 容器环境变量\n        :type EnvironmentVars: list of EnvironmentVar\n        :param Image: 镜像\n        :type Image: str\n        :param Name: 容器名，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 63个字符\n        :type Name: str\n        :param Cpu: CPU，单位：核\n        :type Cpu: float\n        :param Memory: 内存，单位：Gi\n        :type Memory: float\n        :param RestartCount: 重启次数\n        :type RestartCount: int\n        :param CurrentState: 当前状态\n        :type CurrentState: :class:`tencentcloud.cis.v20180408.models.ContainerState`\n        :param PreviousState: 上一次状态\n        :type PreviousState: :class:`tencentcloud.cis.v20180408.models.ContainerState`\n        :param WorkingDir: 容器工作目录\n        :type WorkingDir: str\n        :param ContainerId: 容器ID\n        :type ContainerId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerInstance(AbstractModel):
    """容器实例的具体信息

    """

    def __init__(self):
        """
        :param InstanceId: 容器实例ID\n        :type InstanceId: str\n        :param InstanceName: 容器实例名称\n        :type InstanceName: str\n        :param VpcId: 容器实例所属VpcId\n        :type VpcId: str\n        :param SubnetId: 容器实例所属SubnetId\n        :type SubnetId: str\n        :param State: 容器实例状态\n        :type State: str\n        :param Containers: 容器列表\n        :type Containers: list of Container\n        :param RestartPolicy: 重启策略\n        :type RestartPolicy: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param StartTime: 启动时间\n        :type StartTime: str\n        :param Zone: 可用区\n        :type Zone: str\n        :param VpcName: Vpc名称\n        :type VpcName: str\n        :param VpcCidr: VpcCidr\n        :type VpcCidr: str\n        :param SubnetName: SubnetName\n        :type SubnetName: str\n        :param SubnetCidr: 子网Cidr\n        :type SubnetCidr: str\n        :param LanIp: 内网IP\n        :type LanIp: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerLog(AbstractModel):
    """容器日志

    """

    def __init__(self):
        """
        :param Name: 容器名称\n        :type Name: str\n        :param Log: 日志\n        :type Log: str\n        :param Time: 日志记录时间\n        :type Time: str\n        """
        self.Name = None
        self.Log = None
        self.Time = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Log = params.get("Log")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerState(AbstractModel):
    """容器状态

    """

    def __init__(self):
        """
        :param StartTime: 容器运行开始时间\n        :type StartTime: str\n        :param State: 容器状态\n        :type State: str\n        :param Reason: 状态详情\n        :type Reason: str\n        :param FinishTime: 容器运行结束时间\n        :type FinishTime: str\n        :param ExitCode: 容器运行退出码\n        :type ExitCode: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContainerInstanceRequest(AbstractModel):
    """CreateContainerInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        :param VpcId: vpcId\n        :type VpcId: str\n        :param SubnetId: subnetId\n        :type SubnetId: str\n        :param InstanceName: 容器实例名称，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 40个字符\n        :type InstanceName: str\n        :param RestartPolicy: 重启策略（Always,OnFailure,Never）\n        :type RestartPolicy: str\n        :param Containers: 容器列表\n        :type Containers: list of Container\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContainerInstanceResponse(AbstractModel):
    """CreateContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 容器实例ID\n        :type InstanceId: str\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceName: 容器实例名称\n        :type InstanceName: str\n        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContainerInstanceResponse(AbstractModel):
    """DeleteContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Msg: 操作信息\n        :type Msg: str\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceName: 容器实例名称\n        :type InstanceName: str\n        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerInstanceEventsResponse(AbstractModel):
    """DescribeContainerInstanceEvents返回参数结构体

    """

    def __init__(self):
        """
        :param EventList: 容器实例事件列表\n        :type EventList: list of Event\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceName: 容器实例名称\n        :type InstanceName: str\n        """
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerInstanceResponse(AbstractModel):
    """DescribeContainerInstance返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerInstance: 容器实例详细信息\n        :type ContainerInstance: :class:`tencentcloud.cis.v20180408.models.ContainerInstance`\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为10\n        :type Limit: int\n        :param Filters: 过滤条件。
- Zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。
- VpcId - String - 是否必填：否 -（过滤条件）按照VpcId过滤。
- InstanceName - String - 是否必填：否 -（过滤条件）按照容器实例名称做模糊查询。\n        :type Filters: list of Filter\n        """
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
        


class DescribeContainerInstancesResponse(AbstractModel):
    """DescribeContainerInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerInstanceList: 容器实例列表\n        :type ContainerInstanceList: list of ContainerInstance\n        :param TotalCount: 容器实例总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceName: 容器实例名称\n        :type InstanceName: str\n        :param ContainerName: 容器名称\n        :type ContainerName: str\n        :param Tail: 日志显示尾部行数\n        :type Tail: int\n        :param SinceTime: 日志起始时间\n        :type SinceTime: str\n        """
        self.InstanceName = None
        self.ContainerName = None
        self.Tail = None
        self.SinceTime = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.ContainerName = params.get("ContainerName")
        self.Tail = params.get("Tail")
        self.SinceTime = params.get("SinceTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerLogResponse(AbstractModel):
    """DescribeContainerLog返回参数结构体

    """

    def __init__(self):
        """
        :param ContainerLogList: 容器日志数组\n        :type ContainerLogList: list of ContainerLog\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 环境变量名\n        :type Name: str\n        :param Value: 环境变量值\n        :type Value: str\n        """
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
        


class Event(AbstractModel):
    """容器实例事件

    """

    def __init__(self):
        """
        :param FirstSeen: 事件首次出现时间\n        :type FirstSeen: str\n        :param LastSeen: 事件上次出现时间\n        :type LastSeen: str\n        :param Level: 事件等级\n        :type Level: str\n        :param Count: 事件出现次数\n        :type Count: str\n        :param Reason: 事件出现原因\n        :type Reason: str\n        :param Message: 事件消息\n        :type Message: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        """
        :param Name: 过滤字段，可选值 - Zone，VpcId，InstanceName\n        :type Name: str\n        :param ValueList: 过滤值列表\n        :type ValueList: list of str\n        """
        self.Name = None
        self.ValueList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ValueList = params.get("ValueList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateCisRequest(AbstractModel):
    """InquiryPriceCreateCis请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        :param Cpu: CPU，单位：核\n        :type Cpu: float\n        :param Memory: 内存，单位：Gi\n        :type Memory: float\n        """
        self.Zone = None
        self.Cpu = None
        self.Memory = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateCisResponse(AbstractModel):
    """InquiryPriceCreateCis返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格\n        :type Price: :class:`tencentcloud.cis.v20180408.models.Price`\n        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。\n        :type RequestId: str\n        """
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
        :param DiscountPrice: 原价，单位：元\n        :type DiscountPrice: float\n        :param OriginalPrice: 折扣价，单位：元\n        :type OriginalPrice: float\n        """
        self.DiscountPrice = None
        self.OriginalPrice = None


    def _deserialize(self, params):
        self.DiscountPrice = params.get("DiscountPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        