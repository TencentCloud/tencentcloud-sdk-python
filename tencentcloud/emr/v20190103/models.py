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


class AddMetricScaleStrategyRequest(AbstractModel):
    """AddMetricScaleStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StrategyType: 1表示按负载规则扩容，2表示按时间规则扩容。必须填写，并且和下面的规则策略匹配
        :type StrategyType: int
        :param _LoadAutoScaleStrategy: 按负载扩容的规则。
        :type LoadAutoScaleStrategy: :class:`tencentcloud.emr.v20190103.models.LoadAutoScaleStrategy`
        :param _TimeAutoScaleStrategy: 按时间扩缩容的规则。
        :type TimeAutoScaleStrategy: :class:`tencentcloud.emr.v20190103.models.TimeAutoScaleStrategy`
        """
        self._InstanceId = None
        self._StrategyType = None
        self._LoadAutoScaleStrategy = None
        self._TimeAutoScaleStrategy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def LoadAutoScaleStrategy(self):
        return self._LoadAutoScaleStrategy

    @LoadAutoScaleStrategy.setter
    def LoadAutoScaleStrategy(self, LoadAutoScaleStrategy):
        self._LoadAutoScaleStrategy = LoadAutoScaleStrategy

    @property
    def TimeAutoScaleStrategy(self):
        return self._TimeAutoScaleStrategy

    @TimeAutoScaleStrategy.setter
    def TimeAutoScaleStrategy(self, TimeAutoScaleStrategy):
        self._TimeAutoScaleStrategy = TimeAutoScaleStrategy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyType = params.get("StrategyType")
        if params.get("LoadAutoScaleStrategy") is not None:
            self._LoadAutoScaleStrategy = LoadAutoScaleStrategy()
            self._LoadAutoScaleStrategy._deserialize(params.get("LoadAutoScaleStrategy"))
        if params.get("TimeAutoScaleStrategy") is not None:
            self._TimeAutoScaleStrategy = TimeAutoScaleStrategy()
            self._TimeAutoScaleStrategy._deserialize(params.get("TimeAutoScaleStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMetricScaleStrategyResponse(AbstractModel):
    """AddMetricScaleStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class AddUsersForUserManagerRequest(AbstractModel):
    """AddUsersForUserManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群字符串ID
        :type InstanceId: str
        :param _UserManagerUserList: 用户信息列表
        :type UserManagerUserList: list of UserInfoForUserManager
        """
        self._InstanceId = None
        self._UserManagerUserList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserManagerUserList(self):
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserInfoForUserManager()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersForUserManagerResponse(AbstractModel):
    """AddUsersForUserManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessUserList: 添加成功的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessUserList: list of str
        :param _FailedUserList: 添加失败的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedUserList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessUserList = None
        self._FailedUserList = None
        self._RequestId = None

    @property
    def SuccessUserList(self):
        return self._SuccessUserList

    @SuccessUserList.setter
    def SuccessUserList(self, SuccessUserList):
        self._SuccessUserList = SuccessUserList

    @property
    def FailedUserList(self):
        return self._FailedUserList

    @FailedUserList.setter
    def FailedUserList(self, FailedUserList):
        self._FailedUserList = FailedUserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessUserList = params.get("SuccessUserList")
        self._FailedUserList = params.get("FailedUserList")
        self._RequestId = params.get("RequestId")


class AllNodeResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: 描述Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CoreResourceSpec: 描述Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _TaskResourceSpec: 描述Taskr节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CommonResourceSpec: 描述Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _MasterCount: Master节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterCount: int
        :param _CoreCount: Corer节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreCount: int
        :param _TaskCount: Task节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCount: int
        :param _CommonCount: Common节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._CommonResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = NodeResourceSpec()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = NodeResourceSpec()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = NodeResourceSpec()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = NodeResourceSpec()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationStatics(AbstractModel):
    """yarn application 统计信息

    """

    def __init__(self):
        r"""
        :param _Queue: 队列名
        :type Queue: str
        :param _User: 用户名
        :type User: str
        :param _ApplicationType: 作业类型
        :type ApplicationType: str
        :param _SumMemorySeconds: SumMemorySeconds含义
        :type SumMemorySeconds: int
        :param _SumVCoreSeconds: SumVCoreSeconds含义
        :type SumVCoreSeconds: int
        :param _SumHDFSBytesWritten: SumHDFSBytesWritten（带单位）
        :type SumHDFSBytesWritten: str
        :param _SumHDFSBytesRead: SumHDFSBytesRead（待单位）
        :type SumHDFSBytesRead: str
        :param _CountApps: 作业数
        :type CountApps: int
        """
        self._Queue = None
        self._User = None
        self._ApplicationType = None
        self._SumMemorySeconds = None
        self._SumVCoreSeconds = None
        self._SumHDFSBytesWritten = None
        self._SumHDFSBytesRead = None
        self._CountApps = None

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def SumMemorySeconds(self):
        return self._SumMemorySeconds

    @SumMemorySeconds.setter
    def SumMemorySeconds(self, SumMemorySeconds):
        self._SumMemorySeconds = SumMemorySeconds

    @property
    def SumVCoreSeconds(self):
        return self._SumVCoreSeconds

    @SumVCoreSeconds.setter
    def SumVCoreSeconds(self, SumVCoreSeconds):
        self._SumVCoreSeconds = SumVCoreSeconds

    @property
    def SumHDFSBytesWritten(self):
        return self._SumHDFSBytesWritten

    @SumHDFSBytesWritten.setter
    def SumHDFSBytesWritten(self, SumHDFSBytesWritten):
        self._SumHDFSBytesWritten = SumHDFSBytesWritten

    @property
    def SumHDFSBytesRead(self):
        return self._SumHDFSBytesRead

    @SumHDFSBytesRead.setter
    def SumHDFSBytesRead(self, SumHDFSBytesRead):
        self._SumHDFSBytesRead = SumHDFSBytesRead

    @property
    def CountApps(self):
        return self._CountApps

    @CountApps.setter
    def CountApps(self, CountApps):
        self._CountApps = CountApps


    def _deserialize(self, params):
        self._Queue = params.get("Queue")
        self._User = params.get("User")
        self._ApplicationType = params.get("ApplicationType")
        self._SumMemorySeconds = params.get("SumMemorySeconds")
        self._SumVCoreSeconds = params.get("SumVCoreSeconds")
        self._SumHDFSBytesWritten = params.get("SumHDFSBytesWritten")
        self._SumHDFSBytesRead = params.get("SumHDFSBytesRead")
        self._CountApps = params.get("CountApps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Arg(AbstractModel):
    """通用的参数

    """

    def __init__(self):
        r"""
        :param _Key: key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Values: 值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScaleRecord(AbstractModel):
    """弹性扩缩容记录

    """

    def __init__(self):
        r"""
        :param _StrategyName: 扩缩容规则名。
        :type StrategyName: str
        :param _ScaleAction: "SCALE_OUT"和"SCALE_IN"，分别表示扩容和缩容。
        :type ScaleAction: str
        :param _ActionStatus: 取值为"SUCCESS","FAILED","PART_SUCCESS","IN_PROCESS"，分别表示成功、失败、部分成功和流程中。
        :type ActionStatus: str
        :param _ActionTime: 流程触发时间。
        :type ActionTime: str
        :param _ScaleInfo: 扩缩容相关描述信息。
        :type ScaleInfo: str
        :param _ExpectScaleNum: 只在ScaleAction为SCALE_OUT时有效。
        :type ExpectScaleNum: int
        :param _EndTime: 流程结束时间。
        :type EndTime: str
        :param _StrategyType: 策略类型，按负载或者按时间，1表示负载伸缩，2表示时间伸缩
        :type StrategyType: int
        :param _SpecInfo: 扩容时所使用规格信息。
        :type SpecInfo: str
        :param _CompensateFlag: 补偿扩容，0表示不开启，1表示开启
注意：此字段可能返回 null，表示取不到有效值。
        :type CompensateFlag: int
        :param _CompensateCount: 补偿次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompensateCount: int
        :param _RetryCount: 重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryCount: int
        :param _RetryInfo: 重试信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryInfo: str
        :param _RetryEnReason: 重试英文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryEnReason: str
        :param _RetryReason: 重试描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryReason: str
        """
        self._StrategyName = None
        self._ScaleAction = None
        self._ActionStatus = None
        self._ActionTime = None
        self._ScaleInfo = None
        self._ExpectScaleNum = None
        self._EndTime = None
        self._StrategyType = None
        self._SpecInfo = None
        self._CompensateFlag = None
        self._CompensateCount = None
        self._RetryCount = None
        self._RetryInfo = None
        self._RetryEnReason = None
        self._RetryReason = None

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def ScaleAction(self):
        return self._ScaleAction

    @ScaleAction.setter
    def ScaleAction(self, ScaleAction):
        self._ScaleAction = ScaleAction

    @property
    def ActionStatus(self):
        return self._ActionStatus

    @ActionStatus.setter
    def ActionStatus(self, ActionStatus):
        self._ActionStatus = ActionStatus

    @property
    def ActionTime(self):
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def ScaleInfo(self):
        return self._ScaleInfo

    @ScaleInfo.setter
    def ScaleInfo(self, ScaleInfo):
        self._ScaleInfo = ScaleInfo

    @property
    def ExpectScaleNum(self):
        return self._ExpectScaleNum

    @ExpectScaleNum.setter
    def ExpectScaleNum(self, ExpectScaleNum):
        self._ExpectScaleNum = ExpectScaleNum

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def SpecInfo(self):
        return self._SpecInfo

    @SpecInfo.setter
    def SpecInfo(self, SpecInfo):
        self._SpecInfo = SpecInfo

    @property
    def CompensateFlag(self):
        return self._CompensateFlag

    @CompensateFlag.setter
    def CompensateFlag(self, CompensateFlag):
        self._CompensateFlag = CompensateFlag

    @property
    def CompensateCount(self):
        return self._CompensateCount

    @CompensateCount.setter
    def CompensateCount(self, CompensateCount):
        self._CompensateCount = CompensateCount

    @property
    def RetryCount(self):
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def RetryInfo(self):
        return self._RetryInfo

    @RetryInfo.setter
    def RetryInfo(self, RetryInfo):
        self._RetryInfo = RetryInfo

    @property
    def RetryEnReason(self):
        return self._RetryEnReason

    @RetryEnReason.setter
    def RetryEnReason(self, RetryEnReason):
        self._RetryEnReason = RetryEnReason

    @property
    def RetryReason(self):
        return self._RetryReason

    @RetryReason.setter
    def RetryReason(self, RetryReason):
        self._RetryReason = RetryReason


    def _deserialize(self, params):
        self._StrategyName = params.get("StrategyName")
        self._ScaleAction = params.get("ScaleAction")
        self._ActionStatus = params.get("ActionStatus")
        self._ActionTime = params.get("ActionTime")
        self._ScaleInfo = params.get("ScaleInfo")
        self._ExpectScaleNum = params.get("ExpectScaleNum")
        self._EndTime = params.get("EndTime")
        self._StrategyType = params.get("StrategyType")
        self._SpecInfo = params.get("SpecInfo")
        self._CompensateFlag = params.get("CompensateFlag")
        self._CompensateCount = params.get("CompensateCount")
        self._RetryCount = params.get("RetryCount")
        self._RetryInfo = params.get("RetryInfo")
        self._RetryEnReason = params.get("RetryEnReason")
        self._RetryReason = params.get("RetryReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScaleResourceConf(AbstractModel):
    """弹性扩缩容规格配置

    """

    def __init__(self):
        r"""
        :param _Id: 配置ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _ClusterId: 集群实例ID。
        :type ClusterId: int
        :param _ScaleLowerBound: 自动扩缩容保留最小实例数。
        :type ScaleLowerBound: int
        :param _ScaleUpperBound: 自动扩缩容最大实例数。
        :type ScaleUpperBound: int
        :param _StrategyType: 扩容规则类型，1为按负载指标扩容规则，2为按时间扩容规则
        :type StrategyType: int
        :param _NextTimeCanScale: 下次能可扩容时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextTimeCanScale: int
        :param _GraceDownFlag: 优雅缩容开关
注意：此字段可能返回 null，表示取不到有效值。
        :type GraceDownFlag: bool
        :param _HardwareType: "CVM"表示规格全部使用CVM相关类型，"POD"表示规格使用容器相关类型,默认为"CVM"。
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareType: str
        :param _PayMode: "POSTPAY"表示只使用按量计费，"SPOT_FIRST"表示竞价实例优先，只有HardwareType为"HOST"时支持竞价实例优先，"POD"只支持纯按量计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _PostPayPercentMin: 竞价实例优先的场景下，按量计费资源数量的最低百分比，整数
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPayPercentMin: int
        :param _ChangeToPod: 预设资源类型为HOST时，支持勾选“资源不足时切换POD”；支持取消勾选；默认不勾选（0），勾选（1)
注意：此字段可能返回 null，表示取不到有效值。
        :type ChangeToPod: int
        :param _GroupName: 伸缩组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _YarnNodeLabel: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type YarnNodeLabel: str
        :param _GroupStatus: 伸缩组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: int
        :param _Parallel: 并行伸缩 0关闭；1开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Parallel: int
        :param _EnableMNode: 是否支持MNode
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableMNode: int
        """
        self._Id = None
        self._ClusterId = None
        self._ScaleLowerBound = None
        self._ScaleUpperBound = None
        self._StrategyType = None
        self._NextTimeCanScale = None
        self._GraceDownFlag = None
        self._HardwareType = None
        self._PayMode = None
        self._PostPayPercentMin = None
        self._ChangeToPod = None
        self._GroupName = None
        self._YarnNodeLabel = None
        self._GroupStatus = None
        self._Parallel = None
        self._EnableMNode = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ScaleLowerBound(self):
        return self._ScaleLowerBound

    @ScaleLowerBound.setter
    def ScaleLowerBound(self, ScaleLowerBound):
        self._ScaleLowerBound = ScaleLowerBound

    @property
    def ScaleUpperBound(self):
        return self._ScaleUpperBound

    @ScaleUpperBound.setter
    def ScaleUpperBound(self, ScaleUpperBound):
        self._ScaleUpperBound = ScaleUpperBound

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def NextTimeCanScale(self):
        return self._NextTimeCanScale

    @NextTimeCanScale.setter
    def NextTimeCanScale(self, NextTimeCanScale):
        self._NextTimeCanScale = NextTimeCanScale

    @property
    def GraceDownFlag(self):
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def HardwareType(self):
        return self._HardwareType

    @HardwareType.setter
    def HardwareType(self, HardwareType):
        self._HardwareType = HardwareType

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PostPayPercentMin(self):
        return self._PostPayPercentMin

    @PostPayPercentMin.setter
    def PostPayPercentMin(self, PostPayPercentMin):
        self._PostPayPercentMin = PostPayPercentMin

    @property
    def ChangeToPod(self):
        return self._ChangeToPod

    @ChangeToPod.setter
    def ChangeToPod(self, ChangeToPod):
        self._ChangeToPod = ChangeToPod

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def GroupStatus(self):
        return self._GroupStatus

    @GroupStatus.setter
    def GroupStatus(self, GroupStatus):
        self._GroupStatus = GroupStatus

    @property
    def Parallel(self):
        return self._Parallel

    @Parallel.setter
    def Parallel(self, Parallel):
        self._Parallel = Parallel

    @property
    def EnableMNode(self):
        return self._EnableMNode

    @EnableMNode.setter
    def EnableMNode(self, EnableMNode):
        self._EnableMNode = EnableMNode


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ClusterId = params.get("ClusterId")
        self._ScaleLowerBound = params.get("ScaleLowerBound")
        self._ScaleUpperBound = params.get("ScaleUpperBound")
        self._StrategyType = params.get("StrategyType")
        self._NextTimeCanScale = params.get("NextTimeCanScale")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._HardwareType = params.get("HardwareType")
        self._PayMode = params.get("PayMode")
        self._PostPayPercentMin = params.get("PostPayPercentMin")
        self._ChangeToPod = params.get("ChangeToPod")
        self._GroupName = params.get("GroupName")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        self._GroupStatus = params.get("GroupStatus")
        self._Parallel = params.get("Parallel")
        self._EnableMNode = params.get("EnableMNode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BootstrapAction(AbstractModel):
    """引导脚本

    """

    def __init__(self):
        r"""
        :param _Path: 脚本位置，支持cos上的文件，且只支持https协议。
        :type Path: str
        :param _WhenRun: 执行时间。
resourceAfter 表示在机器资源申请成功后执行。
clusterBefore 表示在集群初始化前执行。
clusterAfter 表示在集群初始化后执行。
        :type WhenRun: str
        :param _Args: 脚本参数
        :type Args: list of str
        """
        self._Path = None
        self._WhenRun = None
        self._Args = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def WhenRun(self):
        return self._WhenRun

    @WhenRun.setter
    def WhenRun(self, WhenRun):
        self._WhenRun = WhenRun

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._WhenRun = params.get("WhenRun")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSSettings(AbstractModel):
    """COS 相关配置

    """

    def __init__(self):
        r"""
        :param _CosSecretId: COS SecretId
        :type CosSecretId: str
        :param _CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        :param _LogOnCosPath: 日志存储在COS上的路径
        :type LogOnCosPath: str
        """
        self._CosSecretId = None
        self._CosSecretKey = None
        self._LogOnCosPath = None

    @property
    def CosSecretId(self):
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def LogOnCosPath(self):
        return self._LogOnCosPath

    @LogOnCosPath.setter
    def LogOnCosPath(self, LogOnCosPath):
        self._LogOnCosPath = LogOnCosPath


    def _deserialize(self, params):
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._LogOnCosPath = params.get("LogOnCosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CapacityGlobalConfig(AbstractModel):
    """资源调度-容量调度器的全局设置

    """

    def __init__(self):
        r"""
        :param _EnableLabel: 是否开启了标签调度
        :type EnableLabel: bool
        :param _LabelDir: 如果开启了标签调度，标签信息存放的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelDir: str
        :param _QueueMappingOverride: 是否覆盖用户指定队列，为true表示覆盖。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueMappingOverride: bool
        :param _DefaultSettings: 高级设置
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultSettings: list of DefaultSetting
        """
        self._EnableLabel = None
        self._LabelDir = None
        self._QueueMappingOverride = None
        self._DefaultSettings = None

    @property
    def EnableLabel(self):
        return self._EnableLabel

    @EnableLabel.setter
    def EnableLabel(self, EnableLabel):
        self._EnableLabel = EnableLabel

    @property
    def LabelDir(self):
        return self._LabelDir

    @LabelDir.setter
    def LabelDir(self, LabelDir):
        self._LabelDir = LabelDir

    @property
    def QueueMappingOverride(self):
        return self._QueueMappingOverride

    @QueueMappingOverride.setter
    def QueueMappingOverride(self, QueueMappingOverride):
        self._QueueMappingOverride = QueueMappingOverride

    @property
    def DefaultSettings(self):
        return self._DefaultSettings

    @DefaultSettings.setter
    def DefaultSettings(self, DefaultSettings):
        self._DefaultSettings = DefaultSettings


    def _deserialize(self, params):
        self._EnableLabel = params.get("EnableLabel")
        self._LabelDir = params.get("LabelDir")
        self._QueueMappingOverride = params.get("QueueMappingOverride")
        if params.get("DefaultSettings") is not None:
            self._DefaultSettings = []
            for item in params.get("DefaultSettings"):
                obj = DefaultSetting()
                obj._deserialize(item)
                self._DefaultSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbInfo(AbstractModel):
    """出参

    """

    def __init__(self):
        r"""
        :param _InstanceName: 数据库实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Ip: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _MemSize: 数据库内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Volume: 数据库磁盘规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param _Service: 服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param _PayType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: int
        :param _ExpireFlag: 过期标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireFlag: bool
        :param _Status: 数据库状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsAutoRenew: 续费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param _SerialNo: 数据库字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param _ZoneId: ZoneId
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _RegionId: RegionId
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        """
        self._InstanceName = None
        self._Ip = None
        self._Port = None
        self._MemSize = None
        self._Volume = None
        self._Service = None
        self._ExpireTime = None
        self._ApplyTime = None
        self._PayType = None
        self._ExpireFlag = None
        self._Status = None
        self._IsAutoRenew = None
        self._SerialNo = None
        self._ZoneId = None
        self._RegionId = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ExpireFlag(self):
        return self._ExpireFlag

    @ExpireFlag.setter
    def ExpireFlag(self, ExpireFlag):
        self._ExpireFlag = ExpireFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._MemSize = params.get("MemSize")
        self._Volume = params.get("Volume")
        self._Service = params.get("Service")
        self._ExpireTime = params.get("ExpireTime")
        self._ApplyTime = params.get("ApplyTime")
        self._PayType = params.get("PayType")
        self._ExpireFlag = params.get("ExpireFlag")
        self._Status = params.get("Status")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._SerialNo = params.get("SerialNo")
        self._ZoneId = params.get("ZoneId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExternalServiceInfo(AbstractModel):
    """当前集群共用组件与集群对应关系

    """

    def __init__(self):
        r"""
        :param _DependType: 依赖关系，0:被其他集群依赖，1:依赖其他集群
注意：此字段可能返回 null，表示取不到有效值。
        :type DependType: int
        :param _Service: 共用组件
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _ClusterId: 共用集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterStatus: 共用集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: int
        """
        self._DependType = None
        self._Service = None
        self._ClusterId = None
        self._ClusterStatus = None

    @property
    def DependType(self):
        return self._DependType

    @DependType.setter
    def DependType(self, DependType):
        self._DependType = DependType

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus


    def _deserialize(self, params):
        self._DependType = params.get("DependType")
        self._Service = params.get("Service")
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterIDToFlowID(AbstractModel):
    """集群id与流程id的mapping

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _FlowId: 流程id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        """
        self._ClusterId = None
        self._FlowId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstancesInfo(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        r"""
        :param _Id: ID号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Ftitle: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Ftitle: str
        :param _ClusterName: 集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _ZoneId: 地区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _VpcId: 集群VPCID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param _Status: 实例的状态码。取值范围：
<li>2：表示集群运行中。</li>
<li>3：表示集群创建中。</li>
<li>4：表示集群扩容中。</li>
<li>5：表示集群增加router节点中。</li>
<li>6：表示集群安装组件中。</li>
<li>7：表示集群执行命令中。</li>
<li>8：表示重启服务中。</li>
<li>9：表示进入维护中。</li>
<li>10：表示服务暂停中。</li>
<li>11：表示退出维护中。</li>
<li>12：表示退出暂停中。</li>
<li>13：表示配置下发中。</li>
<li>14：表示销毁集群中。</li>
<li>15：表示销毁core节点中。</li>
<li>16：销毁task节点中。</li>
<li>17：表示销毁router节点中。</li>
<li>18：表示更改webproxy密码中。</li>
<li>19：表示集群隔离中。</li>
<li>20：表示集群冲正中。</li>
<li>21：表示集群回收中。</li>
<li>22：表示变配等待中。</li>
<li>23：表示集群已隔离。</li>
<li>24：表示缩容节点中。</li>
<li>33：表示集群等待退费中。</li>
<li>34：表示集群已退费。</li>
<li>301：表示创建失败。</li>
<li>302：表示扩容失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _AddTime: 添加时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _RunTime: 已经运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunTime: str
        :param _Config: 集群产品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param _MasterIp: 主节点外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterIp: str
        :param _EmrVersion: EMR版本
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrVersion: str
        :param _ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _TradeVersion: 交易版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        :param _ResourceOrderId: 资源订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOrderId: int
        :param _IsTradeCluster: 是否计费集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTradeCluster: int
        :param _AlarmInfo: 集群错误状态告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: 是否采用新架构
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param _MetaDb: 元数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaDb: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HiveMetaDb: Hive元数据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HiveMetaDb: str
        :param _ServiceClass: 集群类型:EMR,CLICKHOUSE,DRUID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceClass: str
        :param _AliasInfo: 集群所有节点的别名序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasInfo: str
        :param _ProductId: 集群版本Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        :param _Zone: 地区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SceneName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneName: str
        :param _SceneServiceClass: 场景化集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneServiceClass: str
        :param _SceneEmrVersion: 场景化EMR版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneEmrVersion: str
        :param _DisplayName: 场景化集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _VpcName: vpc name
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _SubnetName: subnet name
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _ClusterExternalServiceInfo: 集群依赖关系
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterExternalServiceInfo: list of ClusterExternalServiceInfo
        :param _UniqVpcId: 集群vpcid 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网id 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _TopologyInfoList: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TopologyInfoList: list of TopologyInfo
        :param _IsMultiZoneCluster: 是否是跨AZ集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiZoneCluster: bool
        :param _IsCvmReplace: 是否开通异常节点自动补偿
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCvmReplace: bool
        :param _ClusterTitle: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTitle: str
        :param _ConfigDetail: 集群产品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigDetail: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigDetail`
        """
        self._Id = None
        self._ClusterId = None
        self._Ftitle = None
        self._ClusterName = None
        self._RegionId = None
        self._ZoneId = None
        self._AppId = None
        self._Uin = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AddTime = None
        self._RunTime = None
        self._Config = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._TradeVersion = None
        self._ResourceOrderId = None
        self._IsTradeCluster = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._MetaDb = None
        self._Tags = None
        self._HiveMetaDb = None
        self._ServiceClass = None
        self._AliasInfo = None
        self._ProductId = None
        self._Zone = None
        self._SceneName = None
        self._SceneServiceClass = None
        self._SceneEmrVersion = None
        self._DisplayName = None
        self._VpcName = None
        self._SubnetName = None
        self._ClusterExternalServiceInfo = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._TopologyInfoList = None
        self._IsMultiZoneCluster = None
        self._IsCvmReplace = None
        self._ClusterTitle = None
        self._ConfigDetail = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Ftitle(self):
        warnings.warn("parameter `Ftitle` is deprecated", DeprecationWarning) 

        return self._Ftitle

    @Ftitle.setter
    def Ftitle(self, Ftitle):
        warnings.warn("parameter `Ftitle` is deprecated", DeprecationWarning) 

        self._Ftitle = Ftitle

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def Config(self):
        warnings.warn("parameter `Config` is deprecated", DeprecationWarning) 

        return self._Config

    @Config.setter
    def Config(self, Config):
        warnings.warn("parameter `Config` is deprecated", DeprecationWarning) 

        self._Config = Config

    @property
    def MasterIp(self):
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def TradeVersion(self):
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion

    @property
    def ResourceOrderId(self):
        return self._ResourceOrderId

    @ResourceOrderId.setter
    def ResourceOrderId(self, ResourceOrderId):
        self._ResourceOrderId = ResourceOrderId

    @property
    def IsTradeCluster(self):
        return self._IsTradeCluster

    @IsTradeCluster.setter
    def IsTradeCluster(self, IsTradeCluster):
        self._IsTradeCluster = IsTradeCluster

    @property
    def AlarmInfo(self):
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def MetaDb(self):
        return self._MetaDb

    @MetaDb.setter
    def MetaDb(self, MetaDb):
        self._MetaDb = MetaDb

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HiveMetaDb(self):
        return self._HiveMetaDb

    @HiveMetaDb.setter
    def HiveMetaDb(self, HiveMetaDb):
        self._HiveMetaDb = HiveMetaDb

    @property
    def ServiceClass(self):
        return self._ServiceClass

    @ServiceClass.setter
    def ServiceClass(self, ServiceClass):
        self._ServiceClass = ServiceClass

    @property
    def AliasInfo(self):
        return self._AliasInfo

    @AliasInfo.setter
    def AliasInfo(self, AliasInfo):
        self._AliasInfo = AliasInfo

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneServiceClass(self):
        return self._SceneServiceClass

    @SceneServiceClass.setter
    def SceneServiceClass(self, SceneServiceClass):
        self._SceneServiceClass = SceneServiceClass

    @property
    def SceneEmrVersion(self):
        return self._SceneEmrVersion

    @SceneEmrVersion.setter
    def SceneEmrVersion(self, SceneEmrVersion):
        self._SceneEmrVersion = SceneEmrVersion

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def ClusterExternalServiceInfo(self):
        return self._ClusterExternalServiceInfo

    @ClusterExternalServiceInfo.setter
    def ClusterExternalServiceInfo(self, ClusterExternalServiceInfo):
        self._ClusterExternalServiceInfo = ClusterExternalServiceInfo

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def TopologyInfoList(self):
        return self._TopologyInfoList

    @TopologyInfoList.setter
    def TopologyInfoList(self, TopologyInfoList):
        self._TopologyInfoList = TopologyInfoList

    @property
    def IsMultiZoneCluster(self):
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsCvmReplace(self):
        return self._IsCvmReplace

    @IsCvmReplace.setter
    def IsCvmReplace(self, IsCvmReplace):
        self._IsCvmReplace = IsCvmReplace

    @property
    def ClusterTitle(self):
        return self._ClusterTitle

    @ClusterTitle.setter
    def ClusterTitle(self, ClusterTitle):
        self._ClusterTitle = ClusterTitle

    @property
    def ConfigDetail(self):
        return self._ConfigDetail

    @ConfigDetail.setter
    def ConfigDetail(self, ConfigDetail):
        self._ConfigDetail = ConfigDetail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ClusterId = params.get("ClusterId")
        self._Ftitle = params.get("Ftitle")
        self._ClusterName = params.get("ClusterName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self._Config = EmrProductConfigOutter()
            self._Config._deserialize(params.get("Config"))
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._TradeVersion = params.get("TradeVersion")
        self._ResourceOrderId = params.get("ResourceOrderId")
        self._IsTradeCluster = params.get("IsTradeCluster")
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HiveMetaDb = params.get("HiveMetaDb")
        self._ServiceClass = params.get("ServiceClass")
        self._AliasInfo = params.get("AliasInfo")
        self._ProductId = params.get("ProductId")
        self._Zone = params.get("Zone")
        self._SceneName = params.get("SceneName")
        self._SceneServiceClass = params.get("SceneServiceClass")
        self._SceneEmrVersion = params.get("SceneEmrVersion")
        self._DisplayName = params.get("DisplayName")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        if params.get("ClusterExternalServiceInfo") is not None:
            self._ClusterExternalServiceInfo = []
            for item in params.get("ClusterExternalServiceInfo"):
                obj = ClusterExternalServiceInfo()
                obj._deserialize(item)
                self._ClusterExternalServiceInfo.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("TopologyInfoList") is not None:
            self._TopologyInfoList = []
            for item in params.get("TopologyInfoList"):
                obj = TopologyInfo()
                obj._deserialize(item)
                self._TopologyInfoList.append(obj)
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsCvmReplace = params.get("IsCvmReplace")
        self._ClusterTitle = params.get("ClusterTitle")
        if params.get("ConfigDetail") is not None:
            self._ConfigDetail = EmrProductConfigDetail()
            self._ConfigDetail._deserialize(params.get("ConfigDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterSetting(AbstractModel):
    """集群配置。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 付费方式。
PREPAID 包年包月。
POSTPAID_BY_HOUR 按量计费，默认方式。
        :type InstanceChargeType: str
        :param _SupportHA: 是否为HA集群。
        :type SupportHA: bool
        :param _SecurityGroupIds: 集群所使用的安全组，目前仅支持一个。
        :type SecurityGroupIds: list of str
        :param _Placement: 实例位置。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _VPCSettings: 实例所在VPC。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _LoginSettings: 实例登录配置。
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _TagSpecification: 实例标签，示例：["{\"TagKey\":\"test-tag1\",\"TagValue\":\"001\"}","{\"TagKey\":\"test-tag2\",\"TagValue\":\"002\"}"]。
        :type TagSpecification: list of str
        :param _MetaDB: 元数据库配置。
        :type MetaDB: :class:`tencentcloud.emr.v20190103.models.MetaDbInfo`
        :param _ResourceSpec: 实例硬件配置。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResourceSpec`
        :param _PublicIpAssigned: 是否申请公网IP，默认为false。
        :type PublicIpAssigned: bool
        :param _InstanceChargePrepaid: 包年包月配置，只对包年包月集群生效。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _DisasterRecoverGroupIds: 集群置放群组。
        :type DisasterRecoverGroupIds: str
        :param _CbsEncryptFlag: 是否使用cbs加密。
        :type CbsEncryptFlag: bool
        :param _RemoteTcpDefaultPort: 是否使用远程登录，默认为false。
        :type RemoteTcpDefaultPort: bool
        """
        self._InstanceChargeType = None
        self._SupportHA = None
        self._SecurityGroupIds = None
        self._Placement = None
        self._VPCSettings = None
        self._LoginSettings = None
        self._TagSpecification = None
        self._MetaDB = None
        self._ResourceSpec = None
        self._PublicIpAssigned = None
        self._InstanceChargePrepaid = None
        self._DisasterRecoverGroupIds = None
        self._CbsEncryptFlag = None
        self._RemoteTcpDefaultPort = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def MetaDB(self):
        return self._MetaDB

    @MetaDB.setter
    def MetaDB(self, MetaDB):
        self._MetaDB = MetaDB

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def CbsEncryptFlag(self):
        return self._CbsEncryptFlag

    @CbsEncryptFlag.setter
    def CbsEncryptFlag(self, CbsEncryptFlag):
        self._CbsEncryptFlag = CbsEncryptFlag

    @property
    def RemoteTcpDefaultPort(self):
        return self._RemoteTcpDefaultPort

    @RemoteTcpDefaultPort.setter
    def RemoteTcpDefaultPort(self, RemoteTcpDefaultPort):
        self._RemoteTcpDefaultPort = RemoteTcpDefaultPort


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SupportHA = params.get("SupportHA")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._TagSpecification = params.get("TagSpecification")
        if params.get("MetaDB") is not None:
            self._MetaDB = MetaDbInfo()
            self._MetaDB._deserialize(params.get("MetaDB"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = JobFlowResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._CbsEncryptFlag = params.get("CbsEncryptFlag")
        self._RemoteTcpDefaultPort = params.get("RemoteTcpDefaultPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentBasicRestartInfo(AbstractModel):
    """操作的进程范围

    """

    def __init__(self):
        r"""
        :param _ComponentName: 进程名，必填，如NameNode
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentName: str
        :param _IpList: 操作的IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpList: list of str
        """
        self._ComponentName = None
        self._IpList = None

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._ComponentName = params.get("ComponentName")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigModifyInfoV2(AbstractModel):
    """资源调度 - 队列修改信息

    """

    def __init__(self):
        r"""
        :param _OpType: 操作类型，可选值：

- 0：新建队列
- 1：编辑-全量覆盖
- 2：新建子队列
- 3：删除
- 4：克隆，与新建子队列的行为一样，特别的对于`fair`，可以复制子队列到新建队列
- 6：编辑-增量更新
注意：此字段可能返回 null，表示取不到有效值。
        :type OpType: int
        :param _Name: 队列名称，不支持修改。
        :type Name: str
        :param _ParentId: 新建队列 传root的MyId；新建子队列 传 选中队列的 myId；克隆 要传 选中队列 parentId
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _MyId: 编辑、删除 传选中队列的 myId。克隆只有在调度器是`fair`时才需要传，用来复制子队列到新队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type MyId: str
        :param _BasicParams: 基础配置信息。key的取值与**DescribeYarnQueue**返回的字段一致。
###### 公平调度器
key的取值信息如下：

- type，父队列，取值为 **parent** 或 **null**
- aclSubmitApps，提交访问控制，取值为**AclForYarnQueue类型的json串**或**null**
- aclAdministerApps，管理访问控制，取值为**AclForYarnQueue类型的json串**或**null**
- minSharePreemptionTimeout，最小共享优先权超时时间，取值为**数字字符串**或**null**
- fairSharePreemptionTimeout，公平份额抢占超时时间，取值为**数字字符串**或**null**
- fairSharePreemptionThreshold，公平份额抢占阈值，取值为**数字字符串**或**null**，其中数字的范围是（0，1]
- allowPreemptionFrom，抢占模式，取值为**布尔字符串**或**null**
- schedulingPolicy，调度策略，取值为**drf**、**fair**、**fifo**或**null**

```
type AclForYarnQueue struct {
	User  *string `json:"user"` //用户名
	Group *string `json:"group"`//组名
}
```
###### 容量调度器
key的取值信息如下：

- state，队列状态，取值为**STOPPED**或**RUNNING**
- default-node-label-expression，默认标签表达式，取值为**标签**或**null**
- acl_submit_applications，提交访问控制，取值为**AclForYarnQueue类型的json串**或**null**
- acl_administer_queue，管理访问控制，取值为**AclForYarnQueue类型的json串**或**null**
- maximum-allocation-mb，分配Container最大内存数量，取值为**数字字符串**或**null**
- maximum-allocation-vcores，Container最大vCore数量，取值为**数字字符串**或**null**
```
type AclForYarnQueue struct {
	User  *string `json:"user"` //用户名
	Group *string `json:"group"`//组名
}
```
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicParams: :class:`tencentcloud.emr.v20190103.models.ItemSeq`
        :param _ConfigSetParams: 配置集信息，取值见该复杂类型的参数说明。配置集是计划模式在队列中表现，表示的是不同时间段不同的配置值，所有队列的配置集名称都一样，对于单个队列，每个配置集中的标签与参数都一样，只是参数值不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigSetParams: list of ConfigSetInfo
        :param _DeleteLables: 容量调度专用，`OpType`为`6`时才生效，表示要删除这个队列中的哪些标签。优先级高于ConfigSetParams中的LabelParams。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteLables: list of str
        """
        self._OpType = None
        self._Name = None
        self._ParentId = None
        self._MyId = None
        self._BasicParams = None
        self._ConfigSetParams = None
        self._DeleteLables = None

    @property
    def OpType(self):
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def MyId(self):
        return self._MyId

    @MyId.setter
    def MyId(self, MyId):
        self._MyId = MyId

    @property
    def BasicParams(self):
        return self._BasicParams

    @BasicParams.setter
    def BasicParams(self, BasicParams):
        self._BasicParams = BasicParams

    @property
    def ConfigSetParams(self):
        return self._ConfigSetParams

    @ConfigSetParams.setter
    def ConfigSetParams(self, ConfigSetParams):
        self._ConfigSetParams = ConfigSetParams

    @property
    def DeleteLables(self):
        return self._DeleteLables

    @DeleteLables.setter
    def DeleteLables(self, DeleteLables):
        self._DeleteLables = DeleteLables


    def _deserialize(self, params):
        self._OpType = params.get("OpType")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._MyId = params.get("MyId")
        if params.get("BasicParams") is not None:
            self._BasicParams = ItemSeq()
            self._BasicParams._deserialize(params.get("BasicParams"))
        if params.get("ConfigSetParams") is not None:
            self._ConfigSetParams = []
            for item in params.get("ConfigSetParams"):
                obj = ConfigSetInfo()
                obj._deserialize(item)
                self._ConfigSetParams.append(obj)
        self._DeleteLables = params.get("DeleteLables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSetInfo(AbstractModel):
    """资源调度-配置集信息

    """

    def __init__(self):
        r"""
        :param _ConfigSet: 配置集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigSet: str
        :param _LabelParams: 容量调度器会使用，里面设置了标签相关的配置。key的取值与**DescribeYarnQueue**返回的字段一致。
key的取值信息如下：
- labelName，标签名称，标签管理里的标签。
- capacity，容量，取值为**数字字符串**
- maximum-capacity，最大容量，取值为**数字字符串**
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelParams: list of ItemSeq
        :param _BasicParams: 设置配置集相关的参数。key的取值与**DescribeYarnQueue**返回的字段一致。
###### 公平调度器
key的取值信息如下：
- minResources，最大资源量，取值为**YarnResource类型的json串**或**null**
- maxResources，最大资源量，取值为**YarnResource类型的json串**或**null**
- maxChildResources，能够分配给为未声明子队列的最大资源量，取值为**数字字符串**或**null**
- maxRunningApps，最高可同时处于运行的App数量，取值为**数字字符串**或**null**
- weight，权重，取值为**数字字符串**或**null**
- maxAMShare，App Master最大份额，取值为**数字字符串**或**null**，其中数字的范围是[0，1]或-1

```
type YarnResource struct {
	Vcores *int `json:"vcores"`
	Memory *int `json:"memory"`
	Type *string `json:"type"` // 取值为`percent`或`null`当值为`percent`时，表示使用的百分比，否则就是使用的绝对数值。只有maxResources、maxChildResources才可以取值为`percent`
}
```

###### 容量调度器
key的取值信息如下：
- minimum-user-limit-percent，用户最小容量，取值为**YarnResource类型的json串**或**null**，其中数字的范围是[0，100]
- user-limit-factor，用户资源因子，取值为**YarnResource类型的json串**或**null**
- maximum-applications，最大应用数Max-Applications，取值为**数字字符串**或**null**，其中数字为正整数
- maximum-am-resource-percent，最大AM比例，取值为**数字字符串**或**null**，其中数字的范围是[0，1]或-1
- default-application-priority，资源池优先级，取值为**数字字符串**或**null**，其中数字为正整数
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicParams: list of Item
        """
        self._ConfigSet = None
        self._LabelParams = None
        self._BasicParams = None

    @property
    def ConfigSet(self):
        return self._ConfigSet

    @ConfigSet.setter
    def ConfigSet(self, ConfigSet):
        self._ConfigSet = ConfigSet

    @property
    def LabelParams(self):
        return self._LabelParams

    @LabelParams.setter
    def LabelParams(self, LabelParams):
        self._LabelParams = LabelParams

    @property
    def BasicParams(self):
        return self._BasicParams

    @BasicParams.setter
    def BasicParams(self, BasicParams):
        self._BasicParams = BasicParams


    def _deserialize(self, params):
        self._ConfigSet = params.get("ConfigSet")
        if params.get("LabelParams") is not None:
            self._LabelParams = []
            for item in params.get("LabelParams"):
                obj = ItemSeq()
                obj._deserialize(item)
                self._LabelParams.append(obj)
        if params.get("BasicParams") is not None:
            self._BasicParams = []
            for item in params.get("BasicParams"):
                obj = Item()
                obj._deserialize(item)
                self._BasicParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Configuration(AbstractModel):
    """自定义配置参数

    """

    def __init__(self):
        r"""
        :param _Classification: 配置文件名，支持SPARK、HIVE、HDFS、YARN的部分配置文件自定义。
        :type Classification: str
        :param _Properties: 配置参数通过KV的形式传入，部分文件支持自定义，可以通过特殊的键"content"传入所有内容。
        :type Properties: str
        """
        self._Classification = None
        self._Properties = None

    @property
    def Classification(self):
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._Classification = params.get("Classification")
        self._Properties = params.get("Properties")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductVersion: EMR产品版本名称如EMR-V2.3.0 表示2.3.0版本的EMR， 当前支持产品版本名称查询：[产品版本名称](https://cloud.tencent.com/document/product/589/66338)
        :type ProductVersion: str
        :param _EnableSupportHAFlag: 是否开启节点高可用。取值范围：
<li>true：表示开启节点高可用。</li>
<li>false：表示不开启节点高可用。</li>
        :type EnableSupportHAFlag: bool
        :param _InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：按小时后付费。</li>
        :type InstanceChargeType: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _SceneSoftwareConfig: 集群应用场景以及支持部署组件配置
        :type SceneSoftwareConfig: :class:`tencentcloud.emr.v20190103.models.SceneSoftwareConfig`
        :param _InstanceChargePrepaid: 即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _SecurityGroupIds: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。
        :type SecurityGroupIds: list of str
        :param _ScriptBootstrapActionConfig: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _ClientToken: 唯一随机标识，时效性为5分钟，需要调用者指定 防止客户端重复创建资源，例如 a9a90aa6-****-****-****-fae360632808
        :type ClientToken: str
        :param _NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。
        :type NeedMasterWan: str
        :param _EnableRemoteLoginFlag: 是否开启外网远程登录。（在SecurityGroupId不为空时，该参数无效）不填默认为不开启 取值范围：
<li>true：表示开启</li>
<li>false：表示不开启</li>
        :type EnableRemoteLoginFlag: bool
        :param _EnableKerberosFlag: 是否开启Kerberos认证。默认不开启 取值范围：
<li>true：表示开启</li>
<li>false：表示不开启</li>
        :type EnableKerberosFlag: bool
        :param _CustomConf: [自定义软件配置](https://cloud.tencent.com/document/product/589/35655?from_cn_redirect=1)
        :type CustomConf: str
        :param _Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/product/213/17810)的返回值中的DisasterRecoverGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _EnableCbsEncryptFlag: 是否开启集群维度CBS加密。默认不加密 取值范围：
<li>true：表示加密</li>
<li>false：表示不加密</li>
        :type EnableCbsEncryptFlag: bool
        :param _MetaDBInfo: MetaDB信息，当MetaType选择EMR_NEW_META时，MetaDataJdbcUrl MetaDataUser MetaDataPass UnifyMetaInstanceId不用填
当MetaType选择EMR_EXIT_META时，填写UnifyMetaInstanceId
当MetaType选择USER_CUSTOM_META时，填写MetaDataJdbcUrl MetaDataUser MetaDataPass
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaDBInfo`
        :param _DependService: 共享组件信息
        :type DependService: list of DependService
        :param _ZoneResourceConfiguration: 节点资源的规格，有几个可用区，就填几个，按顺序第一个为主可用区，第二个为备可用区，第三个为仲裁可用区。如果没有开启跨AZ，则长度为1即可。
        :type ZoneResourceConfiguration: list of ZoneResourceConfiguration
        :param _CosBucket: cos桶路径，创建StarRocks存算分离集群时用到
        :type CosBucket: str
        """
        self._ProductVersion = None
        self._EnableSupportHAFlag = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._LoginSettings = None
        self._SceneSoftwareConfig = None
        self._InstanceChargePrepaid = None
        self._SecurityGroupIds = None
        self._ScriptBootstrapActionConfig = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._EnableRemoteLoginFlag = None
        self._EnableKerberosFlag = None
        self._CustomConf = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._EnableCbsEncryptFlag = None
        self._MetaDBInfo = None
        self._DependService = None
        self._ZoneResourceConfiguration = None
        self._CosBucket = None

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def EnableSupportHAFlag(self):
        return self._EnableSupportHAFlag

    @EnableSupportHAFlag.setter
    def EnableSupportHAFlag(self, EnableSupportHAFlag):
        self._EnableSupportHAFlag = EnableSupportHAFlag

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SceneSoftwareConfig(self):
        return self._SceneSoftwareConfig

    @SceneSoftwareConfig.setter
    def SceneSoftwareConfig(self, SceneSoftwareConfig):
        self._SceneSoftwareConfig = SceneSoftwareConfig

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ScriptBootstrapActionConfig(self):
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def EnableRemoteLoginFlag(self):
        return self._EnableRemoteLoginFlag

    @EnableRemoteLoginFlag.setter
    def EnableRemoteLoginFlag(self, EnableRemoteLoginFlag):
        self._EnableRemoteLoginFlag = EnableRemoteLoginFlag

    @property
    def EnableKerberosFlag(self):
        return self._EnableKerberosFlag

    @EnableKerberosFlag.setter
    def EnableKerberosFlag(self, EnableKerberosFlag):
        self._EnableKerberosFlag = EnableKerberosFlag

    @property
    def CustomConf(self):
        return self._CustomConf

    @CustomConf.setter
    def CustomConf(self, CustomConf):
        self._CustomConf = CustomConf

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def EnableCbsEncryptFlag(self):
        return self._EnableCbsEncryptFlag

    @EnableCbsEncryptFlag.setter
    def EnableCbsEncryptFlag(self, EnableCbsEncryptFlag):
        self._EnableCbsEncryptFlag = EnableCbsEncryptFlag

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def DependService(self):
        return self._DependService

    @DependService.setter
    def DependService(self, DependService):
        self._DependService = DependService

    @property
    def ZoneResourceConfiguration(self):
        return self._ZoneResourceConfiguration

    @ZoneResourceConfiguration.setter
    def ZoneResourceConfiguration(self, ZoneResourceConfiguration):
        self._ZoneResourceConfiguration = ZoneResourceConfiguration

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket


    def _deserialize(self, params):
        self._ProductVersion = params.get("ProductVersion")
        self._EnableSupportHAFlag = params.get("EnableSupportHAFlag")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("SceneSoftwareConfig") is not None:
            self._SceneSoftwareConfig = SceneSoftwareConfig()
            self._SceneSoftwareConfig._deserialize(params.get("SceneSoftwareConfig"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._EnableRemoteLoginFlag = params.get("EnableRemoteLoginFlag")
        self._EnableKerberosFlag = params.get("EnableKerberosFlag")
        self._CustomConf = params.get("CustomConf")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._EnableCbsEncryptFlag = params.get("EnableCbsEncryptFlag")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaDBInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        if params.get("DependService") is not None:
            self._DependService = []
            for item in params.get("DependService"):
                obj = DependService()
                obj._deserialize(item)
                self._DependService.append(obj)
        if params.get("ZoneResourceConfiguration") is not None:
            self._ZoneResourceConfiguration = []
            for item in params.get("ZoneResourceConfiguration"):
                obj = ZoneResourceConfiguration()
                obj._deserialize(item)
                self._ZoneResourceConfiguration.append(obj)
        self._CosBucket = params.get("CosBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
51:表示STARROCKS-V1.4.0
54:表示STARROCKS-V2.0.0
27:表示KAFKA-V1.0.0
50:表示KAFKA-V2.0.0
16:表示EMR-V2.3.0
20:表示EMR-V2.5.0
30:表示EMR-V2.6.0
38:表示EMR-V2.7.0
25:表示EMR-V3.1.0
33:表示EMR-V3.2.1
34:表示EMR-V3.3.0
37:表示EMR-V3.4.0
44:表示EMR-V3.5.0
53:表示EMR-V3.6.0
        :type ProductId: int
        :param _Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）对应不同可选组件列表，不同产品版本可选组件列表查询：[组件版本](https://cloud.tencent.com/document/product/589/20279) ；
填写实例值：hive、flink。
        :type Software: list of str
        :param _SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param _InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>
        :type InstanceName: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _ResourceSpec: 节点资源的规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _COSSettings: 开启COS访问需要设置的参数。
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _SgId: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。
        :type SgId: str
        :param _PreExecutedFileSettings: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _AutoRenew: 包年包月实例是否自动续费。取值范围：
<li>0：表示不自动续费。</li>
<li>1：表示自动续费。</li>
        :type AutoRenew: int
        :param _ClientToken: 唯一随机标识，时效5分钟，需要调用者指定 防止客户端重新创建资源，例如 a9a90aa6-****-****-****-fae36063280
        :type ClientToken: str
        :param _NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。
        :type NeedMasterWan: str
        :param _RemoteLoginAtCreate: 是否需要开启外网远程登录，即22号端口。在SgId不为空时，该参数无效。
        :type RemoteLoginAtCreate: int
        :param _CheckSecurity: 是否开启安全集群。0表示不开启，非0表示开启。
        :type CheckSecurity: int
        :param _ExtendFsField: 访问外部文件系统。
        :type ExtendFsField: str
        :param _Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/product/213/15486 ) 的返回值中的SecurityGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _CbsEncrypt: 集群维度CBS加密盘，默认0表示不加密，1表示加密
        :type CbsEncrypt: int
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_DEFAULT_META：表示集群默认创建</li>
<li>EMR_EXIST_META：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ApplicationRole: 自定义应用角色。
        :type ApplicationRole: str
        :param _SceneName: 场景化取值：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: 共享组件信息
        :type ExternalService: list of ExternalService
        :param _VersionID: 如果为0，则MultiZone、MultiDeployStrategy、MultiZoneSettings是disable的状态，如果为1，则废弃ResourceSpec，使用MultiZoneSettings。
        :type VersionID: int
        :param _MultiZone: true表示开启跨AZ部署；仅为新建集群时的用户参数，后续不支持调整。
        :type MultiZone: bool
        :param _MultiZoneSettings: 节点资源的规格，有几个可用区，就填几个，按顺序第一个为主可用区，第二个为备可用区，第三个为仲裁可用区。如果没有开启跨AZ，则长度为1即可。
        :type MultiZoneSettings: list of MultiZoneSetting
        :param _CosBucket: cos桶路径，创建StarRocks存算分离集群时用到
        :type CosBucket: str
        """
        self._ProductId = None
        self._Software = None
        self._SupportHA = None
        self._InstanceName = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._LoginSettings = None
        self._VPCSettings = None
        self._ResourceSpec = None
        self._COSSettings = None
        self._Placement = None
        self._SgId = None
        self._PreExecutedFileSettings = None
        self._AutoRenew = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._RemoteLoginAtCreate = None
        self._CheckSecurity = None
        self._ExtendFsField = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._CbsEncrypt = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ApplicationRole = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZone = None
        self._MultiZoneSettings = None
        self._CosBucket = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def COSSettings(self):
        return self._COSSettings

    @COSSettings.setter
    def COSSettings(self, COSSettings):
        self._COSSettings = COSSettings

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def SgId(self):
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def PreExecutedFileSettings(self):
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def RemoteLoginAtCreate(self):
        return self._RemoteLoginAtCreate

    @RemoteLoginAtCreate.setter
    def RemoteLoginAtCreate(self, RemoteLoginAtCreate):
        self._RemoteLoginAtCreate = RemoteLoginAtCreate

    @property
    def CheckSecurity(self):
        return self._CheckSecurity

    @CheckSecurity.setter
    def CheckSecurity(self, CheckSecurity):
        self._CheckSecurity = CheckSecurity

    @property
    def ExtendFsField(self):
        return self._ExtendFsField

    @ExtendFsField.setter
    def ExtendFsField(self, ExtendFsField):
        self._ExtendFsField = ExtendFsField

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def CbsEncrypt(self):
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZone(self):
        return self._MultiZone

    @MultiZone.setter
    def MultiZone(self, MultiZone):
        self._MultiZone = MultiZone

    @property
    def MultiZoneSettings(self):
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Software = params.get("Software")
        self._SupportHA = params.get("SupportHA")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("COSSettings") is not None:
            self._COSSettings = COSSettings()
            self._COSSettings._deserialize(params.get("COSSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._AutoRenew = params.get("AutoRenew")
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self._CheckSecurity = params.get("CheckSecurity")
        self._ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ApplicationRole = params.get("ApplicationRole")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        self._MultiZone = params.get("MultiZone")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        self._CosBucket = params.get("CosBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateSLInstanceRequest(AbstractModel):
    """CreateSLInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _PayMode: 实例计费模式，0表示后付费，即按量计费。
        :type PayMode: int
        :param _DiskType: 实例存储类型，填写CLOUD_HSSD，表示性能云存储。
        :type DiskType: str
        :param _DiskSize: 实例单节点磁盘容量，单位GB，单节点磁盘容量需大于等于100，小于等于10000，容量调整步长为20。
        :type DiskSize: int
        :param _NodeType: 实例节点规格，可填写4C16G、8C32G、16C64G、32C128G，不区分大小写。
        :type NodeType: str
        :param _ZoneSettings: 实例可用区详细配置，当前支持多可用区，可用区数量只能为1或3，包含区域名称，VPC信息、节点数量，其中所有区域节点总数需大于等于3，小于等于50。
        :type ZoneSettings: list of ZoneSetting
        :param _Tags: 实例要绑定的标签列表。
        :type Tags: list of Tag
        """
        self._InstanceName = None
        self._PayMode = None
        self._DiskType = None
        self._DiskSize = None
        self._NodeType = None
        self._ZoneSettings = None
        self._Tags = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ZoneSettings(self):
        return self._ZoneSettings

    @ZoneSettings.setter
    def ZoneSettings(self, ZoneSettings):
        self._ZoneSettings = ZoneSettings

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._NodeType = params.get("NodeType")
        if params.get("ZoneSettings") is not None:
            self._ZoneSettings = []
            for item in params.get("ZoneSettings"):
                obj = ZoneSetting()
                obj._deserialize(item)
                self._ZoneSettings.append(obj)
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
        


class CreateSLInstanceResponse(AbstractModel):
    """CreateSLInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一标识符（字符串表示）
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CustomMetaDBInfo(AbstractModel):
    """用户Hive-MetaDB信息

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，示例: jdbc:mysql://10.10.10.10:3306/dbname
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: 自定义MetaDB用户名
        :type MetaDataUser: str
        :param _MetaDataPass: 自定义MetaDB密码
        :type MetaDataPass: str
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_DEFAULT_META：表示集群默认创建</li>
<li>EMR_EXIST_META：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None

    @property
    def MetaDataJdbcUrl(self):
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomMetaInfo(AbstractModel):
    """用户自建Hive-MetaDB信息

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，请以 jdbc:mysql:// 开头
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: 自定义MetaDB用户名
        :type MetaDataUser: str
        :param _MetaDataPass: 自定义MetaDB密码
        :type MetaDataPass: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None

    @property
    def MetaDataJdbcUrl(self):
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomServiceDefine(AbstractModel):
    """共用自建组件参数

    """

    def __init__(self):
        r"""
        :param _Name: 自定义参数key
        :type Name: str
        :param _Value: 自定义参数value
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
        


class DayRepeatStrategy(AbstractModel):
    """弹性扩缩容按天重复任务描述

    """

    def __init__(self):
        r"""
        :param _ExecuteAtTimeOfDay: 重复任务执行的具体时刻，例如"01:02:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteAtTimeOfDay: str
        :param _Step: 每隔Step天执行一次
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: int
        """
        self._ExecuteAtTimeOfDay = None
        self._Step = None

    @property
    def ExecuteAtTimeOfDay(self):
        return self._ExecuteAtTimeOfDay

    @ExecuteAtTimeOfDay.setter
    def ExecuteAtTimeOfDay(self, ExecuteAtTimeOfDay):
        self._ExecuteAtTimeOfDay = ExecuteAtTimeOfDay

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step


    def _deserialize(self, params):
        self._ExecuteAtTimeOfDay = params.get("ExecuteAtTimeOfDay")
        self._Step = params.get("Step")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultSetting(AbstractModel):
    """资源调度的默认设置

    """

    def __init__(self):
        r"""
        :param _Name: 名称，作为入参的key
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Prompt: 提示
        :type Prompt: str
        :param _Key: key，用于展示，该配置对应与配置文件中的配置项
        :type Key: str
        :param _Value: Name对应的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Desc = None
        self._Prompt = None
        self._Key = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

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
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Prompt = params.get("Prompt")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScaleStrategyRequest(AbstractModel):
    """DeleteAutoScaleStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StrategyType: 自动扩缩容规则类型，1表示按照负载指标扩缩容，2表示按照时间规则扩缩容。
        :type StrategyType: int
        :param _StrategyId: 规则ID。
        :type StrategyId: int
        :param _GroupId: 伸缩组Id
        :type GroupId: int
        """
        self._InstanceId = None
        self._StrategyType = None
        self._StrategyId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyType = params.get("StrategyType")
        self._StrategyId = params.get("StrategyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScaleStrategyResponse(AbstractModel):
    """DeleteAutoScaleStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteUserManagerUserListRequest(AbstractModel):
    """DeleteUserManagerUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _UserNameList: 集群用户名列表
        :type UserNameList: list of str
        :param _TkeClusterId: tke/eks集群id，容器集群传
        :type TkeClusterId: str
        :param _DisplayStrategy: 默认空，容器版传"native"
        :type DisplayStrategy: str
        :param _UserGroupList: 用户组
        :type UserGroupList: list of UserAndGroup
        :param _DeleteHomeDir: 是否删除家目录，只针对cvm集群
        :type DeleteHomeDir: bool
        """
        self._InstanceId = None
        self._UserNameList = None
        self._TkeClusterId = None
        self._DisplayStrategy = None
        self._UserGroupList = None
        self._DeleteHomeDir = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserNameList(self):
        return self._UserNameList

    @UserNameList.setter
    def UserNameList(self, UserNameList):
        self._UserNameList = UserNameList

    @property
    def TkeClusterId(self):
        return self._TkeClusterId

    @TkeClusterId.setter
    def TkeClusterId(self, TkeClusterId):
        self._TkeClusterId = TkeClusterId

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def UserGroupList(self):
        return self._UserGroupList

    @UserGroupList.setter
    def UserGroupList(self, UserGroupList):
        self._UserGroupList = UserGroupList

    @property
    def DeleteHomeDir(self):
        return self._DeleteHomeDir

    @DeleteHomeDir.setter
    def DeleteHomeDir(self, DeleteHomeDir):
        self._DeleteHomeDir = DeleteHomeDir


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserNameList = params.get("UserNameList")
        self._TkeClusterId = params.get("TkeClusterId")
        self._DisplayStrategy = params.get("DisplayStrategy")
        if params.get("UserGroupList") is not None:
            self._UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserAndGroup()
                obj._deserialize(item)
                self._UserGroupList.append(obj)
        self._DeleteHomeDir = params.get("DeleteHomeDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserManagerUserListResponse(AbstractModel):
    """DeleteUserManagerUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DependService(AbstractModel):
    """共用组件信息

    """

    def __init__(self):
        r"""
        :param _ServiceName: 共用组件名
        :type ServiceName: str
        :param _InstanceId: 共用组件集群
        :type InstanceId: str
        """
        self._ServiceName = None
        self._InstanceId = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployYarnConfRequest(AbstractModel):
    """DeployYarnConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployYarnConfResponse(AbstractModel):
    """DeployYarnConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 启动流程后的流程ID，可以使用[DescribeClusterFlowStatusDetail](https://cloud.tencent.com/document/product/589/107224)接口来获取流程状态
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DescribeAutoScaleGroupGlobalConfRequest(AbstractModel):
    """DescribeAutoScaleGroupGlobalConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScaleGroupGlobalConfResponse(AbstractModel):
    """DescribeAutoScaleGroupGlobalConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupGlobalConfs: 集群所有伸缩组全局信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupGlobalConfs: list of GroupGlobalConfs
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupGlobalConfs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GroupGlobalConfs(self):
        return self._GroupGlobalConfs

    @GroupGlobalConfs.setter
    def GroupGlobalConfs(self, GroupGlobalConfs):
        self._GroupGlobalConfs = GroupGlobalConfs

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
        if params.get("GroupGlobalConfs") is not None:
            self._GroupGlobalConfs = []
            for item in params.get("GroupGlobalConfs"):
                obj = GroupGlobalConfs()
                obj._deserialize(item)
                self._GroupGlobalConfs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoScaleRecordsRequest(AbstractModel):
    """DescribeAutoScaleRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Filters: 记录过滤参数，目前仅能为“StartTime”,“EndTime”和“StrategyName”。StartTime和EndTime支持2006-01-02 15:04:05 或者2006/01/02 15:04:05的时间格式
        :type Filters: list of KeyValue
        :param _Offset: 分页参数。
        :type Offset: int
        :param _Limit: 分页参数。最大支持100
        :type Limit: int
        :param _RecordSource: 表示是自动(0)还是托管伸缩(1)
        :type RecordSource: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._RecordSource = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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

    @property
    def RecordSource(self):
        return self._RecordSource

    @RecordSource.setter
    def RecordSource(self, RecordSource):
        self._RecordSource = RecordSource


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RecordSource = params.get("RecordSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScaleRecordsResponse(AbstractModel):
    """DescribeAutoScaleRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总扩缩容记录数。
        :type TotalCount: int
        :param _RecordList: 记录列表。
        :type RecordList: list of AutoScaleRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = AutoScaleRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScaleStrategiesRequest(AbstractModel):
    """DescribeAutoScaleStrategies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _GroupId: 伸缩组id
        :type GroupId: int
        """
        self._InstanceId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScaleStrategiesResponse(AbstractModel):
    """DescribeAutoScaleStrategies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadAutoScaleStrategies: 按负载伸缩规则
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadAutoScaleStrategies: list of LoadAutoScaleStrategy
        :param _TimeBasedAutoScaleStrategies: 按时间伸缩规则
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeBasedAutoScaleStrategies: list of TimeAutoScaleStrategy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadAutoScaleStrategies = None
        self._TimeBasedAutoScaleStrategies = None
        self._RequestId = None

    @property
    def LoadAutoScaleStrategies(self):
        return self._LoadAutoScaleStrategies

    @LoadAutoScaleStrategies.setter
    def LoadAutoScaleStrategies(self, LoadAutoScaleStrategies):
        self._LoadAutoScaleStrategies = LoadAutoScaleStrategies

    @property
    def TimeBasedAutoScaleStrategies(self):
        return self._TimeBasedAutoScaleStrategies

    @TimeBasedAutoScaleStrategies.setter
    def TimeBasedAutoScaleStrategies(self, TimeBasedAutoScaleStrategies):
        self._TimeBasedAutoScaleStrategies = TimeBasedAutoScaleStrategies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadAutoScaleStrategies") is not None:
            self._LoadAutoScaleStrategies = []
            for item in params.get("LoadAutoScaleStrategies"):
                obj = LoadAutoScaleStrategy()
                obj._deserialize(item)
                self._LoadAutoScaleStrategies.append(obj)
        if params.get("TimeBasedAutoScaleStrategies") is not None:
            self._TimeBasedAutoScaleStrategies = []
            for item in params.get("TimeBasedAutoScaleStrategies"):
                obj = TimeAutoScaleStrategy()
                obj._deserialize(item)
                self._TimeBasedAutoScaleStrategies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterFlowStatusDetailRequest(AbstractModel):
    """DescribeClusterFlowStatusDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: EMR实例ID
        :type InstanceId: str
        :param _FlowParam: 流程相关参数
        :type FlowParam: :class:`tencentcloud.emr.v20190103.models.FlowParam`
        :param _NeedExtraDetail: 是否返回任务额外信息
默认: false
        :type NeedExtraDetail: bool
        """
        self._InstanceId = None
        self._FlowParam = None
        self._NeedExtraDetail = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowParam(self):
        return self._FlowParam

    @FlowParam.setter
    def FlowParam(self, FlowParam):
        self._FlowParam = FlowParam

    @property
    def NeedExtraDetail(self):
        return self._NeedExtraDetail

    @NeedExtraDetail.setter
    def NeedExtraDetail(self, NeedExtraDetail):
        self._NeedExtraDetail = NeedExtraDetail


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FlowParam") is not None:
            self._FlowParam = FlowParam()
            self._FlowParam._deserialize(params.get("FlowParam"))
        self._NeedExtraDetail = params.get("NeedExtraDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterFlowStatusDetailResponse(AbstractModel):
    """DescribeClusterFlowStatusDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StageDetails: 任务步骤详情
注意：此字段可能返回 null，表示取不到有效值。
        :type StageDetails: list of StageInfoDetail
        :param _FlowDesc: 任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDesc: list of FlowParamsDesc
        :param _FlowName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param _FlowTotalProgress: 总任务流程进度：
例如：0.8
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowTotalProgress: float
        :param _FlowTotalStatus: 定义流程总状态：
0:初始化，
1:运行中，
2:完成，
3:完成（存在跳过步骤），
-1:失败，
-3:阻塞，
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowTotalStatus: int
        :param _FlowExtraDetail: 流程额外信息
NeedExtraDetail为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowExtraDetail: list of FlowExtraDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StageDetails = None
        self._FlowDesc = None
        self._FlowName = None
        self._FlowTotalProgress = None
        self._FlowTotalStatus = None
        self._FlowExtraDetail = None
        self._RequestId = None

    @property
    def StageDetails(self):
        return self._StageDetails

    @StageDetails.setter
    def StageDetails(self, StageDetails):
        self._StageDetails = StageDetails

    @property
    def FlowDesc(self):
        return self._FlowDesc

    @FlowDesc.setter
    def FlowDesc(self, FlowDesc):
        self._FlowDesc = FlowDesc

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowTotalProgress(self):
        return self._FlowTotalProgress

    @FlowTotalProgress.setter
    def FlowTotalProgress(self, FlowTotalProgress):
        self._FlowTotalProgress = FlowTotalProgress

    @property
    def FlowTotalStatus(self):
        return self._FlowTotalStatus

    @FlowTotalStatus.setter
    def FlowTotalStatus(self, FlowTotalStatus):
        self._FlowTotalStatus = FlowTotalStatus

    @property
    def FlowExtraDetail(self):
        return self._FlowExtraDetail

    @FlowExtraDetail.setter
    def FlowExtraDetail(self, FlowExtraDetail):
        self._FlowExtraDetail = FlowExtraDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StageDetails") is not None:
            self._StageDetails = []
            for item in params.get("StageDetails"):
                obj = StageInfoDetail()
                obj._deserialize(item)
                self._StageDetails.append(obj)
        if params.get("FlowDesc") is not None:
            self._FlowDesc = []
            for item in params.get("FlowDesc"):
                obj = FlowParamsDesc()
                obj._deserialize(item)
                self._FlowDesc.append(obj)
        self._FlowName = params.get("FlowName")
        self._FlowTotalProgress = params.get("FlowTotalProgress")
        self._FlowTotalStatus = params.get("FlowTotalStatus")
        if params.get("FlowExtraDetail") is not None:
            self._FlowExtraDetail = []
            for item in params.get("FlowExtraDetail"):
                obj = FlowExtraDetail()
                obj._deserialize(item)
                self._FlowExtraDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type InstanceId: str
        :param _NodeFlag: 节点标识，取值为：
<li>all：表示获取全部类型节点，cdb信息除外。</li>
<li>master：表示获取master节点信息。</li>
<li>core：表示获取core节点信息。</li>
<li>task：表示获取task节点信息。</li>
<li>common：表示获取common节点信息。</li>
<li>router：表示获取router节点信息。</li>
<li>db：表示获取正常状态的cdb信息。</li>
<li>recyle：表示获取回收站隔离中的节点信息，包括cdb信息。</li>
<li>renew：表示获取所有待续费的节点信息，包括cdb信息，自动续费节点不会返回。</li>
注意：现在只支持以上取值，输入其他值会导致错误。
        :type NodeFlag: str
        :param _ExportDb: 导出全部节点信息csv时是否携带cdb信息
        :type ExportDb: bool
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为100，最大值为100。
如果offset和limit都不填，或者都填0，则返回全部数据
        :type Limit: int
        :param _HardwareResourceType: 资源类型:支持all/host/pod，默认为all
        :type HardwareResourceType: str
        :param _SearchFields: 支持搜索的字段
        :type SearchFields: list of SearchItem
        :param _OrderField: 无
        :type OrderField: str
        :param _Asc: 无
        :type Asc: int
        """
        self._InstanceId = None
        self._NodeFlag = None
        self._ExportDb = None
        self._Offset = None
        self._Limit = None
        self._HardwareResourceType = None
        self._SearchFields = None
        self._OrderField = None
        self._Asc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def ExportDb(self):
        return self._ExportDb

    @ExportDb.setter
    def ExportDb(self, ExportDb):
        self._ExportDb = ExportDb

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
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def SearchFields(self):
        return self._SearchFields

    @SearchFields.setter
    def SearchFields(self, SearchFields):
        self._SearchFields = SearchFields

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeFlag = params.get("NodeFlag")
        self._ExportDb = params.get("ExportDb")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("SearchFields") is not None:
            self._SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self._SearchFields.append(obj)
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 查询到的节点总数
        :type TotalCnt: int
        :param _NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeHardwareInfo
        :param _TagKeys: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param _HardwareResourceTypeList: 资源类型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareResourceTypeList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._NodeList = None
        self._TagKeys = None
        self._HardwareResourceTypeList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def HardwareResourceTypeList(self):
        return self._HardwareResourceTypeList

    @HardwareResourceTypeList.setter
    def HardwareResourceTypeList(self, HardwareResourceTypeList):
        self._HardwareResourceTypeList = HardwareResourceTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._HardwareResourceTypeList = params.get("HardwareResourceTypeList")
        self._RequestId = params.get("RequestId")


class DescribeCvmQuotaRequest(AbstractModel):
    """DescribeCvmQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: EMR集群ID
        :type ClusterId: str
        :param _ZoneId: 区ID
        :type ZoneId: int
        """
        self._ClusterId = None
        self._ZoneId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCvmQuotaResponse(AbstractModel):
    """DescribeCvmQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PostPaidQuotaSet: 后付费配额列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPaidQuotaSet: list of QuotaEntity
        :param _SpotPaidQuotaSet: 竞价实例配额列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotPaidQuotaSet: list of QuotaEntity
        :param _EksQuotaSet: eks配额
注意：此字段可能返回 null，表示取不到有效值。
        :type EksQuotaSet: list of PodSaleSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PostPaidQuotaSet = None
        self._SpotPaidQuotaSet = None
        self._EksQuotaSet = None
        self._RequestId = None

    @property
    def PostPaidQuotaSet(self):
        return self._PostPaidQuotaSet

    @PostPaidQuotaSet.setter
    def PostPaidQuotaSet(self, PostPaidQuotaSet):
        self._PostPaidQuotaSet = PostPaidQuotaSet

    @property
    def SpotPaidQuotaSet(self):
        return self._SpotPaidQuotaSet

    @SpotPaidQuotaSet.setter
    def SpotPaidQuotaSet(self, SpotPaidQuotaSet):
        self._SpotPaidQuotaSet = SpotPaidQuotaSet

    @property
    def EksQuotaSet(self):
        return self._EksQuotaSet

    @EksQuotaSet.setter
    def EksQuotaSet(self, EksQuotaSet):
        self._EksQuotaSet = EksQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PostPaidQuotaSet") is not None:
            self._PostPaidQuotaSet = []
            for item in params.get("PostPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self._PostPaidQuotaSet.append(obj)
        if params.get("SpotPaidQuotaSet") is not None:
            self._SpotPaidQuotaSet = []
            for item in params.get("SpotPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self._SpotPaidQuotaSet.append(obj)
        if params.get("EksQuotaSet") is not None:
            self._EksQuotaSet = []
            for item in params.get("EksQuotaSet"):
                obj = PodSaleSpec()
                obj._deserialize(item)
                self._EksQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEmrApplicationStaticsRequest(AbstractModel):
    """DescribeEmrApplicationStatics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _StartTime: 起始时间，时间戳（秒）
        :type StartTime: int
        :param _EndTime: 结束时间，时间戳（秒）
        :type EndTime: int
        :param _Queues: 过滤的队列名
        :type Queues: list of str
        :param _Users: 过滤的用户名
        :type Users: list of str
        :param _ApplicationTypes: 过滤的作业类型
        :type ApplicationTypes: list of str
        :param _GroupBy: 分组字段，可选：queue, user, applicationType
        :type GroupBy: list of str
        :param _OrderBy: 排序字段，可选：sumMemorySeconds, sumVCoreSeconds, sumHDFSBytesWritten, sumHDFSBytesRead
        :type OrderBy: str
        :param _IsAsc: 是否顺序排序，0-逆序，1-正序
        :type IsAsc: int
        :param _Offset: 页号
        :type Offset: int
        :param _Limit: 页容量，范围为[10,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._GroupBy = None
        self._OrderBy = None
        self._IsAsc = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Queues(self):
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IsAsc(self):
        return self._IsAsc

    @IsAsc.setter
    def IsAsc(self, IsAsc):
        self._IsAsc = IsAsc

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
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._IsAsc = params.get("IsAsc")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmrApplicationStaticsResponse(AbstractModel):
    """DescribeEmrApplicationStatics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Statics: 作业统计信息
        :type Statics: list of ApplicationStatics
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Queues: 可选择的队列名
        :type Queues: list of str
        :param _Users: 可选择的用户名
        :type Users: list of str
        :param _ApplicationTypes: 可选择的作业类型
        :type ApplicationTypes: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Statics = None
        self._TotalCount = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._RequestId = None

    @property
    def Statics(self):
        return self._Statics

    @Statics.setter
    def Statics(self, Statics):
        self._Statics = Statics

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Queues(self):
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Statics") is not None:
            self._Statics = []
            for item in params.get("Statics"):
                obj = ApplicationStatics()
                obj._deserialize(item)
                self._Statics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._RequestId = params.get("RequestId")


class DescribeEmrOverviewMetricsRequest(AbstractModel):
    """DescribeEmrOverviewMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _End: 结束时间
        :type End: int
        :param _Metric: 指标名
        :type Metric: str
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _Downsample: 粒度 30s-max 1m-max 1h-max等
        :type Downsample: str
        :param _Start: 起始时间，画饼状图时不传
        :type Start: int
        :param _Aggregator: 聚合方法，扩展用，这里目前不用传
        :type Aggregator: str
        :param _Tags: 指标要查询的具体type 如："{"type":"CapacityTotal|CapacityRemaining"}"
        :type Tags: str
        """
        self._End = None
        self._Metric = None
        self._InstanceId = None
        self._Downsample = None
        self._Start = None
        self._Aggregator = None
        self._Tags = None

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Downsample(self):
        return self._Downsample

    @Downsample.setter
    def Downsample(self, Downsample):
        self._Downsample = Downsample

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def Aggregator(self):
        return self._Aggregator

    @Aggregator.setter
    def Aggregator(self, Aggregator):
        self._Aggregator = Aggregator

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._End = params.get("End")
        self._Metric = params.get("Metric")
        self._InstanceId = params.get("InstanceId")
        self._Downsample = params.get("Downsample")
        self._Start = params.get("Start")
        self._Aggregator = params.get("Aggregator")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmrOverviewMetricsResponse(AbstractModel):
    """DescribeEmrOverviewMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 指标数据明细
        :type Result: list of OverviewMetricData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = OverviewMetricData()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGlobalConfigRequest(AbstractModel):
    """DescribeGlobalConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalConfigResponse(AbstractModel):
    """DescribeGlobalConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableResourceSchedule: 是否开启了资源调度功能
        :type EnableResourceSchedule: bool
        :param _ActiveScheduler: 当前生效的资源调度器
        :type ActiveScheduler: str
        :param _CapacityGlobalConfig: 公平调度器的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityGlobalConfig: :class:`tencentcloud.emr.v20190103.models.CapacityGlobalConfig`
        :param _FairGlobalConfig: 容量调度器的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FairGlobalConfig: :class:`tencentcloud.emr.v20190103.models.FairGlobalConfig`
        :param _Scheduler: 最新的资源调度器
        :type Scheduler: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnableResourceSchedule = None
        self._ActiveScheduler = None
        self._CapacityGlobalConfig = None
        self._FairGlobalConfig = None
        self._Scheduler = None
        self._RequestId = None

    @property
    def EnableResourceSchedule(self):
        return self._EnableResourceSchedule

    @EnableResourceSchedule.setter
    def EnableResourceSchedule(self, EnableResourceSchedule):
        self._EnableResourceSchedule = EnableResourceSchedule

    @property
    def ActiveScheduler(self):
        return self._ActiveScheduler

    @ActiveScheduler.setter
    def ActiveScheduler(self, ActiveScheduler):
        self._ActiveScheduler = ActiveScheduler

    @property
    def CapacityGlobalConfig(self):
        return self._CapacityGlobalConfig

    @CapacityGlobalConfig.setter
    def CapacityGlobalConfig(self, CapacityGlobalConfig):
        self._CapacityGlobalConfig = CapacityGlobalConfig

    @property
    def FairGlobalConfig(self):
        return self._FairGlobalConfig

    @FairGlobalConfig.setter
    def FairGlobalConfig(self, FairGlobalConfig):
        self._FairGlobalConfig = FairGlobalConfig

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnableResourceSchedule = params.get("EnableResourceSchedule")
        self._ActiveScheduler = params.get("ActiveScheduler")
        if params.get("CapacityGlobalConfig") is not None:
            self._CapacityGlobalConfig = CapacityGlobalConfig()
            self._CapacityGlobalConfig._deserialize(params.get("CapacityGlobalConfig"))
        if params.get("FairGlobalConfig") is not None:
            self._FairGlobalConfig = FairGlobalConfig()
            self._FairGlobalConfig._deserialize(params.get("FairGlobalConfig"))
        self._Scheduler = params.get("Scheduler")
        self._RequestId = params.get("RequestId")


class DescribeHBaseTableOverviewRequest(AbstractModel):
    """DescribeHBaseTableOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 分页查询编号偏移量，从0开始	
        :type Offset: int
        :param _Limit: 分页查询时的分页大小，最小1，最大100
        :type Limit: int
        :param _Table: 表名称，模糊匹配
        :type Table: str
        :param _OrderField: 排序的字段，有默认值
        :type OrderField: str
        :param _OrderType: 默认为降序，asc代表升序，desc代表降序
        :type OrderType: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Table = None
        self._OrderField = None
        self._OrderType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Table = params.get("Table")
        self._OrderField = params.get("OrderField")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHBaseTableOverviewResponse(AbstractModel):
    """DescribeHBaseTableOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableMonitorList: 概览数据数组
        :type TableMonitorList: list of OverviewRow
        :param _TotalCount: 概览数据数组长度
        :type TotalCount: int
        :param _SchemaList: 表schema信息
        :type SchemaList: list of TableSchemaItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableMonitorList = None
        self._TotalCount = None
        self._SchemaList = None
        self._RequestId = None

    @property
    def TableMonitorList(self):
        return self._TableMonitorList

    @TableMonitorList.setter
    def TableMonitorList(self, TableMonitorList):
        self._TableMonitorList = TableMonitorList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SchemaList(self):
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TableMonitorList") is not None:
            self._TableMonitorList = []
            for item in params.get("TableMonitorList"):
                obj = OverviewRow()
                obj._deserialize(item)
                self._TableMonitorList.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = TableSchemaItem()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHDFSStorageInfoRequest(AbstractModel):
    """DescribeHDFSStorageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _StartTime: 获取查询信息开始时间 (s)
        :type StartTime: int
        :param _EndTime: 获取查询信息结束时间 (s)
        :type EndTime: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHDFSStorageInfoResponse(AbstractModel):
    """DescribeHDFSStorageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SampleTime: 采样时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleTime: int
        :param _StorageSummaryDistribution: hdfs存储详情
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSummaryDistribution: list of StorageSummaryDistribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SampleTime = None
        self._StorageSummaryDistribution = None
        self._RequestId = None

    @property
    def SampleTime(self):
        return self._SampleTime

    @SampleTime.setter
    def SampleTime(self, SampleTime):
        self._SampleTime = SampleTime

    @property
    def StorageSummaryDistribution(self):
        return self._StorageSummaryDistribution

    @StorageSummaryDistribution.setter
    def StorageSummaryDistribution(self, StorageSummaryDistribution):
        self._StorageSummaryDistribution = StorageSummaryDistribution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SampleTime = params.get("SampleTime")
        if params.get("StorageSummaryDistribution") is not None:
            self._StorageSummaryDistribution = []
            for item in params.get("StorageSummaryDistribution"):
                obj = StorageSummaryDistribution()
                obj._deserialize(item)
                self._StorageSummaryDistribution.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHiveQueriesRequest(AbstractModel):
    """DescribeHiveQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        :param _State: 执行状态,ERROR等
        :type State: list of str
        :param _EndTimeGte: 结束时间大于的时间点
        :type EndTimeGte: int
        :param _EndTimeLte: 结束时间小于时间点
        :type EndTimeLte: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._State = None
        self._EndTimeGte = None
        self._EndTimeLte = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def EndTimeGte(self):
        return self._EndTimeGte

    @EndTimeGte.setter
    def EndTimeGte(self, EndTimeGte):
        self._EndTimeGte = EndTimeGte

    @property
    def EndTimeLte(self):
        return self._EndTimeLte

    @EndTimeLte.setter
    def EndTimeLte(self, EndTimeLte):
        self._EndTimeLte = EndTimeLte


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._State = params.get("State")
        self._EndTimeGte = params.get("EndTimeGte")
        self._EndTimeLte = params.get("EndTimeLte")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHiveQueriesResponse(AbstractModel):
    """DescribeHiveQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of HiveQuery
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = HiveQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImpalaQueriesRequest(AbstractModel):
    """DescribeImpalaQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        :param _State: 执行状态，CREATED、INITIALIZED、COMPILED、RUNNING、FINISHED、EXCEPTION
        :type State: list of str
        :param _EndTimeGte: 结束时间大于的时间点
        :type EndTimeGte: int
        :param _EndTimeLte: 结束时间小于的时间点
        :type EndTimeLte: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._State = None
        self._EndTimeGte = None
        self._EndTimeLte = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def EndTimeGte(self):
        return self._EndTimeGte

    @EndTimeGte.setter
    def EndTimeGte(self, EndTimeGte):
        self._EndTimeGte = EndTimeGte

    @property
    def EndTimeLte(self):
        return self._EndTimeLte

    @EndTimeLte.setter
    def EndTimeLte(self, EndTimeLte):
        self._EndTimeLte = EndTimeLte


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._State = params.get("State")
        self._EndTimeGte = params.get("EndTimeGte")
        self._EndTimeLte = params.get("EndTimeLte")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImpalaQueriesResponse(AbstractModel):
    """DescribeImpalaQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of ImpalaQuery
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ImpalaQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInsightListRequest(AbstractModel):
    """DescribeInsightList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 获取的洞察结果开始时间，此时间针对对App或者Hive查询的开始时间的过滤
        :type StartTime: int
        :param _EndTime: 获取的洞察结果结束时间，此时间针对对App或者Hive查询的开始时间的过滤
        :type EndTime: int
        :param _PageSize: 分页查询时的分页大小，最小1，最大100
        :type PageSize: int
        :param _Page: 分页查询时的页号，从1开始
        :type Page: int
        :param _Type: 查询类型,支持HIVE,SPARK,DLC_SPARK,SPARK_SQL,SCHEDULE,MAPREDUCE,TRINO等类型,默认查询全部
        :type Type: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._Page = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInsightListResponse(AbstractModel):
    """DescribeInsightList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，分页查询时使用
        :type TotalCount: int
        :param _ResultList: 洞察结果数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultList: list of InsightResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResultList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResultList(self):
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = InsightResult()
                obj._deserialize(item)
                self._ResultList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRenewNodesRequest(AbstractModel):
    """DescribeInstanceRenewNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceRenewNodesResponse(AbstractModel):
    """DescribeInstanceRenewNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 查询到的节点总数
        :type TotalCnt: int
        :param _NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of RenewInstancesInfo
        :param _MetaInfo: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaInfo: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._NodeList = None
        self._MetaInfo = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def MetaInfo(self):
        return self._MetaInfo

    @MetaInfo.setter
    def MetaInfo(self, MetaInfo):
        self._MetaInfo = MetaInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = RenewInstancesInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._MetaInfo = params.get("MetaInfo")
        self._RequestId = params.get("RequestId")


class DescribeInstancesListRequest(AbstractModel):
    """DescribeInstancesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: 集群筛选策略。取值范围：<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li><li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li><li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>
        :type DisplayStrategy: str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为100，最大值为100。
如果limit和offset都为0，则查询全部记录；
        :type Limit: int
        :param _OrderField: 排序字段。取值范围：<li>clusterId：表示按照实例ID排序。</li><li>addTime：表示按照实例创建时间排序。</li><li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param _Asc: 按照OrderField升序或者降序进行排序。取值范围：<li>0：表示升序。</li><li>1：表示降序。</li>默认值为0。
        :type Asc: int
        :param _Filters: 自定义查询过滤器。示例：<li>根据ClusterId过滤实例：[{"Name":"ClusterId","Values":["emr-xxxxxxxx"]}]</li><li>根据clusterName过滤实例：[{"Name": "ClusterName","Values": ["cluster_name"]}]</li><li>根据ClusterStatus过滤实例：[{"Name": "ClusterStatus","Values": ["2"]}]</li>
        :type Filters: list of Filters
        """
        self._DisplayStrategy = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Asc = None
        self._Filters = None

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesListResponse(AbstractModel):
    """DescribeInstancesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 符合条件的实例总数。
        :type TotalCnt: int
        :param _InstancesList: 集群实例列表
        :type InstancesList: list of EmrListInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def InstancesList(self):
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = EmrListInstance()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: 集群筛选策略。取值范围：
<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li>
<li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li>
<li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>
        :type DisplayStrategy: str
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如: emr-xxxxxxxx 。(此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的 Ids.N 一节)。如果不填写实例ID，返回该APPID下所有实例列表。
        :type InstanceIds: list of str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为100，最大值为100。
        :type Limit: int
        :param _ProjectId: 建议必填-1，表示拉取所有项目下的集群。
不填默认值为0，表示拉取默认项目下的集群。
实例所属项目ID。该参数可以通过调用 [DescribeProjects](https://cloud.tencent.com/document/product/651/78725) 的返回值中的 projectId 字段来获取。
        :type ProjectId: int
        :param _OrderField: 排序字段。取值范围：
<li>clusterId：表示按照实例ID排序。</li>
<li>addTime：表示按照实例创建时间排序。</li>
<li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param _Asc: 按照OrderField升序或者降序进行排序。取值范围：
<li>0：表示降序。</li>
<li>1：表示升序。</li>默认值为0。
        :type Asc: int
        """
        self._DisplayStrategy = None
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._OrderField = None
        self._Asc = None

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 符合条件的实例总数。
        :type TotalCnt: int
        :param _ClusterList: EMR实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstancesInfo
        :param _TagKeys: 实例关联的标签键列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._ClusterList = None
        self._TagKeys = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def ClusterList(self):
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._RequestId = params.get("RequestId")


class DescribeJobFlowRequest(AbstractModel):
    """DescribeJobFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobFlowId: 流程任务Id，RunJobFlow接口返回的值。
        :type JobFlowId: int
        """
        self._JobFlowId = None

    @property
    def JobFlowId(self):
        return self._JobFlowId

    @JobFlowId.setter
    def JobFlowId(self, JobFlowId):
        self._JobFlowId = JobFlowId


    def _deserialize(self, params):
        self._JobFlowId = params.get("JobFlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobFlowResponse(AbstractModel):
    """DescribeJobFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _State: 流程任务状态，可以为以下值：
JobFlowInit，流程任务初始化。
JobFlowResourceApplied，资源申请中，通常为JobFlow需要新建集群时的状态。
JobFlowResourceReady，执行流程任务的资源就绪。
JobFlowStepsRunning，流程任务步骤已提交。
JobFlowStepsComplete，流程任务步骤已完成。
JobFlowTerminating，流程任务所需资源销毁中。
JobFlowFinish，流程任务已完成。
        :type State: str
        :param _Details: 流程任务步骤结果。
        :type Details: list of JobResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._State = None
        self._Details = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = JobResult()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKyuubiQueryInfoRequest(AbstractModel):
    """DescribeKyuubiQueryInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 获取查询信息开始时间 (s)
        :type StartTime: int
        :param _EndTime: 获取查询信息结束时间 (s)
        :type EndTime: int
        :param _PageSize: 分页查询时的分页大小，最小1，最大100
        :type PageSize: int
        :param _Page: 分页查询时的页号，从1开始
        :type Page: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._Page = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKyuubiQueryInfoResponse(AbstractModel):
    """DescribeKyuubiQueryInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，分页查询时使用
        :type TotalCount: int
        :param _KyuubiQueryInfoList: Kyuubi查询信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KyuubiQueryInfoList: list of KyuubiQueryInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KyuubiQueryInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KyuubiQueryInfoList(self):
        return self._KyuubiQueryInfoList

    @KyuubiQueryInfoList.setter
    def KyuubiQueryInfoList(self, KyuubiQueryInfoList):
        self._KyuubiQueryInfoList = KyuubiQueryInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KyuubiQueryInfoList") is not None:
            self._KyuubiQueryInfoList = []
            for item in params.get("KyuubiQueryInfoList"):
                obj = KyuubiQueryInfo()
                obj._deserialize(item)
                self._KyuubiQueryInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceScheduleDiffDetailRequest(AbstractModel):
    """DescribeResourceScheduleDiffDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _Scheduler: 查询的变更明细对应的调度器，可选值为fair、capacity。如果不传或者传空会使用最新的调度器
        :type Scheduler: str
        """
        self._InstanceId = None
        self._Scheduler = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceScheduleDiffDetailResponse(AbstractModel):
    """DescribeResourceScheduleDiffDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: 变化项的明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of DiffDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DiffDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceScheduleRequest(AbstractModel):
    """DescribeResourceSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceScheduleResponse(AbstractModel):
    """DescribeResourceSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OpenSwitch: 资源调度功能是否开启
        :type OpenSwitch: bool
        :param _Scheduler: 正在使用的资源调度器
        :type Scheduler: str
        :param _FSInfo: 公平调度器的信息
        :type FSInfo: str
        :param _CSInfo: 容量调度器的信息
        :type CSInfo: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OpenSwitch = None
        self._Scheduler = None
        self._FSInfo = None
        self._CSInfo = None
        self._RequestId = None

    @property
    def OpenSwitch(self):
        return self._OpenSwitch

    @OpenSwitch.setter
    def OpenSwitch(self, OpenSwitch):
        self._OpenSwitch = OpenSwitch

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def FSInfo(self):
        return self._FSInfo

    @FSInfo.setter
    def FSInfo(self, FSInfo):
        self._FSInfo = FSInfo

    @property
    def CSInfo(self):
        return self._CSInfo

    @CSInfo.setter
    def CSInfo(self, CSInfo):
        self._CSInfo = CSInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OpenSwitch = params.get("OpenSwitch")
        self._Scheduler = params.get("Scheduler")
        self._FSInfo = params.get("FSInfo")
        self._CSInfo = params.get("CSInfo")
        self._RequestId = params.get("RequestId")


class DescribeSLInstanceListRequest(AbstractModel):
    """DescribeSLInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: 实例筛选策略。取值范围：<li>clusterList：表示查询除了已销毁实例之外的实例列表。</li><li>monitorManage：表示查询除了已销毁、创建中以及创建失败的实例之外的实例列表。</li>
        :type DisplayStrategy: str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为10，最大值为100。	
        :type Limit: int
        :param _OrderField: 排序字段。取值范围：<li>clusterId：表示按照实例ID排序。</li><li>addTime：表示按照实例创建时间排序。</li><li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param _Asc: 按照OrderField升序或者降序进行排序。取值范围：<li>0：表示升序。</li><li>1：表示降序。</li>默认值为0。
        :type Asc: int
        :param _Filters: 自定义查询过滤器。示例：<li>根据ClusterId过滤实例：[{"Name":"ClusterId","Values":["emr-xxxxxxxx"]}]</li><li>根据clusterName过滤实例：[{"Name": "ClusterName","Values": ["cluster_name"]}]</li><li>根据ClusterStatus过滤实例：[{"Name": "ClusterStatus","Values": ["2"]}]</li>
        :type Filters: list of Filters
        """
        self._DisplayStrategy = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Asc = None
        self._Filters = None

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSLInstanceListResponse(AbstractModel):
    """DescribeSLInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 符合条件的实例总数。	
        :type TotalCnt: int
        :param _InstancesList: 实例信息列表，如果进行了分页，只显示当前分页的示例信息列表。
        :type InstancesList: list of SLInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def InstancesList(self):
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = SLInstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSLInstanceRequest(AbstractModel):
    """DescribeSLInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一标识符（字符串表示）
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSLInstanceResponse(AbstractModel):
    """DescribeSLInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _PayMode: 实例计费模式。0表示后付费，即按量计费，1表示预付费，即包年包月。
        :type PayMode: int
        :param _DiskType: 实例存储类型。
        :type DiskType: str
        :param _DiskSize: 实例单节点磁盘容量，单位GB。
        :type DiskSize: int
        :param _NodeType: 实例节点规格。
        :type NodeType: str
        :param _ZoneSettings: 实例可用区详细配置，包含可用区名称，VPC信息、节点数量。
        :type ZoneSettings: list of ZoneSetting
        :param _Tags: 实例绑定的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceName = None
        self._PayMode = None
        self._DiskType = None
        self._DiskSize = None
        self._NodeType = None
        self._ZoneSettings = None
        self._Tags = None
        self._RequestId = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ZoneSettings(self):
        return self._ZoneSettings

    @ZoneSettings.setter
    def ZoneSettings(self, ZoneSettings):
        self._ZoneSettings = ZoneSettings

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
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._NodeType = params.get("NodeType")
        if params.get("ZoneSettings") is not None:
            self._ZoneSettings = []
            for item in params.get("ZoneSettings"):
                obj = ZoneSetting()
                obj._deserialize(item)
                self._ZoneSettings.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceNodeInfosRequest(AbstractModel):
    """DescribeServiceNodeInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 页大小
        :type Limit: int
        :param _SearchText: 搜索字段
        :type SearchText: str
        :param _ConfStatus: '配置状态，-2：配置失败，-1:配置过期，1：已同步', -99 '全部'
        :type ConfStatus: int
        :param _MaintainStateId: 过滤条件：维护状态
0代表所有状态
1代表正常模式
2代表维护模式

        :type MaintainStateId: int
        :param _OperatorStateId: 过滤条件：操作状态
0代表所有状态
1代表已启动
2代表已停止
        :type OperatorStateId: int
        :param _HealthStateId: 过滤条件：健康状态
"0"代表不可用
"1"代表良好
"-2"代表未知
"-99"代表所有
"-3"代表存在隐患
"-4"代表未探测
        :type HealthStateId: str
        :param _ServiceName: 服务组件名称，都是大写例如YARN
        :type ServiceName: str
        :param _NodeTypeName: 节点名称
master
core
task
common
router

        :type NodeTypeName: str
        :param _DataNodeMaintenanceId: 过滤条件：dn是否处于维护状态
0代表所有状态
1代表处于维护状态
        :type DataNodeMaintenanceId: int
        :param _SearchFields: 支持搜索的字段
        :type SearchFields: list of SearchItem
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._SearchText = None
        self._ConfStatus = None
        self._MaintainStateId = None
        self._OperatorStateId = None
        self._HealthStateId = None
        self._ServiceName = None
        self._NodeTypeName = None
        self._DataNodeMaintenanceId = None
        self._SearchFields = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def SearchText(self):
        return self._SearchText

    @SearchText.setter
    def SearchText(self, SearchText):
        self._SearchText = SearchText

    @property
    def ConfStatus(self):
        return self._ConfStatus

    @ConfStatus.setter
    def ConfStatus(self, ConfStatus):
        self._ConfStatus = ConfStatus

    @property
    def MaintainStateId(self):
        return self._MaintainStateId

    @MaintainStateId.setter
    def MaintainStateId(self, MaintainStateId):
        self._MaintainStateId = MaintainStateId

    @property
    def OperatorStateId(self):
        return self._OperatorStateId

    @OperatorStateId.setter
    def OperatorStateId(self, OperatorStateId):
        self._OperatorStateId = OperatorStateId

    @property
    def HealthStateId(self):
        return self._HealthStateId

    @HealthStateId.setter
    def HealthStateId(self, HealthStateId):
        self._HealthStateId = HealthStateId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def NodeTypeName(self):
        return self._NodeTypeName

    @NodeTypeName.setter
    def NodeTypeName(self, NodeTypeName):
        self._NodeTypeName = NodeTypeName

    @property
    def DataNodeMaintenanceId(self):
        return self._DataNodeMaintenanceId

    @DataNodeMaintenanceId.setter
    def DataNodeMaintenanceId(self, DataNodeMaintenanceId):
        self._DataNodeMaintenanceId = DataNodeMaintenanceId

    @property
    def SearchFields(self):
        return self._SearchFields

    @SearchFields.setter
    def SearchFields(self, SearchFields):
        self._SearchFields = SearchFields


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchText = params.get("SearchText")
        self._ConfStatus = params.get("ConfStatus")
        self._MaintainStateId = params.get("MaintainStateId")
        self._OperatorStateId = params.get("OperatorStateId")
        self._HealthStateId = params.get("HealthStateId")
        self._ServiceName = params.get("ServiceName")
        self._NodeTypeName = params.get("NodeTypeName")
        self._DataNodeMaintenanceId = params.get("DataNodeMaintenanceId")
        if params.get("SearchFields") is not None:
            self._SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self._SearchFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceNodeInfosResponse(AbstractModel):
    """DescribeServiceNodeInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCnt: int
        :param _ServiceNodeList: 进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceNodeList: list of ServiceNodeDetailInfo
        :param _AliasInfo: 集群所有节点的别名序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasInfo: str
        :param _SupportNodeFlagFilterList: 支持的FlagNode列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportNodeFlagFilterList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._ServiceNodeList = None
        self._AliasInfo = None
        self._SupportNodeFlagFilterList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def ServiceNodeList(self):
        return self._ServiceNodeList

    @ServiceNodeList.setter
    def ServiceNodeList(self, ServiceNodeList):
        self._ServiceNodeList = ServiceNodeList

    @property
    def AliasInfo(self):
        return self._AliasInfo

    @AliasInfo.setter
    def AliasInfo(self, AliasInfo):
        self._AliasInfo = AliasInfo

    @property
    def SupportNodeFlagFilterList(self):
        return self._SupportNodeFlagFilterList

    @SupportNodeFlagFilterList.setter
    def SupportNodeFlagFilterList(self, SupportNodeFlagFilterList):
        self._SupportNodeFlagFilterList = SupportNodeFlagFilterList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("ServiceNodeList") is not None:
            self._ServiceNodeList = []
            for item in params.get("ServiceNodeList"):
                obj = ServiceNodeDetailInfo()
                obj._deserialize(item)
                self._ServiceNodeList.append(obj)
        self._AliasInfo = params.get("AliasInfo")
        self._SupportNodeFlagFilterList = params.get("SupportNodeFlagFilterList")
        self._RequestId = params.get("RequestId")


class DescribeSparkQueriesRequest(AbstractModel):
    """DescribeSparkQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        :param _Status: 执行状态:RUNNING,COMPLETED,FAILED
        :type Status: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkQueriesResponse(AbstractModel):
    """DescribeSparkQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Results: 结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of SparkQuery
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SparkQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStarRocksQueryInfoRequest(AbstractModel):
    """DescribeStarRocksQueryInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 获取查询信息开始时间 (s)
        :type StartTime: int
        :param _EndTime: 获取查询信息结束时间 (s)
        :type EndTime: int
        :param _PageSize: 分页查询时的分页大小，最小1，最大100
        :type PageSize: int
        :param _Page: 分页查询时的页号，从1开始
        :type Page: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._Page = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStarRocksQueryInfoResponse(AbstractModel):
    """DescribeStarRocksQueryInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，分页查询时使用
        :type TotalCount: int
        :param _StarRocksQueryInfoList: Starrocks 查询信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StarRocksQueryInfoList: list of StarRocksQueryInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._StarRocksQueryInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StarRocksQueryInfoList(self):
        return self._StarRocksQueryInfoList

    @StarRocksQueryInfoList.setter
    def StarRocksQueryInfoList(self, StarRocksQueryInfoList):
        self._StarRocksQueryInfoList = StarRocksQueryInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StarRocksQueryInfoList") is not None:
            self._StarRocksQueryInfoList = []
            for item in params.get("StarRocksQueryInfoList"):
                obj = StarRocksQueryInfo()
                obj._deserialize(item)
                self._StarRocksQueryInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrinoQueryInfoRequest(AbstractModel):
    """DescribeTrinoQueryInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 获取查询信息开始时间 (s)
        :type StartTime: int
        :param _EndTime: 获取查询信息结束时间 (s)
        :type EndTime: int
        :param _PageSize: 分页查询时的分页大小，最小1，最大100
        :type PageSize: int
        :param _Page: 分页查询时的页号，从1开始
        :type Page: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._Page = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrinoQueryInfoResponse(AbstractModel):
    """DescribeTrinoQueryInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，分页查询时使用
        :type TotalCount: int
        :param _QueryInfoList: 查询结果数组
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryInfoList: list of TrinoQueryInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueryInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueryInfoList(self):
        return self._QueryInfoList

    @QueryInfoList.setter
    def QueryInfoList(self, QueryInfoList):
        self._QueryInfoList = QueryInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueryInfoList") is not None:
            self._QueryInfoList = []
            for item in params.get("QueryInfoList"):
                obj = TrinoQueryInfo()
                obj._deserialize(item)
                self._QueryInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsersForUserManagerRequest(AbstractModel):
    """DescribeUsersForUserManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 分页的大小。
默认查询全部；PageNo和PageSize不合理的设置，都是查询全部
        :type PageSize: int
        :param _UserManagerFilter: 查询用户列表过滤器
        :type UserManagerFilter: :class:`tencentcloud.emr.v20190103.models.UserManagerFilter`
        :param _NeedKeytabInfo: 是否需要keytab文件的信息，仅对开启kerberos的集群有效，默认为false
        :type NeedKeytabInfo: bool
        """
        self._InstanceId = None
        self._PageNo = None
        self._PageSize = None
        self._UserManagerFilter = None
        self._NeedKeytabInfo = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserManagerFilter(self):
        return self._UserManagerFilter

    @UserManagerFilter.setter
    def UserManagerFilter(self, UserManagerFilter):
        self._UserManagerFilter = UserManagerFilter

    @property
    def NeedKeytabInfo(self):
        return self._NeedKeytabInfo

    @NeedKeytabInfo.setter
    def NeedKeytabInfo(self, NeedKeytabInfo):
        self._NeedKeytabInfo = NeedKeytabInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        if params.get("UserManagerFilter") is not None:
            self._UserManagerFilter = UserManagerFilter()
            self._UserManagerFilter._deserialize(params.get("UserManagerFilter"))
        self._NeedKeytabInfo = params.get("NeedKeytabInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersForUserManagerResponse(AbstractModel):
    """DescribeUsersForUserManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 总数
        :type TotalCnt: int
        :param _UserManagerUserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserManagerUserList: list of UserManagerUserBriefInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._UserManagerUserList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def UserManagerUserList(self):
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserManagerUserBriefInfo()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeYarnApplicationsRequest(AbstractModel):
    """DescribeYarnApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页偏移量，Offset=0表示第一页；如果limit=100，Offset=1，则表示第二页，数据第101条开始查询，返回100条数据；如果limit=100，Offset=2，则表示第三页，数据第201条开始查询，返回100条数据。依次类推
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeYarnApplicationsResponse(AbstractModel):
    """DescribeYarnApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of YarnApplication
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = YarnApplication()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeYarnQueueRequest(AbstractModel):
    """DescribeYarnQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群Id
        :type InstanceId: str
        :param _Scheduler: 调度器，可选值：

1. capacity
2. fair
        :type Scheduler: str
        """
        self._InstanceId = None
        self._Scheduler = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeYarnQueueResponse(AbstractModel):
    """DescribeYarnQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Queue: 队列信息。是一个对象转成的json字符串，对应的golang结构体如下所示，例如`QueueWithConfigSetForFairScheduler`的第一个字段`Name`：```Name                         string                               `json:"name"` //队列名称```- `Name`：字段名- `string`：字段类型- `json:"name"`：表示在序列化和反序列化`json`时，对应的`json key`，下面以`json key`来指代- `//`：后面的注释内容对应页面上看到的名称字段类型以`*`开头的表示取值可能为json规范下的null，不同的语言需要使用能表达null的类型来接收，例如java的包装类型；字段类型以`[]`开头的表示是数组类型；`json key`在调用`ModifyYarnQueueV2 `接口也会使用。- 公平调度器```type QueueWithConfigSetForFairScheduler struct {	Name                         string                               `json:"name"` //队列名称	MyId                         string                  `json:"myId"` // 队列id，用于编辑、删除、克隆时使用	ParentId                     string                  `json:"parentId"`  // 父队列Id	Type                         *string                              `json:"type"` // 队列归属。parent或空，当确定某个队列是父队列，且没有子队列时，才可以设置，通常用来支持放置策略nestedUserQueue	AclSubmitApps                *AclForYarnQueue                     `json:"aclSubmitApps"` // 提交访问控制	AclAdministerApps            *AclForYarnQueue                     `json:"aclAdministerApps"` // 管理访问控制	MinSharePreemptionTimeout    *int                                 `json:"minSharePreemptionTimeout"` // 最小共享优先权超时时间	FairSharePreemptionTimeout   *int                                 `json:"fairSharePreemptionTimeout"` // 公平份额抢占超时时间	FairSharePreemptionThreshold *float32                             `json:"fairSharePreemptionThreshold"` // 公平份额抢占阈值。取值 （0，1]	AllowPreemptionFrom          *bool                                `json:"allowPreemptionFrom"`                                        // 抢占模式	SchedulingPolicy             *string                              `json:"schedulingPolicy"`  // 调度策略，取值有drf、fair、fifo	IsDefault                    *bool                                `json:"isDefault"` // 是否是root.default队列	IsRoot                       *bool                                `json:"isRoot"` // 是否是root队列	ConfigSets                   []ConfigSetForFairScheduler          `json:"configSets"` // 配置集设置	Children                     []QueueWithConfigSetForFairScheduler `json:"queues"` // 子队列信息。递归}type AclForYarnQueue struct {	User  *string `json:"user"` //用户名	Group *string `json:"group"`//组名}type ConfigSetForFairScheduler struct {	Name              string        `json:"name"` // 配置集名称	MinResources      *YarnResource `json:"minResources"` // 最小资源量	MaxResources      *YarnResource `json:"maxResources"` // 最大资源量	MaxChildResources *YarnResource `json:"maxChildResources"` // 能够分配给为未声明子队列的最大资源量	MaxRunningApps    *int          `json:"maxRunningApps"` // 最高可同时处于运行的App数量	Weight            *float32      `json:"weight"`                   // 权重	MaxAMShare        *float32      `json:"maxAMShare"` // App Master最大份额}type YarnResource struct {	Vcores *int `json:"vcores"`	Memory *int `json:"memory"`	Type *string `json:"type"` // 当值为`percent`时，表示使用的百分比，否则就是使用的绝对数值}```- 容量调度器```type QueueForCapacitySchedulerV3 struct {	Name                       string                `json:"name"` // 队列名称	MyId                       string                `json:"myId"` // 队列id，用于编辑、删除、克隆时使用	ParentId                   string                `json:"parentId"` // 父队列Id	Configs                    []ConfigForCapacityV3 `json:"configs"` //配置集设置	State                      *string         `json:"state"` // 资源池状态	DefaultNodeLabelExpression *string               `json:"default-node-label-expression"` // 默认标签表达式	AclSubmitApps              *AclForYarnQueue      `json:"acl_submit_applications"` // 提交访问控制	AclAdminQueue              *AclForYarnQueue      `json:"acl_administer_queue"` //管理访问控制	MaxAllocationMB *int32 `json:"maximum-allocation-mb"` // 分配Container最大内存数量	MaxAllocationVcores *int32                         `json:"maximum-allocation-vcores"` // Container最大vCore数量	IsDefault           *bool                          `json:"isDefault"`// 是否是root.default队列	IsRoot              *bool                          `json:"isRoot"` // 是否是root队列	Queues              []*QueueForCapacitySchedulerV3 `json:"queues"`//子队列信息。递归}type ConfigForCapacityV3 struct {	Name                string          `json:"configName"` // 配置集名称	Labels              []CapacityLabel `json:"labels"` // 标签信息	MinUserLimitPercent *int32          `json:"minimum-user-limit-percent"` // 用户最小容量	UserLimitFactor     *float32        `json:"user-limit-factor" valid:"rangeExcludeLeft(0|)"`  // 用户资源因子	MaxApps *int32 `json:"maximum-applications" valid:"rangeExcludeLeft(0|)"` // 最大应用数Max-Applications	MaxAmPercent               *float32 `json:"maximum-am-resource-percent"` // 最大AM比例	DefaultApplicationPriority *int32   `json:"default-application-priority"` // 资源池优先级}type CapacityLabel struct {	Name        string   `json:"labelName"`	Capacity    *float32 `json:"capacity"`  // 容量	MaxCapacity *float32 `json:"maximum-capacity"` //最大容量}type AclForYarnQueue struct {	User  *string `json:"user"` //用户名	Group *string `json:"group"`//组名}```
        :type Queue: str
        :param _Version: 版本
        :type Version: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Queue = None
        self._Version = None
        self._RequestId = None

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Queue = params.get("Queue")
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class DescribeYarnScheduleHistoryRequest(AbstractModel):
    """DescribeYarnScheduleHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Limit: 页码
        :type Limit: int
        :param _Offset: 页大小
        :type Offset: int
        :param _SchedulerType: 调度器类型 可选值为“ALL”，"Capacity Scheduler", "Fair Scheduler"
        :type SchedulerType: str
        :param _TaskState: 任务类型0:等待执行，1:执行中，2：完成，-1:失败 ，-99:全部
        :type TaskState: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._SchedulerType = None
        self._TaskState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SchedulerType(self):
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def TaskState(self):
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SchedulerType = params.get("SchedulerType")
        self._TaskState = params.get("TaskState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeYarnScheduleHistoryResponse(AbstractModel):
    """DescribeYarnScheduleHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of SchedulerTaskInfo
        :param _Total: 任务详情总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _SchedulerNameList: 调度类型筛选列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerNameList: list of str
        :param _StateList: 状态筛选列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StateList: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._Total = None
        self._SchedulerNameList = None
        self._StateList = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SchedulerNameList(self):
        return self._SchedulerNameList

    @SchedulerNameList.setter
    def SchedulerNameList(self, SchedulerNameList):
        self._SchedulerNameList = SchedulerNameList

    @property
    def StateList(self):
        return self._StateList

    @StateList.setter
    def StateList(self, StateList):
        self._StateList = StateList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = SchedulerTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Total = params.get("Total")
        self._SchedulerNameList = params.get("SchedulerNameList")
        self._StateList = params.get("StateList")
        self._RequestId = params.get("RequestId")


class DiffDetail(AbstractModel):
    """动态生成的变更详情

    """

    def __init__(self):
        r"""
        :param _Name: tab页的头
        :type Name: str
        :param _Count: 变化项的个数
        :type Count: int
        :param _Rows: 要渲染的明细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Rows: list of DiffDetailItem
        :param _Header: 要渲染的头部信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: list of DiffHeader
        """
        self._Name = None
        self._Count = None
        self._Rows = None
        self._Header = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Header(self):
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = DiffDetailItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        if params.get("Header") is not None:
            self._Header = []
            for item in params.get("Header"):
                obj = DiffHeader()
                obj._deserialize(item)
                self._Header.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiffDetailItem(AbstractModel):
    """动态生成的变更详情条目

    """

    def __init__(self):
        r"""
        :param _Attribute: 属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Attribute: str
        :param _InEffect: 当前生效
注意：此字段可能返回 null，表示取不到有效值。
        :type InEffect: str
        :param _PendingEffectiveness: 待生效
注意：此字段可能返回 null，表示取不到有效值。
        :type PendingEffectiveness: str
        :param _Operation: 操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _Queue: 队列
注意：此字段可能返回 null，表示取不到有效值。
        :type Queue: str
        :param _ConfigSet: 配置集
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigSet: str
        :param _LabelName: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        :param _InEffectIndex: 当前所在位置
注意：此字段可能返回 null，表示取不到有效值。
        :type InEffectIndex: str
        :param _PendingEffectIndex: 待生效的位置
注意：此字段可能返回 null，表示取不到有效值。
        :type PendingEffectIndex: str
        :param _PlanName: 计划模式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanName: str
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _RuleName: 放置规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._Attribute = None
        self._InEffect = None
        self._PendingEffectiveness = None
        self._Operation = None
        self._Queue = None
        self._ConfigSet = None
        self._LabelName = None
        self._InEffectIndex = None
        self._PendingEffectIndex = None
        self._PlanName = None
        self._Label = None
        self._RuleName = None
        self._UserName = None

    @property
    def Attribute(self):
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def InEffect(self):
        return self._InEffect

    @InEffect.setter
    def InEffect(self, InEffect):
        self._InEffect = InEffect

    @property
    def PendingEffectiveness(self):
        return self._PendingEffectiveness

    @PendingEffectiveness.setter
    def PendingEffectiveness(self, PendingEffectiveness):
        self._PendingEffectiveness = PendingEffectiveness

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def ConfigSet(self):
        return self._ConfigSet

    @ConfigSet.setter
    def ConfigSet(self, ConfigSet):
        self._ConfigSet = ConfigSet

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def InEffectIndex(self):
        return self._InEffectIndex

    @InEffectIndex.setter
    def InEffectIndex(self, InEffectIndex):
        self._InEffectIndex = InEffectIndex

    @property
    def PendingEffectIndex(self):
        return self._PendingEffectIndex

    @PendingEffectIndex.setter
    def PendingEffectIndex(self, PendingEffectIndex):
        self._PendingEffectIndex = PendingEffectIndex

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._Attribute = params.get("Attribute")
        self._InEffect = params.get("InEffect")
        self._PendingEffectiveness = params.get("PendingEffectiveness")
        self._Operation = params.get("Operation")
        self._Queue = params.get("Queue")
        self._ConfigSet = params.get("ConfigSet")
        self._LabelName = params.get("LabelName")
        self._InEffectIndex = params.get("InEffectIndex")
        self._PendingEffectIndex = params.get("PendingEffectIndex")
        self._PlanName = params.get("PlanName")
        self._Label = params.get("Label")
        self._RuleName = params.get("RuleName")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiffHeader(AbstractModel):
    """动态生成的变更详情

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Id: ID，前端会使用
        :type Id: str
        """
        self._Name = None
        self._Id = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskGroup(AbstractModel):
    """磁盘组。

    """

    def __init__(self):
        r"""
        :param _Spec: 磁盘规格。
        :type Spec: :class:`tencentcloud.emr.v20190103.models.DiskSpec`
        :param _Count: 同类型磁盘数量。
        :type Count: int
        """
        self._Spec = None
        self._Count = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        if params.get("Spec") is not None:
            self._Spec = DiskSpec()
            self._Spec._deserialize(params.get("Spec"))
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskSpec(AbstractModel):
    """磁盘描述。

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型。
LOCAL_BASIC  本地盘。
CLOUD_BASIC 云硬盘。
LOCAL_SSD 本地SSD。
CLOUD_SSD 云SSD。
CLOUD_PREMIUM 高效云盘。
CLOUD_HSSD 增强型云SSD。
        :type DiskType: str
        :param _DiskSize: 磁盘大小，单位GB。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskSpecInfo(AbstractModel):
    """节点磁盘信息

    """

    def __init__(self):
        r"""
        :param _Count: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _DiskType: 系统盘类型 取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
<li>LOCAL_BASIC：表示本地盘。</li>
<li>LOCAL_SSD：表示本地SSD。</li>

数据盘类型 取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
<li>LOCAL_BASIC：表示本地盘。</li>
<li>LOCAL_SSD：表示本地SSD。</li>
<li>CLOUD_HSSD：表示增强型SSD云硬盘。</li>
<li>CLOUD_THROUGHPUT：表示吞吐型云硬盘。</li>
<li>CLOUD_TSSD：表示极速型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 数据容量，单位为GB
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _ExtraPerformance: 额外性能
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraPerformance: int
        """
        self._Count = None
        self._DiskType = None
        self._DiskSize = None
        self._ExtraPerformance = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ExtraPerformance(self):
        return self._ExtraPerformance

    @ExtraPerformance.setter
    def ExtraPerformance(self, ExtraPerformance):
        self._ExtraPerformance = ExtraPerformance


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._ExtraPerformance = params.get("ExtraPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Dps(AbstractModel):
    """采样序列

    """

    def __init__(self):
        r"""
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Value: 采样值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicPodSpec(AbstractModel):
    """POD浮动规格

    """

    def __init__(self):
        r"""
        :param _RequestCpu: 需求最小cpu核数
        :type RequestCpu: float
        :param _LimitCpu: 需求最大cpu核数
        :type LimitCpu: float
        :param _RequestMemory: 需求最小memory，单位MB
        :type RequestMemory: float
        :param _LimitMemory: 需求最大memory，单位MB
        :type LimitMemory: float
        """
        self._RequestCpu = None
        self._LimitCpu = None
        self._RequestMemory = None
        self._LimitMemory = None

    @property
    def RequestCpu(self):
        return self._RequestCpu

    @RequestCpu.setter
    def RequestCpu(self, RequestCpu):
        self._RequestCpu = RequestCpu

    @property
    def LimitCpu(self):
        return self._LimitCpu

    @LimitCpu.setter
    def LimitCpu(self, LimitCpu):
        self._LimitCpu = LimitCpu

    @property
    def RequestMemory(self):
        return self._RequestMemory

    @RequestMemory.setter
    def RequestMemory(self, RequestMemory):
        self._RequestMemory = RequestMemory

    @property
    def LimitMemory(self):
        return self._LimitMemory

    @LimitMemory.setter
    def LimitMemory(self, LimitMemory):
        self._LimitMemory = LimitMemory


    def _deserialize(self, params):
        self._RequestCpu = params.get("RequestCpu")
        self._LimitCpu = params.get("LimitCpu")
        self._RequestMemory = params.get("RequestMemory")
        self._LimitMemory = params.get("LimitMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrListInstance(AbstractModel):
    """集群列表返回示例

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _StatusDesc: 常见状态描述：集群生产中,集群运行中,集群创建中,集群已关闭,集群已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _ClusterName: 集群名字
        :type ClusterName: str
        :param _ZoneId: 集群地域
        :type ZoneId: int
        :param _AppId: 用户APPID
        :type AppId: int
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _RunTime: 运行时间
        :type RunTime: str
        :param _MasterIp: 集群IP
        :type MasterIp: str
        :param _EmrVersion: 集群版本
        :type EmrVersion: str
        :param _ChargeType: 集群计费类型
        :type ChargeType: int
        :param _Id: emr ID
        :type Id: int
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _RegionId: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param _VpcId: 网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _Zone: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Status: 状态码, 取值为-2(集群已删除), -1(集群已关闭), 0(集群生产中), 2(集群运行中), 3(集群创建中)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Tags: 实例标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AlarmInfo: 告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: 是否是woodpecker集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param _VpcName: Vpc中文
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _SubnetName: 子网中文
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _UniqVpcId: 字符串VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 字符串子网
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _ClusterClass: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterClass: str
        :param _IsMultiZoneCluster: 是否为跨AZ集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiZoneCluster: bool
        :param _IsHandsCluster: 是否手戳集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHandsCluster: bool
        :param _OutSideSoftInfo: 体外客户端组件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSideSoftInfo: list of SoftDependInfo
        :param _IsSupportOutsideCluster: 当前集群的应用场景是否支持体外客户端
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportOutsideCluster: bool
        :param _IsDedicatedCluster: 是否专有集群场景集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDedicatedCluster: bool
        """
        self._ClusterId = None
        self._StatusDesc = None
        self._ClusterName = None
        self._ZoneId = None
        self._AppId = None
        self._AddTime = None
        self._RunTime = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._Id = None
        self._ProductId = None
        self._ProjectId = None
        self._RegionId = None
        self._SubnetId = None
        self._VpcId = None
        self._Zone = None
        self._Status = None
        self._Tags = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._VpcName = None
        self._SubnetName = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ClusterClass = None
        self._IsMultiZoneCluster = None
        self._IsHandsCluster = None
        self._OutSideSoftInfo = None
        self._IsSupportOutsideCluster = None
        self._IsDedicatedCluster = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def MasterIp(self):
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AlarmInfo(self):
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ClusterClass(self):
        return self._ClusterClass

    @ClusterClass.setter
    def ClusterClass(self, ClusterClass):
        self._ClusterClass = ClusterClass

    @property
    def IsMultiZoneCluster(self):
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsHandsCluster(self):
        return self._IsHandsCluster

    @IsHandsCluster.setter
    def IsHandsCluster(self, IsHandsCluster):
        self._IsHandsCluster = IsHandsCluster

    @property
    def OutSideSoftInfo(self):
        return self._OutSideSoftInfo

    @OutSideSoftInfo.setter
    def OutSideSoftInfo(self, OutSideSoftInfo):
        self._OutSideSoftInfo = OutSideSoftInfo

    @property
    def IsSupportOutsideCluster(self):
        return self._IsSupportOutsideCluster

    @IsSupportOutsideCluster.setter
    def IsSupportOutsideCluster(self, IsSupportOutsideCluster):
        self._IsSupportOutsideCluster = IsSupportOutsideCluster

    @property
    def IsDedicatedCluster(self):
        return self._IsDedicatedCluster

    @IsDedicatedCluster.setter
    def IsDedicatedCluster(self, IsDedicatedCluster):
        self._IsDedicatedCluster = IsDedicatedCluster


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._StatusDesc = params.get("StatusDesc")
        self._ClusterName = params.get("ClusterName")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ClusterClass = params.get("ClusterClass")
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsHandsCluster = params.get("IsHandsCluster")
        if params.get("OutSideSoftInfo") is not None:
            self._OutSideSoftInfo = []
            for item in params.get("OutSideSoftInfo"):
                obj = SoftDependInfo()
                obj._deserialize(item)
                self._OutSideSoftInfo.append(obj)
        self._IsSupportOutsideCluster = params.get("IsSupportOutsideCluster")
        self._IsDedicatedCluster = params.get("IsDedicatedCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrPrice(AbstractModel):
    """Emr询价描述

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param _DiscountCost: 折扣价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _PriceSpec: 询价配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _SupportSpotPaid: 是否支持竞价实例
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportSpotPaid: bool
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._SupportSpotPaid = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def SupportSpotPaid(self):
        return self._SupportSpotPaid

    @SupportSpotPaid.setter
    def SupportSpotPaid(self, SupportSpotPaid):
        self._SupportSpotPaid = SupportSpotPaid


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        self._SupportSpotPaid = params.get("SupportSpotPaid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigDetail(AbstractModel):
    """EMR产品配置

    """

    def __init__(self):
        r"""
        :param _SoftInfo: 软件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param _MasterNodeSize: Master节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param _CoreNodeSize: Core节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param _TaskNodeSize: Task节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param _ComNodeSize: Common节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param _MasterResource: Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.ResourceDetail`
        :param _CoreResource: Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.ResourceDetail`
        :param _TaskResource: Task节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.ResourceDetail`
        :param _ComResource: Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.ResourceDetail`
        :param _OnCos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。
        :type OnCos: bool
        :param _ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _RouterNodeSize: Router节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RouterNodeSize: int
        :param _SupportHA: 是否支持HA
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportHA: bool
        :param _SecurityOn: 是否支持安全模式
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityOn: bool
        :param _SecurityGroup: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: str
        :param _CbsEncrypt: 是否开启Cbs加密
注意：此字段可能返回 null，表示取不到有效值。
        :type CbsEncrypt: int
        :param _ApplicationRole: 自定义应用角色。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRole: str
        :param _SecurityGroups: 安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param _PublicKeyId: SSH密钥Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKeyId: str
        """
        self._SoftInfo = None
        self._MasterNodeSize = None
        self._CoreNodeSize = None
        self._TaskNodeSize = None
        self._ComNodeSize = None
        self._MasterResource = None
        self._CoreResource = None
        self._TaskResource = None
        self._ComResource = None
        self._OnCos = None
        self._ChargeType = None
        self._RouterNodeSize = None
        self._SupportHA = None
        self._SecurityOn = None
        self._SecurityGroup = None
        self._CbsEncrypt = None
        self._ApplicationRole = None
        self._SecurityGroups = None
        self._PublicKeyId = None

    @property
    def SoftInfo(self):
        return self._SoftInfo

    @SoftInfo.setter
    def SoftInfo(self, SoftInfo):
        self._SoftInfo = SoftInfo

    @property
    def MasterNodeSize(self):
        return self._MasterNodeSize

    @MasterNodeSize.setter
    def MasterNodeSize(self, MasterNodeSize):
        self._MasterNodeSize = MasterNodeSize

    @property
    def CoreNodeSize(self):
        return self._CoreNodeSize

    @CoreNodeSize.setter
    def CoreNodeSize(self, CoreNodeSize):
        self._CoreNodeSize = CoreNodeSize

    @property
    def TaskNodeSize(self):
        return self._TaskNodeSize

    @TaskNodeSize.setter
    def TaskNodeSize(self, TaskNodeSize):
        self._TaskNodeSize = TaskNodeSize

    @property
    def ComNodeSize(self):
        return self._ComNodeSize

    @ComNodeSize.setter
    def ComNodeSize(self, ComNodeSize):
        self._ComNodeSize = ComNodeSize

    @property
    def MasterResource(self):
        return self._MasterResource

    @MasterResource.setter
    def MasterResource(self, MasterResource):
        self._MasterResource = MasterResource

    @property
    def CoreResource(self):
        return self._CoreResource

    @CoreResource.setter
    def CoreResource(self, CoreResource):
        self._CoreResource = CoreResource

    @property
    def TaskResource(self):
        return self._TaskResource

    @TaskResource.setter
    def TaskResource(self, TaskResource):
        self._TaskResource = TaskResource

    @property
    def ComResource(self):
        return self._ComResource

    @ComResource.setter
    def ComResource(self, ComResource):
        self._ComResource = ComResource

    @property
    def OnCos(self):
        return self._OnCos

    @OnCos.setter
    def OnCos(self, OnCos):
        self._OnCos = OnCos

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RouterNodeSize(self):
        return self._RouterNodeSize

    @RouterNodeSize.setter
    def RouterNodeSize(self, RouterNodeSize):
        self._RouterNodeSize = RouterNodeSize

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityOn(self):
        return self._SecurityOn

    @SecurityOn.setter
    def SecurityOn(self, SecurityOn):
        self._SecurityOn = SecurityOn

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def CbsEncrypt(self):
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def PublicKeyId(self):
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._SoftInfo = params.get("SoftInfo")
        self._MasterNodeSize = params.get("MasterNodeSize")
        self._CoreNodeSize = params.get("CoreNodeSize")
        self._TaskNodeSize = params.get("TaskNodeSize")
        self._ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self._MasterResource = ResourceDetail()
            self._MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self._CoreResource = ResourceDetail()
            self._CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self._TaskResource = ResourceDetail()
            self._TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self._ComResource = ResourceDetail()
            self._ComResource._deserialize(params.get("ComResource"))
        self._OnCos = params.get("OnCos")
        self._ChargeType = params.get("ChargeType")
        self._RouterNodeSize = params.get("RouterNodeSize")
        self._SupportHA = params.get("SupportHA")
        self._SecurityOn = params.get("SecurityOn")
        self._SecurityGroup = params.get("SecurityGroup")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._ApplicationRole = params.get("ApplicationRole")
        self._SecurityGroups = params.get("SecurityGroups")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigOutter(AbstractModel):
    """EMR产品配置

    """

    def __init__(self):
        r"""
        :param _SoftInfo: 软件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param _MasterNodeSize: Master节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param _CoreNodeSize: Core节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param _TaskNodeSize: Task节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param _ComNodeSize: Common节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param _MasterResource: Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _CoreResource: Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _TaskResource: Task节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _ComResource: Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _OnCos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。
        :type OnCos: bool
        :param _ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _RouterNodeSize: Router节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RouterNodeSize: int
        :param _SupportHA: 是否支持HA
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportHA: bool
        :param _SecurityOn: 是否支持安全模式
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityOn: bool
        :param _SecurityGroup: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: str
        :param _CbsEncrypt: 是否开启Cbs加密
注意：此字段可能返回 null，表示取不到有效值。
        :type CbsEncrypt: int
        :param _ApplicationRole: 自定义应用角色。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRole: str
        :param _SecurityGroups: 安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param _PublicKeyId: SSH密钥Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKeyId: str
        """
        self._SoftInfo = None
        self._MasterNodeSize = None
        self._CoreNodeSize = None
        self._TaskNodeSize = None
        self._ComNodeSize = None
        self._MasterResource = None
        self._CoreResource = None
        self._TaskResource = None
        self._ComResource = None
        self._OnCos = None
        self._ChargeType = None
        self._RouterNodeSize = None
        self._SupportHA = None
        self._SecurityOn = None
        self._SecurityGroup = None
        self._CbsEncrypt = None
        self._ApplicationRole = None
        self._SecurityGroups = None
        self._PublicKeyId = None

    @property
    def SoftInfo(self):
        return self._SoftInfo

    @SoftInfo.setter
    def SoftInfo(self, SoftInfo):
        self._SoftInfo = SoftInfo

    @property
    def MasterNodeSize(self):
        return self._MasterNodeSize

    @MasterNodeSize.setter
    def MasterNodeSize(self, MasterNodeSize):
        self._MasterNodeSize = MasterNodeSize

    @property
    def CoreNodeSize(self):
        return self._CoreNodeSize

    @CoreNodeSize.setter
    def CoreNodeSize(self, CoreNodeSize):
        self._CoreNodeSize = CoreNodeSize

    @property
    def TaskNodeSize(self):
        return self._TaskNodeSize

    @TaskNodeSize.setter
    def TaskNodeSize(self, TaskNodeSize):
        self._TaskNodeSize = TaskNodeSize

    @property
    def ComNodeSize(self):
        return self._ComNodeSize

    @ComNodeSize.setter
    def ComNodeSize(self, ComNodeSize):
        self._ComNodeSize = ComNodeSize

    @property
    def MasterResource(self):
        return self._MasterResource

    @MasterResource.setter
    def MasterResource(self, MasterResource):
        self._MasterResource = MasterResource

    @property
    def CoreResource(self):
        return self._CoreResource

    @CoreResource.setter
    def CoreResource(self, CoreResource):
        self._CoreResource = CoreResource

    @property
    def TaskResource(self):
        return self._TaskResource

    @TaskResource.setter
    def TaskResource(self, TaskResource):
        self._TaskResource = TaskResource

    @property
    def ComResource(self):
        return self._ComResource

    @ComResource.setter
    def ComResource(self, ComResource):
        self._ComResource = ComResource

    @property
    def OnCos(self):
        return self._OnCos

    @OnCos.setter
    def OnCos(self, OnCos):
        self._OnCos = OnCos

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RouterNodeSize(self):
        return self._RouterNodeSize

    @RouterNodeSize.setter
    def RouterNodeSize(self, RouterNodeSize):
        self._RouterNodeSize = RouterNodeSize

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityOn(self):
        return self._SecurityOn

    @SecurityOn.setter
    def SecurityOn(self, SecurityOn):
        self._SecurityOn = SecurityOn

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def CbsEncrypt(self):
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def PublicKeyId(self):
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._SoftInfo = params.get("SoftInfo")
        self._MasterNodeSize = params.get("MasterNodeSize")
        self._CoreNodeSize = params.get("CoreNodeSize")
        self._TaskNodeSize = params.get("TaskNodeSize")
        self._ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self._MasterResource = OutterResource()
            self._MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self._CoreResource = OutterResource()
            self._CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self._TaskResource = OutterResource()
            self._TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self._ComResource = OutterResource()
            self._ComResource._deserialize(params.get("ComResource"))
        self._OnCos = params.get("OnCos")
        self._ChargeType = params.get("ChargeType")
        self._RouterNodeSize = params.get("RouterNodeSize")
        self._SupportHA = params.get("SupportHA")
        self._SecurityOn = params.get("SecurityOn")
        self._SecurityGroup = params.get("SecurityGroup")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._ApplicationRole = params.get("ApplicationRole")
        self._SecurityGroups = params.get("SecurityGroups")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Execution(AbstractModel):
    """执行动作。

    """

    def __init__(self):
        r"""
        :param _JobType: 任务类型，目前支持以下类型。
1. “MR”，将通过hadoop jar的方式提交。
2. "HIVE"，将通过hive -f的方式提交。
3. "SPARK"，将通过spark-submit的方式提交。
        :type JobType: str
        :param _Args: 任务参数，提供除提交指令以外的参数。
        :type Args: list of str
        """
        self._JobType = None
        self._Args = None

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._JobType = params.get("JobType")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalService(AbstractModel):
    """共用组件信息

    """

    def __init__(self):
        r"""
        :param _ShareType: 共用组件类型，EMR/CUSTOM
        :type ShareType: str
        :param _CustomServiceDefineList: 自定义参数集合
        :type CustomServiceDefineList: list of CustomServiceDefine
        :param _Service: 共用组件名
        :type Service: str
        :param _InstanceId: 共用组件集群
        :type InstanceId: str
        """
        self._ShareType = None
        self._CustomServiceDefineList = None
        self._Service = None
        self._InstanceId = None

    @property
    def ShareType(self):
        return self._ShareType

    @ShareType.setter
    def ShareType(self, ShareType):
        self._ShareType = ShareType

    @property
    def CustomServiceDefineList(self):
        return self._CustomServiceDefineList

    @CustomServiceDefineList.setter
    def CustomServiceDefineList(self, CustomServiceDefineList):
        self._CustomServiceDefineList = CustomServiceDefineList

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ShareType = params.get("ShareType")
        if params.get("CustomServiceDefineList") is not None:
            self._CustomServiceDefineList = []
            for item in params.get("CustomServiceDefineList"):
                obj = CustomServiceDefine()
                obj._deserialize(item)
                self._CustomServiceDefineList.append(obj)
        self._Service = params.get("Service")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FairGlobalConfig(AbstractModel):
    """资源调度-公平调度器的全局配置

    """

    def __init__(self):
        r"""
        :param _UserMaxAppsDefault: 对应与页面的<p>程序上限</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserMaxAppsDefault: int
        """
        self._UserMaxAppsDefault = None

    @property
    def UserMaxAppsDefault(self):
        return self._UserMaxAppsDefault

    @UserMaxAppsDefault.setter
    def UserMaxAppsDefault(self, UserMaxAppsDefault):
        self._UserMaxAppsDefault = UserMaxAppsDefault


    def _deserialize(self, params):
        self._UserMaxAppsDefault = params.get("UserMaxAppsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """Emr集群列表实例自定义查询过滤

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Values: 过滤字段值
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
        


class FlowExtraDetail(AbstractModel):
    """流程额外信息

    """

    def __init__(self):
        r"""
        :param _Title: 额外信息Title
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Detail: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of FlowParamsDesc
        """
        self._Title = None
        self._Detail = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Title = params.get("Title")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = FlowParamsDesc()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowParam(AbstractModel):
    """FlowParam流程参数

    """

    def __init__(self):
        r"""
        :param _FKey: 流程参数key
TraceId：通过TraceId查询
FlowId： 通过FlowId查询
        :type FKey: str
        :param _FValue: 参数value
        :type FValue: str
        """
        self._FKey = None
        self._FValue = None

    @property
    def FKey(self):
        return self._FKey

    @FKey.setter
    def FKey(self, FKey):
        self._FKey = FKey

    @property
    def FValue(self):
        return self._FValue

    @FValue.setter
    def FValue(self, FValue):
        self._FValue = FValue


    def _deserialize(self, params):
        self._FKey = params.get("FKey")
        self._FValue = params.get("FValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowParamsDesc(AbstractModel):
    """任务参数描述

    """

    def __init__(self):
        r"""
        :param _PKey: 参数key
        :type PKey: str
        :param _PValue: 参数value
注意：此字段可能返回 null，表示取不到有效值。
        :type PValue: str
        """
        self._PKey = None
        self._PValue = None

    @property
    def PKey(self):
        return self._PKey

    @PKey.setter
    def PKey(self, PKey):
        self._PKey = PKey

    @property
    def PValue(self):
        return self._PValue

    @PValue.setter
    def PValue(self, PValue):
        self._PValue = PValue


    def _deserialize(self, params):
        self._PKey = params.get("PKey")
        self._PValue = params.get("PValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupGlobalConfs(AbstractModel):
    """集群所有伸缩组全局参数信息

    """

    def __init__(self):
        r"""
        :param _GroupGlobalConf: 伸缩组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupGlobalConf: :class:`tencentcloud.emr.v20190103.models.AutoScaleResourceConf`
        :param _CurrentNodes: 当前伸缩组扩容出来的节点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentNodes: int
        :param _CurrentPostPaidNodes: 当前伸缩组扩容出来的后付费节点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentPostPaidNodes: int
        :param _CurrentSpotPaidNodes: 当前伸缩组扩容出来的竞价实例节点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentSpotPaidNodes: int
        """
        self._GroupGlobalConf = None
        self._CurrentNodes = None
        self._CurrentPostPaidNodes = None
        self._CurrentSpotPaidNodes = None

    @property
    def GroupGlobalConf(self):
        return self._GroupGlobalConf

    @GroupGlobalConf.setter
    def GroupGlobalConf(self, GroupGlobalConf):
        self._GroupGlobalConf = GroupGlobalConf

    @property
    def CurrentNodes(self):
        return self._CurrentNodes

    @CurrentNodes.setter
    def CurrentNodes(self, CurrentNodes):
        self._CurrentNodes = CurrentNodes

    @property
    def CurrentPostPaidNodes(self):
        return self._CurrentPostPaidNodes

    @CurrentPostPaidNodes.setter
    def CurrentPostPaidNodes(self, CurrentPostPaidNodes):
        self._CurrentPostPaidNodes = CurrentPostPaidNodes

    @property
    def CurrentSpotPaidNodes(self):
        return self._CurrentSpotPaidNodes

    @CurrentSpotPaidNodes.setter
    def CurrentSpotPaidNodes(self, CurrentSpotPaidNodes):
        self._CurrentSpotPaidNodes = CurrentSpotPaidNodes


    def _deserialize(self, params):
        if params.get("GroupGlobalConf") is not None:
            self._GroupGlobalConf = AutoScaleResourceConf()
            self._GroupGlobalConf._deserialize(params.get("GroupGlobalConf"))
        self._CurrentNodes = params.get("CurrentNodes")
        self._CurrentPostPaidNodes = params.get("CurrentPostPaidNodes")
        self._CurrentSpotPaidNodes = params.get("CurrentSpotPaidNodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """进程健康状态

    """

    def __init__(self):
        r"""
        :param _Code: 运行正常
        :type Code: int
        :param _Text: 运行正常
        :type Text: str
        :param _Desc: 运行正常
        :type Desc: str
        """
        self._Code = None
        self._Text = None
        self._Desc = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Text = params.get("Text")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HiveQuery(AbstractModel):
    """Hive查询详情

    """

    def __init__(self):
        r"""
        :param _Statement: 查询语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Statement: str
        :param _Duration: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _StartTime: 开始时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 结束时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _JobIds: appId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobIds: list of str
        :param _ExecutionEngine: 执行引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEngine: str
        :param _Id: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self._Statement = None
        self._Duration = None
        self._StartTime = None
        self._EndTime = None
        self._State = None
        self._User = None
        self._JobIds = None
        self._ExecutionEngine = None
        self._Id = None

    @property
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def ExecutionEngine(self):
        return self._ExecutionEngine

    @ExecutionEngine.setter
    def ExecutionEngine(self, ExecutionEngine):
        self._ExecutionEngine = ExecutionEngine

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Duration = params.get("Duration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._User = params.get("User")
        self._JobIds = params.get("JobIds")
        self._ExecutionEngine = params.get("ExecutionEngine")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostVolumeContext(AbstractModel):
    """Pod HostPath挂载方式描述

    """

    def __init__(self):
        r"""
        :param _VolumePath: Pod挂载宿主机的目录。资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumePath: str
        """
        self._VolumePath = None

    @property
    def VolumePath(self):
        return self._VolumePath

    @VolumePath.setter
    def VolumePath(self, VolumePath):
        self._VolumePath = VolumePath


    def _deserialize(self, params):
        self._VolumePath = params.get("VolumePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImpalaQuery(AbstractModel):
    """Impala查询详情

    """

    def __init__(self):
        r"""
        :param _Statement: 执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Statement: str
        :param _Id: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _Duration: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _State: 执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _RowsFetched: 获取行数
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsFetched: int
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _DefaultDB: 默认DB
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDB: str
        :param _Coordinator: 执行的Coordinator节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Coordinator: str
        :param _MaxNodePeakMemoryUsage: 单节点内存峰值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNodePeakMemoryUsage: str
        :param _QueryType: 查询类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryType: str
        :param _ScanHDFSRows: 扫描的HDFS行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanHDFSRows: int
        :param _ScanKUDURows: 扫描的Kudu行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanKUDURows: int
        :param _ScanRowsTotal: 扫描的总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRowsTotal: int
        :param _TotalBytesRead: 读取的总字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalBytesRead: int
        :param _TotalBytesSent: 发送的总字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalBytesSent: int
        :param _TotalCpuTime: CPU总时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCpuTime: int
        :param _TotalInnerBytesSent: 内部数据发送总量(Bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalInnerBytesSent: int
        :param _TotalScanBytesSent: 内部扫描数据发送总量(Bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalScanBytesSent: int
        :param _EstimatedPerHostMemBytes: 预估单节点内存
注意：此字段可能返回 null，表示取不到有效值。
        :type EstimatedPerHostMemBytes: int
        :param _NumRowsFetchedFromCache: 从缓存中获取的数据行数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumRowsFetchedFromCache: int
        :param _SessionId: 会话ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _PerNodePeakMemoryBytesSum: 单节点内存峰值和(Bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type PerNodePeakMemoryBytesSum: int
        :param _BackendsCount: 后端个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BackendsCount: int
        :param _FragmentInstancesCount: fragment数
注意：此字段可能返回 null，表示取不到有效值。
        :type FragmentInstancesCount: int
        :param _RemainingFragmentCount: 剩余未完成Fragment数
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingFragmentCount: int
        """
        self._Statement = None
        self._Id = None
        self._StartTime = None
        self._Duration = None
        self._EndTime = None
        self._State = None
        self._RowsFetched = None
        self._User = None
        self._DefaultDB = None
        self._Coordinator = None
        self._MaxNodePeakMemoryUsage = None
        self._QueryType = None
        self._ScanHDFSRows = None
        self._ScanKUDURows = None
        self._ScanRowsTotal = None
        self._TotalBytesRead = None
        self._TotalBytesSent = None
        self._TotalCpuTime = None
        self._TotalInnerBytesSent = None
        self._TotalScanBytesSent = None
        self._EstimatedPerHostMemBytes = None
        self._NumRowsFetchedFromCache = None
        self._SessionId = None
        self._PerNodePeakMemoryBytesSum = None
        self._BackendsCount = None
        self._FragmentInstancesCount = None
        self._RemainingFragmentCount = None

    @property
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RowsFetched(self):
        return self._RowsFetched

    @RowsFetched.setter
    def RowsFetched(self, RowsFetched):
        self._RowsFetched = RowsFetched

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DefaultDB(self):
        return self._DefaultDB

    @DefaultDB.setter
    def DefaultDB(self, DefaultDB):
        self._DefaultDB = DefaultDB

    @property
    def Coordinator(self):
        return self._Coordinator

    @Coordinator.setter
    def Coordinator(self, Coordinator):
        self._Coordinator = Coordinator

    @property
    def MaxNodePeakMemoryUsage(self):
        return self._MaxNodePeakMemoryUsage

    @MaxNodePeakMemoryUsage.setter
    def MaxNodePeakMemoryUsage(self, MaxNodePeakMemoryUsage):
        self._MaxNodePeakMemoryUsage = MaxNodePeakMemoryUsage

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ScanHDFSRows(self):
        return self._ScanHDFSRows

    @ScanHDFSRows.setter
    def ScanHDFSRows(self, ScanHDFSRows):
        self._ScanHDFSRows = ScanHDFSRows

    @property
    def ScanKUDURows(self):
        return self._ScanKUDURows

    @ScanKUDURows.setter
    def ScanKUDURows(self, ScanKUDURows):
        self._ScanKUDURows = ScanKUDURows

    @property
    def ScanRowsTotal(self):
        return self._ScanRowsTotal

    @ScanRowsTotal.setter
    def ScanRowsTotal(self, ScanRowsTotal):
        self._ScanRowsTotal = ScanRowsTotal

    @property
    def TotalBytesRead(self):
        return self._TotalBytesRead

    @TotalBytesRead.setter
    def TotalBytesRead(self, TotalBytesRead):
        self._TotalBytesRead = TotalBytesRead

    @property
    def TotalBytesSent(self):
        return self._TotalBytesSent

    @TotalBytesSent.setter
    def TotalBytesSent(self, TotalBytesSent):
        self._TotalBytesSent = TotalBytesSent

    @property
    def TotalCpuTime(self):
        return self._TotalCpuTime

    @TotalCpuTime.setter
    def TotalCpuTime(self, TotalCpuTime):
        self._TotalCpuTime = TotalCpuTime

    @property
    def TotalInnerBytesSent(self):
        return self._TotalInnerBytesSent

    @TotalInnerBytesSent.setter
    def TotalInnerBytesSent(self, TotalInnerBytesSent):
        self._TotalInnerBytesSent = TotalInnerBytesSent

    @property
    def TotalScanBytesSent(self):
        return self._TotalScanBytesSent

    @TotalScanBytesSent.setter
    def TotalScanBytesSent(self, TotalScanBytesSent):
        self._TotalScanBytesSent = TotalScanBytesSent

    @property
    def EstimatedPerHostMemBytes(self):
        return self._EstimatedPerHostMemBytes

    @EstimatedPerHostMemBytes.setter
    def EstimatedPerHostMemBytes(self, EstimatedPerHostMemBytes):
        self._EstimatedPerHostMemBytes = EstimatedPerHostMemBytes

    @property
    def NumRowsFetchedFromCache(self):
        return self._NumRowsFetchedFromCache

    @NumRowsFetchedFromCache.setter
    def NumRowsFetchedFromCache(self, NumRowsFetchedFromCache):
        self._NumRowsFetchedFromCache = NumRowsFetchedFromCache

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def PerNodePeakMemoryBytesSum(self):
        return self._PerNodePeakMemoryBytesSum

    @PerNodePeakMemoryBytesSum.setter
    def PerNodePeakMemoryBytesSum(self, PerNodePeakMemoryBytesSum):
        self._PerNodePeakMemoryBytesSum = PerNodePeakMemoryBytesSum

    @property
    def BackendsCount(self):
        return self._BackendsCount

    @BackendsCount.setter
    def BackendsCount(self, BackendsCount):
        self._BackendsCount = BackendsCount

    @property
    def FragmentInstancesCount(self):
        return self._FragmentInstancesCount

    @FragmentInstancesCount.setter
    def FragmentInstancesCount(self, FragmentInstancesCount):
        self._FragmentInstancesCount = FragmentInstancesCount

    @property
    def RemainingFragmentCount(self):
        return self._RemainingFragmentCount

    @RemainingFragmentCount.setter
    def RemainingFragmentCount(self, RemainingFragmentCount):
        self._RemainingFragmentCount = RemainingFragmentCount


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._RowsFetched = params.get("RowsFetched")
        self._User = params.get("User")
        self._DefaultDB = params.get("DefaultDB")
        self._Coordinator = params.get("Coordinator")
        self._MaxNodePeakMemoryUsage = params.get("MaxNodePeakMemoryUsage")
        self._QueryType = params.get("QueryType")
        self._ScanHDFSRows = params.get("ScanHDFSRows")
        self._ScanKUDURows = params.get("ScanKUDURows")
        self._ScanRowsTotal = params.get("ScanRowsTotal")
        self._TotalBytesRead = params.get("TotalBytesRead")
        self._TotalBytesSent = params.get("TotalBytesSent")
        self._TotalCpuTime = params.get("TotalCpuTime")
        self._TotalInnerBytesSent = params.get("TotalInnerBytesSent")
        self._TotalScanBytesSent = params.get("TotalScanBytesSent")
        self._EstimatedPerHostMemBytes = params.get("EstimatedPerHostMemBytes")
        self._NumRowsFetchedFromCache = params.get("NumRowsFetchedFromCache")
        self._SessionId = params.get("SessionId")
        self._PerNodePeakMemoryBytesSum = params.get("PerNodePeakMemoryBytesSum")
        self._BackendsCount = params.get("BackendsCount")
        self._FragmentInstancesCount = params.get("FragmentInstancesCount")
        self._RemainingFragmentCount = params.get("RemainingFragmentCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrRequest(AbstractModel):
    """InquirePriceRenewEmr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费一个月
        :type TimeSpan: int
        :param _InstanceId: 待续费集群ID列表。
        :type InstanceId: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。
        :type PayMode: int
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
        self._TimeSpan = None
        self._InstanceId = None
        self._Placement = None
        self._PayMode = None
        self._TimeUnit = None
        self._Currency = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._InstanceId = params.get("InstanceId")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrResponse(AbstractModel):
    """InquirePriceRenewEmr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param _Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：<li>ProductId为2(EMR-V2.0.1)的时候，必选组件包括：hdfs-2.7.3,yarn-2.7.3,zookeeper-3.4.9,knox-1.2.0</li><li>ProductId为16(EMR-V2.3.0)的时候，必选组件包括：hdfs-2.8.5,yarn-2.8.5,zookeeper-3.5.5,knox-1.2.0</li><li>ProductId为20(EMR-V2.5.0)的时候，必选组件包括：hdfs-2.8.5,yarn-2.8.5,zookeeper-3.6.1,knox-1.2.0</li><li>ProductId为30(EMR-V2.6.0)的时候，必选组件包括：hdfs-2.8.5,yarn-2.8.5,zookeeper-3.6.1,openldap-2.4.44,knox-1.2.0</li><li>ProductId为38(EMR-V2.7.0)的时候，必选组件包括：hdfs-2.8.5,yarn-2.8.5,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li><li>ProductId为57(EMR-V2.8.0)的时候，必选组件包括：hdfs-2.8.5,yarn-2.8.5,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li><li>ProductId为7(EMR-V3.0.0)的时候，必选组件包括：hdfs-3.1.2,yarn-3.1.2,zookeeper-3.4.9,knox-1.2.0</li><li>ProductId为25(EMR-V3.1.0)的时候，必选组件包括：hdfs-3.1.2,yarn-3.1.2,zookeeper-3.6.1,knox-1.2.0</li><li>ProductId为31(EMR-V3.1.1)的时候，必选组件包括：hdfs-3.1.2,yarn-3.1.2,zookeeper-3.6.1,knox-1.2.0</li><li>ProductId为28(EMR-V3.2.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.1,knox-1.2.0</li><li>ProductId为33(EMR-V3.2.1)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.1,openldap-2.4.44,knox-1.2.0</li><li>ProductId为34(EMR-V3.3.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.1,openldap-2.4.44,knox-1.2.0</li><li>ProductId为37(EMR-V3.4.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li><li>ProductId为44(EMR-V3.5.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li><li>ProductId为53(EMR-V3.6.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li><li>ProductId为58(EMR-V3.6.1)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.3,openldap-2.4.46,knox-1.6.1</li><li>ProductId为47(EMR-V4.0.0)的时候，必选组件包括：hdfs-3.2.2,yarn-3.2.2,zookeeper-3.6.3,openldap-2.4.44,knox-1.6.1</li>
        :type Software: list of str
        :param _ResourceSpec: 询价的节点规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：<li>2：表示EMR-V2.0.1</li><li>16：表示EMR-V2.3.0</li><li>20：表示EMR-V2.5.0</li><li>30：表示EMR-V2.6.0</li><li>38：表示EMR-V2.7.0</li><li>57：表示EMR-V2.8.0</li><li>7：表示EMR-V3.0.0</li><li>25：表示EMR-V3.1.0</li><li>31：表示EMR-V3.1.1</li><li>28：表示EMR-V3.2.0</li><li>33：表示EMR-V3.2.1</li><li>34：表示EMR-V3.3.0</li><li>37：表示EMR-V3.4.0</li><li>44：表示EMR-V3.5.0</li><li>53：表示EMR-V3.6.0</li><li>58：表示EMR-V3.6.1</li><li>47：表示EMR-V4.0.0</li>
        :type ProductId: int
        :param _SceneName: 场景化取值：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: 共用组件信息
        :type ExternalService: list of ExternalService
        :param _VersionID: 当前默认值为0，跨AZ特性支持后为1
        :type VersionID: int
        :param _MultiZoneSettings: 可用区的规格信息
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._Currency = None
        self._PayMode = None
        self._SupportHA = None
        self._Software = None
        self._ResourceSpec = None
        self._Placement = None
        self._VPCSettings = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ProductId = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZoneSettings = None

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
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZoneSettings(self):
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._Currency = params.get("Currency")
        self._PayMode = params.get("PayMode")
        self._SupportHA = params.get("SupportHA")
        self._Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ProductId = params.get("ProductId")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 购买实例的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _PriceList: 价格清单
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceList: list of ZoneDetailPriceResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceList = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

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
    def PriceList(self):
        return self._PriceList

    @PriceList.setter
    def PriceList(self, PriceList):
        self._PriceList = PriceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceList") is not None:
            self._PriceList = []
            for item in params.get("PriceList"):
                obj = ZoneDetailPriceResult()
                obj._deserialize(item)
                self._PriceList.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费一个月
        :type TimeSpan: int
        :param _ResourceIds: 待续费节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr)查询。
        :type ResourceIds: list of str
        :param _PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。
        :type PayMode: int
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _ModifyPayMode: 是否按量转包年包月。0：否，1：是。
        :type ModifyPayMode: int
        """
        self._TimeSpan = None
        self._ResourceIds = None
        self._PayMode = None
        self._TimeUnit = None
        self._Currency = None
        self._Placement = None
        self._ModifyPayMode = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ModifyPayMode(self):
        return self._ModifyPayMode

    @ModifyPayMode.setter
    def ModifyPayMode(self, ModifyPayMode):
        self._ModifyPayMode = ModifyPayMode


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._ResourceIds = params.get("ResourceIds")
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _ZoneId: 实例所属的可用区ID，例如100003。该参数可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/213/15707) 的返回值中的ZoneId字段来获取。
        :type ZoneId: int
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param _TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        :param _MasterCount: 扩容的Master节点数量。
        :type MasterCount: int
        :param _ResourceBaseType: 类型为ComputeResource和EMR以及默认，默认为EMR
        :type ResourceBaseType: str
        :param _ComputeResourceId: 计算资源id
        :type ComputeResourceId: str
        :param _HardwareResourceType: 扩容资源类型
        :type HardwareResourceType: str
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._ZoneId = None
        self._PayMode = None
        self._InstanceId = None
        self._CoreCount = None
        self._TaskCount = None
        self._Currency = None
        self._RouterCount = None
        self._MasterCount = None
        self._ResourceBaseType = None
        self._ComputeResourceId = None
        self._HardwareResourceType = None

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
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RouterCount(self):
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def ResourceBaseType(self):
        return self._ResourceBaseType

    @ResourceBaseType.setter
    def ResourceBaseType(self, ResourceBaseType):
        self._ResourceBaseType = ResourceBaseType

    @property
    def ComputeResourceId(self):
        return self._ComputeResourceId

    @ComputeResourceId.setter
    def ComputeResourceId(self, ComputeResourceId):
        self._ComputeResourceId = ComputeResourceId

    @property
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._ZoneId = params.get("ZoneId")
        self._PayMode = params.get("PayMode")
        self._InstanceId = params.get("InstanceId")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._Currency = params.get("Currency")
        self._RouterCount = params.get("RouterCount")
        self._MasterCount = params.get("MasterCount")
        self._ResourceBaseType = params.get("ResourceBaseType")
        self._ComputeResourceId = params.get("ComputeResourceId")
        self._HardwareResourceType = params.get("HardwareResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param _Unit: 扩容的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _PriceSpec: 询价的节点规格。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _MultipleEmrPrice: 对应入参MultipleResources中多个规格的询价结果，其它出参返回的是第一个规格的询价结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MultipleEmrPrice: list of EmrPrice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._MultipleEmrPrice = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def MultipleEmrPrice(self):
        return self._MultipleEmrPrice

    @MultipleEmrPrice.setter
    def MultipleEmrPrice(self, MultipleEmrPrice):
        self._MultipleEmrPrice = MultipleEmrPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        if params.get("MultipleEmrPrice") is not None:
            self._MultipleEmrPrice = []
            for item in params.get("MultipleEmrPrice"):
                obj = EmrPrice()
                obj._deserialize(item)
                self._MultipleEmrPrice.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 变配的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _UpdateSpec: 节点变配的目标配置。
        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _ResourceIdList: 批量变配资源ID列表
        :type ResourceIdList: list of str
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._PayMode = None
        self._UpdateSpec = None
        self._Placement = None
        self._Currency = None
        self._ResourceIdList = None

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def UpdateSpec(self):
        return self._UpdateSpec

    @UpdateSpec.setter
    def UpdateSpec(self, UpdateSpec):
        self._UpdateSpec = UpdateSpec

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def ResourceIdList(self):
        return self._ResourceIdList

    @ResourceIdList.setter
    def ResourceIdList(self, ResourceIdList):
        self._ResourceIdList = ResourceIdList


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._PayMode = params.get("PayMode")
        if params.get("UpdateSpec") is not None:
            self._UpdateSpec = UpdateInstanceSettings()
            self._UpdateSpec._deserialize(params.get("UpdateSpec"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._Currency = params.get("Currency")
        self._ResourceIdList = params.get("ResourceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 变配的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _PriceDetail: 价格详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceDetail: list of PriceDetail
        :param _NewConfigPrice: 新配置价格
注意：此字段可能返回 null，表示取不到有效值。
        :type NewConfigPrice: :class:`tencentcloud.emr.v20190103.models.PriceResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceDetail = None
        self._NewConfigPrice = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

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
    def PriceDetail(self):
        return self._PriceDetail

    @PriceDetail.setter
    def PriceDetail(self, PriceDetail):
        self._PriceDetail = PriceDetail

    @property
    def NewConfigPrice(self):
        return self._NewConfigPrice

    @NewConfigPrice.setter
    def NewConfigPrice(self, NewConfigPrice):
        self._NewConfigPrice = NewConfigPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceDetail") is not None:
            self._PriceDetail = []
            for item in params.get("PriceDetail"):
                obj = PriceDetail()
                obj._deserialize(item)
                self._PriceDetail.append(obj)
        if params.get("NewConfigPrice") is not None:
            self._NewConfigPrice = PriceResult()
            self._NewConfigPrice._deserialize(params.get("NewConfigPrice"))
        self._RequestId = params.get("RequestId")


class InsightResult(AbstractModel):
    """洞察结果项

    """

    def __init__(self):
        r"""
        :param _ID: 当Type为HIVE时，是Hive查询ID，当Type为MAPREDUCE，SPARK，TEZ时则是YarnAppID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Type: 洞察应用的类型，HIVE,SPARK,MAPREDUCE,TEZ
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _RuleID: 洞察规则ID
HIVE-ScanManyMeta:元数据扫描过多
HIVE-ScanManyPartition:大表扫描
HIVE-SlowCompile:编译耗时过长
HIVE-UnSuitableConfig:不合理参数
MAPREDUCE-MapperDataSkew:Map数据倾斜
MAPREDUCE-MapperMemWaste:MapMemory资源浪费
MAPREDUCE-MapperSlowTask:Map慢Task
MAPREDUCE-MapperTaskGC:MapperTaskGC
MAPREDUCE-MemExceeded:峰值内存超限
MAPREDUCE-ReducerDataSkew:Reduce数据倾斜
MAPREDUCE-ReducerMemWaste:ReduceMemory资源浪费
MAPREDUCE-ReducerSlowTask:Reduce慢Task
MAPREDUCE-ReducerTaskGC:ReducerTaskGC
MAPREDUCE-SchedulingDelay:调度延迟
SPARK-CpuWaste:CPU资源浪费
SPARK-DataSkew:数据倾斜
SPARK-ExecutorGC:ExecutorGC
SPARK-MemExceeded:峰值内存超限
SPARK-MemWaste:Memory资源浪费
SPARK-ScheduleOverhead:ScheduleOverhead
SPARK-ScheduleSkew:调度倾斜
SPARK-SlowTask:慢Task
TEZ-DataSkew:数据倾斜
TEZ-MapperDataSkew:Map数据倾斜
TEZ-ReducerDataSkew:Reduce数据倾斜
TEZ-TezMemWaste:Memory资源浪费
TEZ-TezSlowTask:慢Task
TEZ-TezTaskGC:TasksGC
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: str
        :param _RuleName: 洞察规则名字，可参考RuleID的说明
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _RuleExplain: 洞察规则解释
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleExplain: str
        :param _Detail: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        :param _Suggestion: 建议信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Value: 洞察异常衡量值，同类型的洞察项越大越严重，不同类型的洞察项无对比意义
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        :param _ScheduleTaskExecID: 调度任务执行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTaskExecID: str
        :param _ScheduleFlowName: 调度流，DAG
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleFlowName: str
        :param _ScheduleTaskName: 调度flow中的某个task节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTaskName: str
        :param _JobConf: Yarn任务的部分核心配置
注意：此字段可能返回 null，表示取不到有效值。
        :type JobConf: str
        """
        self._ID = None
        self._Type = None
        self._RuleID = None
        self._RuleName = None
        self._RuleExplain = None
        self._Detail = None
        self._Suggestion = None
        self._Value = None
        self._ScheduleTaskExecID = None
        self._ScheduleFlowName = None
        self._ScheduleTaskName = None
        self._JobConf = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleExplain(self):
        return self._RuleExplain

    @RuleExplain.setter
    def RuleExplain(self, RuleExplain):
        self._RuleExplain = RuleExplain

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ScheduleTaskExecID(self):
        return self._ScheduleTaskExecID

    @ScheduleTaskExecID.setter
    def ScheduleTaskExecID(self, ScheduleTaskExecID):
        self._ScheduleTaskExecID = ScheduleTaskExecID

    @property
    def ScheduleFlowName(self):
        return self._ScheduleFlowName

    @ScheduleFlowName.setter
    def ScheduleFlowName(self, ScheduleFlowName):
        self._ScheduleFlowName = ScheduleFlowName

    @property
    def ScheduleTaskName(self):
        return self._ScheduleTaskName

    @ScheduleTaskName.setter
    def ScheduleTaskName(self, ScheduleTaskName):
        self._ScheduleTaskName = ScheduleTaskName

    @property
    def JobConf(self):
        return self._JobConf

    @JobConf.setter
    def JobConf(self, JobConf):
        self._JobConf = JobConf


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Type = params.get("Type")
        self._RuleID = params.get("RuleID")
        self._RuleName = params.get("RuleName")
        self._RuleExplain = params.get("RuleExplain")
        self._Detail = params.get("Detail")
        self._Suggestion = params.get("Suggestion")
        self._Value = params.get("Value")
        self._ScheduleTaskExecID = params.get("ScheduleTaskExecID")
        self._ScheduleFlowName = params.get("ScheduleFlowName")
        self._ScheduleTaskName = params.get("ScheduleTaskName")
        self._JobConf = params.get("JobConf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """实例预付费参数，只有在付费类型为PREPAID时生效。

    """

    def __init__(self):
        r"""
        :param _Period: 包年包月时间，默认为1，单位：月。
取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 24, 36, 48, 60。
        :type Period: int
        :param _RenewFlag: 是否自动续费，默认为否。
<li>true：是</li>
<li>false：否</li>
        :type RenewFlag: bool
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Item(AbstractModel):
    """代表一个kv结构

    """

    def __init__(self):
        r"""
        :param _Key: 健值
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 值
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
        


class ItemSeq(AbstractModel):
    """键值对组成的列表

    """

    def __init__(self):
        r"""
        :param _Items: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        """
        self._Items = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResource(AbstractModel):
    """机器资源描述。

    """

    def __init__(self):
        r"""
        :param _Spec: 机器类型描述。
        :type Spec: str
        :param _InstanceType: 机器类型描述，可参考CVM的该含义。
        :type InstanceType: str
        :param _Tags: 标签KV对。
        :type Tags: list of Tag
        :param _DiskGroups: 磁盘描述列表。
        :type DiskGroups: list of DiskGroup
        """
        self._Spec = None
        self._InstanceType = None
        self._Tags = None
        self._DiskGroups = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskGroups(self):
        return self._DiskGroups

    @DiskGroups.setter
    def DiskGroups(self, DiskGroups):
        self._DiskGroups = DiskGroups


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DiskGroups") is not None:
            self._DiskGroups = []
            for item in params.get("DiskGroups"):
                obj = DiskGroup()
                obj._deserialize(item)
                self._DiskGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResourceSpec(AbstractModel):
    """流程作业资源描述

    """

    def __init__(self):
        r"""
        :param _MasterCount: 主节点数量。
        :type MasterCount: int
        :param _MasterResourceSpec: 主节点配置。
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _CoreCount: Core节点数量
        :type CoreCount: int
        :param _CoreResourceSpec: Core节点配置。
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _TaskCount: Task节点数量。
        :type TaskCount: int
        :param _CommonCount: Common节点数量。
        :type CommonCount: int
        :param _TaskResourceSpec: Task节点配置。
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _CommonResourceSpec: Common节点配置。
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        """
        self._MasterCount = None
        self._MasterResourceSpec = None
        self._CoreCount = None
        self._CoreResourceSpec = None
        self._TaskCount = None
        self._CommonCount = None
        self._TaskResourceSpec = None
        self._CommonResourceSpec = None

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec


    def _deserialize(self, params):
        self._MasterCount = params.get("MasterCount")
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = JobFlowResource()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        self._CoreCount = params.get("CoreCount")
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = JobFlowResource()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        self._TaskCount = params.get("TaskCount")
        self._CommonCount = params.get("CommonCount")
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = JobFlowResource()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = JobFlowResource()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobResult(AbstractModel):
    """任务步骤结果描述

    """

    def __init__(self):
        r"""
        :param _Name: 任务步骤名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ActionOnFailure: 任务步骤失败时的处理策略，可以为以下值：
"CONTINUE"，跳过当前失败步骤，继续后续步骤。
“TERMINATE_CLUSTER”，终止当前及后续步骤，并销毁集群。
“CANCEL_AND_WAIT”，取消当前步骤并阻塞等待处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionOnFailure: str
        :param _JobState: 当前步骤的状态，可以为以下值：
“JobFlowStepStatusInit”，初始化状态，等待执行。
“JobFlowStepStatusRunning”，任务步骤正在执行。
“JobFlowStepStatusFailed”，任务步骤执行失败。
“JobFlowStepStatusSucceed”，任务步骤执行成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type JobState: str
        :param _ApplicationId: YARN任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        """
        self._Name = None
        self._ActionOnFailure = None
        self._JobState = None
        self._ApplicationId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionOnFailure(self):
        return self._ActionOnFailure

    @ActionOnFailure.setter
    def ActionOnFailure(self, ActionOnFailure):
        self._ActionOnFailure = ActionOnFailure

    @property
    def JobState(self):
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionOnFailure = params.get("ActionOnFailure")
        self._JobState = params.get("JobState")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """键值对，主要用来做Filter

    """

    def __init__(self):
        r"""
        :param _Key: 键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 值
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
        


class KyuubiQueryInfo(AbstractModel):
    """Kyuubi查询信息

    """

    def __init__(self):
        r"""
        :param _ClientIP: 提交IP
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param _Duration: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _EngineID: Engine Id
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineID: str
        :param _EngineType: 计算引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: str
        :param _Id: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _SessionID: Session Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionID: str
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param _ExecutionState: 执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionState: str
        :param _ExecutionStatement: 执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStatement: str
        :param _StatementID: Statement Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StatementID: str
        :param _User: 提交用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        """
        self._ClientIP = None
        self._Duration = None
        self._EndTime = None
        self._EngineID = None
        self._EngineType = None
        self._Id = None
        self._SessionID = None
        self._BeginTime = None
        self._ExecutionState = None
        self._ExecutionStatement = None
        self._StatementID = None
        self._User = None

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EngineID(self):
        return self._EngineID

    @EngineID.setter
    def EngineID(self, EngineID):
        self._EngineID = EngineID

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def ExecutionState(self):
        return self._ExecutionState

    @ExecutionState.setter
    def ExecutionState(self, ExecutionState):
        self._ExecutionState = ExecutionState

    @property
    def ExecutionStatement(self):
        return self._ExecutionStatement

    @ExecutionStatement.setter
    def ExecutionStatement(self, ExecutionStatement):
        self._ExecutionStatement = ExecutionStatement

    @property
    def StatementID(self):
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._ClientIP = params.get("ClientIP")
        self._Duration = params.get("Duration")
        self._EndTime = params.get("EndTime")
        self._EngineID = params.get("EngineID")
        self._EngineType = params.get("EngineType")
        self._Id = params.get("Id")
        self._SessionID = params.get("SessionID")
        self._BeginTime = params.get("BeginTime")
        self._ExecutionState = params.get("ExecutionState")
        self._ExecutionStatement = params.get("ExecutionStatement")
        self._StatementID = params.get("StatementID")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadAutoScaleStrategy(AbstractModel):
    """自动扩缩容基于负载指标的规则

    """

    def __init__(self):
        r"""
        :param _StrategyId: 规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _StrategyName: 规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param _CalmDownTime: 规则生效冷却时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CalmDownTime: int
        :param _ScaleAction: 扩缩容动作，1表示扩容，2表示缩容。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleAction: int
        :param _ScaleNum: 每次规则生效时的扩缩容数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleNum: int
        :param _ProcessMethod: 指标处理方法，1表示MAX，2表示MIN，3表示AVG。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessMethod: int
        :param _Priority: 规则优先级，添加时无效，默认为自增。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _StrategyStatus: 规则状态，1表示启动，3表示禁用。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyStatus: int
        :param _YarnNodeLabel: 规则扩容指定 yarn node label
注意：此字段可能返回 null，表示取不到有效值。
        :type YarnNodeLabel: str
        :param _PeriodValid: 规则生效的有效时间
        :type PeriodValid: str
        :param _GraceDownFlag: 优雅缩容开关
        :type GraceDownFlag: bool
        :param _GraceDownTime: 优雅缩容等待时间
        :type GraceDownTime: int
        :param _Tags: 绑定标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ConfigGroupAssigned: 预设配置组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigGroupAssigned: str
        :param _MeasureMethod: 扩容资源计算方法，"DEFAULT","INSTANCE", "CPU", "MEMORYGB"。
"DEFAULT"表示默认方式，与"INSTANCE"意义相同。
"INSTANCE"表示按照节点计算，默认方式。
"CPU"表示按照机器的核数计算。
"MEMORYGB"表示按照机器内存数计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type MeasureMethod: str
        :param _LoadMetricsConditions: 多指标触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadMetricsConditions: :class:`tencentcloud.emr.v20190103.models.LoadMetricsConditions`
        """
        self._StrategyId = None
        self._StrategyName = None
        self._CalmDownTime = None
        self._ScaleAction = None
        self._ScaleNum = None
        self._ProcessMethod = None
        self._Priority = None
        self._StrategyStatus = None
        self._YarnNodeLabel = None
        self._PeriodValid = None
        self._GraceDownFlag = None
        self._GraceDownTime = None
        self._Tags = None
        self._ConfigGroupAssigned = None
        self._MeasureMethod = None
        self._LoadMetricsConditions = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def CalmDownTime(self):
        return self._CalmDownTime

    @CalmDownTime.setter
    def CalmDownTime(self, CalmDownTime):
        self._CalmDownTime = CalmDownTime

    @property
    def ScaleAction(self):
        return self._ScaleAction

    @ScaleAction.setter
    def ScaleAction(self, ScaleAction):
        self._ScaleAction = ScaleAction

    @property
    def ScaleNum(self):
        return self._ScaleNum

    @ScaleNum.setter
    def ScaleNum(self, ScaleNum):
        self._ScaleNum = ScaleNum

    @property
    def ProcessMethod(self):
        return self._ProcessMethod

    @ProcessMethod.setter
    def ProcessMethod(self, ProcessMethod):
        self._ProcessMethod = ProcessMethod

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def StrategyStatus(self):
        return self._StrategyStatus

    @StrategyStatus.setter
    def StrategyStatus(self, StrategyStatus):
        self._StrategyStatus = StrategyStatus

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def PeriodValid(self):
        return self._PeriodValid

    @PeriodValid.setter
    def PeriodValid(self, PeriodValid):
        self._PeriodValid = PeriodValid

    @property
    def GraceDownFlag(self):
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def GraceDownTime(self):
        return self._GraceDownTime

    @GraceDownTime.setter
    def GraceDownTime(self, GraceDownTime):
        self._GraceDownTime = GraceDownTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ConfigGroupAssigned(self):
        return self._ConfigGroupAssigned

    @ConfigGroupAssigned.setter
    def ConfigGroupAssigned(self, ConfigGroupAssigned):
        self._ConfigGroupAssigned = ConfigGroupAssigned

    @property
    def MeasureMethod(self):
        return self._MeasureMethod

    @MeasureMethod.setter
    def MeasureMethod(self, MeasureMethod):
        self._MeasureMethod = MeasureMethod

    @property
    def LoadMetricsConditions(self):
        return self._LoadMetricsConditions

    @LoadMetricsConditions.setter
    def LoadMetricsConditions(self, LoadMetricsConditions):
        self._LoadMetricsConditions = LoadMetricsConditions


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._CalmDownTime = params.get("CalmDownTime")
        self._ScaleAction = params.get("ScaleAction")
        self._ScaleNum = params.get("ScaleNum")
        self._ProcessMethod = params.get("ProcessMethod")
        self._Priority = params.get("Priority")
        self._StrategyStatus = params.get("StrategyStatus")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        self._PeriodValid = params.get("PeriodValid")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._GraceDownTime = params.get("GraceDownTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ConfigGroupAssigned = params.get("ConfigGroupAssigned")
        self._MeasureMethod = params.get("MeasureMethod")
        if params.get("LoadMetricsConditions") is not None:
            self._LoadMetricsConditions = LoadMetricsConditions()
            self._LoadMetricsConditions._deserialize(params.get("LoadMetricsConditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadMetricsCondition(AbstractModel):
    """负载指标条件

    """

    def __init__(self):
        r"""
        :param _StatisticPeriod: 规则统计周期，提供1min,3min,5min。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticPeriod: int
        :param _TriggerThreshold: 触发次数，当连续触发超过TriggerThreshold次后才开始扩缩容。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerThreshold: int
        :param _LoadMetrics: 扩缩容负载指标。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadMetrics: str
        :param _MetricId: 规则元数据记录ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricId: int
        :param _Conditions: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of TriggerCondition
        """
        self._StatisticPeriod = None
        self._TriggerThreshold = None
        self._LoadMetrics = None
        self._MetricId = None
        self._Conditions = None

    @property
    def StatisticPeriod(self):
        return self._StatisticPeriod

    @StatisticPeriod.setter
    def StatisticPeriod(self, StatisticPeriod):
        self._StatisticPeriod = StatisticPeriod

    @property
    def TriggerThreshold(self):
        return self._TriggerThreshold

    @TriggerThreshold.setter
    def TriggerThreshold(self, TriggerThreshold):
        self._TriggerThreshold = TriggerThreshold

    @property
    def LoadMetrics(self):
        return self._LoadMetrics

    @LoadMetrics.setter
    def LoadMetrics(self, LoadMetrics):
        self._LoadMetrics = LoadMetrics

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._StatisticPeriod = params.get("StatisticPeriod")
        self._TriggerThreshold = params.get("TriggerThreshold")
        self._LoadMetrics = params.get("LoadMetrics")
        self._MetricId = params.get("MetricId")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = TriggerCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadMetricsConditions(AbstractModel):
    """负载指标

    """

    def __init__(self):
        r"""
        :param _LoadMetrics: 触发规则条件
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadMetrics: list of LoadMetricsCondition
        """
        self._LoadMetrics = None

    @property
    def LoadMetrics(self):
        return self._LoadMetrics

    @LoadMetrics.setter
    def LoadMetrics(self, LoadMetrics):
        self._LoadMetrics = LoadMetrics


    def _deserialize(self, params):
        if params.get("LoadMetrics") is not None:
            self._LoadMetrics = []
            for item in params.get("LoadMetrics"):
                obj = LoadMetricsCondition()
                obj._deserialize(item)
                self._LoadMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """登录设置

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码，8-16个字符，包含大写字母、小写字母、数字和特殊字符四种，特殊符号仅支持!@%^*，密码第一位不能为特殊字符
        :type Password: str
        :param _PublicKeyId: 密钥ID。关联密钥后，就可以通过对应的私钥来访问实例；PublicKeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取
        :type PublicKeyId: str
        """
        self._Password = None
        self._PublicKeyId = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PublicKeyId(self):
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetaDbInfo(AbstractModel):
    """元数据库信息

    """

    def __init__(self):
        r"""
        :param _MetaType: 元数据类型。
        :type MetaType: str
        :param _UnifyMetaInstanceId: 统一元数据库实例ID。
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自建元数据库信息。
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        """
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo


    def _deserialize(self, params):
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricTags(AbstractModel):
    """指标tag

    """

    def __init__(self):
        r"""
        :param _Unit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Type: 指标Type
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._Unit = None
        self._Type = None

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ResourceIds: 实例ID
        :type ResourceIds: list of str
        :param _RenewFlag: NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费  NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：表示不通知即将过期，也不自动续费。
        :type RenewFlag: str
        :param _ComputeResourceId: 计算资源id
        :type ComputeResourceId: str
        """
        self._InstanceId = None
        self._ResourceIds = None
        self._RenewFlag = None
        self._ComputeResourceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ComputeResourceId(self):
        return self._ComputeResourceId

    @ComputeResourceId.setter
    def ComputeResourceId(self, ComputeResourceId):
        self._ComputeResourceId = ComputeResourceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        self._RenewFlag = params.get("RenewFlag")
        self._ComputeResourceId = params.get("ComputeResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyAutoScaleStrategyRequest(AbstractModel):
    """ModifyAutoScaleStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StrategyType: 自动扩缩容规则类型，1表示按负载指标扩缩容，2表示按时间扩缩容。
        :type StrategyType: int
        :param _LoadAutoScaleStrategies: 按负载扩缩容的指标。
        :type LoadAutoScaleStrategies: list of LoadAutoScaleStrategy
        :param _TimeAutoScaleStrategies: 按时间扩缩容的规则。
        :type TimeAutoScaleStrategies: list of TimeAutoScaleStrategy
        :param _GroupId: 伸缩组Id
        :type GroupId: int
        """
        self._InstanceId = None
        self._StrategyType = None
        self._LoadAutoScaleStrategies = None
        self._TimeAutoScaleStrategies = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def LoadAutoScaleStrategies(self):
        return self._LoadAutoScaleStrategies

    @LoadAutoScaleStrategies.setter
    def LoadAutoScaleStrategies(self, LoadAutoScaleStrategies):
        self._LoadAutoScaleStrategies = LoadAutoScaleStrategies

    @property
    def TimeAutoScaleStrategies(self):
        return self._TimeAutoScaleStrategies

    @TimeAutoScaleStrategies.setter
    def TimeAutoScaleStrategies(self, TimeAutoScaleStrategies):
        self._TimeAutoScaleStrategies = TimeAutoScaleStrategies

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyType = params.get("StrategyType")
        if params.get("LoadAutoScaleStrategies") is not None:
            self._LoadAutoScaleStrategies = []
            for item in params.get("LoadAutoScaleStrategies"):
                obj = LoadAutoScaleStrategy()
                obj._deserialize(item)
                self._LoadAutoScaleStrategies.append(obj)
        if params.get("TimeAutoScaleStrategies") is not None:
            self._TimeAutoScaleStrategies = []
            for item in params.get("TimeAutoScaleStrategies"):
                obj = TimeAutoScaleStrategy()
                obj._deserialize(item)
                self._TimeAutoScaleStrategies.append(obj)
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScaleStrategyResponse(AbstractModel):
    """ModifyAutoScaleStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyGlobalConfigRequest(AbstractModel):
    """ModifyGlobalConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _Items: 修改的配置列表。其中Key的取值与`DescribeGlobalConfig`接口的出参一一对应，不区分大小写（如果报错找不到Key，以出参为准），分别为：
1. 开启或关闭资源调度：enableResourceSchedule；在关闭时会有一个同步的选项，Key为sync，取值为true或false。
2. 调度器类型：scheduler。
2. 开启或关闭标签：enableLabel，取值为true或false。
2. 标签目录：labelDir。
3. 是否覆盖用户指定队列：queueMappingOverride，取值为true、false。
4. 程序上限：userMaxAppsDefault。
5. 动态配置项：`DescribeGlobalConfig`接口返回的DefaultSettings中的Name字段。
Value的取值都是字符串，对于**是否覆盖用户指定队列**、**程序上限**，json规范中的null表示清空该配置的值。支持修改单个配置项的值。对于**动态配置项**则需要全量传递以进行覆盖。
        :type Items: list of Item
        """
        self._InstanceId = None
        self._Items = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalConfigResponse(AbstractModel):
    """ModifyGlobalConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyResourcePoolsRequest(AbstractModel):
    """ModifyResourcePools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群id
        :type InstanceId: str
        :param _Key: 取值范围：
<li>fair:代表公平调度标识</li>
<li>capacity:代表容量调度标识</li>
        :type Key: str
        """
        self._InstanceId = None
        self._Key = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePoolsResponse(AbstractModel):
    """ModifyResourcePools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDraft: false表示不是草稿，提交刷新请求成功
        :type IsDraft: bool
        :param _ErrorMsg: 扩展字段，暂时没用
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def IsDraft(self):
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyResourceScheduleConfigRequest(AbstractModel):
    """ModifyResourceScheduleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _Key: 业务标识，fair表示编辑公平的配置项，fairPlan表示编辑执行计划，capacity表示编辑容量的配置项
        :type Key: str
        :param _Value: 修改后的模块消息
        :type Value: str
        """
        self._InstanceId = None
        self._Key = None
        self._Value = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigResponse(AbstractModel):
    """ModifyResourceScheduleConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDraft: true为草稿，表示还没有刷新资源池
        :type IsDraft: bool
        :param _ErrorMsg: 校验错误信息，如果不为空，则说明校验失败，配置没有成功
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def IsDraft(self):
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyResourceSchedulerRequest(AbstractModel):
    """ModifyResourceScheduler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _OldValue: 老的调度器:fair
        :type OldValue: str
        :param _NewValue: 新的调度器:capacity
        :type NewValue: str
        """
        self._InstanceId = None
        self._OldValue = None
        self._NewValue = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceSchedulerResponse(AbstractModel):
    """ModifyResourceScheduler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyResourceTags(AbstractModel):
    """强制修改标签

    """

    def __init__(self):
        r"""
        :param _ResourceId: 集群id 或者 cvm id
        :type ResourceId: str
        :param _Resource: 资源6段式表达式
        :type Resource: str
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceRegion: ap-beijing
        :type ResourceRegion: str
        :param _ServiceType: emr
        :type ServiceType: str
        :param _DeleteTags: 删除的标签列表
        :type DeleteTags: list of Tag
        :param _AddTags: 添加的标签列表
        :type AddTags: list of Tag
        :param _ModifyTags: 修改的标签列表
        :type ModifyTags: list of Tag
        """
        self._ResourceId = None
        self._Resource = None
        self._ResourcePrefix = None
        self._ResourceRegion = None
        self._ServiceType = None
        self._DeleteTags = None
        self._AddTags = None
        self._ModifyTags = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags

    @property
    def AddTags(self):
        return self._AddTags

    @AddTags.setter
    def AddTags(self, AddTags):
        self._AddTags = AddTags

    @property
    def ModifyTags(self):
        return self._ModifyTags

    @ModifyTags.setter
    def ModifyTags(self, ModifyTags):
        self._ModifyTags = ModifyTags


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Resource = params.get("Resource")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = Tag()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        if params.get("AddTags") is not None:
            self._AddTags = []
            for item in params.get("AddTags"):
                obj = Tag()
                obj._deserialize(item)
                self._AddTags.append(obj)
        if params.get("ModifyTags") is not None:
            self._ModifyTags = []
            for item in params.get("ModifyTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ModifyTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagsRequest(AbstractModel):
    """ModifyResourcesTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModifyType: 标签类型，取值Cluster或者Node
        :type ModifyType: str
        :param _ModifyResourceTagsInfoList: 标签信息
        :type ModifyResourceTagsInfoList: list of ModifyResourceTags
        """
        self._ModifyType = None
        self._ModifyResourceTagsInfoList = None

    @property
    def ModifyType(self):
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ModifyResourceTagsInfoList(self):
        return self._ModifyResourceTagsInfoList

    @ModifyResourceTagsInfoList.setter
    def ModifyResourceTagsInfoList(self, ModifyResourceTagsInfoList):
        self._ModifyResourceTagsInfoList = ModifyResourceTagsInfoList


    def _deserialize(self, params):
        self._ModifyType = params.get("ModifyType")
        if params.get("ModifyResourceTagsInfoList") is not None:
            self._ModifyResourceTagsInfoList = []
            for item in params.get("ModifyResourceTagsInfoList"):
                obj = ModifyResourceTags()
                obj._deserialize(item)
                self._ModifyResourceTagsInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagsResponse(AbstractModel):
    """ModifyResourcesTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessList: 成功的资源id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessList: list of str
        :param _FailList: 失败的资源id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailList: list of str
        :param _PartSuccessList: 部分成功的资源id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PartSuccessList: list of str
        :param _ClusterToFlowIdList: 集群id与流程id的映射列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterToFlowIdList: list of ClusterIDToFlowID
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessList = None
        self._FailList = None
        self._PartSuccessList = None
        self._ClusterToFlowIdList = None
        self._RequestId = None

    @property
    def SuccessList(self):
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

    @property
    def FailList(self):
        return self._FailList

    @FailList.setter
    def FailList(self, FailList):
        self._FailList = FailList

    @property
    def PartSuccessList(self):
        return self._PartSuccessList

    @PartSuccessList.setter
    def PartSuccessList(self, PartSuccessList):
        self._PartSuccessList = PartSuccessList

    @property
    def ClusterToFlowIdList(self):
        return self._ClusterToFlowIdList

    @ClusterToFlowIdList.setter
    def ClusterToFlowIdList(self, ClusterToFlowIdList):
        self._ClusterToFlowIdList = ClusterToFlowIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessList = params.get("SuccessList")
        self._FailList = params.get("FailList")
        self._PartSuccessList = params.get("PartSuccessList")
        if params.get("ClusterToFlowIdList") is not None:
            self._ClusterToFlowIdList = []
            for item in params.get("ClusterToFlowIdList"):
                obj = ClusterIDToFlowID()
                obj._deserialize(item)
                self._ClusterToFlowIdList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifySLInstanceRequest(AbstractModel):
    """ModifySLInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一标识符（字符串表示）。
        :type InstanceId: str
        :param _Zone: 需要变更的区域名称。
        :type Zone: str
        :param _NodeNum: 该区域变配后的目标节点数量，所有区域节点总数应大于等于3，小于等于50。
        :type NodeNum: int
        """
        self._InstanceId = None
        self._Zone = None
        self._NodeNum = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._NodeNum = params.get("NodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySLInstanceResponse(AbstractModel):
    """ModifySLInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyUserManagerPwdRequest(AbstractModel):
    """ModifyUserManagerPwd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _PassWord: 密码
        :type PassWord: str
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserManagerPwdResponse(AbstractModel):
    """ModifyUserManagerPwd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyYarnDeployRequest(AbstractModel):
    """ModifyYarnDeploy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _NewScheduler: 切换后的调度器，可选值为fair、capacity
        :type NewScheduler: str
        :param _OldScheduler: 现在使用的调度器，可选值为fair、capacity
        :type OldScheduler: str
        """
        self._InstanceId = None
        self._NewScheduler = None
        self._OldScheduler = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewScheduler(self):
        return self._NewScheduler

    @NewScheduler.setter
    def NewScheduler(self, NewScheduler):
        self._NewScheduler = NewScheduler

    @property
    def OldScheduler(self):
        return self._OldScheduler

    @OldScheduler.setter
    def OldScheduler(self, OldScheduler):
        self._OldScheduler = OldScheduler


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewScheduler = params.get("NewScheduler")
        self._OldScheduler = params.get("OldScheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyYarnDeployResponse(AbstractModel):
    """ModifyYarnDeploy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDraft: 为false不点亮部署生效、重置
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDraft: bool
        :param _ErrorMsg: 错误信息，预留
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def IsDraft(self):
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyYarnQueueV2Request(AbstractModel):
    """ModifyYarnQueueV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群Id
        :type InstanceId: str
        :param _Scheduler: 调度器类型。可选值：

1. capacity
2. fair
        :type Scheduler: str
        :param _ConfigModifyInfoList: 资源池数据
        :type ConfigModifyInfoList: list of ConfigModifyInfoV2
        """
        self._InstanceId = None
        self._Scheduler = None
        self._ConfigModifyInfoList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ConfigModifyInfoList(self):
        return self._ConfigModifyInfoList

    @ConfigModifyInfoList.setter
    def ConfigModifyInfoList(self, ConfigModifyInfoList):
        self._ConfigModifyInfoList = ConfigModifyInfoList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Scheduler = params.get("Scheduler")
        if params.get("ConfigModifyInfoList") is not None:
            self._ConfigModifyInfoList = []
            for item in params.get("ConfigModifyInfoList"):
                obj = ConfigModifyInfoV2()
                obj._deserialize(item)
                self._ConfigModifyInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyYarnQueueV2Response(AbstractModel):
    """ModifyYarnQueueV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class MonthRepeatStrategy(AbstractModel):
    """定时伸缩每月重复任务策略

    """

    def __init__(self):
        r"""
        :param _ExecuteAtTimeOfDay: 重复任务执行的具体时刻，例如"01:02:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteAtTimeOfDay: str
        :param _DaysOfMonthRange: 每月中的天数时间段描述，长度只能为2，例如[2,10]表示每月2-10号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DaysOfMonthRange: list of int non-negative
        """
        self._ExecuteAtTimeOfDay = None
        self._DaysOfMonthRange = None

    @property
    def ExecuteAtTimeOfDay(self):
        return self._ExecuteAtTimeOfDay

    @ExecuteAtTimeOfDay.setter
    def ExecuteAtTimeOfDay(self, ExecuteAtTimeOfDay):
        self._ExecuteAtTimeOfDay = ExecuteAtTimeOfDay

    @property
    def DaysOfMonthRange(self):
        return self._DaysOfMonthRange

    @DaysOfMonthRange.setter
    def DaysOfMonthRange(self, DaysOfMonthRange):
        self._DaysOfMonthRange = DaysOfMonthRange


    def _deserialize(self, params):
        self._ExecuteAtTimeOfDay = params.get("ExecuteAtTimeOfDay")
        self._DaysOfMonthRange = params.get("DaysOfMonthRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDisk(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        r"""
        :param _DiskType: 云盘类型
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_HSSD：表示增强型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param _Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._DiskType = None
        self._Volume = None
        self._Count = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._Volume = params.get("Volume")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDiskMC(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        r"""
        :param _Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Type: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Size: 磁盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: str
        :param _Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        """
        self._Count = None
        self._Type = None
        self._Size = None
        self._Volume = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiZoneSetting(AbstractModel):
    """各个可用区的参数信息

    """

    def __init__(self):
        r"""
        :param _ZoneTag: "master"、"standby"、"third-party"
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneTag: str
        :param _VPCSettings: 无
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _Placement: 无
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _ResourceSpec: 无
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        self._ZoneTag = None
        self._VPCSettings = None
        self._Placement = None
        self._ResourceSpec = None

    @property
    def ZoneTag(self):
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec


    def _deserialize(self, params):
        self._ZoneTag = params.get("ZoneTag")
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: 描述Master节点资源
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CoreResourceSpec: 描述Core节点资源
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _TaskResourceSpec: 描述Task节点资源
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _MasterCount: Master节点数量
        :type MasterCount: int
        :param _CoreCount: Core节点数量
        :type CoreCount: int
        :param _TaskCount: Task节点数量
        :type TaskCount: int
        :param _CommonResourceSpec: 描述Common节点资源
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CommonCount: Common节点数量
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonResourceSpec = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = Resource()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = Resource()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = Resource()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = Resource()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDetailPriceResult(AbstractModel):
    """用于创建集群价格清单 节点价格详情

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型 master core task common router mysql
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _PartDetailPrice: 节点组成部分价格详情
        :type PartDetailPrice: list of PartDetailPriceItem
        """
        self._NodeType = None
        self._PartDetailPrice = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def PartDetailPrice(self):
        return self._PartDetailPrice

    @PartDetailPrice.setter
    def PartDetailPrice(self, PartDetailPrice):
        self._PartDetailPrice = PartDetailPrice


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        if params.get("PartDetailPrice") is not None:
            self._PartDetailPrice = []
            for item in params.get("PartDetailPrice"):
                obj = PartDetailPriceItem()
                obj._deserialize(item)
                self._PartDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeHardwareInfo(AbstractModel):
    """节点硬件信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _SerialNo: 序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param _OrderNo: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param _WanIp: master节点绑定外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param _Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: int
        :param _Spec: 节点规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _CpuNum: 节点核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param _MemSize: 节点内存
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _MemDesc: 节点内存描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MemDesc: str
        :param _RegionId: 节点所在region
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _ZoneId: 节点所在Zone
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param _FreeTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeTime: str
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param _NameTag: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NameTag: str
        :param _Services: 节点部署服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: str
        :param _StorageType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _CdbIp: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbIp: str
        :param _CdbPort: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbPort: int
        :param _HwDiskSize: 硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSize: int
        :param _HwDiskSizeDesc: 硬盘容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSizeDesc: str
        :param _HwMemSize: 内存容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSize: int
        :param _HwMemSizeDesc: 内存容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSizeDesc: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _EmrResourceId: 节点资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrResourceId: str
        :param _IsAutoRenew: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param _DeviceClass: 设备标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param _Mutable: 支持变配
注意：此字段可能返回 null，表示取不到有效值。
        :type Mutable: int
        :param _MCMultiDisk: 多云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type MCMultiDisk: list of MultiDiskMC
        :param _CdbNodeInfo: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        :param _Ip: 内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Destroyable: 此节点是否可销毁，1可销毁，0不可销毁
注意：此字段可能返回 null，表示取不到有效值。
        :type Destroyable: int
        :param _Tags: 节点绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoFlag: 是否是自动扩缩容节点，0为普通节点，1为自动扩缩容节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoFlag: int
        :param _HardwareResourceType: 资源类型, host/pod
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareResourceType: str
        :param _IsDynamicSpec: 是否浮动规格，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: 浮动规格值json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: str
        :param _SupportModifyPayMode: 是否支持变更计费类型 1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportModifyPayMode: int
        :param _RootStorageType: 系统盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RootStorageType: int
        :param _Zone: 可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SubnetInfo: 子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetInfo: :class:`tencentcloud.emr.v20190103.models.SubnetInfo`
        :param _Clients: 客户端
注意：此字段可能返回 null，表示取不到有效值。
        :type Clients: str
        :param _CurrentTime: 系统当前时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentTime: str
        :param _IsFederation: 是否用于联邦 ,1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFederation: int
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ServiceClient: 服务
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceClient: str
        :param _DisableApiTermination: 该实例是否开启实例保护，true为开启 false为关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableApiTermination: bool
        :param _TradeVersion: 0表示老计费，1表示新计费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        :param _ServicesStatus: 各组件状态，Zookeeper:STARTED,ResourceManager:STARTED，STARTED已启动，STOPED已停止
注意：此字段可能返回 null，表示取不到有效值。
        :type ServicesStatus: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _SharedClusterId: 共享集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type SharedClusterId: str
        :param _SharedClusterIdDesc: 共享集群id描述
注意：此字段可能返回 null，表示取不到有效值。
        :type SharedClusterIdDesc: str
        """
        self._AppId = None
        self._SerialNo = None
        self._OrderNo = None
        self._WanIp = None
        self._Flag = None
        self._Spec = None
        self._CpuNum = None
        self._MemSize = None
        self._MemDesc = None
        self._RegionId = None
        self._ZoneId = None
        self._ApplyTime = None
        self._FreeTime = None
        self._DiskSize = None
        self._NameTag = None
        self._Services = None
        self._StorageType = None
        self._RootSize = None
        self._ChargeType = None
        self._CdbIp = None
        self._CdbPort = None
        self._HwDiskSize = None
        self._HwDiskSizeDesc = None
        self._HwMemSize = None
        self._HwMemSizeDesc = None
        self._ExpireTime = None
        self._EmrResourceId = None
        self._IsAutoRenew = None
        self._DeviceClass = None
        self._Mutable = None
        self._MCMultiDisk = None
        self._CdbNodeInfo = None
        self._Ip = None
        self._Destroyable = None
        self._Tags = None
        self._AutoFlag = None
        self._HardwareResourceType = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._SupportModifyPayMode = None
        self._RootStorageType = None
        self._Zone = None
        self._SubnetInfo = None
        self._Clients = None
        self._CurrentTime = None
        self._IsFederation = None
        self._DeviceName = None
        self._ServiceClient = None
        self._DisableApiTermination = None
        self._TradeVersion = None
        self._ServicesStatus = None
        self._Remark = None
        self._SharedClusterId = None
        self._SharedClusterIdDesc = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def OrderNo(self):
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def CpuNum(self):
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemDesc(self):
        return self._MemDesc

    @MemDesc.setter
    def MemDesc(self, MemDesc):
        self._MemDesc = MemDesc

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def FreeTime(self):
        return self._FreeTime

    @FreeTime.setter
    def FreeTime(self, FreeTime):
        self._FreeTime = FreeTime

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NameTag(self):
        return self._NameTag

    @NameTag.setter
    def NameTag(self, NameTag):
        self._NameTag = NameTag

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def CdbIp(self):
        return self._CdbIp

    @CdbIp.setter
    def CdbIp(self, CdbIp):
        self._CdbIp = CdbIp

    @property
    def CdbPort(self):
        return self._CdbPort

    @CdbPort.setter
    def CdbPort(self, CdbPort):
        self._CdbPort = CdbPort

    @property
    def HwDiskSize(self):
        return self._HwDiskSize

    @HwDiskSize.setter
    def HwDiskSize(self, HwDiskSize):
        self._HwDiskSize = HwDiskSize

    @property
    def HwDiskSizeDesc(self):
        return self._HwDiskSizeDesc

    @HwDiskSizeDesc.setter
    def HwDiskSizeDesc(self, HwDiskSizeDesc):
        self._HwDiskSizeDesc = HwDiskSizeDesc

    @property
    def HwMemSize(self):
        return self._HwMemSize

    @HwMemSize.setter
    def HwMemSize(self, HwMemSize):
        self._HwMemSize = HwMemSize

    @property
    def HwMemSizeDesc(self):
        return self._HwMemSizeDesc

    @HwMemSizeDesc.setter
    def HwMemSizeDesc(self, HwMemSizeDesc):
        self._HwMemSizeDesc = HwMemSizeDesc

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EmrResourceId(self):
        return self._EmrResourceId

    @EmrResourceId.setter
    def EmrResourceId(self, EmrResourceId):
        self._EmrResourceId = EmrResourceId

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def Mutable(self):
        return self._Mutable

    @Mutable.setter
    def Mutable(self, Mutable):
        self._Mutable = Mutable

    @property
    def MCMultiDisk(self):
        return self._MCMultiDisk

    @MCMultiDisk.setter
    def MCMultiDisk(self, MCMultiDisk):
        self._MCMultiDisk = MCMultiDisk

    @property
    def CdbNodeInfo(self):
        return self._CdbNodeInfo

    @CdbNodeInfo.setter
    def CdbNodeInfo(self, CdbNodeInfo):
        self._CdbNodeInfo = CdbNodeInfo

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Destroyable(self):
        return self._Destroyable

    @Destroyable.setter
    def Destroyable(self, Destroyable):
        self._Destroyable = Destroyable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoFlag(self):
        return self._AutoFlag

    @AutoFlag.setter
    def AutoFlag(self, AutoFlag):
        self._AutoFlag = AutoFlag

    @property
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def IsDynamicSpec(self):
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

    @property
    def SupportModifyPayMode(self):
        return self._SupportModifyPayMode

    @SupportModifyPayMode.setter
    def SupportModifyPayMode(self, SupportModifyPayMode):
        self._SupportModifyPayMode = SupportModifyPayMode

    @property
    def RootStorageType(self):
        return self._RootStorageType

    @RootStorageType.setter
    def RootStorageType(self, RootStorageType):
        self._RootStorageType = RootStorageType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfo(self):
        return self._SubnetInfo

    @SubnetInfo.setter
    def SubnetInfo(self, SubnetInfo):
        self._SubnetInfo = SubnetInfo

    @property
    def Clients(self):
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def CurrentTime(self):
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def IsFederation(self):
        return self._IsFederation

    @IsFederation.setter
    def IsFederation(self, IsFederation):
        self._IsFederation = IsFederation

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ServiceClient(self):
        return self._ServiceClient

    @ServiceClient.setter
    def ServiceClient(self, ServiceClient):
        self._ServiceClient = ServiceClient

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def TradeVersion(self):
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion

    @property
    def ServicesStatus(self):
        return self._ServicesStatus

    @ServicesStatus.setter
    def ServicesStatus(self, ServicesStatus):
        self._ServicesStatus = ServicesStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SharedClusterId(self):
        return self._SharedClusterId

    @SharedClusterId.setter
    def SharedClusterId(self, SharedClusterId):
        self._SharedClusterId = SharedClusterId

    @property
    def SharedClusterIdDesc(self):
        return self._SharedClusterIdDesc

    @SharedClusterIdDesc.setter
    def SharedClusterIdDesc(self, SharedClusterIdDesc):
        self._SharedClusterIdDesc = SharedClusterIdDesc


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._SerialNo = params.get("SerialNo")
        self._OrderNo = params.get("OrderNo")
        self._WanIp = params.get("WanIp")
        self._Flag = params.get("Flag")
        self._Spec = params.get("Spec")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._MemDesc = params.get("MemDesc")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._ApplyTime = params.get("ApplyTime")
        self._FreeTime = params.get("FreeTime")
        self._DiskSize = params.get("DiskSize")
        self._NameTag = params.get("NameTag")
        self._Services = params.get("Services")
        self._StorageType = params.get("StorageType")
        self._RootSize = params.get("RootSize")
        self._ChargeType = params.get("ChargeType")
        self._CdbIp = params.get("CdbIp")
        self._CdbPort = params.get("CdbPort")
        self._HwDiskSize = params.get("HwDiskSize")
        self._HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self._HwMemSize = params.get("HwMemSize")
        self._HwMemSizeDesc = params.get("HwMemSizeDesc")
        self._ExpireTime = params.get("ExpireTime")
        self._EmrResourceId = params.get("EmrResourceId")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._DeviceClass = params.get("DeviceClass")
        self._Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self._MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self._MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self._CdbNodeInfo = CdbInfo()
            self._CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self._Ip = params.get("Ip")
        self._Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoFlag = params.get("AutoFlag")
        self._HardwareResourceType = params.get("HardwareResourceType")
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        self._DynamicPodSpec = params.get("DynamicPodSpec")
        self._SupportModifyPayMode = params.get("SupportModifyPayMode")
        self._RootStorageType = params.get("RootStorageType")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfo") is not None:
            self._SubnetInfo = SubnetInfo()
            self._SubnetInfo._deserialize(params.get("SubnetInfo"))
        self._Clients = params.get("Clients")
        self._CurrentTime = params.get("CurrentTime")
        self._IsFederation = params.get("IsFederation")
        self._DeviceName = params.get("DeviceName")
        self._ServiceClient = params.get("ServiceClient")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._TradeVersion = params.get("TradeVersion")
        self._ServicesStatus = params.get("ServicesStatus")
        self._Remark = params.get("Remark")
        self._SharedClusterId = params.get("SharedClusterId")
        self._SharedClusterIdDesc = params.get("SharedClusterIdDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeResourceSpec(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _InstanceType: 规格类型，如S2.MEDIUM8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _SystemDisk: 系统盘，系统盘个数不超过1块
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: list of DiskSpecInfo
        :param _Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _DataDisk: 云数据盘，云数据盘总个数不超过15块
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisk: list of DiskSpecInfo
        :param _LocalDataDisk: 本地数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDataDisk: list of DiskSpecInfo
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._Tags = None
        self._DataDisk = None
        self._LocalDataDisk = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataDisk(self):
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def LocalDataDisk(self):
        return self._LocalDataDisk

    @LocalDataDisk.setter
    def LocalDataDisk(self, LocalDataDisk):
        self._LocalDataDisk = LocalDataDisk


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._SystemDisk.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataDisk") is not None:
            self._DataDisk = []
            for item in params.get("DataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._DataDisk.append(obj)
        if params.get("LocalDataDisk") is not None:
            self._LocalDataDisk = []
            for item in params.get("LocalDataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._LocalDataDisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotRepeatStrategy(AbstractModel):
    """弹性扩缩容执行一次规则上下文

    """

    def __init__(self):
        r"""
        :param _ExecuteAt: 该次任务执行的具体完整时间，格式为"2020-07-13 00:00:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteAt: str
        """
        self._ExecuteAt = None

    @property
    def ExecuteAt(self):
        return self._ExecuteAt

    @ExecuteAt.setter
    def ExecuteAt(self, ExecuteAt):
        self._ExecuteAt = ExecuteAt


    def _deserialize(self, params):
        self._ExecuteAt = params.get("ExecuteAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpScope(AbstractModel):
    """操作范围

    """

    def __init__(self):
        r"""
        :param _ServiceInfoList: 操作范围，要操作的服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInfoList: list of ServiceBasicRestartInfo
        """
        self._ServiceInfoList = None

    @property
    def ServiceInfoList(self):
        return self._ServiceInfoList

    @ServiceInfoList.setter
    def ServiceInfoList(self, ServiceInfoList):
        self._ServiceInfoList = ServiceInfoList


    def _deserialize(self, params):
        if params.get("ServiceInfoList") is not None:
            self._ServiceInfoList = []
            for item in params.get("ServiceInfoList"):
                obj = ServiceBasicRestartInfo()
                obj._deserialize(item)
                self._ServiceInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutterResource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _Spec: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _SpecName: 规格名
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: CPU个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self._Spec = None
        self._SpecName = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._InstanceType = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._SpecName = params.get("SpecName")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewMetricData(AbstractModel):
    """概览数据

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _First: 第一个数据时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type First: int
        :param _Last: 最后一个数据时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Last: int
        :param _Interval: 采样点时间间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: int
        :param _DataPoints: 采样点数据
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPoints: list of str
        :param _Tags: 指标tags
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: :class:`tencentcloud.emr.v20190103.models.MetricTags`
        """
        self._Metric = None
        self._First = None
        self._Last = None
        self._Interval = None
        self._DataPoints = None
        self._Tags = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def First(self):
        return self._First

    @First.setter
    def First(self, First):
        self._First = First

    @property
    def Last(self):
        return self._Last

    @Last.setter
    def Last(self, Last):
        self._Last = Last

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def DataPoints(self):
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._First = params.get("First")
        self._Last = params.get("Last")
        self._Interval = params.get("Interval")
        self._DataPoints = params.get("DataPoints")
        if params.get("Tags") is not None:
            self._Tags = MetricTags()
            self._Tags._deserialize(params.get("Tags"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewRow(AbstractModel):
    """Hbase的TableMetric Overview返回

    """

    def __init__(self):
        r"""
        :param _Table: 表名字
        :type Table: str
        :param _ReadRequestCount: 读请求次数
        :type ReadRequestCount: float
        :param _WriteRequestCount: 写请求次数
        :type WriteRequestCount: float
        :param _MemstoreSize: 当前memstore的size
        :type MemstoreSize: float
        :param _StoreFileSize: 当前region中StroreFile的size
        :type StoreFileSize: float
        :param _Operation: regions，点击可跳转
        :type Operation: str
        """
        self._Table = None
        self._ReadRequestCount = None
        self._WriteRequestCount = None
        self._MemstoreSize = None
        self._StoreFileSize = None
        self._Operation = None

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def ReadRequestCount(self):
        return self._ReadRequestCount

    @ReadRequestCount.setter
    def ReadRequestCount(self, ReadRequestCount):
        self._ReadRequestCount = ReadRequestCount

    @property
    def WriteRequestCount(self):
        return self._WriteRequestCount

    @WriteRequestCount.setter
    def WriteRequestCount(self, WriteRequestCount):
        self._WriteRequestCount = WriteRequestCount

    @property
    def MemstoreSize(self):
        return self._MemstoreSize

    @MemstoreSize.setter
    def MemstoreSize(self, MemstoreSize):
        self._MemstoreSize = MemstoreSize

    @property
    def StoreFileSize(self):
        return self._StoreFileSize

    @StoreFileSize.setter
    def StoreFileSize(self, StoreFileSize):
        self._StoreFileSize = StoreFileSize

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._Table = params.get("Table")
        self._ReadRequestCount = params.get("ReadRequestCount")
        self._WriteRequestCount = params.get("WriteRequestCount")
        self._MemstoreSize = params.get("MemstoreSize")
        self._StoreFileSize = params.get("StoreFileSize")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartDetailPriceItem(AbstractModel):
    """用于创建集群价格清单-节点组成部分价格

    """

    def __init__(self):
        r"""
        :param _InstanceType: 类型包括：节点->node、系统盘->rootDisk、云数据盘->dataDisk、metaDB
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Price: 单价（原价）
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param _RealCost: 单价（折扣价）
注意：此字段可能返回 null，表示取不到有效值。
        :type RealCost: float
        :param _RealTotalCost: 总价（折扣价）
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: float
        :param _Policy: 折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: float
        :param _GoodsNum: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        """
        self._InstanceType = None
        self._Price = None
        self._RealCost = None
        self._RealTotalCost = None
        self._Policy = None
        self._GoodsNum = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Price = params.get("Price")
        self._RealCost = params.get("RealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Policy = params.get("Policy")
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersistentVolumeContext(AbstractModel):
    """Pod PVC存储方式描述

    """

    def __init__(self):
        r"""
        :param _DiskSize: 磁盘大小，单位为GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _DiskType: 磁盘类型。CLOUD_PREMIUM;CLOUD_SSD
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskNum = None

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
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述集群实例位置信息

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用[DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用[DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        """
        self._Zone = None
        self._ProjectId = None

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


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewParameter(AbstractModel):
    """POD自定义权限和自定义参数

    """

    def __init__(self):
        r"""
        :param _InstanceId: TKE或EKS集群ID
        :type InstanceId: str
        :param _Config: 自定义权限
如：
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: 自定义参数
如：
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._InstanceId = None
        self._Config = None
        self._Parameter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewSpec(AbstractModel):
    """扩容容器资源时的资源描述

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: 外部资源提供者的标识符，例如"cls-a1cd23fa"。
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: 外部资源提供者类型，例如"tke",当前仅支持"tke"。
        :type ResourceProviderType: str
        :param _NodeFlag: 资源的用途，即节点类型，当前仅支持"TASK"。
        :type NodeFlag: str
        :param _Cpu: CPU核数。
        :type Cpu: int
        :param _Memory: 内存大小，单位为GB。
        :type Memory: int
        :param _CpuType: Eks集群-CPU类型，当前支持"intel"和"amd"
        :type CpuType: str
        :param _PodVolumes: Pod节点数据目录挂载信息。
        :type PodVolumes: list of PodVolume
        :param _EnableDynamicSpecFlag: 是否浮动规格，默认否
<li>true：代表是</li>
<li>false：代表否</li>
        :type EnableDynamicSpecFlag: bool
        :param _DynamicPodSpec: 浮动规格
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: 代表vpc网络唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 代表vpc子网唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _PodName: pod name
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeFlag = None
        self._Cpu = None
        self._Memory = None
        self._CpuType = None
        self._PodVolumes = None
        self._EnableDynamicSpecFlag = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

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
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def EnableDynamicSpecFlag(self):
        return self._EnableDynamicSpecFlag

    @EnableDynamicSpecFlag.setter
    def EnableDynamicSpecFlag(self, EnableDynamicSpecFlag):
        self._EnableDynamicSpecFlag = EnableDynamicSpecFlag

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

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
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeFlag = params.get("NodeFlag")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._EnableDynamicSpecFlag = params.get("EnableDynamicSpecFlag")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodParameter(AbstractModel):
    """POD自定义权限和自定义参数

    """

    def __init__(self):
        r"""
        :param _ClusterId: TKE或EKS集群ID
        :type ClusterId: str
        :param _Config: 自定义权限
如：
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: 自定义参数
如：
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._ClusterId = None
        self._Config = None
        self._Parameter = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSaleSpec(AbstractModel):
    """Pod资源售卖规格

    """

    def __init__(self):
        r"""
        :param _NodeType: 可售卖的资源规格，仅为以下值:"TASK","CORE","MASTER","ROUTER"。
        :type NodeType: str
        :param _Cpu: Cpu核数。
        :type Cpu: int
        :param _Memory: 内存数量，单位为GB。
        :type Memory: int
        :param _Number: 该规格资源可申请的最大数量。
        :type Number: int
        """
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._Number = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

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
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpec(AbstractModel):
    """扩容容器资源时的资源描述

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: 外部资源提供者的标识符，例如"cls-a1cd23fa"。
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: 外部资源提供者类型，例如"tke",当前仅支持"tke"。
        :type ResourceProviderType: str
        :param _NodeType: 资源的用途，即节点类型，当前仅支持"TASK"。
        :type NodeType: str
        :param _Cpu: CPU核数。
        :type Cpu: int
        :param _Memory: 内存大小，单位为GB。
        :type Memory: int
        :param _DataVolumes: 资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用。弃用
        :type DataVolumes: list of str
        :param _CpuType: Eks集群-CPU类型，当前支持"intel"和"amd"
        :type CpuType: str
        :param _PodVolumes: Pod节点数据目录挂载信息。
        :type PodVolumes: list of PodVolume
        :param _IsDynamicSpec: 是否浮动规格，1是，0否
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: 浮动规格
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: 代表vpc网络唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 代表vpc子网唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _PodName: pod name
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._DataVolumes = None
        self._CpuType = None
        self._PodVolumes = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

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
    def DataVolumes(self):
        return self._DataVolumes

    @DataVolumes.setter
    def DataVolumes(self, DataVolumes):
        self._DataVolumes = DataVolumes

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def IsDynamicSpec(self):
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

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
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DataVolumes = params.get("DataVolumes")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpecInfo(AbstractModel):
    """Pod相关信息

    """

    def __init__(self):
        r"""
        :param _PodSpec: 使用Pod资源扩容时，指定的Pod规格以及来源等信息
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodNewSpec`
        :param _PodParameter: POD自定义权限和自定义参数
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodNewParameter`
        """
        self._PodSpec = None
        self._PodParameter = None

    @property
    def PodSpec(self):
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def PodParameter(self):
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter


    def _deserialize(self, params):
        if params.get("PodSpec") is not None:
            self._PodSpec = PodNewSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        if params.get("PodParameter") is not None:
            self._PodParameter = PodNewParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodState(AbstractModel):
    """单个pod状态

    """

    def __init__(self):
        r"""
        :param _Name: pod的名称
        :type Name: str
        :param _Uuid: pod uuid
        :type Uuid: str
        :param _State: pod的状态
        :type State: str
        :param _Reason: pod处于该状态原因
        :type Reason: str
        :param _OwnerCluster: pod所属集群
        :type OwnerCluster: str
        :param _Memory: pod内存大小
        :type Memory: int
        """
        self._Name = None
        self._Uuid = None
        self._State = None
        self._Reason = None
        self._OwnerCluster = None
        self._Memory = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

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
    def OwnerCluster(self):
        return self._OwnerCluster

    @OwnerCluster.setter
    def OwnerCluster(self, OwnerCluster):
        self._OwnerCluster = OwnerCluster

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Uuid = params.get("Uuid")
        self._State = params.get("State")
        self._Reason = params.get("Reason")
        self._OwnerCluster = params.get("OwnerCluster")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodVolume(AbstractModel):
    """Pod的存储设备描述信息。

    """

    def __init__(self):
        r"""
        :param _VolumeType: 存储类型，可为"pvc"，"hostpath"。
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeType: str
        :param _PVCVolume: 当VolumeType为"pvc"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`
        :param _HostVolume: 当VolumeType为"hostpath"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`
        """
        self._VolumeType = None
        self._PVCVolume = None
        self._HostVolume = None

    @property
    def VolumeType(self):
        return self._VolumeType

    @VolumeType.setter
    def VolumeType(self, VolumeType):
        self._VolumeType = VolumeType

    @property
    def PVCVolume(self):
        return self._PVCVolume

    @PVCVolume.setter
    def PVCVolume(self, PVCVolume):
        self._PVCVolume = PVCVolume

    @property
    def HostVolume(self):
        return self._HostVolume

    @HostVolume.setter
    def HostVolume(self, HostVolume):
        self._HostVolume = HostVolume


    def _deserialize(self, params):
        self._VolumeType = params.get("VolumeType")
        if params.get("PVCVolume") is not None:
            self._PVCVolume = PersistentVolumeContext()
            self._PVCVolume._deserialize(params.get("PVCVolume"))
        if params.get("HostVolume") is not None:
            self._HostVolume = HostVolumeContext()
            self._HostVolume._deserialize(params.get("HostVolume"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreExecuteFileSettings(AbstractModel):
    """预执行脚本配置

    """

    def __init__(self):
        r"""
        :param _Path: 脚本在COS上路径，已废弃
        :type Path: str
        :param _Args: 执行脚本参数
        :type Args: list of str
        :param _Bucket: COS的Bucket名称，已废弃
        :type Bucket: str
        :param _Region: COS的Region名称，已废弃
        :type Region: str
        :param _Domain: COS的Domain数据，已废弃
        :type Domain: str
        :param _RunOrder: 执行顺序
        :type RunOrder: int
        :param _WhenRun: resourceAfter 或 clusterAfter
        :type WhenRun: str
        :param _CosFileName: 脚本文件名，已废弃
        :type CosFileName: str
        :param _CosFileURI: 脚本的cos地址
        :type CosFileURI: str
        :param _CosSecretId: cos的SecretId
        :type CosSecretId: str
        :param _CosSecretKey: Cos的SecretKey
        :type CosSecretKey: str
        :param _AppId: cos的appid，已废弃
        :type AppId: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._Path = None
        self._Args = None
        self._Bucket = None
        self._Region = None
        self._Domain = None
        self._RunOrder = None
        self._WhenRun = None
        self._CosFileName = None
        self._CosFileURI = None
        self._CosSecretId = None
        self._CosSecretKey = None
        self._AppId = None
        self._Remark = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RunOrder(self):
        return self._RunOrder

    @RunOrder.setter
    def RunOrder(self, RunOrder):
        self._RunOrder = RunOrder

    @property
    def WhenRun(self):
        return self._WhenRun

    @WhenRun.setter
    def WhenRun(self, WhenRun):
        self._WhenRun = WhenRun

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName

    @property
    def CosFileURI(self):
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def CosSecretId(self):
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Args = params.get("Args")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._RunOrder = params.get("RunOrder")
        self._WhenRun = params.get("WhenRun")
        self._CosFileName = params.get("CosFileName")
        self._CosFileURI = params.get("CosFileURI")
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._AppId = params.get("AppId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """价格详情

    """

    def __init__(self):
        r"""
        :param _ResourceId: 节点ID
        :type ResourceId: str
        :param _Formula: 价格计算公式
        :type Formula: str
        :param _OriginalCost: 原价
        :type OriginalCost: float
        :param _DiscountCost: 折扣价
        :type DiscountCost: float
        """
        self._ResourceId = None
        self._Formula = None
        self._OriginalCost = None
        self._DiscountCost = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Formula(self):
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Formula = params.get("Formula")
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceResource(AbstractModel):
    """询价资源

    """

    def __init__(self):
        r"""
        :param _Spec: 需要的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: 核心数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _MultiDisks: 云盘列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param _DiskCnt: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCnt: int
        :param _InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        :param _LocalDiskNum: 本地盘的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._MultiDisks = None
        self._DiskCnt = None
        self._InstanceType = None
        self._Tags = None
        self._DiskNum = None
        self._LocalDiskNum = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MultiDisks(self):
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def DiskCnt(self):
        return self._DiskCnt

    @DiskCnt.setter
    def DiskCnt(self, DiskCnt):
        self._DiskCnt = DiskCnt

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum

    @property
    def LocalDiskNum(self):
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        self._DiskCnt = params.get("DiskCnt")
        self._InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DiskNum = params.get("DiskNum")
        self._LocalDiskNum = params.get("LocalDiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceResult(AbstractModel):
    """询价结果

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        """
        self._OriginalCost = None
        self._DiscountCost = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaEntity(AbstractModel):
    """获取CVM配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 已使用配额
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedQuota: int
        :param _RemainingQuota: 剩余配额
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingQuota: int
        :param _TotalQuota: 总配额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalQuota: int
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._UsedQuota = None
        self._RemainingQuota = None
        self._TotalQuota = None
        self._Zone = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesInfo(AbstractModel):
    """集群续费实例信息

    """

    def __init__(self):
        r"""
        :param _EmrResourceId: 节点资源ID
        :type EmrResourceId: str
        :param _Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点
        :type Flag: int
        :param _Ip: 内网IP
        :type Ip: str
        :param _MemDesc: 节点内存描述
        :type MemDesc: str
        :param _CpuNum: 节点核数
        :type CpuNum: int
        :param _DiskSize: 硬盘大小
        :type DiskSize: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _Spec: 节点规格
        :type Spec: str
        :param _StorageType: 磁盘类型
        :type StorageType: int
        """
        self._EmrResourceId = None
        self._Flag = None
        self._Ip = None
        self._MemDesc = None
        self._CpuNum = None
        self._DiskSize = None
        self._ExpireTime = None
        self._Spec = None
        self._StorageType = None

    @property
    def EmrResourceId(self):
        return self._EmrResourceId

    @EmrResourceId.setter
    def EmrResourceId(self, EmrResourceId):
        self._EmrResourceId = EmrResourceId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MemDesc(self):
        return self._MemDesc

    @MemDesc.setter
    def MemDesc(self, MemDesc):
        self._MemDesc = MemDesc

    @property
    def CpuNum(self):
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._EmrResourceId = params.get("EmrResourceId")
        self._Flag = params.get("Flag")
        self._Ip = params.get("Ip")
        self._MemDesc = params.get("MemDesc")
        self._CpuNum = params.get("CpuNum")
        self._DiskSize = params.get("DiskSize")
        self._ExpireTime = params.get("ExpireTime")
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepeatStrategy(AbstractModel):
    """定时伸缩任务策略

    """

    def __init__(self):
        r"""
        :param _RepeatType: 取值范围"DAY","DOW","DOM","NONE"，分别表示按天重复、按周重复、按月重复和一次执行。必须填写
        :type RepeatType: str
        :param _DayRepeat: 按天重复规则，当RepeatType为"DAY"时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type DayRepeat: :class:`tencentcloud.emr.v20190103.models.DayRepeatStrategy`
        :param _WeekRepeat: 按周重复规则，当RepeatType为"DOW"时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekRepeat: :class:`tencentcloud.emr.v20190103.models.WeekRepeatStrategy`
        :param _MonthRepeat: 按月重复规则，当RepeatType为"DOM"时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthRepeat: :class:`tencentcloud.emr.v20190103.models.MonthRepeatStrategy`
        :param _NotRepeat: 一次执行规则，当RepeatType为"NONE"时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type NotRepeat: :class:`tencentcloud.emr.v20190103.models.NotRepeatStrategy`
        :param _Expire: 规则过期时间，超过该时间后，规则将自动置为暂停状态，形式为"2020-07-23 00:00:00"。必须填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Expire: str
        """
        self._RepeatType = None
        self._DayRepeat = None
        self._WeekRepeat = None
        self._MonthRepeat = None
        self._NotRepeat = None
        self._Expire = None

    @property
    def RepeatType(self):
        return self._RepeatType

    @RepeatType.setter
    def RepeatType(self, RepeatType):
        self._RepeatType = RepeatType

    @property
    def DayRepeat(self):
        return self._DayRepeat

    @DayRepeat.setter
    def DayRepeat(self, DayRepeat):
        self._DayRepeat = DayRepeat

    @property
    def WeekRepeat(self):
        return self._WeekRepeat

    @WeekRepeat.setter
    def WeekRepeat(self, WeekRepeat):
        self._WeekRepeat = WeekRepeat

    @property
    def MonthRepeat(self):
        return self._MonthRepeat

    @MonthRepeat.setter
    def MonthRepeat(self, MonthRepeat):
        self._MonthRepeat = MonthRepeat

    @property
    def NotRepeat(self):
        return self._NotRepeat

    @NotRepeat.setter
    def NotRepeat(self, NotRepeat):
        self._NotRepeat = NotRepeat

    @property
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._RepeatType = params.get("RepeatType")
        if params.get("DayRepeat") is not None:
            self._DayRepeat = DayRepeatStrategy()
            self._DayRepeat._deserialize(params.get("DayRepeat"))
        if params.get("WeekRepeat") is not None:
            self._WeekRepeat = WeekRepeatStrategy()
            self._WeekRepeat._deserialize(params.get("WeekRepeat"))
        if params.get("MonthRepeat") is not None:
            self._MonthRepeat = MonthRepeatStrategy()
            self._MonthRepeat._deserialize(params.get("MonthRepeat"))
        if params.get("NotRepeat") is not None:
            self._NotRepeat = NotRepeatStrategy()
            self._NotRepeat._deserialize(params.get("NotRepeat"))
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetYarnConfigRequest(AbstractModel):
    """ResetYarnConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _Key: 要重置的配置别名，可选值：

- capacityLabel：重置标签管理的配置
- fair：重置公平调度的配置
- capacity：重置容量调度的配置
        :type Key: str
        """
        self._InstanceId = None
        self._Key = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetYarnConfigResponse(AbstractModel):
    """ResetYarnConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class Resource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _Spec: 节点规格描述，如CVM.SA2。
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _StorageType: 存储类型
取值范围：
<li>4：表示云SSD。</li>
<li>5：表示高效云盘。</li>
<li>6：表示增强型SSD云硬盘。</li>
<li>11：表示吞吐型云硬盘。</li>
<li>12：表示极速型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 磁盘类型
取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _MemSize: 内存容量,单位为M
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 数据盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _RootSize: 系统盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MultiDisks: 云盘列表，当数据盘为一块云盘时，直接使用DiskType和DiskSize参数，超出部分使用MultiDisks
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param _Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceType: 规格类型，如S2.MEDIUM8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _LocalDiskNum: 本地盘数量，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        :param _DiskNum: 本地盘数量，如2
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._RootSize = None
        self._MultiDisks = None
        self._Tags = None
        self._InstanceType = None
        self._LocalDiskNum = None
        self._DiskNum = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MultiDisks(self):
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LocalDiskNum(self):
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum

    @property
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._LocalDiskNum = params.get("LocalDiskNum")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceDetail(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _Spec: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _SpecName: 规格名
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: CPU个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self._Spec = None
        self._SpecName = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._InstanceType = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._SpecName = params.get("SpecName")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartPolicy(AbstractModel):
    """组件重启策略

    """

    def __init__(self):
        r"""
        :param _Name: 重启策略名。
        :type Name: str
        :param _DisplayName: 策略展示名称。
        :type DisplayName: str
        :param _Describe: 策略描述。
        :type Describe: str
        :param _BatchSizeRange: 批量重启节点数可选范围。
        :type BatchSizeRange: list of int
        :param _IsDefault: 是否是默认策略。
        :type IsDefault: str
        """
        self._Name = None
        self._DisplayName = None
        self._Describe = None
        self._BatchSizeRange = None
        self._IsDefault = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def BatchSizeRange(self):
        return self._BatchSizeRange

    @BatchSizeRange.setter
    def BatchSizeRange(self, BatchSizeRange):
        self._BatchSizeRange = BatchSizeRange

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DisplayName = params.get("DisplayName")
        self._Describe = params.get("Describe")
        self._BatchSizeRange = params.get("BatchSizeRange")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowRequest(AbstractModel):
    """RunJobFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 作业名称。
        :type Name: str
        :param _CreateCluster: 是否新创建集群。
true，新创建集群，则使用Instance中的参数进行集群创建。
false，使用已有集群，则通过InstanceId传入。
        :type CreateCluster: bool
        :param _Steps: 作业流程执行步骤。
        :type Steps: list of Step
        :param _InstancePolicy: 作业流程正常完成时，集群的处理方式，可选择:
Terminate 销毁集群。
Reserve 保留集群。
        :type InstancePolicy: str
        :param _ProductVersion: 只有CreateCluster为true时生效，目前只支持EMR版本，例如EMR-2.2.0，不支持ClickHouse和Druid版本。
        :type ProductVersion: str
        :param _SecurityClusterFlag: 只在CreateCluster为true时生效。
true 表示安装kerberos，false表示不安装kerberos。
        :type SecurityClusterFlag: bool
        :param _Software: 只在CreateCluster为true时生效。
新建集群时，要安装的软件列表。
        :type Software: list of str
        :param _BootstrapActions: 引导脚本。
        :type BootstrapActions: list of BootstrapAction
        :param _Configurations: 指定配置创建集群。
        :type Configurations: list of Configuration
        :param _LogUri: 作业日志保存地址。
        :type LogUri: str
        :param _InstanceId: 只在CreateCluster为false时生效。
        :type InstanceId: str
        :param _ApplicationRole: 自定义应用角色，大数据应用访问外部服务时使用的角色，默认为"EME_QCSRole"。
        :type ApplicationRole: str
        :param _ClientToken: 重入标签，用来可重入检查，防止在一段时间内，创建相同的流程作业。
        :type ClientToken: str
        :param _Instance: 只在CreateCluster为true时生效，使用该配置创建集群。
        :type Instance: :class:`tencentcloud.emr.v20190103.models.ClusterSetting`
        """
        self._Name = None
        self._CreateCluster = None
        self._Steps = None
        self._InstancePolicy = None
        self._ProductVersion = None
        self._SecurityClusterFlag = None
        self._Software = None
        self._BootstrapActions = None
        self._Configurations = None
        self._LogUri = None
        self._InstanceId = None
        self._ApplicationRole = None
        self._ClientToken = None
        self._Instance = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateCluster(self):
        return self._CreateCluster

    @CreateCluster.setter
    def CreateCluster(self, CreateCluster):
        self._CreateCluster = CreateCluster

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def InstancePolicy(self):
        return self._InstancePolicy

    @InstancePolicy.setter
    def InstancePolicy(self, InstancePolicy):
        self._InstancePolicy = InstancePolicy

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def SecurityClusterFlag(self):
        return self._SecurityClusterFlag

    @SecurityClusterFlag.setter
    def SecurityClusterFlag(self, SecurityClusterFlag):
        self._SecurityClusterFlag = SecurityClusterFlag

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def BootstrapActions(self):
        return self._BootstrapActions

    @BootstrapActions.setter
    def BootstrapActions(self, BootstrapActions):
        self._BootstrapActions = BootstrapActions

    @property
    def Configurations(self):
        return self._Configurations

    @Configurations.setter
    def Configurations(self, Configurations):
        self._Configurations = Configurations

    @property
    def LogUri(self):
        return self._LogUri

    @LogUri.setter
    def LogUri(self, LogUri):
        self._LogUri = LogUri

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreateCluster = params.get("CreateCluster")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = Step()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._InstancePolicy = params.get("InstancePolicy")
        self._ProductVersion = params.get("ProductVersion")
        self._SecurityClusterFlag = params.get("SecurityClusterFlag")
        self._Software = params.get("Software")
        if params.get("BootstrapActions") is not None:
            self._BootstrapActions = []
            for item in params.get("BootstrapActions"):
                obj = BootstrapAction()
                obj._deserialize(item)
                self._BootstrapActions.append(obj)
        if params.get("Configurations") is not None:
            self._Configurations = []
            for item in params.get("Configurations"):
                obj = Configuration()
                obj._deserialize(item)
                self._Configurations.append(obj)
        self._LogUri = params.get("LogUri")
        self._InstanceId = params.get("InstanceId")
        self._ApplicationRole = params.get("ApplicationRole")
        self._ClientToken = params.get("ClientToken")
        if params.get("Instance") is not None:
            self._Instance = ClusterSetting()
            self._Instance._deserialize(params.get("Instance"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowResponse(AbstractModel):
    """RunJobFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobFlowId: 作业流程ID。
        :type JobFlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobFlowId = None
        self._RequestId = None

    @property
    def JobFlowId(self):
        return self._JobFlowId

    @JobFlowId.setter
    def JobFlowId(self, JobFlowId):
        self._JobFlowId = JobFlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobFlowId = params.get("JobFlowId")
        self._RequestId = params.get("RequestId")


class SLInstanceInfo(AbstractModel):
    """EMR Lite HBase 实例信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群实例字符串ID
        :type ClusterId: str
        :param _Id: 集群实例数字ID
        :type Id: int
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _ClusterName: 实例名称
        :type ClusterName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _ZoneId: 主可用区ID
        :type ZoneId: int
        :param _Zone: 主可用区
        :type Zone: str
        :param _AppId: 用户APPID
        :type AppId: int
        :param _VpcId: 主可用区私有网络ID
        :type VpcId: int
        :param _SubnetId: 主可用区子网ID
        :type SubnetId: int
        :param _Status: 状态码
        :type Status: int
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _PayMode: 集群计费类型。0表示按量计费，1表示包年包月
        :type PayMode: int
        :param _ZoneSettings: 多可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneSettings: list of ZoneSetting
        :param _Tags: 实例标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ClusterId = None
        self._Id = None
        self._StatusDesc = None
        self._ClusterName = None
        self._RegionId = None
        self._ZoneId = None
        self._Zone = None
        self._AppId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AddTime = None
        self._PayMode = None
        self._ZoneSettings = None
        self._Tags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ZoneSettings(self):
        return self._ZoneSettings

    @ZoneSettings.setter
    def ZoneSettings(self, ZoneSettings):
        self._ZoneSettings = ZoneSettings

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Id = params.get("Id")
        self._StatusDesc = params.get("StatusDesc")
        self._ClusterName = params.get("ClusterName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._PayMode = params.get("PayMode")
        if params.get("ZoneSettings") is not None:
            self._ZoneSettings = []
            for item in params.get("ZoneSettings"):
                obj = ZoneSetting()
                obj._deserialize(item)
                self._ZoneSettings.append(obj)
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
        


class ScaleOutClusterRequest(AbstractModel):
    """ScaleOutCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点计费模式。取值范围：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：按小时后付费。</li>
<li>SPOTPAID：竞价付费（仅支持TASK节点）。</li>
        :type InstanceChargeType: str
        :param _InstanceId: 集群实例ID。
        :type InstanceId: str
        :param _ScaleOutNodeConfig: 扩容节点类型以及数量
        :type ScaleOutNodeConfig: :class:`tencentcloud.emr.v20190103.models.ScaleOutNodeConfig`
        :param _ClientToken: 唯一随机标识，时效5分钟，需要调用者指定 防止客户端重新创建资源，例如 a9a90aa6-****-****-****-fae36063280
        :type ClientToken: str
        :param _InstanceChargePrepaid: 即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _ScriptBootstrapActionConfig: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _SoftDeployInfo: 扩容部署服务，新增节点将默认继承当前节点类型中所部署服务，部署服务含默认可选服务，该参数仅支持可选服务填写，如：存量task节点已部署HDFS、YARN、impala；使用api扩容task节不部署impala时，部署服务仅填写HDFS、YARN。[组件名对应的映射关系表](https://cloud.tencent.com/document/product/589/98760)。
        :type SoftDeployInfo: list of int
        :param _ServiceNodeInfo: 部署进程，默认部署扩容服务的全部进程，支持修改部署进程，如：当前task节点部署服务为：HDFS、YARN、impala，默认部署服务为：DataNode,NodeManager,ImpalaServer，若用户需修改部署进程信息，部署进程：	DataNode,NodeManager,ImpalaServerCoordinator或DataNode,NodeManager,ImpalaServerExecutor。[进程名对应的映射关系表](https://cloud.tencent.com/document/product/589/98760)。
        :type ServiceNodeInfo: list of int
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/product/213/17810)的返回值中的DisasterRecoverGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: 扩容节点绑定标签列表。
        :type Tags: list of Tag
        :param _HardwareSourceType: 扩容所选资源类型，可选范围为"host","pod"，host为普通的CVM资源，Pod为TKE集群或EKS集群提供的资源
        :type HardwareSourceType: str
        :param _PodSpecInfo: Pod相关资源信息
        :type PodSpecInfo: :class:`tencentcloud.emr.v20190103.models.PodSpecInfo`
        :param _ClickHouseClusterName: 使用clickhouse集群扩容时，选择的机器分组名称
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: 使用clickhouse集群扩容时，选择的机器分组类型。new为新增，old为选择旧分组
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: 扩容指定 Yarn Node Label
        :type YarnNodeLabel: str
        :param _EnableStartServiceFlag: 扩容后是否启动服务，默认取值否
<li>true：是</li>
<li>false：否</li>
        :type EnableStartServiceFlag: bool
        :param _ResourceSpec: 规格设置
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用[DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _SubnetId: 子网，默认是集群创建时的子网
        :type SubnetId: str
        :param _ScaleOutServiceConfGroupsInfo: 扩容指定配置组
        :type ScaleOutServiceConfGroupsInfo: list of ScaleOutServiceConfGroupsInfo
        """
        self._InstanceChargeType = None
        self._InstanceId = None
        self._ScaleOutNodeConfig = None
        self._ClientToken = None
        self._InstanceChargePrepaid = None
        self._ScriptBootstrapActionConfig = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareSourceType = None
        self._PodSpecInfo = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._EnableStartServiceFlag = None
        self._ResourceSpec = None
        self._Zone = None
        self._SubnetId = None
        self._ScaleOutServiceConfGroupsInfo = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ScaleOutNodeConfig(self):
        return self._ScaleOutNodeConfig

    @ScaleOutNodeConfig.setter
    def ScaleOutNodeConfig(self, ScaleOutNodeConfig):
        self._ScaleOutNodeConfig = ScaleOutNodeConfig

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def ScriptBootstrapActionConfig(self):
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def SoftDeployInfo(self):
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareSourceType(self):
        return self._HardwareSourceType

    @HardwareSourceType.setter
    def HardwareSourceType(self, HardwareSourceType):
        self._HardwareSourceType = HardwareSourceType

    @property
    def PodSpecInfo(self):
        return self._PodSpecInfo

    @PodSpecInfo.setter
    def PodSpecInfo(self, PodSpecInfo):
        self._PodSpecInfo = PodSpecInfo

    @property
    def ClickHouseClusterName(self):
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def EnableStartServiceFlag(self):
        return self._EnableStartServiceFlag

    @EnableStartServiceFlag.setter
    def EnableStartServiceFlag(self, EnableStartServiceFlag):
        self._EnableStartServiceFlag = EnableStartServiceFlag

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ScaleOutServiceConfGroupsInfo(self):
        return self._ScaleOutServiceConfGroupsInfo

    @ScaleOutServiceConfGroupsInfo.setter
    def ScaleOutServiceConfGroupsInfo(self, ScaleOutServiceConfGroupsInfo):
        self._ScaleOutServiceConfGroupsInfo = ScaleOutServiceConfGroupsInfo


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceId = params.get("InstanceId")
        if params.get("ScaleOutNodeConfig") is not None:
            self._ScaleOutNodeConfig = ScaleOutNodeConfig()
            self._ScaleOutNodeConfig._deserialize(params.get("ScaleOutNodeConfig"))
        self._ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareSourceType = params.get("HardwareSourceType")
        if params.get("PodSpecInfo") is not None:
            self._PodSpecInfo = PodSpecInfo()
            self._PodSpecInfo._deserialize(params.get("PodSpecInfo"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        self._EnableStartServiceFlag = params.get("EnableStartServiceFlag")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NodeResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        if params.get("ScaleOutServiceConfGroupsInfo") is not None:
            self._ScaleOutServiceConfGroupsInfo = []
            for item in params.get("ScaleOutServiceConfGroupsInfo"):
                obj = ScaleOutServiceConfGroupsInfo()
                obj._deserialize(item)
                self._ScaleOutServiceConfGroupsInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterResponse(AbstractModel):
    """ScaleOutCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param _FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _TraceId: 查询流程状态，流程额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._ClientToken = None
        self._FlowId = None
        self._TraceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _ClientToken: 唯一随机标识，时效5分钟，需要调用者指定 防止客户端重新创建资源，例如 a9a90aa6-****-****-****-fae36063280
        :type ClientToken: str
        :param _PreExecutedFileSettings: 引导操作脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param _CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param _UnNecessaryNodeList: 扩容时不需要安装的进程。
        :type UnNecessaryNodeList: list of int non-negative
        :param _RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        :param _SoftDeployInfo: 部署的服务。
<li>SoftDeployInfo和ServiceNodeInfo是同组参数，和UnNecessaryNodeList参数互斥。</li>
<li>建议使用SoftDeployInfo和ServiceNodeInfo组合。</li>
        :type SoftDeployInfo: list of int non-negative
        :param _ServiceNodeInfo: 启动的进程。
        :type ServiceNodeInfo: list of int non-negative
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: 扩容节点绑定标签列表。
        :type Tags: list of Tag
        :param _HardwareResourceType: 扩容所选资源类型，可选范围为"host","pod"，host为普通的CVM资源，Pod为TKE集群或EKS集群提供的资源
        :type HardwareResourceType: str
        :param _PodSpec: 使用Pod资源扩容时，指定的Pod规格以及来源等信息
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`
        :param _ClickHouseClusterName: 使用clickhouse集群扩容时，选择的机器分组名称
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: 使用clickhouse集群扩容时，选择的机器分组类型。new为新增，old为选择旧分组
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: 规则扩容指定 yarn node label
        :type YarnNodeLabel: str
        :param _PodParameter: POD自定义权限和自定义参数
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodParameter`
        :param _MasterCount: 扩容的Master节点的数量。
使用clickhouse集群扩容时，该参数不生效。
使用kafka集群扩容时，该参数不生效。
当HardwareResourceType=POD时，该参数不生效。
        :type MasterCount: int
        :param _StartServiceAfterScaleOut: 扩容后是否启动服务，true：启动，false：不启动
        :type StartServiceAfterScaleOut: str
        :param _ZoneId: 可用区，默认是集群的主可用区
        :type ZoneId: int
        :param _SubnetId: 子网，默认是集群创建时的子网
        :type SubnetId: str
        :param _ScaleOutServiceConfAssign: 预设配置组
        :type ScaleOutServiceConfAssign: str
        :param _AutoRenew: 0表示关闭自动续费，1表示开启自动续费
        :type AutoRenew: int
        :param _ResourceBaseType: 类型为ComputeResource和EMR以及默认，默认为EMR,类型为EMR时,InstanceId生效,类型为ComputeResource时,使用ComputeResourceId标识
        :type ResourceBaseType: str
        :param _ComputeResourceId: 计算资源id
        :type ComputeResourceId: str
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._InstanceId = None
        self._PayMode = None
        self._ClientToken = None
        self._PreExecutedFileSettings = None
        self._TaskCount = None
        self._CoreCount = None
        self._UnNecessaryNodeList = None
        self._RouterCount = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareResourceType = None
        self._PodSpec = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._PodParameter = None
        self._MasterCount = None
        self._StartServiceAfterScaleOut = None
        self._ZoneId = None
        self._SubnetId = None
        self._ScaleOutServiceConfAssign = None
        self._AutoRenew = None
        self._ResourceBaseType = None
        self._ComputeResourceId = None

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def PreExecutedFileSettings(self):
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def UnNecessaryNodeList(self):
        return self._UnNecessaryNodeList

    @UnNecessaryNodeList.setter
    def UnNecessaryNodeList(self, UnNecessaryNodeList):
        self._UnNecessaryNodeList = UnNecessaryNodeList

    @property
    def RouterCount(self):
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def SoftDeployInfo(self):
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def PodSpec(self):
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def ClickHouseClusterName(self):
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def PodParameter(self):
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def StartServiceAfterScaleOut(self):
        return self._StartServiceAfterScaleOut

    @StartServiceAfterScaleOut.setter
    def StartServiceAfterScaleOut(self, StartServiceAfterScaleOut):
        self._StartServiceAfterScaleOut = StartServiceAfterScaleOut

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ScaleOutServiceConfAssign(self):
        return self._ScaleOutServiceConfAssign

    @ScaleOutServiceConfAssign.setter
    def ScaleOutServiceConfAssign(self, ScaleOutServiceConfAssign):
        self._ScaleOutServiceConfAssign = ScaleOutServiceConfAssign

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ResourceBaseType(self):
        return self._ResourceBaseType

    @ResourceBaseType.setter
    def ResourceBaseType(self, ResourceBaseType):
        self._ResourceBaseType = ResourceBaseType

    @property
    def ComputeResourceId(self):
        return self._ComputeResourceId

    @ComputeResourceId.setter
    def ComputeResourceId(self, ComputeResourceId):
        self._ComputeResourceId = ComputeResourceId


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._InstanceId = params.get("InstanceId")
        self._PayMode = params.get("PayMode")
        self._ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._TaskCount = params.get("TaskCount")
        self._CoreCount = params.get("CoreCount")
        self._UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self._RouterCount = params.get("RouterCount")
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("PodSpec") is not None:
            self._PodSpec = PodSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        if params.get("PodParameter") is not None:
            self._PodParameter = PodParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        self._MasterCount = params.get("MasterCount")
        self._StartServiceAfterScaleOut = params.get("StartServiceAfterScaleOut")
        self._ZoneId = params.get("ZoneId")
        self._SubnetId = params.get("SubnetId")
        self._ScaleOutServiceConfAssign = params.get("ScaleOutServiceConfAssign")
        self._AutoRenew = params.get("AutoRenew")
        self._ResourceBaseType = params.get("ResourceBaseType")
        self._ComputeResourceId = params.get("ComputeResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _DealNames: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param _FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _BillId: 大订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillId: str
        :param _TraceId: 扩容TraceId
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealNames = None
        self._ClientToken = None
        self._FlowId = None
        self._BillId = None
        self._TraceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealNames = params.get("DealNames")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._BillId = params.get("BillId")
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class ScaleOutNodeConfig(AbstractModel):
    """扩容节点类型以及数量

    """

    def __init__(self):
        r"""
        :param _NodeFlag: 扩容节点类型取值范围：
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _NodeCount: 扩容节点数量
        :type NodeCount: int
        """
        self._NodeFlag = None
        self._NodeCount = None

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount


    def _deserialize(self, params):
        self._NodeFlag = params.get("NodeFlag")
        self._NodeCount = params.get("NodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutServiceConfGroupsInfo(AbstractModel):
    """扩容指定配置组

    """

    def __init__(self):
        r"""
        :param _ServiceComponentName: 组件版本名称 如 HDFS-2.8.5
        :type ServiceComponentName: str
        :param _ConfGroupName: 配置组名 如hdfs-core-defaultGroup    ConfGroupName参数传入 代表配置组维度 
                                                             ConfGroupName参数不传 默认 代表集群维度
        :type ConfGroupName: str
        """
        self._ServiceComponentName = None
        self._ConfGroupName = None

    @property
    def ServiceComponentName(self):
        return self._ServiceComponentName

    @ServiceComponentName.setter
    def ServiceComponentName(self, ServiceComponentName):
        self._ServiceComponentName = ServiceComponentName

    @property
    def ConfGroupName(self):
        return self._ConfGroupName

    @ConfGroupName.setter
    def ConfGroupName(self, ConfGroupName):
        self._ConfGroupName = ConfGroupName


    def _deserialize(self, params):
        self._ServiceComponentName = params.get("ServiceComponentName")
        self._ConfGroupName = params.get("ConfGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneSoftwareConfig(AbstractModel):
    """集群应用场景以及支持部署组件信息

    """

    def __init__(self):
        r"""
        :param _Software: 部署的组件列表。不同的EMR产品版本ProductVersion 对应不同可选组件列表，不同产品版本可选组件列表查询：[组件版本](https://cloud.tencent.com/document/product/589/20279) ；
填写实例值：hive、flink。
        :type Software: list of str
        :param _SceneName: 默认Hadoop-Default,[场景查询](https://cloud.tencent.com/document/product/589/14624)场景化取值范围：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
Hadoop-Default
        :type SceneName: str
        """
        self._Software = None
        self._SceneName = None

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName


    def _deserialize(self, params):
        self._Software = params.get("Software")
        self._SceneName = params.get("SceneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulerTaskDetail(AbstractModel):
    """调度任务详情

    """

    def __init__(self):
        r"""
        :param _Step: 步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: str
        :param _Progress: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: str
        :param _FailReason: 失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _JobId: 用来获取详情的id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: int
        """
        self._Step = None
        self._Progress = None
        self._FailReason = None
        self._JobId = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._Progress = params.get("Progress")
        self._FailReason = params.get("FailReason")
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulerTaskInfo(AbstractModel):
    """yarn资源调度历史

    """

    def __init__(self):
        r"""
        :param _SchedulerName: 调度器类型
        :type SchedulerName: str
        :param _OperatorName: 操作类型
        :type OperatorName: str
        :param _CreateTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _Details: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of SchedulerTaskDetail
        """
        self._SchedulerName = None
        self._OperatorName = None
        self._CreateTime = None
        self._EndTime = None
        self._State = None
        self._Details = None

    @property
    def SchedulerName(self):
        return self._SchedulerName

    @SchedulerName.setter
    def SchedulerName(self, SchedulerName):
        self._SchedulerName = SchedulerName

    @property
    def OperatorName(self):
        return self._OperatorName

    @OperatorName.setter
    def OperatorName(self, OperatorName):
        self._OperatorName = OperatorName

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
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._SchedulerName = params.get("SchedulerName")
        self._OperatorName = params.get("OperatorName")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = SchedulerTaskDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptBootstrapActionConfig(AbstractModel):
    """添加引导操作

    """

    def __init__(self):
        r"""
        :param _CosFileURI: 脚本的cos地址，参照格式：https://beijing-111111.cos.ap-beijing.myqcloud.com/data/test.sh查询cos存储桶列表：[存储桶列表](https://console.cloud.tencent.com/cos/bucket)
        :type CosFileURI: str
        :param _ExecutionMoment: 引导脚步执行时机范围
<li>resourceAfter：节点初始化后</li>
<li>clusterAfter：集群启动后</li>
<li>clusterBefore：集群启动前</li>
        :type ExecutionMoment: str
        :param _Args: 执行脚本参数，参数格式请遵循标准Shell规范
        :type Args: list of str
        :param _CosFileName: 脚本文件名
        :type CosFileName: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._CosFileURI = None
        self._ExecutionMoment = None
        self._Args = None
        self._CosFileName = None
        self._Remark = None

    @property
    def CosFileURI(self):
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def ExecutionMoment(self):
        return self._ExecutionMoment

    @ExecutionMoment.setter
    def ExecutionMoment(self, ExecutionMoment):
        self._ExecutionMoment = ExecutionMoment

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._CosFileURI = params.get("CosFileURI")
        self._ExecutionMoment = params.get("ExecutionMoment")
        self._Args = params.get("Args")
        self._CosFileName = params.get("CosFileName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchItem(AbstractModel):
    """搜索字段

    """

    def __init__(self):
        r"""
        :param _SearchType: 支持搜索的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchType: str
        :param _SearchValue: 支持搜索的值
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchValue: str
        """
        self._SearchType = None
        self._SearchValue = None

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._SearchType = params.get("SearchType")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceBasicRestartInfo(AbstractModel):
    """操作的服务范围

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名，必填，如HDFS
        :type ServiceName: str
        :param _ComponentInfoList: 如果没传，则表示所有进程
        :type ComponentInfoList: list of ComponentBasicRestartInfo
        """
        self._ServiceName = None
        self._ComponentInfoList = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ComponentInfoList(self):
        return self._ComponentInfoList

    @ComponentInfoList.setter
    def ComponentInfoList(self, ComponentInfoList):
        self._ComponentInfoList = ComponentInfoList


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        if params.get("ComponentInfoList") is not None:
            self._ComponentInfoList = []
            for item in params.get("ComponentInfoList"):
                obj = ComponentBasicRestartInfo()
                obj._deserialize(item)
                self._ComponentInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceNodeDetailInfo(AbstractModel):
    """服务进程信息

    """

    def __init__(self):
        r"""
        :param _Ip: 进程所在节点IP
        :type Ip: str
        :param _NodeType: 进程类型
        :type NodeType: int
        :param _NodeName: 进程名称
        :type NodeName: str
        :param _ServiceStatus: 服务组件状态
        :type ServiceStatus: int
        :param _MonitorStatus: 进程监控状态
        :type MonitorStatus: int
        :param _Status: 服务组件状态
        :type Status: int
        :param _PortsInfo: 进程端口信息
        :type PortsInfo: str
        :param _LastRestartTime: 最近重启时间
        :type LastRestartTime: str
        :param _Flag: 节点类型
        :type Flag: int
        :param _ConfGroupId: 配置组ID
        :type ConfGroupId: int
        :param _ConfGroupName: 配置组名称
        :type ConfGroupName: str
        :param _ConfStatus: 节点是否需要重启
        :type ConfStatus: int
        :param _ServiceDetectionInfo: 进程探测信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDetectionInfo: list of ServiceProcessFunctionInfo
        :param _NodeFlagFilter: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeFlagFilter: str
        :param _HealthStatus: 进程健康状态
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: :class:`tencentcloud.emr.v20190103.models.HealthStatus`
        :param _IsSupportRoleMonitor: 角色是否支持监控
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportRoleMonitor: bool
        :param _StopPolicies: 暂停策略
注意：此字段可能返回 null，表示取不到有效值。
        :type StopPolicies: list of RestartPolicy
        :param _HAState: 测试环境api强校验，现网没有，emrcc接口返回有。不加会报错
注意：此字段可能返回 null，表示取不到有效值。
        :type HAState: str
        :param _NameService: NameService名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NameService: str
        :param _IsFederation: 是否支持联邦
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFederation: bool
        :param _DataNodeMaintenanceState: datanode是否是维护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DataNodeMaintenanceState: int
        """
        self._Ip = None
        self._NodeType = None
        self._NodeName = None
        self._ServiceStatus = None
        self._MonitorStatus = None
        self._Status = None
        self._PortsInfo = None
        self._LastRestartTime = None
        self._Flag = None
        self._ConfGroupId = None
        self._ConfGroupName = None
        self._ConfStatus = None
        self._ServiceDetectionInfo = None
        self._NodeFlagFilter = None
        self._HealthStatus = None
        self._IsSupportRoleMonitor = None
        self._StopPolicies = None
        self._HAState = None
        self._NameService = None
        self._IsFederation = None
        self._DataNodeMaintenanceState = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ServiceStatus(self):
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PortsInfo(self):
        return self._PortsInfo

    @PortsInfo.setter
    def PortsInfo(self, PortsInfo):
        self._PortsInfo = PortsInfo

    @property
    def LastRestartTime(self):
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ConfGroupId(self):
        return self._ConfGroupId

    @ConfGroupId.setter
    def ConfGroupId(self, ConfGroupId):
        self._ConfGroupId = ConfGroupId

    @property
    def ConfGroupName(self):
        return self._ConfGroupName

    @ConfGroupName.setter
    def ConfGroupName(self, ConfGroupName):
        self._ConfGroupName = ConfGroupName

    @property
    def ConfStatus(self):
        return self._ConfStatus

    @ConfStatus.setter
    def ConfStatus(self, ConfStatus):
        self._ConfStatus = ConfStatus

    @property
    def ServiceDetectionInfo(self):
        return self._ServiceDetectionInfo

    @ServiceDetectionInfo.setter
    def ServiceDetectionInfo(self, ServiceDetectionInfo):
        self._ServiceDetectionInfo = ServiceDetectionInfo

    @property
    def NodeFlagFilter(self):
        return self._NodeFlagFilter

    @NodeFlagFilter.setter
    def NodeFlagFilter(self, NodeFlagFilter):
        self._NodeFlagFilter = NodeFlagFilter

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def IsSupportRoleMonitor(self):
        return self._IsSupportRoleMonitor

    @IsSupportRoleMonitor.setter
    def IsSupportRoleMonitor(self, IsSupportRoleMonitor):
        self._IsSupportRoleMonitor = IsSupportRoleMonitor

    @property
    def StopPolicies(self):
        return self._StopPolicies

    @StopPolicies.setter
    def StopPolicies(self, StopPolicies):
        self._StopPolicies = StopPolicies

    @property
    def HAState(self):
        return self._HAState

    @HAState.setter
    def HAState(self, HAState):
        self._HAState = HAState

    @property
    def NameService(self):
        return self._NameService

    @NameService.setter
    def NameService(self, NameService):
        self._NameService = NameService

    @property
    def IsFederation(self):
        return self._IsFederation

    @IsFederation.setter
    def IsFederation(self, IsFederation):
        self._IsFederation = IsFederation

    @property
    def DataNodeMaintenanceState(self):
        return self._DataNodeMaintenanceState

    @DataNodeMaintenanceState.setter
    def DataNodeMaintenanceState(self, DataNodeMaintenanceState):
        self._DataNodeMaintenanceState = DataNodeMaintenanceState


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._NodeType = params.get("NodeType")
        self._NodeName = params.get("NodeName")
        self._ServiceStatus = params.get("ServiceStatus")
        self._MonitorStatus = params.get("MonitorStatus")
        self._Status = params.get("Status")
        self._PortsInfo = params.get("PortsInfo")
        self._LastRestartTime = params.get("LastRestartTime")
        self._Flag = params.get("Flag")
        self._ConfGroupId = params.get("ConfGroupId")
        self._ConfGroupName = params.get("ConfGroupName")
        self._ConfStatus = params.get("ConfStatus")
        if params.get("ServiceDetectionInfo") is not None:
            self._ServiceDetectionInfo = []
            for item in params.get("ServiceDetectionInfo"):
                obj = ServiceProcessFunctionInfo()
                obj._deserialize(item)
                self._ServiceDetectionInfo.append(obj)
        self._NodeFlagFilter = params.get("NodeFlagFilter")
        if params.get("HealthStatus") is not None:
            self._HealthStatus = HealthStatus()
            self._HealthStatus._deserialize(params.get("HealthStatus"))
        self._IsSupportRoleMonitor = params.get("IsSupportRoleMonitor")
        if params.get("StopPolicies") is not None:
            self._StopPolicies = []
            for item in params.get("StopPolicies"):
                obj = RestartPolicy()
                obj._deserialize(item)
                self._StopPolicies.append(obj)
        self._HAState = params.get("HAState")
        self._NameService = params.get("NameService")
        self._IsFederation = params.get("IsFederation")
        self._DataNodeMaintenanceState = params.get("DataNodeMaintenanceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceProcessFunctionInfo(AbstractModel):
    """进程检测信息

    """

    def __init__(self):
        r"""
        :param _DetectAlert: 探测告警级别
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectAlert: str
        :param _DetetcFunctionKey: 探测功能描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DetetcFunctionKey: str
        :param _DetetcFunctionValue: 探测功能结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetetcFunctionValue: str
        :param _DetetcTime: 探测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetetcTime: str
        :param _DetectFunctionKey: 探测功能描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectFunctionKey: str
        :param _DetectFunctionValue: 探测功能结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectFunctionValue: str
        :param _DetectTime: 探测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectTime: str
        """
        self._DetectAlert = None
        self._DetetcFunctionKey = None
        self._DetetcFunctionValue = None
        self._DetetcTime = None
        self._DetectFunctionKey = None
        self._DetectFunctionValue = None
        self._DetectTime = None

    @property
    def DetectAlert(self):
        return self._DetectAlert

    @DetectAlert.setter
    def DetectAlert(self, DetectAlert):
        self._DetectAlert = DetectAlert

    @property
    def DetetcFunctionKey(self):
        warnings.warn("parameter `DetetcFunctionKey` is deprecated", DeprecationWarning) 

        return self._DetetcFunctionKey

    @DetetcFunctionKey.setter
    def DetetcFunctionKey(self, DetetcFunctionKey):
        warnings.warn("parameter `DetetcFunctionKey` is deprecated", DeprecationWarning) 

        self._DetetcFunctionKey = DetetcFunctionKey

    @property
    def DetetcFunctionValue(self):
        warnings.warn("parameter `DetetcFunctionValue` is deprecated", DeprecationWarning) 

        return self._DetetcFunctionValue

    @DetetcFunctionValue.setter
    def DetetcFunctionValue(self, DetetcFunctionValue):
        warnings.warn("parameter `DetetcFunctionValue` is deprecated", DeprecationWarning) 

        self._DetetcFunctionValue = DetetcFunctionValue

    @property
    def DetetcTime(self):
        warnings.warn("parameter `DetetcTime` is deprecated", DeprecationWarning) 

        return self._DetetcTime

    @DetetcTime.setter
    def DetetcTime(self, DetetcTime):
        warnings.warn("parameter `DetetcTime` is deprecated", DeprecationWarning) 

        self._DetetcTime = DetetcTime

    @property
    def DetectFunctionKey(self):
        return self._DetectFunctionKey

    @DetectFunctionKey.setter
    def DetectFunctionKey(self, DetectFunctionKey):
        self._DetectFunctionKey = DetectFunctionKey

    @property
    def DetectFunctionValue(self):
        return self._DetectFunctionValue

    @DetectFunctionValue.setter
    def DetectFunctionValue(self, DetectFunctionValue):
        self._DetectFunctionValue = DetectFunctionValue

    @property
    def DetectTime(self):
        return self._DetectTime

    @DetectTime.setter
    def DetectTime(self, DetectTime):
        self._DetectTime = DetectTime


    def _deserialize(self, params):
        self._DetectAlert = params.get("DetectAlert")
        self._DetetcFunctionKey = params.get("DetetcFunctionKey")
        self._DetetcFunctionValue = params.get("DetetcFunctionValue")
        self._DetetcTime = params.get("DetetcTime")
        self._DetectFunctionKey = params.get("DetectFunctionKey")
        self._DetectFunctionValue = params.get("DetectFunctionValue")
        self._DetectTime = params.get("DetectTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShortNodeInfo(AbstractModel):
    """节点信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型，Master/Core/Task/Router/Common
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _NodeSize: 节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSize: int
        """
        self._NodeType = None
        self._NodeSize = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeSize(self):
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeSize = params.get("NodeSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftDependInfo(AbstractModel):
    """体外客户端组件依赖信息

    """

    def __init__(self):
        r"""
        :param _SoftName: 组件名称
        :type SoftName: str
        :param _Required: 是否必选
        :type Required: bool
        """
        self._SoftName = None
        self._Required = None

    @property
    def SoftName(self):
        return self._SoftName

    @SoftName.setter
    def SoftName(self, SoftName):
        self._SoftName = SoftName

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._SoftName = params.get("SoftName")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkQuery(AbstractModel):
    """spark查询详情

    """

    def __init__(self):
        r"""
        :param _Statement: 执行语句
        :type Statement: str
        :param _Duration: 执行时长（单位毫秒）
        :type Duration: int
        :param _Status: 执行状态
        :type Status: str
        :param _Id: 查询ID
        :type Id: str
        :param _ScanPartitionNum: 扫描分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPartitionNum: int
        :param _ScanRowNum: 扫描总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRowNum: int
        :param _ScanFileNum: 扫描总文件数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanFileNum: int
        :param _ScanTotalData: 查询扫描总数据量(单位B)
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTotalData: int
        :param _ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: list of str
        :param _OutputRowNum: 输出总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputRowNum: int
        :param _OutputFileNum: 输出总文件数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFileNum: int
        :param _OutputPartitionNum: 输出分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputPartitionNum: int
        :param _OutputTotalData: 输出总数据量（单位B）
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputTotalData: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        """
        self._Statement = None
        self._Duration = None
        self._Status = None
        self._Id = None
        self._ScanPartitionNum = None
        self._ScanRowNum = None
        self._ScanFileNum = None
        self._ScanTotalData = None
        self._ApplicationId = None
        self._OutputRowNum = None
        self._OutputFileNum = None
        self._OutputPartitionNum = None
        self._OutputTotalData = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ScanPartitionNum(self):
        return self._ScanPartitionNum

    @ScanPartitionNum.setter
    def ScanPartitionNum(self, ScanPartitionNum):
        self._ScanPartitionNum = ScanPartitionNum

    @property
    def ScanRowNum(self):
        return self._ScanRowNum

    @ScanRowNum.setter
    def ScanRowNum(self, ScanRowNum):
        self._ScanRowNum = ScanRowNum

    @property
    def ScanFileNum(self):
        return self._ScanFileNum

    @ScanFileNum.setter
    def ScanFileNum(self, ScanFileNum):
        self._ScanFileNum = ScanFileNum

    @property
    def ScanTotalData(self):
        return self._ScanTotalData

    @ScanTotalData.setter
    def ScanTotalData(self, ScanTotalData):
        self._ScanTotalData = ScanTotalData

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def OutputRowNum(self):
        return self._OutputRowNum

    @OutputRowNum.setter
    def OutputRowNum(self, OutputRowNum):
        self._OutputRowNum = OutputRowNum

    @property
    def OutputFileNum(self):
        return self._OutputFileNum

    @OutputFileNum.setter
    def OutputFileNum(self, OutputFileNum):
        self._OutputFileNum = OutputFileNum

    @property
    def OutputPartitionNum(self):
        return self._OutputPartitionNum

    @OutputPartitionNum.setter
    def OutputPartitionNum(self, OutputPartitionNum):
        self._OutputPartitionNum = OutputPartitionNum

    @property
    def OutputTotalData(self):
        return self._OutputTotalData

    @OutputTotalData.setter
    def OutputTotalData(self, OutputTotalData):
        self._OutputTotalData = OutputTotalData

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Duration = params.get("Duration")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._ScanPartitionNum = params.get("ScanPartitionNum")
        self._ScanRowNum = params.get("ScanRowNum")
        self._ScanFileNum = params.get("ScanFileNum")
        self._ScanTotalData = params.get("ScanTotalData")
        self._ApplicationId = params.get("ApplicationId")
        self._OutputRowNum = params.get("OutputRowNum")
        self._OutputFileNum = params.get("OutputFileNum")
        self._OutputPartitionNum = params.get("OutputPartitionNum")
        self._OutputTotalData = params.get("OutputTotalData")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StageInfoDetail(AbstractModel):
    """任务步骤详情

    """

    def __init__(self):
        r"""
        :param _Stage: 步骤id
        :type Stage: str
        :param _Name: 步骤名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _IsShow: 是否展示
        :type IsShow: bool
        :param _IsSubFlow: 是否子流程
        :type IsSubFlow: bool
        :param _SubFlowFlag: 子流程标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubFlowFlag: str
        :param _Status: 步骤运行状态：0:未开始 1:进行中 2:已完成 3:部分完成  -1:失败
        :type Status: int
        :param _Desc: 步骤运行状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Progress: 运行进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _Starttime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Starttime: str
        :param _Endtime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Endtime: str
        :param _HadWoodDetail: 是否有详情信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HadWoodDetail: bool
        :param _WoodJobId: Wood子流程Id
注意：此字段可能返回 null，表示取不到有效值。
        :type WoodJobId: int
        :param _LanguageKey: 多语言版本Key
注意：此字段可能返回 null，表示取不到有效值。
        :type LanguageKey: str
        :param _FailedReason: 如果stage失败，失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _TimeConsuming: 步骤耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeConsuming: str
        """
        self._Stage = None
        self._Name = None
        self._IsShow = None
        self._IsSubFlow = None
        self._SubFlowFlag = None
        self._Status = None
        self._Desc = None
        self._Progress = None
        self._Starttime = None
        self._Endtime = None
        self._HadWoodDetail = None
        self._WoodJobId = None
        self._LanguageKey = None
        self._FailedReason = None
        self._TimeConsuming = None

    @property
    def Stage(self):
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsShow(self):
        return self._IsShow

    @IsShow.setter
    def IsShow(self, IsShow):
        self._IsShow = IsShow

    @property
    def IsSubFlow(self):
        return self._IsSubFlow

    @IsSubFlow.setter
    def IsSubFlow(self, IsSubFlow):
        self._IsSubFlow = IsSubFlow

    @property
    def SubFlowFlag(self):
        return self._SubFlowFlag

    @SubFlowFlag.setter
    def SubFlowFlag(self, SubFlowFlag):
        self._SubFlowFlag = SubFlowFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Starttime(self):
        return self._Starttime

    @Starttime.setter
    def Starttime(self, Starttime):
        self._Starttime = Starttime

    @property
    def Endtime(self):
        return self._Endtime

    @Endtime.setter
    def Endtime(self, Endtime):
        self._Endtime = Endtime

    @property
    def HadWoodDetail(self):
        return self._HadWoodDetail

    @HadWoodDetail.setter
    def HadWoodDetail(self, HadWoodDetail):
        self._HadWoodDetail = HadWoodDetail

    @property
    def WoodJobId(self):
        return self._WoodJobId

    @WoodJobId.setter
    def WoodJobId(self, WoodJobId):
        self._WoodJobId = WoodJobId

    @property
    def LanguageKey(self):
        return self._LanguageKey

    @LanguageKey.setter
    def LanguageKey(self, LanguageKey):
        self._LanguageKey = LanguageKey

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def TimeConsuming(self):
        return self._TimeConsuming

    @TimeConsuming.setter
    def TimeConsuming(self, TimeConsuming):
        self._TimeConsuming = TimeConsuming


    def _deserialize(self, params):
        self._Stage = params.get("Stage")
        self._Name = params.get("Name")
        self._IsShow = params.get("IsShow")
        self._IsSubFlow = params.get("IsSubFlow")
        self._SubFlowFlag = params.get("SubFlowFlag")
        self._Status = params.get("Status")
        self._Desc = params.get("Desc")
        self._Progress = params.get("Progress")
        self._Starttime = params.get("Starttime")
        self._Endtime = params.get("Endtime")
        self._HadWoodDetail = params.get("HadWoodDetail")
        self._WoodJobId = params.get("WoodJobId")
        self._LanguageKey = params.get("LanguageKey")
        self._FailedReason = params.get("FailedReason")
        self._TimeConsuming = params.get("TimeConsuming")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StarRocksQueryInfo(AbstractModel):
    """StarRocks 查询信息

    """

    def __init__(self):
        r"""
        :param _ClientIP: 提交IP
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param _CPUCost: CPU总时间(ns)
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUCost: int
        :param _DefaultDB: 默认DB
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDB: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _ExecutionIP: 执行IP
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionIP: str
        :param _QueryID: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryID: str
        :param _QueryType: 查询类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryType: str
        :param _MemCost: 消耗总内存(bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type MemCost: int
        :param _PlanCpuCosts: plan阶段CPU占用(ns)
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanCpuCosts: int
        :param _PlanMemCosts: plan阶段内存占用(bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanMemCosts: int
        :param _QueryTime: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryTime: int
        :param _ResourceGroup: 资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroup: str
        :param _ReturnRows: 获取行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnRows: int
        :param _ScanBytes: 扫描数据量(bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanBytes: int
        :param _ScanRows: 扫描行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRows: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param _ExecutionState: 执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionState: str
        :param _ExecutionStatement: 执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStatement: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        """
        self._ClientIP = None
        self._CPUCost = None
        self._DefaultDB = None
        self._EndTime = None
        self._ExecutionIP = None
        self._QueryID = None
        self._QueryType = None
        self._MemCost = None
        self._PlanCpuCosts = None
        self._PlanMemCosts = None
        self._QueryTime = None
        self._ResourceGroup = None
        self._ReturnRows = None
        self._ScanBytes = None
        self._ScanRows = None
        self._BeginTime = None
        self._ExecutionState = None
        self._ExecutionStatement = None
        self._User = None

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def CPUCost(self):
        return self._CPUCost

    @CPUCost.setter
    def CPUCost(self, CPUCost):
        self._CPUCost = CPUCost

    @property
    def DefaultDB(self):
        return self._DefaultDB

    @DefaultDB.setter
    def DefaultDB(self, DefaultDB):
        self._DefaultDB = DefaultDB

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionIP(self):
        return self._ExecutionIP

    @ExecutionIP.setter
    def ExecutionIP(self, ExecutionIP):
        self._ExecutionIP = ExecutionIP

    @property
    def QueryID(self):
        return self._QueryID

    @QueryID.setter
    def QueryID(self, QueryID):
        self._QueryID = QueryID

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def MemCost(self):
        return self._MemCost

    @MemCost.setter
    def MemCost(self, MemCost):
        self._MemCost = MemCost

    @property
    def PlanCpuCosts(self):
        return self._PlanCpuCosts

    @PlanCpuCosts.setter
    def PlanCpuCosts(self, PlanCpuCosts):
        self._PlanCpuCosts = PlanCpuCosts

    @property
    def PlanMemCosts(self):
        return self._PlanMemCosts

    @PlanMemCosts.setter
    def PlanMemCosts(self, PlanMemCosts):
        self._PlanMemCosts = PlanMemCosts

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def ResourceGroup(self):
        return self._ResourceGroup

    @ResourceGroup.setter
    def ResourceGroup(self, ResourceGroup):
        self._ResourceGroup = ResourceGroup

    @property
    def ReturnRows(self):
        return self._ReturnRows

    @ReturnRows.setter
    def ReturnRows(self, ReturnRows):
        self._ReturnRows = ReturnRows

    @property
    def ScanBytes(self):
        return self._ScanBytes

    @ScanBytes.setter
    def ScanBytes(self, ScanBytes):
        self._ScanBytes = ScanBytes

    @property
    def ScanRows(self):
        return self._ScanRows

    @ScanRows.setter
    def ScanRows(self, ScanRows):
        self._ScanRows = ScanRows

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def ExecutionState(self):
        return self._ExecutionState

    @ExecutionState.setter
    def ExecutionState(self, ExecutionState):
        self._ExecutionState = ExecutionState

    @property
    def ExecutionStatement(self):
        return self._ExecutionStatement

    @ExecutionStatement.setter
    def ExecutionStatement(self, ExecutionStatement):
        self._ExecutionStatement = ExecutionStatement

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._ClientIP = params.get("ClientIP")
        self._CPUCost = params.get("CPUCost")
        self._DefaultDB = params.get("DefaultDB")
        self._EndTime = params.get("EndTime")
        self._ExecutionIP = params.get("ExecutionIP")
        self._QueryID = params.get("QueryID")
        self._QueryType = params.get("QueryType")
        self._MemCost = params.get("MemCost")
        self._PlanCpuCosts = params.get("PlanCpuCosts")
        self._PlanMemCosts = params.get("PlanMemCosts")
        self._QueryTime = params.get("QueryTime")
        self._ResourceGroup = params.get("ResourceGroup")
        self._ReturnRows = params.get("ReturnRows")
        self._ScanBytes = params.get("ScanBytes")
        self._ScanRows = params.get("ScanRows")
        self._BeginTime = params.get("BeginTime")
        self._ExecutionState = params.get("ExecutionState")
        self._ExecutionStatement = params.get("ExecutionStatement")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorRequest(AbstractModel):
    """StartStopServiceOrMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _OpType: 操作类型，当前支持
<li>StartService：启动服务</li>
<li>StopService：停止服务</li>
<li>StartMonitor：退出维护</li>
<li>StopMonitor：进入维护</li>
<li>RestartService：重启服务 如果操作类型选择重启服务 StrategyConfig操作策略则是必填项</li>
        :type OpType: str
        :param _OpScope: 操作范围
        :type OpScope: :class:`tencentcloud.emr.v20190103.models.OpScope`
        :param _StrategyConfig: 操作策略
        :type StrategyConfig: :class:`tencentcloud.emr.v20190103.models.StrategyConfig`
        :param _StopParams: 暂停服务时用的参数
        :type StopParams: :class:`tencentcloud.emr.v20190103.models.StopParams`
        :param _KeepMonitorButNotRecoverProcess: 当OpType为<li>StopMonitor</li>才有用，true表示进入维护模式但是仍然监控进程但是不拉起进程
        :type KeepMonitorButNotRecoverProcess: bool
        """
        self._InstanceId = None
        self._OpType = None
        self._OpScope = None
        self._StrategyConfig = None
        self._StopParams = None
        self._KeepMonitorButNotRecoverProcess = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OpType(self):
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def OpScope(self):
        return self._OpScope

    @OpScope.setter
    def OpScope(self, OpScope):
        self._OpScope = OpScope

    @property
    def StrategyConfig(self):
        return self._StrategyConfig

    @StrategyConfig.setter
    def StrategyConfig(self, StrategyConfig):
        self._StrategyConfig = StrategyConfig

    @property
    def StopParams(self):
        return self._StopParams

    @StopParams.setter
    def StopParams(self, StopParams):
        self._StopParams = StopParams

    @property
    def KeepMonitorButNotRecoverProcess(self):
        return self._KeepMonitorButNotRecoverProcess

    @KeepMonitorButNotRecoverProcess.setter
    def KeepMonitorButNotRecoverProcess(self, KeepMonitorButNotRecoverProcess):
        self._KeepMonitorButNotRecoverProcess = KeepMonitorButNotRecoverProcess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OpType = params.get("OpType")
        if params.get("OpScope") is not None:
            self._OpScope = OpScope()
            self._OpScope._deserialize(params.get("OpScope"))
        if params.get("StrategyConfig") is not None:
            self._StrategyConfig = StrategyConfig()
            self._StrategyConfig._deserialize(params.get("StrategyConfig"))
        if params.get("StopParams") is not None:
            self._StopParams = StopParams()
            self._StopParams._deserialize(params.get("StopParams"))
        self._KeepMonitorButNotRecoverProcess = params.get("KeepMonitorButNotRecoverProcess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorResponse(AbstractModel):
    """StartStopServiceOrMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class Step(AbstractModel):
    """执行步骤

    """

    def __init__(self):
        r"""
        :param _Name: 执行步骤名称。
        :type Name: str
        :param _ExecutionStep: 执行动作。
        :type ExecutionStep: :class:`tencentcloud.emr.v20190103.models.Execution`
        :param _ActionOnFailure: 执行失败策略。
1. TERMINATE_CLUSTER 执行失败时退出并销毁集群。
2. CONTINUE 执行失败时跳过并执行后续步骤。
        :type ActionOnFailure: str
        :param _User: 指定执行Step时的用户名，非必须，默认为hadoop。
        :type User: str
        """
        self._Name = None
        self._ExecutionStep = None
        self._ActionOnFailure = None
        self._User = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExecutionStep(self):
        return self._ExecutionStep

    @ExecutionStep.setter
    def ExecutionStep(self, ExecutionStep):
        self._ExecutionStep = ExecutionStep

    @property
    def ActionOnFailure(self):
        return self._ActionOnFailure

    @ActionOnFailure.setter
    def ActionOnFailure(self, ActionOnFailure):
        self._ActionOnFailure = ActionOnFailure

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("ExecutionStep") is not None:
            self._ExecutionStep = Execution()
            self._ExecutionStep._deserialize(params.get("ExecutionStep"))
        self._ActionOnFailure = params.get("ActionOnFailure")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopParams(AbstractModel):
    """停止服务时的参数

    """

    def __init__(self):
        r"""
        :param _StopPolicy: 安全模式：safe
默认模式：default
        :type StopPolicy: str
        :param _ThreadCount: 线程数
        :type ThreadCount: int
        """
        self._StopPolicy = None
        self._ThreadCount = None

    @property
    def StopPolicy(self):
        return self._StopPolicy

    @StopPolicy.setter
    def StopPolicy(self, StopPolicy):
        self._StopPolicy = StopPolicy

    @property
    def ThreadCount(self):
        return self._ThreadCount

    @ThreadCount.setter
    def ThreadCount(self, ThreadCount):
        self._ThreadCount = ThreadCount


    def _deserialize(self, params):
        self._StopPolicy = params.get("StopPolicy")
        self._ThreadCount = params.get("ThreadCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageSummaryDistribution(AbstractModel):
    """HDFS文件存储详情

    """

    def __init__(self):
        r"""
        :param _MetricItem: 数据项
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricItem: str
        :param _MetricName: 数据项描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _Dps: 采样值
注意：此字段可能返回 null，表示取不到有效值。
        :type Dps: list of Dps
        """
        self._MetricItem = None
        self._MetricName = None
        self._Dps = None

    @property
    def MetricItem(self):
        return self._MetricItem

    @MetricItem.setter
    def MetricItem(self, MetricItem):
        self._MetricItem = MetricItem

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Dps(self):
        return self._Dps

    @Dps.setter
    def Dps(self, Dps):
        self._Dps = Dps


    def _deserialize(self, params):
        self._MetricItem = params.get("MetricItem")
        self._MetricName = params.get("MetricName")
        if params.get("Dps") is not None:
            self._Dps = []
            for item in params.get("Dps"):
                obj = Dps()
                obj._deserialize(item)
                self._Dps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyConfig(AbstractModel):
    """重启/停止/启动服务/监控的配置

    """

    def __init__(self):
        r"""
        :param _RollingRestartSwitch: 0:关闭滚动重启
1:开启滚动启动
注意：此字段可能返回 null，表示取不到有效值。
        :type RollingRestartSwitch: int
        :param _BatchSize: 滚动重启每批次的重启数量，最大重启台数为 99999 台
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _TimeWait: 滚动重启每批停止等待时间 ,最大间隔为 5 分钟 单位是秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeWait: int
        :param _DealOnFail: 操作失败处理策略，0:失败阻塞, 1:失败自动跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOnFail: int
        :param _Args: 指令需要指定的参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Args: list of Arg
        """
        self._RollingRestartSwitch = None
        self._BatchSize = None
        self._TimeWait = None
        self._DealOnFail = None
        self._Args = None

    @property
    def RollingRestartSwitch(self):
        return self._RollingRestartSwitch

    @RollingRestartSwitch.setter
    def RollingRestartSwitch(self, RollingRestartSwitch):
        self._RollingRestartSwitch = RollingRestartSwitch

    @property
    def BatchSize(self):
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def TimeWait(self):
        return self._TimeWait

    @TimeWait.setter
    def TimeWait(self, TimeWait):
        self._TimeWait = TimeWait

    @property
    def DealOnFail(self):
        return self._DealOnFail

    @DealOnFail.setter
    def DealOnFail(self, DealOnFail):
        self._DealOnFail = DealOnFail

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._RollingRestartSwitch = params.get("RollingRestartSwitch")
        self._BatchSize = params.get("BatchSize")
        self._TimeWait = params.get("TimeWait")
        self._DealOnFail = params.get("DealOnFail")
        if params.get("Args") is not None:
            self._Args = []
            for item in params.get("Args"):
                obj = Arg()
                obj._deserialize(item)
                self._Args.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInfo(AbstractModel):
    """子网信息

    """

    def __init__(self):
        r"""
        :param _SubnetName: 子网信息（名字）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _SubnetId: 子网信息（ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._SubnetName = None
        self._SubnetId = None

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateRequest(AbstractModel):
    """SyncPodState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Message: EmrService中pod状态信息
        :type Message: :class:`tencentcloud.emr.v20190103.models.PodState`
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self._Message = PodState()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateResponse(AbstractModel):
    """SyncPodState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class TableSchemaItem(AbstractModel):
    """表格schema信息

    """

    def __init__(self):
        r"""
        :param _Name: 列标识
        :type Name: str
        :param _Sortable: 是否可按该列排序
        :type Sortable: bool
        :param _WithFilter: 是否可筛选
        :type WithFilter: bool
        :param _Candidates: 筛选的候选集
注意：此字段可能返回 null，表示取不到有效值。
        :type Candidates: list of str
        :param _Clickable: 是否可点击
注意：此字段可能返回 null，表示取不到有效值。
        :type Clickable: bool
        :param _Title: 展示的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        """
        self._Name = None
        self._Sortable = None
        self._WithFilter = None
        self._Candidates = None
        self._Clickable = None
        self._Title = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sortable(self):
        return self._Sortable

    @Sortable.setter
    def Sortable(self, Sortable):
        self._Sortable = Sortable

    @property
    def WithFilter(self):
        return self._WithFilter

    @WithFilter.setter
    def WithFilter(self, WithFilter):
        self._WithFilter = WithFilter

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates

    @property
    def Clickable(self):
        return self._Clickable

    @Clickable.setter
    def Clickable(self, Clickable):
        self._Clickable = Clickable

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sortable = params.get("Sortable")
        self._WithFilter = params.get("WithFilter")
        self._Candidates = params.get("Candidates")
        self._Clickable = params.get("Clickable")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateClusterNodesRequest(AbstractModel):
    """TerminateClusterNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CvmInstanceIds: 销毁资源列表
        :type CvmInstanceIds: list of str
        :param _NodeFlag: 销毁节点类型取值范围：
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _GraceDownFlag: 优雅缩容开关
  <li>true:开启</li>
  <li>false:不开启</li>
        :type GraceDownFlag: bool
        :param _GraceDownTime: 优雅缩容等待时间,时间范围60到1800  单位秒
        :type GraceDownTime: int
        """
        self._InstanceId = None
        self._CvmInstanceIds = None
        self._NodeFlag = None
        self._GraceDownFlag = None
        self._GraceDownTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceIds(self):
        return self._CvmInstanceIds

    @CvmInstanceIds.setter
    def CvmInstanceIds(self, CvmInstanceIds):
        self._CvmInstanceIds = CvmInstanceIds

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def GraceDownFlag(self):
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def GraceDownTime(self):
        return self._GraceDownTime

    @GraceDownTime.setter
    def GraceDownTime(self, GraceDownTime):
        self._GraceDownTime = GraceDownTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceIds = params.get("CvmInstanceIds")
        self._NodeFlag = params.get("NodeFlag")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._GraceDownTime = params.get("GraceDownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateClusterNodesResponse(AbstractModel):
    """TerminateClusterNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 缩容流程ID。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ResourceIds: 销毁节点ID。该参数为预留参数，用户无需配置。
        :type ResourceIds: list of str
        :param _ResourceBaseType: 类型为ComputeResource和EMR以及默认，默认为EMR,类型为EMR时,InstanceId生效,类型为ComputeResource时,使用ComputeResourceId标识
        :type ResourceBaseType: str
        :param _ComputeResourceId: 计算资源ID
        :type ComputeResourceId: str
        """
        self._InstanceId = None
        self._ResourceIds = None
        self._ResourceBaseType = None
        self._ComputeResourceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ResourceBaseType(self):
        return self._ResourceBaseType

    @ResourceBaseType.setter
    def ResourceBaseType(self, ResourceBaseType):
        self._ResourceBaseType = ResourceBaseType

    @property
    def ComputeResourceId(self):
        return self._ComputeResourceId

    @ComputeResourceId.setter
    def ComputeResourceId(self, ComputeResourceId):
        self._ComputeResourceId = ComputeResourceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        self._ResourceBaseType = params.get("ResourceBaseType")
        self._ComputeResourceId = params.get("ComputeResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class TerminateSLInstanceRequest(AbstractModel):
    """TerminateSLInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一标识符（字符串表示）
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSLInstanceResponse(AbstractModel):
    """TerminateSLInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ResourceIds: 待销毁节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr)查询。
        :type ResourceIds: list of str
        """
        self._InstanceId = None
        self._ResourceIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class TimeAutoScaleStrategy(AbstractModel):
    """时间扩缩容规则

    """

    def __init__(self):
        r"""
        :param _StrategyName: 策略名字，集群内唯一。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param _IntervalTime: 策略触发后的冷却时间，该段时间内，将不能触发弹性扩缩容。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntervalTime: int
        :param _ScaleAction: 扩缩容动作，1表示扩容，2表示缩容。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleAction: int
        :param _ScaleNum: 扩缩容数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleNum: int
        :param _StrategyStatus: 规则状态，1表示有效，2表示无效，3表示暂停。必须填写
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyStatus: int
        :param _Priority: 规则优先级，越小越高。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _RetryValidTime: 当多条规则同时触发，其中某些未真正执行时，在该时间范围内，将会重试。
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryValidTime: int
        :param _RepeatStrategy: 时间扩缩容重复策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RepeatStrategy: :class:`tencentcloud.emr.v20190103.models.RepeatStrategy`
        :param _StrategyId: 策略唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _GraceDownFlag: 优雅缩容开关
注意：此字段可能返回 null，表示取不到有效值。
        :type GraceDownFlag: bool
        :param _GraceDownTime: 优雅缩容等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type GraceDownTime: int
        :param _Tags: 绑定标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ConfigGroupAssigned: 预设配置组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigGroupAssigned: str
        :param _MeasureMethod: 扩容资源计算方法，"DEFAULT","INSTANCE", "CPU", "MEMORYGB"。
"DEFAULT"表示默认方式，与"INSTANCE"意义相同。
"INSTANCE"表示按照节点计算，默认方式。
"CPU"表示按照机器的核数计算。
"MEMORYGB"表示按照机器内存数计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type MeasureMethod: str
        :param _TerminatePolicy: 销毁策略, "DEFAULT",默认销毁策略，由缩容规则触发缩容，"TIMING"表示定时销毁
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminatePolicy: str
        :param _MaxUse: 最长使用时间， 秒数，最短1小时，最长24小时
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUse: int
        :param _SoftDeployInfo: 节点部署服务列表。部署服务仅填写HDFS、YARN。[组件名对应的映射关系表](https://cloud.tencent.com/document/product/589/98760)
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftDeployInfo: list of int
        :param _ServiceNodeInfo: 启动进程列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceNodeInfo: list of int
        :param _CompensateFlag: 补偿扩容，0表示不开启，1表示开启
注意：此字段可能返回 null，表示取不到有效值。
        :type CompensateFlag: int
        :param _GroupId: 伸缩组id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        """
        self._StrategyName = None
        self._IntervalTime = None
        self._ScaleAction = None
        self._ScaleNum = None
        self._StrategyStatus = None
        self._Priority = None
        self._RetryValidTime = None
        self._RepeatStrategy = None
        self._StrategyId = None
        self._GraceDownFlag = None
        self._GraceDownTime = None
        self._Tags = None
        self._ConfigGroupAssigned = None
        self._MeasureMethod = None
        self._TerminatePolicy = None
        self._MaxUse = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._CompensateFlag = None
        self._GroupId = None

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def ScaleAction(self):
        return self._ScaleAction

    @ScaleAction.setter
    def ScaleAction(self, ScaleAction):
        self._ScaleAction = ScaleAction

    @property
    def ScaleNum(self):
        return self._ScaleNum

    @ScaleNum.setter
    def ScaleNum(self, ScaleNum):
        self._ScaleNum = ScaleNum

    @property
    def StrategyStatus(self):
        return self._StrategyStatus

    @StrategyStatus.setter
    def StrategyStatus(self, StrategyStatus):
        self._StrategyStatus = StrategyStatus

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RetryValidTime(self):
        return self._RetryValidTime

    @RetryValidTime.setter
    def RetryValidTime(self, RetryValidTime):
        self._RetryValidTime = RetryValidTime

    @property
    def RepeatStrategy(self):
        return self._RepeatStrategy

    @RepeatStrategy.setter
    def RepeatStrategy(self, RepeatStrategy):
        self._RepeatStrategy = RepeatStrategy

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GraceDownFlag(self):
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def GraceDownTime(self):
        return self._GraceDownTime

    @GraceDownTime.setter
    def GraceDownTime(self, GraceDownTime):
        self._GraceDownTime = GraceDownTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ConfigGroupAssigned(self):
        return self._ConfigGroupAssigned

    @ConfigGroupAssigned.setter
    def ConfigGroupAssigned(self, ConfigGroupAssigned):
        self._ConfigGroupAssigned = ConfigGroupAssigned

    @property
    def MeasureMethod(self):
        return self._MeasureMethod

    @MeasureMethod.setter
    def MeasureMethod(self, MeasureMethod):
        self._MeasureMethod = MeasureMethod

    @property
    def TerminatePolicy(self):
        return self._TerminatePolicy

    @TerminatePolicy.setter
    def TerminatePolicy(self, TerminatePolicy):
        self._TerminatePolicy = TerminatePolicy

    @property
    def MaxUse(self):
        return self._MaxUse

    @MaxUse.setter
    def MaxUse(self, MaxUse):
        self._MaxUse = MaxUse

    @property
    def SoftDeployInfo(self):
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def CompensateFlag(self):
        return self._CompensateFlag

    @CompensateFlag.setter
    def CompensateFlag(self, CompensateFlag):
        self._CompensateFlag = CompensateFlag

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._StrategyName = params.get("StrategyName")
        self._IntervalTime = params.get("IntervalTime")
        self._ScaleAction = params.get("ScaleAction")
        self._ScaleNum = params.get("ScaleNum")
        self._StrategyStatus = params.get("StrategyStatus")
        self._Priority = params.get("Priority")
        self._RetryValidTime = params.get("RetryValidTime")
        if params.get("RepeatStrategy") is not None:
            self._RepeatStrategy = RepeatStrategy()
            self._RepeatStrategy._deserialize(params.get("RepeatStrategy"))
        self._StrategyId = params.get("StrategyId")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._GraceDownTime = params.get("GraceDownTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ConfigGroupAssigned = params.get("ConfigGroupAssigned")
        self._MeasureMethod = params.get("MeasureMethod")
        self._TerminatePolicy = params.get("TerminatePolicy")
        self._MaxUse = params.get("MaxUse")
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._CompensateFlag = params.get("CompensateFlag")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopologyInfo(AbstractModel):
    """集群节点拓扑信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _Zone: 可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SubnetInfoList: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetInfoList: list of SubnetInfo
        :param _NodeInfoList: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfoList: list of ShortNodeInfo
        """
        self._ZoneId = None
        self._Zone = None
        self._SubnetInfoList = None
        self._NodeInfoList = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfoList(self):
        return self._SubnetInfoList

    @SubnetInfoList.setter
    def SubnetInfoList(self, SubnetInfoList):
        self._SubnetInfoList = SubnetInfoList

    @property
    def NodeInfoList(self):
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfoList") is not None:
            self._SubnetInfoList = []
            for item in params.get("SubnetInfoList"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._SubnetInfoList.append(obj)
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = ShortNodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerCondition(AbstractModel):
    """规则触发条件

    """

    def __init__(self):
        r"""
        :param _CompareMethod: 条件比较方法，1表示大于，2表示小于，3表示大于等于，4表示小于等于。
        :type CompareMethod: int
        :param _Threshold: 条件阈值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: float
        """
        self._CompareMethod = None
        self._Threshold = None

    @property
    def CompareMethod(self):
        return self._CompareMethod

    @CompareMethod.setter
    def CompareMethod(self, CompareMethod):
        self._CompareMethod = CompareMethod

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._CompareMethod = params.get("CompareMethod")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrinoQueryInfo(AbstractModel):
    """trino 查询信息

    """

    def __init__(self):
        r"""
        :param _Catalog: catalog
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param _ClientIpAddr: 提交IP
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpAddr: str
        :param _CompletedSplits: 切片数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompletedSplits: str
        :param _CpuTime: CPU时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuTime: int
        :param _CumulativeMemory: 累计内存
注意：此字段可能返回 null，表示取不到有效值。
        :type CumulativeMemory: int
        :param _DurationMillis: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationMillis: int
        :param _EndTime: 结束时间 (s)
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _Id: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _InternalNetworkBytes: 内部传输量
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalNetworkBytes: int
        :param _OutputBytes: 输出字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputBytes: int
        :param _PeakUserMemoryBytes: 峰值内存量
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakUserMemoryBytes: int
        :param _PhysicalInputBytes: 物理输入量
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalInputBytes: int
        :param _ProcessedInputBytes: 处理输入量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedInputBytes: int
        :param _SqlCompileTime: 编译时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlCompileTime: int
        :param _StartTime: 开始时间 (s)
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _State: 执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Statement: 执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Statement: str
        :param _User: 提交用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _WrittenBytes: 写入字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type WrittenBytes: int
        """
        self._Catalog = None
        self._ClientIpAddr = None
        self._CompletedSplits = None
        self._CpuTime = None
        self._CumulativeMemory = None
        self._DurationMillis = None
        self._EndTime = None
        self._Id = None
        self._InternalNetworkBytes = None
        self._OutputBytes = None
        self._PeakUserMemoryBytes = None
        self._PhysicalInputBytes = None
        self._ProcessedInputBytes = None
        self._SqlCompileTime = None
        self._StartTime = None
        self._State = None
        self._Statement = None
        self._User = None
        self._WrittenBytes = None

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def ClientIpAddr(self):
        return self._ClientIpAddr

    @ClientIpAddr.setter
    def ClientIpAddr(self, ClientIpAddr):
        self._ClientIpAddr = ClientIpAddr

    @property
    def CompletedSplits(self):
        return self._CompletedSplits

    @CompletedSplits.setter
    def CompletedSplits(self, CompletedSplits):
        self._CompletedSplits = CompletedSplits

    @property
    def CpuTime(self):
        return self._CpuTime

    @CpuTime.setter
    def CpuTime(self, CpuTime):
        self._CpuTime = CpuTime

    @property
    def CumulativeMemory(self):
        return self._CumulativeMemory

    @CumulativeMemory.setter
    def CumulativeMemory(self, CumulativeMemory):
        self._CumulativeMemory = CumulativeMemory

    @property
    def DurationMillis(self):
        return self._DurationMillis

    @DurationMillis.setter
    def DurationMillis(self, DurationMillis):
        self._DurationMillis = DurationMillis

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InternalNetworkBytes(self):
        return self._InternalNetworkBytes

    @InternalNetworkBytes.setter
    def InternalNetworkBytes(self, InternalNetworkBytes):
        self._InternalNetworkBytes = InternalNetworkBytes

    @property
    def OutputBytes(self):
        return self._OutputBytes

    @OutputBytes.setter
    def OutputBytes(self, OutputBytes):
        self._OutputBytes = OutputBytes

    @property
    def PeakUserMemoryBytes(self):
        return self._PeakUserMemoryBytes

    @PeakUserMemoryBytes.setter
    def PeakUserMemoryBytes(self, PeakUserMemoryBytes):
        self._PeakUserMemoryBytes = PeakUserMemoryBytes

    @property
    def PhysicalInputBytes(self):
        return self._PhysicalInputBytes

    @PhysicalInputBytes.setter
    def PhysicalInputBytes(self, PhysicalInputBytes):
        self._PhysicalInputBytes = PhysicalInputBytes

    @property
    def ProcessedInputBytes(self):
        return self._ProcessedInputBytes

    @ProcessedInputBytes.setter
    def ProcessedInputBytes(self, ProcessedInputBytes):
        self._ProcessedInputBytes = ProcessedInputBytes

    @property
    def SqlCompileTime(self):
        return self._SqlCompileTime

    @SqlCompileTime.setter
    def SqlCompileTime(self, SqlCompileTime):
        self._SqlCompileTime = SqlCompileTime

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
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def WrittenBytes(self):
        return self._WrittenBytes

    @WrittenBytes.setter
    def WrittenBytes(self, WrittenBytes):
        self._WrittenBytes = WrittenBytes


    def _deserialize(self, params):
        self._Catalog = params.get("Catalog")
        self._ClientIpAddr = params.get("ClientIpAddr")
        self._CompletedSplits = params.get("CompletedSplits")
        self._CpuTime = params.get("CpuTime")
        self._CumulativeMemory = params.get("CumulativeMemory")
        self._DurationMillis = params.get("DurationMillis")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._InternalNetworkBytes = params.get("InternalNetworkBytes")
        self._OutputBytes = params.get("OutputBytes")
        self._PeakUserMemoryBytes = params.get("PeakUserMemoryBytes")
        self._PhysicalInputBytes = params.get("PhysicalInputBytes")
        self._ProcessedInputBytes = params.get("ProcessedInputBytes")
        self._SqlCompileTime = params.get("SqlCompileTime")
        self._StartTime = params.get("StartTime")
        self._State = params.get("State")
        self._Statement = params.get("Statement")
        self._User = params.get("User")
        self._WrittenBytes = params.get("WrittenBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceSettings(AbstractModel):
    """变配资源规格

    """

    def __init__(self):
        r"""
        :param _Memory: 内存容量，单位为G
        :type Memory: int
        :param _CPUCores: CPU核数
        :type CPUCores: int
        :param _ResourceId: 机器资源ID（EMR测资源标识）
        :type ResourceId: str
        :param _InstanceType: 变配机器规格
        :type InstanceType: str
        """
        self._Memory = None
        self._CPUCores = None
        self._ResourceId = None
        self._InstanceType = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CPUCores(self):
        return self._CPUCores

    @CPUCores.setter
    def CPUCores(self, CPUCores):
        self._CPUCores = CPUCores

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._CPUCores = params.get("CPUCores")
        self._ResourceId = params.get("ResourceId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAndGroup(AbstractModel):
    """容器集群用户组信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _UserGroup: 用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroup: str
        """
        self._UserName = None
        self._UserGroup = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoForUserManager(AbstractModel):
    """添加的用户信息列表

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _UserGroup: 用户所属的组
        :type UserGroup: str
        :param _PassWord: 密码
        :type PassWord: str
        :param _ReMark: 备注
        :type ReMark: str
        """
        self._UserName = None
        self._UserGroup = None
        self._PassWord = None
        self._ReMark = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def PassWord(self):
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def ReMark(self):
        return self._ReMark

    @ReMark.setter
    def ReMark(self, ReMark):
        self._ReMark = ReMark


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._PassWord = params.get("PassWord")
        self._ReMark = params.get("ReMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerFilter(AbstractModel):
    """用户管理列表过滤器

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._UserName = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerUserBriefInfo(AbstractModel):
    """用户管理中用户的简要信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _UserGroup: 用户所属的组
        :type UserGroup: str
        :param _UserType: Manager表示管理员、NormalUser表示普通用户
        :type UserType: str
        :param _CreateTime: 用户创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SupportDownLoadKeyTab: 是否可以下载用户对应的keytab文件，对开启kerberos的集群才有意义
        :type SupportDownLoadKeyTab: bool
        :param _DownLoadKeyTabUrl: keytab文件的下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownLoadKeyTabUrl: str
        """
        self._UserName = None
        self._UserGroup = None
        self._UserType = None
        self._CreateTime = None
        self._SupportDownLoadKeyTab = None
        self._DownLoadKeyTabUrl = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SupportDownLoadKeyTab(self):
        return self._SupportDownLoadKeyTab

    @SupportDownLoadKeyTab.setter
    def SupportDownLoadKeyTab(self, SupportDownLoadKeyTab):
        self._SupportDownLoadKeyTab = SupportDownLoadKeyTab

    @property
    def DownLoadKeyTabUrl(self):
        return self._DownLoadKeyTabUrl

    @DownLoadKeyTabUrl.setter
    def DownLoadKeyTabUrl(self, DownLoadKeyTabUrl):
        self._DownLoadKeyTabUrl = DownLoadKeyTabUrl


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._UserType = params.get("UserType")
        self._CreateTime = params.get("CreateTime")
        self._SupportDownLoadKeyTab = params.get("SupportDownLoadKeyTab")
        self._DownLoadKeyTabUrl = params.get("DownLoadKeyTabUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCSettings(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
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
        


class VirtualPrivateCloud(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
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
        


class WeekRepeatStrategy(AbstractModel):
    """定时扩容每周重复任务策略

    """

    def __init__(self):
        r"""
        :param _ExecuteAtTimeOfDay: 重复任务执行的具体时刻，例如"01:02:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteAtTimeOfDay: str
        :param _DaysOfWeek: 每周几的数字描述，例如，[1,3,4]表示每周周一、周三、周四。
注意：此字段可能返回 null，表示取不到有效值。
        :type DaysOfWeek: list of int non-negative
        """
        self._ExecuteAtTimeOfDay = None
        self._DaysOfWeek = None

    @property
    def ExecuteAtTimeOfDay(self):
        return self._ExecuteAtTimeOfDay

    @ExecuteAtTimeOfDay.setter
    def ExecuteAtTimeOfDay(self, ExecuteAtTimeOfDay):
        self._ExecuteAtTimeOfDay = ExecuteAtTimeOfDay

    @property
    def DaysOfWeek(self):
        return self._DaysOfWeek

    @DaysOfWeek.setter
    def DaysOfWeek(self, DaysOfWeek):
        self._DaysOfWeek = DaysOfWeek


    def _deserialize(self, params):
        self._ExecuteAtTimeOfDay = params.get("ExecuteAtTimeOfDay")
        self._DaysOfWeek = params.get("DaysOfWeek")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class YarnApplication(AbstractModel):
    """Yarn 运行的Application信息

    """

    def __init__(self):
        r"""
        :param _Id: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Name: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Queue: 队列
注意：此字段可能返回 null，表示取不到有效值。
        :type Queue: str
        :param _ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param _ElapsedTime: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ElapsedTime: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _FinalStatus: 最终状态
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalStatus: str
        :param _Progress: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _StartedTime: 开始时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedTime: int
        :param _FinishedTime: 结束时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedTime: int
        :param _AllocatedMB: 申请内存MB
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedMB: int
        :param _AllocatedVCores: 申请VCores
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedVCores: int
        :param _RunningContainers: 运行的Containers数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningContainers: int
        :param _MemorySeconds: 内存MB*时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MemorySeconds: int
        :param _VCoreSeconds: VCores*时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreSeconds: int
        :param _QueueUsagePercentage: 队列资源占比
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueUsagePercentage: float
        :param _ClusterUsagePercentage: 集群资源占比
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterUsagePercentage: float
        :param _PreemptedResourceMB: 预占用的内存
注意：此字段可能返回 null，表示取不到有效值。
        :type PreemptedResourceMB: int
        :param _PreemptedResourceVCores: 预占用的VCore
注意：此字段可能返回 null，表示取不到有效值。
        :type PreemptedResourceVCores: int
        :param _NumNonAMContainerPreempted: 预占的非应用程序主节点容器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumNonAMContainerPreempted: int
        :param _NumAMContainerPreempted: AM预占用的容器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumAMContainerPreempted: int
        :param _MapsTotal: Map总数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapsTotal: int
        :param _MapsCompleted: 完成的Map数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapsCompleted: int
        :param _ReducesTotal: Reduce总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReducesTotal: int
        :param _ReducesCompleted: 完成的Reduce数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReducesCompleted: int
        :param _AvgMapTime: 平均Map时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgMapTime: int
        :param _AvgReduceTime: 平均Reduce时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgReduceTime: int
        :param _AvgShuffleTime: 平均Shuffle时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgShuffleTime: int
        :param _AvgMergeTime: 平均Merge时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgMergeTime: int
        :param _FailedReduceAttempts: 失败的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReduceAttempts: int
        :param _KilledReduceAttempts: Kill的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type KilledReduceAttempts: int
        :param _SuccessfulReduceAttempts: 成功的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessfulReduceAttempts: int
        :param _FailedMapAttempts: 失败的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMapAttempts: int
        :param _KilledMapAttempts: Kill的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type KilledMapAttempts: int
        :param _SuccessfulMapAttempts: 成功的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessfulMapAttempts: int
        :param _GcTimeMillis: GC毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type GcTimeMillis: int
        :param _VCoreMillisMaps: Map使用的VCore毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreMillisMaps: int
        :param _MbMillisMaps: Map使用的内存毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MbMillisMaps: int
        :param _VCoreMillisReduces: Reduce使用的VCore毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreMillisReduces: int
        :param _MbMillisReduces: Reduce使用的内存毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MbMillisReduces: int
        :param _TotalLaunchedMaps: 启动Map的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalLaunchedMaps: int
        :param _TotalLaunchedReduces: 启动Reduce的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalLaunchedReduces: int
        :param _MapInputRecords: Map输入记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapInputRecords: int
        :param _MapOutputRecords: Map输出记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapOutputRecords: int
        :param _ReduceInputRecords: Reduce输入记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReduceInputRecords: int
        :param _ReduceOutputRecords: Reduce输出记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReduceOutputRecords: int
        :param _HDFSBytesWritten: HDFS写入字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSBytesWritten: int
        :param _HDFSBytesRead: HDFS读取字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSBytesRead: int
        """
        self._Id = None
        self._User = None
        self._Name = None
        self._Queue = None
        self._ApplicationType = None
        self._ElapsedTime = None
        self._State = None
        self._FinalStatus = None
        self._Progress = None
        self._StartedTime = None
        self._FinishedTime = None
        self._AllocatedMB = None
        self._AllocatedVCores = None
        self._RunningContainers = None
        self._MemorySeconds = None
        self._VCoreSeconds = None
        self._QueueUsagePercentage = None
        self._ClusterUsagePercentage = None
        self._PreemptedResourceMB = None
        self._PreemptedResourceVCores = None
        self._NumNonAMContainerPreempted = None
        self._NumAMContainerPreempted = None
        self._MapsTotal = None
        self._MapsCompleted = None
        self._ReducesTotal = None
        self._ReducesCompleted = None
        self._AvgMapTime = None
        self._AvgReduceTime = None
        self._AvgShuffleTime = None
        self._AvgMergeTime = None
        self._FailedReduceAttempts = None
        self._KilledReduceAttempts = None
        self._SuccessfulReduceAttempts = None
        self._FailedMapAttempts = None
        self._KilledMapAttempts = None
        self._SuccessfulMapAttempts = None
        self._GcTimeMillis = None
        self._VCoreMillisMaps = None
        self._MbMillisMaps = None
        self._VCoreMillisReduces = None
        self._MbMillisReduces = None
        self._TotalLaunchedMaps = None
        self._TotalLaunchedReduces = None
        self._MapInputRecords = None
        self._MapOutputRecords = None
        self._ReduceInputRecords = None
        self._ReduceOutputRecords = None
        self._HDFSBytesWritten = None
        self._HDFSBytesRead = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ElapsedTime(self):
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FinalStatus(self):
        return self._FinalStatus

    @FinalStatus.setter
    def FinalStatus(self, FinalStatus):
        self._FinalStatus = FinalStatus

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartedTime(self):
        return self._StartedTime

    @StartedTime.setter
    def StartedTime(self, StartedTime):
        self._StartedTime = StartedTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def AllocatedMB(self):
        return self._AllocatedMB

    @AllocatedMB.setter
    def AllocatedMB(self, AllocatedMB):
        self._AllocatedMB = AllocatedMB

    @property
    def AllocatedVCores(self):
        return self._AllocatedVCores

    @AllocatedVCores.setter
    def AllocatedVCores(self, AllocatedVCores):
        self._AllocatedVCores = AllocatedVCores

    @property
    def RunningContainers(self):
        return self._RunningContainers

    @RunningContainers.setter
    def RunningContainers(self, RunningContainers):
        self._RunningContainers = RunningContainers

    @property
    def MemorySeconds(self):
        return self._MemorySeconds

    @MemorySeconds.setter
    def MemorySeconds(self, MemorySeconds):
        self._MemorySeconds = MemorySeconds

    @property
    def VCoreSeconds(self):
        return self._VCoreSeconds

    @VCoreSeconds.setter
    def VCoreSeconds(self, VCoreSeconds):
        self._VCoreSeconds = VCoreSeconds

    @property
    def QueueUsagePercentage(self):
        return self._QueueUsagePercentage

    @QueueUsagePercentage.setter
    def QueueUsagePercentage(self, QueueUsagePercentage):
        self._QueueUsagePercentage = QueueUsagePercentage

    @property
    def ClusterUsagePercentage(self):
        return self._ClusterUsagePercentage

    @ClusterUsagePercentage.setter
    def ClusterUsagePercentage(self, ClusterUsagePercentage):
        self._ClusterUsagePercentage = ClusterUsagePercentage

    @property
    def PreemptedResourceMB(self):
        return self._PreemptedResourceMB

    @PreemptedResourceMB.setter
    def PreemptedResourceMB(self, PreemptedResourceMB):
        self._PreemptedResourceMB = PreemptedResourceMB

    @property
    def PreemptedResourceVCores(self):
        return self._PreemptedResourceVCores

    @PreemptedResourceVCores.setter
    def PreemptedResourceVCores(self, PreemptedResourceVCores):
        self._PreemptedResourceVCores = PreemptedResourceVCores

    @property
    def NumNonAMContainerPreempted(self):
        return self._NumNonAMContainerPreempted

    @NumNonAMContainerPreempted.setter
    def NumNonAMContainerPreempted(self, NumNonAMContainerPreempted):
        self._NumNonAMContainerPreempted = NumNonAMContainerPreempted

    @property
    def NumAMContainerPreempted(self):
        return self._NumAMContainerPreempted

    @NumAMContainerPreempted.setter
    def NumAMContainerPreempted(self, NumAMContainerPreempted):
        self._NumAMContainerPreempted = NumAMContainerPreempted

    @property
    def MapsTotal(self):
        return self._MapsTotal

    @MapsTotal.setter
    def MapsTotal(self, MapsTotal):
        self._MapsTotal = MapsTotal

    @property
    def MapsCompleted(self):
        return self._MapsCompleted

    @MapsCompleted.setter
    def MapsCompleted(self, MapsCompleted):
        self._MapsCompleted = MapsCompleted

    @property
    def ReducesTotal(self):
        return self._ReducesTotal

    @ReducesTotal.setter
    def ReducesTotal(self, ReducesTotal):
        self._ReducesTotal = ReducesTotal

    @property
    def ReducesCompleted(self):
        return self._ReducesCompleted

    @ReducesCompleted.setter
    def ReducesCompleted(self, ReducesCompleted):
        self._ReducesCompleted = ReducesCompleted

    @property
    def AvgMapTime(self):
        return self._AvgMapTime

    @AvgMapTime.setter
    def AvgMapTime(self, AvgMapTime):
        self._AvgMapTime = AvgMapTime

    @property
    def AvgReduceTime(self):
        return self._AvgReduceTime

    @AvgReduceTime.setter
    def AvgReduceTime(self, AvgReduceTime):
        self._AvgReduceTime = AvgReduceTime

    @property
    def AvgShuffleTime(self):
        return self._AvgShuffleTime

    @AvgShuffleTime.setter
    def AvgShuffleTime(self, AvgShuffleTime):
        self._AvgShuffleTime = AvgShuffleTime

    @property
    def AvgMergeTime(self):
        return self._AvgMergeTime

    @AvgMergeTime.setter
    def AvgMergeTime(self, AvgMergeTime):
        self._AvgMergeTime = AvgMergeTime

    @property
    def FailedReduceAttempts(self):
        return self._FailedReduceAttempts

    @FailedReduceAttempts.setter
    def FailedReduceAttempts(self, FailedReduceAttempts):
        self._FailedReduceAttempts = FailedReduceAttempts

    @property
    def KilledReduceAttempts(self):
        return self._KilledReduceAttempts

    @KilledReduceAttempts.setter
    def KilledReduceAttempts(self, KilledReduceAttempts):
        self._KilledReduceAttempts = KilledReduceAttempts

    @property
    def SuccessfulReduceAttempts(self):
        return self._SuccessfulReduceAttempts

    @SuccessfulReduceAttempts.setter
    def SuccessfulReduceAttempts(self, SuccessfulReduceAttempts):
        self._SuccessfulReduceAttempts = SuccessfulReduceAttempts

    @property
    def FailedMapAttempts(self):
        return self._FailedMapAttempts

    @FailedMapAttempts.setter
    def FailedMapAttempts(self, FailedMapAttempts):
        self._FailedMapAttempts = FailedMapAttempts

    @property
    def KilledMapAttempts(self):
        return self._KilledMapAttempts

    @KilledMapAttempts.setter
    def KilledMapAttempts(self, KilledMapAttempts):
        self._KilledMapAttempts = KilledMapAttempts

    @property
    def SuccessfulMapAttempts(self):
        return self._SuccessfulMapAttempts

    @SuccessfulMapAttempts.setter
    def SuccessfulMapAttempts(self, SuccessfulMapAttempts):
        self._SuccessfulMapAttempts = SuccessfulMapAttempts

    @property
    def GcTimeMillis(self):
        return self._GcTimeMillis

    @GcTimeMillis.setter
    def GcTimeMillis(self, GcTimeMillis):
        self._GcTimeMillis = GcTimeMillis

    @property
    def VCoreMillisMaps(self):
        return self._VCoreMillisMaps

    @VCoreMillisMaps.setter
    def VCoreMillisMaps(self, VCoreMillisMaps):
        self._VCoreMillisMaps = VCoreMillisMaps

    @property
    def MbMillisMaps(self):
        return self._MbMillisMaps

    @MbMillisMaps.setter
    def MbMillisMaps(self, MbMillisMaps):
        self._MbMillisMaps = MbMillisMaps

    @property
    def VCoreMillisReduces(self):
        return self._VCoreMillisReduces

    @VCoreMillisReduces.setter
    def VCoreMillisReduces(self, VCoreMillisReduces):
        self._VCoreMillisReduces = VCoreMillisReduces

    @property
    def MbMillisReduces(self):
        return self._MbMillisReduces

    @MbMillisReduces.setter
    def MbMillisReduces(self, MbMillisReduces):
        self._MbMillisReduces = MbMillisReduces

    @property
    def TotalLaunchedMaps(self):
        return self._TotalLaunchedMaps

    @TotalLaunchedMaps.setter
    def TotalLaunchedMaps(self, TotalLaunchedMaps):
        self._TotalLaunchedMaps = TotalLaunchedMaps

    @property
    def TotalLaunchedReduces(self):
        return self._TotalLaunchedReduces

    @TotalLaunchedReduces.setter
    def TotalLaunchedReduces(self, TotalLaunchedReduces):
        self._TotalLaunchedReduces = TotalLaunchedReduces

    @property
    def MapInputRecords(self):
        return self._MapInputRecords

    @MapInputRecords.setter
    def MapInputRecords(self, MapInputRecords):
        self._MapInputRecords = MapInputRecords

    @property
    def MapOutputRecords(self):
        return self._MapOutputRecords

    @MapOutputRecords.setter
    def MapOutputRecords(self, MapOutputRecords):
        self._MapOutputRecords = MapOutputRecords

    @property
    def ReduceInputRecords(self):
        return self._ReduceInputRecords

    @ReduceInputRecords.setter
    def ReduceInputRecords(self, ReduceInputRecords):
        self._ReduceInputRecords = ReduceInputRecords

    @property
    def ReduceOutputRecords(self):
        return self._ReduceOutputRecords

    @ReduceOutputRecords.setter
    def ReduceOutputRecords(self, ReduceOutputRecords):
        self._ReduceOutputRecords = ReduceOutputRecords

    @property
    def HDFSBytesWritten(self):
        return self._HDFSBytesWritten

    @HDFSBytesWritten.setter
    def HDFSBytesWritten(self, HDFSBytesWritten):
        self._HDFSBytesWritten = HDFSBytesWritten

    @property
    def HDFSBytesRead(self):
        return self._HDFSBytesRead

    @HDFSBytesRead.setter
    def HDFSBytesRead(self, HDFSBytesRead):
        self._HDFSBytesRead = HDFSBytesRead


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._User = params.get("User")
        self._Name = params.get("Name")
        self._Queue = params.get("Queue")
        self._ApplicationType = params.get("ApplicationType")
        self._ElapsedTime = params.get("ElapsedTime")
        self._State = params.get("State")
        self._FinalStatus = params.get("FinalStatus")
        self._Progress = params.get("Progress")
        self._StartedTime = params.get("StartedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._AllocatedMB = params.get("AllocatedMB")
        self._AllocatedVCores = params.get("AllocatedVCores")
        self._RunningContainers = params.get("RunningContainers")
        self._MemorySeconds = params.get("MemorySeconds")
        self._VCoreSeconds = params.get("VCoreSeconds")
        self._QueueUsagePercentage = params.get("QueueUsagePercentage")
        self._ClusterUsagePercentage = params.get("ClusterUsagePercentage")
        self._PreemptedResourceMB = params.get("PreemptedResourceMB")
        self._PreemptedResourceVCores = params.get("PreemptedResourceVCores")
        self._NumNonAMContainerPreempted = params.get("NumNonAMContainerPreempted")
        self._NumAMContainerPreempted = params.get("NumAMContainerPreempted")
        self._MapsTotal = params.get("MapsTotal")
        self._MapsCompleted = params.get("MapsCompleted")
        self._ReducesTotal = params.get("ReducesTotal")
        self._ReducesCompleted = params.get("ReducesCompleted")
        self._AvgMapTime = params.get("AvgMapTime")
        self._AvgReduceTime = params.get("AvgReduceTime")
        self._AvgShuffleTime = params.get("AvgShuffleTime")
        self._AvgMergeTime = params.get("AvgMergeTime")
        self._FailedReduceAttempts = params.get("FailedReduceAttempts")
        self._KilledReduceAttempts = params.get("KilledReduceAttempts")
        self._SuccessfulReduceAttempts = params.get("SuccessfulReduceAttempts")
        self._FailedMapAttempts = params.get("FailedMapAttempts")
        self._KilledMapAttempts = params.get("KilledMapAttempts")
        self._SuccessfulMapAttempts = params.get("SuccessfulMapAttempts")
        self._GcTimeMillis = params.get("GcTimeMillis")
        self._VCoreMillisMaps = params.get("VCoreMillisMaps")
        self._MbMillisMaps = params.get("MbMillisMaps")
        self._VCoreMillisReduces = params.get("VCoreMillisReduces")
        self._MbMillisReduces = params.get("MbMillisReduces")
        self._TotalLaunchedMaps = params.get("TotalLaunchedMaps")
        self._TotalLaunchedReduces = params.get("TotalLaunchedReduces")
        self._MapInputRecords = params.get("MapInputRecords")
        self._MapOutputRecords = params.get("MapOutputRecords")
        self._ReduceInputRecords = params.get("ReduceInputRecords")
        self._ReduceOutputRecords = params.get("ReduceOutputRecords")
        self._HDFSBytesWritten = params.get("HDFSBytesWritten")
        self._HDFSBytesRead = params.get("HDFSBytesRead")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetailPriceResult(AbstractModel):
    """用于创建集群价格清单 不同可用区下价格详情

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _NodeDetailPrice: 不同节点的价格详情
        :type NodeDetailPrice: list of NodeDetailPriceResult
        """
        self._ZoneId = None
        self._NodeDetailPrice = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodeDetailPrice(self):
        return self._NodeDetailPrice

    @NodeDetailPrice.setter
    def NodeDetailPrice(self, NodeDetailPrice):
        self._NodeDetailPrice = NodeDetailPrice


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("NodeDetailPrice") is not None:
            self._NodeDetailPrice = []
            for item in params.get("NodeDetailPrice"):
                obj = NodeDetailPriceResult()
                obj._deserialize(item)
                self._NodeDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResourceConfiguration(AbstractModel):
    """可用区配置信息

    """

    def __init__(self):
        r"""
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.emr.v20190103.models.VirtualPrivateCloud`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _AllNodeResourceSpec: 所有节点资源的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type AllNodeResourceSpec: :class:`tencentcloud.emr.v20190103.models.AllNodeResourceSpec`
        :param _ZoneTag: 如果是单可用区，ZoneTag可以不用填， 如果是双AZ部署，第一个可用区ZoneTag选择master，第二个可用区ZoneTag选择standby，如果是三AZ部署，第一个可用区ZoneTag选择master，第二个可用区ZoneTag选择standby，第三个可用区ZoneTag选择third-party，取值范围：
  <li>master</li>
  <li>standby</li>
  <li>third-party</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneTag: str
        """
        self._VirtualPrivateCloud = None
        self._Placement = None
        self._AllNodeResourceSpec = None
        self._ZoneTag = None

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def AllNodeResourceSpec(self):
        return self._AllNodeResourceSpec

    @AllNodeResourceSpec.setter
    def AllNodeResourceSpec(self, AllNodeResourceSpec):
        self._AllNodeResourceSpec = AllNodeResourceSpec

    @property
    def ZoneTag(self):
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag


    def _deserialize(self, params):
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("AllNodeResourceSpec") is not None:
            self._AllNodeResourceSpec = AllNodeResourceSpec()
            self._AllNodeResourceSpec._deserialize(params.get("AllNodeResourceSpec"))
        self._ZoneTag = params.get("ZoneTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """可用区配置描述。

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称
        :type Zone: str
        :param _VPCSettings: 可用区VPC和子网
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _NodeNum: 可用区节点数量
        :type NodeNum: int
        """
        self._Zone = None
        self._VPCSettings = None
        self._NodeNum = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        self._NodeNum = params.get("NodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        