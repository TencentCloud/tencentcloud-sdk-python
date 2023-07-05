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


class ActiveCarrierPrivilegeNumber(AbstractModel):
    """生效运营商白名单号码

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _Caller: 主叫号码
        :type Caller: str
        :param _Callee: 被叫号码
        :type Callee: str
        :param _CreateTime: 生效unix时间戳(秒)
        :type CreateTime: int
        """
        self._SdkAppId = None
        self._Caller = None
        self._Callee = None
        self._CreateTime = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskCalleeInfo(AbstractModel):
    """外呼任务被叫信息

    """

    def __init__(self):
        r"""
        :param _Callee: 被叫号码
        :type Callee: str
        :param _State: 呼叫状态 0初始 1已接听 2未接听 3呼叫中 4待重试
        :type State: int
        :param _Sessions: 会话ID列表
        :type Sessions: list of str
        """
        self._Callee = None
        self._State = None
        self._Sessions = None

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Sessions(self):
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._State = params.get("State")
        self._Sessions = params.get("Sessions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskInfo(AbstractModel):
    """自动外呼任务列表项

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
        :type Name: str
        :param _CalleeCount: 被叫数量
        :type CalleeCount: int
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _NotBefore: 起始时间戳
        :type NotBefore: int
        :param _NotAfter: 结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NotAfter: int
        :param _IvrId: 任务使用的IvrId
        :type IvrId: int
        :param _State: 任务状态0初始 1运行中 2已完成 3结束中 4已结束
        :type State: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._Name = None
        self._CalleeCount = None
        self._Callers = None
        self._NotBefore = None
        self._NotAfter = None
        self._IvrId = None
        self._State = None
        self._TaskId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CalleeCount(self):
        return self._CalleeCount

    @CalleeCount.setter
    def CalleeCount(self, CalleeCount):
        self._CalleeCount = CalleeCount

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def NotBefore(self):
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def IvrId(self):
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CalleeCount = params.get("CalleeCount")
        self._Callers = params.get("Callers")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupRequest(AbstractModel):
    """BindNumberCallOutSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Number: 待绑定的号码
        :type Number: str
        :param _SkillGroupIds: 待绑定的技能组Id列表
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupResponse(AbstractModel):
    """BindNumberCallOutSkillGroup返回参数结构体

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


class BindStaffSkillGroupListRequest(AbstractModel):
    """BindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param _SkillGroupList: 绑定技能组列表
        :type SkillGroupList: list of int
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindStaffSkillGroupListResponse(AbstractModel):
    """BindStaffSkillGroupList返回参数结构体

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


class CallInMetrics(AbstractModel):
    """呼入实时指标

    """

    def __init__(self):
        r"""
        :param _IvrCount: IVR驻留数量
        :type IvrCount: int
        :param _QueueCount: 排队中数量
        :type QueueCount: int
        :param _RingCount: 振铃中数量
        :type RingCount: int
        :param _AcceptCount: 接通中数量
        :type AcceptCount: int
        :param _TransferOuterCount: 客服转接外线中数量
        :type TransferOuterCount: int
        :param _MaxQueueDuration: 最大排队时长
        :type MaxQueueDuration: int
        :param _AvgQueueDuration: 平均排队时长
        :type AvgQueueDuration: int
        :param _MaxRingDuration: 最大振铃时长
        :type MaxRingDuration: int
        :param _AvgRingDuration: 平均振铃时长
        :type AvgRingDuration: int
        :param _MaxAcceptDuration: 最大接通时长
        :type MaxAcceptDuration: int
        :param _AvgAcceptDuration: 平均接通时长
        :type AvgAcceptDuration: int
        """
        self._IvrCount = None
        self._QueueCount = None
        self._RingCount = None
        self._AcceptCount = None
        self._TransferOuterCount = None
        self._MaxQueueDuration = None
        self._AvgQueueDuration = None
        self._MaxRingDuration = None
        self._AvgRingDuration = None
        self._MaxAcceptDuration = None
        self._AvgAcceptDuration = None

    @property
    def IvrCount(self):
        return self._IvrCount

    @IvrCount.setter
    def IvrCount(self, IvrCount):
        self._IvrCount = IvrCount

    @property
    def QueueCount(self):
        return self._QueueCount

    @QueueCount.setter
    def QueueCount(self, QueueCount):
        self._QueueCount = QueueCount

    @property
    def RingCount(self):
        return self._RingCount

    @RingCount.setter
    def RingCount(self, RingCount):
        self._RingCount = RingCount

    @property
    def AcceptCount(self):
        return self._AcceptCount

    @AcceptCount.setter
    def AcceptCount(self, AcceptCount):
        self._AcceptCount = AcceptCount

    @property
    def TransferOuterCount(self):
        return self._TransferOuterCount

    @TransferOuterCount.setter
    def TransferOuterCount(self, TransferOuterCount):
        self._TransferOuterCount = TransferOuterCount

    @property
    def MaxQueueDuration(self):
        return self._MaxQueueDuration

    @MaxQueueDuration.setter
    def MaxQueueDuration(self, MaxQueueDuration):
        self._MaxQueueDuration = MaxQueueDuration

    @property
    def AvgQueueDuration(self):
        return self._AvgQueueDuration

    @AvgQueueDuration.setter
    def AvgQueueDuration(self, AvgQueueDuration):
        self._AvgQueueDuration = AvgQueueDuration

    @property
    def MaxRingDuration(self):
        return self._MaxRingDuration

    @MaxRingDuration.setter
    def MaxRingDuration(self, MaxRingDuration):
        self._MaxRingDuration = MaxRingDuration

    @property
    def AvgRingDuration(self):
        return self._AvgRingDuration

    @AvgRingDuration.setter
    def AvgRingDuration(self, AvgRingDuration):
        self._AvgRingDuration = AvgRingDuration

    @property
    def MaxAcceptDuration(self):
        return self._MaxAcceptDuration

    @MaxAcceptDuration.setter
    def MaxAcceptDuration(self, MaxAcceptDuration):
        self._MaxAcceptDuration = MaxAcceptDuration

    @property
    def AvgAcceptDuration(self):
        return self._AvgAcceptDuration

    @AvgAcceptDuration.setter
    def AvgAcceptDuration(self, AvgAcceptDuration):
        self._AvgAcceptDuration = AvgAcceptDuration


    def _deserialize(self, params):
        self._IvrCount = params.get("IvrCount")
        self._QueueCount = params.get("QueueCount")
        self._RingCount = params.get("RingCount")
        self._AcceptCount = params.get("AcceptCount")
        self._TransferOuterCount = params.get("TransferOuterCount")
        self._MaxQueueDuration = params.get("MaxQueueDuration")
        self._AvgQueueDuration = params.get("AvgQueueDuration")
        self._MaxRingDuration = params.get("MaxRingDuration")
        self._AvgRingDuration = params.get("AvgRingDuration")
        self._MaxAcceptDuration = params.get("MaxAcceptDuration")
        self._AvgAcceptDuration = params.get("AvgAcceptDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInNumberMetrics(AbstractModel):
    """呼入线路维度相关指标

    """

    def __init__(self):
        r"""
        :param _Number: 线路号码
        :type Number: str
        :param _Metrics: 线路相关指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _SkillGroupMetrics: 所属技能组相关指标
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        """
        self._Number = None
        self._Metrics = None
        self._SkillGroupMetrics = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def SkillGroupMetrics(self):
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics


    def _deserialize(self, params):
        self._Number = params.get("Number")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInSkillGroupMetrics(AbstractModel):
    """呼入技能组相关指标

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _Metrics: 数据指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _Name: 技能组名称
        :type Name: str
        """
        self._SkillGroupId = None
        self._Metrics = None
        self._Name = None

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CalleeAttribute(AbstractModel):
    """被叫属性

    """

    def __init__(self):
        r"""
        :param _Callee: 被叫号码
        :type Callee: str
        :param _UUI: 随路数据
        :type UUI: str
        :param _Variables: 参数
        :type Variables: list of Variable
        """
        self._Callee = None
        self._UUI = None
        self._Variables = None

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def UUI(self):
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def Variables(self):
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._UUI = params.get("UUI")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarrierPrivilegeNumberApplicant(AbstractModel):
    """运营商白名单号码申请单

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _ApplicantId: 申请单Id
        :type ApplicantId: int
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _Callees: 被叫号码列表
        :type Callees: list of str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _State: 审批状态:1 待审核、2 通过、3 拒绝
        :type State: int
        :param _CreateTime: 创建时间，unix时间戳(秒)
        :type CreateTime: int
        :param _UpdateTime: 更新时间，unix时间戳(秒)
        :type UpdateTime: int
        """
        self._SdkAppId = None
        self._ApplicantId = None
        self._Callers = None
        self._Callees = None
        self._Description = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ApplicantId(self):
        return self._ApplicantId

    @ApplicantId.setter
    def ApplicantId(self, ApplicantId):
        self._ApplicantId = ApplicantId

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ApplicantId = params.get("ApplicantId")
        self._Callers = params.get("Callers")
        self._Callees = params.get("Callees")
        self._Description = params.get("Description")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoCalloutTaskRequest(AbstractModel):
    """CreateAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _NotBefore: 任务起始时间戳，Unix 秒级时间戳
        :type NotBefore: int
        :param _Callees: 被叫号码列表
        :type Callees: list of str
        :param _Callers: 主叫号码列表
        :type Callers: list of str
        :param _IvrId: 呼叫使用的Ivr
        :type IvrId: int
        :param _Name: 任务名
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _NotAfter: 任务停止时间戳，Unix 秒级时间戳
        :type NotAfter: int
        :param _Tries: 最大尝试次数
        :type Tries: int
        :param _Variables: 自定义变量（仅高级版支持）
        :type Variables: list of Variable
        :param _UUI: UUI
        :type UUI: str
        :param _CalleeAttributes: 被叫属性
        :type CalleeAttributes: list of CalleeAttribute
        """
        self._SdkAppId = None
        self._NotBefore = None
        self._Callees = None
        self._Callers = None
        self._IvrId = None
        self._Name = None
        self._Description = None
        self._NotAfter = None
        self._Tries = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def NotBefore(self):
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def Callees(self):
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IvrId(self):
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotAfter(self):
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Tries(self):
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def Variables(self):
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._NotBefore = params.get("NotBefore")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._IvrId = params.get("IvrId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotAfter = params.get("NotAfter")
        self._Tries = params.get("Tries")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoCalloutTaskResponse(AbstractModel):
    """CreateAutoCalloutTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCCCSkillGroupRequest(AbstractModel):
    """CreateCCCSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填）
        :type SdkAppId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _SkillGroupType: 技能组类型0-电话，1-在线，3-音频，4-视频
        :type SkillGroupType: int
        :param _MaxConcurrency: 技能组接待人数上限（该技能组中1个座席可接待的人数上限）默认为1。1、若技能组类型为在线，则接待上限可设置为1及以上
2、若技能组类型为电话、音频、视频，则接待上线必须只能为1
        :type MaxConcurrency: int
        """
        self._SdkAppId = None
        self._SkillGroupName = None
        self._SkillGroupType = None
        self._MaxConcurrency = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def SkillGroupType(self):
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._SkillGroupType = params.get("SkillGroupType")
        self._MaxConcurrency = params.get("MaxConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCCSkillGroupResponse(AbstractModel):
    """CreateCCCSkillGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SkillGroupId = None
        self._RequestId = None

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._RequestId = params.get("RequestId")


class CreateCallOutSessionRequest(AbstractModel):
    """CreateCallOutSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID
        :type SdkAppId: int
        :param _UserId: 客服用户 ID，一般为客服邮箱
        :type UserId: str
        :param _Callee: 被叫号码，须带 0086 前缀
        :type Callee: str
        :param _Caller: 主叫号码（废弃，使用Callers），须带 0086 前缀
        :type Caller: str
        :param _Callers: 指定主叫号码列表，如果前面的号码失败了会自动换成下一个号码，须带 0086 前缀
        :type Callers: list of str
        :param _IsForceUseMobile: 是否强制使用手机外呼，当前只支持 true，若为 true 请确保已配置白名单
        :type IsForceUseMobile: bool
        :param _Uui: 自定义数据，长度限制 1024 字节
        :type Uui: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Callee = None
        self._Caller = None
        self._Callers = None
        self._IsForceUseMobile = None
        self._Uui = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IsForceUseMobile(self):
        return self._IsForceUseMobile

    @IsForceUseMobile.setter
    def IsForceUseMobile(self, IsForceUseMobile):
        self._IsForceUseMobile = IsForceUseMobile

    @property
    def Uui(self):
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        self._Uui = Uui


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Callee = params.get("Callee")
        self._Caller = params.get("Caller")
        self._Callers = params.get("Callers")
        self._IsForceUseMobile = params.get("IsForceUseMobile")
        self._Uui = params.get("Uui")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCallOutSessionResponse(AbstractModel):
    """CreateCallOutSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 新创建的会话 ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateCarrierPrivilegeNumberApplicantRequest(AbstractModel):
    """CreateCarrierPrivilegeNumberApplicant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId
        :type SdkAppId: int
        :param _Callers: 主叫号码，必须为实例中存在的号码，格式为0086xxxx（暂时只支持国内号码）
        :type Callers: list of str
        :param _Callees: 被叫号码，必须为实例中坐席绑定的手机号码，格式为0086xxxx（暂时只支持国内号码）
        :type Callees: list of str
        :param _Description: 描述
        :type Description: str
        """
        self._SdkAppId = None
        self._Callers = None
        self._Callees = None
        self._Description = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callers = params.get("Callers")
        self._Callees = params.get("Callees")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCarrierPrivilegeNumberApplicantResponse(AbstractModel):
    """CreateCarrierPrivilegeNumberApplicant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicantId: 申请单Id
        :type ApplicantId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicantId = None
        self._RequestId = None

    @property
    def ApplicantId(self):
        return self._ApplicantId

    @ApplicantId.setter
    def ApplicantId(self, ApplicantId):
        self._ApplicantId = ApplicantId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicantId = params.get("ApplicantId")
        self._RequestId = params.get("RequestId")


class CreateExtensionRequest(AbstractModel):
    """CreateExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _SkillGroupIds: 绑定的技能组列表
        :type SkillGroupIds: list of int non-negative
        :param _Relation: 绑定的坐席邮箱
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExtensionResponse(AbstractModel):
    """CreateExtension返回参数结构体

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


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SeatUserId: 座席账号。
        :type SeatUserId: str
        """
        self._SdkAppId = None
        self._SeatUserId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SeatUserId(self):
        return self._SeatUserId

    @SeatUserId.setter
    def SeatUserId(self, SeatUserId):
        self._SeatUserId = SeatUserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SeatUserId = params.get("SeatUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSDKLoginTokenResponse(AbstractModel):
    """CreateSDKLoginToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: SDK 登录 Token。
        :type Token: str
        :param _ExpiredTime: 过期时间戳，Unix 时间戳。
        :type ExpiredTime: int
        :param _SdkURL: SDK 加载路径会随着 SDK 的发布而变动。
        :type SdkURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiredTime = None
        self._SdkURL = None
        self._RequestId = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SdkURL(self):
        return self._SdkURL

    @SdkURL.setter
    def SdkURL(self, SdkURL):
        self._SdkURL = SdkURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SdkURL = params.get("SdkURL")
        self._RequestId = params.get("RequestId")


class CreateStaffRequest(AbstractModel):
    """CreateStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Staffs: 客服信息，个数不超过 10
        :type Staffs: list of SeatUserInfo
        :param _SendPassword: 是否发送密码邮件，默认true
        :type SendPassword: bool
        """
        self._SdkAppId = None
        self._Staffs = None
        self._SendPassword = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Staffs(self):
        return self._Staffs

    @Staffs.setter
    def Staffs(self, Staffs):
        self._Staffs = Staffs

    @property
    def SendPassword(self):
        return self._SendPassword

    @SendPassword.setter
    def SendPassword(self, SendPassword):
        self._SendPassword = SendPassword


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Staffs") is not None:
            self._Staffs = []
            for item in params.get("Staffs"):
                obj = SeatUserInfo()
                obj._deserialize(item)
                self._Staffs.append(obj)
        self._SendPassword = params.get("SendPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaffResponse(AbstractModel):
    """CreateStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorStaffList: 错误坐席列表及错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorStaffList: list of ErrStaffItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorStaffList = None
        self._RequestId = None

    @property
    def ErrorStaffList(self):
        return self._ErrorStaffList

    @ErrorStaffList.setter
    def ErrorStaffList(self, ErrorStaffList):
        self._ErrorStaffList = ErrorStaffList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorStaffList") is not None:
            self._ErrorStaffList = []
            for item in params.get("ErrorStaffList"):
                obj = ErrStaffItem()
                obj._deserialize(item)
                self._ErrorStaffList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateUserSigRequest(AbstractModel):
    """CreateUserSig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Uid: 用户 ID
        :type Uid: str
        :param _ExpiredTime: 有效期，单位秒，不超过 1 小时
        :type ExpiredTime: int
        :param _ClientData: 用户签名数据
        :type ClientData: str
        """
        self._SdkAppId = None
        self._Uid = None
        self._ExpiredTime = None
        self._ClientData = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def ClientData(self):
        return self._ClientData

    @ClientData.setter
    def ClientData(self, ClientData):
        self._ClientData = ClientData


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Uid = params.get("Uid")
        self._ExpiredTime = params.get("ExpiredTime")
        self._ClientData = params.get("ClientData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSigResponse(AbstractModel):
    """CreateUserSig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserSig: 签名结果
        :type UserSig: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserSig = None
        self._RequestId = None

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserSig = params.get("UserSig")
        self._RequestId = params.get("RequestId")


class DeleteExtensionRequest(AbstractModel):
    """DeleteExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExtensionResponse(AbstractModel):
    """DeleteExtension返回参数结构体

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


class DeleteStaffRequest(AbstractModel):
    """DeleteStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffList: 待删除客服邮箱列表
        :type StaffList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStaffResponse(AbstractModel):
    """DeleteStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineStaffList: 无法删除的状态为在线的客服列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineStaffList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OnlineStaffList = None
        self._RequestId = None

    @property
    def OnlineStaffList(self):
        return self._OnlineStaffList

    @OnlineStaffList.setter
    def OnlineStaffList(self, OnlineStaffList):
        self._OnlineStaffList = OnlineStaffList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OnlineStaffList = params.get("OnlineStaffList")
        self._RequestId = params.get("RequestId")


class DescribeActiveCarrierPrivilegeNumberRequest(AbstractModel):
    """DescribeActiveCarrierPrivilegeNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _PageNumber: 默认0
        :type PageNumber: int
        :param _PageSize: 默认10，最大100
        :type PageSize: int
        :param _Filters: 筛选条件 Name支持PhoneNumber(按号码模糊查找)
        :type Filters: list of Filter
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
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
        


class DescribeActiveCarrierPrivilegeNumberResponse(AbstractModel):
    """DescribeActiveCarrierPrivilegeNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _ActiveCarrierPrivilegeNumbers: 生效列表
        :type ActiveCarrierPrivilegeNumbers: list of ActiveCarrierPrivilegeNumber
        :param _PendingApplicantIds: 待审核单号
        :type PendingApplicantIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ActiveCarrierPrivilegeNumbers = None
        self._PendingApplicantIds = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ActiveCarrierPrivilegeNumbers(self):
        return self._ActiveCarrierPrivilegeNumbers

    @ActiveCarrierPrivilegeNumbers.setter
    def ActiveCarrierPrivilegeNumbers(self, ActiveCarrierPrivilegeNumbers):
        self._ActiveCarrierPrivilegeNumbers = ActiveCarrierPrivilegeNumbers

    @property
    def PendingApplicantIds(self):
        return self._PendingApplicantIds

    @PendingApplicantIds.setter
    def PendingApplicantIds(self, PendingApplicantIds):
        self._PendingApplicantIds = PendingApplicantIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ActiveCarrierPrivilegeNumbers") is not None:
            self._ActiveCarrierPrivilegeNumbers = []
            for item in params.get("ActiveCarrierPrivilegeNumbers"):
                obj = ActiveCarrierPrivilegeNumber()
                obj._deserialize(item)
                self._ActiveCarrierPrivilegeNumbers.append(obj)
        self._PendingApplicantIds = params.get("PendingApplicantIds")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTaskRequest(AbstractModel):
    """DescribeAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoCalloutTaskResponse(AbstractModel):
    """DescribeAutoCalloutTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _NotBefore: 任务起始时间戳
        :type NotBefore: int
        :param _NotAfter: 任务结束时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NotAfter: int
        :param _Callers: 主叫列表
        :type Callers: list of str
        :param _Callees: 被叫信息列表
        :type Callees: list of AutoCalloutTaskCalleeInfo
        :param _IvrId: 任务使用的IvrId
        :type IvrId: int
        :param _State: 任务状态 0初始 1运行中 2已完成 3结束中 4已终止
        :type State: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._NotBefore = None
        self._NotAfter = None
        self._Callers = None
        self._Callees = None
        self._IvrId = None
        self._State = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotBefore(self):
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Callers(self):
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def IvrId(self):
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._Callers = params.get("Callers")
        if params.get("Callees") is not None:
            self._Callees = []
            for item in params.get("Callees"):
                obj = AutoCalloutTaskCalleeInfo()
                obj._deserialize(item)
                self._Callees.append(obj)
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTasksRequest(AbstractModel):
    """DescribeAutoCalloutTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoCalloutTasksResponse(AbstractModel):
    """DescribeAutoCalloutTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Tasks: 任务列表
        :type Tasks: list of AutoCalloutTaskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AutoCalloutTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCCBuyInfoListRequest(AbstractModel):
    """DescribeCCCBuyInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppIds: 应用ID列表，不传时查询所有应用
        :type SdkAppIds: list of int
        """
        self._SdkAppIds = None

    @property
    def SdkAppIds(self):
        return self._SdkAppIds

    @SdkAppIds.setter
    def SdkAppIds(self, SdkAppIds):
        self._SdkAppIds = SdkAppIds


    def _deserialize(self, params):
        self._SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCCBuyInfoListResponse(AbstractModel):
    """DescribeCCCBuyInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 应用总数
        :type TotalCount: int
        :param _SdkAppIdBuyList: 应用购买信息列表
        :type SdkAppIdBuyList: list of SdkAppIdBuyInfo
        :param _PackageBuyList: 套餐包购买信息列表
        :type PackageBuyList: list of PackageBuyInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SdkAppIdBuyList = None
        self._PackageBuyList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SdkAppIdBuyList(self):
        return self._SdkAppIdBuyList

    @SdkAppIdBuyList.setter
    def SdkAppIdBuyList(self, SdkAppIdBuyList):
        self._SdkAppIdBuyList = SdkAppIdBuyList

    @property
    def PackageBuyList(self):
        return self._PackageBuyList

    @PackageBuyList.setter
    def PackageBuyList(self, PackageBuyList):
        self._PackageBuyList = PackageBuyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SdkAppIdBuyList") is not None:
            self._SdkAppIdBuyList = []
            for item in params.get("SdkAppIdBuyList"):
                obj = SdkAppIdBuyInfo()
                obj._deserialize(item)
                self._SdkAppIdBuyList.append(obj)
        if params.get("PackageBuyList") is not None:
            self._PackageBuyList = []
            for item in params.get("PackageBuyList"):
                obj = PackageBuyInfo()
                obj._deserialize(item)
                self._PackageBuyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallInMetricsRequest(AbstractModel):
    """DescribeCallInMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _EnabledSkillGroup: 是否返回技能组维度信息，默认“是”
        :type EnabledSkillGroup: bool
        :param _EnabledNumber: 是否返回线路维度信息，默认“否”
        :type EnabledNumber: bool
        :param _GroupIdList: 筛选技能组列表
        :type GroupIdList: list of int
        """
        self._SdkAppId = None
        self._EnabledSkillGroup = None
        self._EnabledNumber = None
        self._GroupIdList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def EnabledSkillGroup(self):
        return self._EnabledSkillGroup

    @EnabledSkillGroup.setter
    def EnabledSkillGroup(self, EnabledSkillGroup):
        self._EnabledSkillGroup = EnabledSkillGroup

    @property
    def EnabledNumber(self):
        return self._EnabledNumber

    @EnabledNumber.setter
    def EnabledNumber(self, EnabledNumber):
        self._EnabledNumber = EnabledNumber

    @property
    def GroupIdList(self):
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._EnabledSkillGroup = params.get("EnabledSkillGroup")
        self._EnabledNumber = params.get("EnabledNumber")
        self._GroupIdList = params.get("GroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallInMetricsResponse(AbstractModel):
    """DescribeCallInMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _TotalMetrics: 总体指标
        :type TotalMetrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _NumberMetrics: 线路维度指标
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberMetrics: list of CallInNumberMetrics
        :param _SkillGroupMetrics: 技能组维度指标
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Timestamp = None
        self._TotalMetrics = None
        self._NumberMetrics = None
        self._SkillGroupMetrics = None
        self._RequestId = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def TotalMetrics(self):
        return self._TotalMetrics

    @TotalMetrics.setter
    def TotalMetrics(self, TotalMetrics):
        self._TotalMetrics = TotalMetrics

    @property
    def NumberMetrics(self):
        return self._NumberMetrics

    @NumberMetrics.setter
    def NumberMetrics(self, NumberMetrics):
        self._NumberMetrics = NumberMetrics

    @property
    def SkillGroupMetrics(self):
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("TotalMetrics") is not None:
            self._TotalMetrics = CallInMetrics()
            self._TotalMetrics._deserialize(params.get("TotalMetrics"))
        if params.get("NumberMetrics") is not None:
            self._NumberMetrics = []
            for item in params.get("NumberMetrics"):
                obj = CallInNumberMetrics()
                obj._deserialize(item)
                self._NumberMetrics.append(obj)
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCarrierPrivilegeNumberApplicantsRequest(AbstractModel):
    """DescribeCarrierPrivilegeNumberApplicants请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例Id
        :type SdkAppId: int
        :param _PageNumber: 默认0，从0开始
        :type PageNumber: int
        :param _PageSize: 默认10，最大100
        :type PageSize: int
        :param _Filters: 筛选条件,Name支持ApplicantId,PhoneNumber(按号码模糊查找)
        :type Filters: list of Filter
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
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
        


class DescribeCarrierPrivilegeNumberApplicantsResponse(AbstractModel):
    """DescribeCarrierPrivilegeNumberApplicants返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 筛选出的总申请单数量
        :type TotalCount: int
        :param _Applicants: 申请单列表
        :type Applicants: list of CarrierPrivilegeNumberApplicant
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Applicants = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Applicants(self):
        return self._Applicants

    @Applicants.setter
    def Applicants(self, Applicants):
        self._Applicants = Applicants

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Applicants") is not None:
            self._Applicants = []
            for item in params.get("Applicants"):
                obj = CarrierPrivilegeNumberApplicant()
                obj._deserialize(item)
                self._Applicants.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChatMessagesRequest(AbstractModel):
    """DescribeChatMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _CdrId: 服务记录ID（废弃）
        :type CdrId: str
        :param _Limit: 返回记录条数，最大为100 默认20
        :type Limit: int
        :param _Offset: 返回记录偏移，默认为 0
        :type Offset: int
        :param _Order: 1为从早到晚，2为从晚到早，默认为2
        :type Order: int
        :param _SessionId: 服务记录 SessionID（必填）
        :type SessionId: str
        """
        self._InstanceId = None
        self._SdkAppId = None
        self._CdrId = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._SessionId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CdrId(self):
        return self._CdrId

    @CdrId.setter
    def CdrId(self, CdrId):
        self._CdrId = CdrId

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SdkAppId = params.get("SdkAppId")
        self._CdrId = params.get("CdrId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChatMessagesResponse(AbstractModel):
    """DescribeChatMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Messages: 消息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Messages: list of MessageBody
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Messages = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageBody()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtensionRequest(AbstractModel):
    """DescribeExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionResponse(AbstractModel):
    """DescribeExtension返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionDomain: 域名
        :type ExtensionDomain: str
        :param _Password: 注册密码
        :type Password: str
        :param _OutboundProxy: 代理服务器地址
        :type OutboundProxy: str
        :param _Transport: 传输协议
        :type Transport: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExtensionId = None
        self._ExtensionDomain = None
        self._Password = None
        self._OutboundProxy = None
        self._Transport = None
        self._RequestId = None

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionDomain(self):
        return self._ExtensionDomain

    @ExtensionDomain.setter
    def ExtensionDomain(self, ExtensionDomain):
        self._ExtensionDomain = ExtensionDomain

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def OutboundProxy(self):
        return self._OutboundProxy

    @OutboundProxy.setter
    def OutboundProxy(self, OutboundProxy):
        self._OutboundProxy = OutboundProxy

    @property
    def Transport(self):
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionDomain = params.get("ExtensionDomain")
        self._Password = params.get("Password")
        self._OutboundProxy = params.get("OutboundProxy")
        self._Transport = params.get("Transport")
        self._RequestId = params.get("RequestId")


class DescribeExtensionsRequest(AbstractModel):
    """DescribeExtensions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _PageNumber: 分页页号（从0开始）
        :type PageNumber: int
        :param _ExtensionIds: 筛选分机号列表
        :type ExtensionIds: list of str
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _FuzzingKeyWord: 模糊查询字段（模糊查询分机号、分机名称、坐席邮箱、坐席名称）
        :type FuzzingKeyWord: str
        :param _IsNeedStatus: 是否需要返回话机当前状态
        :type IsNeedStatus: bool
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._ExtensionIds = None
        self._PageSize = None
        self._FuzzingKeyWord = None
        self._IsNeedStatus = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def ExtensionIds(self):
        return self._ExtensionIds

    @ExtensionIds.setter
    def ExtensionIds(self, ExtensionIds):
        self._ExtensionIds = ExtensionIds

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FuzzingKeyWord(self):
        return self._FuzzingKeyWord

    @FuzzingKeyWord.setter
    def FuzzingKeyWord(self, FuzzingKeyWord):
        self._FuzzingKeyWord = FuzzingKeyWord

    @property
    def IsNeedStatus(self):
        return self._IsNeedStatus

    @IsNeedStatus.setter
    def IsNeedStatus(self, IsNeedStatus):
        self._IsNeedStatus = IsNeedStatus


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._ExtensionIds = params.get("ExtensionIds")
        self._PageSize = params.get("PageSize")
        self._FuzzingKeyWord = params.get("FuzzingKeyWord")
        self._IsNeedStatus = params.get("IsNeedStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionsResponse(AbstractModel):
    """DescribeExtensions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询总数
        :type Total: int
        :param _ExtensionList: 话机信息列表
        :type ExtensionList: list of ExtensionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ExtensionList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ExtensionList(self):
        return self._ExtensionList

    @ExtensionList.setter
    def ExtensionList(self, ExtensionList):
        self._ExtensionList = ExtensionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ExtensionList") is not None:
            self._ExtensionList = []
            for item in params.get("ExtensionList"):
                obj = ExtensionInfo()
                obj._deserialize(item)
                self._ExtensionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIMCdrsRequest(AbstractModel):
    """DescribeIMCdrs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimestamp: 起始时间（必填），Unix 秒级时间戳
        :type StartTimestamp: int
        :param _EndTimestamp: 结束时间（必填），Unix 秒级时间戳
        :type EndTimestamp: int
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Limit: 返回记录条数，最大为100默认20
        :type Limit: int
        :param _Offset: 返回记录偏移，默认为 0
        :type Offset: int
        :param _Type: 1为全媒体，2为文本客服，不填则查询全部
        :type Type: int
        """
        self._StartTimestamp = None
        self._EndTimestamp = None
        self._InstanceId = None
        self._SdkAppId = None
        self._Limit = None
        self._Offset = None
        self._Type = None

    @property
    def StartTimestamp(self):
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def EndTimestamp(self):
        return self._EndTimestamp

    @EndTimestamp.setter
    def EndTimestamp(self, EndTimestamp):
        self._EndTimestamp = EndTimestamp

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._StartTimestamp = params.get("StartTimestamp")
        self._EndTimestamp = params.get("EndTimestamp")
        self._InstanceId = params.get("InstanceId")
        self._SdkAppId = params.get("SdkAppId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIMCdrsResponse(AbstractModel):
    """DescribeIMCdrs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _IMCdrs: 服务记录列表
        :type IMCdrs: list of IMCdrInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IMCdrs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IMCdrs(self):
        return self._IMCdrs

    @IMCdrs.setter
    def IMCdrs(self, IMCdrs):
        self._IMCdrs = IMCdrs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IMCdrs") is not None:
            self._IMCdrs = []
            for item in params.get("IMCdrs"):
                obj = IMCdrInfo()
                obj._deserialize(item)
                self._IMCdrs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNumbersRequest(AbstractModel):
    """DescribeNumbers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageNumber: 页数，从0开始
        :type PageNumber: int
        :param _PageSize: 分页大小，默认20
        :type PageSize: int
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNumbersResponse(AbstractModel):
    """DescribeNumbers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Numbers: 号码列表
        :type Numbers: list of NumberInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Numbers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Numbers(self):
        return self._Numbers

    @Numbers.setter
    def Numbers(self, Numbers):
        self._Numbers = Numbers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Numbers") is not None:
            self._Numbers = []
            for item in params.get("Numbers"):
                obj = NumberInfo()
                obj._deserialize(item)
                self._Numbers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePSTNActiveSessionListRequest(AbstractModel):
    """DescribePSTNActiveSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Offset: 数据偏移
        :type Offset: int
        :param _Limit: 返回的数据条数，最大 25
        :type Limit: int
        """
        self._SdkAppId = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

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
        self._SdkAppId = params.get("SdkAppId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePSTNActiveSessionListResponse(AbstractModel):
    """DescribePSTNActiveSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 列表总条数
        :type Total: int
        :param _Sessions: 列表内容
        :type Sessions: list of PSTNSessionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Sessions = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sessions(self):
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = PSTNSessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProtectedTelCdrRequest(AbstractModel):
    """DescribeProtectedTelCdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 秒级时间戳
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 秒级时间戳
        :type EndTimeStamp: int
        :param _SdkAppId: 应用 ID，可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def StartTimeStamp(self):
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectedTelCdrResponse(AbstractModel):
    """DescribeProtectedTelCdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 话单记录总数
        :type TotalCount: int
        :param _TelCdrs: 话单记录
        :type TelCdrs: list of TelCdrInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        self._TelCdrs = TelCdrs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSkillGroupInfoListRequest(AbstractModel):
    """DescribeSkillGroupInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _SkillGroupId: 技能组ID，查询单个技能组时使用
        :type SkillGroupId: int
        :param _ModifiedTime: 查询修改时间大于等于ModifiedTime的技能组时使用
        :type ModifiedTime: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._SkillGroupId = None
        self._ModifiedTime = None
        self._SkillGroupName = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupName = params.get("SkillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillGroupInfoListResponse(AbstractModel):
    """DescribeSkillGroupInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 技能组总数
        :type TotalCount: int
        :param _SkillGroupList: 技能组信息列表
        :type SkillGroupList: list of SkillGroupInfoItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SkillGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SkillGroupList(self):
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupInfoItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffInfoListRequest(AbstractModel):
    """DescribeStaffInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸，上限 9999
        :type PageSize: int
        :param _PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param _StaffMail: 坐席账号，查询单个坐席时使用
        :type StaffMail: str
        :param _ModifiedTime: 查询修改时间大于等于ModifiedTime的坐席时使用
        :type ModifiedTime: int
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._StaffMail = None
        self._ModifiedTime = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def StaffMail(self):
        return self._StaffMail

    @StaffMail.setter
    def StaffMail(self, StaffMail):
        self._StaffMail = StaffMail

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._StaffMail = params.get("StaffMail")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffInfoListResponse(AbstractModel):
    """DescribeStaffInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 坐席用户总数
        :type TotalCount: int
        :param _StaffList: 坐席用户信息列表
        :type StaffList: list of StaffInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._StaffList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StaffList(self):
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StaffList") is not None:
            self._StaffList = []
            for item in params.get("StaffList"):
                obj = StaffInfo()
                obj._deserialize(item)
                self._StaffList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffStatusMetricsRequest(AbstractModel):
    """DescribeStaffStatusMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffList: 筛选坐席列表，默认不传返回全部坐席信息
        :type StaffList: list of str
        :param _GroupIdList: 筛选技能组ID列表
        :type GroupIdList: list of int
        :param _StatusList: 筛选坐席状态列表
        :type StatusList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None
        self._GroupIdList = None
        self._StatusList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

    @property
    def GroupIdList(self):
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        self._GroupIdList = params.get("GroupIdList")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffStatusMetricsResponse(AbstractModel):
    """DescribeStaffStatusMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 坐席状态实时信息
        :type Metrics: list of StaffStatusMetrics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = StaffStatusMetrics()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 时间戳
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 时间戳，查询时间范围最大为90天
        :type EndTimeStamp: int
        :param _SdkAppIdList: 应用ID列表，多个ID时，返回值为多个ID使用总和
        :type SdkAppIdList: list of int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppIdList = None

    @property
    def StartTimeStamp(self):
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppIdList(self):
        return self._SdkAppIdList

    @SdkAppIdList.setter
    def SdkAppIdList(self, SdkAppIdList):
        self._SdkAppIdList = SdkAppIdList


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppIdList = params.get("SdkAppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCallInfoResponse(AbstractModel):
    """DescribeTelCallInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TelCallOutCount: 呼出套餐包消耗分钟数
        :type TelCallOutCount: int
        :param _TelCallInCount: 呼入套餐包消耗分钟数
        :type TelCallInCount: int
        :param _SeatUsedCount: 坐席使用统计个数
        :type SeatUsedCount: int
        :param _VoipCallInCount: 音频套餐包消耗分钟数
        :type VoipCallInCount: int
        :param _AsrOfflineCount: 离线语音转文字套餐包消耗分钟数
        :type AsrOfflineCount: int
        :param _AsrRealtimeCount: 实时语音转文字套餐包消耗分钟数
        :type AsrRealtimeCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TelCallOutCount = None
        self._TelCallInCount = None
        self._SeatUsedCount = None
        self._VoipCallInCount = None
        self._AsrOfflineCount = None
        self._AsrRealtimeCount = None
        self._RequestId = None

    @property
    def TelCallOutCount(self):
        return self._TelCallOutCount

    @TelCallOutCount.setter
    def TelCallOutCount(self, TelCallOutCount):
        self._TelCallOutCount = TelCallOutCount

    @property
    def TelCallInCount(self):
        return self._TelCallInCount

    @TelCallInCount.setter
    def TelCallInCount(self, TelCallInCount):
        self._TelCallInCount = TelCallInCount

    @property
    def SeatUsedCount(self):
        return self._SeatUsedCount

    @SeatUsedCount.setter
    def SeatUsedCount(self, SeatUsedCount):
        self._SeatUsedCount = SeatUsedCount

    @property
    def VoipCallInCount(self):
        return self._VoipCallInCount

    @VoipCallInCount.setter
    def VoipCallInCount(self, VoipCallInCount):
        self._VoipCallInCount = VoipCallInCount

    @property
    def AsrOfflineCount(self):
        return self._AsrOfflineCount

    @AsrOfflineCount.setter
    def AsrOfflineCount(self, AsrOfflineCount):
        self._AsrOfflineCount = AsrOfflineCount

    @property
    def AsrRealtimeCount(self):
        return self._AsrRealtimeCount

    @AsrRealtimeCount.setter
    def AsrRealtimeCount(self, AsrRealtimeCount):
        self._AsrRealtimeCount = AsrRealtimeCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TelCallOutCount = params.get("TelCallOutCount")
        self._TelCallInCount = params.get("TelCallInCount")
        self._SeatUsedCount = params.get("SeatUsedCount")
        self._VoipCallInCount = params.get("VoipCallInCount")
        self._AsrOfflineCount = params.get("AsrOfflineCount")
        self._AsrRealtimeCount = params.get("AsrRealtimeCount")
        self._RequestId = params.get("RequestId")


class DescribeTelCdrRequest(AbstractModel):
    """DescribeTelCdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 起始时间戳，Unix 秒级时间戳
        :type StartTimeStamp: int
        :param _EndTimeStamp: 结束时间戳，Unix 秒级时间戳
        :type EndTimeStamp: int
        :param _InstanceId: 实例 ID（废弃）
        :type InstanceId: int
        :param _Limit: 返回数据条数，上限（废弃）
        :type Limit: int
        :param _Offset: 偏移（废弃）
        :type Offset: int
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _PageSize: 分页尺寸（必填），上限 100
        :type PageSize: int
        :param _PageNumber: 分页页码（必填），从 0 开始
        :type PageNumber: int
        :param _Phones: 按手机号筛选
        :type Phones: list of str
        :param _SessionIds: 按SessionId筛选
        :type SessionIds: list of str
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._Phones = None
        self._SessionIds = None

    @property
    def StartTimeStamp(self):
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Phones(self):
        return self._Phones

    @Phones.setter
    def Phones(self, Phones):
        self._Phones = Phones

    @property
    def SessionIds(self):
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Phones = params.get("Phones")
        self._SessionIds = params.get("SessionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCdrResponse(AbstractModel):
    """DescribeTelCdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 话单记录总数
        :type TotalCount: int
        :param _TelCdrs: 话单记录
        :type TelCdrs: list of TelCdrInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        self._TelCdrs = TelCdrs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelSessionRequest(AbstractModel):
    """DescribeTelSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _SessionId: 会话 ID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelSessionResponse(AbstractModel):
    """DescribeTelSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: 会话信息
        :type Session: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self._Session = PSTNSession()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DisableCCCPhoneNumberRequest(AbstractModel):
    """DisableCCCPhoneNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumbers: 号码列表，0086开头
        :type PhoneNumbers: list of str
        :param _Disabled: 停用开关，0启用 1停用
        :type Disabled: int
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        """
        self._PhoneNumbers = None
        self._Disabled = None
        self._SdkAppId = None

    @property
    def PhoneNumbers(self):
        return self._PhoneNumbers

    @PhoneNumbers.setter
    def PhoneNumbers(self, PhoneNumbers):
        self._PhoneNumbers = PhoneNumbers

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._PhoneNumbers = params.get("PhoneNumbers")
        self._Disabled = params.get("Disabled")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCCCPhoneNumberResponse(AbstractModel):
    """DisableCCCPhoneNumber返回参数结构体

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


class ErrStaffItem(AbstractModel):
    """批量添加客服时，返回出错客服的信息

    """

    def __init__(self):
        r"""
        :param _StaffEmail: 坐席邮箱地址
        :type StaffEmail: str
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误描述
        :type Message: str
        """
        self._StaffEmail = None
        self._Code = None
        self._Message = None

    @property
    def StaffEmail(self):
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._StaffEmail = params.get("StaffEmail")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionInfo(AbstractModel):
    """话机信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 实例ID
        :type SdkAppId: int
        :param _FullExtensionId: 分机全名
        :type FullExtensionId: str
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _SkillGroupId: 所属技能组列表
        :type SkillGroupId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ModifyTime: 最后修改时间
        :type ModifyTime: int
        :param _Status: 话机状态(0 离线、100 空闲、200忙碌）
        :type Status: int
        :param _Register: 是否注册
        :type Register: bool
        :param _Relation: 绑定坐席邮箱
        :type Relation: str
        :param _RelationName: 绑定坐席名称
        :type RelationName: str
        """
        self._SdkAppId = None
        self._FullExtensionId = None
        self._ExtensionId = None
        self._SkillGroupId = None
        self._ExtensionName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Status = None
        self._Register = None
        self._Relation = None
        self._RelationName = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def FullExtensionId(self):
        return self._FullExtensionId

    @FullExtensionId.setter
    def FullExtensionId(self, FullExtensionId):
        self._FullExtensionId = FullExtensionId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ExtensionName(self):
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Register(self):
        return self._Register

    @Register.setter
    def Register(self, Register):
        self._Register = Register

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def RelationName(self):
        return self._RelationName

    @RelationName.setter
    def RelationName(self, RelationName):
        self._RelationName = RelationName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._FullExtensionId = params.get("FullExtensionId")
        self._ExtensionId = params.get("ExtensionId")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ExtensionName = params.get("ExtensionName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Status = params.get("Status")
        self._Register = params.get("Register")
        self._Relation = params.get("Relation")
        self._RelationName = params.get("RelationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """筛选条件

    """

    def __init__(self):
        r"""
        :param _Name: 筛选字段名
        :type Name: str
        :param _Values: 筛选条件值
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
        


class HangUpCallRequest(AbstractModel):
    """HangUpCall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HangUpCallResponse(AbstractModel):
    """HangUpCall返回参数结构体

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


class IMCdrInfo(AbstractModel):
    """文本会话服务记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 服务记录ID
        :type Id: str
        :param _Duration: 服务时长秒数
        :type Duration: int
        :param _EndStatus: 结束状态
0 异常结束
1 正常结束
3 无坐席在线
17 坐席放弃接听
100 黑名单
101 坐席手动转接
102 IVR阶段放弃
108 用户超时自动结束
        :type EndStatus: int
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _Type: 服务类型 1为全媒体，2为文本客服
        :type Type: int
        :param _StaffId: 客服ID
        :type StaffId: str
        :param _Timestamp: 服务时间戳
        :type Timestamp: int
        :param _SessionId: 会话ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _SkillGroupId: 技能组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupId: str
        :param _SkillGroupName: 技能组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupName: str
        :param _Satisfaction: 满意度
注意：此字段可能返回 null，表示取不到有效值。
        :type Satisfaction: :class:`tencentcloud.ccc.v20200210.models.IMSatisfaction`
        """
        self._Id = None
        self._Duration = None
        self._EndStatus = None
        self._Nickname = None
        self._Type = None
        self._StaffId = None
        self._Timestamp = None
        self._SessionId = None
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Satisfaction = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndStatus(self):
        return self._EndStatus

    @EndStatus.setter
    def EndStatus(self, EndStatus):
        self._EndStatus = EndStatus

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StaffId(self):
        return self._StaffId

    @StaffId.setter
    def StaffId(self, StaffId):
        self._StaffId = StaffId

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Satisfaction(self):
        return self._Satisfaction

    @Satisfaction.setter
    def Satisfaction(self, Satisfaction):
        self._Satisfaction = Satisfaction


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Duration = params.get("Duration")
        self._EndStatus = params.get("EndStatus")
        self._Nickname = params.get("Nickname")
        self._Type = params.get("Type")
        self._StaffId = params.get("StaffId")
        self._Timestamp = params.get("Timestamp")
        self._SessionId = params.get("SessionId")
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        if params.get("Satisfaction") is not None:
            self._Satisfaction = IMSatisfaction()
            self._Satisfaction._deserialize(params.get("Satisfaction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IMSatisfaction(AbstractModel):
    """IM满意度

    """

    def __init__(self):
        r"""
        :param _Id: 满意度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Label: 满意度标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        """
        self._Id = None
        self._Label = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IVRKeyPressedElement(AbstractModel):
    """ivr 按键信息

    """

    def __init__(self):
        r"""
        :param _Key: 按键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Label: 按键关联的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        """
        self._Key = None
        self._Label = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """单条消息

    """

    def __init__(self):
        r"""
        :param _Type: 消息类型
        :type Type: str
        :param _Content: 消息内容
        :type Content: str
        """
        self._Type = None
        self._Content = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageBody(AbstractModel):
    """聊天消息

    """

    def __init__(self):
        r"""
        :param _Timestamp: 消息时间戳
        :type Timestamp: int
        :param _From: 发消息的用户ID
        :type From: str
        :param _Messages: 消息列表
        :type Messages: list of Message
        """
        self._Timestamp = None
        self._From = None
        self._Messages = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._From = params.get("From")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtensionRequest(AbstractModel):
    """ModifyExtension请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        :param _ExtensionName: 分机名称
        :type ExtensionName: str
        :param _SkillGroupIds: 所属技能组列表
        :type SkillGroupIds: list of int
        :param _Relation: 绑定坐席邮箱账号
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtensionResponse(AbstractModel):
    """ModifyExtension返回参数结构体

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


class ModifyStaffRequest(AbstractModel):
    """ModifyStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _Email: 座席账户
        :type Email: str
        :param _Name: 座席名称
        :type Name: str
        :param _Phone: 座席手机号（带0086前缀,示例：008618011111111）
        :type Phone: str
        :param _Nick: 座席昵称
        :type Nick: str
        :param _SkillGroupIds: 绑定技能组ID列表
        :type SkillGroupIds: list of int
        :param _UseMobileCallOut: 是否开启手机外呼开关
        :type UseMobileCallOut: bool
        :param _UseMobileAccept: 手机接听模式 0 - 关闭 | 1 - 仅离线 | 2 - 始终
        :type UseMobileAccept: int
        """
        self._SdkAppId = None
        self._Email = None
        self._Name = None
        self._Phone = None
        self._Nick = None
        self._SkillGroupIds = None
        self._UseMobileCallOut = None
        self._UseMobileAccept = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def SkillGroupIds(self):
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def UseMobileCallOut(self):
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def UseMobileAccept(self):
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Email = params.get("Email")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._UseMobileAccept = params.get("UseMobileAccept")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStaffResponse(AbstractModel):
    """ModifyStaff返回参数结构体

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


class NumberInfo(AbstractModel):
    """号码信息

    """

    def __init__(self):
        r"""
        :param _Number: 号码
        :type Number: str
        :param _CallOutSkillGroupIds: 绑定的外呼技能组
        :type CallOutSkillGroupIds: list of int non-negative
        """
        self._Number = None
        self._CallOutSkillGroupIds = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def CallOutSkillGroupIds(self):
        return self._CallOutSkillGroupIds

    @CallOutSkillGroupIds.setter
    def CallOutSkillGroupIds(self, CallOutSkillGroupIds):
        self._CallOutSkillGroupIds = CallOutSkillGroupIds


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._CallOutSkillGroupIds = params.get("CallOutSkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSession(AbstractModel):
    """PSTN 会话类型。

    """

    def __init__(self):
        r"""
        :param _SessionID: 会话 ID
        :type SessionID: str
        :param _RoomID: 会话临时房间 ID
        :type RoomID: str
        :param _Caller: 主叫
        :type Caller: str
        :param _Callee: 被叫
        :type Callee: str
        :param _StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: int
        :param _RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: int
        :param _StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param _StaffNumber: 坐席工号
        :type StaffNumber: str
        :param _SessionStatus: 会话状态
ringing 振铃中
seatJoining  等待坐席接听
inProgress 进行中
finished 已完成
        :type SessionStatus: str
        :param _Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param _OutBoundCaller: 转外线使用的号码（转外线主叫）
        :type OutBoundCaller: str
        :param _OutBoundCallee: 转外线被叫
        :type OutBoundCallee: str
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._OutBoundCaller = None
        self._OutBoundCallee = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def RingTimestamp(self):
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OutBoundCaller(self):
        return self._OutBoundCaller

    @OutBoundCaller.setter
    def OutBoundCaller(self, OutBoundCaller):
        self._OutBoundCaller = OutBoundCaller

    @property
    def OutBoundCallee(self):
        return self._OutBoundCallee

    @OutBoundCallee.setter
    def OutBoundCallee(self, OutBoundCallee):
        self._OutBoundCallee = OutBoundCallee

    @property
    def ProtectedCaller(self):
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._OutBoundCaller = params.get("OutBoundCaller")
        self._OutBoundCallee = params.get("OutBoundCallee")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSessionInfo(AbstractModel):
    """PSTN 会话信息

    """

    def __init__(self):
        r"""
        :param _SessionID: 会话 ID
        :type SessionID: str
        :param _RoomID: 会话临时房间 ID
        :type RoomID: str
        :param _Caller: 主叫
        :type Caller: str
        :param _Callee: 被叫
        :type Callee: str
        :param _StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: str
        :param _AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: str
        :param _StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param _StaffNumber: 坐席工号
        :type StaffNumber: str
        :param _SessionStatus: 坐席状态 inProgress 进行中
        :type SessionStatus: str
        :param _Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param _RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._RingTimestamp = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def AcceptTimestamp(self):
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RingTimestamp(self):
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def ProtectedCaller(self):
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._RingTimestamp = params.get("RingTimestamp")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageBuyInfo(AbstractModel):
    """套餐包购买信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 套餐包Id
        :type PackageId: str
        :param _Type: 套餐包类型，0-外呼套餐包|1-400呼入套餐包
        :type Type: int
        :param _CapacitySize: 套餐包总量
        :type CapacitySize: int
        :param _CapacityRemain: 套餐包剩余量
        :type CapacityRemain: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        """
        self._PackageId = None
        self._Type = None
        self._CapacitySize = None
        self._CapacityRemain = None
        self._BuyTime = None
        self._EndTime = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CapacitySize(self):
        return self._CapacitySize

    @CapacitySize.setter
    def CapacitySize(self, CapacitySize):
        self._CapacitySize = CapacitySize

    @property
    def CapacityRemain(self):
        return self._CapacityRemain

    @CapacityRemain.setter
    def CapacityRemain(self, CapacityRemain):
        self._CapacityRemain = CapacityRemain

    @property
    def BuyTime(self):
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._Type = params.get("Type")
        self._CapacitySize = params.get("CapacitySize")
        self._CapacityRemain = params.get("CapacityRemain")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneNumBuyInfo(AbstractModel):
    """号码购买信息

    """

    def __init__(self):
        r"""
        :param _PhoneNum: 电话号码
        :type PhoneNum: str
        :param _Type: 号码类型，0-固话|1-虚商号码|2-运营商号码|3-400号码
        :type Type: int
        :param _CallType: 号码呼叫类型，1-呼入|2-呼出|3-呼入呼出
        :type CallType: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        :param _State: 号码状态，1正常|2欠费停用|4管理员停用|5违规停用
        :type State: int
        """
        self._PhoneNum = None
        self._Type = None
        self._CallType = None
        self._BuyTime = None
        self._EndTime = None
        self._State = None

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallType(self):
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def BuyTime(self):
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

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


    def _deserialize(self, params):
        self._PhoneNum = params.get("PhoneNum")
        self._Type = params.get("Type")
        self._CallType = params.get("CallType")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordRequest(AbstractModel):
    """ResetExtensionPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TCCC 实例应用 ID
        :type SdkAppId: int
        :param _ExtensionId: 分机号
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordResponse(AbstractModel):
    """ResetExtensionPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 重置后密码
        :type Password: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class SdkAppIdBuyInfo(AbstractModel):
    """应用购买信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _Name: 应用名称
        :type Name: str
        :param _StaffBuyNum: 坐席购买数（还在有效期内）
        :type StaffBuyNum: int
        :param _StaffBuyList: 坐席购买列表 （还在有效期内）
        :type StaffBuyList: list of StaffBuyInfo
        :param _PhoneNumBuyList: 号码购买列表
        :type PhoneNumBuyList: list of PhoneNumBuyInfo
        """
        self._SdkAppId = None
        self._Name = None
        self._StaffBuyNum = None
        self._StaffBuyList = None
        self._PhoneNumBuyList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StaffBuyNum(self):
        return self._StaffBuyNum

    @StaffBuyNum.setter
    def StaffBuyNum(self, StaffBuyNum):
        self._StaffBuyNum = StaffBuyNum

    @property
    def StaffBuyList(self):
        return self._StaffBuyList

    @StaffBuyList.setter
    def StaffBuyList(self, StaffBuyList):
        self._StaffBuyList = StaffBuyList

    @property
    def PhoneNumBuyList(self):
        return self._PhoneNumBuyList

    @PhoneNumBuyList.setter
    def PhoneNumBuyList(self, PhoneNumBuyList):
        self._PhoneNumBuyList = PhoneNumBuyList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._StaffBuyNum = params.get("StaffBuyNum")
        if params.get("StaffBuyList") is not None:
            self._StaffBuyList = []
            for item in params.get("StaffBuyList"):
                obj = StaffBuyInfo()
                obj._deserialize(item)
                self._StaffBuyList.append(obj)
        if params.get("PhoneNumBuyList") is not None:
            self._PhoneNumBuyList = []
            for item in params.get("PhoneNumBuyList"):
                obj = PhoneNumBuyInfo()
                obj._deserialize(item)
                self._PhoneNumBuyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeatUserInfo(AbstractModel):
    """坐席用户信息

    """

    def __init__(self):
        r"""
        :param _Name: 坐席名称
        :type Name: str
        :param _Mail: 坐席邮箱
        :type Mail: str
        :param _StaffNumber: 工号
注意：此字段可能返回 null，表示取不到有效值。
        :type StaffNumber: str
        :param _Phone: 坐席电话号码（带0086前缀）
        :type Phone: str
        :param _Nick: 坐席昵称
        :type Nick: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _SkillGroupNameList: 坐席关联的技能组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupNameList: list of str
        """
        self._Name = None
        self._Mail = None
        self._StaffNumber = None
        self._Phone = None
        self._Nick = None
        self._UserId = None
        self._SkillGroupNameList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def StaffNumber(self):
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SkillGroupNameList(self):
        return self._SkillGroupNameList

    @SkillGroupNameList.setter
    def SkillGroupNameList(self, SkillGroupNameList):
        self._SkillGroupNameList = SkillGroupNameList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._StaffNumber = params.get("StaffNumber")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._UserId = params.get("UserId")
        self._SkillGroupNameList = params.get("SkillGroupNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServeParticipant(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param _Mail: 坐席邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Mail: str
        :param _Phone: 坐席电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _RingTimestamp: 振铃时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type AcceptTimestamp: int
        :param _EndedTimestamp: 结束时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type EndedTimestamp: int
        :param _RecordId: 录音 ID，能够索引到坐席侧的录音
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _Type: 参与者类型，"staffSeat", "outboundSeat", "staffPhoneSeat"
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _TransferFrom: 转接来源坐席信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFrom: str
        :param _TransferFromType: 转接来源参与者类型，取值与 Type 一致
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFromType: str
        :param _TransferTo: 转接去向坐席信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferTo: str
        :param _TransferToType: 转接去向参与者类型，取值与 Type 一致
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferToType: str
        :param _SkillGroupId: 技能组 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupId: int
        :param _EndStatusString: 结束状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EndStatusString: str
        :param _RecordURL: 录音 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordURL: str
        :param _Sequence: 参与者序号，从 0 开始
注意：此字段可能返回 null，表示取不到有效值。
        :type Sequence: int
        :param _StartTimestamp: 开始时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimestamp: int
        :param _SkillGroupName: 技能组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupName: str
        :param _CustomRecordURL: 录音转存第三方COS地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRecordURL: str
        """
        self._Mail = None
        self._Phone = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._RecordId = None
        self._Type = None
        self._TransferFrom = None
        self._TransferFromType = None
        self._TransferTo = None
        self._TransferToType = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._RecordURL = None
        self._Sequence = None
        self._StartTimestamp = None
        self._SkillGroupName = None
        self._CustomRecordURL = None

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def RingTimestamp(self):
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TransferFrom(self):
        return self._TransferFrom

    @TransferFrom.setter
    def TransferFrom(self, TransferFrom):
        self._TransferFrom = TransferFrom

    @property
    def TransferFromType(self):
        return self._TransferFromType

    @TransferFromType.setter
    def TransferFromType(self, TransferFromType):
        self._TransferFromType = TransferFromType

    @property
    def TransferTo(self):
        return self._TransferTo

    @TransferTo.setter
    def TransferTo(self, TransferTo):
        self._TransferTo = TransferTo

    @property
    def TransferToType(self):
        return self._TransferToType

    @TransferToType.setter
    def TransferToType(self, TransferToType):
        self._TransferToType = TransferToType

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def RecordURL(self):
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def Sequence(self):
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def StartTimestamp(self):
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def CustomRecordURL(self):
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL


    def _deserialize(self, params):
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._RecordId = params.get("RecordId")
        self._Type = params.get("Type")
        self._TransferFrom = params.get("TransferFrom")
        self._TransferFromType = params.get("TransferFromType")
        self._TransferTo = params.get("TransferTo")
        self._TransferToType = params.get("TransferToType")
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._RecordURL = params.get("RecordURL")
        self._Sequence = params.get("Sequence")
        self._StartTimestamp = params.get("StartTimestamp")
        self._SkillGroupName = params.get("SkillGroupName")
        self._CustomRecordURL = params.get("CustomRecordURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupInfoItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _Type: （废弃）类型：IM、TEL、ALL（全媒体）
        :type Type: str
        :param _RoutePolicy: 会话分配策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RoutePolicy: str
        :param _UsingLastSeat: 会话分配是否优先上次服务坐席
注意：此字段可能返回 null，表示取不到有效值。
        :type UsingLastSeat: int
        :param _MaxConcurrency: 单客服最大并发数（电话类型默认1）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConcurrency: int
        :param _LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTimestamp: int
        :param _SkillGroupType: 技能组类型0-电话，1-在线，3-音频，4-视频	
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupType: int
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Type = None
        self._RoutePolicy = None
        self._UsingLastSeat = None
        self._MaxConcurrency = None
        self._LastModifyTimestamp = None
        self._SkillGroupType = None

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RoutePolicy(self):
        return self._RoutePolicy

    @RoutePolicy.setter
    def RoutePolicy(self, RoutePolicy):
        self._RoutePolicy = RoutePolicy

    @property
    def UsingLastSeat(self):
        return self._UsingLastSeat

    @UsingLastSeat.setter
    def UsingLastSeat(self, UsingLastSeat):
        self._UsingLastSeat = UsingLastSeat

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def LastModifyTimestamp(self):
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def SkillGroupType(self):
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Type = params.get("Type")
        self._RoutePolicy = params.get("RoutePolicy")
        self._UsingLastSeat = params.get("UsingLastSeat")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._SkillGroupType = params.get("SkillGroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param _SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param _Priority: 优先级
        :type Priority: int
        :param _Type: 类型：IM、TEL、ALL（全媒体）
        :type Type: str
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Priority = None
        self._Type = None

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Priority = params.get("Priority")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffBuyInfo(AbstractModel):
    """坐席购买信息

    """

    def __init__(self):
        r"""
        :param _Num: 购买坐席数量
        :type Num: int
        :param _BuyTime: 购买时间戳
        :type BuyTime: int
        :param _EndTime: 截止时间戳
        :type EndTime: int
        """
        self._Num = None
        self._BuyTime = None
        self._EndTime = None

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def BuyTime(self):
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffInfo(AbstractModel):
    """带有技能组优先级的坐席信息

    """

    def __init__(self):
        r"""
        :param _Name: 坐席名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Mail: 坐席邮箱
        :type Mail: str
        :param _Phone: 坐席电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Nick: 坐席昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _StaffNumber: 坐席工号
注意：此字段可能返回 null，表示取不到有效值。
        :type StaffNumber: str
        :param _SkillGroupList: 所属技能组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupList: list of SkillGroupItem
        :param _LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTimestamp: int
        """
        self._Name = None
        self._Mail = None
        self._Phone = None
        self._Nick = None
        self._StaffNumber = None
        self._SkillGroupList = None
        self._LastModifyTimestamp = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def StaffNumber(self):
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SkillGroupList(self):
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

    @property
    def LastModifyTimestamp(self):
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._StaffNumber = params.get("StaffNumber")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusExtra(AbstractModel):
    """坐席状态补充信息

    """

    def __init__(self):
        r"""
        :param _Type: im - 文本 | tel - 电话 | all - 全媒体
        :type Type: str
        :param _Direct: in - 呼入 | out - 呼出
        :type Direct: str
        """
        self._Type = None
        self._Direct = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Direct(self):
        return self._Direct

    @Direct.setter
    def Direct(self, Direct):
        self._Direct = Direct


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Direct = params.get("Direct")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusMetrics(AbstractModel):
    """坐席状态相关信息

    """

    def __init__(self):
        r"""
        :param _Email: 坐席邮箱
        :type Email: str
        :param _Status: 坐席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线
        :type Status: str
        :param _StatusExtra: 坐席状态补充信息
        :type StatusExtra: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        :param _OnlineDuration: 当天在线总时长
        :type OnlineDuration: int
        :param _FreeDuration: 当天示闲总时长
        :type FreeDuration: int
        :param _BusyDuration: 当天忙碌总时长
        :type BusyDuration: int
        :param _NotReadyDuration: 当天示忙总时长
        :type NotReadyDuration: int
        :param _RestDuration: 当天小休总时长
        :type RestDuration: int
        :param _AfterCallWorkDuration: 当天话后调整总时长
        :type AfterCallWorkDuration: int
        :param _Reason: 小休原因
        :type Reason: str
        :param _ReserveRest: 是否预约小休
        :type ReserveRest: bool
        :param _ReserveNotReady: 是否预约示忙
        :type ReserveNotReady: bool
        :param _UseMobileAccept: 手机接听模式： 0 - 关闭 | 1 - 仅离线 | 2- 始终
        :type UseMobileAccept: int
        :param _UseMobileCallOut: 手机外呼开关
        :type UseMobileCallOut: bool
        :param _LastOnlineTimestamp: 最近一次上线时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTimestamp: int
        :param _LastStatusTimestamp: 最近一次状态时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastStatusTimestamp: int
        """
        self._Email = None
        self._Status = None
        self._StatusExtra = None
        self._OnlineDuration = None
        self._FreeDuration = None
        self._BusyDuration = None
        self._NotReadyDuration = None
        self._RestDuration = None
        self._AfterCallWorkDuration = None
        self._Reason = None
        self._ReserveRest = None
        self._ReserveNotReady = None
        self._UseMobileAccept = None
        self._UseMobileCallOut = None
        self._LastOnlineTimestamp = None
        self._LastStatusTimestamp = None

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusExtra(self):
        return self._StatusExtra

    @StatusExtra.setter
    def StatusExtra(self, StatusExtra):
        self._StatusExtra = StatusExtra

    @property
    def OnlineDuration(self):
        return self._OnlineDuration

    @OnlineDuration.setter
    def OnlineDuration(self, OnlineDuration):
        self._OnlineDuration = OnlineDuration

    @property
    def FreeDuration(self):
        return self._FreeDuration

    @FreeDuration.setter
    def FreeDuration(self, FreeDuration):
        self._FreeDuration = FreeDuration

    @property
    def BusyDuration(self):
        return self._BusyDuration

    @BusyDuration.setter
    def BusyDuration(self, BusyDuration):
        self._BusyDuration = BusyDuration

    @property
    def NotReadyDuration(self):
        return self._NotReadyDuration

    @NotReadyDuration.setter
    def NotReadyDuration(self, NotReadyDuration):
        self._NotReadyDuration = NotReadyDuration

    @property
    def RestDuration(self):
        return self._RestDuration

    @RestDuration.setter
    def RestDuration(self, RestDuration):
        self._RestDuration = RestDuration

    @property
    def AfterCallWorkDuration(self):
        return self._AfterCallWorkDuration

    @AfterCallWorkDuration.setter
    def AfterCallWorkDuration(self, AfterCallWorkDuration):
        self._AfterCallWorkDuration = AfterCallWorkDuration

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReserveRest(self):
        return self._ReserveRest

    @ReserveRest.setter
    def ReserveRest(self, ReserveRest):
        self._ReserveRest = ReserveRest

    @property
    def ReserveNotReady(self):
        return self._ReserveNotReady

    @ReserveNotReady.setter
    def ReserveNotReady(self, ReserveNotReady):
        self._ReserveNotReady = ReserveNotReady

    @property
    def UseMobileAccept(self):
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept

    @property
    def UseMobileCallOut(self):
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def LastOnlineTimestamp(self):
        return self._LastOnlineTimestamp

    @LastOnlineTimestamp.setter
    def LastOnlineTimestamp(self, LastOnlineTimestamp):
        self._LastOnlineTimestamp = LastOnlineTimestamp

    @property
    def LastStatusTimestamp(self):
        return self._LastStatusTimestamp

    @LastStatusTimestamp.setter
    def LastStatusTimestamp(self, LastStatusTimestamp):
        self._LastStatusTimestamp = LastStatusTimestamp


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        if params.get("StatusExtra") is not None:
            self._StatusExtra = StaffStatusExtra()
            self._StatusExtra._deserialize(params.get("StatusExtra"))
        self._OnlineDuration = params.get("OnlineDuration")
        self._FreeDuration = params.get("FreeDuration")
        self._BusyDuration = params.get("BusyDuration")
        self._NotReadyDuration = params.get("NotReadyDuration")
        self._RestDuration = params.get("RestDuration")
        self._AfterCallWorkDuration = params.get("AfterCallWorkDuration")
        self._Reason = params.get("Reason")
        self._ReserveRest = params.get("ReserveRest")
        self._ReserveNotReady = params.get("ReserveNotReady")
        self._UseMobileAccept = params.get("UseMobileAccept")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._LastOnlineTimestamp = params.get("LastOnlineTimestamp")
        self._LastStatusTimestamp = params.get("LastStatusTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoCalloutTaskRequest(AbstractModel):
    """StopAutoCalloutTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 呼叫中心实例Id
        :type SdkAppId: int
        :param _TaskId: 任务Id
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoCalloutTaskResponse(AbstractModel):
    """StopAutoCalloutTask返回参数结构体

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


class TelCdrInfo(AbstractModel):
    """电话话单信息

    """

    def __init__(self):
        r"""
        :param _Caller: 主叫号码
        :type Caller: str
        :param _Callee: 被叫号码
        :type Callee: str
        :param _Time: 呼叫发起时间戳，Unix 时间戳
        :type Time: int
        :param _Direction: 呼入呼出方向 0 呼入 1 呼出
        :type Direction: int
        :param _Duration: 通话时长
        :type Duration: int
        :param _RecordURL: 录音信息
        :type RecordURL: str
        :param _SeatUser: 坐席信息
        :type SeatUser: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        :param _EndStatus: EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无坐席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      CallinBlockedContact  呼入黑名单 

电话呼出               2	              unconnected	未接通
                         
电话呼出             201            unknown	未知状态

电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	 207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区

        :type EndStatus: int
        :param _SkillGroup: 技能组名称
        :type SkillGroup: str
        :param _CallerLocation: 主叫归属地
        :type CallerLocation: str
        :param _IVRDuration: IVR 阶段耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type IVRDuration: int
        :param _RingTimestamp: 振铃时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type RingTimestamp: int
        :param _AcceptTimestamp: 接听时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type AcceptTimestamp: int
        :param _EndedTimestamp: 结束时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type EndedTimestamp: int
        :param _IVRKeyPressed: IVR 按键信息 ，e.g. ["1","2","3"]
注意：此字段可能返回 null，表示取不到有效值。
        :type IVRKeyPressed: list of str
        :param _HungUpSide: 挂机方 seat 坐席 user 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type HungUpSide: str
        :param _ServeParticipants: 服务参与者列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServeParticipants: list of ServeParticipant
        :param _SkillGroupId: 技能组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupId: int
        :param _EndStatusString: EndStatus与EndStatusString一一对应，具体枚举如下：

**场景	         EndStatus	EndStatusString	状态说明**

电话呼入&呼出	1	        ok	                        正常结束

电话呼入&呼出	0	        error	                系统错误

电话呼入	             102	        ivrGiveUp	        IVR 期间用户放弃

电话呼入	             103	        waitingGiveUp	       会话排队期间用户放弃

电话呼入	             104	        ringingGiveUp	       会话振铃期间用户放弃

电话呼入	             105	        noSeatOnline	       无坐席在线

电话呼入              106	       notWorkTime	       非工作时间   

电话呼入	            107	       ivrEnd	               IVR 后直接结束

电话呼入	            100	      CallinBlockedContact  呼入黑名单 

电话呼出               2	              unconnected	未接通
                         
电话呼出             201            unknown	未知状态
听
电话呼出            203	    userReject	拒接挂断

电话呼出	          204	    powerOff	关机

电话呼出           205            numberNotExist	空号

电话呼出	         206	           busy	通话中

电话呼出   	 207	           outOfCredit	欠费

电话呼出	         208	           operatorError	运营商线路异常

电话呼出         	209	           callerCancel	主叫取消

电话呼出	        210	           notInService	不在服务区


注意：此字段可能返回 null，表示取不到有效值。
        :type EndStatusString: str
        :param _StartTimestamp: 会话开始时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimestamp: int
        :param _QueuedTimestamp: 进入排队时间，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuedTimestamp: int
        :param _PostIVRKeyPressed: 后置IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
注意：此字段可能返回 null，表示取不到有效值。
        :type PostIVRKeyPressed: list of IVRKeyPressedElement
        :param _QueuedSkillGroupId: 排队技能组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuedSkillGroupId: int
        :param _SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _ProtectedCaller: 主叫号码保护ID，开启号码保护映射功能时有效，且Caller字段置空
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedCaller: str
        :param _ProtectedCallee: 被叫号码保护ID，开启号码保护映射功能时有效，且Callee字段置空
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedCallee: str
        :param _Uui: 客户自定义数据（User-to-User Interface）
注意：此字段可能返回 null，表示取不到有效值。
        :type Uui: str
        :param _IVRKeyPressedEx: IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
注意：此字段可能返回 null，表示取不到有效值。
        :type IVRKeyPressedEx: list of IVRKeyPressedElement
        :param _AsrUrl: 获取录音ASR文本信息地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrUrl: str
        :param _CustomRecordURL: 录音转存第三方COS地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRecordURL: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _QueuedSkillGroupName: 排队技能组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuedSkillGroupName: str
        :param _VoicemailRecordURL: 通话中语音留言录音URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicemailRecordURL: list of str
        :param _VoicemailAsrURL: 通话中语音留言ASR文本信息地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VoicemailAsrURL: list of str
        """
        self._Caller = None
        self._Callee = None
        self._Time = None
        self._Direction = None
        self._Duration = None
        self._RecordURL = None
        self._SeatUser = None
        self._EndStatus = None
        self._SkillGroup = None
        self._CallerLocation = None
        self._IVRDuration = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._IVRKeyPressed = None
        self._HungUpSide = None
        self._ServeParticipants = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._StartTimestamp = None
        self._QueuedTimestamp = None
        self._PostIVRKeyPressed = None
        self._QueuedSkillGroupId = None
        self._SessionId = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None
        self._Uui = None
        self._IVRKeyPressedEx = None
        self._AsrUrl = None
        self._CustomRecordURL = None
        self._Remark = None
        self._QueuedSkillGroupName = None
        self._VoicemailRecordURL = None
        self._VoicemailAsrURL = None

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordURL(self):
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def SeatUser(self):
        return self._SeatUser

    @SeatUser.setter
    def SeatUser(self, SeatUser):
        self._SeatUser = SeatUser

    @property
    def EndStatus(self):
        return self._EndStatus

    @EndStatus.setter
    def EndStatus(self, EndStatus):
        self._EndStatus = EndStatus

    @property
    def SkillGroup(self):
        return self._SkillGroup

    @SkillGroup.setter
    def SkillGroup(self, SkillGroup):
        self._SkillGroup = SkillGroup

    @property
    def CallerLocation(self):
        return self._CallerLocation

    @CallerLocation.setter
    def CallerLocation(self, CallerLocation):
        self._CallerLocation = CallerLocation

    @property
    def IVRDuration(self):
        return self._IVRDuration

    @IVRDuration.setter
    def IVRDuration(self, IVRDuration):
        self._IVRDuration = IVRDuration

    @property
    def RingTimestamp(self):
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def IVRKeyPressed(self):
        return self._IVRKeyPressed

    @IVRKeyPressed.setter
    def IVRKeyPressed(self, IVRKeyPressed):
        self._IVRKeyPressed = IVRKeyPressed

    @property
    def HungUpSide(self):
        return self._HungUpSide

    @HungUpSide.setter
    def HungUpSide(self, HungUpSide):
        self._HungUpSide = HungUpSide

    @property
    def ServeParticipants(self):
        return self._ServeParticipants

    @ServeParticipants.setter
    def ServeParticipants(self, ServeParticipants):
        self._ServeParticipants = ServeParticipants

    @property
    def SkillGroupId(self):
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def StartTimestamp(self):
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def QueuedTimestamp(self):
        return self._QueuedTimestamp

    @QueuedTimestamp.setter
    def QueuedTimestamp(self, QueuedTimestamp):
        self._QueuedTimestamp = QueuedTimestamp

    @property
    def PostIVRKeyPressed(self):
        return self._PostIVRKeyPressed

    @PostIVRKeyPressed.setter
    def PostIVRKeyPressed(self, PostIVRKeyPressed):
        self._PostIVRKeyPressed = PostIVRKeyPressed

    @property
    def QueuedSkillGroupId(self):
        return self._QueuedSkillGroupId

    @QueuedSkillGroupId.setter
    def QueuedSkillGroupId(self, QueuedSkillGroupId):
        self._QueuedSkillGroupId = QueuedSkillGroupId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ProtectedCaller(self):
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee

    @property
    def Uui(self):
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        self._Uui = Uui

    @property
    def IVRKeyPressedEx(self):
        return self._IVRKeyPressedEx

    @IVRKeyPressedEx.setter
    def IVRKeyPressedEx(self, IVRKeyPressedEx):
        self._IVRKeyPressedEx = IVRKeyPressedEx

    @property
    def AsrUrl(self):
        return self._AsrUrl

    @AsrUrl.setter
    def AsrUrl(self, AsrUrl):
        self._AsrUrl = AsrUrl

    @property
    def CustomRecordURL(self):
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def QueuedSkillGroupName(self):
        return self._QueuedSkillGroupName

    @QueuedSkillGroupName.setter
    def QueuedSkillGroupName(self, QueuedSkillGroupName):
        self._QueuedSkillGroupName = QueuedSkillGroupName

    @property
    def VoicemailRecordURL(self):
        return self._VoicemailRecordURL

    @VoicemailRecordURL.setter
    def VoicemailRecordURL(self, VoicemailRecordURL):
        self._VoicemailRecordURL = VoicemailRecordURL

    @property
    def VoicemailAsrURL(self):
        return self._VoicemailAsrURL

    @VoicemailAsrURL.setter
    def VoicemailAsrURL(self, VoicemailAsrURL):
        self._VoicemailAsrURL = VoicemailAsrURL


    def _deserialize(self, params):
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._Time = params.get("Time")
        self._Direction = params.get("Direction")
        self._Duration = params.get("Duration")
        self._RecordURL = params.get("RecordURL")
        if params.get("SeatUser") is not None:
            self._SeatUser = SeatUserInfo()
            self._SeatUser._deserialize(params.get("SeatUser"))
        self._EndStatus = params.get("EndStatus")
        self._SkillGroup = params.get("SkillGroup")
        self._CallerLocation = params.get("CallerLocation")
        self._IVRDuration = params.get("IVRDuration")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._IVRKeyPressed = params.get("IVRKeyPressed")
        self._HungUpSide = params.get("HungUpSide")
        if params.get("ServeParticipants") is not None:
            self._ServeParticipants = []
            for item in params.get("ServeParticipants"):
                obj = ServeParticipant()
                obj._deserialize(item)
                self._ServeParticipants.append(obj)
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._StartTimestamp = params.get("StartTimestamp")
        self._QueuedTimestamp = params.get("QueuedTimestamp")
        if params.get("PostIVRKeyPressed") is not None:
            self._PostIVRKeyPressed = []
            for item in params.get("PostIVRKeyPressed"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._PostIVRKeyPressed.append(obj)
        self._QueuedSkillGroupId = params.get("QueuedSkillGroupId")
        self._SessionId = params.get("SessionId")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        self._Uui = params.get("Uui")
        if params.get("IVRKeyPressedEx") is not None:
            self._IVRKeyPressedEx = []
            for item in params.get("IVRKeyPressedEx"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._IVRKeyPressedEx.append(obj)
        self._AsrUrl = params.get("AsrUrl")
        self._CustomRecordURL = params.get("CustomRecordURL")
        self._Remark = params.get("Remark")
        self._QueuedSkillGroupName = params.get("QueuedSkillGroupName")
        self._VoicemailRecordURL = params.get("VoicemailRecordURL")
        self._VoicemailAsrURL = params.get("VoicemailAsrURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindNumberCallOutSkillGroupRequest(AbstractModel):
    """UnbindNumberCallOutSkillGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _Number: 待解绑的号码
        :type Number: str
        :param _SkillGroupIds: 待解绑的技能组Id列表
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindNumberCallOutSkillGroupResponse(AbstractModel):
    """UnbindNumberCallOutSkillGroup返回参数结构体

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


class UnbindStaffSkillGroupListRequest(AbstractModel):
    """UnbindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用 ID（必填），可以查看 https://console.cloud.tencent.com/ccc
        :type SdkAppId: int
        :param _StaffEmail: 客服邮箱
        :type StaffEmail: str
        :param _SkillGroupList: 解绑技能组列表
        :type SkillGroupList: list of int
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindStaffSkillGroupListResponse(AbstractModel):
    """UnbindStaffSkillGroupList返回参数结构体

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


class Variable(AbstractModel):
    """变量

    """

    def __init__(self):
        r"""
        :param _Key: 变量名
        :type Key: str
        :param _Value: 变量值
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
        