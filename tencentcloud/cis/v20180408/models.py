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
        r"""
        :param _Command: 容器启动命令
        :type Command: str
        :param _Args: 容器启动参数
        :type Args: list of str
        :param _EnvironmentVars: 容器环境变量
        :type EnvironmentVars: list of EnvironmentVar
        :param _Image: 镜像
        :type Image: str
        :param _Name: 容器名，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 63个字符
        :type Name: str
        :param _Cpu: CPU，单位：核
        :type Cpu: float
        :param _Memory: 内存，单位：Gi
        :type Memory: float
        :param _RestartCount: 重启次数
        :type RestartCount: int
        :param _CurrentState: 当前状态
        :type CurrentState: :class:`tencentcloud.cis.v20180408.models.ContainerState`
        :param _PreviousState: 上一次状态
        :type PreviousState: :class:`tencentcloud.cis.v20180408.models.ContainerState`
        :param _WorkingDir: 容器工作目录
        :type WorkingDir: str
        :param _ContainerId: 容器ID
        :type ContainerId: str
        """
        self._Command = None
        self._Args = None
        self._EnvironmentVars = None
        self._Image = None
        self._Name = None
        self._Cpu = None
        self._Memory = None
        self._RestartCount = None
        self._CurrentState = None
        self._PreviousState = None
        self._WorkingDir = None
        self._ContainerId = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def EnvironmentVars(self):
        return self._EnvironmentVars

    @EnvironmentVars.setter
    def EnvironmentVars(self, EnvironmentVars):
        self._EnvironmentVars = EnvironmentVars

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def CurrentState(self):
        return self._CurrentState

    @CurrentState.setter
    def CurrentState(self, CurrentState):
        self._CurrentState = CurrentState

    @property
    def PreviousState(self):
        return self._PreviousState

    @PreviousState.setter
    def PreviousState(self, PreviousState):
        self._PreviousState = PreviousState

    @property
    def WorkingDir(self):
        return self._WorkingDir

    @WorkingDir.setter
    def WorkingDir(self, WorkingDir):
        self._WorkingDir = WorkingDir

    @property
    def ContainerId(self):
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId


    def _deserialize(self, params):
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        if params.get("EnvironmentVars") is not None:
            self._EnvironmentVars = []
            for item in params.get("EnvironmentVars"):
                obj = EnvironmentVar()
                obj._deserialize(item)
                self._EnvironmentVars.append(obj)
        self._Image = params.get("Image")
        self._Name = params.get("Name")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._RestartCount = params.get("RestartCount")
        if params.get("CurrentState") is not None:
            self._CurrentState = ContainerState()
            self._CurrentState._deserialize(params.get("CurrentState"))
        if params.get("PreviousState") is not None:
            self._PreviousState = ContainerState()
            self._PreviousState._deserialize(params.get("PreviousState"))
        self._WorkingDir = params.get("WorkingDir")
        self._ContainerId = params.get("ContainerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerInstance(AbstractModel):
    """容器实例的具体信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 容器实例ID
        :type InstanceId: str
        :param _InstanceName: 容器实例名称
        :type InstanceName: str
        :param _VpcId: 容器实例所属VpcId
        :type VpcId: str
        :param _SubnetId: 容器实例所属SubnetId
        :type SubnetId: str
        :param _State: 容器实例状态
        :type State: str
        :param _Containers: 容器列表
        :type Containers: list of Container
        :param _RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 启动时间
        :type StartTime: str
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcName: Vpc名称
        :type VpcName: str
        :param _VpcCidr: VpcCidr
        :type VpcCidr: str
        :param _SubnetName: SubnetName
        :type SubnetName: str
        :param _SubnetCidr: 子网Cidr
        :type SubnetCidr: str
        :param _LanIp: 内网IP
        :type LanIp: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._State = None
        self._Containers = None
        self._RestartPolicy = None
        self._CreateTime = None
        self._StartTime = None
        self._Zone = None
        self._VpcName = None
        self._VpcCidr = None
        self._SubnetName = None
        self._SubnetCidr = None
        self._LanIp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidr(self):
        return self._VpcCidr

    @VpcCidr.setter
    def VpcCidr(self, VpcCidr):
        self._VpcCidr = VpcCidr

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetCidr(self):
        return self._SubnetCidr

    @SubnetCidr.setter
    def SubnetCidr(self, SubnetCidr):
        self._SubnetCidr = SubnetCidr

    @property
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._State = params.get("State")
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        self._RestartPolicy = params.get("RestartPolicy")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._Zone = params.get("Zone")
        self._VpcName = params.get("VpcName")
        self._VpcCidr = params.get("VpcCidr")
        self._SubnetName = params.get("SubnetName")
        self._SubnetCidr = params.get("SubnetCidr")
        self._LanIp = params.get("LanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerLog(AbstractModel):
    """容器日志

    """

    def __init__(self):
        r"""
        :param _Name: 容器名称
        :type Name: str
        :param _Log: 日志
        :type Log: str
        :param _Time: 日志记录时间
        :type Time: str
        """
        self._Name = None
        self._Log = None
        self._Time = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Log = params.get("Log")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerState(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param _StartTime: 容器运行开始时间
        :type StartTime: str
        :param _State: 容器状态
        :type State: str
        :param _Reason: 状态详情
        :type Reason: str
        :param _FinishTime: 容器运行结束时间
        :type FinishTime: str
        :param _ExitCode: 容器运行退出码
        :type ExitCode: int
        """
        self._StartTime = None
        self._State = None
        self._Reason = None
        self._FinishTime = None
        self._ExitCode = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExitCode(self):
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._State = params.get("State")
        self._Reason = params.get("Reason")
        self._FinishTime = params.get("FinishTime")
        self._ExitCode = params.get("ExitCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContainerInstanceRequest(AbstractModel):
    """CreateContainerInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcId: vpcId
        :type VpcId: str
        :param _SubnetId: subnetId
        :type SubnetId: str
        :param _InstanceName: 容器实例名称，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 40个字符
        :type InstanceName: str
        :param _RestartPolicy: 重启策略（Always,OnFailure,Never）
        :type RestartPolicy: str
        :param _Containers: 容器列表
        :type Containers: list of Container
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._RestartPolicy = None
        self._Containers = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._RestartPolicy = params.get("RestartPolicy")
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContainerInstanceResponse(AbstractModel):
    """CreateContainerInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 容器实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DeleteContainerInstanceRequest(AbstractModel):
    """DeleteContainerInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self._InstanceName = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContainerInstanceResponse(AbstractModel):
    """DeleteContainerInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 操作信息
        :type Msg: str
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeContainerInstanceEventsRequest(AbstractModel):
    """DescribeContainerInstanceEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self._InstanceName = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerInstanceEventsResponse(AbstractModel):
    """DescribeContainerInstanceEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventList: 容器实例事件列表
        :type EventList: list of Event
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._EventList = None
        self._RequestId = None

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeContainerInstanceRequest(AbstractModel):
    """DescribeContainerInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 容器实例名称
        :type InstanceName: str
        """
        self._InstanceName = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerInstanceResponse(AbstractModel):
    """DescribeContainerInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerInstance: 容器实例详细信息
        :type ContainerInstance: :class:`tencentcloud.cis.v20180408.models.ContainerInstance`
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._ContainerInstance = None
        self._RequestId = None

    @property
    def ContainerInstance(self):
        return self._ContainerInstance

    @ContainerInstance.setter
    def ContainerInstance(self, ContainerInstance):
        self._ContainerInstance = ContainerInstance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerInstance") is not None:
            self._ContainerInstance = ContainerInstance()
            self._ContainerInstance._deserialize(params.get("ContainerInstance"))
        self._RequestId = params.get("RequestId")


class DescribeContainerInstancesRequest(AbstractModel):
    """DescribeContainerInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10
        :type Limit: int
        :param _Filters: 过滤条件。
- Zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。
- VpcId - String - 是否必填：否 -（过滤条件）按照VpcId过滤。
- InstanceName - String - 是否必填：否 -（过滤条件）按照容器实例名称做模糊查询。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerInstancesResponse(AbstractModel):
    """DescribeContainerInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerInstanceList: 容器实例列表
        :type ContainerInstanceList: list of ContainerInstance
        :param _TotalCount: 容器实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._ContainerInstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ContainerInstanceList(self):
        return self._ContainerInstanceList

    @ContainerInstanceList.setter
    def ContainerInstanceList(self, ContainerInstanceList):
        self._ContainerInstanceList = ContainerInstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerInstanceList") is not None:
            self._ContainerInstanceList = []
            for item in params.get("ContainerInstanceList"):
                obj = ContainerInstance()
                obj._deserialize(item)
                self._ContainerInstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeContainerLogRequest(AbstractModel):
    """DescribeContainerLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 容器实例名称
        :type InstanceName: str
        :param _ContainerName: 容器名称
        :type ContainerName: str
        :param _Tail: 日志显示尾部行数
        :type Tail: int
        :param _SinceTime: 日志起始时间
        :type SinceTime: str
        """
        self._InstanceName = None
        self._ContainerName = None
        self._Tail = None
        self._SinceTime = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def Tail(self):
        return self._Tail

    @Tail.setter
    def Tail(self, Tail):
        self._Tail = Tail

    @property
    def SinceTime(self):
        return self._SinceTime

    @SinceTime.setter
    def SinceTime(self, SinceTime):
        self._SinceTime = SinceTime


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._ContainerName = params.get("ContainerName")
        self._Tail = params.get("Tail")
        self._SinceTime = params.get("SinceTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerLogResponse(AbstractModel):
    """DescribeContainerLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerLogList: 容器日志数组
        :type ContainerLogList: list of ContainerLog
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._ContainerLogList = None
        self._RequestId = None

    @property
    def ContainerLogList(self):
        return self._ContainerLogList

    @ContainerLogList.setter
    def ContainerLogList(self, ContainerLogList):
        self._ContainerLogList = ContainerLogList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerLogList") is not None:
            self._ContainerLogList = []
            for item in params.get("ContainerLogList"):
                obj = ContainerLog()
                obj._deserialize(item)
                self._ContainerLogList.append(obj)
        self._RequestId = params.get("RequestId")


class EnvironmentVar(AbstractModel):
    """容器环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量名
        :type Name: str
        :param _Value: 环境变量值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """容器实例事件

    """

    def __init__(self):
        r"""
        :param _FirstSeen: 事件首次出现时间
        :type FirstSeen: str
        :param _LastSeen: 事件上次出现时间
        :type LastSeen: str
        :param _Level: 事件等级
        :type Level: str
        :param _Count: 事件出现次数
        :type Count: str
        :param _Reason: 事件出现原因
        :type Reason: str
        :param _Message: 事件消息
        :type Message: str
        """
        self._FirstSeen = None
        self._LastSeen = None
        self._Level = None
        self._Count = None
        self._Reason = None
        self._Message = None

    @property
    def FirstSeen(self):
        return self._FirstSeen

    @FirstSeen.setter
    def FirstSeen(self, FirstSeen):
        self._FirstSeen = FirstSeen

    @property
    def LastSeen(self):
        return self._LastSeen

    @LastSeen.setter
    def LastSeen(self, LastSeen):
        self._LastSeen = LastSeen

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._FirstSeen = params.get("FirstSeen")
        self._LastSeen = params.get("LastSeen")
        self._Level = params.get("Level")
        self._Count = params.get("Count")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段，可选值 - Zone，VpcId，InstanceName
        :type Name: str
        :param _ValueList: 过滤值列表
        :type ValueList: list of str
        """
        self._Name = None
        self._ValueList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ValueList(self):
        return self._ValueList

    @ValueList.setter
    def ValueList(self, ValueList):
        self._ValueList = ValueList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ValueList = params.get("ValueList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateCisRequest(AbstractModel):
    """InquiryPriceCreateCis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _Cpu: CPU，单位：核
        :type Cpu: float
        :param _Memory: 内存，单位：Gi
        :type Memory: float
        """
        self._Zone = None
        self._Cpu = None
        self._Memory = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateCisResponse(AbstractModel):
    """InquiryPriceCreateCis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 价格
        :type Price: :class:`tencentcloud.cis.v20180408.models.Price`
        :param _RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        r"""
        :param _DiscountPrice: 原价，单位：元
        :type DiscountPrice: float
        :param _OriginalPrice: 折扣价，单位：元
        :type OriginalPrice: float
        """
        self._DiscountPrice = None
        self._OriginalPrice = None

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice


    def _deserialize(self, params):
        self._DiscountPrice = params.get("DiscountPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        