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


class Activity(AbstractModel):
    """计算环境的创建或销毁活动

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动ID
        :type ActivityId: str
        :param _ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        :param _ComputeNodeActivityType: 计算节点活动类型，创建或者销毁
        :type ComputeNodeActivityType: str
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _Cause: 起因
        :type Cause: str
        :param _ActivityState: 活动状态
        :type ActivityState: str
        :param _StateReason: 状态原因
        :type StateReason: str
        :param _StartTime: 活动开始时间
        :type StartTime: str
        :param _EndTime: 活动结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _InstanceId: 云服务器实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self._ActivityId = None
        self._ComputeNodeId = None
        self._ComputeNodeActivityType = None
        self._EnvId = None
        self._Cause = None
        self._ActivityState = None
        self._StateReason = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ComputeNodeId(self):
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId

    @property
    def ComputeNodeActivityType(self):
        return self._ComputeNodeActivityType

    @ComputeNodeActivityType.setter
    def ComputeNodeActivityType(self, ComputeNodeActivityType):
        self._ComputeNodeActivityType = ComputeNodeActivityType

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Cause(self):
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def ActivityState(self):
        return self._ActivityState

    @ActivityState.setter
    def ActivityState(self, ActivityState):
        self._ActivityState = ActivityState

    @property
    def StateReason(self):
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ComputeNodeId = params.get("ComputeNodeId")
        self._ComputeNodeActivityType = params.get("ComputeNodeActivityType")
        self._EnvId = params.get("EnvId")
        self._Cause = params.get("Cause")
        self._ActivityState = params.get("ActivityState")
        self._StateReason = params.get("StateReason")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentRunningMode(AbstractModel):
    """agent运行模式

    """

    def __init__(self):
        r"""
        :param _Scene: 场景类型，支持WINDOWS
        :type Scene: str
        :param _User: 运行Agent的User
        :type User: str
        :param _Session: 运行Agent的Session
        :type Session: str
        """
        self._Scene = None
        self._User = None
        self._Session = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Session(self):
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._User = params.get("User")
        self._Session = params.get("Session")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnonymousComputeEnv(AbstractModel):
    """计算环境

    """

    def __init__(self):
        r"""
        :param _EnvType: 计算环境管理类型
        :type EnvType: str
        :param _EnvData: 计算环境具体参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param _AgentRunningMode: agent运行模式，适用于Windows系统
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._AgentRunningMode = None

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def AgentRunningMode(self):
        return self._AgentRunningMode

    @AgentRunningMode.setter
    def AgentRunningMode(self, AgentRunningMode):
        self._AgentRunningMode = AgentRunningMode


    def _deserialize(self, params):
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("AgentRunningMode") is not None:
            self._AgentRunningMode = AgentRunningMode()
            self._AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Application(AbstractModel):
    """应用程序信息

    """

    def __init__(self):
        r"""
        :param _DeliveryForm: 应用程序的交付方式，包括PACKAGE、LOCAL 两种取值，分别指远程存储的软件包、计算环境本地。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliveryForm: str
        :param _Command: 任务执行命令。与Commands不能同时指定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param _PackagePath: 应用程序软件包的远程存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type PackagePath: str
        :param _Docker: 应用使用Docker的相关配置。在使用Docker配置的情况下，DeliveryForm 为 LOCAL 表示直接使用Docker镜像内部的应用软件，通过Docker方式运行；DeliveryForm 为 PACKAGE，表示将远程应用包注入到Docker镜像后，通过Docker方式运行。为避免Docker不同版本的兼容性问题，Docker安装包及相关依赖由Batch统一负责，对于已安装Docker的自定义镜像，请卸载后再使用Docker特性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Docker: :class:`tencentcloud.batch.v20170312.models.Docker`
        :param _Commands: 任务执行命令信息。与Command不能同时指定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Commands: list of CommandLine
        """
        self._DeliveryForm = None
        self._Command = None
        self._PackagePath = None
        self._Docker = None
        self._Commands = None

    @property
    def DeliveryForm(self):
        return self._DeliveryForm

    @DeliveryForm.setter
    def DeliveryForm(self, DeliveryForm):
        self._DeliveryForm = DeliveryForm

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def PackagePath(self):
        return self._PackagePath

    @PackagePath.setter
    def PackagePath(self, PackagePath):
        self._PackagePath = PackagePath

    @property
    def Docker(self):
        return self._Docker

    @Docker.setter
    def Docker(self, Docker):
        self._Docker = Docker

    @property
    def Commands(self):
        return self._Commands

    @Commands.setter
    def Commands(self, Commands):
        self._Commands = Commands


    def _deserialize(self, params):
        self._DeliveryForm = params.get("DeliveryForm")
        self._Command = params.get("Command")
        self._PackagePath = params.get("PackagePath")
        if params.get("Docker") is not None:
            self._Docker = Docker()
            self._Docker._deserialize(params.get("Docker"))
        if params.get("Commands") is not None:
            self._Commands = []
            for item in params.get("Commands"):
                obj = CommandLine()
                obj._deserialize(item)
                self._Commands.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesRequest(AbstractModel):
    """AttachInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _Instances: 加入计算环境实例列表
        :type Instances: list of Instance
        """
        self._EnvId = None
        self._Instances = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesResponse(AbstractModel):
    """AttachInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Authentication(AbstractModel):
    """授权认证信息

    """

    def __init__(self):
        r"""
        :param _Scene: 授权场景，例如COS
        :type Scene: str
        :param _SecretId: SecretId
        :type SecretId: str
        :param _SecretKey: SecretKey
        :type SecretKey: str
        """
        self._Scene = None
        self._SecretId = None
        self._SecretKey = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommandLine(AbstractModel):
    """任务执行信息描述。

    """

    def __init__(self):
        r"""
        :param _Command: 任务执行命令。
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        """
        self._Command = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvCreateInfo(AbstractModel):
    """计算环境创建信息。

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境 ID
        :type EnvId: str
        :param _EnvName: 计算环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvName: str
        :param _EnvDescription: 计算环境描述
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvDescription: str
        :param _EnvType: 计算环境类型，仅支持“MANAGED”类型
        :type EnvType: str
        :param _EnvData: 计算环境参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: 数据盘挂载选项
注意：此字段可能返回 null，表示取不到有效值。
        :type MountDataDisks: list of MountDataDisk
        :param _InputMappings: 输入映射
注意：此字段可能返回 null，表示取不到有效值。
        :type InputMappings: list of InputMapping
        :param _Authentications: 授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentications: list of Authentication
        :param _Notifications: 通知信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Notifications: list of Notification
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _Tags: 计算环境标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._EnvId = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._InputMappings = None
        self._Authentications = None
        self._Notifications = None
        self._DesiredComputeNodeCount = None
        self._Tags = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def InputMappings(self):
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def Authentications(self):
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def Notifications(self):
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvData(AbstractModel):
    """计算环境属性数据

    """

    def __init__(self):
        r"""
        :param _InstanceTypes: CVM实例类型列表
        :type InstanceTypes: list of str
        """
        self._InstanceTypes = None

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes


    def _deserialize(self, params):
        self._InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvView(AbstractModel):
    """计算环境信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ComputeNodeMetrics: 计算节点统计指标
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param _EnvType: 计算环境类型
        :type EnvType: str
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _ResourceType: 计算环境资源类型，当前为CVM和CPM（黑石）
        :type ResourceType: str
        :param _NextAction: 下一步动作
        :type NextAction: str
        :param _AttachedComputeNodeCount: 用户添加到计算环境中的计算节点个数
        :type AttachedComputeNodeCount: int
        :param _Tags: 计算环境绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._EnvId = None
        self._EnvName = None
        self._Placement = None
        self._CreateTime = None
        self._ComputeNodeMetrics = None
        self._EnvType = None
        self._DesiredComputeNodeCount = None
        self._ResourceType = None
        self._NextAction = None
        self._AttachedComputeNodeCount = None
        self._Tags = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ComputeNodeMetrics(self):
        return self._ComputeNodeMetrics

    @ComputeNodeMetrics.setter
    def ComputeNodeMetrics(self, ComputeNodeMetrics):
        self._ComputeNodeMetrics = ComputeNodeMetrics

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def NextAction(self):
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def AttachedComputeNodeCount(self):
        return self._AttachedComputeNodeCount

    @AttachedComputeNodeCount.setter
    def AttachedComputeNodeCount(self, AttachedComputeNodeCount):
        self._AttachedComputeNodeCount = AttachedComputeNodeCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeMetrics") is not None:
            self._ComputeNodeMetrics = ComputeNodeMetrics()
            self._ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self._EnvType = params.get("EnvType")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._ResourceType = params.get("ResourceType")
        self._NextAction = params.get("NextAction")
        self._AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNode(AbstractModel):
    """计算节点

    """

    def __init__(self):
        r"""
        :param _ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        :param _ComputeNodeInstanceId: 计算节点实例ID，对于CVM场景，即为CVM的InstanceId
        :type ComputeNodeInstanceId: str
        :param _ComputeNodeState: 计算节点状态
        :type ComputeNodeState: str
        :param _Cpu: CPU核数
        :type Cpu: int
        :param _Mem: 内存容量，单位GiB
        :type Mem: int
        :param _ResourceCreatedTime: 资源创建完成时间
        :type ResourceCreatedTime: str
        :param _TaskInstanceNumAvailable: 计算节点运行  TaskInstance 可用容量。0表示计算节点忙碌。
        :type TaskInstanceNumAvailable: int
        :param _AgentVersion: Batch Agent 版本
        :type AgentVersion: str
        :param _PrivateIpAddresses: 实例内网IP
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: 实例公网IP
        :type PublicIpAddresses: list of str
        :param _ResourceType: 计算环境资源类型，当前为CVM和CPM（黑石）
        :type ResourceType: str
        :param _ResourceOrigin: 计算环境资源来源。<br>BATCH_CREATED：由批量计算创建的实例资源。<br>
USER_ATTACHED：用户添加到计算环境中的实例资源。
        :type ResourceOrigin: str
        """
        self._ComputeNodeId = None
        self._ComputeNodeInstanceId = None
        self._ComputeNodeState = None
        self._Cpu = None
        self._Mem = None
        self._ResourceCreatedTime = None
        self._TaskInstanceNumAvailable = None
        self._AgentVersion = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._ResourceType = None
        self._ResourceOrigin = None

    @property
    def ComputeNodeId(self):
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId

    @property
    def ComputeNodeInstanceId(self):
        return self._ComputeNodeInstanceId

    @ComputeNodeInstanceId.setter
    def ComputeNodeInstanceId(self, ComputeNodeInstanceId):
        self._ComputeNodeInstanceId = ComputeNodeInstanceId

    @property
    def ComputeNodeState(self):
        return self._ComputeNodeState

    @ComputeNodeState.setter
    def ComputeNodeState(self, ComputeNodeState):
        self._ComputeNodeState = ComputeNodeState

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def ResourceCreatedTime(self):
        return self._ResourceCreatedTime

    @ResourceCreatedTime.setter
    def ResourceCreatedTime(self, ResourceCreatedTime):
        self._ResourceCreatedTime = ResourceCreatedTime

    @property
    def TaskInstanceNumAvailable(self):
        return self._TaskInstanceNumAvailable

    @TaskInstanceNumAvailable.setter
    def TaskInstanceNumAvailable(self, TaskInstanceNumAvailable):
        self._TaskInstanceNumAvailable = TaskInstanceNumAvailable

    @property
    def AgentVersion(self):
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceOrigin(self):
        return self._ResourceOrigin

    @ResourceOrigin.setter
    def ResourceOrigin(self, ResourceOrigin):
        self._ResourceOrigin = ResourceOrigin


    def _deserialize(self, params):
        self._ComputeNodeId = params.get("ComputeNodeId")
        self._ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self._ComputeNodeState = params.get("ComputeNodeState")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._ResourceCreatedTime = params.get("ResourceCreatedTime")
        self._TaskInstanceNumAvailable = params.get("TaskInstanceNumAvailable")
        self._AgentVersion = params.get("AgentVersion")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._ResourceType = params.get("ResourceType")
        self._ResourceOrigin = params.get("ResourceOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeMetrics(AbstractModel):
    """计算节点统计指标

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: 已经完成提交的计算节点数量
        :type SubmittedCount: int
        :param _CreatingCount: 创建中的计算节点数量
        :type CreatingCount: int
        :param _CreationFailedCount: 创建失败的计算节点数量
        :type CreationFailedCount: int
        :param _CreatedCount: 完成创建的计算节点数量
        :type CreatedCount: int
        :param _RunningCount: 运行中的计算节点数量
        :type RunningCount: int
        :param _DeletingCount: 销毁中的计算节点数量
        :type DeletingCount: int
        :param _AbnormalCount: 异常的计算节点数量
        :type AbnormalCount: int
        """
        self._SubmittedCount = None
        self._CreatingCount = None
        self._CreationFailedCount = None
        self._CreatedCount = None
        self._RunningCount = None
        self._DeletingCount = None
        self._AbnormalCount = None

    @property
    def SubmittedCount(self):
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def CreatingCount(self):
        return self._CreatingCount

    @CreatingCount.setter
    def CreatingCount(self, CreatingCount):
        self._CreatingCount = CreatingCount

    @property
    def CreationFailedCount(self):
        return self._CreationFailedCount

    @CreationFailedCount.setter
    def CreationFailedCount(self, CreationFailedCount):
        self._CreationFailedCount = CreationFailedCount

    @property
    def CreatedCount(self):
        return self._CreatedCount

    @CreatedCount.setter
    def CreatedCount(self, CreatedCount):
        self._CreatedCount = CreatedCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def DeletingCount(self):
        return self._DeletingCount

    @DeletingCount.setter
    def DeletingCount(self, DeletingCount):
        self._DeletingCount = DeletingCount

    @property
    def AbnormalCount(self):
        return self._AbnormalCount

    @AbnormalCount.setter
    def AbnormalCount(self, AbnormalCount):
        self._AbnormalCount = AbnormalCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._CreatingCount = params.get("CreatingCount")
        self._CreationFailedCount = params.get("CreationFailedCount")
        self._CreatedCount = params.get("CreatedCount")
        self._RunningCount = params.get("RunningCount")
        self._DeletingCount = params.get("DeletingCount")
        self._AbnormalCount = params.get("AbnormalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CpmVirtualPrivateCloud(AbstractModel):
    """黑石私有网络

    """

    def __init__(self):
        r"""
        :param _VpcId: 黑石私有网络ID
        :type VpcId: str
        :param _SubnetId: 黑石子网ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvRequest(AbstractModel):
    """CreateComputeEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ComputeEnv: 计算环境信息
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`
        :param _Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        """
        self._ComputeEnv = None
        self._Placement = None
        self._ClientToken = None

    @property
    def ComputeEnv(self):
        return self._ComputeEnv

    @ComputeEnv.setter
    def ComputeEnv(self, ComputeEnv):
        self._ComputeEnv = ComputeEnv

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self._ComputeEnv = NamedComputeEnv()
            self._ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvResponse(AbstractModel):
    """CreateComputeEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateCpmComputeEnvRequest(AbstractModel):
    """CreateCpmComputeEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ComputeEnv: 计算环境信息
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedCpmComputeEnv`
        :param _Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        """
        self._ComputeEnv = None
        self._Placement = None
        self._ClientToken = None

    @property
    def ComputeEnv(self):
        return self._ComputeEnv

    @ComputeEnv.setter
    def ComputeEnv(self, ComputeEnv):
        self._ComputeEnv = ComputeEnv

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self._ComputeEnv = NamedCpmComputeEnv()
            self._ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCpmComputeEnvResponse(AbstractModel):
    """CreateCpmComputeEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param _TaskTemplateInfo: 任务模板内容，参数要求与任务一致
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param _TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        :param _Tags: 标签列表。通过指定该参数可以支持绑定标签到任务模板。每个任务模板最多绑定10个标签。
        :type Tags: list of Tag
        """
        self._TaskTemplateName = None
        self._TaskTemplateInfo = None
        self._TaskTemplateDescription = None
        self._Tags = None

    @property
    def TaskTemplateName(self):
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateInfo(self):
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo

    @property
    def TaskTemplateDescription(self):
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskTemplateName = params.get("TaskTemplateName")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskTemplateResponse(AbstractModel):
    """CreateTaskTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskTemplateId = None
        self._RequestId = None

    @property
    def TaskTemplateId(self):
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param _DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><li>CLOUD_BSSD：通用型SSD云硬盘<br><br>默认取值：LOCAL_BASIC。<br><br>该参数对`ResizeInstanceDisk`接口无效。
        :type DiskType: str
        :param _DiskId: 数据盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID，暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param _DeleteWithInstance: 数据盘是否随子机销毁。取值范围：
<li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘
<li>FALSE：子机销毁时，保留数据盘<br>
默认取值：TRUE<br>
该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _SnapshotId: 数据盘快照ID。选择的数据盘快照大小需小于数据盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _Encrypt: 数据盘是加密。取值范围：
<li>true：加密
<li>false：不加密<br>
默认取值：false<br>
该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        :param _KmsKeyId: 自定义CMK对应的ID，取值为UUID或者类似kms-abcd1234。用于加密云盘。

该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param _ThroughputPerformance: 云硬盘性能，单位：MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param _CdcId: 所属的独享集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskId = None
        self._DeleteWithInstance = None
        self._SnapshotId = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._ThroughputPerformance = None
        self._CdcId = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._SnapshotId = params.get("SnapshotId")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvRequest(AbstractModel):
    """DeleteComputeEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvResponse(AbstractModel):
    """DeleteComputeEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateIds: 用于删除任务模板信息
        :type TaskTemplateIds: list of str
        """
        self._TaskTemplateIds = None

    @property
    def TaskTemplateIds(self):
        return self._TaskTemplateIds

    @TaskTemplateIds.setter
    def TaskTemplateIds(self, TaskTemplateIds):
        self._TaskTemplateIds = TaskTemplateIds


    def _deserialize(self, params):
        self._TaskTemplateIds = params.get("TaskTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskTemplatesResponse(AbstractModel):
    """DeleteTaskTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """依赖关系

    """

    def __init__(self):
        r"""
        :param _StartTask: 依赖关系的起点任务名称
        :type StartTask: str
        :param _EndTask: 依赖关系的终点任务名称
        :type EndTask: str
        """
        self._StartTask = None
        self._EndTask = None

    @property
    def StartTask(self):
        return self._StartTask

    @StartTask.setter
    def StartTask(self, StartTask):
        self._StartTask = StartTask

    @property
    def EndTask(self):
        return self._EndTask

    @EndTask.setter
    def EndTask(self, EndTask):
        self._EndTask = EndTask


    def _deserialize(self, params):
        self._StartTask = params.get("StartTask")
        self._EndTask = params.get("EndTask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableCvmInstanceTypesRequest(AbstractModel):
    """DescribeAvailableCvmInstanceTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> instance-family String - 是否必填：否 -（过滤条件）按照机型系列过滤。实例机型系列形如：S1、I1、M1等。</li>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeAvailableCvmInstanceTypesResponse(AbstractModel):
    """DescribeAvailableCvmInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeConfigSet: 机型配置数组
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeConfigSet = None
        self._RequestId = None

    @property
    def InstanceTypeConfigSet(self):
        return self._InstanceTypeConfigSet

    @InstanceTypeConfigSet.setter
    def InstanceTypeConfigSet(self, InstanceTypeConfigSet):
        self._InstanceTypeConfigSet = InstanceTypeConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self._InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self._InstanceTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvActivitiesRequest(AbstractModel):
    """DescribeComputeEnvActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _Filters: 过滤条件
<li> compute-node-id - String - 是否必填：否 -（过滤条件）按照计算节点ID过滤。</li>
        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        self._EnvId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
        self._EnvId = params.get("EnvId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = Filter()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvActivitiesResponse(AbstractModel):
    """DescribeComputeEnvActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivitySet: 计算环境中的活动列表
        :type ActivitySet: list of Activity
        :param _TotalCount: 活动数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivitySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ActivitySet(self):
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

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
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfoRequest(AbstractModel):
    """DescribeComputeEnvCreateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvCreateInfoResponse(AbstractModel):
    """DescribeComputeEnvCreateInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境 ID
        :type EnvId: str
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _EnvDescription: 计算环境描述
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvDescription: str
        :param _EnvType: 计算环境类型，仅支持“MANAGED”类型
        :type EnvType: str
        :param _EnvData: 计算环境参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param _InputMappings: 输入映射
        :type InputMappings: list of InputMapping
        :param _Authentications: 授权信息
        :type Authentications: list of Authentication
        :param _Notifications: 通知信息
        :type Notifications: list of Notification
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _Tags: 计算环境绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._InputMappings = None
        self._Authentications = None
        self._Notifications = None
        self._DesiredComputeNodeCount = None
        self._Tags = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def InputMappings(self):
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def Authentications(self):
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def Notifications(self):
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfosRequest(AbstractModel):
    """DescribeComputeEnvCreateInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvIds: 计算环境ID列表，与Filters参数不能同时指定。
        :type EnvIds: list of str
        :param _Filters: 过滤条件
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>
<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>
与EnvIds参数不能同时指定。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._EnvIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EnvIds(self):
        return self._EnvIds

    @EnvIds.setter
    def EnvIds(self, EnvIds):
        self._EnvIds = EnvIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvCreateInfosResponse(AbstractModel):
    """DescribeComputeEnvCreateInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 计算环境数量
        :type TotalCount: int
        :param _ComputeEnvCreateInfoSet: 计算环境创建信息列表
        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ComputeEnvCreateInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ComputeEnvCreateInfoSet(self):
        return self._ComputeEnvCreateInfoSet

    @ComputeEnvCreateInfoSet.setter
    def ComputeEnvCreateInfoSet(self, ComputeEnvCreateInfoSet):
        self._ComputeEnvCreateInfoSet = ComputeEnvCreateInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ComputeEnvCreateInfoSet") is not None:
            self._ComputeEnvCreateInfoSet = []
            for item in params.get("ComputeEnvCreateInfoSet"):
                obj = ComputeEnvCreateInfo()
                obj._deserialize(item)
                self._ComputeEnvCreateInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvRequest(AbstractModel):
    """DescribeComputeEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvResponse(AbstractModel):
    """DescribeComputeEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: 计算环境创建时间
        :type CreateTime: str
        :param _ComputeNodeSet: 计算节点列表信息
        :type ComputeNodeSet: list of ComputeNode
        :param _ComputeNodeMetrics: 计算节点统计指标
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _EnvType: 计算环境类型
        :type EnvType: str
        :param _ResourceType: 计算环境资源类型，当前为CVM和CPM（黑石）
        :type ResourceType: str
        :param _NextAction: 下一步动作
        :type NextAction: str
        :param _AttachedComputeNodeCount: 用户添加到计算环境中的计算节点个数
        :type AttachedComputeNodeCount: int
        :param _Tags: 计算环境绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._EnvName = None
        self._Placement = None
        self._CreateTime = None
        self._ComputeNodeSet = None
        self._ComputeNodeMetrics = None
        self._DesiredComputeNodeCount = None
        self._EnvType = None
        self._ResourceType = None
        self._NextAction = None
        self._AttachedComputeNodeCount = None
        self._Tags = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ComputeNodeSet(self):
        return self._ComputeNodeSet

    @ComputeNodeSet.setter
    def ComputeNodeSet(self, ComputeNodeSet):
        self._ComputeNodeSet = ComputeNodeSet

    @property
    def ComputeNodeMetrics(self):
        return self._ComputeNodeMetrics

    @ComputeNodeMetrics.setter
    def ComputeNodeMetrics(self, ComputeNodeMetrics):
        self._ComputeNodeMetrics = ComputeNodeMetrics

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def NextAction(self):
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def AttachedComputeNodeCount(self):
        return self._AttachedComputeNodeCount

    @AttachedComputeNodeCount.setter
    def AttachedComputeNodeCount(self, AttachedComputeNodeCount):
        self._AttachedComputeNodeCount = AttachedComputeNodeCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeSet") is not None:
            self._ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNode()
                obj._deserialize(item)
                self._ComputeNodeSet.append(obj)
        if params.get("ComputeNodeMetrics") is not None:
            self._ComputeNodeMetrics = ComputeNodeMetrics()
            self._ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvType = params.get("EnvType")
        self._ResourceType = params.get("ResourceType")
        self._NextAction = params.get("NextAction")
        self._AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvsRequest(AbstractModel):
    """DescribeComputeEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvIds: 计算环境ID列表，与Filters参数不能同时指定。
        :type EnvIds: list of str
        :param _Filters: 过滤条件
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>
<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>
<li> resource-type - String - 是否必填：否 -（过滤条件）按照计算资源类型过滤，取值CVM或者CPM(黑石)。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li>tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。</li>
与EnvIds参数不能同时指定。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._EnvIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EnvIds(self):
        return self._EnvIds

    @EnvIds.setter
    def EnvIds(self, EnvIds):
        self._EnvIds = EnvIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvsResponse(AbstractModel):
    """DescribeComputeEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ComputeEnvSet: 计算环境列表
        :type ComputeEnvSet: list of ComputeEnvView
        :param _TotalCount: 计算环境数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ComputeEnvSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ComputeEnvSet(self):
        return self._ComputeEnvSet

    @ComputeEnvSet.setter
    def ComputeEnvSet(self, ComputeEnvSet):
        self._ComputeEnvSet = ComputeEnvSet

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
        if params.get("ComputeEnvSet") is not None:
            self._ComputeEnvSet = []
            for item in params.get("ComputeEnvSet"):
                obj = ComputeEnvView()
                obj._deserialize(item)
                self._ComputeEnvSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCpmOsInfoRequest(AbstractModel):
    """DescribeCpmOsInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceClassCode: 黑石设备类型代号。 可以从[DescribeDeviceClass](https://cloud.tencent.com/document/api/386/32911)查询设备类型列表。
        :type DeviceClassCode: str
        """
        self._DeviceClassCode = None

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode


    def _deserialize(self, params):
        self._DeviceClassCode = params.get("DeviceClassCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCpmOsInfoResponse(AbstractModel):
    """DescribeCpmOsInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OsInfoSet: 操作系统信息列表。
        :type OsInfoSet: list of OsInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OsInfoSet = None
        self._RequestId = None

    @property
    def OsInfoSet(self):
        return self._OsInfoSet

    @OsInfoSet.setter
    def OsInfoSet(self, OsInfoSet):
        self._OsInfoSet = OsInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OsInfoSet") is not None:
            self._OsInfoSet = []
            for item in params.get("OsInfoSet"):
                obj = OsInfo()
                obj._deserialize(item)
                self._OsInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCvmZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> instance-family String - 是否必填：否 -（过滤条件）按照机型系列过滤。实例机型系列形如：S1、I1、M1等。</li>
<li> instance-type - String - 是否必填：否 - （过滤条件）按照机型过滤。</li>
<li> instance-charge-type - String - 是否必填：否 -（过滤条件）按照实例计费模式过滤。 ( POSTPAID_BY_HOUR：表示后付费，即按量计费机型 | SPOTPAID：表示竞价付费机型。 )  </li>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeCvmZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeQuotaSet: 可用区机型配置列表。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeQuotaSet = None
        self._RequestId = None

    @property
    def InstanceTypeQuotaSet(self):
        return self._InstanceTypeQuotaSet

    @InstanceTypeQuotaSet.setter
    def InstanceTypeQuotaSet(self, InstanceTypeQuotaSet):
        self._InstanceTypeQuotaSet = InstanceTypeQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self._InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self._InstanceTypeQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceCategoriesRequest(AbstractModel):
    """DescribeInstanceCategories请求参数结构体

    """


class DescribeInstanceCategoriesResponse(AbstractModel):
    """DescribeInstanceCategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceCategorySet: CVM实例分类列表
        :type InstanceCategorySet: list of InstanceCategoryItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceCategorySet = None
        self._RequestId = None

    @property
    def InstanceCategorySet(self):
        return self._InstanceCategorySet

    @InstanceCategorySet.setter
    def InstanceCategorySet(self, InstanceCategorySet):
        self._InstanceCategorySet = InstanceCategorySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceCategorySet") is not None:
            self._InstanceCategorySet = []
            for item in params.get("InstanceCategorySet"):
                obj = InstanceCategoryItem()
                obj._deserialize(item)
                self._InstanceCategorySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业标识
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _JobName: 作业名称
        :type JobName: str
        :param _Zone: 可用区信息
        :type Zone: str
        :param _Priority: 作业优先级
        :type Priority: int
        :param _JobState: 作业状态
        :type JobState: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _TaskSet: 任务视图信息
        :type TaskSet: list of TaskView
        :param _DependenceSet: 任务间依赖信息
        :type DependenceSet: list of Dependence
        :param _TaskMetrics: 任务统计指标
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param _TaskInstanceMetrics: 任务实例统计指标
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param _StateReason: 作业失败原因
        :type StateReason: str
        :param _Tags: 作业绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _NextAction: 下一步动作
注意：此字段可能返回 null，表示取不到有效值。
        :type NextAction: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._Zone = None
        self._Priority = None
        self._JobState = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskSet = None
        self._DependenceSet = None
        self._TaskMetrics = None
        self._TaskInstanceMetrics = None
        self._StateReason = None
        self._Tags = None
        self._NextAction = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def JobState(self):
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskSet(self):
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def DependenceSet(self):
        return self._DependenceSet

    @DependenceSet.setter
    def DependenceSet(self, DependenceSet):
        self._DependenceSet = DependenceSet

    @property
    def TaskMetrics(self):
        return self._TaskMetrics

    @TaskMetrics.setter
    def TaskMetrics(self, TaskMetrics):
        self._TaskMetrics = TaskMetrics

    @property
    def TaskInstanceMetrics(self):
        return self._TaskInstanceMetrics

    @TaskInstanceMetrics.setter
    def TaskInstanceMetrics(self, TaskInstanceMetrics):
        self._TaskInstanceMetrics = TaskInstanceMetrics

    @property
    def StateReason(self):
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextAction(self):
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Zone = params.get("Zone")
        self._Priority = params.get("Priority")
        self._JobState = params.get("JobState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskView()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        if params.get("DependenceSet") is not None:
            self._DependenceSet = []
            for item in params.get("DependenceSet"):
                obj = Dependence()
                obj._deserialize(item)
                self._DependenceSet.append(obj)
        if params.get("TaskMetrics") is not None:
            self._TaskMetrics = TaskMetrics()
            self._TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("TaskInstanceMetrics") is not None:
            self._TaskInstanceMetrics = TaskInstanceMetrics()
            self._TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self._StateReason = params.get("StateReason")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextAction = params.get("NextAction")
        self._RequestId = params.get("RequestId")


class DescribeJobSubmitInfoRequest(AbstractModel):
    """DescribeJobSubmitInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobSubmitInfoResponse(AbstractModel):
    """DescribeJobSubmitInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _JobName: 作业名称
        :type JobName: str
        :param _JobDescription: 作业描述
        :type JobDescription: str
        :param _Priority: 作业优先级，任务（Task）和任务实例（TaskInstance）会继承作业优先级
        :type Priority: int
        :param _Tasks: 任务信息
        :type Tasks: list of Task
        :param _Dependences: 依赖信息
        :type Dependences: list of Dependence
        :param _Tags: 作业绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._JobDescription = None
        self._Priority = None
        self._Tasks = None
        self._Dependences = None
        self._Tags = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobDescription(self):
        return self._JobDescription

    @JobDescription.setter
    def JobDescription(self, JobDescription):
        self._JobDescription = JobDescription

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Dependences(self):
        return self._Dependences

    @Dependences.setter
    def Dependences(self, Dependences):
        self._Dependences = Dependences

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobDescription = params.get("JobDescription")
        self._Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("Dependences") is not None:
            self._Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self._Dependences.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 作业ID列表，与Filters参数不能同时指定。
        :type JobIds: list of str
        :param _Filters: 过滤条件
<li> job-id - String - 是否必填：否 -（过滤条件）按照作业ID过滤。</li>
<li> job-name - String - 是否必填：否 -（过滤条件）按照作业名称过滤。</li>
<li> job-state - String - 是否必填：否 -（过滤条件）按照作业状态过滤。</li>
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。</li>
与JobIds参数不能同时指定。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._JobIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobSet: 作业列表
        :type JobSet: list of JobView
        :param _TotalCount: 符合条件的作业数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def JobSet(self):
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

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
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = JobView()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogsRequest(AbstractModel):
    """DescribeTaskLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskInstanceIndexes: 任务实例集合
        :type TaskInstanceIndexes: list of int non-negative
        :param _Offset: 起始任务实例
        :type Offset: int
        :param _Limit: 最大任务实例数
        :type Limit: int
        """
        self._JobId = None
        self._TaskName = None
        self._TaskInstanceIndexes = None
        self._Offset = None
        self._Limit = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceIndexes(self):
        return self._TaskInstanceIndexes

    @TaskInstanceIndexes.setter
    def TaskInstanceIndexes(self, TaskInstanceIndexes):
        self._TaskInstanceIndexes = TaskInstanceIndexes

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


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskInstanceIndexes = params.get("TaskInstanceIndexes")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogsResponse(AbstractModel):
    """DescribeTaskLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务实例总数
        :type TotalCount: int
        :param _TaskInstanceLogSet: 任务实例日志详情集合
        :type TaskInstanceLogSet: list of TaskInstanceLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInstanceLogSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInstanceLogSet(self):
        return self._TaskInstanceLogSet

    @TaskInstanceLogSet.setter
    def TaskInstanceLogSet(self, TaskInstanceLogSet):
        self._TaskInstanceLogSet = TaskInstanceLogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInstanceLogSet") is not None:
            self._TaskInstanceLogSet = []
            for item in params.get("TaskInstanceLogSet"):
                obj = TaskInstanceLog()
                obj._deserialize(item)
                self._TaskInstanceLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量。默认取值100，最大取值1000。
        :type Limit: int
        :param _Filters: 过滤条件，详情如下：
<li> task-instance-type - String - 是否必填： 否 - 按照任务实例状态进行过滤（SUBMITTED：已提交；PENDING：等待中；RUNNABLE：可运行；STARTING：启动中；RUNNING：运行中；SUCCEED：成功；FAILED：失败；FAILED_INTERRUPTED：失败后保留实例）。</li>
        :type Filters: list of Filter
        """
        self._JobId = None
        self._TaskName = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

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
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
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
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskState: 任务状态
        :type TaskState: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _TaskInstanceTotalCount: 任务实例总数
        :type TaskInstanceTotalCount: int
        :param _TaskInstanceSet: 任务实例信息
        :type TaskInstanceSet: list of TaskInstanceView
        :param _TaskInstanceMetrics: 任务实例统计指标
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._TaskName = None
        self._TaskState = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskInstanceTotalCount = None
        self._TaskInstanceSet = None
        self._TaskInstanceMetrics = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskState(self):
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskInstanceTotalCount(self):
        return self._TaskInstanceTotalCount

    @TaskInstanceTotalCount.setter
    def TaskInstanceTotalCount(self, TaskInstanceTotalCount):
        self._TaskInstanceTotalCount = TaskInstanceTotalCount

    @property
    def TaskInstanceSet(self):
        return self._TaskInstanceSet

    @TaskInstanceSet.setter
    def TaskInstanceSet(self, TaskInstanceSet):
        self._TaskInstanceSet = TaskInstanceSet

    @property
    def TaskInstanceMetrics(self):
        return self._TaskInstanceMetrics

    @TaskInstanceMetrics.setter
    def TaskInstanceMetrics(self, TaskInstanceMetrics):
        self._TaskInstanceMetrics = TaskInstanceMetrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskState = params.get("TaskState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._TaskInstanceTotalCount = params.get("TaskInstanceTotalCount")
        if params.get("TaskInstanceSet") is not None:
            self._TaskInstanceSet = []
            for item in params.get("TaskInstanceSet"):
                obj = TaskInstanceView()
                obj._deserialize(item)
                self._TaskInstanceSet.append(obj)
        if params.get("TaskInstanceMetrics") is not None:
            self._TaskInstanceMetrics = TaskInstanceMetrics()
            self._TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self._RequestId = params.get("RequestId")


class DescribeTaskTemplatesRequest(AbstractModel):
    """DescribeTaskTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateIds: 任务模板ID列表，与Filters参数不能同时指定。
        :type TaskTemplateIds: list of str
        :param _Filters: 过滤条件
<li> task-template-name - String - 是否必填：否 -（过滤条件）按照任务模板名称过滤。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。</li>
与TaskTemplateIds参数不能同时指定。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._TaskTemplateIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TaskTemplateIds(self):
        return self._TaskTemplateIds

    @TaskTemplateIds.setter
    def TaskTemplateIds(self, TaskTemplateIds):
        self._TaskTemplateIds = TaskTemplateIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._TaskTemplateIds = params.get("TaskTemplateIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskTemplatesResponse(AbstractModel):
    """DescribeTaskTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateSet: 任务模板列表
        :type TaskTemplateSet: list of TaskTemplateView
        :param _TotalCount: 任务模板数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskTemplateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TaskTemplateSet(self):
        return self._TaskTemplateSet

    @TaskTemplateSet.setter
    def TaskTemplateSet(self, TaskTemplateSet):
        self._TaskTemplateSet = TaskTemplateSet

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
        if params.get("TaskTemplateSet") is not None:
            self._TaskTemplateSet = []
            for item in params.get("TaskTemplateSet"):
                obj = TaskTemplateView()
                obj._deserialize(item)
                self._TaskTemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        """
        self._EnvId = None
        self._InstanceIds = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachInstancesResponse(AbstractModel):
    """DetachInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker容器信息

    """

    def __init__(self):
        r"""
        :param _User: Docker Hub 用户名或 Tencent Registry 用户名
        :type User: str
        :param _Password: Docker Hub 密码或 Tencent Registry 密码
        :type Password: str
        :param _Image: Docker Hub填写“[user/repo]:[tag]”，Tencent Registry填写“ccr.ccs.tencentyun.com/[namespace/repo]:[tag]”
        :type Image: str
        :param _Server: Docker Hub 可以不填，但确保具有公网访问能力。或者是 Tencent Registry 服务地址“ccr.ccs.tencentyun.com”
        :type Server: str
        :param _MaxRetryCount: 拉取Docker镜像重试次数。默认值：0。
        :type MaxRetryCount: int
        :param _DelayOnRetry: 拉取Docker镜像失败时延迟时间。单位：秒。
        :type DelayOnRetry: int
        :param _DockerRunOption: Docker命令运行参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerRunOption: str
        """
        self._User = None
        self._Password = None
        self._Image = None
        self._Server = None
        self._MaxRetryCount = None
        self._DelayOnRetry = None
        self._DockerRunOption = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def MaxRetryCount(self):
        return self._MaxRetryCount

    @MaxRetryCount.setter
    def MaxRetryCount(self, MaxRetryCount):
        self._MaxRetryCount = MaxRetryCount

    @property
    def DelayOnRetry(self):
        return self._DelayOnRetry

    @DelayOnRetry.setter
    def DelayOnRetry(self, DelayOnRetry):
        self._DelayOnRetry = DelayOnRetry

    @property
    def DockerRunOption(self):
        return self._DockerRunOption

    @DockerRunOption.setter
    def DockerRunOption(self, DockerRunOption):
        self._DockerRunOption = DockerRunOption


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Image = params.get("Image")
        self._Server = params.get("Server")
        self._MaxRetryCount = params.get("MaxRetryCount")
        self._DelayOnRetry = params.get("DelayOnRetry")
        self._DockerRunOption = params.get("DockerRunOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        r"""
        :param _SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        :param _MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`
        :param _AutomationService: 开启云自动化助手服务（TencentCloud Automation Tools，TAT）。若不指定该参数，则公共镜像默认开启云自动化助手服务，其他镜像默认不开启云自动化助手服务。
        :type AutomationService: :class:`tencentcloud.batch.v20170312.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None

    @property
    def SecurityService(self):
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = RunAutomationServiceEnabled()
            self._AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvData(AbstractModel):
    """计算环境数据

    """

    def __init__(self):
        r"""
        :param _InstanceType: CVM实例类型，不能与InstanceTypes和InstanceTypeOptions同时出现。
        :type InstanceType: str
        :param _ImageId: CVM镜像ID
        :type ImageId: str
        :param _SystemDisk: 实例系统盘配置信息
        :type SystemDisk: :class:`tencentcloud.batch.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息配置，与Zones和VirtualPrivateClouds不能同时指定。
        :type VirtualPrivateCloud: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`
        :param _InstanceName: CVM实例显示名称
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.batch.v20170312.models.EnhancedService`
        :param _InstanceChargeType: CVM实例计费类型<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数
        :type InstanceMarketOptions: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: CVM实例类型列表，不能与InstanceType和InstanceTypeOptions同时出现。指定该字段后，计算节点按照机型先后顺序依次尝试创建，直到实例创建成功，结束遍历过程。最多支持10个机型。
        :type InstanceTypes: list of str
        :param _InstanceTypeOptions: CVM实例机型配置。不能与InstanceType和InstanceTypes同时出现。
        :type InstanceTypeOptions: :class:`tencentcloud.batch.v20170312.models.InstanceTypeOptions`
        :param _Zones: 可用区列表，支持跨可用区创建CVM实例。与VirtualPrivateCloud和VirtualPrivateClouds不能同时指定。
        :type Zones: list of str
        :param _VirtualPrivateClouds: 私有网络列表，支持跨私有网络创建CVM实例。与VirtualPrivateCloud和Zones不能同时指定。
        :type VirtualPrivateClouds: list of VirtualPrivateCloud
        """
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._InstanceTypeOptions = None
        self._Zones = None
        self._VirtualPrivateClouds = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTypeOptions(self):
        return self._InstanceTypeOptions

    @InstanceTypeOptions.setter
    def InstanceTypeOptions(self, InstanceTypeOptions):
        self._InstanceTypeOptions = InstanceTypeOptions

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def VirtualPrivateClouds(self):
        return self._VirtualPrivateClouds

    @VirtualPrivateClouds.setter
    def VirtualPrivateClouds(self, VirtualPrivateClouds):
        self._VirtualPrivateClouds = VirtualPrivateClouds


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTypeOptions") is not None:
            self._InstanceTypeOptions = InstanceTypeOptions()
            self._InstanceTypeOptions._deserialize(params.get("InstanceTypeOptions"))
        self._Zones = params.get("Zones")
        if params.get("VirtualPrivateClouds") is not None:
            self._VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = VirtualPrivateCloud()
                obj._deserialize(item)
                self._VirtualPrivateClouds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvDataCpm(AbstractModel):
    """黑石计算环境数据

    """

    def __init__(self):
        r"""
        :param _Zones: 黑石可用区名称列表。如ap-guangzhou-bls-1, 可通过黑石接口[DescribeRegions]( https://cloud.tencent.com/document/api/386/33564)接口获取。不是Batch可用区名称。目前仅支持一个可用区名称。
        :type Zones: list of str
        :param _InstanceTypes: 购买的机型ID。通过黑石接口[DescribeDeviceClass]( https://cloud.tencent.com/document/api/386/32911)查询设备型号，获取机型信息。
        :type InstanceTypes: list of str
        :param _TimeUnit: 购买时长单位，取值：m(月)。
        :type TimeUnit: str
        :param _TimeSpan: 购买时长。
        :type TimeSpan: int
        :param _RaidId: RAID类型ID。通过黑石接口[DescribeDeviceClassPartition]( https://cloud.tencent.com/document/api/386/32910)查询机型RAID方式以及系统盘大小，获取RAID信息。
        :type RaidId: int
        :param _OsTypeId: 部署服务器的操作系统ID。通过批量计算接口DescribeCpmOsInfo查询操作系统信息。
        :type OsTypeId: int
        :param _VirtualPrivateClouds: 黑石VPC列表，目前仅支持一个VPC。
        :type VirtualPrivateClouds: list of CpmVirtualPrivateCloud
        :param _NeedSecurityAgent: 是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0。
        :type NeedSecurityAgent: int
        :param _NeedMonitorAgent: 是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0。
        :type NeedMonitorAgent: int
        :param _AutoRenewFlag: 自动续费标志位，取值：1(自动续费) 0(不自动续费)，默认取值0。
        :type AutoRenewFlag: int
        :param _IsZoning: 数据盘是否格式化，取值：1(格式化) 0(不格式化)，默认取值为1。
        :type IsZoning: int
        :param _FileSystem: 指定数据盘的文件系统格式，当前支持 ext4和xfs选项， 默认为ext4。 参数适用于数据盘和Linux， 且在IsZoning为1时生效。
        :type FileSystem: str
        :param _Password: 设置Linux root或Windows Administrator的密码。若不设置此参数，默认情况下会随机生成密码，并以站内信方式通知到用户。
        :type Password: str
        :param _ApplyEip: 是否分配弹性公网IP，取值：1(分配) 0(不分配)，默认取值0。
        :type ApplyEip: int
        :param _EipPayMode: 弹性公网IP计费模式，取值：flow(按流量计费) bandwidth(按带宽计费)，默认取值flow。
        :type EipPayMode: str
        :param _EipBandwidth: 弹性公网IP带宽限制，单位Mb。
        :type EipBandwidth: int
        :param _ImageId: 自定义镜像ID，取值生效时用自定义镜像部署物理机。
        :type ImageId: str
        :param _SysRootSpace: 系统盘根分区大小，单位为G，默认取值10G。通过黑石接口[DescribeDeviceClassPartition]( https://cloud.tencent.com/document/api/386/32910)查询机型RAID方式以及系统盘大小，获取根分区信息。
        :type SysRootSpace: int
        :param _SysDataSpace: /data分区大小，单位为G。如果系统盘还有剩余大小，会分配给/data分区。（特殊情况：如果剩余空间不足10G，并且没有指定/data分区，则剩余空间会分配给Root分区）。
        :type SysDataSpace: int
        :param _HyperThreading: 是否开启超线程，取值：1(开启) 0(关闭)，默认取值1。
        :type HyperThreading: int
        :param _LanIps: 指定的内网IP列表，不指定时自动分配。
        :type LanIps: list of str
        """
        self._Zones = None
        self._InstanceTypes = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RaidId = None
        self._OsTypeId = None
        self._VirtualPrivateClouds = None
        self._NeedSecurityAgent = None
        self._NeedMonitorAgent = None
        self._AutoRenewFlag = None
        self._IsZoning = None
        self._FileSystem = None
        self._Password = None
        self._ApplyEip = None
        self._EipPayMode = None
        self._EipBandwidth = None
        self._ImageId = None
        self._SysRootSpace = None
        self._SysDataSpace = None
        self._HyperThreading = None
        self._LanIps = None

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def RaidId(self):
        return self._RaidId

    @RaidId.setter
    def RaidId(self, RaidId):
        self._RaidId = RaidId

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def VirtualPrivateClouds(self):
        return self._VirtualPrivateClouds

    @VirtualPrivateClouds.setter
    def VirtualPrivateClouds(self, VirtualPrivateClouds):
        self._VirtualPrivateClouds = VirtualPrivateClouds

    @property
    def NeedSecurityAgent(self):
        return self._NeedSecurityAgent

    @NeedSecurityAgent.setter
    def NeedSecurityAgent(self, NeedSecurityAgent):
        self._NeedSecurityAgent = NeedSecurityAgent

    @property
    def NeedMonitorAgent(self):
        return self._NeedMonitorAgent

    @NeedMonitorAgent.setter
    def NeedMonitorAgent(self, NeedMonitorAgent):
        self._NeedMonitorAgent = NeedMonitorAgent

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def IsZoning(self):
        return self._IsZoning

    @IsZoning.setter
    def IsZoning(self, IsZoning):
        self._IsZoning = IsZoning

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ApplyEip(self):
        return self._ApplyEip

    @ApplyEip.setter
    def ApplyEip(self, ApplyEip):
        self._ApplyEip = ApplyEip

    @property
    def EipPayMode(self):
        return self._EipPayMode

    @EipPayMode.setter
    def EipPayMode(self, EipPayMode):
        self._EipPayMode = EipPayMode

    @property
    def EipBandwidth(self):
        return self._EipBandwidth

    @EipBandwidth.setter
    def EipBandwidth(self, EipBandwidth):
        self._EipBandwidth = EipBandwidth

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SysRootSpace(self):
        return self._SysRootSpace

    @SysRootSpace.setter
    def SysRootSpace(self, SysRootSpace):
        self._SysRootSpace = SysRootSpace

    @property
    def SysDataSpace(self):
        return self._SysDataSpace

    @SysDataSpace.setter
    def SysDataSpace(self, SysDataSpace):
        self._SysDataSpace = SysDataSpace

    @property
    def HyperThreading(self):
        return self._HyperThreading

    @HyperThreading.setter
    def HyperThreading(self, HyperThreading):
        self._HyperThreading = HyperThreading

    @property
    def LanIps(self):
        return self._LanIps

    @LanIps.setter
    def LanIps(self, LanIps):
        self._LanIps = LanIps


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._InstanceTypes = params.get("InstanceTypes")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RaidId = params.get("RaidId")
        self._OsTypeId = params.get("OsTypeId")
        if params.get("VirtualPrivateClouds") is not None:
            self._VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = CpmVirtualPrivateCloud()
                obj._deserialize(item)
                self._VirtualPrivateClouds.append(obj)
        self._NeedSecurityAgent = params.get("NeedSecurityAgent")
        self._NeedMonitorAgent = params.get("NeedMonitorAgent")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._IsZoning = params.get("IsZoning")
        self._FileSystem = params.get("FileSystem")
        self._Password = params.get("Password")
        self._ApplyEip = params.get("ApplyEip")
        self._EipPayMode = params.get("EipPayMode")
        self._EipBandwidth = params.get("EipBandwidth")
        self._ImageId = params.get("ImageId")
        self._SysRootSpace = params.get("SysRootSpace")
        self._SysDataSpace = params.get("SysDataSpace")
        self._HyperThreading = params.get("HyperThreading")
        self._LanIps = params.get("LanIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量名称
        :type Name: str
        :param _Value: 环境变量取值
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
        


class EventConfig(AbstractModel):
    """事件配置

    """

    def __init__(self):
        r"""
        :param _EventName: 事件类型，包括：<br/><li>“JOB_RUNNING”：作业运行，适用于"SubmitJob"。</li><li>“JOB_SUCCEED”：作业成功，适用于"SubmitJob"。</li><li>“JOB_FAILED”：作业失败，适用于"SubmitJob"。</li><li>“JOB_FAILED_INTERRUPTED”：作业失败，保留实例，适用于"SubmitJob"。</li><li>“TASK_RUNNING”：任务运行，适用于"SubmitJob"。</li><li>“TASK_SUCCEED”：任务成功，适用于"SubmitJob"。</li><li>“TASK_FAILED”：任务失败，适用于"SubmitJob"。</li><li>“TASK_FAILED_INTERRUPTED”：任务失败，保留实例，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_RUNNING”：任务实例运行，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_SUCCEED”：任务实例成功，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_FAILED”：任务实例失败，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_FAILED_INTERRUPTED”：任务实例失败，保留实例，适用于"SubmitJob"。</li><li>“COMPUTE_ENV_CREATED”：计算环境已创建，适用于"CreateComputeEnv"。</li><li>“COMPUTE_ENV_DELETED”：计算环境已删除，适用于"CreateComputeEnv"。</li><li>“COMPUTE_NODE_CREATED”：计算节点已创建，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_CREATION_FAILED”：计算节点创建失败，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_RUNNING”：计算节点运行中，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_ABNORMAL”：计算节点异常，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_DELETING”：计算节点已删除，适用于"CreateComputeEnv"和"SubmitJob"。</li>
        :type EventName: str
        :param _EventVars: 自定义键值对
        :type EventVars: list of EventVar
        """
        self._EventName = None
        self._EventVars = None

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventVars(self):
        return self._EventVars

    @EventVars.setter
    def EventVars(self, EventVars):
        self._EventVars = EventVars


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        if params.get("EventVars") is not None:
            self._EventVars = []
            for item in params.get("EventVars"):
                obj = EventVar()
                obj._deserialize(item)
                self._EventVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventVar(AbstractModel):
    """自定义键值对

    """

    def __init__(self):
        r"""
        :param _Name: 自定义键
        :type Name: str
        :param _Value: 自定义值
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
        


class Externals(AbstractModel):
    """扩展数据

    """

    def __init__(self):
        r"""
        :param _ReleaseAddress: 释放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseAddress: bool
        :param _UnsupportNetworks: 不支持的网络类型，取值范围：<br><li>BASIC：基础网络<br><li>VPC1.0：私有网络VPC1.0
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsupportNetworks: list of str
        :param _StorageBlockAttr: HDD本地存储属性
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageBlockAttr: :class:`tencentcloud.batch.v20170312.models.StorageBlock`
        """
        self._ReleaseAddress = None
        self._UnsupportNetworks = None
        self._StorageBlockAttr = None

    @property
    def ReleaseAddress(self):
        return self._ReleaseAddress

    @ReleaseAddress.setter
    def ReleaseAddress(self, ReleaseAddress):
        self._ReleaseAddress = ReleaseAddress

    @property
    def UnsupportNetworks(self):
        return self._UnsupportNetworks

    @UnsupportNetworks.setter
    def UnsupportNetworks(self, UnsupportNetworks):
        self._UnsupportNetworks = UnsupportNetworks

    @property
    def StorageBlockAttr(self):
        return self._StorageBlockAttr

    @StorageBlockAttr.setter
    def StorageBlockAttr(self, StorageBlockAttr):
        self._StorageBlockAttr = StorageBlockAttr


    def _deserialize(self, params):
        self._ReleaseAddress = params.get("ReleaseAddress")
        self._UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self._StorageBlockAttr = StorageBlock()
            self._StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputMapping(AbstractModel):
    """输入映射

    """

    def __init__(self):
        r"""
        :param _SourcePath: 源端路径
        :type SourcePath: str
        :param _DestinationPath: 目的端路径
        :type DestinationPath: str
        :param _MountOptionParameter: 挂载配置项参数
        :type MountOptionParameter: str
        """
        self._SourcePath = None
        self._DestinationPath = None
        self._MountOptionParameter = None

    @property
    def SourcePath(self):
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def DestinationPath(self):
        return self._DestinationPath

    @DestinationPath.setter
    def DestinationPath(self, DestinationPath):
        self._DestinationPath = DestinationPath

    @property
    def MountOptionParameter(self):
        return self._MountOptionParameter

    @MountOptionParameter.setter
    def MountOptionParameter(self, MountOptionParameter):
        self._MountOptionParameter = MountOptionParameter


    def _deserialize(self, params):
        self._SourcePath = params.get("SourcePath")
        self._DestinationPath = params.get("DestinationPath")
        self._MountOptionParameter = params.get("MountOptionParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """描述实例的信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _LoginSettings: 实例登录设置。
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        """
        self._InstanceId = None
        self._ImageId = None
        self._LoginSettings = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCategoryItem(AbstractModel):
    """实例分类列表

    """

    def __init__(self):
        r"""
        :param _InstanceCategory: 实例类型名
        :type InstanceCategory: str
        :param _InstanceFamilySet: 实例族列表
        :type InstanceFamilySet: list of str
        """
        self._InstanceCategory = None
        self._InstanceFamilySet = None

    @property
    def InstanceCategory(self):
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def InstanceFamilySet(self):
        return self._InstanceFamilySet

    @InstanceFamilySet.setter
    def InstanceFamilySet(self, InstanceFamilySet):
        self._InstanceFamilySet = InstanceFamilySet


    def _deserialize(self, params):
        self._InstanceCategory = params.get("InstanceCategory")
        self._InstanceFamilySet = params.get("InstanceFamilySet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """竞价请求相关选项

    """

    def __init__(self):
        r"""
        :param _SpotOptions: 竞价相关选项
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotOptions: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`
        :param _MarketType: 市场选项类型，当前只支持取值：spot
注意：此字段可能返回 null，表示取不到有效值。
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        return self._MarketType

    @MarketType.setter
    def MarketType(self, MarketType):
        self._MarketType = MarketType


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self._SpotOptions = SpotMarketOptions()
            self._SpotOptions._deserialize(params.get("SpotOptions"))
        self._MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """批量计算可用的InstanceTypeConfig信息

    """

    def __init__(self):
        r"""
        :param _Mem: 内存容量，单位：`GB`。
        :type Mem: int
        :param _Cpu: CPU核数，单位：核。
        :type Cpu: int
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _Zone: 可用区。
        :type Zone: str
        :param _InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        """
        self._Mem = None
        self._Cpu = None
        self._InstanceType = None
        self._Zone = None
        self._InstanceFamily = None

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._Mem = params.get("Mem")
        self._Cpu = params.get("Cpu")
        self._InstanceType = params.get("InstanceType")
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeOptions(AbstractModel):
    """实例机型配置。

    """

    def __init__(self):
        r"""
        :param _CPU: CPU核数。
        :type CPU: int
        :param _Memory: 内存值，单位GB。
        :type Memory: int
        :param _InstanceCategories: 实例机型类别，可选参数：“ALL”、“GENERAL”、“GENERAL_2”、“GENERAL_3”、“COMPUTE”、“COMPUTE_2”和“COMPUTE_3”。默认值“ALL”。
        :type InstanceCategories: list of str
        """
        self._CPU = None
        self._Memory = None
        self._InstanceCategories = None

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceCategories(self):
        return self._InstanceCategories

    @InstanceCategories.setter
    def InstanceCategories(self, InstanceCategories):
        self._InstanceCategories = InstanceCategories


    def _deserialize(self, params):
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceCategories = params.get("InstanceCategories")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuotaItem(AbstractModel):
    """描述实例机型配额信息。

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。
        :type Zone: str
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _InstanceChargeType: 实例计费模式。取值范围： <br><li>PREPAID：表示预付费，即包年包月<br><li>POSTPAID_BY_HOUR：表示后付费，即按量计费<br><li>CDHPAID：表示[专用宿主机](https://cloud.tencent.com/document/product/416)付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
        :type InstanceChargeType: str
        :param _NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param _Externals: 扩展属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Externals: :class:`tencentcloud.batch.v20170312.models.Externals`
        :param _Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param _Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param _InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param _TypeName: 机型名称。
        :type TypeName: str
        :param _LocalDiskTypeList: 本地磁盘规格列表。当该参数返回为空值时，表示当前情况下无法创建本地盘。
        :type LocalDiskTypeList: list of LocalDiskType
        :param _Status: 实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br><li>SOLD_OUT：表示实例已售罄。
        :type Status: str
        :param _Price: 实例的售卖价格。
        :type Price: :class:`tencentcloud.batch.v20170312.models.ItemPrice`
        :param _SoldOutReason: 售罄原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type SoldOutReason: str
        :param _InstanceBandwidth: 内网带宽，单位Gbps。
        :type InstanceBandwidth: float
        :param _InstancePps: 网络收发包能力，单位万PPS。
        :type InstancePps: int
        :param _StorageBlockAmount: 本地存储块数量。
        :type StorageBlockAmount: int
        :param _CpuType: 处理器型号。
        :type CpuType: str
        :param _Gpu: 实例的GPU数量。
        :type Gpu: int
        :param _Fpga: 实例的FPGA数量。
        :type Fpga: int
        :param _Remark: 实例备注信息。
        :type Remark: str
        :param _GpuCount: 实例机型映射的物理GPU卡数，单位：卡。vGPU卡型小于1，直通卡型大于等于1。vGPU是通过分片虚拟化技术，将物理GPU卡重新划分，同一块GPU卡经虚拟化分割后可分配至不同的实例使用。直通卡型会将GPU设备直接挂载给实例使用。
        :type GpuCount: float
        :param _Frequency: 实例的CPU主频信息
        :type Frequency: str
        :param _StatusCategory: 描述库存情况。取值范围： <br><li> UnderStock：表示对应库存即将售罄<br><li> NormalStock：表示对应库存供应有保障<br><li> EnoughStock：表示对应库存非常充足<br><li> WithoutStock：表示对应库存已经售罄
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCategory: str
        """
        self._Zone = None
        self._InstanceType = None
        self._InstanceChargeType = None
        self._NetworkCard = None
        self._Externals = None
        self._Cpu = None
        self._Memory = None
        self._InstanceFamily = None
        self._TypeName = None
        self._LocalDiskTypeList = None
        self._Status = None
        self._Price = None
        self._SoldOutReason = None
        self._InstanceBandwidth = None
        self._InstancePps = None
        self._StorageBlockAmount = None
        self._CpuType = None
        self._Gpu = None
        self._Fpga = None
        self._Remark = None
        self._GpuCount = None
        self._Frequency = None
        self._StatusCategory = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

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
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def LocalDiskTypeList(self):
        return self._LocalDiskTypeList

    @LocalDiskTypeList.setter
    def LocalDiskTypeList(self, LocalDiskTypeList):
        self._LocalDiskTypeList = LocalDiskTypeList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def SoldOutReason(self):
        return self._SoldOutReason

    @SoldOutReason.setter
    def SoldOutReason(self, SoldOutReason):
        self._SoldOutReason = SoldOutReason

    @property
    def InstanceBandwidth(self):
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def StorageBlockAmount(self):
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GpuCount(self):
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def StatusCategory(self):
        return self._StatusCategory

    @StatusCategory.setter
    def StatusCategory(self, StatusCategory):
        self._StatusCategory = StatusCategory


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceFamily = params.get("InstanceFamily")
        self._TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self._LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self._LocalDiskTypeList.append(obj)
        self._Status = params.get("Status")
        if params.get("Price") is not None:
            self._Price = ItemPrice()
            self._Price._deserialize(params.get("Price"))
        self._SoldOutReason = params.get("SoldOutReason")
        self._InstanceBandwidth = params.get("InstanceBandwidth")
        self._InstancePps = params.get("InstancePps")
        self._StorageBlockAmount = params.get("StorageBlockAmount")
        self._CpuType = params.get("CpuType")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._Remark = params.get("Remark")
        self._GpuCount = params.get("GpuCount")
        self._Frequency = params.get("Frequency")
        self._StatusCategory = params.get("StatusCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费<br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费<br><li>BANDWIDTH_PACKAGE：带宽包用户<br>默认取值：非带宽包用户默认与子机付费类型保持一致，比如子机付费类型为预付费，网络计费类型默认为预付费；子机付费类型为后付费，网络计费类型默认为后付费。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/12523)。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>true：表示分配公网IP<br><li>false：表示不分配公网IP<br><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。该参数仅在RunInstances接口中作为入参使用。
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: 带宽包ID。可通过[`DescribeBandwidthPackages`](https://cloud.tencent.com/document/api/215/19209)接口返回值中的`BandwidthPackageId`获取。该参数仅在RunInstances接口中作为入参使用。
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 后续合计费用的原价，后付费模式使用，单位：元。<br><li>如返回了其他时间区间项，如UnitPriceSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _ChargeUnit: 后续计价单元，后付费模式使用，可取值范围： <br><li>HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）：<br><li>GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _OriginalPrice: 预支合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 预支合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param _UnitPriceDiscount: 后续合计费用的折扣价，后付费模式使用，单位：元<br><li>如返回了其他时间区间项，如UnitPriceDiscountSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _UnitPriceSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceSecondStep: float
        :param _UnitPriceDiscountSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountSecondStep: float
        :param _UnitPriceThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceThirdStep: float
        :param _UnitPriceDiscountThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountThirdStep: float
        :param _OriginalPriceThreeYear: 预支三年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceThreeYear: float
        :param _DiscountPriceThreeYear: 预支三年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceThreeYear: float
        :param _DiscountThreeYear: 预支三年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountThreeYear: float
        :param _OriginalPriceFiveYear: 预支五年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceFiveYear: float
        :param _DiscountPriceFiveYear: 预支五年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceFiveYear: float
        :param _DiscountFiveYear: 预支五年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountFiveYear: float
        :param _OriginalPriceOneYear: 预支一年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceOneYear: float
        :param _DiscountPriceOneYear: 预支一年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceOneYear: float
        :param _DiscountOneYear: 预支一年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountOneYear: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._UnitPriceDiscount = None
        self._UnitPriceSecondStep = None
        self._UnitPriceDiscountSecondStep = None
        self._UnitPriceThirdStep = None
        self._UnitPriceDiscountThirdStep = None
        self._OriginalPriceThreeYear = None
        self._DiscountPriceThreeYear = None
        self._DiscountThreeYear = None
        self._OriginalPriceFiveYear = None
        self._DiscountPriceFiveYear = None
        self._DiscountFiveYear = None
        self._OriginalPriceOneYear = None
        self._DiscountPriceOneYear = None
        self._DiscountOneYear = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceSecondStep(self):
        return self._UnitPriceSecondStep

    @UnitPriceSecondStep.setter
    def UnitPriceSecondStep(self, UnitPriceSecondStep):
        self._UnitPriceSecondStep = UnitPriceSecondStep

    @property
    def UnitPriceDiscountSecondStep(self):
        return self._UnitPriceDiscountSecondStep

    @UnitPriceDiscountSecondStep.setter
    def UnitPriceDiscountSecondStep(self, UnitPriceDiscountSecondStep):
        self._UnitPriceDiscountSecondStep = UnitPriceDiscountSecondStep

    @property
    def UnitPriceThirdStep(self):
        return self._UnitPriceThirdStep

    @UnitPriceThirdStep.setter
    def UnitPriceThirdStep(self, UnitPriceThirdStep):
        self._UnitPriceThirdStep = UnitPriceThirdStep

    @property
    def UnitPriceDiscountThirdStep(self):
        return self._UnitPriceDiscountThirdStep

    @UnitPriceDiscountThirdStep.setter
    def UnitPriceDiscountThirdStep(self, UnitPriceDiscountThirdStep):
        self._UnitPriceDiscountThirdStep = UnitPriceDiscountThirdStep

    @property
    def OriginalPriceThreeYear(self):
        return self._OriginalPriceThreeYear

    @OriginalPriceThreeYear.setter
    def OriginalPriceThreeYear(self, OriginalPriceThreeYear):
        self._OriginalPriceThreeYear = OriginalPriceThreeYear

    @property
    def DiscountPriceThreeYear(self):
        return self._DiscountPriceThreeYear

    @DiscountPriceThreeYear.setter
    def DiscountPriceThreeYear(self, DiscountPriceThreeYear):
        self._DiscountPriceThreeYear = DiscountPriceThreeYear

    @property
    def DiscountThreeYear(self):
        return self._DiscountThreeYear

    @DiscountThreeYear.setter
    def DiscountThreeYear(self, DiscountThreeYear):
        self._DiscountThreeYear = DiscountThreeYear

    @property
    def OriginalPriceFiveYear(self):
        return self._OriginalPriceFiveYear

    @OriginalPriceFiveYear.setter
    def OriginalPriceFiveYear(self, OriginalPriceFiveYear):
        self._OriginalPriceFiveYear = OriginalPriceFiveYear

    @property
    def DiscountPriceFiveYear(self):
        return self._DiscountPriceFiveYear

    @DiscountPriceFiveYear.setter
    def DiscountPriceFiveYear(self, DiscountPriceFiveYear):
        self._DiscountPriceFiveYear = DiscountPriceFiveYear

    @property
    def DiscountFiveYear(self):
        return self._DiscountFiveYear

    @DiscountFiveYear.setter
    def DiscountFiveYear(self, DiscountFiveYear):
        self._DiscountFiveYear = DiscountFiveYear

    @property
    def OriginalPriceOneYear(self):
        return self._OriginalPriceOneYear

    @OriginalPriceOneYear.setter
    def OriginalPriceOneYear(self, OriginalPriceOneYear):
        self._OriginalPriceOneYear = OriginalPriceOneYear

    @property
    def DiscountPriceOneYear(self):
        return self._DiscountPriceOneYear

    @DiscountPriceOneYear.setter
    def DiscountPriceOneYear(self, DiscountPriceOneYear):
        self._DiscountPriceOneYear = DiscountPriceOneYear

    @property
    def DiscountOneYear(self):
        return self._DiscountOneYear

    @DiscountOneYear.setter
    def DiscountOneYear(self, DiscountOneYear):
        self._DiscountOneYear = DiscountOneYear


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self._UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self._UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self._UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")
        self._OriginalPriceThreeYear = params.get("OriginalPriceThreeYear")
        self._DiscountPriceThreeYear = params.get("DiscountPriceThreeYear")
        self._DiscountThreeYear = params.get("DiscountThreeYear")
        self._OriginalPriceFiveYear = params.get("OriginalPriceFiveYear")
        self._DiscountPriceFiveYear = params.get("DiscountPriceFiveYear")
        self._DiscountFiveYear = params.get("DiscountFiveYear")
        self._OriginalPriceOneYear = params.get("OriginalPriceOneYear")
        self._DiscountPriceOneYear = params.get("DiscountPriceOneYear")
        self._DiscountOneYear = params.get("DiscountOneYear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """作业

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务信息
        :type Tasks: list of Task
        :param _JobName: 作业名称
        :type JobName: str
        :param _JobDescription: 作业描述
        :type JobDescription: str
        :param _Priority: 作业优先级，任务（Task）和任务实例（TaskInstance）会继承作业优先级
        :type Priority: int
        :param _Dependences: 依赖信息
        :type Dependences: list of Dependence
        :param _Notifications: 通知信息
        :type Notifications: list of Notification
        :param _TaskExecutionDependOn: 对于存在依赖关系的任务中，后序任务执行对于前序任务的依赖条件。取值范围包括 PRE_TASK_SUCCEED，PRE_TASK_AT_LEAST_PARTLY_SUCCEED，PRE_TASK_FINISHED，默认值为PRE_TASK_SUCCEED。
        :type TaskExecutionDependOn: str
        :param _StateIfCreateCvmFailed: 表示创建 CVM 失败按照何种策略处理。取值范围包括 FAILED，RUNNABLE。FAILED 表示创建 CVM 失败按照一次执行失败处理，RUNNABLE 表示创建 CVM 失败按照继续等待处理。默认值为FAILED。StateIfCreateCvmFailed对于提交的指定计算环境的作业无效。
        :type StateIfCreateCvmFailed: str
        :param _Tags: 标签列表。通过指定该参数可以支持绑定标签到作业。每个作业最多绑定10个标签。
        :type Tags: list of Tag
        :param _NotificationTarget: 表示通知信息的通知目标类型。
取值范围：CMQ，TDMQ_CMQ。
CMQ:表示向腾讯云CMQ发送消息。
TDMQ_CMQ：表示向腾讯云TDMQ_CMQ发送消息。<br/>默认值为CMQ。<br/>注：腾讯云计划于2022年6月前正式下线消息队列 CMQ，建议使用TDMQ_CMQ。参考文档：[CMQ迁移到TDMQ_CMQ](https://cloud.tencent.com/document/product/406/60860)
        :type NotificationTarget: str
        """
        self._Tasks = None
        self._JobName = None
        self._JobDescription = None
        self._Priority = None
        self._Dependences = None
        self._Notifications = None
        self._TaskExecutionDependOn = None
        self._StateIfCreateCvmFailed = None
        self._Tags = None
        self._NotificationTarget = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobDescription(self):
        return self._JobDescription

    @JobDescription.setter
    def JobDescription(self, JobDescription):
        self._JobDescription = JobDescription

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Dependences(self):
        return self._Dependences

    @Dependences.setter
    def Dependences(self, Dependences):
        self._Dependences = Dependences

    @property
    def Notifications(self):
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def TaskExecutionDependOn(self):
        return self._TaskExecutionDependOn

    @TaskExecutionDependOn.setter
    def TaskExecutionDependOn(self, TaskExecutionDependOn):
        self._TaskExecutionDependOn = TaskExecutionDependOn

    @property
    def StateIfCreateCvmFailed(self):
        return self._StateIfCreateCvmFailed

    @StateIfCreateCvmFailed.setter
    def StateIfCreateCvmFailed(self, StateIfCreateCvmFailed):
        self._StateIfCreateCvmFailed = StateIfCreateCvmFailed

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._JobName = params.get("JobName")
        self._JobDescription = params.get("JobDescription")
        self._Priority = params.get("Priority")
        if params.get("Dependences") is not None:
            self._Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self._Dependences.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._TaskExecutionDependOn = params.get("TaskExecutionDependOn")
        self._StateIfCreateCvmFailed = params.get("StateIfCreateCvmFailed")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NotificationTarget = params.get("NotificationTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobView(AbstractModel):
    """作业信息

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _JobName: 作业名称
        :type JobName: str
        :param _JobState: 作业状态
        :type JobState: str
        :param _Priority: 作业优先级
        :type Priority: int
        :param _Placement: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _TaskMetrics: 任务统计指标
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param _Tags: 作业绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._JobId = None
        self._JobName = None
        self._JobState = None
        self._Priority = None
        self._Placement = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskMetrics = None
        self._Tags = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobState(self):
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskMetrics(self):
        return self._TaskMetrics

    @TaskMetrics.setter
    def TaskMetrics(self, TaskMetrics):
        self._TaskMetrics = TaskMetrics

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobState = params.get("JobState")
        self._Priority = params.get("Priority")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        if params.get("TaskMetrics") is not None:
            self._TaskMetrics = TaskMetrics()
            self._TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskType(AbstractModel):
    """本地磁盘规格

    """

    def __init__(self):
        r"""
        :param _Type: 本地磁盘类型。
        :type Type: str
        :param _PartitionType: 本地磁盘属性。
        :type PartitionType: str
        :param _MinSize: 本地磁盘最小值。
        :type MinSize: int
        :param _MaxSize: 本地磁盘最大值。
        :type MaxSize: int
        :param _Required: 购买时本地盘是否为必选。取值范围：<br><li>REQUIRED：表示必选<br><li>OPTIONAL：表示可选。
        :type Required: str
        """
        self._Type = None
        self._PartitionType = None
        self._MinSize = None
        self._MaxSize = None
        self._Required = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PartitionType = params.get("PartitionType")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? \/ ]中的特殊符号。<br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? \/]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param _KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :type KeyIds: list of str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyComputeEnvRequest(AbstractModel):
    """ModifyComputeEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param _EnvData: 计算环境属性数据
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.ComputeEnvData`
        """
        self._EnvId = None
        self._DesiredComputeNodeCount = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvData = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        if params.get("EnvData") is not None:
            self._EnvData = ComputeEnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyComputeEnvResponse(AbstractModel):
    """ModifyComputeEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param _TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param _TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        :param _TaskTemplateInfo: 任务模板信息
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        self._TaskTemplateId = None
        self._TaskTemplateName = None
        self._TaskTemplateDescription = None
        self._TaskTemplateInfo = None

    @property
    def TaskTemplateId(self):
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def TaskTemplateName(self):
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateDescription(self):
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def TaskTemplateInfo(self):
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._TaskTemplateName = params.get("TaskTemplateName")
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskTemplateResponse(AbstractModel):
    """ModifyTaskTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """数据盘挂载选项

    """

    def __init__(self):
        r"""
        :param _LocalPath: 挂载点，Linux系统合法路径，或Windows系统盘符,比如"H:\\"
        :type LocalPath: str
        :param _FileSystemType: 文件系统类型，Linux系统下支持"EXT3"和"EXT4"两种，默认"EXT3"；Windows系统下仅支持"NTFS"
        :type FileSystemType: str
        """
        self._LocalPath = None
        self._FileSystemType = None

    @property
    def LocalPath(self):
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def FileSystemType(self):
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamedComputeEnv(AbstractModel):
    """计算环境

    """

    def __init__(self):
        r"""
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param _EnvType: 计算环境管理类型
        :type EnvType: str
        :param _EnvData: 计算环境具体参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param _Authentications: 授权信息
        :type Authentications: list of Authentication
        :param _InputMappings: 输入映射信息
        :type InputMappings: list of InputMapping
        :param _AgentRunningMode: agent运行模式，适用于Windows系统
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        :param _Notifications: 通知信息
        :type Notifications: list of Notification
        :param _ActionIfComputeNodeInactive: 非活跃节点处理策略，默认“RECREATE”，即对于实例创建失败或异常退还的计算节点，定期重新创建实例资源。
        :type ActionIfComputeNodeInactive: str
        :param _ResourceMaxRetryCount: 对于实例创建失败或异常退还的计算节点，定期重新创建实例资源的最大重试次数，最大值100，如果不设置的话，系统会设置一个默认值，当前为7
        :type ResourceMaxRetryCount: int
        :param _Tags: 标签列表。通过指定该参数可以支持绑定标签到计算环境。每个计算环境最多绑定10个标签。
        :type Tags: list of Tag
        :param _NotificationTarget: 表示通知信息的通知目标类型。
取值范围：CMQ，TDMQ_CMQ。
CMQ:表示向腾讯云CMQ发送消息。
TDMQ_CMQ：表示向腾讯云TDMQ_CMQ发送消息。<br/>默认值为CMQ。<br/>注：腾讯云计划于2022年6月前正式下线消息队列 CMQ，建议使用TDMQ_CMQ。参考文档：[CMQ迁移到TDMQ_CMQ](https://cloud.tencent.com/document/product/406/60860)
        :type NotificationTarget: str
        """
        self._EnvName = None
        self._DesiredComputeNodeCount = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._Authentications = None
        self._InputMappings = None
        self._AgentRunningMode = None
        self._Notifications = None
        self._ActionIfComputeNodeInactive = None
        self._ResourceMaxRetryCount = None
        self._Tags = None
        self._NotificationTarget = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvDescription(self):
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def Authentications(self):
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def InputMappings(self):
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def AgentRunningMode(self):
        return self._AgentRunningMode

    @AgentRunningMode.setter
    def AgentRunningMode(self, AgentRunningMode):
        self._AgentRunningMode = AgentRunningMode

    @property
    def Notifications(self):
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def ActionIfComputeNodeInactive(self):
        return self._ActionIfComputeNodeInactive

    @ActionIfComputeNodeInactive.setter
    def ActionIfComputeNodeInactive(self, ActionIfComputeNodeInactive):
        self._ActionIfComputeNodeInactive = ActionIfComputeNodeInactive

    @property
    def ResourceMaxRetryCount(self):
        return self._ResourceMaxRetryCount

    @ResourceMaxRetryCount.setter
    def ResourceMaxRetryCount(self, ResourceMaxRetryCount):
        self._ResourceMaxRetryCount = ResourceMaxRetryCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("AgentRunningMode") is not None:
            self._AgentRunningMode = AgentRunningMode()
            self._AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self._ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NotificationTarget = params.get("NotificationTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamedCpmComputeEnv(AbstractModel):
    """黑石计算环境

    """

    def __init__(self):
        r"""
        :param _EnvName: 计算环境名称
        :type EnvName: str
        :param _EnvData: 计算环境具体参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvDataCpm`
        :param _DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param _EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param _EnvType: 计算环境管理类型， 取值MANAGED。
        :type EnvType: str
        :param _Authentications: 授权信息
        :type Authentications: list of Authentication
        :param _InputMappings: 输入映射信息
        :type InputMappings: list of InputMapping
        :param _Notifications: 通知信息
        :type Notifications: :class:`tencentcloud.batch.v20170312.models.Notification`
        :param _ActionIfComputeNodeInactive: 非活跃节点处理策略，默认“RECREATE”，即对于实例创建失败或异常退还的计算节点，定期重新创建实例资源。
        :type ActionIfComputeNodeInactive: str
        :param _ResourceMaxRetryCount: 对于实例创建失败或异常退还的计算节点，定期重新创建实例资源的最大重试次数，最大值100，如果不设置的话，系统会设置一个默认值，当前为7。
        :type ResourceMaxRetryCount: int
        :param _Tags: 标签列表。通过指定该参数可以支持绑定标签到黑石计算环境。每个黑石计算环境最多绑定10个标签。
        :type Tags: list of Tag
        :param _NotificationTarget: 表示通知信息的通知目标类型。
取值范围：CMQ，TDMQ_CMQ。
CMQ:表示向腾讯云CMQ发送消息。
TDMQ_CMQ：表示向腾讯云TDMQ_CMQ发送消息。<br/>默认值为CMQ。<br/>注：腾讯云计划于2022年6月前正式下线消息队列 CMQ，建议使用TDMQ_CMQ。参考文档：[CMQ迁移到TDMQ_CMQ](https://cloud.tencent.com/document/product/406/60860)
        :type NotificationTarget: str
        """
        self._EnvName = None
        self._EnvData = None
        self._DesiredComputeNodeCount = None
        self._EnvDescription = None
        self._EnvType = None
        self._Authentications = None
        self._InputMappings = None
        self._Notifications = None
        self._ActionIfComputeNodeInactive = None
        self._ResourceMaxRetryCount = None
        self._Tags = None
        self._NotificationTarget = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvData(self):
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def DesiredComputeNodeCount(self):
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvDescription(self):
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def Authentications(self):
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def InputMappings(self):
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def Notifications(self):
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def ActionIfComputeNodeInactive(self):
        return self._ActionIfComputeNodeInactive

    @ActionIfComputeNodeInactive.setter
    def ActionIfComputeNodeInactive(self, ActionIfComputeNodeInactive):
        self._ActionIfComputeNodeInactive = ActionIfComputeNodeInactive

    @property
    def ResourceMaxRetryCount(self):
        return self._ResourceMaxRetryCount

    @ResourceMaxRetryCount.setter
    def ResourceMaxRetryCount(self, ResourceMaxRetryCount):
        self._ResourceMaxRetryCount = ResourceMaxRetryCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        if params.get("EnvData") is not None:
            self._EnvData = EnvDataCpm()
            self._EnvData._deserialize(params.get("EnvData"))
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = Notification()
            self._Notifications._deserialize(params.get("Notifications"))
        self._ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self._ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NotificationTarget = params.get("NotificationTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Notification(AbstractModel):
    """通知信息

    """

    def __init__(self):
        r"""
        :param _TopicName: CMQ主题名字，要求主题名有效且关联订阅
        :type TopicName: str
        :param _EventConfigs: 事件配置
        :type EventConfigs: list of EventConfig
        """
        self._TopicName = None
        self._EventConfigs = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def EventConfigs(self):
        return self._EventConfigs

    @EventConfigs.setter
    def EventConfigs(self, EventConfigs):
        self._EventConfigs = EventConfigs


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        if params.get("EventConfigs") is not None:
            self._EventConfigs = []
            for item in params.get("EventConfigs"):
                obj = EventConfig()
                obj._deserialize(item)
                self._EventConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsInfo(AbstractModel):
    """操作系统类型

    """

    def __init__(self):
        r"""
        :param _OsTypeId: 操作系统ID。
        :type OsTypeId: int
        :param _OsName: 操作系统名称。
        :type OsName: str
        :param _OsDescription: 操作系统名称描述。
        :type OsDescription: str
        :param _OsEnglishDescription: 操作系统英文名称。
        :type OsEnglishDescription: str
        :param _OsClass: 操作系统的分类，如CentOs Debian。
        :type OsClass: str
        :param _ImageTag: 标识镜像分类。public:公共镜像; private: 专属镜像。
        :type ImageTag: str
        :param _MaxPartitionSize: 操作系统，ext4文件下所支持的最大的磁盘大小。单位为T。
        :type MaxPartitionSize: int
        """
        self._OsTypeId = None
        self._OsName = None
        self._OsDescription = None
        self._OsEnglishDescription = None
        self._OsClass = None
        self._ImageTag = None
        self._MaxPartitionSize = None

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsDescription(self):
        return self._OsDescription

    @OsDescription.setter
    def OsDescription(self, OsDescription):
        self._OsDescription = OsDescription

    @property
    def OsEnglishDescription(self):
        return self._OsEnglishDescription

    @OsEnglishDescription.setter
    def OsEnglishDescription(self, OsEnglishDescription):
        self._OsEnglishDescription = OsEnglishDescription

    @property
    def OsClass(self):
        return self._OsClass

    @OsClass.setter
    def OsClass(self, OsClass):
        self._OsClass = OsClass

    @property
    def ImageTag(self):
        return self._ImageTag

    @ImageTag.setter
    def ImageTag(self, ImageTag):
        self._ImageTag = ImageTag

    @property
    def MaxPartitionSize(self):
        return self._MaxPartitionSize

    @MaxPartitionSize.setter
    def MaxPartitionSize(self, MaxPartitionSize):
        self._MaxPartitionSize = MaxPartitionSize


    def _deserialize(self, params):
        self._OsTypeId = params.get("OsTypeId")
        self._OsName = params.get("OsName")
        self._OsDescription = params.get("OsDescription")
        self._OsEnglishDescription = params.get("OsEnglishDescription")
        self._OsClass = params.get("OsClass")
        self._ImageTag = params.get("ImageTag")
        self._MaxPartitionSize = params.get("MaxPartitionSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMapping(AbstractModel):
    """输出映射

    """

    def __init__(self):
        r"""
        :param _SourcePath: 源端路径
        :type SourcePath: str
        :param _DestinationPath: 目的端路径
        :type DestinationPath: str
        :param _OutputMappingOption: 输出映射选项
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputMappingOption: :class:`tencentcloud.batch.v20170312.models.OutputMappingOption`
        """
        self._SourcePath = None
        self._DestinationPath = None
        self._OutputMappingOption = None

    @property
    def SourcePath(self):
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def DestinationPath(self):
        return self._DestinationPath

    @DestinationPath.setter
    def DestinationPath(self, DestinationPath):
        self._DestinationPath = DestinationPath

    @property
    def OutputMappingOption(self):
        return self._OutputMappingOption

    @OutputMappingOption.setter
    def OutputMappingOption(self, OutputMappingOption):
        self._OutputMappingOption = OutputMappingOption


    def _deserialize(self, params):
        self._SourcePath = params.get("SourcePath")
        self._DestinationPath = params.get("DestinationPath")
        if params.get("OutputMappingOption") is not None:
            self._OutputMappingOption = OutputMappingOption()
            self._OutputMappingOption._deserialize(params.get("OutputMappingOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMappingConfig(AbstractModel):
    """输出映射配置

    """

    def __init__(self):
        r"""
        :param _Scene: 存储类型，仅支持COS
        :type Scene: str
        :param _WorkerNum: 并行worker数量
        :type WorkerNum: int
        :param _WorkerPartSize: worker分块大小，单位MB
        :type WorkerPartSize: int
        """
        self._Scene = None
        self._WorkerNum = None
        self._WorkerPartSize = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def WorkerNum(self):
        return self._WorkerNum

    @WorkerNum.setter
    def WorkerNum(self, WorkerNum):
        self._WorkerNum = WorkerNum

    @property
    def WorkerPartSize(self):
        return self._WorkerPartSize

    @WorkerPartSize.setter
    def WorkerPartSize(self, WorkerPartSize):
        self._WorkerPartSize = WorkerPartSize


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._WorkerNum = params.get("WorkerNum")
        self._WorkerPartSize = params.get("WorkerPartSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMappingOption(AbstractModel):
    """输出映射选项

    """

    def __init__(self):
        r"""
        :param _Workspace: 容器场景下,输出选项从实例映射到容器内的实例侧的工作空间。
BATCH_WORKSPACE: 工作空间为BATCH在实例内定义的工作空间，BATCH侧保证作业之间的隔离。（默认）
GLOBAL_WORKSPACE: 工作空间为实例操作系统空间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Workspace: str
        """
        self._Workspace = None

    @property
    def Workspace(self):
        return self._Workspace

    @Workspace.setter
    def Workspace(self, Workspace):
        self._Workspace = Workspace


    def _deserialize(self, params):
        self._Workspace = params.get("Workspace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机（仅专用宿主机产品可用），母机IP等

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区ID。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _HostIds: 实例所属的专用宿主机ID列表，仅用于入参。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :type HostIds: list of str
        :param _HostId: 实例所属的专用宿主机ID，仅用于出参。
        :type HostId: str
        """
        self._Zone = None
        self._ProjectId = None
        self._HostIds = None
        self._HostId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._HostIds = params.get("HostIds")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectInfo(AbstractModel):
    """重定向信息

    """

    def __init__(self):
        r"""
        :param _StdoutRedirectPath: 标准输出重定向路径
        :type StdoutRedirectPath: str
        :param _StderrRedirectPath: 标准错误重定向路径
        :type StderrRedirectPath: str
        :param _StdoutRedirectFileName: 标准输出重定向文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutRedirectFileName: str
        :param _StderrRedirectFileName: 标准错误重定向文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrRedirectFileName: str
        """
        self._StdoutRedirectPath = None
        self._StderrRedirectPath = None
        self._StdoutRedirectFileName = None
        self._StderrRedirectFileName = None

    @property
    def StdoutRedirectPath(self):
        return self._StdoutRedirectPath

    @StdoutRedirectPath.setter
    def StdoutRedirectPath(self, StdoutRedirectPath):
        self._StdoutRedirectPath = StdoutRedirectPath

    @property
    def StderrRedirectPath(self):
        return self._StderrRedirectPath

    @StderrRedirectPath.setter
    def StderrRedirectPath(self, StderrRedirectPath):
        self._StderrRedirectPath = StderrRedirectPath

    @property
    def StdoutRedirectFileName(self):
        return self._StdoutRedirectFileName

    @StdoutRedirectFileName.setter
    def StdoutRedirectFileName(self, StdoutRedirectFileName):
        self._StdoutRedirectFileName = StdoutRedirectFileName

    @property
    def StderrRedirectFileName(self):
        return self._StderrRedirectFileName

    @StderrRedirectFileName.setter
    def StderrRedirectFileName(self, StderrRedirectFileName):
        self._StderrRedirectFileName = StderrRedirectFileName


    def _deserialize(self, params):
        self._StdoutRedirectPath = params.get("StdoutRedirectPath")
        self._StderrRedirectPath = params.get("StderrRedirectPath")
        self._StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self._StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectLocalInfo(AbstractModel):
    """本地重定向信息

    """

    def __init__(self):
        r"""
        :param _StdoutLocalPath: 标准输出重定向本地路径
        :type StdoutLocalPath: str
        :param _StderrLocalPath: 标准错误重定向本地路径
        :type StderrLocalPath: str
        :param _StdoutLocalFileName: 标准输出重定向本地文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutLocalFileName: str
        :param _StderrLocalFileName: 标准错误重定向本地文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrLocalFileName: str
        """
        self._StdoutLocalPath = None
        self._StderrLocalPath = None
        self._StdoutLocalFileName = None
        self._StderrLocalFileName = None

    @property
    def StdoutLocalPath(self):
        return self._StdoutLocalPath

    @StdoutLocalPath.setter
    def StdoutLocalPath(self, StdoutLocalPath):
        self._StdoutLocalPath = StdoutLocalPath

    @property
    def StderrLocalPath(self):
        return self._StderrLocalPath

    @StderrLocalPath.setter
    def StderrLocalPath(self, StderrLocalPath):
        self._StderrLocalPath = StderrLocalPath

    @property
    def StdoutLocalFileName(self):
        return self._StdoutLocalFileName

    @StdoutLocalFileName.setter
    def StdoutLocalFileName(self, StdoutLocalFileName):
        self._StdoutLocalFileName = StdoutLocalFileName

    @property
    def StderrLocalFileName(self):
        return self._StderrLocalFileName

    @StderrLocalFileName.setter
    def StderrLocalFileName(self, StderrLocalFileName):
        self._StderrLocalFileName = StderrLocalFileName


    def _deserialize(self, params):
        self._StdoutLocalPath = params.get("StdoutLocalPath")
        self._StderrLocalPath = params.get("StderrLocalPath")
        self._StdoutLocalFileName = params.get("StdoutLocalFileName")
        self._StderrLocalFileName = params.get("StderrLocalFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsRequest(AbstractModel):
    """RetryJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 作业ID列表。
        :type JobIds: list of str
        """
        self._JobIds = None

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsResponse(AbstractModel):
    """RetryJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “云自动化助手” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启云自动化助手。取值范围：<br><li>true：表示开启云自动化助手服务<br><li>false：表示不开启云自动化助手服务<br><br>默认取值：false。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云监控](/document/product/248)服务。取值范围：<br><li>true：表示开启云监控服务<br><li>false：表示不开启云监控服务<br><br>默认取值：true。
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>true：表示开启云安全服务<br><li>false：表示不开启云安全服务<br><br>默认取值：true。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        r"""
        :param _MaxPrice: 竞价出价
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPrice: str
        :param _SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        return self._SpotInstanceType

    @SpotInstanceType.setter
    def SpotInstanceType(self, SpotInstanceType):
        self._SpotInstanceType = SpotInstanceType


    def _deserialize(self, params):
        self._MaxPrice = params.get("MaxPrice")
        self._SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageBlock(AbstractModel):
    """HDD的本地存储信息

    """

    def __init__(self):
        r"""
        :param _Type: HDD本地存储类型，值为：LOCAL_PRO.
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _MinSize: HDD本地存储的最小容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param _MaxSize: HDD本地存储的最大容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self._Type = None
        self._MinSize = None
        self._MaxSize = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitJobRequest(AbstractModel):
    """SubmitJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 作业所提交的位置信息。通过该参数可以指定作业关联CVM所属可用区等信息。
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _Job: 作业信息
        :type Job: :class:`tencentcloud.batch.v20170312.models.Job`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        """
        self._Placement = None
        self._Job = None
        self._ClientToken = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitJobResponse(AbstractModel):
    """SubmitJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 当通过本接口来提交作业时会返回该参数，表示一个作业ID。返回作业ID列表并不代表作业解析/运行成功，可根据 DescribeJob 接口查询其状态。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_BSSD：通用性SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><br>默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param _DiskId: 系统盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        :param _CdcId: 所属的独享集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None
        self._CdcId = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签。

    """

    def __init__(self):
        r"""
        :param _Key: 标签键。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param _Application: 应用程序信息
        :type Application: :class:`tencentcloud.batch.v20170312.models.Application`
        :param _TaskName: 任务名称，在一个作业内部唯一
        :type TaskName: str
        :param _TaskInstanceNum: 任务实例运行个数
        :type TaskInstanceNum: int
        :param _ComputeEnv: 运行环境信息，ComputeEnv 和 EnvId 必须指定一个（且只有一个）参数。
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`
        :param _EnvId: 计算环境ID，ComputeEnv 和 EnvId 必须指定一个（且只有一个）参数。
        :type EnvId: str
        :param _RedirectInfo: 重定向信息
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param _RedirectLocalInfo: 重定向本地信息
        :type RedirectLocalInfo: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`
        :param _InputMappings: 输入映射
        :type InputMappings: list of InputMapping
        :param _OutputMappings: 输出映射
        :type OutputMappings: list of OutputMapping
        :param _OutputMappingConfigs: 输出映射配置
        :type OutputMappingConfigs: list of OutputMappingConfig
        :param _EnvVars: 自定义环境变量
        :type EnvVars: list of EnvVar
        :param _Authentications: 授权信息
        :type Authentications: list of Authentication
        :param _FailedAction: TaskInstance失败后处理方式，取值包括TERMINATE（默认）、INTERRUPT、FAST_INTERRUPT。
        :type FailedAction: str
        :param _MaxRetryCount: 任务失败后的最大重试次数，默认为0
        :type MaxRetryCount: int
        :param _Timeout: 任务启动后的超时时间，单位秒，默认为86400秒
        :type Timeout: int
        :param _MaxConcurrentNum: 任务最大并发数限制，默认没有限制。
        :type MaxConcurrentNum: int
        :param _RestartComputeNode: 任务完成后，重启计算节点。适用于指定计算环境执行任务。
        :type RestartComputeNode: bool
        :param _ResourceMaxRetryCount: 启动任务过程中，创建计算资源如CVM失败后的最大重试次数，默认为0。最大值100。
        :type ResourceMaxRetryCount: int
        """
        self._Application = None
        self._TaskName = None
        self._TaskInstanceNum = None
        self._ComputeEnv = None
        self._EnvId = None
        self._RedirectInfo = None
        self._RedirectLocalInfo = None
        self._InputMappings = None
        self._OutputMappings = None
        self._OutputMappingConfigs = None
        self._EnvVars = None
        self._Authentications = None
        self._FailedAction = None
        self._MaxRetryCount = None
        self._Timeout = None
        self._MaxConcurrentNum = None
        self._RestartComputeNode = None
        self._ResourceMaxRetryCount = None

    @property
    def Application(self):
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceNum(self):
        return self._TaskInstanceNum

    @TaskInstanceNum.setter
    def TaskInstanceNum(self, TaskInstanceNum):
        self._TaskInstanceNum = TaskInstanceNum

    @property
    def ComputeEnv(self):
        return self._ComputeEnv

    @ComputeEnv.setter
    def ComputeEnv(self, ComputeEnv):
        self._ComputeEnv = ComputeEnv

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RedirectInfo(self):
        return self._RedirectInfo

    @RedirectInfo.setter
    def RedirectInfo(self, RedirectInfo):
        self._RedirectInfo = RedirectInfo

    @property
    def RedirectLocalInfo(self):
        return self._RedirectLocalInfo

    @RedirectLocalInfo.setter
    def RedirectLocalInfo(self, RedirectLocalInfo):
        self._RedirectLocalInfo = RedirectLocalInfo

    @property
    def InputMappings(self):
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def OutputMappings(self):
        return self._OutputMappings

    @OutputMappings.setter
    def OutputMappings(self, OutputMappings):
        self._OutputMappings = OutputMappings

    @property
    def OutputMappingConfigs(self):
        return self._OutputMappingConfigs

    @OutputMappingConfigs.setter
    def OutputMappingConfigs(self, OutputMappingConfigs):
        self._OutputMappingConfigs = OutputMappingConfigs

    @property
    def EnvVars(self):
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def Authentications(self):
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def FailedAction(self):
        return self._FailedAction

    @FailedAction.setter
    def FailedAction(self, FailedAction):
        self._FailedAction = FailedAction

    @property
    def MaxRetryCount(self):
        return self._MaxRetryCount

    @MaxRetryCount.setter
    def MaxRetryCount(self, MaxRetryCount):
        self._MaxRetryCount = MaxRetryCount

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def MaxConcurrentNum(self):
        return self._MaxConcurrentNum

    @MaxConcurrentNum.setter
    def MaxConcurrentNum(self, MaxConcurrentNum):
        self._MaxConcurrentNum = MaxConcurrentNum

    @property
    def RestartComputeNode(self):
        return self._RestartComputeNode

    @RestartComputeNode.setter
    def RestartComputeNode(self, RestartComputeNode):
        self._RestartComputeNode = RestartComputeNode

    @property
    def ResourceMaxRetryCount(self):
        return self._ResourceMaxRetryCount

    @ResourceMaxRetryCount.setter
    def ResourceMaxRetryCount(self, ResourceMaxRetryCount):
        self._ResourceMaxRetryCount = ResourceMaxRetryCount


    def _deserialize(self, params):
        if params.get("Application") is not None:
            self._Application = Application()
            self._Application._deserialize(params.get("Application"))
        self._TaskName = params.get("TaskName")
        self._TaskInstanceNum = params.get("TaskInstanceNum")
        if params.get("ComputeEnv") is not None:
            self._ComputeEnv = AnonymousComputeEnv()
            self._ComputeEnv._deserialize(params.get("ComputeEnv"))
        self._EnvId = params.get("EnvId")
        if params.get("RedirectInfo") is not None:
            self._RedirectInfo = RedirectInfo()
            self._RedirectInfo._deserialize(params.get("RedirectInfo"))
        if params.get("RedirectLocalInfo") is not None:
            self._RedirectLocalInfo = RedirectLocalInfo()
            self._RedirectLocalInfo._deserialize(params.get("RedirectLocalInfo"))
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("OutputMappings") is not None:
            self._OutputMappings = []
            for item in params.get("OutputMappings"):
                obj = OutputMapping()
                obj._deserialize(item)
                self._OutputMappings.append(obj)
        if params.get("OutputMappingConfigs") is not None:
            self._OutputMappingConfigs = []
            for item in params.get("OutputMappingConfigs"):
                obj = OutputMappingConfig()
                obj._deserialize(item)
                self._OutputMappingConfigs.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        self._FailedAction = params.get("FailedAction")
        self._MaxRetryCount = params.get("MaxRetryCount")
        self._Timeout = params.get("Timeout")
        self._MaxConcurrentNum = params.get("MaxConcurrentNum")
        self._RestartComputeNode = params.get("RestartComputeNode")
        self._ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceLog(AbstractModel):
    """任务实例日志详情。

    """

    def __init__(self):
        r"""
        :param _TaskInstanceIndex: 任务实例
        :type TaskInstanceIndex: int
        :param _StdoutLog: 标准输出日志（Base64编码，解码后最大日志长度2048字节）
注意：此字段可能返回 null，表示取不到有效值。
        :type StdoutLog: str
        :param _StderrLog: 标准错误日志（Base64编码，解码后最大日志长度2048字节）
注意：此字段可能返回 null，表示取不到有效值。
        :type StderrLog: str
        :param _StdoutRedirectPath: 标准输出重定向路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StdoutRedirectPath: str
        :param _StderrRedirectPath: 标准错误重定向路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StderrRedirectPath: str
        :param _StdoutRedirectFileName: 标准输出重定向文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type StdoutRedirectFileName: str
        :param _StderrRedirectFileName: 标准错误重定向文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type StderrRedirectFileName: str
        """
        self._TaskInstanceIndex = None
        self._StdoutLog = None
        self._StderrLog = None
        self._StdoutRedirectPath = None
        self._StderrRedirectPath = None
        self._StdoutRedirectFileName = None
        self._StderrRedirectFileName = None

    @property
    def TaskInstanceIndex(self):
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex

    @property
    def StdoutLog(self):
        return self._StdoutLog

    @StdoutLog.setter
    def StdoutLog(self, StdoutLog):
        self._StdoutLog = StdoutLog

    @property
    def StderrLog(self):
        return self._StderrLog

    @StderrLog.setter
    def StderrLog(self, StderrLog):
        self._StderrLog = StderrLog

    @property
    def StdoutRedirectPath(self):
        return self._StdoutRedirectPath

    @StdoutRedirectPath.setter
    def StdoutRedirectPath(self, StdoutRedirectPath):
        self._StdoutRedirectPath = StdoutRedirectPath

    @property
    def StderrRedirectPath(self):
        return self._StderrRedirectPath

    @StderrRedirectPath.setter
    def StderrRedirectPath(self, StderrRedirectPath):
        self._StderrRedirectPath = StderrRedirectPath

    @property
    def StdoutRedirectFileName(self):
        return self._StdoutRedirectFileName

    @StdoutRedirectFileName.setter
    def StdoutRedirectFileName(self, StdoutRedirectFileName):
        self._StdoutRedirectFileName = StdoutRedirectFileName

    @property
    def StderrRedirectFileName(self):
        return self._StderrRedirectFileName

    @StderrRedirectFileName.setter
    def StderrRedirectFileName(self, StderrRedirectFileName):
        self._StderrRedirectFileName = StderrRedirectFileName


    def _deserialize(self, params):
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        self._StdoutLog = params.get("StdoutLog")
        self._StderrLog = params.get("StderrLog")
        self._StdoutRedirectPath = params.get("StdoutRedirectPath")
        self._StderrRedirectPath = params.get("StderrRedirectPath")
        self._StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self._StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceMetrics(AbstractModel):
    """任务实例统计指标

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: Submitted个数
        :type SubmittedCount: int
        :param _PendingCount: Pending个数
        :type PendingCount: int
        :param _RunnableCount: Runnable个数
        :type RunnableCount: int
        :param _StartingCount: Starting个数
        :type StartingCount: int
        :param _RunningCount: Running个数
        :type RunningCount: int
        :param _SucceedCount: Succeed个数
        :type SucceedCount: int
        :param _FailedInterruptedCount: FailedInterrupted个数
        :type FailedInterruptedCount: int
        :param _FailedCount: Failed个数
        :type FailedCount: int
        """
        self._SubmittedCount = None
        self._PendingCount = None
        self._RunnableCount = None
        self._StartingCount = None
        self._RunningCount = None
        self._SucceedCount = None
        self._FailedInterruptedCount = None
        self._FailedCount = None

    @property
    def SubmittedCount(self):
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def PendingCount(self):
        return self._PendingCount

    @PendingCount.setter
    def PendingCount(self, PendingCount):
        self._PendingCount = PendingCount

    @property
    def RunnableCount(self):
        return self._RunnableCount

    @RunnableCount.setter
    def RunnableCount(self, RunnableCount):
        self._RunnableCount = RunnableCount

    @property
    def StartingCount(self):
        return self._StartingCount

    @StartingCount.setter
    def StartingCount(self, StartingCount):
        self._StartingCount = StartingCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def SucceedCount(self):
        return self._SucceedCount

    @SucceedCount.setter
    def SucceedCount(self, SucceedCount):
        self._SucceedCount = SucceedCount

    @property
    def FailedInterruptedCount(self):
        return self._FailedInterruptedCount

    @FailedInterruptedCount.setter
    def FailedInterruptedCount(self, FailedInterruptedCount):
        self._FailedInterruptedCount = FailedInterruptedCount

    @property
    def FailedCount(self):
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._PendingCount = params.get("PendingCount")
        self._RunnableCount = params.get("RunnableCount")
        self._StartingCount = params.get("StartingCount")
        self._RunningCount = params.get("RunningCount")
        self._SucceedCount = params.get("SucceedCount")
        self._FailedInterruptedCount = params.get("FailedInterruptedCount")
        self._FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceView(AbstractModel):
    """任务实例视图信息

    """

    def __init__(self):
        r"""
        :param _TaskInstanceIndex: 任务实例索引
        :type TaskInstanceIndex: int
        :param _TaskInstanceState: 任务实例状态
        :type TaskInstanceState: str
        :param _ExitCode: 应用程序执行结束的exit code
注意：此字段可能返回 null，表示取不到有效值。
        :type ExitCode: int
        :param _StateReason: 任务实例状态原因，任务实例失败时，会记录失败原因
        :type StateReason: str
        :param _ComputeNodeInstanceId: 任务实例运行时所在计算节点（例如CVM）的InstanceId。任务实例未运行或者完结时，本字段为空。任务实例重试时，本字段会随之变化
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputeNodeInstanceId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _LaunchTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTime: str
        :param _RunningTime: 开始运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _RedirectInfo: 重定向信息
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param _StateDetailedReason: 任务实例状态原因详情，任务实例失败时，会记录失败原因
        :type StateDetailedReason: str
        """
        self._TaskInstanceIndex = None
        self._TaskInstanceState = None
        self._ExitCode = None
        self._StateReason = None
        self._ComputeNodeInstanceId = None
        self._CreateTime = None
        self._LaunchTime = None
        self._RunningTime = None
        self._EndTime = None
        self._RedirectInfo = None
        self._StateDetailedReason = None

    @property
    def TaskInstanceIndex(self):
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex

    @property
    def TaskInstanceState(self):
        return self._TaskInstanceState

    @TaskInstanceState.setter
    def TaskInstanceState(self, TaskInstanceState):
        self._TaskInstanceState = TaskInstanceState

    @property
    def ExitCode(self):
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def StateReason(self):
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def ComputeNodeInstanceId(self):
        return self._ComputeNodeInstanceId

    @ComputeNodeInstanceId.setter
    def ComputeNodeInstanceId(self, ComputeNodeInstanceId):
        self._ComputeNodeInstanceId = ComputeNodeInstanceId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LaunchTime(self):
        return self._LaunchTime

    @LaunchTime.setter
    def LaunchTime(self, LaunchTime):
        self._LaunchTime = LaunchTime

    @property
    def RunningTime(self):
        return self._RunningTime

    @RunningTime.setter
    def RunningTime(self, RunningTime):
        self._RunningTime = RunningTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RedirectInfo(self):
        return self._RedirectInfo

    @RedirectInfo.setter
    def RedirectInfo(self, RedirectInfo):
        self._RedirectInfo = RedirectInfo

    @property
    def StateDetailedReason(self):
        return self._StateDetailedReason

    @StateDetailedReason.setter
    def StateDetailedReason(self, StateDetailedReason):
        self._StateDetailedReason = StateDetailedReason


    def _deserialize(self, params):
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        self._TaskInstanceState = params.get("TaskInstanceState")
        self._ExitCode = params.get("ExitCode")
        self._StateReason = params.get("StateReason")
        self._ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self._CreateTime = params.get("CreateTime")
        self._LaunchTime = params.get("LaunchTime")
        self._RunningTime = params.get("RunningTime")
        self._EndTime = params.get("EndTime")
        if params.get("RedirectInfo") is not None:
            self._RedirectInfo = RedirectInfo()
            self._RedirectInfo._deserialize(params.get("RedirectInfo"))
        self._StateDetailedReason = params.get("StateDetailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMetrics(AbstractModel):
    """任务统计指标

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: Submitted个数
        :type SubmittedCount: int
        :param _PendingCount: Pending个数
        :type PendingCount: int
        :param _RunnableCount: Runnable个数
        :type RunnableCount: int
        :param _StartingCount: Starting个数
        :type StartingCount: int
        :param _RunningCount: Running个数
        :type RunningCount: int
        :param _SucceedCount: Succeed个数
        :type SucceedCount: int
        :param _FailedInterruptedCount: FailedInterrupted个数
        :type FailedInterruptedCount: int
        :param _FailedCount: Failed个数
        :type FailedCount: int
        """
        self._SubmittedCount = None
        self._PendingCount = None
        self._RunnableCount = None
        self._StartingCount = None
        self._RunningCount = None
        self._SucceedCount = None
        self._FailedInterruptedCount = None
        self._FailedCount = None

    @property
    def SubmittedCount(self):
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def PendingCount(self):
        return self._PendingCount

    @PendingCount.setter
    def PendingCount(self, PendingCount):
        self._PendingCount = PendingCount

    @property
    def RunnableCount(self):
        return self._RunnableCount

    @RunnableCount.setter
    def RunnableCount(self, RunnableCount):
        self._RunnableCount = RunnableCount

    @property
    def StartingCount(self):
        return self._StartingCount

    @StartingCount.setter
    def StartingCount(self, StartingCount):
        self._StartingCount = StartingCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def SucceedCount(self):
        return self._SucceedCount

    @SucceedCount.setter
    def SucceedCount(self, SucceedCount):
        self._SucceedCount = SucceedCount

    @property
    def FailedInterruptedCount(self):
        return self._FailedInterruptedCount

    @FailedInterruptedCount.setter
    def FailedInterruptedCount(self, FailedInterruptedCount):
        self._FailedInterruptedCount = FailedInterruptedCount

    @property
    def FailedCount(self):
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._PendingCount = params.get("PendingCount")
        self._RunnableCount = params.get("RunnableCount")
        self._StartingCount = params.get("StartingCount")
        self._RunningCount = params.get("RunningCount")
        self._SucceedCount = params.get("SucceedCount")
        self._FailedInterruptedCount = params.get("FailedInterruptedCount")
        self._FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTemplateView(AbstractModel):
    """任务模板信息

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param _TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param _TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        :param _TaskTemplateInfo: 任务模板信息
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Tags: 任务模板绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._TaskTemplateId = None
        self._TaskTemplateName = None
        self._TaskTemplateDescription = None
        self._TaskTemplateInfo = None
        self._CreateTime = None
        self._Tags = None

    @property
    def TaskTemplateId(self):
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def TaskTemplateName(self):
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateDescription(self):
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def TaskTemplateInfo(self):
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._TaskTemplateName = params.get("TaskTemplateName")
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskView(AbstractModel):
    """任务视图信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskState: 任务状态
        :type TaskState: str
        :param _CreateTime: 开始时间
        :type CreateTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._TaskName = None
        self._TaskState = None
        self._CreateTime = None
        self._EndTime = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskState(self):
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskState = params.get("TaskState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeRequest(AbstractModel):
    """TerminateComputeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        """
        self._EnvId = None
        self._ComputeNodeId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ComputeNodeId(self):
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ComputeNodeId = params.get("ComputeNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeResponse(AbstractModel):
    """TerminateComputeNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 计算环境ID
        :type EnvId: str
        :param _ComputeNodeIds: 计算节点ID列表
        :type ComputeNodeIds: list of str
        """
        self._EnvId = None
        self._ComputeNodeIds = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ComputeNodeIds(self):
        return self._ComputeNodeIds

    @ComputeNodeIds.setter
    def ComputeNodeIds(self, ComputeNodeIds):
        self._ComputeNodeIds = ComputeNodeIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ComputeNodeIds = params.get("ComputeNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodesResponse(AbstractModel):
    """TerminateComputeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateJobResponse(AbstractModel):
    """TerminateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskInstanceIndex: 任务实例索引
        :type TaskInstanceIndex: int
        """
        self._JobId = None
        self._TaskName = None
        self._TaskInstanceIndex = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceIndex(self):
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTaskInstanceResponse(AbstractModel):
    """TerminateTaskInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type SubnetId: str
        :param _AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：<br><li>true：表示用作公网网关<br><li>false：表示不作为公网网关<br><br>默认取值：false。
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

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
    def AsVpcGateway(self):
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        