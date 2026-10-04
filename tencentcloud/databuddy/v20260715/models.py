# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AddConsoleUsersRequest(AbstractModel):
    r"""AddConsoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserUins: <p>用户 UIN 列表，单次最多100个</p>
        :type UserUins: list of str
        :param _RoleIds: <p>角色 ID 列表</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul>
        :type RoleIds: list of str
        """
        self._UserUins = None
        self._RoleIds = None

    @property
    def UserUins(self):
        r"""<p>用户 UIN 列表，单次最多100个</p>
        :rtype: list of str
        """
        return self._UserUins

    @UserUins.setter
    def UserUins(self, UserUins):
        self._UserUins = UserUins

    @property
    def RoleIds(self):
        r"""<p>角色 ID 列表</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul>
        :rtype: list of str
        """
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        self._UserUins = params.get("UserUins")
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddConsoleUsersResponse(AbstractModel):
    r"""AddConsoleUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddConsoleUsersRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddConsoleUsersRsp(AbstractModel):
    r"""添加控制台用户响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedDependencyConfig(AbstractModel):
    r"""高级依赖配置

    """

    def __init__(self):
        r"""
        :param _Operator: 逻辑运算符号OR / AND
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Conditions: 任务运行条件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of TaskRunConditionRule
        """
        self._Operator = None
        self._Conditions = None

    @property
    def Operator(self):
        r"""逻辑运算符号OR / AND
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Conditions(self):
        r"""任务运行条件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskRunConditionRule
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = TaskRunConditionRule()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedParameter(AbstractModel):
    r"""高级运行参数（工作流高级运行时用户填入的参数）

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmBrief(AbstractModel):
    r"""告警配置

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警 ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmId: str
        :param _AlarmMonitorType: 告警的监控对象类型，如工作流、任务等，当前支持 1. WORKFLOW 2. TASK
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmMonitorType: str
        :param _AlarmGroups: 告警组，最多 50 个
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmGroups: list of AlarmGroup
        :param _DoNotDisturbWhenSkipped: 被跳过时免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :type DoNotDisturbWhenSkipped: bool
        :param _DoNotDisturbWhenManuallyTerminated: 被手动终止时免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :type DoNotDisturbWhenManuallyTerminated: bool
        :param _DoNotDisturbUntilTheLastRetry: 最后一次重试前免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :type DoNotDisturbUntilTheLastRetry: bool
        """
        self._AlarmId = None
        self._AlarmMonitorType = None
        self._AlarmGroups = None
        self._DoNotDisturbWhenSkipped = None
        self._DoNotDisturbWhenManuallyTerminated = None
        self._DoNotDisturbUntilTheLastRetry = None

    @property
    def AlarmId(self):
        r"""告警 ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def AlarmMonitorType(self):
        r"""告警的监控对象类型，如工作流、任务等，当前支持 1. WORKFLOW 2. TASK
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlarmMonitorType

    @AlarmMonitorType.setter
    def AlarmMonitorType(self, AlarmMonitorType):
        self._AlarmMonitorType = AlarmMonitorType

    @property
    def AlarmGroups(self):
        r"""告警组，最多 50 个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups

    @property
    def DoNotDisturbWhenSkipped(self):
        r"""被跳过时免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DoNotDisturbWhenSkipped

    @DoNotDisturbWhenSkipped.setter
    def DoNotDisturbWhenSkipped(self, DoNotDisturbWhenSkipped):
        self._DoNotDisturbWhenSkipped = DoNotDisturbWhenSkipped

    @property
    def DoNotDisturbWhenManuallyTerminated(self):
        r"""被手动终止时免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DoNotDisturbWhenManuallyTerminated

    @DoNotDisturbWhenManuallyTerminated.setter
    def DoNotDisturbWhenManuallyTerminated(self, DoNotDisturbWhenManuallyTerminated):
        self._DoNotDisturbWhenManuallyTerminated = DoNotDisturbWhenManuallyTerminated

    @property
    def DoNotDisturbUntilTheLastRetry(self):
        r"""最后一次重试前免打扰，默认值 false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DoNotDisturbUntilTheLastRetry

    @DoNotDisturbUntilTheLastRetry.setter
    def DoNotDisturbUntilTheLastRetry(self, DoNotDisturbUntilTheLastRetry):
        self._DoNotDisturbUntilTheLastRetry = DoNotDisturbUntilTheLastRetry


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._AlarmMonitorType = params.get("AlarmMonitorType")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        self._DoNotDisturbWhenSkipped = params.get("DoNotDisturbWhenSkipped")
        self._DoNotDisturbWhenManuallyTerminated = params.get("DoNotDisturbWhenManuallyTerminated")
        self._DoNotDisturbUntilTheLastRetry = params.get("DoNotDisturbUntilTheLastRetry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmGroup(AbstractModel):
    r"""告警组

    """

    def __init__(self):
        r"""
        :param _ChannelId: <p>通知渠道ID，可通过基础平台通知渠道相关接口获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _ChannelName: <p>通知渠道名称，可以是用户组名称或邮箱地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param _IsEmailChannel: <p>是否启用邮件渠道，默认值：false</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEmailChannel: bool
        :param _AlarmConditions: <p>告警条件列表。取值：<br>START：启动<br>SUCCESS：成功<br>FAILURE：失败<br>MONITOR_INDICATOR_ALARM：监控指标告警</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmConditions: list of str
        :param _ChannelType: <p>通知渠道类型。取值：0 未指定，1 Email，2 Webhook，3 Teams，4 Slack</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelType: int
        """
        self._ChannelId = None
        self._ChannelName = None
        self._IsEmailChannel = None
        self._AlarmConditions = None
        self._ChannelType = None

    @property
    def ChannelId(self):
        r"""<p>通知渠道ID，可通过基础平台通知渠道相关接口获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""<p>通知渠道名称，可以是用户组名称或邮箱地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def IsEmailChannel(self):
        r"""<p>是否启用邮件渠道，默认值：false</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsEmailChannel

    @IsEmailChannel.setter
    def IsEmailChannel(self, IsEmailChannel):
        self._IsEmailChannel = IsEmailChannel

    @property
    def AlarmConditions(self):
        r"""<p>告警条件列表。取值：<br>START：启动<br>SUCCESS：成功<br>FAILURE：失败<br>MONITOR_INDICATOR_ALARM：监控指标告警</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AlarmConditions

    @AlarmConditions.setter
    def AlarmConditions(self, AlarmConditions):
        self._AlarmConditions = AlarmConditions

    @property
    def ChannelType(self):
        r"""<p>通知渠道类型。取值：0 未指定，1 Email，2 Webhook，3 Teams，4 Slack</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ChannelType

    @ChannelType.setter
    def ChannelType(self, ChannelType):
        self._ChannelType = ChannelType


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._IsEmailChannel = params.get("IsEmailChannel")
        self._AlarmConditions = params.get("AlarmConditions")
        self._ChannelType = params.get("ChannelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncActionRsp(AbstractModel):
    r"""批量异步操作的逐项结果

    """

    def __init__(self):
        r"""
        :param _ActionResults: 多个操作项的结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionResults: list of RunActionBrief
        """
        self._ActionResults = None

    @property
    def ActionResults(self):
        r"""多个操作项的结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RunActionBrief
        """
        return self._ActionResults

    @ActionResults.setter
    def ActionResults(self, ActionResults):
        self._ActionResults = ActionResults


    def _deserialize(self, params):
        if params.get("ActionResults") is not None:
            self._ActionResults = []
            for item in params.get("ActionResults"):
                obj = RunActionBrief()
                obj._deserialize(item)
                self._ActionResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncOperation(AbstractModel):
    r"""OneFlow 透传的 Workspace 异步文件操作信息；作业状态由 Workspace 持久化和维护

    """

    def __init__(self):
        r"""
        :param _IsAsync: 是否异步执行；ZIP 解压创建时为 true
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAsync: bool
        :param _JobId: Workspace 持久化的异步作业 ID，用于查询作业进度
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _OperationId: 调用方生成的提交幂等与链路追踪标识
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationId: str
        :param _Status: 异步作业状态：0-未指定，1-已受理，2-解压中，3-回调处理中，4-成功，5-部分失败，6-失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._IsAsync = None
        self._JobId = None
        self._OperationId = None
        self._Status = None

    @property
    def IsAsync(self):
        r"""是否异步执行；ZIP 解压创建时为 true
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync

    @property
    def JobId(self):
        r"""Workspace 持久化的异步作业 ID，用于查询作业进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def OperationId(self):
        r"""调用方生成的提交幂等与链路追踪标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Status(self):
        r"""异步作业状态：0-未指定，1-已受理，2-解压中，3-回调处理中，4-成功，5-部分失败，6-失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._IsAsync = params.get("IsAsync")
        self._JobId = params.get("JobId")
        self._OperationId = params.get("OperationId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Audit(AbstractModel):
    r"""审计信息

    """

    def __init__(self):
        r"""
        :param _Creator: 创建者。注意：此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _CreatedAt: 创建时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _LastModifier: 最后修改者。注意：此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifier: str
        :param _LastModifiedAt: 最后修改时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedAt: str
        :param _CreatorName: 创建者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorName: str
        :param _LastModifierName: 最后修改者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifierName: str
        """
        self._Creator = None
        self._CreatedAt = None
        self._LastModifier = None
        self._LastModifiedAt = None
        self._CreatorName = None
        self._LastModifierName = None

    @property
    def Creator(self):
        r"""创建者。注意：此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""创建时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LastModifier(self):
        r"""最后修改者。注意：此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastModifier

    @LastModifier.setter
    def LastModifier(self, LastModifier):
        self._LastModifier = LastModifier

    @property
    def LastModifiedAt(self):
        r"""最后修改时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastModifiedAt

    @LastModifiedAt.setter
    def LastModifiedAt(self, LastModifiedAt):
        self._LastModifiedAt = LastModifiedAt

    @property
    def CreatorName(self):
        r"""创建者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorName

    @CreatorName.setter
    def CreatorName(self, CreatorName):
        self._CreatorName = CreatorName

    @property
    def LastModifierName(self):
        r"""最后修改者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastModifierName

    @LastModifierName.setter
    def LastModifierName(self, LastModifierName):
        self._LastModifierName = LastModifierName


    def _deserialize(self, params):
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._LastModifier = params.get("LastModifier")
        self._LastModifiedAt = params.get("LastModifiedAt")
        self._CreatorName = params.get("CreatorName")
        self._LastModifierName = params.get("LastModifierName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonFailItem(AbstractModel):
    r"""通用错误信息

    """

    def __init__(self):
        r"""
        :param _Item: <p>uin或者groupId</p>
        :type Item: str
        :param _FailReason: <p>错误信息</p>
        :type FailReason: str
        """
        self._Item = None
        self._FailReason = None

    @property
    def Item(self):
        r"""<p>uin或者groupId</p>
        :rtype: str
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def FailReason(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonTagInfo(AbstractModel):
    r"""通用标签信息（用于查询展示场景），适用于表标签、字段标签等各类资产标签的轻量展示，供GetTable等接口返回使用

    """

    def __init__(self):
        r"""
        :param _LabelId: 标签ID
        :type LabelId: str
        :param _LabelName: 标签名称
        :type LabelName: str
        :param _LabelValueId: 标签值ID，属性标签（LabelType=3）可为0
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValueId: str
        :param _LabelValue: 标签值，脱敏标签（LabelType=4）时可为空
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _Type: 标签类型，取值参考LabelType枚举定义：1-治理标签，2-自定义标签，3-属性标签，4-脱敏标签
        :type Type: int
        :param _Deleted: 标签是否已删除。true表示该LabelId在meta_biz_label中查不到记录，标签已被物理删除；false（默认）表示标签仍存在
        :type Deleted: bool
        """
        self._LabelId = None
        self._LabelName = None
        self._LabelValueId = None
        self._LabelValue = None
        self._Type = None
        self._Deleted = None

    @property
    def LabelId(self):
        r"""标签ID
        :rtype: str
        """
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId

    @property
    def LabelName(self):
        r"""标签名称
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def LabelValueId(self):
        r"""标签值ID，属性标签（LabelType=3）可为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelValueId

    @LabelValueId.setter
    def LabelValueId(self, LabelValueId):
        self._LabelValueId = LabelValueId

    @property
    def LabelValue(self):
        r"""标签值，脱敏标签（LabelType=4）时可为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def Type(self):
        r"""标签类型，取值参考LabelType枚举定义：1-治理标签，2-自定义标签，3-属性标签，4-脱敏标签
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Deleted(self):
        r"""标签是否已删除。true表示该LabelId在meta_biz_label中查不到记录，标签已被物理删除；false（默认）表示标签仍存在
        :rtype: bool
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted


    def _deserialize(self, params):
        self._LabelId = params.get("LabelId")
        self._LabelName = params.get("LabelName")
        self._LabelValueId = params.get("LabelValueId")
        self._LabelValue = params.get("LabelValue")
        self._Type = params.get("Type")
        self._Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleGroupInfo(AbstractModel):
    r"""控制台用户组信息（对外标准版，与内部 UserGroupRoleInfo 解耦）

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: str
        :param _GroupName: 用户组名称
        :type GroupName: str
        :param _Roles: 角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of RoleBasicInfo
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _UserCount: 用户组下用户数量
        :type UserCount: int
        :param _GroupType: 用户组类型。取值为枚举数值的字符串形式："0"=控制台系统类型（包含全部user）、"1"=控制台自定义类型、"2"=工作空间系统类型、"3"=工作空间自定义类型
        :type GroupType: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Roles = None
        self._CreateTime = None
        self._UpdateTime = None
        self._UserCount = None
        self._GroupType = None

    @property
    def GroupId(self):
        r"""用户组 ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""用户组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Roles(self):
        r"""角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RoleBasicInfo
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UserCount(self):
        r"""用户组下用户数量
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def GroupType(self):
        r"""用户组类型。取值为枚举数值的字符串形式："0"=控制台系统类型（包含全部user）、"1"=控制台自定义类型、"2"=工作空间系统类型、"3"=工作空间自定义类型
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("Roles") is not None:
            self._Roles = []
            for item in params.get("Roles"):
                obj = RoleBasicInfo()
                obj._deserialize(item)
                self._Roles.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._UserCount = params.get("UserCount")
        self._GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleGroupUserInfo(AbstractModel):
    r"""控制台用户组成员信息（对外标准版，与内部 GroupUserInfo 解耦）

    """

    def __init__(self):
        r"""
        :param _UserUin: 用户 UIN
        :type UserUin: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._UserUin = None
        self._UserName = None
        self._Nickname = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def UserUin(self):
        r"""用户 UIN
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._UserUin = params.get("UserUin")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleRoleInfo(AbstractModel):
    r"""控制台角色信息（对外标准版，与内部 Role 解耦）

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 角色基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        :param _MetaData: 角色元信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.databuddy.v20260715.models.RoleMetaData`
        :param _Permissions: 角色权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of RolePermission
        """
        self._BasicInfo = None
        self._MetaData = None
        self._Permissions = None

    @property
    def BasicInfo(self):
        r"""角色基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def MetaData(self):
        r"""角色元信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RoleMetaData`
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def Permissions(self):
        r"""角色权限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RolePermission
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = RoleBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("MetaData") is not None:
            self._MetaData = RoleMetaData()
            self._MetaData._deserialize(params.get("MetaData"))
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = RolePermission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleUserInfo(AbstractModel):
    r"""控制台用户信息（规范化，与内部 UserDetailInfo 解耦）

    """

    def __init__(self):
        r"""
        :param _UserUin: 用户 UIN
        :type UserUin: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _Roles: 角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of RoleBasicInfo
        :param _UserSource: 用户来源，group：用户组、user:用户
        :type UserSource: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _IsOwner: 是否主账号
        :type IsOwner: bool
        :param _UserTag: 0: 普通用户 1: entraId用户
        :type UserTag: int
        :param _IsAdmin: 是否具有 admin 权限的子账号
        :type IsAdmin: bool
        """
        self._UserUin = None
        self._UserName = None
        self._Nickname = None
        self._Roles = None
        self._UserSource = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsOwner = None
        self._UserTag = None
        self._IsAdmin = None

    @property
    def UserUin(self):
        r"""用户 UIN
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Roles(self):
        r"""角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RoleBasicInfo
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def UserSource(self):
        r"""用户来源，group：用户组、user:用户
        :rtype: str
        """
        return self._UserSource

    @UserSource.setter
    def UserSource(self, UserSource):
        self._UserSource = UserSource

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsOwner(self):
        r"""是否主账号
        :rtype: bool
        """
        return self._IsOwner

    @IsOwner.setter
    def IsOwner(self, IsOwner):
        self._IsOwner = IsOwner

    @property
    def UserTag(self):
        r"""0: 普通用户 1: entraId用户
        :rtype: int
        """
        return self._UserTag

    @UserTag.setter
    def UserTag(self, UserTag):
        self._UserTag = UserTag

    @property
    def IsAdmin(self):
        r"""是否具有 admin 权限的子账号
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin


    def _deserialize(self, params):
        self._UserUin = params.get("UserUin")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        if params.get("Roles") is not None:
            self._Roles = []
            for item in params.get("Roles"):
                obj = RoleBasicInfo()
                obj._deserialize(item)
                self._Roles.append(obj)
        self._UserSource = params.get("UserSource")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsOwner = params.get("IsOwner")
        self._UserTag = params.get("UserTag")
        self._IsAdmin = params.get("IsAdmin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCatalogRequest(AbstractModel):
    r"""CreateCatalog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: catalog名称
        :type Name: str
        :param _Type: catalog类型, 可选值TABLE、MODEL、VOLUME
        :type Type: str
        :param _WorkspaceId: 工作空间唯一id
        :type WorkspaceId: str
        :param _Comment: 描述
        :type Comment: str
        :param _ConnectionId: connection 的 ID
        :type ConnectionId: str
        :param _CatalogSource: 数据目录来源，可选（融合版新增字段），取值参考 CatalogSourceEnum：METALAKE（专业版）/ CONNECTION（分析版），不传时默认按 METALAKE 处理
        :type CatalogSource: str
        """
        self._Name = None
        self._Type = None
        self._WorkspaceId = None
        self._Comment = None
        self._ConnectionId = None
        self._CatalogSource = None

    @property
    def Name(self):
        r"""catalog名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""catalog类型, 可选值TABLE、MODEL、VOLUME
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WorkspaceId(self):
        r"""工作空间唯一id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Comment(self):
        r"""描述
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def ConnectionId(self):
        r"""connection 的 ID
        :rtype: str
        """
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def CatalogSource(self):
        r"""数据目录来源，可选（融合版新增字段），取值参考 CatalogSourceEnum：METALAKE（专业版）/ CONNECTION（分析版），不传时默认按 METALAKE 处理
        :rtype: str
        """
        return self._CatalogSource

    @CatalogSource.setter
    def CatalogSource(self, CatalogSource):
        self._CatalogSource = CatalogSource


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Comment = params.get("Comment")
        self._ConnectionId = params.get("ConnectionId")
        self._CatalogSource = params.get("CatalogSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCatalogResponse(AbstractModel):
    r"""CreateCatalog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建catalog响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateCatalogRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建catalog响应
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateCatalogRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateCatalogRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCatalogRsp(AbstractModel):
    r"""创建数据目录的响应

    """

    def __init__(self):
        r"""
        :param _CatalogId: 新创建的数据目录的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CatalogId: str
        """
        self._CatalogId = None

    @property
    def CatalogId(self):
        r"""新创建的数据目录的id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId


    def _deserialize(self, params):
        self._CatalogId = params.get("CatalogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleGroupRequest(AbstractModel):
    r"""CreateConsoleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: <p>用户组名称</p>
        :type GroupName: str
        :param _GroupNickname: <p>用户组别名</p>
        :type GroupNickname: str
        :param _Description: <p>用户组描述</p>
        :type Description: str
        """
        self._GroupName = None
        self._GroupNickname = None
        self._Description = None

    @property
    def GroupName(self):
        r"""<p>用户组名称</p>
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNickname(self):
        r"""<p>用户组别名</p>
        :rtype: str
        """
        return self._GroupNickname

    @GroupNickname.setter
    def GroupNickname(self, GroupNickname):
        self._GroupNickname = GroupNickname

    @property
    def Description(self):
        r"""<p>用户组描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupNickname = params.get("GroupNickname")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleGroupResponse(AbstractModel):
    r"""CreateConsoleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateConsoleGroupRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateConsoleGroupRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateConsoleGroupRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateConsoleGroupRsp(AbstractModel):
    r"""创建控制台用户组响应

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建成功的用户组 ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        r"""创建成功的用户组 ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileRequest(AbstractModel):
    r"""CreateFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :type WorkspaceId: str
        :param _FileName: <p>文件名，含后缀，最长 255 字节。不能以 . 或 .. 开头/结尾，不能含空格与控制字符</p>
        :type FileName: str
        :param _ParentFolderPath: <p>父文件夹路径，以 / 开头、末尾不带 /，根目录传 /。来源：ListFiles 接口返回的 Path</p>
        :type ParentFolderPath: str
        :param _FileType: <p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :type FileType: str
        :param _FileConfig: <p>文件运行配置</p>
        :type FileConfig: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        :param _BundleId: <p>绑定的 BundleId。来源：ListBundles 接口返回的 BundleId</p>
        :type BundleId: str
        :param _BundleInfo: <p>绑定的 BundleInfo，JSON 字符串</p>
        :type BundleInfo: str
        :param _Storage: <p>文件初始内容。不传则按FileType 生成默认内容</p>
        :type Storage: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        :param _ExtractArchive: 是否将 Storage 中的 ZIP 文件异步解压创建，默认 false。true 时异步作业由 Workspace 负责全生命周期，响应仅通过 AsyncOperation 返回作业信息（FileId 为空）；作业进度查询由基础平台 WS 接口实现，不在本协议中定义。
        :type ExtractArchive: bool
        """
        self._WorkspaceId = None
        self._FileName = None
        self._ParentFolderPath = None
        self._FileType = None
        self._FileConfig = None
        self._BundleId = None
        self._BundleInfo = None
        self._Storage = None
        self._ExtractArchive = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileName(self):
        r"""<p>文件名，含后缀，最长 255 字节。不能以 . 或 .. 开头/结尾，不能含空格与控制字符</p>
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ParentFolderPath(self):
        r"""<p>父文件夹路径，以 / 开头、末尾不带 /，根目录传 /。来源：ListFiles 接口返回的 Path</p>
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def FileType(self):
        r"""<p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileConfig(self):
        r"""<p>文件运行配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        """
        return self._FileConfig

    @FileConfig.setter
    def FileConfig(self, FileConfig):
        self._FileConfig = FileConfig

    @property
    def BundleId(self):
        r"""<p>绑定的 BundleId。来源：ListBundles 接口返回的 BundleId</p>
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>绑定的 BundleInfo，JSON 字符串</p>
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def Storage(self):
        r"""<p>文件初始内容。不传则按FileType 生成默认内容</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ExtractArchive(self):
        r"""是否将 Storage 中的 ZIP 文件异步解压创建，默认 false。true 时异步作业由 Workspace 负责全生命周期，响应仅通过 AsyncOperation 返回作业信息（FileId 为空）；作业进度查询由基础平台 WS 接口实现，不在本协议中定义。
        :rtype: bool
        """
        return self._ExtractArchive

    @ExtractArchive.setter
    def ExtractArchive(self, ExtractArchive):
        self._ExtractArchive = ExtractArchive


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileName = params.get("FileName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._FileType = params.get("FileType")
        if params.get("FileConfig") is not None:
            self._FileConfig = FileConfig()
            self._FileConfig._deserialize(params.get("FileConfig"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        if params.get("Storage") is not None:
            self._Storage = FileStorage()
            self._Storage._deserialize(params.get("Storage"))
        self._ExtractArchive = params.get("ExtractArchive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileResponse(AbstractModel):
    r"""CreateFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = FileInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateFolderRequest(AbstractModel):
    r"""CreateFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间名称</p>
        :type WorkspaceId: str
        :param _FolderName: <p>文件夹名称</p>
        :type FolderName: str
        :param _FolderType: <p>文件夹类型</p><p>枚举值：</p><ul><li>FOLDER： 文件夹</li><li>GIT_FOLDER： git文件夹</li></ul>
        :type FolderType: str
        :param _ParentFolder: <p>父节点</p>
        :type ParentFolder: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        :param _GitConfig: <p>git配置，FolderType=GIT_FOLDER 时必填</p>
        :type GitConfig: :class:`tencentcloud.databuddy.v20260715.models.GitRepoConfig`
        """
        self._WorkspaceId = None
        self._FolderName = None
        self._FolderType = None
        self._ParentFolder = None
        self._GitConfig = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间名称</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FolderName(self):
        r"""<p>文件夹名称</p>
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderType(self):
        r"""<p>文件夹类型</p><p>枚举值：</p><ul><li>FOLDER： 文件夹</li><li>GIT_FOLDER： git文件夹</li></ul>
        :rtype: str
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType

    @property
    def ParentFolder(self):
        r"""<p>父节点</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._ParentFolder

    @ParentFolder.setter
    def ParentFolder(self, ParentFolder):
        self._ParentFolder = ParentFolder

    @property
    def GitConfig(self):
        r"""<p>git配置，FolderType=GIT_FOLDER 时必填</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GitRepoConfig`
        """
        return self._GitConfig

    @GitConfig.setter
    def GitConfig(self, GitConfig):
        self._GitConfig = GitConfig


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FolderName = params.get("FolderName")
        self._FolderType = params.get("FolderType")
        if params.get("ParentFolder") is not None:
            self._ParentFolder = FolderLocator()
            self._ParentFolder._deserialize(params.get("ParentFolder"))
        if params.get("GitConfig") is not None:
            self._GitConfig = GitRepoConfig()
            self._GitConfig._deserialize(params.get("GitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFolderResponse(AbstractModel):
    r"""CreateFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>创建文件夹结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateFolderRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>创建文件夹结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateFolderRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateFolderRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateFolderRsp(AbstractModel):
    r"""创建文件夹回包

    """

    def __init__(self):
        r"""
        :param _FolderId: <p>文件夹 ID</p>
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""<p>文件夹 ID</p>
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchemaRequest(AbstractModel):
    r"""CreateSchema请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogName: catalog名称
        :type CatalogName: str
        :param _Name: schema名称
        :type Name: str
        :param _Comment: 描述
        :type Comment: str
        :param _WorkspaceId: 调用时所在workspace唯一id
        :type WorkspaceId: str
        :param _ConnectionId: 数据源连接ID，可选（融合版新增字段）。分析版catalog不支持创建schema，传入非空时服务端返回ANA_CATALOG_NOT_SUPPORTED错误
        :type ConnectionId: str
        """
        self._CatalogName = None
        self._Name = None
        self._Comment = None
        self._WorkspaceId = None
        self._ConnectionId = None

    @property
    def CatalogName(self):
        r"""catalog名称
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def Name(self):
        r"""schema名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Comment(self):
        r"""描述
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def WorkspaceId(self):
        r"""调用时所在workspace唯一id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ConnectionId(self):
        r"""数据源连接ID，可选（融合版新增字段）。分析版catalog不支持创建schema，传入非空时服务端返回ANA_CATALOG_NOT_SUPPORTED错误
        :rtype: str
        """
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId


    def _deserialize(self, params):
        self._CatalogName = params.get("CatalogName")
        self._Name = params.get("Name")
        self._Comment = params.get("Comment")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ConnectionId = params.get("ConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchemaResponse(AbstractModel):
    r"""CreateSchema返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateSchemaRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateSchemaRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateSchemaRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateSchemaRsp(AbstractModel):
    r"""创建schema的响应

    """

    def __init__(self):
        r"""
        :param _Schema: schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Schema: :class:`tencentcloud.databuddy.v20260715.models.Schema`
        """
        self._Schema = None

    @property
    def Schema(self):
        r"""schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.Schema`
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        if params.get("Schema") is not None:
            self._Schema = Schema()
            self._Schema._deserialize(params.get("Schema"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowRequest(AbstractModel):
    r"""CreateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _BaseInfo: <p>工作流基本信息。必填，其中 WorkflowName 必填且工作空间内唯一</p>
        :type BaseInfo: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfo`
        :param _Trigger: <p>工作流调度配置</p>
        :type Trigger: list of WorkflowTriggerConfiguration
        :param _ParamList: <p>工作流参数列表</p>
        :type ParamList: list of ParamInfo
        :param _LabelList: <p>标签列表</p>
        :type LabelList: list of LabelBrief
        :param _Alarm: <p>工作流告警配置</p>
        :type Alarm: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        :param _MonitorMetric: <p>监控指标配置。若告警条件中选择了监控告警，则本字段必填</p>
        :type MonitorMetric: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        :param _AdvanceConfig: <p>工作流高级设置</p>
        :type AdvanceConfig: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        :param _TaskList: <p>工作流任务列表</p>
        :type TaskList: list of WorkflowTask
        :param _BundleId: <p>BundleId，可通过 Bundle 相关接口获取</p>
        :type BundleId: str
        :param _BundleInfo: <p>Bundle信息</p>
        :type BundleInfo: str
        :param _GitConfigId: <p>Git配置ID，可通过 Git 配置相关接口获取</p>
        :type GitConfigId: str
        :param _GitBranch: <p>Git分支信息</p>
        :type GitBranch: str
        """
        self._WorkspaceId = None
        self._BaseInfo = None
        self._Trigger = None
        self._ParamList = None
        self._LabelList = None
        self._Alarm = None
        self._MonitorMetric = None
        self._AdvanceConfig = None
        self._TaskList = None
        self._BundleId = None
        self._BundleInfo = None
        self._GitConfigId = None
        self._GitBranch = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def BaseInfo(self):
        r"""<p>工作流基本信息。必填，其中 WorkflowName 必填且工作空间内唯一</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def Trigger(self):
        r"""<p>工作流调度配置</p>
        :rtype: list of WorkflowTriggerConfiguration
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def ParamList(self):
        r"""<p>工作流参数列表</p>
        :rtype: list of ParamInfo
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def LabelList(self):
        r"""<p>标签列表</p>
        :rtype: list of LabelBrief
        """
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def Alarm(self):
        r"""<p>工作流告警配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        """
        return self._Alarm

    @Alarm.setter
    def Alarm(self, Alarm):
        self._Alarm = Alarm

    @property
    def MonitorMetric(self):
        r"""<p>监控指标配置。若告警条件中选择了监控告警，则本字段必填</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        """
        return self._MonitorMetric

    @MonitorMetric.setter
    def MonitorMetric(self, MonitorMetric):
        self._MonitorMetric = MonitorMetric

    @property
    def AdvanceConfig(self):
        r"""<p>工作流高级设置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig

    @property
    def TaskList(self):
        r"""<p>工作流任务列表</p>
        :rtype: list of WorkflowTask
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def BundleId(self):
        r"""<p>BundleId，可通过 Bundle 相关接口获取</p>
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>Bundle信息</p>
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def GitConfigId(self):
        r"""<p>Git配置ID，可通过 Git 配置相关接口获取</p>
        :rtype: str
        """
        return self._GitConfigId

    @GitConfigId.setter
    def GitConfigId(self, GitConfigId):
        self._GitConfigId = GitConfigId

    @property
    def GitBranch(self):
        r"""<p>Git分支信息</p>
        :rtype: str
        """
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("BaseInfo") is not None:
            self._BaseInfo = WorkflowBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("Trigger") is not None:
            self._Trigger = []
            for item in params.get("Trigger"):
                obj = WorkflowTriggerConfiguration()
                obj._deserialize(item)
                self._Trigger.append(obj)
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        if params.get("LabelList") is not None:
            self._LabelList = []
            for item in params.get("LabelList"):
                obj = LabelBrief()
                obj._deserialize(item)
                self._LabelList.append(obj)
        if params.get("Alarm") is not None:
            self._Alarm = AlarmBrief()
            self._Alarm._deserialize(params.get("Alarm"))
        if params.get("MonitorMetric") is not None:
            self._MonitorMetric = MonitorMetricBrief()
            self._MonitorMetric._deserialize(params.get("MonitorMetric"))
        if params.get("AdvanceConfig") is not None:
            self._AdvanceConfig = WorkflowAdvanceConfig()
            self._AdvanceConfig._deserialize(params.get("AdvanceConfig"))
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = WorkflowTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        self._GitConfigId = params.get("GitConfigId")
        self._GitBranch = params.get("GitBranch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    r"""CreateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>创建工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>创建工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateWorkflowRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkflowRsp(AbstractModel):
    r"""CreateWorkflowRsp

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        """
        self._WorkflowId = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceRequest(AbstractModel):
    r"""CreateWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceName: <p>工作空间名称，max_len=128</p>
        :type WorkspaceName: str
        :param _WorkspaceRegion: <p>工作空间地域（如 ap-guangzhou），max_len=64</p>
        :type WorkspaceRegion: str
        :param _Description: <p>工作空间描述，max_len=300</p>
        :type Description: str
        """
        self._WorkspaceName = None
        self._WorkspaceRegion = None
        self._Description = None

    @property
    def WorkspaceName(self):
        r"""<p>工作空间名称，max_len=128</p>
        :rtype: str
        """
        return self._WorkspaceName

    @WorkspaceName.setter
    def WorkspaceName(self, WorkspaceName):
        self._WorkspaceName = WorkspaceName

    @property
    def WorkspaceRegion(self):
        r"""<p>工作空间地域（如 ap-guangzhou），max_len=64</p>
        :rtype: str
        """
        return self._WorkspaceRegion

    @WorkspaceRegion.setter
    def WorkspaceRegion(self, WorkspaceRegion):
        self._WorkspaceRegion = WorkspaceRegion

    @property
    def Description(self):
        r"""<p>工作空间描述，max_len=300</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._WorkspaceName = params.get("WorkspaceName")
        self._WorkspaceRegion = params.get("WorkspaceRegion")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceResponse(AbstractModel):
    r"""CreateWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>创建成功的工作空间ID</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>创建成功的工作空间ID</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateWorkspaceRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceRoleRequest(AbstractModel):
    r"""CreateWorkspaceRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间id</p>
        :type WorkspaceId: str
        :param _BasicInfo: <p>角色基础信息</p>
        :type BasicInfo: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        :param _Permissions: <p>角色权限</p>
        :type Permissions: list of RolePermission
        """
        self._WorkspaceId = None
        self._BasicInfo = None
        self._Permissions = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间id</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def BasicInfo(self):
        r"""<p>角色基础信息</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def Permissions(self):
        r"""<p>角色权限</p>
        :rtype: list of RolePermission
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("BasicInfo") is not None:
            self._BasicInfo = RoleBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = RolePermission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceRoleResponse(AbstractModel):
    r"""CreateWorkspaceRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>创建工作空间角色返回</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRoleResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>创建工作空间角色返回</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRoleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateWorkspaceRoleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceRoleResult(AbstractModel):
    r"""创建工作空间角色结果

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
        :type RoleId: str
        :param _Status: 创建工作空间角色是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._RoleId = None
        self._Status = None

    @property
    def RoleId(self):
        r"""角色id
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def Status(self):
        r"""创建工作空间角色是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceRsp(AbstractModel):
    r"""创建工作空间响应

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 创建成功的工作空间ID
        :type WorkspaceId: str
        """
        self._WorkspaceId = None

    @property
    def WorkspaceId(self):
        r"""创建成功的工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCatalogRequest(AbstractModel):
    r"""DeleteCatalog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogName: 数据目录名
        :type CatalogName: str
        :param _WorkspaceId: 调用时所在workspace唯一id
        :type WorkspaceId: str
        :param _ConnectionId: 数据源连接ID，可选（融合版新增字段）。非空→走分析版路径，空/缺省→走专业版TcLake路径
        :type ConnectionId: str
        """
        self._CatalogName = None
        self._WorkspaceId = None
        self._ConnectionId = None

    @property
    def CatalogName(self):
        r"""数据目录名
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def WorkspaceId(self):
        r"""调用时所在workspace唯一id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ConnectionId(self):
        r"""数据源连接ID，可选（融合版新增字段）。非空→走分析版路径，空/缺省→走专业版TcLake路径
        :rtype: str
        """
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId


    def _deserialize(self, params):
        self._CatalogName = params.get("CatalogName")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ConnectionId = params.get("ConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCatalogResponse(AbstractModel):
    r"""DeleteCatalog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteCatalogRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteCatalogRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteCatalogRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteCatalogRsp(AbstractModel):
    r"""删除数据目录描述的响应

    """

    def __init__(self):
        r"""
        :param _Result: 操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        r"""操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsoleGroupsRequest(AbstractModel):
    r"""DeleteConsoleGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: <p>要删除的用户组 ID 列表，单次最多100个</p>
        :type GroupIds: list of str
        """
        self._GroupIds = None

    @property
    def GroupIds(self):
        r"""<p>要删除的用户组 ID 列表，单次最多100个</p>
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsoleGroupsResponse(AbstractModel):
    r"""DeleteConsoleGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteConsoleGroupsRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteConsoleGroupsRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteConsoleGroupsRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteConsoleGroupsRsp(AbstractModel):
    r"""删除控制台用户组响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileRequest(AbstractModel):
    r"""DeleteFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :type WorkspaceId: str
        :param _FileId: <p>文件 ID。来源：CreateFile / ListFiles / GetFile 接口返回的 FileId</p>
        :type FileId: str
        :param _FileType: <p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :type FileType: str
        """
        self._WorkspaceId = None
        self._FileId = None
        self._FileType = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileId(self):
        r"""<p>文件 ID。来源：CreateFile / ListFiles / GetFile 接口返回的 FileId</p>
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileType(self):
        r"""<p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileId = params.get("FileId")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileResponse(AbstractModel):
    r"""DeleteFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteFileResult(AbstractModel):
    r"""文件删除结果

    """

    def __init__(self):
        r"""
        :param _FileId: <p>被删除的文件 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param _Status: <p>删除是否成功</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._FileId = None
        self._Status = None

    @property
    def FileId(self):
        r"""<p>被删除的文件 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Status(self):
        r"""<p>删除是否成功</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFolderRequest(AbstractModel):
    r"""DeleteFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间id</p>
        :type WorkspaceId: str
        :param _Folder: <p>待删除的文件夹</p>
        :type Folder: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        :param _ForceDelete: <p>软删除还是从回收站硬删除</p><p>枚举值：</p><ul><li>false： 软删除到回收站</li><li>true： 从回收站硬删除</li></ul>
        :type ForceDelete: bool
        """
        self._WorkspaceId = None
        self._Folder = None
        self._ForceDelete = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间id</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Folder(self):
        r"""<p>待删除的文件夹</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._Folder

    @Folder.setter
    def Folder(self, Folder):
        self._Folder = Folder

    @property
    def ForceDelete(self):
        r"""<p>软删除还是从回收站硬删除</p><p>枚举值：</p><ul><li>false： 软删除到回收站</li><li>true： 从回收站硬删除</li></ul>
        :rtype: bool
        """
        return self._ForceDelete

    @ForceDelete.setter
    def ForceDelete(self, ForceDelete):
        self._ForceDelete = ForceDelete


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Folder") is not None:
            self._Folder = FolderLocator()
            self._Folder._deserialize(params.get("Folder"))
        self._ForceDelete = params.get("ForceDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFolderResponse(AbstractModel):
    r"""DeleteFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>删除文件夹结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteFolderRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>删除文件夹结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteFolderRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteFolderRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteFolderRsp(AbstractModel):
    r"""删除文件夹回包

    """

    def __init__(self):
        r"""
        :param _Status: <p>删除文件夹状态</p>
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""<p>删除文件夹状态</p>
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSchemaRequest(AbstractModel):
    r"""DeleteSchema请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogName: 数据目录名
        :type CatalogName: str
        :param _SchemaName: 数据库名
        :type SchemaName: str
        :param _WorkspaceId: 调用时所在workspace唯一id
        :type WorkspaceId: str
        :param _ConnectionId: 数据源连接ID，可选（融合版新增字段）。分析版catalog不支持删除schema，传入非空时服务端返回ANA_CATALOG_NOT_SUPPORTED错误
        :type ConnectionId: str
        """
        self._CatalogName = None
        self._SchemaName = None
        self._WorkspaceId = None
        self._ConnectionId = None

    @property
    def CatalogName(self):
        r"""数据目录名
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def SchemaName(self):
        r"""数据库名
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def WorkspaceId(self):
        r"""调用时所在workspace唯一id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ConnectionId(self):
        r"""数据源连接ID，可选（融合版新增字段）。分析版catalog不支持删除schema，传入非空时服务端返回ANA_CATALOG_NOT_SUPPORTED错误
        :rtype: str
        """
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId


    def _deserialize(self, params):
        self._CatalogName = params.get("CatalogName")
        self._SchemaName = params.get("SchemaName")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ConnectionId = params.get("ConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSchemaResponse(AbstractModel):
    r"""DeleteSchema返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteSchemaRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteSchemaRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteSchemaRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteSchemaRsp(AbstractModel):
    r"""删除Schema的响应

    """

    def __init__(self):
        r"""
        :param _Result: 操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        r"""操作结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowRequest(AbstractModel):
    r"""DeleteWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>待删除的工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        """
        self._WorkspaceId = None
        self._WorkflowId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>待删除的工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    r"""DeleteWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>删除工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>删除工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteWorkflowRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkflowRsp(AbstractModel):
    r"""DeleteWorkflowRsp

    """

    def __init__(self):
        r"""
        :param _Status: 删除状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""删除状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkspaceRequest(AbstractModel):
    r"""DeleteWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID</p>
        :type WorkspaceId: str
        """
        self._WorkspaceId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkspaceResponse(AbstractModel):
    r"""DeleteWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>操作结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>操作结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteWorkspaceRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkspaceRoleRequest(AbstractModel):
    r"""DeleteWorkspaceRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _RoleId: 角色ID
        :type RoleId: str
        """
        self._WorkspaceId = None
        self._RoleId = None

    @property
    def WorkspaceId(self):
        r"""工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def RoleId(self):
        r"""角色ID
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkspaceRoleResponse(AbstractModel):
    r"""DeleteWorkspaceRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除工作空间角色结果
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRoleResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""删除工作空间角色结果
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRoleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteWorkspaceRoleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkspaceRoleResult(AbstractModel):
    r"""删除工作空间角色结果

    """

    def __init__(self):
        r"""
        :param _Status: 删除工作空间角色是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""删除工作空间角色是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkspaceRsp(AbstractModel):
    r"""删除工作空间响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependOnBrief(AbstractModel):
    r"""任务依赖简要信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过 ListWorkflowTasks 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        """
        self._TaskId = None
        self._TaskName = None

    @property
    def TaskId(self):
        r"""任务ID，可通过 ListWorkflowTasks 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchOption(AbstractModel):
    r"""数据获取选项，用于get/list请求中控制响应返回哪些额外内容

    """

    def __init__(self):
        r"""
        :param _FetchPermissions: <p>是否在响应中返回权限列表，默认false</p>
        :type FetchPermissions: bool
        :param _FetchFeatureTableDetail: <p>是否获取特征表详情，当AssetType为TABLE时有效</p>
        :type FetchFeatureTableDetail: bool
        :param _FilterPermissions: <p>按权限过滤，传入权限列表，仅返回当前用户拥有指定权限的实体。例如传入[&quot;SELECT_TABLE&quot;]则仅返回当前用户有SELECT_TABLE权限的实体。只对list接口生效，为空时不进行权限过滤</p>
        :type FilterPermissions: list of str
        :param _FetchOwners: <p>是否在响应中返回负责人信息。不传或为true时返回负责人信息（默认返回），显式传false时不返回</p>
        :type FetchOwners: bool
        :param _FetchUserInfo: <p>是否将用户Uin转换为用户名(userName)。影响范围：Audit中的CreatorName/LastModifierName、MetaOwner中的OwnerName。不传或为true时执行转换（默认转换），显式传false时不转换</p>
        :type FetchUserInfo: bool
        :param _FetchMask: <p>是否返回字段脱敏策略信息，默认不返回，传true则会查询表字段对应的字段脱敏策略信息</p>
        :type FetchMask: bool
        :param _FetchTags: <p>是否返回标签信息，默认不返回。传true时，GetTable/ListTables/GetCatalog/ListCatalogs/GetSchema/ListSchemas/GetView/ListViews/GetFunction/ListFunctions/GetVolume/ListVolumes/GetModel/ListModels等接口会在对应实体中返回标签（Tags）字段</p>
        :type FetchTags: bool
        :param _FetchDimensions: <p>是否返回字段关联的字典维度信息，默认不传，不返回</p>
        :type FetchDimensions: bool
        """
        self._FetchPermissions = None
        self._FetchFeatureTableDetail = None
        self._FilterPermissions = None
        self._FetchOwners = None
        self._FetchUserInfo = None
        self._FetchMask = None
        self._FetchTags = None
        self._FetchDimensions = None

    @property
    def FetchPermissions(self):
        r"""<p>是否在响应中返回权限列表，默认false</p>
        :rtype: bool
        """
        return self._FetchPermissions

    @FetchPermissions.setter
    def FetchPermissions(self, FetchPermissions):
        self._FetchPermissions = FetchPermissions

    @property
    def FetchFeatureTableDetail(self):
        r"""<p>是否获取特征表详情，当AssetType为TABLE时有效</p>
        :rtype: bool
        """
        return self._FetchFeatureTableDetail

    @FetchFeatureTableDetail.setter
    def FetchFeatureTableDetail(self, FetchFeatureTableDetail):
        self._FetchFeatureTableDetail = FetchFeatureTableDetail

    @property
    def FilterPermissions(self):
        r"""<p>按权限过滤，传入权限列表，仅返回当前用户拥有指定权限的实体。例如传入[&quot;SELECT_TABLE&quot;]则仅返回当前用户有SELECT_TABLE权限的实体。只对list接口生效，为空时不进行权限过滤</p>
        :rtype: list of str
        """
        return self._FilterPermissions

    @FilterPermissions.setter
    def FilterPermissions(self, FilterPermissions):
        self._FilterPermissions = FilterPermissions

    @property
    def FetchOwners(self):
        r"""<p>是否在响应中返回负责人信息。不传或为true时返回负责人信息（默认返回），显式传false时不返回</p>
        :rtype: bool
        """
        return self._FetchOwners

    @FetchOwners.setter
    def FetchOwners(self, FetchOwners):
        self._FetchOwners = FetchOwners

    @property
    def FetchUserInfo(self):
        r"""<p>是否将用户Uin转换为用户名(userName)。影响范围：Audit中的CreatorName/LastModifierName、MetaOwner中的OwnerName。不传或为true时执行转换（默认转换），显式传false时不转换</p>
        :rtype: bool
        """
        return self._FetchUserInfo

    @FetchUserInfo.setter
    def FetchUserInfo(self, FetchUserInfo):
        self._FetchUserInfo = FetchUserInfo

    @property
    def FetchMask(self):
        r"""<p>是否返回字段脱敏策略信息，默认不返回，传true则会查询表字段对应的字段脱敏策略信息</p>
        :rtype: bool
        """
        return self._FetchMask

    @FetchMask.setter
    def FetchMask(self, FetchMask):
        self._FetchMask = FetchMask

    @property
    def FetchTags(self):
        r"""<p>是否返回标签信息，默认不返回。传true时，GetTable/ListTables/GetCatalog/ListCatalogs/GetSchema/ListSchemas/GetView/ListViews/GetFunction/ListFunctions/GetVolume/ListVolumes/GetModel/ListModels等接口会在对应实体中返回标签（Tags）字段</p>
        :rtype: bool
        """
        return self._FetchTags

    @FetchTags.setter
    def FetchTags(self, FetchTags):
        self._FetchTags = FetchTags

    @property
    def FetchDimensions(self):
        r"""<p>是否返回字段关联的字典维度信息，默认不传，不返回</p>
        :rtype: bool
        """
        return self._FetchDimensions

    @FetchDimensions.setter
    def FetchDimensions(self, FetchDimensions):
        self._FetchDimensions = FetchDimensions


    def _deserialize(self, params):
        self._FetchPermissions = params.get("FetchPermissions")
        self._FetchFeatureTableDetail = params.get("FetchFeatureTableDetail")
        self._FilterPermissions = params.get("FilterPermissions")
        self._FetchOwners = params.get("FetchOwners")
        self._FetchUserInfo = params.get("FetchUserInfo")
        self._FetchMask = params.get("FetchMask")
        self._FetchTags = params.get("FetchTags")
        self._FetchDimensions = params.get("FetchDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileConfig(AbstractModel):
    r"""文件运行配置

    """

    def __init__(self):
        r"""
        :param _Params: <p>高级运行参数，变量替换用，map-json String,String</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _ResourceId: <p>执行资源 ID。来源：ListComputeResources 接口返回的 ResourceId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _DefaultCatalog: <p>默认 catalog</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCatalog: str
        :param _DefaultSchema: <p>默认 schema</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultSchema: str
        :param _AdvanceConfig: <p>高级配置，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceConfig: str
        :param _ExtraParams: <p>扩展参数，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParams: str
        :param _Widgets: <p>Notebook 交互控件定义，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Widgets: str
        :param _OutputConf: <p>各单元格输出配置。仅 Get 出参返回，入参忽略</p>
        :type OutputConf: list of FileOutputConf
        :param _SqlSyntax: <p>SQL脚本语法标记</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlSyntax: str
        :param _ClusterId: <p>平台集群id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._Params = None
        self._ResourceId = None
        self._DefaultCatalog = None
        self._DefaultSchema = None
        self._AdvanceConfig = None
        self._ExtraParams = None
        self._Widgets = None
        self._OutputConf = None
        self._SqlSyntax = None
        self._ClusterId = None

    @property
    def Params(self):
        r"""<p>高级运行参数，变量替换用，map-json String,String</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def ResourceId(self):
        r"""<p>执行资源 ID。来源：ListComputeResources 接口返回的 ResourceId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DefaultCatalog(self):
        r"""<p>默认 catalog</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultCatalog

    @DefaultCatalog.setter
    def DefaultCatalog(self, DefaultCatalog):
        self._DefaultCatalog = DefaultCatalog

    @property
    def DefaultSchema(self):
        r"""<p>默认 schema</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultSchema

    @DefaultSchema.setter
    def DefaultSchema(self, DefaultSchema):
        self._DefaultSchema = DefaultSchema

    @property
    def AdvanceConfig(self):
        r"""<p>高级配置，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig

    @property
    def ExtraParams(self):
        r"""<p>扩展参数，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExtraParams

    @ExtraParams.setter
    def ExtraParams(self, ExtraParams):
        self._ExtraParams = ExtraParams

    @property
    def Widgets(self):
        r"""<p>Notebook 交互控件定义，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Widgets

    @Widgets.setter
    def Widgets(self, Widgets):
        self._Widgets = Widgets

    @property
    def OutputConf(self):
        r"""<p>各单元格输出配置。仅 Get 出参返回，入参忽略</p>
        :rtype: list of FileOutputConf
        """
        return self._OutputConf

    @OutputConf.setter
    def OutputConf(self, OutputConf):
        self._OutputConf = OutputConf

    @property
    def SqlSyntax(self):
        r"""<p>SQL脚本语法标记</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SqlSyntax

    @SqlSyntax.setter
    def SqlSyntax(self, SqlSyntax):
        self._SqlSyntax = SqlSyntax

    @property
    def ClusterId(self):
        r"""<p>平台集群id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Params = params.get("Params")
        self._ResourceId = params.get("ResourceId")
        self._DefaultCatalog = params.get("DefaultCatalog")
        self._DefaultSchema = params.get("DefaultSchema")
        self._AdvanceConfig = params.get("AdvanceConfig")
        self._ExtraParams = params.get("ExtraParams")
        self._Widgets = params.get("Widgets")
        if params.get("OutputConf") is not None:
            self._OutputConf = []
            for item in params.get("OutputConf"):
                obj = FileOutputConf()
                obj._deserialize(item)
                self._OutputConf.append(obj)
        self._SqlSyntax = params.get("SqlSyntax")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    r"""文件详情

    """

    def __init__(self):
        r"""
        :param _AppId: <p>主账号 AppId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _WorkspaceId: <p>工作空间 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _FileId: <p>文件 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param _FileName: <p>文件名，含后缀</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileType: <p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _Path: <p>文件在工作空间中的完整路径，以 / 开头，如 /etl/daily/demo.ipynb</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _FileConfig: <p>文件运行配置</p>
        :type FileConfig: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        :param _BundleId: <p>绑定的 BundleId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: <p>绑定的 BundleInfo，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        :param _Status: <p>文件状态。active=正常，deleted=已删除</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _OwnerUserName: <p>文件负责人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserName: str
        :param _CreateUserUin: <p>创建人子账号 Uin</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _UpdateUserUin: <p>最近更新人子账号 Uin</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _CreateTime: <p>创建时间，毫秒级时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>最近更新时间，毫秒级时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Storage: <p>文件存储信息。仅当请求 IncludeContent=true 时返回内容</p>
        :type Storage: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        :param _Permissions: <p>当前调用方对该文件的权限点列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: str
        :param _ReleaseStatus: <p>是否已发布</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseStatus: bool
        :param _ResourceMode: <p>资源模式。1=分布式，2=单节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMode: int
        :param _AsyncOperation: ZIP 异步创建时透传 Workspace 作业信息；普通同步创建或其他复用该返回结构的接口不设置该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOperation: :class:`tencentcloud.databuddy.v20260715.models.AsyncOperation`
        """
        self._AppId = None
        self._WorkspaceId = None
        self._FileId = None
        self._FileName = None
        self._FileType = None
        self._Path = None
        self._FileConfig = None
        self._BundleId = None
        self._BundleInfo = None
        self._Status = None
        self._OwnerUserName = None
        self._CreateUserUin = None
        self._UpdateUserUin = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Storage = None
        self._Permissions = None
        self._ReleaseStatus = None
        self._ResourceMode = None
        self._AsyncOperation = None

    @property
    def AppId(self):
        r"""<p>主账号 AppId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileId(self):
        r"""<p>文件 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileName(self):
        r"""<p>文件名，含后缀</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""<p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Path(self):
        r"""<p>文件在工作空间中的完整路径，以 / 开头，如 /etl/daily/demo.ipynb</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def FileConfig(self):
        r"""<p>文件运行配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        """
        return self._FileConfig

    @FileConfig.setter
    def FileConfig(self, FileConfig):
        self._FileConfig = FileConfig

    @property
    def BundleId(self):
        r"""<p>绑定的 BundleId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>绑定的 BundleInfo，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def Status(self):
        r"""<p>文件状态。active=正常，deleted=已删除</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUserName(self):
        r"""<p>文件负责人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserName

    @OwnerUserName.setter
    def OwnerUserName(self, OwnerUserName):
        self._OwnerUserName = OwnerUserName

    @property
    def CreateUserUin(self):
        r"""<p>创建人子账号 Uin</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def UpdateUserUin(self):
        r"""<p>最近更新人子账号 Uin</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def CreateTime(self):
        r"""<p>创建时间，毫秒级时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>最近更新时间，毫秒级时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Storage(self):
        r"""<p>文件存储信息。仅当请求 IncludeContent=true 时返回内容</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Permissions(self):
        r"""<p>当前调用方对该文件的权限点列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ReleaseStatus(self):
        r"""<p>是否已发布</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def ResourceMode(self):
        r"""<p>资源模式。1=分布式，2=单节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceMode

    @ResourceMode.setter
    def ResourceMode(self, ResourceMode):
        self._ResourceMode = ResourceMode

    @property
    def AsyncOperation(self):
        r"""ZIP 异步创建时透传 Workspace 作业信息；普通同步创建或其他复用该返回结构的接口不设置该字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AsyncOperation`
        """
        return self._AsyncOperation

    @AsyncOperation.setter
    def AsyncOperation(self, AsyncOperation):
        self._AsyncOperation = AsyncOperation


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileId = params.get("FileId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._Path = params.get("Path")
        if params.get("FileConfig") is not None:
            self._FileConfig = FileConfig()
            self._FileConfig._deserialize(params.get("FileConfig"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        self._Status = params.get("Status")
        self._OwnerUserName = params.get("OwnerUserName")
        self._CreateUserUin = params.get("CreateUserUin")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Storage") is not None:
            self._Storage = FileStorage()
            self._Storage._deserialize(params.get("Storage"))
        self._Permissions = params.get("Permissions")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._ResourceMode = params.get("ResourceMode")
        if params.get("AsyncOperation") is not None:
            self._AsyncOperation = AsyncOperation()
            self._AsyncOperation._deserialize(params.get("AsyncOperation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileMeta(AbstractModel):
    r"""文件元数据

    """

    def __init__(self):
        r"""
        :param _FileId: <p>文件id</p>
        :type FileId: str
        :param _FileName: <p>文件/文件夹名称</p>
        :type FileName: str
        :param _FileType: <p>文件类型</p>
        :type FileType: str
        :param _CreateTime: <p>创建时间，毫秒秒级时间戳</p><p>参数格式：时间戳</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间</p><p>参数格式：时间戳字符串</p>
        :type UpdateTime: str
        :param _AllowActions: <p>acl权限类型</p>
        :type AllowActions: list of str
        :param _IsFavorite: <p>是否收藏</p>
        :type IsFavorite: bool
        :param _PathName: <p>文件path</p>
        :type PathName: str
        :param _IsSystemGenerated: <p>是否系统创建</p>
        :type IsSystemGenerated: bool
        """
        self._FileId = None
        self._FileName = None
        self._FileType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AllowActions = None
        self._IsFavorite = None
        self._PathName = None
        self._IsSystemGenerated = None

    @property
    def FileId(self):
        r"""<p>文件id</p>
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileName(self):
        r"""<p>文件/文件夹名称</p>
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""<p>文件类型</p>
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CreateTime(self):
        r"""<p>创建时间，毫秒秒级时间戳</p><p>参数格式：时间戳</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p><p>参数格式：时间戳字符串</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AllowActions(self):
        r"""<p>acl权限类型</p>
        :rtype: list of str
        """
        return self._AllowActions

    @AllowActions.setter
    def AllowActions(self, AllowActions):
        self._AllowActions = AllowActions

    @property
    def IsFavorite(self):
        r"""<p>是否收藏</p>
        :rtype: bool
        """
        return self._IsFavorite

    @IsFavorite.setter
    def IsFavorite(self, IsFavorite):
        self._IsFavorite = IsFavorite

    @property
    def PathName(self):
        r"""<p>文件path</p>
        :rtype: str
        """
        return self._PathName

    @PathName.setter
    def PathName(self, PathName):
        self._PathName = PathName

    @property
    def IsSystemGenerated(self):
        r"""<p>是否系统创建</p>
        :rtype: bool
        """
        return self._IsSystemGenerated

    @IsSystemGenerated.setter
    def IsSystemGenerated(self, IsSystemGenerated):
        self._IsSystemGenerated = IsSystemGenerated


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AllowActions = params.get("AllowActions")
        self._IsFavorite = params.get("IsFavorite")
        self._PathName = params.get("PathName")
        self._IsSystemGenerated = params.get("IsSystemGenerated")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileNode(AbstractModel):
    r"""文件节点

    """

    def __init__(self):
        r"""
        :param _Node: <p>当前节点</p>
        :type Node: :class:`tencentcloud.databuddy.v20260715.models.FileMeta`
        :param _Parent: <p>父节点</p>
        :type Parent: :class:`tencentcloud.databuddy.v20260715.models.FileMeta`
        :param _Creator: <p>创建人</p>
        :type Creator: :class:`tencentcloud.databuddy.v20260715.models.UserInfo`
        :param _Owner: <p>拥有者</p>
        :type Owner: :class:`tencentcloud.databuddy.v20260715.models.UserInfo`
        :param _NodeType: <p>节点类型</p>
        :type NodeType: str
        :param _OriginPath: <p>原始路径</p>
        :type OriginPath: str
        :param _DeleteTime: <p>回收时间</p>
        :type DeleteTime: str
        :param _GitConfig: <p>文件git配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitConfig: :class:`tencentcloud.databuddy.v20260715.models.GitRepoConfig`
        """
        self._Node = None
        self._Parent = None
        self._Creator = None
        self._Owner = None
        self._NodeType = None
        self._OriginPath = None
        self._DeleteTime = None
        self._GitConfig = None

    @property
    def Node(self):
        r"""<p>当前节点</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileMeta`
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Parent(self):
        r"""<p>父节点</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileMeta`
        """
        return self._Parent

    @Parent.setter
    def Parent(self, Parent):
        self._Parent = Parent

    @property
    def Creator(self):
        r"""<p>创建人</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UserInfo`
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Owner(self):
        r"""<p>拥有者</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UserInfo`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def NodeType(self):
        r"""<p>节点类型</p>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def OriginPath(self):
        r"""<p>原始路径</p>
        :rtype: str
        """
        return self._OriginPath

    @OriginPath.setter
    def OriginPath(self, OriginPath):
        self._OriginPath = OriginPath

    @property
    def DeleteTime(self):
        r"""<p>回收时间</p>
        :rtype: str
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def GitConfig(self):
        r"""<p>文件git配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GitRepoConfig`
        """
        return self._GitConfig

    @GitConfig.setter
    def GitConfig(self, GitConfig):
        self._GitConfig = GitConfig


    def _deserialize(self, params):
        if params.get("Node") is not None:
            self._Node = FileMeta()
            self._Node._deserialize(params.get("Node"))
        if params.get("Parent") is not None:
            self._Parent = FileMeta()
            self._Parent._deserialize(params.get("Parent"))
        if params.get("Creator") is not None:
            self._Creator = UserInfo()
            self._Creator._deserialize(params.get("Creator"))
        if params.get("Owner") is not None:
            self._Owner = UserInfo()
            self._Owner._deserialize(params.get("Owner"))
        self._NodeType = params.get("NodeType")
        self._OriginPath = params.get("OriginPath")
        self._DeleteTime = params.get("DeleteTime")
        if params.get("GitConfig") is not None:
            self._GitConfig = GitRepoConfig()
            self._GitConfig._deserialize(params.get("GitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileOutputConf(AbstractModel):
    r"""Notebook/Python单元格输出配置

    """

    def __init__(self):
        r"""
        :param _CellId: 单元格 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CellId: str
        :param _DashboardConf: Dashboard 图表配置，JSON 字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type DashboardConf: str
        :param _OutputPath: 执行结果文件的预签名下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputPath: str
        """
        self._CellId = None
        self._DashboardConf = None
        self._OutputPath = None

    @property
    def CellId(self):
        r"""单元格 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CellId

    @CellId.setter
    def CellId(self, CellId):
        self._CellId = CellId

    @property
    def DashboardConf(self):
        r"""Dashboard 图表配置，JSON 字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DashboardConf

    @DashboardConf.setter
    def DashboardConf(self, DashboardConf):
        self._DashboardConf = DashboardConf

    @property
    def OutputPath(self):
        r"""执行结果文件的预签名下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath


    def _deserialize(self, params):
        self._CellId = params.get("CellId")
        self._DashboardConf = params.get("DashboardConf")
        self._OutputPath = params.get("OutputPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileStorage(AbstractModel):
    r"""文件存储

    """

    def __init__(self):
        r"""
        :param _StorageType: 存储类型
        :type StorageType: int
        :param _StoragePath: 存储路径
        :type StoragePath: str
        :param _Content: 文件内容
        :type Content: str
        """
        self._StorageType = None
        self._StoragePath = None
        self._Content = None

    @property
    def StorageType(self):
        r"""存储类型
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StoragePath(self):
        r"""存储路径
        :rtype: str
        """
        return self._StoragePath

    @StoragePath.setter
    def StoragePath(self, StoragePath):
        self._StoragePath = StoragePath

    @property
    def Content(self):
        r"""文件内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._StoragePath = params.get("StoragePath")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FolderLocator(AbstractModel):
    r"""文件夹定位器

    """

    def __init__(self):
        r"""
        :param _FolderId: <p>节点id</p>
        :type FolderId: str
        :param _PathName: <p>节点path</p>
        :type PathName: str
        """
        self._FolderId = None
        self._PathName = None

    @property
    def FolderId(self):
        r"""<p>节点id</p>
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def PathName(self):
        r"""<p>节点path</p>
        :rtype: str
        """
        return self._PathName

    @PathName.setter
    def PathName(self, PathName):
        self._PathName = PathName


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._PathName = params.get("PathName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFileRequest(AbstractModel):
    r"""GetFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :type WorkspaceId: str
        :param _FileId: <p>文件 ID。来源：CreateFile / ListFiles 接口返回的 FileId。与 FilePath 二选一</p>
        :type FileId: str
        :param _FileType: <p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :type FileType: str
        :param _IncludeContent: <p>是否返回文件内容。true 时 Storage.Content 返回 base64 内容，默认 false</p>
        :type IncludeContent: bool
        :param _VersionId: <p>文件版本 ID。来源：ListFileVersions 接口返回的 VersionId。不传则读取最新版本</p>
        :type VersionId: str
        :param _FilePath: <p>文件完整路径，以 / 开头，如 /etl/daily/demo.ipynb。与 FileId 二选一</p>
        :type FilePath: str
        """
        self._WorkspaceId = None
        self._FileId = None
        self._FileType = None
        self._IncludeContent = None
        self._VersionId = None
        self._FilePath = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileId(self):
        r"""<p>文件 ID。来源：CreateFile / ListFiles 接口返回的 FileId。与 FilePath 二选一</p>
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileType(self):
        r"""<p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IncludeContent(self):
        r"""<p>是否返回文件内容。true 时 Storage.Content 返回 base64 内容，默认 false</p>
        :rtype: bool
        """
        return self._IncludeContent

    @IncludeContent.setter
    def IncludeContent(self, IncludeContent):
        self._IncludeContent = IncludeContent

    @property
    def VersionId(self):
        r"""<p>文件版本 ID。来源：ListFileVersions 接口返回的 VersionId。不传则读取最新版本</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def FilePath(self):
        r"""<p>文件完整路径，以 / 开头，如 /etl/daily/demo.ipynb。与 FileId 二选一</p>
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileId = params.get("FileId")
        self._FileType = params.get("FileType")
        self._IncludeContent = params.get("IncludeContent")
        self._VersionId = params.get("VersionId")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFileResponse(AbstractModel):
    r"""GetFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = FileInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetFolderRequest(AbstractModel):
    r"""GetFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间id</p>
        :type WorkspaceId: str
        :param _Folder: <p>文件夹定位</p>
        :type Folder: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        self._WorkspaceId = None
        self._Folder = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间id</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Folder(self):
        r"""<p>文件夹定位</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._Folder

    @Folder.setter
    def Folder(self, Folder):
        self._Folder = Folder


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Folder") is not None:
            self._Folder = FolderLocator()
            self._Folder._deserialize(params.get("Folder"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFolderResponse(AbstractModel):
    r"""GetFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>文件夹详情结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.GetFolderRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>文件夹详情结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetFolderRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetFolderRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetFolderRsp(AbstractModel):
    r"""获取文件夹回包

    """

    def __init__(self):
        r"""
        :param _Folder: <p>文件夹信息</p>
        :type Folder: :class:`tencentcloud.databuddy.v20260715.models.FileNode`
        """
        self._Folder = None

    @property
    def Folder(self):
        r"""<p>文件夹信息</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileNode`
        """
        return self._Folder

    @Folder.setter
    def Folder(self, Folder):
        self._Folder = Folder


    def _deserialize(self, params):
        if params.get("Folder") is not None:
            self._Folder = FileNode()
            self._Folder._deserialize(params.get("Folder"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowRequest(AbstractModel):
    r"""GetWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        """
        self._WorkspaceId = None
        self._WorkflowId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowResponse(AbstractModel):
    r"""GetWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>获取工作流详细信息响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>获取工作流详细信息响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetWorkflowRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkflowRsp(AbstractModel):
    r"""GetWorkflowRsp

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _BaseInfo: <p>工作流基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfoDetail`
        :param _Trigger: <p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Trigger: list of WorkflowTriggerConfiguration
        :param _ParamList: <p>工作流参数列表 参数名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamList: list of ParamInfo
        :param _LabelList: <p>标签 标签名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelList: list of LabelBrief
        :param _Alarm: <p>工作流告警配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarm: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        :param _MonitorMetric: <p>监控指标配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorMetric: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        :param _AdvanceConfig: <p>工作流高级设置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceConfig: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        :param _TaskList: <p>工作流任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskList: list of WorkflowTask
        :param _BundleId: <p>工作流绑定的 Bundle唯一标识，未绑定时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: <p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        :param _GitConfigId: <p>Git配置ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitConfigId: str
        :param _GitBranch: <p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitBranch: str
        """
        self._WorkspaceId = None
        self._BaseInfo = None
        self._Trigger = None
        self._ParamList = None
        self._LabelList = None
        self._Alarm = None
        self._MonitorMetric = None
        self._AdvanceConfig = None
        self._TaskList = None
        self._BundleId = None
        self._BundleInfo = None
        self._GitConfigId = None
        self._GitBranch = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def BaseInfo(self):
        r"""<p>工作流基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfoDetail`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def Trigger(self):
        r"""<p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTriggerConfiguration
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def ParamList(self):
        r"""<p>工作流参数列表 参数名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def LabelList(self):
        r"""<p>标签 标签名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LabelBrief
        """
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def Alarm(self):
        r"""<p>工作流告警配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        """
        return self._Alarm

    @Alarm.setter
    def Alarm(self, Alarm):
        self._Alarm = Alarm

    @property
    def MonitorMetric(self):
        r"""<p>监控指标配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        """
        return self._MonitorMetric

    @MonitorMetric.setter
    def MonitorMetric(self, MonitorMetric):
        self._MonitorMetric = MonitorMetric

    @property
    def AdvanceConfig(self):
        r"""<p>工作流高级设置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig

    @property
    def TaskList(self):
        r"""<p>工作流任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTask
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def BundleId(self):
        r"""<p>工作流绑定的 Bundle唯一标识，未绑定时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def GitConfigId(self):
        r"""<p>Git配置ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitConfigId

    @GitConfigId.setter
    def GitConfigId(self, GitConfigId):
        self._GitConfigId = GitConfigId

    @property
    def GitBranch(self):
        r"""<p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("BaseInfo") is not None:
            self._BaseInfo = WorkflowBaseInfoDetail()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("Trigger") is not None:
            self._Trigger = []
            for item in params.get("Trigger"):
                obj = WorkflowTriggerConfiguration()
                obj._deserialize(item)
                self._Trigger.append(obj)
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        if params.get("LabelList") is not None:
            self._LabelList = []
            for item in params.get("LabelList"):
                obj = LabelBrief()
                obj._deserialize(item)
                self._LabelList.append(obj)
        if params.get("Alarm") is not None:
            self._Alarm = AlarmBrief()
            self._Alarm._deserialize(params.get("Alarm"))
        if params.get("MonitorMetric") is not None:
            self._MonitorMetric = MonitorMetricBrief()
            self._MonitorMetric._deserialize(params.get("MonitorMetric"))
        if params.get("AdvanceConfig") is not None:
            self._AdvanceConfig = WorkflowAdvanceConfig()
            self._AdvanceConfig._deserialize(params.get("AdvanceConfig"))
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = WorkflowTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        self._GitConfigId = params.get("GitConfigId")
        self._GitBranch = params.get("GitBranch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowRunRequest(AbstractModel):
    r"""GetWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowRunId: <p>工作流运行ID，可通过 ListWorkflowRuns 获取。必填</p>
        :type WorkflowRunId: str
        """
        self._WorkspaceId = None
        self._WorkflowRunId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID，可通过 ListWorkflowRuns 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowRunResponse(AbstractModel):
    r"""GetWorkflowRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>查询工作流运行详情响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>查询工作流运行详情响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetWorkflowRunRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkflowRunRsp(AbstractModel):
    r"""查询工作流运行详情响应。

    """

    def __init__(self):
        r"""
        :param _WorkflowRun: 工作流运行信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRun: :class:`tencentcloud.databuddy.v20260715.models.WorkflowRun`
        """
        self._WorkflowRun = None

    @property
    def WorkflowRun(self):
        r"""工作流运行信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowRun`
        """
        return self._WorkflowRun

    @WorkflowRun.setter
    def WorkflowRun(self, WorkflowRun):
        self._WorkflowRun = WorkflowRun


    def _deserialize(self, params):
        if params.get("WorkflowRun") is not None:
            self._WorkflowRun = WorkflowRun()
            self._WorkflowRun._deserialize(params.get("WorkflowRun"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowTaskRunRequest(AbstractModel):
    r"""GetWorkflowTaskRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowTaskRunId: <p>任务运行ID，可通过 ListWorkflowTaskRuns 获取。必填</p>
        :type WorkflowTaskRunId: str
        :param _InnerWorkflowTaskRunListOption: <p>内嵌工作流任务运行列表选项（仅限 FOR_EACH 任务使用）。非必填</p>
        :type InnerWorkflowTaskRunListOption: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRunListOption`
        """
        self._WorkspaceId = None
        self._WorkflowTaskRunId = None
        self._InnerWorkflowTaskRunListOption = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowTaskRunId(self):
        r"""<p>任务运行ID，可通过 ListWorkflowTaskRuns 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowTaskRunId

    @WorkflowTaskRunId.setter
    def WorkflowTaskRunId(self, WorkflowTaskRunId):
        self._WorkflowTaskRunId = WorkflowTaskRunId

    @property
    def InnerWorkflowTaskRunListOption(self):
        r"""<p>内嵌工作流任务运行列表选项（仅限 FOR_EACH 任务使用）。非必填</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRunListOption`
        """
        return self._InnerWorkflowTaskRunListOption

    @InnerWorkflowTaskRunListOption.setter
    def InnerWorkflowTaskRunListOption(self, InnerWorkflowTaskRunListOption):
        self._InnerWorkflowTaskRunListOption = InnerWorkflowTaskRunListOption


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowTaskRunId = params.get("WorkflowTaskRunId")
        if params.get("InnerWorkflowTaskRunListOption") is not None:
            self._InnerWorkflowTaskRunListOption = InnerWorkflowTaskRunListOption()
            self._InnerWorkflowTaskRunListOption._deserialize(params.get("InnerWorkflowTaskRunListOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowTaskRunResponse(AbstractModel):
    r"""GetWorkflowTaskRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>查询任务运行详情响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>查询任务运行详情响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetWorkflowTaskRunRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkflowTaskRunRsp(AbstractModel):
    r"""GetWorkflowTaskRunRsp

    """

    def __init__(self):
        r"""
        :param _TaskName: <p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _WorkflowTaskRunId: <p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTaskRunId: str
        :param _RunState: <p>运行状态。取值参考工作流任务运行状态枚举，如 Pending / Running / Succeeded / Failed / Killed</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _WorkspaceId: <p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowRunId: <p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _TaskId: <p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskTypeName: <p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param _TaskVersionId: <p>任务版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskVersionId: str
        :param _TriggerType: <p>触发类型</p><p>枚举值：</p><ul><li>Scheduler： 调度触发</li><li>Manual： 手动触发</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param _ResourceGroupId: <p>所属资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ErrorCodeString: <p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        :param _RunUserUin: <p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _RunUserName: <p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserName: str
        :param _CreateUserUin: <p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _JobId: <p>执行平台执行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _CreateTime: <p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _DependenceFinishedTime: <p>依赖任务完成时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependenceFinishedTime: str
        :param _RunStartTime: <p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _RunEndTime: <p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunEndTime: str
        :param _RunCostTime: <p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunCostTime: str
        :param _WaitTime: <p>等待时长（依赖就绪到开始运行的等待耗时），单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WaitTime: str
        :param _IssueTime: <p>下发执行平台时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueTime: str
        :param _TimeZone: <p>时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeZone: str
        :param _DependOnList: <p>依赖上游任务ID列表。保留字段，暂时返回为[]</p><p>保留字段，暂时返回为[]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnList: list of str
        :param _RunParams: <p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunParams: str
        :param _TaskTypeExtensions: <p>任务扩展信息，包含脚本路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeExtensions: str
        :param _LeftCoordinate: <p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftCoordinate: float
        :param _TopCoordinate: <p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TopCoordinate: float
        :param _RetryTimes: <p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryTimes: int
        :param _WorkflowName: <p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _RerunTimes: <p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RerunTimes: int
        :param _IsLatestRun: <p>是否最新一次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLatestRun: bool
        :param _ResourceGroupInfoList: <p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupInfoList: list of ResourceGroupInfo
        :param _ErrorMessage: <p>错误消息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _RunResult: <p>运行结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunResult: str
        :param _InnerWorkflowTaskRun: <p>内嵌工作流任务运行详情（仅限 FOR_EACH 任务，其他任务类型不返回该字段）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerWorkflowTaskRun: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRun`
        :param _ScheduledTime: <p>计划调度时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTime: str
        """
        self._TaskName = None
        self._WorkflowTaskRunId = None
        self._RunState = None
        self._WorkspaceId = None
        self._WorkflowId = None
        self._WorkflowRunId = None
        self._TaskId = None
        self._TaskTypeName = None
        self._TaskVersionId = None
        self._TriggerType = None
        self._ResourceGroupId = None
        self._ErrorCodeString = None
        self._RunUserUin = None
        self._RunUserName = None
        self._CreateUserUin = None
        self._JobId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DependenceFinishedTime = None
        self._RunStartTime = None
        self._RunEndTime = None
        self._RunCostTime = None
        self._WaitTime = None
        self._IssueTime = None
        self._TimeZone = None
        self._DependOnList = None
        self._RunParams = None
        self._TaskTypeExtensions = None
        self._LeftCoordinate = None
        self._TopCoordinate = None
        self._RetryTimes = None
        self._WorkflowName = None
        self._RerunTimes = None
        self._IsLatestRun = None
        self._ResourceGroupInfoList = None
        self._ErrorMessage = None
        self._RunResult = None
        self._InnerWorkflowTaskRun = None
        self._ScheduledTime = None

    @property
    def TaskName(self):
        r"""<p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowTaskRunId(self):
        r"""<p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowTaskRunId

    @WorkflowTaskRunId.setter
    def WorkflowTaskRunId(self, WorkflowTaskRunId):
        self._WorkflowTaskRunId = WorkflowTaskRunId

    @property
    def RunState(self):
        r"""<p>运行状态。取值参考工作流任务运行状态枚举，如 Pending / Running / Succeeded / Failed / Killed</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTypeName(self):
        r"""<p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def TaskVersionId(self):
        r"""<p>任务版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskVersionId

    @TaskVersionId.setter
    def TaskVersionId(self, TaskVersionId):
        self._TaskVersionId = TaskVersionId

    @property
    def TriggerType(self):
        r"""<p>触发类型</p><p>枚举值：</p><ul><li>Scheduler： 调度触发</li><li>Manual： 手动触发</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ResourceGroupId(self):
        r"""<p>所属资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ErrorCodeString(self):
        r"""<p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString

    @property
    def RunUserUin(self):
        r"""<p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def RunUserName(self):
        r"""<p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserName

    @RunUserName.setter
    def RunUserName(self, RunUserName):
        self._RunUserName = RunUserName

    @property
    def CreateUserUin(self):
        r"""<p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def JobId(self):
        r"""<p>执行平台执行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CreateTime(self):
        r"""<p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DependenceFinishedTime(self):
        r"""<p>依赖任务完成时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependenceFinishedTime

    @DependenceFinishedTime.setter
    def DependenceFinishedTime(self, DependenceFinishedTime):
        self._DependenceFinishedTime = DependenceFinishedTime

    @property
    def RunStartTime(self):
        r"""<p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def RunEndTime(self):
        r"""<p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def RunCostTime(self):
        r"""<p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunCostTime

    @RunCostTime.setter
    def RunCostTime(self, RunCostTime):
        self._RunCostTime = RunCostTime

    @property
    def WaitTime(self):
        r"""<p>等待时长（依赖就绪到开始运行的等待耗时），单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaitTime

    @WaitTime.setter
    def WaitTime(self, WaitTime):
        self._WaitTime = WaitTime

    @property
    def IssueTime(self):
        r"""<p>下发执行平台时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime

    @property
    def TimeZone(self):
        r"""<p>时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DependOnList(self):
        r"""<p>依赖上游任务ID列表。保留字段，暂时返回为[]</p><p>保留字段，暂时返回为[]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DependOnList

    @DependOnList.setter
    def DependOnList(self, DependOnList):
        self._DependOnList = DependOnList

    @property
    def RunParams(self):
        r"""<p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunParams

    @RunParams.setter
    def RunParams(self, RunParams):
        self._RunParams = RunParams

    @property
    def TaskTypeExtensions(self):
        r"""<p>任务扩展信息，包含脚本路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeExtensions

    @TaskTypeExtensions.setter
    def TaskTypeExtensions(self, TaskTypeExtensions):
        self._TaskTypeExtensions = TaskTypeExtensions

    @property
    def LeftCoordinate(self):
        r"""<p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._LeftCoordinate

    @LeftCoordinate.setter
    def LeftCoordinate(self, LeftCoordinate):
        self._LeftCoordinate = LeftCoordinate

    @property
    def TopCoordinate(self):
        r"""<p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TopCoordinate

    @TopCoordinate.setter
    def TopCoordinate(self, TopCoordinate):
        self._TopCoordinate = TopCoordinate

    @property
    def RetryTimes(self):
        r"""<p>重试次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def WorkflowName(self):
        r"""<p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def RerunTimes(self):
        r"""<p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RerunTimes

    @RerunTimes.setter
    def RerunTimes(self, RerunTimes):
        self._RerunTimes = RerunTimes

    @property
    def IsLatestRun(self):
        r"""<p>是否最新一次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLatestRun

    @IsLatestRun.setter
    def IsLatestRun(self, IsLatestRun):
        self._IsLatestRun = IsLatestRun

    @property
    def ResourceGroupInfoList(self):
        r"""<p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceGroupInfo
        """
        return self._ResourceGroupInfoList

    @ResourceGroupInfoList.setter
    def ResourceGroupInfoList(self, ResourceGroupInfoList):
        self._ResourceGroupInfoList = ResourceGroupInfoList

    @property
    def ErrorMessage(self):
        r"""<p>错误消息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RunResult(self):
        r"""<p>运行结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunResult

    @RunResult.setter
    def RunResult(self, RunResult):
        self._RunResult = RunResult

    @property
    def InnerWorkflowTaskRun(self):
        r"""<p>内嵌工作流任务运行详情（仅限 FOR_EACH 任务，其他任务类型不返回该字段）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRun`
        """
        return self._InnerWorkflowTaskRun

    @InnerWorkflowTaskRun.setter
    def InnerWorkflowTaskRun(self, InnerWorkflowTaskRun):
        self._InnerWorkflowTaskRun = InnerWorkflowTaskRun

    @property
    def ScheduledTime(self):
        r"""<p>计划调度时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduledTime

    @ScheduledTime.setter
    def ScheduledTime(self, ScheduledTime):
        self._ScheduledTime = ScheduledTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._WorkflowTaskRunId = params.get("WorkflowTaskRunId")
        self._RunState = params.get("RunState")
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._TaskId = params.get("TaskId")
        self._TaskTypeName = params.get("TaskTypeName")
        self._TaskVersionId = params.get("TaskVersionId")
        self._TriggerType = params.get("TriggerType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ErrorCodeString = params.get("ErrorCodeString")
        self._RunUserUin = params.get("RunUserUin")
        self._RunUserName = params.get("RunUserName")
        self._CreateUserUin = params.get("CreateUserUin")
        self._JobId = params.get("JobId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DependenceFinishedTime = params.get("DependenceFinishedTime")
        self._RunStartTime = params.get("RunStartTime")
        self._RunEndTime = params.get("RunEndTime")
        self._RunCostTime = params.get("RunCostTime")
        self._WaitTime = params.get("WaitTime")
        self._IssueTime = params.get("IssueTime")
        self._TimeZone = params.get("TimeZone")
        self._DependOnList = params.get("DependOnList")
        self._RunParams = params.get("RunParams")
        self._TaskTypeExtensions = params.get("TaskTypeExtensions")
        self._LeftCoordinate = params.get("LeftCoordinate")
        self._TopCoordinate = params.get("TopCoordinate")
        self._RetryTimes = params.get("RetryTimes")
        self._WorkflowName = params.get("WorkflowName")
        self._RerunTimes = params.get("RerunTimes")
        self._IsLatestRun = params.get("IsLatestRun")
        if params.get("ResourceGroupInfoList") is not None:
            self._ResourceGroupInfoList = []
            for item in params.get("ResourceGroupInfoList"):
                obj = ResourceGroupInfo()
                obj._deserialize(item)
                self._ResourceGroupInfoList.append(obj)
        self._ErrorMessage = params.get("ErrorMessage")
        self._RunResult = params.get("RunResult")
        if params.get("InnerWorkflowTaskRun") is not None:
            self._InnerWorkflowTaskRun = InnerWorkflowTaskRun()
            self._InnerWorkflowTaskRun._deserialize(params.get("InnerWorkflowTaskRun"))
        self._ScheduledTime = params.get("ScheduledTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkspaceRequest(AbstractModel):
    r"""GetWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID</p>
        :type WorkspaceId: str
        """
        self._WorkspaceId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkspaceResponse(AbstractModel):
    r"""GetWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>工作空间详情</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.GetWorkspaceRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>工作空间详情</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkspaceRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetWorkspaceRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkspaceRsp(AbstractModel):
    r"""查询工作空间详情响应

    """

    def __init__(self):
        r"""
        :param _WorkspaceInfo: 工作空间详情
        :type WorkspaceInfo: :class:`tencentcloud.databuddy.v20260715.models.WorkspaceInfo`
        """
        self._WorkspaceInfo = None

    @property
    def WorkspaceInfo(self):
        r"""工作空间详情
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkspaceInfo`
        """
        return self._WorkspaceInfo

    @WorkspaceInfo.setter
    def WorkspaceInfo(self, WorkspaceInfo):
        self._WorkspaceInfo = WorkspaceInfo


    def _deserialize(self, params):
        if params.get("WorkspaceInfo") is not None:
            self._WorkspaceInfo = WorkspaceInfo()
            self._WorkspaceInfo._deserialize(params.get("WorkspaceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitRepoConfig(AbstractModel):
    r"""git配置

    """

    def __init__(self):
        r"""
        :param _SparseCheckout: <p>检出规则</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SparseCheckout: :class:`tencentcloud.databuddy.v20260715.models.SparseCheckoutConfig`
        :param _RepoUrl: <p>Git 仓库地址</p>
        :type RepoUrl: str
        :param _Branch: <p>分支名</p>
        :type Branch: str
        :param _AuthConfigName: <p>关联的 gitAuth 配置名称</p>
        :type AuthConfigName: str
        """
        self._SparseCheckout = None
        self._RepoUrl = None
        self._Branch = None
        self._AuthConfigName = None

    @property
    def SparseCheckout(self):
        r"""<p>检出规则</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.SparseCheckoutConfig`
        """
        return self._SparseCheckout

    @SparseCheckout.setter
    def SparseCheckout(self, SparseCheckout):
        self._SparseCheckout = SparseCheckout

    @property
    def RepoUrl(self):
        r"""<p>Git 仓库地址</p>
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def Branch(self):
        r"""<p>分支名</p>
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def AuthConfigName(self):
        r"""<p>关联的 gitAuth 配置名称</p>
        :rtype: str
        """
        return self._AuthConfigName

    @AuthConfigName.setter
    def AuthConfigName(self, AuthConfigName):
        self._AuthConfigName = AuthConfigName


    def _deserialize(self, params):
        if params.get("SparseCheckout") is not None:
            self._SparseCheckout = SparseCheckoutConfig()
            self._SparseCheckout._deserialize(params.get("SparseCheckout"))
        self._RepoUrl = params.get("RepoUrl")
        self._Branch = params.get("Branch")
        self._AuthConfigName = params.get("AuthConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InnerWorkflowTaskBrief(AbstractModel):
    r"""内嵌工作流任务简要信息（目前只有 FOR_EACH 工作流任务该字段才有值）

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _TaskTypeName: 任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        """
        self._TaskId = None
        self._TaskName = None
        self._TaskTypeName = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeName(self):
        r"""任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskTypeName = params.get("TaskTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InnerWorkflowTaskRun(AbstractModel):
    r"""内嵌工作流任务运行详情（仅限 FOR_EACH 任务）

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _Items: 迭代运行列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of InnerWorkflowTaskRunIteration
        :param _IterationCount: 迭代次数
注意：此字段可能返回 null，表示取不到有效值。
        :type IterationCount: int
        :param _FailureCount: 失败次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureCount: int
        :param _SuccessCount: 成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _InnerWorkflowId: 内嵌工作流ID，可通过 ListWorkflows 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerWorkflowId: str
        :param _InnerTaskId: 内嵌任务ID，可通过 ListWorkflowTasks 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTaskId: str
        :param _InnerTaskRunBizEnumInfos: 内嵌任务运行状态数量统计（实例业务枚举键值对列表）
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTaskRunBizEnumInfos: list of ScheduleBizEnumBrief
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._IterationCount = None
        self._FailureCount = None
        self._SuccessCount = None
        self._InnerWorkflowId = None
        self._InnerTaskId = None
        self._InnerTaskRunBizEnumInfos = None

    @property
    def PageNumber(self):
        r"""当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""迭代运行列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InnerWorkflowTaskRunIteration
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def IterationCount(self):
        r"""迭代次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IterationCount

    @IterationCount.setter
    def IterationCount(self, IterationCount):
        self._IterationCount = IterationCount

    @property
    def FailureCount(self):
        r"""失败次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailureCount

    @FailureCount.setter
    def FailureCount(self, FailureCount):
        self._FailureCount = FailureCount

    @property
    def SuccessCount(self):
        r"""成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def InnerWorkflowId(self):
        r"""内嵌工作流ID，可通过 ListWorkflows 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InnerWorkflowId

    @InnerWorkflowId.setter
    def InnerWorkflowId(self, InnerWorkflowId):
        self._InnerWorkflowId = InnerWorkflowId

    @property
    def InnerTaskId(self):
        r"""内嵌任务ID，可通过 ListWorkflowTasks 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InnerTaskId

    @InnerTaskId.setter
    def InnerTaskId(self, InnerTaskId):
        self._InnerTaskId = InnerTaskId

    @property
    def InnerTaskRunBizEnumInfos(self):
        r"""内嵌任务运行状态数量统计（实例业务枚举键值对列表）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScheduleBizEnumBrief
        """
        return self._InnerTaskRunBizEnumInfos

    @InnerTaskRunBizEnumInfos.setter
    def InnerTaskRunBizEnumInfos(self, InnerTaskRunBizEnumInfos):
        self._InnerTaskRunBizEnumInfos = InnerTaskRunBizEnumInfos


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InnerWorkflowTaskRunIteration()
                obj._deserialize(item)
                self._Items.append(obj)
        self._IterationCount = params.get("IterationCount")
        self._FailureCount = params.get("FailureCount")
        self._SuccessCount = params.get("SuccessCount")
        self._InnerWorkflowId = params.get("InnerWorkflowId")
        self._InnerTaskId = params.get("InnerTaskId")
        if params.get("InnerTaskRunBizEnumInfos") is not None:
            self._InnerTaskRunBizEnumInfos = []
            for item in params.get("InnerTaskRunBizEnumInfos"):
                obj = ScheduleBizEnumBrief()
                obj._deserialize(item)
                self._InnerTaskRunBizEnumInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InnerWorkflowTaskRunIteration(AbstractModel):
    r"""内嵌工作流单次迭代运行信息

    """

    def __init__(self):
        r"""
        :param _WorkflowRunId: <p>内嵌工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _IterationIndex: <p>迭代序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IterationIndex: str
        :param _RunStartTime: <p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _RunEndTime: <p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunEndTime: str
        :param _RunState: <p>运行状态（参考工作流运行状态枚举）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _RunCostTime: <p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunCostTime: str
        :param _WorkflowParams: <p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowParams: str
        :param _ErrorCodeString: <p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        :param _InnerTaskRun: <p>内嵌工作流内部的任务运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTaskRun: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRunIterationBrief`
        """
        self._WorkflowRunId = None
        self._IterationIndex = None
        self._RunStartTime = None
        self._RunEndTime = None
        self._RunState = None
        self._RunCostTime = None
        self._WorkflowParams = None
        self._ErrorCodeString = None
        self._InnerTaskRun = None

    @property
    def WorkflowRunId(self):
        r"""<p>内嵌工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def IterationIndex(self):
        r"""<p>迭代序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IterationIndex

    @IterationIndex.setter
    def IterationIndex(self, IterationIndex):
        self._IterationIndex = IterationIndex

    @property
    def RunStartTime(self):
        r"""<p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def RunEndTime(self):
        r"""<p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def RunState(self):
        r"""<p>运行状态（参考工作流运行状态枚举）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def RunCostTime(self):
        r"""<p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunCostTime

    @RunCostTime.setter
    def RunCostTime(self, RunCostTime):
        self._RunCostTime = RunCostTime

    @property
    def WorkflowParams(self):
        r"""<p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def ErrorCodeString(self):
        r"""<p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString

    @property
    def InnerTaskRun(self):
        r"""<p>内嵌工作流内部的任务运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskRunIterationBrief`
        """
        return self._InnerTaskRun

    @InnerTaskRun.setter
    def InnerTaskRun(self, InnerTaskRun):
        self._InnerTaskRun = InnerTaskRun


    def _deserialize(self, params):
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._IterationIndex = params.get("IterationIndex")
        self._RunStartTime = params.get("RunStartTime")
        self._RunEndTime = params.get("RunEndTime")
        self._RunState = params.get("RunState")
        self._RunCostTime = params.get("RunCostTime")
        self._WorkflowParams = params.get("WorkflowParams")
        self._ErrorCodeString = params.get("ErrorCodeString")
        if params.get("InnerTaskRun") is not None:
            self._InnerTaskRun = InnerWorkflowTaskRunIterationBrief()
            self._InnerTaskRun._deserialize(params.get("InnerTaskRun"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InnerWorkflowTaskRunIterationBrief(AbstractModel):
    r"""内嵌工作流迭代中的任务运行简要信息

    """

    def __init__(self):
        r"""
        :param _WorkflowTaskRunId: <p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTaskRunId: str
        :param _IterationIndex: <p>迭代序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IterationIndex: str
        :param _RunStartTime: <p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _RunEndTime: <p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunEndTime: str
        :param _RunState: <p>运行状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _RunCostTime: <p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunCostTime: str
        :param _TaskParams: <p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskParams: str
        :param _ErrorCodeString: <p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        """
        self._WorkflowTaskRunId = None
        self._IterationIndex = None
        self._RunStartTime = None
        self._RunEndTime = None
        self._RunState = None
        self._RunCostTime = None
        self._TaskParams = None
        self._ErrorCodeString = None

    @property
    def WorkflowTaskRunId(self):
        r"""<p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowTaskRunId

    @WorkflowTaskRunId.setter
    def WorkflowTaskRunId(self, WorkflowTaskRunId):
        self._WorkflowTaskRunId = WorkflowTaskRunId

    @property
    def IterationIndex(self):
        r"""<p>迭代序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IterationIndex

    @IterationIndex.setter
    def IterationIndex(self, IterationIndex):
        self._IterationIndex = IterationIndex

    @property
    def RunStartTime(self):
        r"""<p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def RunEndTime(self):
        r"""<p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def RunState(self):
        r"""<p>运行状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def RunCostTime(self):
        r"""<p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunCostTime

    @RunCostTime.setter
    def RunCostTime(self, RunCostTime):
        self._RunCostTime = RunCostTime

    @property
    def TaskParams(self):
        r"""<p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskParams

    @TaskParams.setter
    def TaskParams(self, TaskParams):
        self._TaskParams = TaskParams

    @property
    def ErrorCodeString(self):
        r"""<p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString


    def _deserialize(self, params):
        self._WorkflowTaskRunId = params.get("WorkflowTaskRunId")
        self._IterationIndex = params.get("IterationIndex")
        self._RunStartTime = params.get("RunStartTime")
        self._RunEndTime = params.get("RunEndTime")
        self._RunState = params.get("RunState")
        self._RunCostTime = params.get("RunCostTime")
        self._TaskParams = params.get("TaskParams")
        self._ErrorCodeString = params.get("ErrorCodeString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InnerWorkflowTaskRunListOption(AbstractModel):
    r"""内嵌工作流任务运行列表选项（仅限 FOR_EACH 任务使用）

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>分页页码，从 1 开始。非必填，默认 1</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: <p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _RunStates: <p>迭代运行状态，精确匹配。非必填，多选（多个值之间为 OR 关系）。</p><p>可填 SUCCESS / FAILED 等，具体参考本接口出参 InnerWorkflowTaskRunIteration.RunState 字段返回值。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStates: list of str
        """
        self._PageNumber = None
        self._PageSize = None
        self._RunStates = None

    @property
    def PageNumber(self):
        r"""<p>分页页码，从 1 开始。非必填，默认 1</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def RunStates(self):
        r"""<p>迭代运行状态，精确匹配。非必填，多选（多个值之间为 OR 关系）。</p><p>可填 SUCCESS / FAILED 等，具体参考本接口出参 InnerWorkflowTaskRunIteration.RunState 字段返回值。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RunStates

    @RunStates.setter
    def RunStates(self, RunStates):
        self._RunStates = RunStates


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._RunStates = params.get("RunStates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    r"""扩展信息键值对

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
        r"""键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class KillWorkflowRunRequest(AbstractModel):
    r"""KillWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        :param _WorkflowRunIds: <p>待终止的工作流运行ID列表，可通过 ListWorkflowRuns 获取</p>
        :type WorkflowRunIds: list of str
        :param _KillAllRuns: <p>是否终止该工作流下所有未进入终态的运行。非必填，默认 false</p>
        :type KillAllRuns: bool
        :param _OnlyKillPendingRuns: <p>是否只终止处于等待中（Pending）状态的运行。非必填，默认 false</p>
        :type OnlyKillPendingRuns: bool
        """
        self._WorkspaceId = None
        self._WorkflowId = None
        self._WorkflowRunIds = None
        self._KillAllRuns = None
        self._OnlyKillPendingRuns = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowRunIds(self):
        r"""<p>待终止的工作流运行ID列表，可通过 ListWorkflowRuns 获取</p>
        :rtype: list of str
        """
        return self._WorkflowRunIds

    @WorkflowRunIds.setter
    def WorkflowRunIds(self, WorkflowRunIds):
        self._WorkflowRunIds = WorkflowRunIds

    @property
    def KillAllRuns(self):
        r"""<p>是否终止该工作流下所有未进入终态的运行。非必填，默认 false</p>
        :rtype: bool
        """
        return self._KillAllRuns

    @KillAllRuns.setter
    def KillAllRuns(self, KillAllRuns):
        self._KillAllRuns = KillAllRuns

    @property
    def OnlyKillPendingRuns(self):
        r"""<p>是否只终止处于等待中（Pending）状态的运行。非必填，默认 false</p>
        :rtype: bool
        """
        return self._OnlyKillPendingRuns

    @OnlyKillPendingRuns.setter
    def OnlyKillPendingRuns(self, OnlyKillPendingRuns):
        self._OnlyKillPendingRuns = OnlyKillPendingRuns


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowRunIds = params.get("WorkflowRunIds")
        self._KillAllRuns = params.get("KillAllRuns")
        self._OnlyKillPendingRuns = params.get("OnlyKillPendingRuns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillWorkflowRunResponse(AbstractModel):
    r"""KillWorkflowRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>终止工作流的运行响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>终止工作流的运行响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AsyncActionRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class LabelBrief(AbstractModel):
    r"""标签信息

    """

    def __init__(self):
        r"""
        :param _LabelKey: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelKey: str
        :param _LabelValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelKeyId: 标签名称ID，可通过标签相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelKeyId: str
        :param _LabelValueId: 标签值ID，可通过标签相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValueId: str
        """
        self._LabelKey = None
        self._LabelValue = None
        self._LabelKeyId = None
        self._LabelValueId = None

    @property
    def LabelKey(self):
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelKey

    @LabelKey.setter
    def LabelKey(self, LabelKey):
        self._LabelKey = LabelKey

    @property
    def LabelValue(self):
        r"""标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelKeyId(self):
        r"""标签名称ID，可通过标签相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelKeyId

    @LabelKeyId.setter
    def LabelKeyId(self, LabelKeyId):
        self._LabelKeyId = LabelKeyId

    @property
    def LabelValueId(self):
        r"""标签值ID，可通过标签相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelValueId

    @LabelValueId.setter
    def LabelValueId(self, LabelValueId):
        self._LabelValueId = LabelValueId


    def _deserialize(self, params):
        self._LabelKey = params.get("LabelKey")
        self._LabelValue = params.get("LabelValue")
        self._LabelKeyId = params.get("LabelKeyId")
        self._LabelValueId = params.get("LabelValueId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleGroupUsersRequest(AbstractModel):
    r"""ListConsoleGroupUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: <p>用户组 ID，可通过 ListConsoleGroups 接口获取</p>
        :type GroupId: str
        :param _UserKeyword: <p>用户名称或 UIN 模糊匹配</p>
        :type UserKeyword: str
        :param _UserUins: <p>通过 UIN 批量查询用户信息</p>
        :type UserUins: list of str
        :param _OrderBys: <p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :type OrderBys: list of OrderBy
        :param _PageNumber: <p>页码，从1开始，默认1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认10，最小10，最大100</p>
        :type PageSize: int
        """
        self._GroupId = None
        self._UserKeyword = None
        self._UserUins = None
        self._OrderBys = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def GroupId(self):
        r"""<p>用户组 ID，可通过 ListConsoleGroups 接口获取</p>
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserKeyword(self):
        r"""<p>用户名称或 UIN 模糊匹配</p>
        :rtype: str
        """
        return self._UserKeyword

    @UserKeyword.setter
    def UserKeyword(self, UserKeyword):
        self._UserKeyword = UserKeyword

    @property
    def UserUins(self):
        r"""<p>通过 UIN 批量查询用户信息</p>
        :rtype: list of str
        """
        return self._UserUins

    @UserUins.setter
    def UserUins(self, UserUins):
        self._UserUins = UserUins

    @property
    def OrderBys(self):
        r"""<p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys

    @property
    def PageNumber(self):
        r"""<p>页码，从1开始，默认1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认10，最小10，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._UserKeyword = params.get("UserKeyword")
        self._UserUins = params.get("UserUins")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleGroupUsersResponse(AbstractModel):
    r"""ListConsoleGroupUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupUsersRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupUsersRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListConsoleGroupUsersRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListConsoleGroupUsersRsp(AbstractModel):
    r"""查询控制台用户组成员列表响应

    """

    def __init__(self):
        r"""
        :param _Items: 用户组成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConsoleGroupUserInfo
        :param _PageNumber: 当前页码
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""用户组成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsoleGroupUserInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""当前页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConsoleGroupUserInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleGroupsRequest(AbstractModel):
    r"""ListConsoleGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页码，从1开始，默认1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认10，最小10，最大100</p>
        :type PageSize: int
        :param _GroupIds: <p>通过用户组ID批量查询；用户组ID可通过 ListConsoleGroups 接口获取</p>
        :type GroupIds: list of str
        :param _GroupKeyword: <p>用户组名称模糊匹配</p>
        :type GroupKeyword: str
        :param _OrderBys: <p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :type OrderBys: list of OrderBy
        """
        self._PageNumber = None
        self._PageSize = None
        self._GroupIds = None
        self._GroupKeyword = None
        self._OrderBys = None

    @property
    def PageNumber(self):
        r"""<p>页码，从1开始，默认1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认10，最小10，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def GroupIds(self):
        r"""<p>通过用户组ID批量查询；用户组ID可通过 ListConsoleGroups 接口获取</p>
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def GroupKeyword(self):
        r"""<p>用户组名称模糊匹配</p>
        :rtype: str
        """
        return self._GroupKeyword

    @GroupKeyword.setter
    def GroupKeyword(self, GroupKeyword):
        self._GroupKeyword = GroupKeyword

    @property
    def OrderBys(self):
        r"""<p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._GroupIds = params.get("GroupIds")
        self._GroupKeyword = params.get("GroupKeyword")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleGroupsResponse(AbstractModel):
    r"""ListConsoleGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupsRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupsRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListConsoleGroupsRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListConsoleGroupsRsp(AbstractModel):
    r"""查询控制台用户组列表响应

    """

    def __init__(self):
        r"""
        :param _Items: 用户组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConsoleGroupInfo
        :param _PageNumber: 当前页码
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""用户组列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsoleGroupInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""当前页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConsoleGroupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleRolesRequest(AbstractModel):
    r"""ListConsoleRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页码，从1开始，默认1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认10，最小10，最大100</p>
        :type PageSize: int
        :param _RoleKeyword: <p>角色名称或描述模糊匹配</p>
        :type RoleKeyword: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._RoleKeyword = None

    @property
    def PageNumber(self):
        r"""<p>页码，从1开始，默认1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认10，最小10，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def RoleKeyword(self):
        r"""<p>角色名称或描述模糊匹配</p>
        :rtype: str
        """
        return self._RoleKeyword

    @RoleKeyword.setter
    def RoleKeyword(self, RoleKeyword):
        self._RoleKeyword = RoleKeyword


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._RoleKeyword = params.get("RoleKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleRolesResponse(AbstractModel):
    r"""ListConsoleRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleRolesRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleRolesRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListConsoleRolesRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListConsoleRolesRsp(AbstractModel):
    r"""查询控制台角色列表响应

    """

    def __init__(self):
        r"""
        :param _Items: 角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConsoleRoleInfo
        :param _PageNumber: 当前页码
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsoleRoleInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""当前页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConsoleRoleInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleUsersRequest(AbstractModel):
    r"""ListConsoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页码，从1开始，默认1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认10，最小10，最大100</p>
        :type PageSize: int
        :param _UserKeyword: <p>用户名称与 UIN 模糊匹配</p>
        :type UserKeyword: str
        :param _RoleIds: <p>用于过滤角色关联的用户</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul><p>可通过 ListConsoleRoles 接口获取</p>
        :type RoleIds: list of str
        :param _OrderBys: <p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :type OrderBys: list of OrderBy
        """
        self._PageNumber = None
        self._PageSize = None
        self._UserKeyword = None
        self._RoleIds = None
        self._OrderBys = None

    @property
    def PageNumber(self):
        r"""<p>页码，从1开始，默认1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认10，最小10，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserKeyword(self):
        r"""<p>用户名称与 UIN 模糊匹配</p>
        :rtype: str
        """
        return self._UserKeyword

    @UserKeyword.setter
    def UserKeyword(self, UserKeyword):
        self._UserKeyword = UserKeyword

    @property
    def RoleIds(self):
        r"""<p>用于过滤角色关联的用户</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul><p>可通过 ListConsoleRoles 接口获取</p>
        :rtype: list of str
        """
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds

    @property
    def OrderBys(self):
        r"""<p>多字段排序，如 [{Name: &#39;CreateTime&#39;, Direction: &#39;Desc&#39;}, {Name: &#39;UserName&#39;, Direction: &#39;Asc&#39;}]，默认按创建时间降序</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._UserKeyword = params.get("UserKeyword")
        self._RoleIds = params.get("RoleIds")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConsoleUsersResponse(AbstractModel):
    r"""ListConsoleUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>控制台用户列表</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>控制台用户列表</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListConsoleUsersRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListConsoleUsersRsp(AbstractModel):
    r"""查询控制台用户列表响应

    """

    def __init__(self):
        r"""
        :param _Items: 用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConsoleUserInfo
        :param _PageNumber: 当前页码
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsoleUserInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""当前页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConsoleUserInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFilesRequest(AbstractModel):
    r"""ListFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间id</p>
        :type WorkspaceId: str
        :param _Parent: <p>父目录，不填默认查询根节点</p>
        :type Parent: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        :param _FileTypes: <p>按文件类型过滤</p>
        :type FileTypes: list of str
        :param _NameKeyword: <p>文件名模糊匹配</p>
        :type NameKeyword: str
        :param _OwnerUserUins: <p>按所有者UIN过滤，多值为或关系</p>
        :type OwnerUserUins: list of str
        :param _OnlyFolder: <p>是否只列出文件夹，默认 false</p>
        :type OnlyFolder: bool
        :param _OrderBys: <p>排序字段列表，如创建时间 [{Name: &#39;CreateTime&#39;, Direction: &#39;DESC&#39;}]，文件名称 [{Name: &#39;Name&#39;, Direction: &#39;ASC&#39;}]</p>
        :type OrderBys: list of OrderBy
        :param _PageNumber: <p>页码，默认1，最小值1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页条数，默认10，最小值10，最大值100</p><p>取值范围：[10, 100]</p>
        :type PageSize: int
        """
        self._WorkspaceId = None
        self._Parent = None
        self._FileTypes = None
        self._NameKeyword = None
        self._OwnerUserUins = None
        self._OnlyFolder = None
        self._OrderBys = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间id</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Parent(self):
        r"""<p>父目录，不填默认查询根节点</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._Parent

    @Parent.setter
    def Parent(self, Parent):
        self._Parent = Parent

    @property
    def FileTypes(self):
        r"""<p>按文件类型过滤</p>
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def NameKeyword(self):
        r"""<p>文件名模糊匹配</p>
        :rtype: str
        """
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword

    @property
    def OwnerUserUins(self):
        r"""<p>按所有者UIN过滤，多值为或关系</p>
        :rtype: list of str
        """
        return self._OwnerUserUins

    @OwnerUserUins.setter
    def OwnerUserUins(self, OwnerUserUins):
        self._OwnerUserUins = OwnerUserUins

    @property
    def OnlyFolder(self):
        r"""<p>是否只列出文件夹，默认 false</p>
        :rtype: bool
        """
        return self._OnlyFolder

    @OnlyFolder.setter
    def OnlyFolder(self, OnlyFolder):
        self._OnlyFolder = OnlyFolder

    @property
    def OrderBys(self):
        r"""<p>排序字段列表，如创建时间 [{Name: &#39;CreateTime&#39;, Direction: &#39;DESC&#39;}]，文件名称 [{Name: &#39;Name&#39;, Direction: &#39;ASC&#39;}]</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys

    @property
    def PageNumber(self):
        r"""<p>页码，默认1，最小值1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页条数，默认10，最小值10，最大值100</p><p>取值范围：[10, 100]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Parent") is not None:
            self._Parent = FolderLocator()
            self._Parent._deserialize(params.get("Parent"))
        self._FileTypes = params.get("FileTypes")
        self._NameKeyword = params.get("NameKeyword")
        self._OwnerUserUins = params.get("OwnerUserUins")
        self._OnlyFolder = params.get("OnlyFolder")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFilesResponse(AbstractModel):
    r"""ListFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>文件列表结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListFilesRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>文件列表结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListFilesRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListFilesRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListFilesRsp(AbstractModel):
    r"""查询文件信息结果

    """

    def __init__(self):
        r"""
        :param _Items: <p>文件/文件夹节点列表</p>
        :type Items: list of FileNode
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页条数</p>
        :type PageSize: int
        :param _TotalCount: <p>总条数</p>
        :type TotalCount: int
        :param _TotalPageNumber: <p>总页数</p>
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""<p>文件/文件夹节点列表</p>
        :rtype: list of FileNode
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页条数</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""<p>总条数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""<p>总页数</p>
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = FileNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSchemasRequest(AbstractModel):
    r"""ListSchemas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogName: <p>数据目录名</p>
        :type CatalogName: str
        :param _MaxResults: <p>最大结果条数</p>
        :type MaxResults: int
        :param _PageToken: <p>分页token</p>
        :type PageToken: str
        :param _WorkspaceId: <p>调用时所在workspace唯一id</p>
        :type WorkspaceId: str
        :param _FetchOption: <p>数据获取选项，可选，控制是否返回权限信息及按权限过滤</p>
        :type FetchOption: :class:`tencentcloud.databuddy.v20260715.models.FetchOption`
        :param _ConnectionId: 数据源连接ID，可选（融合版新增字段）。非空→走分析版路径，空/缺省→走专业版TcLake路径
        :type ConnectionId: str
        """
        self._CatalogName = None
        self._MaxResults = None
        self._PageToken = None
        self._WorkspaceId = None
        self._FetchOption = None
        self._ConnectionId = None

    @property
    def CatalogName(self):
        r"""<p>数据目录名</p>
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def MaxResults(self):
        r"""<p>最大结果条数</p>
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def PageToken(self):
        r"""<p>分页token</p>
        :rtype: str
        """
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def WorkspaceId(self):
        r"""<p>调用时所在workspace唯一id</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FetchOption(self):
        r"""<p>数据获取选项，可选，控制是否返回权限信息及按权限过滤</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FetchOption`
        """
        return self._FetchOption

    @FetchOption.setter
    def FetchOption(self, FetchOption):
        self._FetchOption = FetchOption

    @property
    def ConnectionId(self):
        r"""数据源连接ID，可选（融合版新增字段）。非空→走分析版路径，空/缺省→走专业版TcLake路径
        :rtype: str
        """
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId


    def _deserialize(self, params):
        self._CatalogName = params.get("CatalogName")
        self._MaxResults = params.get("MaxResults")
        self._PageToken = params.get("PageToken")
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("FetchOption") is not None:
            self._FetchOption = FetchOption()
            self._FetchOption._deserialize(params.get("FetchOption"))
        self._ConnectionId = params.get("ConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSchemasResponse(AbstractModel):
    r"""ListSchemas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>操作结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListSchemasRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>操作结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListSchemasRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListSchemasRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListSchemasRsp(AbstractModel):
    r"""获取schema列表响应

    """

    def __init__(self):
        r"""
        :param _Items: schema列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Schema
        :param _NextPageToken: 下页分页token
注意：此字段可能返回 null，表示取不到有效值。
        :type NextPageToken: str
        """
        self._Items = None
        self._NextPageToken = None

    @property
    def Items(self):
        r"""schema列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Schema
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextPageToken(self):
        r"""下页分页token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextPageToken

    @NextPageToken.setter
    def NextPageToken(self, NextPageToken):
        self._NextPageToken = NextPageToken


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Schema()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextPageToken = params.get("NextPageToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowRunsRequest(AbstractModel):
    r"""ListWorkflowRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _PageNumber: <p>分页页码，从 1 开始。非必填，默认 1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :type PageSize: int
        :param _WorkflowId: <p>工作流ID，精确匹配。非必填，单值</p>
        :type WorkflowId: str
        :param _WorkflowNameKeyword: <p>工作流名称关键字，对 WorkflowName 做模糊匹配。非必填，单值</p>
        :type WorkflowNameKeyword: str
        :param _CreateStartTime: <p>运行创建时间下界，范围匹配（CreateTime &gt;= 本值），单位：毫秒时间戳。<br>非必填，单值，对应出参 WorkflowRun.CreateTime</p>
        :type CreateStartTime: str
        :param _CreateEndTime: <p>运行创建时间上界，范围匹配（CreateTime &lt;= 本值），单位：毫秒时间戳。<br>非必填，单值，对应出参 WorkflowRun.CreateTime</p>
        :type CreateEndTime: str
        :param _RunStates: <p>运行状态，精确匹配。非必填，多选（多个值之间为 OR 关系）。运行状态。CREATE(&quot;初始化&quot;), QUEUED(&quot;等待中&quot;), PENDING(&quot;准备中&quot;), RUNNING(&quot;运行中&quot;), SKIPPED(&quot;跳过运行&quot;), SUCCESS(&quot;成功&quot;), FAILED(&quot;失败&quot;), TERMINATING(&quot;终止中&quot;), TERMINATED(&quot;终止&quot;), CANCELLED(&quot;被手动终止&quot;)等</p>
        :type RunStates: list of str
        :param _ErrorCodeStrings: <p>错误码，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :type ErrorCodeStrings: list of str
        :param _RunUserUins: <p>运行人UIN，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :type RunUserUins: list of str
        :param _LabelKeyIds: <p>标签名称ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :type LabelKeyIds: list of str
        :param _LabelValueIds: <p>标签值ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :type LabelValueIds: list of str
        :param _OrderBys: <p>排序条件，多个之间按数组顺序表示优先级。非必填，默认按 CreateTime Desc。<br>可排序字段白名单：CreateTime、EndTime、RunCostTime</p>
        :type OrderBys: list of OrderBy
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._WorkflowId = None
        self._WorkflowNameKeyword = None
        self._CreateStartTime = None
        self._CreateEndTime = None
        self._RunStates = None
        self._ErrorCodeStrings = None
        self._RunUserUins = None
        self._LabelKeyIds = None
        self._LabelValueIds = None
        self._OrderBys = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        r"""<p>分页页码，从 1 开始。非必填，默认 1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，精确匹配。非必填，单值</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowNameKeyword(self):
        r"""<p>工作流名称关键字，对 WorkflowName 做模糊匹配。非必填，单值</p>
        :rtype: str
        """
        return self._WorkflowNameKeyword

    @WorkflowNameKeyword.setter
    def WorkflowNameKeyword(self, WorkflowNameKeyword):
        self._WorkflowNameKeyword = WorkflowNameKeyword

    @property
    def CreateStartTime(self):
        r"""<p>运行创建时间下界，范围匹配（CreateTime &gt;= 本值），单位：毫秒时间戳。<br>非必填，单值，对应出参 WorkflowRun.CreateTime</p>
        :rtype: str
        """
        return self._CreateStartTime

    @CreateStartTime.setter
    def CreateStartTime(self, CreateStartTime):
        self._CreateStartTime = CreateStartTime

    @property
    def CreateEndTime(self):
        r"""<p>运行创建时间上界，范围匹配（CreateTime &lt;= 本值），单位：毫秒时间戳。<br>非必填，单值，对应出参 WorkflowRun.CreateTime</p>
        :rtype: str
        """
        return self._CreateEndTime

    @CreateEndTime.setter
    def CreateEndTime(self, CreateEndTime):
        self._CreateEndTime = CreateEndTime

    @property
    def RunStates(self):
        r"""<p>运行状态，精确匹配。非必填，多选（多个值之间为 OR 关系）。运行状态。CREATE(&quot;初始化&quot;), QUEUED(&quot;等待中&quot;), PENDING(&quot;准备中&quot;), RUNNING(&quot;运行中&quot;), SKIPPED(&quot;跳过运行&quot;), SUCCESS(&quot;成功&quot;), FAILED(&quot;失败&quot;), TERMINATING(&quot;终止中&quot;), TERMINATED(&quot;终止&quot;), CANCELLED(&quot;被手动终止&quot;)等</p>
        :rtype: list of str
        """
        return self._RunStates

    @RunStates.setter
    def RunStates(self, RunStates):
        self._RunStates = RunStates

    @property
    def ErrorCodeStrings(self):
        r"""<p>错误码，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._ErrorCodeStrings

    @ErrorCodeStrings.setter
    def ErrorCodeStrings(self, ErrorCodeStrings):
        self._ErrorCodeStrings = ErrorCodeStrings

    @property
    def RunUserUins(self):
        r"""<p>运行人UIN，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._RunUserUins

    @RunUserUins.setter
    def RunUserUins(self, RunUserUins):
        self._RunUserUins = RunUserUins

    @property
    def LabelKeyIds(self):
        r"""<p>标签名称ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._LabelKeyIds

    @LabelKeyIds.setter
    def LabelKeyIds(self, LabelKeyIds):
        self._LabelKeyIds = LabelKeyIds

    @property
    def LabelValueIds(self):
        r"""<p>标签值ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._LabelValueIds

    @LabelValueIds.setter
    def LabelValueIds(self, LabelValueIds):
        self._LabelValueIds = LabelValueIds

    @property
    def OrderBys(self):
        r"""<p>排序条件，多个之间按数组顺序表示优先级。非必填，默认按 CreateTime Desc。<br>可排序字段白名单：CreateTime、EndTime、RunCostTime</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowNameKeyword = params.get("WorkflowNameKeyword")
        self._CreateStartTime = params.get("CreateStartTime")
        self._CreateEndTime = params.get("CreateEndTime")
        self._RunStates = params.get("RunStates")
        self._ErrorCodeStrings = params.get("ErrorCodeStrings")
        self._RunUserUins = params.get("RunUserUins")
        self._LabelKeyIds = params.get("LabelKeyIds")
        self._LabelValueIds = params.get("LabelValueIds")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowRunsResponse(AbstractModel):
    r"""ListWorkflowRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>工作流运行列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>工作流运行列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListWorkflowRunsRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowRunsRsp(AbstractModel):
    r"""ListWorkflowRunsRsp

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _Items: 工作流运行列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of WorkflowRun
        :param _BizStateEnumInfos: 工作流运行状态数量统计。
统计口径为当前筛选条件下的全量数据，不受 PageNumber / PageSize 影响
注意：此字段可能返回 null，表示取不到有效值。
        :type BizStateEnumInfos: list of ScheduleBizEnumBrief
        :param _BizErrorCodeEnumInfos: 工作流运行错误码数量统计。
统计口径为当前筛选条件下的全量数据，不受 PageNumber / PageSize 影响
注意：此字段可能返回 null，表示取不到有效值。
        :type BizErrorCodeEnumInfos: list of ScheduleBizEnumBrief
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._BizStateEnumInfos = None
        self._BizErrorCodeEnumInfos = None

    @property
    def PageNumber(self):
        r"""当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""工作流运行列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowRun
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def BizStateEnumInfos(self):
        r"""工作流运行状态数量统计。
统计口径为当前筛选条件下的全量数据，不受 PageNumber / PageSize 影响
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScheduleBizEnumBrief
        """
        return self._BizStateEnumInfos

    @BizStateEnumInfos.setter
    def BizStateEnumInfos(self, BizStateEnumInfos):
        self._BizStateEnumInfos = BizStateEnumInfos

    @property
    def BizErrorCodeEnumInfos(self):
        r"""工作流运行错误码数量统计。
统计口径为当前筛选条件下的全量数据，不受 PageNumber / PageSize 影响
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScheduleBizEnumBrief
        """
        return self._BizErrorCodeEnumInfos

    @BizErrorCodeEnumInfos.setter
    def BizErrorCodeEnumInfos(self, BizErrorCodeEnumInfos):
        self._BizErrorCodeEnumInfos = BizErrorCodeEnumInfos


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowRun()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("BizStateEnumInfos") is not None:
            self._BizStateEnumInfos = []
            for item in params.get("BizStateEnumInfos"):
                obj = ScheduleBizEnumBrief()
                obj._deserialize(item)
                self._BizStateEnumInfos.append(obj)
        if params.get("BizErrorCodeEnumInfos") is not None:
            self._BizErrorCodeEnumInfos = []
            for item in params.get("BizErrorCodeEnumInfos"):
                obj = ScheduleBizEnumBrief()
                obj._deserialize(item)
                self._BizErrorCodeEnumInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowTaskRunsRequest(AbstractModel):
    r"""ListWorkflowTaskRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _TaskId: <p>任务ID，可通过 ListWorkflowTasks 获取。非必填，精确匹配。与 WorkflowRunId 至少传一个：仅传 TaskId 时查询该任务的全部运行历史。</p>
        :type TaskId: str
        :param _WorkflowRunId: <p>工作流运行ID，可通过 ListWorkflowRuns 获取。非必填，精确匹配。与 TaskId 至少传一个：仅传 WorkflowRunId 时查询该次工作流运行下的全部任务运行。</p>
        :type WorkflowRunId: str
        :param _PageNumber: <p>分页页码，从 1 开始。非必填，默认 1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :type PageSize: int
        """
        self._WorkspaceId = None
        self._TaskId = None
        self._WorkflowRunId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def TaskId(self):
        r"""<p>任务ID，可通过 ListWorkflowTasks 获取。非必填，精确匹配。与 WorkflowRunId 至少传一个：仅传 TaskId 时查询该任务的全部运行历史。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID，可通过 ListWorkflowRuns 获取。非必填，精确匹配。与 TaskId 至少传一个：仅传 WorkflowRunId 时查询该次工作流运行下的全部任务运行。</p>
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def PageNumber(self):
        r"""<p>分页页码，从 1 开始。非必填，默认 1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._TaskId = params.get("TaskId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowTaskRunsResponse(AbstractModel):
    r"""ListWorkflowTaskRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>查询工作流任务历史运行列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>查询工作流任务历史运行列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListWorkflowTaskRunsRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowTaskRunsRsp(AbstractModel):
    r"""查询工作流任务运行列表响应。

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _Items: 任务运行历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of WorkflowTaskRun
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""任务运行历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTaskRun
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowTaskRun()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsRequest(AbstractModel):
    r"""ListWorkflows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _PageNumber: <p>分页页码，从 1 开始。非必填，默认 1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :type PageSize: int
        :param _WorkflowNameKeyword: <p>工作流名称关键字，对 WorkflowName 做模糊匹配。非必填，单值</p>
        :type WorkflowNameKeyword: str
        :param _WorkflowNames: <p>工作流名称，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :type WorkflowNames: list of str
        :param _WorkflowIds: <p>工作流ID，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :type WorkflowIds: list of str
        :param _RunUserUins: <p>工作流运行人UIN，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :type RunUserUins: list of str
        :param _LabelKeyIds: <p>标签名称ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :type LabelKeyIds: list of str
        :param _LabelValueIds: <p>标签值ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :type LabelValueIds: list of str
        :param _QuickSelectionType: <p>快速筛选类型。非必填，单值</p><p>对齐老云 API（wedata/2025-10-10）文档示例值：</p><ul><li>MY_FAVORITE：我收藏的</li><li>MY_OWNER：我负责的</li><li>MY_AUTHORITY：我有权限</li><li>WorkflowId：支持多个工作流ID筛选</li></ul><p>后端实现现状：当前仅 MY_FAVORITE 生效（设置 favoriteUserUin 过滤当前用户收藏），MY_OWNER / MY_AUTHORITY 暂未在 Service 层实现，传入会被忽略（按全量返回）。</p>
        :type QuickSelectionType: str
        :param _OrderBys: <p>排序条件，多个之间按数组顺序表示优先级。非必填。<br>可排序字段白名单：CreateTime</p>
        :type OrderBys: list of OrderBy
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._WorkflowNameKeyword = None
        self._WorkflowNames = None
        self._WorkflowIds = None
        self._RunUserUins = None
        self._LabelKeyIds = None
        self._LabelValueIds = None
        self._QuickSelectionType = None
        self._OrderBys = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        r"""<p>分页页码，从 1 开始。非必填，默认 1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小。非必填，默认 10，取值范围 [10, 200]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def WorkflowNameKeyword(self):
        r"""<p>工作流名称关键字，对 WorkflowName 做模糊匹配。非必填，单值</p>
        :rtype: str
        """
        return self._WorkflowNameKeyword

    @WorkflowNameKeyword.setter
    def WorkflowNameKeyword(self, WorkflowNameKeyword):
        self._WorkflowNameKeyword = WorkflowNameKeyword

    @property
    def WorkflowNames(self):
        r"""<p>工作流名称，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._WorkflowNames

    @WorkflowNames.setter
    def WorkflowNames(self, WorkflowNames):
        self._WorkflowNames = WorkflowNames

    @property
    def WorkflowIds(self):
        r"""<p>工作流ID，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._WorkflowIds

    @WorkflowIds.setter
    def WorkflowIds(self, WorkflowIds):
        self._WorkflowIds = WorkflowIds

    @property
    def RunUserUins(self):
        r"""<p>工作流运行人UIN，精确匹配。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._RunUserUins

    @RunUserUins.setter
    def RunUserUins(self, RunUserUins):
        self._RunUserUins = RunUserUins

    @property
    def LabelKeyIds(self):
        r"""<p>标签名称ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._LabelKeyIds

    @LabelKeyIds.setter
    def LabelKeyIds(self, LabelKeyIds):
        self._LabelKeyIds = LabelKeyIds

    @property
    def LabelValueIds(self):
        r"""<p>标签值ID，精确匹配，可通过标签相关接口获取。非必填，多选（多个值之间为 OR 关系）</p>
        :rtype: list of str
        """
        return self._LabelValueIds

    @LabelValueIds.setter
    def LabelValueIds(self, LabelValueIds):
        self._LabelValueIds = LabelValueIds

    @property
    def QuickSelectionType(self):
        r"""<p>快速筛选类型。非必填，单值</p><p>对齐老云 API（wedata/2025-10-10）文档示例值：</p><ul><li>MY_FAVORITE：我收藏的</li><li>MY_OWNER：我负责的</li><li>MY_AUTHORITY：我有权限</li><li>WorkflowId：支持多个工作流ID筛选</li></ul><p>后端实现现状：当前仅 MY_FAVORITE 生效（设置 favoriteUserUin 过滤当前用户收藏），MY_OWNER / MY_AUTHORITY 暂未在 Service 层实现，传入会被忽略（按全量返回）。</p>
        :rtype: str
        """
        return self._QuickSelectionType

    @QuickSelectionType.setter
    def QuickSelectionType(self, QuickSelectionType):
        self._QuickSelectionType = QuickSelectionType

    @property
    def OrderBys(self):
        r"""<p>排序条件，多个之间按数组顺序表示优先级。非必填。<br>可排序字段白名单：CreateTime</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._WorkflowNameKeyword = params.get("WorkflowNameKeyword")
        self._WorkflowNames = params.get("WorkflowNames")
        self._WorkflowIds = params.get("WorkflowIds")
        self._RunUserUins = params.get("RunUserUins")
        self._LabelKeyIds = params.get("LabelKeyIds")
        self._LabelValueIds = params.get("LabelValueIds")
        self._QuickSelectionType = params.get("QuickSelectionType")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsResponse(AbstractModel):
    r"""ListWorkflows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>查询工作流列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>查询工作流列表响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListWorkflowsRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowsRsp(AbstractModel):
    r"""ListWorkflowsRsp

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _Items: 工作流列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of WorkflowBrief
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""当前页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""工作流列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowBrief
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowBrief()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkspacesRequest(AbstractModel):
    r"""ListWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID精确匹配</p>
        :type WorkspaceId: str
        :param _WorkspaceKeyword: <p>工作空间名称模糊匹配</p>
        :type WorkspaceKeyword: str
        :param _StatusList: <p>工作空间状态过滤（多选）：0=未指定 1=创建中 2=创建失败 3=正常运行中 4=已删除</p>
        :type StatusList: list of int
        :param _OrderBys: <p>多字段排序，如 [{Name: 'CreateTime', Direction: 'Desc'}]；传入单个即单字段排序，默认按创建时间降序</p>
        :type OrderBys: list of OrderBy
        :param _PageNumber: <p>页码，从1开始，默认1</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认10，最小10，最大100</p>
        :type PageSize: int
        :param _WorkspaceRegion: <p>工作空间地域过滤（多选），如 ap-guangzhou</p>
        :type WorkspaceRegion: list of str
        :param _Creator: <p>创建者UIN过滤（多选）</p>
        :type Creator: list of str
        """
        self._WorkspaceId = None
        self._WorkspaceKeyword = None
        self._StatusList = None
        self._OrderBys = None
        self._PageNumber = None
        self._PageSize = None
        self._WorkspaceRegion = None
        self._Creator = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID精确匹配</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkspaceKeyword(self):
        r"""<p>工作空间名称模糊匹配</p>
        :rtype: str
        """
        return self._WorkspaceKeyword

    @WorkspaceKeyword.setter
    def WorkspaceKeyword(self, WorkspaceKeyword):
        self._WorkspaceKeyword = WorkspaceKeyword

    @property
    def StatusList(self):
        r"""<p>工作空间状态过滤（多选）：0=未指定 1=创建中 2=创建失败 3=正常运行中 4=已删除</p>
        :rtype: list of int
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def OrderBys(self):
        r"""<p>多字段排序，如 [{Name: 'CreateTime', Direction: 'Desc'}]；传入单个即单字段排序，默认按创建时间降序</p>
        :rtype: list of OrderBy
        """
        return self._OrderBys

    @OrderBys.setter
    def OrderBys(self, OrderBys):
        self._OrderBys = OrderBys

    @property
    def PageNumber(self):
        r"""<p>页码，从1开始，默认1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认10，最小10，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def WorkspaceRegion(self):
        r"""<p>工作空间地域过滤（多选），如 ap-guangzhou</p>
        :rtype: list of str
        """
        return self._WorkspaceRegion

    @WorkspaceRegion.setter
    def WorkspaceRegion(self, WorkspaceRegion):
        self._WorkspaceRegion = WorkspaceRegion

    @property
    def Creator(self):
        r"""<p>创建者UIN过滤（多选）</p>
        :rtype: list of str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkspaceKeyword = params.get("WorkspaceKeyword")
        self._StatusList = params.get("StatusList")
        if params.get("OrderBys") is not None:
            self._OrderBys = []
            for item in params.get("OrderBys"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OrderBys.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._WorkspaceRegion = params.get("WorkspaceRegion")
        self._Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkspacesResponse(AbstractModel):
    r"""ListWorkspaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>工作空间列表</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspacesRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>工作空间列表</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspacesRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListWorkspacesRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkspacesRsp(AbstractModel):
    r"""查询工作空间列表响应

    """

    def __init__(self):
        r"""
        :param _Items: <p>工作空间列表</p>
        :type Items: list of WorkspaceInfo
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小</p>
        :type PageSize: int
        :param _TotalCount: <p>总记录数</p>
        :type TotalCount: int
        :param _TotalPageNumber: <p>总页数</p>
        :type TotalPageNumber: int
        :param _IsConsoleAdmin: <p>是否控制台管理员</p>
        :type IsConsoleAdmin: bool
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._IsConsoleAdmin = None

    @property
    def Items(self):
        r"""<p>工作空间列表</p>
        :rtype: list of WorkspaceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""<p>总记录数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""<p>总页数</p>
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def IsConsoleAdmin(self):
        r"""<p>是否控制台管理员</p>
        :rtype: bool
        """
        return self._IsConsoleAdmin

    @IsConsoleAdmin.setter
    def IsConsoleAdmin(self, IsConsoleAdmin):
        self._IsConsoleAdmin = IsConsoleAdmin


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkspaceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._IsConsoleAdmin = params.get("IsConsoleAdmin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetaOwner(AbstractModel):
    r"""元数据责任人信息数据结构

    """

    def __init__(self):
        r"""
        :param _FullName: 元数据名称（全名）:catalog.schema.table
注意：此字段可能返回 null，表示取不到有效值。
        :type FullName: str
        :param _OwnerType: 所有者类型:User
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerType: str
        :param _Owner: 所有者:唯一标识(uin)
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _OwnerName: 所有者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerName: str
        """
        self._FullName = None
        self._OwnerType = None
        self._Owner = None
        self._OwnerName = None

    @property
    def FullName(self):
        r"""元数据名称（全名）:catalog.schema.table
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def OwnerType(self):
        r"""所有者类型:User
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerType

    @OwnerType.setter
    def OwnerType(self, OwnerType):
        self._OwnerType = OwnerType

    @property
    def Owner(self):
        r"""所有者:唯一标识(uin)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def OwnerName(self):
        r"""所有者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerName

    @OwnerName.setter
    def OwnerName(self, OwnerName):
        self._OwnerName = OwnerName


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._OwnerType = params.get("OwnerType")
        self._Owner = params.get("Owner")
        self._OwnerName = params.get("OwnerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricBrief(AbstractModel):
    r"""监控指标配置

    """

    def __init__(self):
        r"""
        :param _MonitorMetricId: 监控指标 ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorMetricId: str
        :param _AlarmMonitorType: 告警的监控对象类型，如工作流、任务等，当前支持 1. WORKFLOW 2. TASK
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmMonitorType: str
        :param _Metrics: 监控指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of MonitorMetricItem
        """
        self._MonitorMetricId = None
        self._AlarmMonitorType = None
        self._Metrics = None

    @property
    def MonitorMetricId(self):
        r"""监控指标 ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MonitorMetricId

    @MonitorMetricId.setter
    def MonitorMetricId(self, MonitorMetricId):
        self._MonitorMetricId = MonitorMetricId

    @property
    def AlarmMonitorType(self):
        r"""告警的监控对象类型，如工作流、任务等，当前支持 1. WORKFLOW 2. TASK
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlarmMonitorType

    @AlarmMonitorType.setter
    def AlarmMonitorType(self, AlarmMonitorType):
        self._AlarmMonitorType = AlarmMonitorType

    @property
    def Metrics(self):
        r"""监控指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MonitorMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._MonitorMetricId = params.get("MonitorMetricId")
        self._AlarmMonitorType = params.get("AlarmMonitorType")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = MonitorMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricItem(AbstractModel):
    r"""单个监控指标

    """

    def __init__(self):
        r"""
        :param _MetricType: 监控指标类型,有三种类型：1. RUN_DURATION（运行时长）2. WAIT_DURATION（等待时长）3. COMPLETION_TIME（完成时间）
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricType: str
        :param _WarningThreshold: 警告阈值，单位为毫秒级别，对于COMPLETION_TIME:从当日时间点00:00起算
注意：此字段可能返回 null，表示取不到有效值。
        :type WarningThreshold: str
        :param _TimeoutThreshold: 超时阈值，单位为毫秒级别，对于COMPLETION_TIME:从当日时间点00:00起算
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutThreshold: str
        """
        self._MetricType = None
        self._WarningThreshold = None
        self._TimeoutThreshold = None

    @property
    def MetricType(self):
        r"""监控指标类型,有三种类型：1. RUN_DURATION（运行时长）2. WAIT_DURATION（等待时长）3. COMPLETION_TIME（完成时间）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def WarningThreshold(self):
        r"""警告阈值，单位为毫秒级别，对于COMPLETION_TIME:从当日时间点00:00起算
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarningThreshold

    @WarningThreshold.setter
    def WarningThreshold(self, WarningThreshold):
        self._WarningThreshold = WarningThreshold

    @property
    def TimeoutThreshold(self):
        r"""超时阈值，单位为毫秒级别，对于COMPLETION_TIME:从当日时间点00:00起算
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeoutThreshold

    @TimeoutThreshold.setter
    def TimeoutThreshold(self, TimeoutThreshold):
        self._TimeoutThreshold = TimeoutThreshold


    def _deserialize(self, params):
        self._MetricType = params.get("MetricType")
        self._WarningThreshold = params.get("WarningThreshold")
        self._TimeoutThreshold = params.get("TimeoutThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    r"""排序字段

    """

    def __init__(self):
        r"""
        :param _Direction: 排序方向，Asc（升序）或 Desc（降序），大小写不敏感
        :type Direction: str
        :param _Name: 排序字段名
        :type Name: str
        """
        self._Direction = None
        self._Name = None

    @property
    def Direction(self):
        r"""排序方向，Asc（升序）或 Desc（降序），大小写不敏感
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Name(self):
        r"""排序字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    r"""参数键值对

    """

    def __init__(self):
        r"""
        :param _ParamId: 参数ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamId: str
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamId = None
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamId(self):
        r"""参数ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamId

    @ParamId.setter
    def ParamId(self, ParamId):
        self._ParamId = ParamId

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamId = params.get("ParamId")
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionDetail(AbstractModel):
    r"""实体权限信息，用于在get/list接口中返回当前用户对实体的权限列表

    """

    def __init__(self):
        r"""
        :param _Permissions: 当前用户对该实体拥有的权限列表
        :type Permissions: list of str
        :param _CatalogWorkspacePrivilege: catalog在工作空间上的权限信息（可选）。取值：WORKSPACE_READONLY（只读）或WORKSPACE_READWRITE（读写）
        :type CatalogWorkspacePrivilege: str
        :param _DenyPrivilegeList: deny权限总列表（用户deny ∪ 角色deny ∪ 继承deny，已去重，已从Permissions中排除）
        :type DenyPrivilegeList: list of str
        """
        self._Permissions = None
        self._CatalogWorkspacePrivilege = None
        self._DenyPrivilegeList = None

    @property
    def Permissions(self):
        r"""当前用户对该实体拥有的权限列表
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def CatalogWorkspacePrivilege(self):
        r"""catalog在工作空间上的权限信息（可选）。取值：WORKSPACE_READONLY（只读）或WORKSPACE_READWRITE（读写）
        :rtype: str
        """
        return self._CatalogWorkspacePrivilege

    @CatalogWorkspacePrivilege.setter
    def CatalogWorkspacePrivilege(self, CatalogWorkspacePrivilege):
        self._CatalogWorkspacePrivilege = CatalogWorkspacePrivilege

    @property
    def DenyPrivilegeList(self):
        r"""deny权限总列表（用户deny ∪ 角色deny ∪ 继承deny，已去重，已从Permissions中排除）
        :rtype: list of str
        """
        return self._DenyPrivilegeList

    @DenyPrivilegeList.setter
    def DenyPrivilegeList(self, DenyPrivilegeList):
        self._DenyPrivilegeList = DenyPrivilegeList


    def _deserialize(self, params):
        self._Permissions = params.get("Permissions")
        self._CatalogWorkspacePrivilege = params.get("CatalogWorkspacePrivilege")
        self._DenyPrivilegeList = params.get("DenyPrivilegeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveConsoleUsersRequest(AbstractModel):
    r"""RemoveConsoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserUins: <p>必填，待移除的用户 UIN 列表，单次最多10个</p>
        :type UserUins: list of str
        """
        self._UserUins = None

    @property
    def UserUins(self):
        r"""<p>必填，待移除的用户 UIN 列表，单次最多10个</p>
        :rtype: list of str
        """
        return self._UserUins

    @UserUins.setter
    def UserUins(self, UserUins):
        self._UserUins = UserUins


    def _deserialize(self, params):
        self._UserUins = params.get("UserUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveConsoleUsersResponse(AbstractModel):
    r"""RemoveConsoleUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>批量移除控制台用户结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>批量移除控制台用户结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RemoveConsoleUsersRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RemoveConsoleUsersRsp(AbstractModel):
    r"""批量移除控制台用户响应

    """

    def __init__(self):
        r"""
        :param _Status: <p>请求已完成处理；即使部分失败也为 true，逐个结果以 SuccessUins/FailItems 为准</p>
        :type Status: bool
        :param _SuccessUins: <p>删除成功的用户 UIN 列表</p>
        :type SuccessUins: list of str
        :param _FailItems: <p>失败项列表（Item 为用户 UIN，FailReason 为失败原因）</p>
        :type FailItems: list of CommonFailItem
        """
        self._Status = None
        self._SuccessUins = None
        self._FailItems = None

    @property
    def Status(self):
        r"""<p>请求已完成处理；即使部分失败也为 true，逐个结果以 SuccessUins/FailItems 为准</p>
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuccessUins(self):
        r"""<p>删除成功的用户 UIN 列表</p>
        :rtype: list of str
        """
        return self._SuccessUins

    @SuccessUins.setter
    def SuccessUins(self, SuccessUins):
        self._SuccessUins = SuccessUins

    @property
    def FailItems(self):
        r"""<p>失败项列表（Item 为用户 UIN，FailReason 为失败原因）</p>
        :rtype: list of CommonFailItem
        """
        return self._FailItems

    @FailItems.setter
    def FailItems(self, FailItems):
        self._FailItems = FailItems


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._SuccessUins = params.get("SuccessUins")
        if params.get("FailItems") is not None:
            self._FailItems = []
            for item in params.get("FailItems"):
                obj = CommonFailItem()
                obj._deserialize(item)
                self._FailItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunWorkflowRunRequest(AbstractModel):
    r"""RerunWorkflowRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        :param _WorkflowRunId: <p>工作流运行ID，可通过 ListWorkflowRuns 获取。必填</p>
        :type WorkflowRunId: str
        :param _RunType: <p>运行类型。必填。取值：1 普通运行，2 高级运行</p>
        :type RunType: int
        :param _AdvancedParams: <p>运行类型为高级运行时填写的自定义运行参数</p>
        :type AdvancedParams: list of TaskSchedulingParameterBrief
        :param _TaskIds: <p>本次需要重跑指定的任务ID集合，可通过 ListWorkflowTasks 获取，不传默认重跑该工作流下所有任务</p>
        :type TaskIds: list of str
        :param _ScheduledTimeConfig: <p>计划调度时间列表配置</p>
        :type ScheduledTimeConfig: :class:`tencentcloud.databuddy.v20260715.models.ScheduledTimeConfig`
        """
        self._WorkspaceId = None
        self._WorkflowId = None
        self._WorkflowRunId = None
        self._RunType = None
        self._AdvancedParams = None
        self._TaskIds = None
        self._ScheduledTimeConfig = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID，可通过 ListWorkflowRuns 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def RunType(self):
        r"""<p>运行类型。必填。取值：1 普通运行，2 高级运行</p>
        :rtype: int
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def AdvancedParams(self):
        r"""<p>运行类型为高级运行时填写的自定义运行参数</p>
        :rtype: list of TaskSchedulingParameterBrief
        """
        return self._AdvancedParams

    @AdvancedParams.setter
    def AdvancedParams(self, AdvancedParams):
        self._AdvancedParams = AdvancedParams

    @property
    def TaskIds(self):
        r"""<p>本次需要重跑指定的任务ID集合，可通过 ListWorkflowTasks 获取，不传默认重跑该工作流下所有任务</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def ScheduledTimeConfig(self):
        r"""<p>计划调度时间列表配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ScheduledTimeConfig`
        """
        return self._ScheduledTimeConfig

    @ScheduledTimeConfig.setter
    def ScheduledTimeConfig(self, ScheduledTimeConfig):
        self._ScheduledTimeConfig = ScheduledTimeConfig


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._RunType = params.get("RunType")
        if params.get("AdvancedParams") is not None:
            self._AdvancedParams = []
            for item in params.get("AdvancedParams"):
                obj = TaskSchedulingParameterBrief()
                obj._deserialize(item)
                self._AdvancedParams.append(obj)
        self._TaskIds = params.get("TaskIds")
        if params.get("ScheduledTimeConfig") is not None:
            self._ScheduledTimeConfig = ScheduledTimeConfig()
            self._ScheduledTimeConfig._deserialize(params.get("ScheduledTimeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunWorkflowRunResponse(AbstractModel):
    r"""RerunWorkflowRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>重跑工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>重跑工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AsyncActionRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ResourceGroupInfo(AbstractModel):
    r"""资源组信息

    """

    def __init__(self):
        r"""
        :param _ResourceGroupId: <p>资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceGroupName: <p>资源组名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _ResourceGroupStatus: <p>资源组状态</p><p>参数格式：0 // 未指定 1 // 待创建 2 // 创建中 3 // 运行中 4 // 已停止 5 // 停止中 6 // 启动中 7 // 更新中 8 // 删除中 9 // 已删除 10 // 用户主动启动 / 自动启动（有任务提交且自动启停开启） 11 // 可用: 仅存在于数据计算型 12 // 不可用: 仅存在于数据计算型 13 // 失败</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupStatus: str
        """
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._ResourceGroupStatus = None

    @property
    def ResourceGroupId(self):
        r"""<p>资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        r"""<p>资源组名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def ResourceGroupStatus(self):
        r"""<p>资源组状态</p><p>参数格式：0 // 未指定 1 // 待创建 2 // 创建中 3 // 运行中 4 // 已停止 5 // 停止中 6 // 启动中 7 // 更新中 8 // 删除中 9 // 已删除 10 // 用户主动启动 / 自动启动（有任务提交且自动启停开启） 11 // 可用: 仅存在于数据计算型 12 // 不可用: 仅存在于数据计算型 13 // 失败</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupStatus

    @ResourceGroupStatus.setter
    def ResourceGroupStatus(self, ResourceGroupStatus):
        self._ResourceGroupStatus = ResourceGroupStatus


    def _deserialize(self, params):
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._ResourceGroupStatus = params.get("ResourceGroupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleBasicInfo(AbstractModel):
    r"""角色基础信息

    """

    def __init__(self):
        r"""
        :param _Id: <p>角色ID，可通过 ListWorkspaceRoles / ListConsoleRoles 接口获取；创建/更新角色时无需填写（由系统自动生成，创建成功后从响应 Data.RoleId 获取）</p>
        :type Id: str
        :param _Name: <p>角色名称</p>
        :type Name: str
        :param _Description: <p>角色描述</p>
        :type Description: str
        :param _DisplayName: <p>显示名称</p>
        :type DisplayName: str
        :param _RoleType: <p>角色类型：workspace=工作空间系统角色，workspace_custom=工作空间自定义角色，console=控制台角色；查询时返回，创建时无需填写（系统固定创建自定义角色）</p>
        :type RoleType: str
        :param _Source: <p>角色来源（查询侧字段，创建时无需填写）：0=未指定，1=用户直绑，2=用户组继承，3=两者都有</p>
        :type Source: int
        :param _GroupNames: <p>继承来源的用户组名称列表（查询侧字段，创建时无需填写），Source=1 时为空</p>
        :type GroupNames: list of str
        """
        self._Id = None
        self._Name = None
        self._Description = None
        self._DisplayName = None
        self._RoleType = None
        self._Source = None
        self._GroupNames = None

    @property
    def Id(self):
        r"""<p>角色ID，可通过 ListWorkspaceRoles / ListConsoleRoles 接口获取；创建/更新角色时无需填写（由系统自动生成，创建成功后从响应 Data.RoleId 获取）</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>角色名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>角色描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DisplayName(self):
        r"""<p>显示名称</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def RoleType(self):
        r"""<p>角色类型：workspace=工作空间系统角色，workspace_custom=工作空间自定义角色，console=控制台角色；查询时返回，创建时无需填写（系统固定创建自定义角色）</p>
        :rtype: str
        """
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def Source(self):
        r"""<p>角色来源（查询侧字段，创建时无需填写）：0=未指定，1=用户直绑，2=用户组继承，3=两者都有</p>
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def GroupNames(self):
        r"""<p>继承来源的用户组名称列表（查询侧字段，创建时无需填写），Source=1 时为空</p>
        :rtype: list of str
        """
        return self._GroupNames

    @GroupNames.setter
    def GroupNames(self, GroupNames):
        self._GroupNames = GroupNames


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._DisplayName = params.get("DisplayName")
        self._RoleType = params.get("RoleType")
        self._Source = params.get("Source")
        self._GroupNames = params.get("GroupNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleMetaData(AbstractModel):
    r"""角色元数据

    """

    def __init__(self):
        r"""
        :param _Creator: 创建者
        :type Creator: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Updater: 更新者
        :type Updater: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Creator = None
        self._CreateTime = None
        self._Updater = None
        self._UpdateTime = None

    @property
    def Creator(self):
        r"""创建者
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Updater(self):
        r"""更新者
        :rtype: str
        """
        return self._Updater

    @Updater.setter
    def Updater(self, Updater):
        self._Updater = Updater

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        self._Updater = params.get("Updater")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RolePermission(AbstractModel):
    r"""角色权限

    """

    def __init__(self):
        r"""
        :param _ModuleId: <p>模块ID，须为当前租户已开通的功能模块（叶子节点）的模块ID（层级编码字符串，如 101=快速开始、109=工作流、116101103=工作空间管理_角色权限），非法值返回 InvalidParameterValue；模块清单可通过控制台「工作空间设置-角色权限」页面查看</p>
        :type ModuleId: str
        :param _Permissions: <p>模块访问权限，单值：R=只读，RW=读写，RWD=读写删除，N=无权限</p>
        :type Permissions: str
        """
        self._ModuleId = None
        self._Permissions = None

    @property
    def ModuleId(self):
        r"""<p>模块ID，须为当前租户已开通的功能模块（叶子节点）的模块ID（层级编码字符串，如 101=快速开始、109=工作流、116101103=工作空间管理_角色权限），非法值返回 InvalidParameterValue；模块清单可通过控制台「工作空间设置-角色权限」页面查看</p>
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def Permissions(self):
        r"""<p>模块访问权限，单值：R=只读，RW=读写，RWD=读写删除，N=无权限</p>
        :rtype: str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunActionBrief(AbstractModel):
    r"""单个操作项的执行结果。 由 RunWorkflow / RerunWorkflowRun / KillWorkflowRun 共用： RunWorkflow—— WorkflowId / WorkflowName 有值，WorkflowRunId 为空 RerunWorkflowRun —— WorkflowId / WorkflowName / WorkflowRunId 均有值 KillWorkflowRun  —— WorkflowId / WorkflowName / WorkflowRunId 均有值

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _RunActionId: 操作动作ID，用于追踪具体的执行动作
注意：此字段可能返回 null，表示取不到有效值。
        :type RunActionId: str
        :param _ErrorMessage: 失败错误信息，操作失败时返回具体的错误描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _OpStatus: 操作状态，true 表示成功，false 表示失败
注意：此字段可能返回 null，表示取不到有效值。
        :type OpStatus: bool
        :param _WorkflowRunId: 工作流运行ID。重跑 / 终止场景返回被操作的运行ID；运行工作流场景为空
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._RunActionId = None
        self._ErrorMessage = None
        self._OpStatus = None
        self._WorkflowRunId = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def RunActionId(self):
        r"""操作动作ID，用于追踪具体的执行动作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunActionId

    @RunActionId.setter
    def RunActionId(self, RunActionId):
        self._RunActionId = RunActionId

    @property
    def ErrorMessage(self):
        r"""失败错误信息，操作失败时返回具体的错误描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def OpStatus(self):
        r"""操作状态，true 表示成功，false 表示失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._OpStatus

    @OpStatus.setter
    def OpStatus(self, OpStatus):
        self._OpStatus = OpStatus

    @property
    def WorkflowRunId(self):
        r"""工作流运行ID。重跑 / 终止场景返回被操作的运行ID；运行工作流场景为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._RunActionId = params.get("RunActionId")
        self._ErrorMessage = params.get("ErrorMessage")
        self._OpStatus = params.get("OpStatus")
        self._WorkflowRunId = params.get("WorkflowRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowRequest(AbstractModel):
    r"""RunWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        :param _RunType: <p>运行类型。必填。取值：1 普通运行，2 高级运行</p>
        :type RunType: int
        :param _AdvancedParams: <p>运行类型为高级运行时填写的自定义运行参数</p>
        :type AdvancedParams: list of TaskSchedulingParameterBrief
        :param _TaskIds: <p>本次需要运行指定的任务ID集合，可通过 ListWorkflowTasks 获取，不传默认运行该工作流下所有任务</p>
        :type TaskIds: list of str
        :param _IdempotencyToken: <p>幂等令牌。非必填，相同令牌的重复请求只会触发一次运行</p>
        :type IdempotencyToken: str
        :param _ScheduledTimeConfig: <p>计划调度时间列表配置</p>
        :type ScheduledTimeConfig: :class:`tencentcloud.databuddy.v20260715.models.ScheduledTimeConfig`
        """
        self._WorkspaceId = None
        self._WorkflowId = None
        self._RunType = None
        self._AdvancedParams = None
        self._TaskIds = None
        self._IdempotencyToken = None
        self._ScheduledTimeConfig = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def RunType(self):
        r"""<p>运行类型。必填。取值：1 普通运行，2 高级运行</p>
        :rtype: int
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def AdvancedParams(self):
        r"""<p>运行类型为高级运行时填写的自定义运行参数</p>
        :rtype: list of TaskSchedulingParameterBrief
        """
        return self._AdvancedParams

    @AdvancedParams.setter
    def AdvancedParams(self, AdvancedParams):
        self._AdvancedParams = AdvancedParams

    @property
    def TaskIds(self):
        r"""<p>本次需要运行指定的任务ID集合，可通过 ListWorkflowTasks 获取，不传默认运行该工作流下所有任务</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def IdempotencyToken(self):
        r"""<p>幂等令牌。非必填，相同令牌的重复请求只会触发一次运行</p>
        :rtype: str
        """
        return self._IdempotencyToken

    @IdempotencyToken.setter
    def IdempotencyToken(self, IdempotencyToken):
        self._IdempotencyToken = IdempotencyToken

    @property
    def ScheduledTimeConfig(self):
        r"""<p>计划调度时间列表配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ScheduledTimeConfig`
        """
        return self._ScheduledTimeConfig

    @ScheduledTimeConfig.setter
    def ScheduledTimeConfig(self, ScheduledTimeConfig):
        self._ScheduledTimeConfig = ScheduledTimeConfig


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._RunType = params.get("RunType")
        if params.get("AdvancedParams") is not None:
            self._AdvancedParams = []
            for item in params.get("AdvancedParams"):
                obj = TaskSchedulingParameterBrief()
                obj._deserialize(item)
                self._AdvancedParams.append(obj)
        self._TaskIds = params.get("TaskIds")
        self._IdempotencyToken = params.get("IdempotencyToken")
        if params.get("ScheduledTimeConfig") is not None:
            self._ScheduledTimeConfig = ScheduledTimeConfig()
            self._ScheduledTimeConfig._deserialize(params.get("ScheduledTimeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowResponse(AbstractModel):
    r"""RunWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>运行工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>运行工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AsyncActionRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AsyncActionRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ScheduleBizEnumBrief(AbstractModel):
    r"""枚举项统计（如运行状态、错误码的数量分布）

    """

    def __init__(self):
        r"""
        :param _LabelKey: 枚举标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelKey: str
        :param _LabelValue: 枚举标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _Count: 枚举项统计数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._LabelKey = None
        self._LabelValue = None
        self._Count = None

    @property
    def LabelKey(self):
        r"""枚举标签键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelKey

    @LabelKey.setter
    def LabelKey(self, LabelKey):
        self._LabelKey = LabelKey

    @property
    def LabelValue(self):
        r"""枚举标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def Count(self):
        r"""枚举项统计数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._LabelKey = params.get("LabelKey")
        self._LabelValue = params.get("LabelValue")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledTimeConfig(AbstractModel):
    r"""计划调度时间配置

    """

    def __init__(self):
        r"""
        :param _ScheduledTimeZone: <p>调度时区，IANA 时区 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTimeZone: str
        :param _StartTime: <p>调度生效开始时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: <p>调度生效结束时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CycleType: <p>周期类型</p><p>枚举值：</p><ul><li>DAY_CYCLE： 天</li><li>HOUR_CYCLE： 小时</li><li>MINUTE_CYCLE： 分钟</li><li>WEEK_CYCLE： 周</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _CycleNum: <p>周期步长</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleNum: int
        """
        self._ScheduledTimeZone = None
        self._StartTime = None
        self._EndTime = None
        self._CycleType = None
        self._CycleNum = None

    @property
    def ScheduledTimeZone(self):
        r"""<p>调度时区，IANA 时区 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduledTimeZone

    @ScheduledTimeZone.setter
    def ScheduledTimeZone(self, ScheduledTimeZone):
        self._ScheduledTimeZone = ScheduledTimeZone

    @property
    def StartTime(self):
        r"""<p>调度生效开始时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>调度生效结束时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CycleType(self):
        r"""<p>周期类型</p><p>枚举值：</p><ul><li>DAY_CYCLE： 天</li><li>HOUR_CYCLE： 小时</li><li>MINUTE_CYCLE： 分钟</li><li>WEEK_CYCLE： 周</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def CycleNum(self):
        r"""<p>周期步长</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CycleNum

    @CycleNum.setter
    def CycleNum(self, CycleNum):
        self._CycleNum = CycleNum


    def _deserialize(self, params):
        self._ScheduledTimeZone = params.get("ScheduledTimeZone")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CycleType = params.get("CycleType")
        self._CycleNum = params.get("CycleNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Schema(AbstractModel):
    r"""Schema信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>schema名称</p>
        :type Name: str
        :param _Comment: <p>描述。注意：此字段可能返回null，表示取不到有效值</p>
        :type Comment: str
        :param _Properties: <p>属性。注意：此字段可能返回null，表示取不到有效值</p>
        :type Properties: list of KVPair
        :param _Audit: <p>审计信息。注意：此字段可能返回null，表示取不到有效值</p>
        :type Audit: :class:`tencentcloud.databuddy.v20260715.models.Audit`
        :param _MetaOwner: <p>owner信息</p>
        :type MetaOwner: :class:`tencentcloud.databuddy.v20260715.models.MetaOwner`
        :param _AssetGuid: <p>资产全局唯一ID，通过WedataAssetUIDUtils.generateUID生成</p>
        :type AssetGuid: str
        :param _PermissionDetail: <p>当前用户对该schema的权限信息。注意：此字段可能返回null，请求中未开启FetchPermissions时不返回</p>
        :type PermissionDetail: :class:`tencentcloud.databuddy.v20260715.models.PermissionDetail`
        :param _Tags: <p>标签信息列表。注意：此字段可能返回null，请求中未开启FetchTags时不返回</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of CommonTagInfo
        """
        self._Name = None
        self._Comment = None
        self._Properties = None
        self._Audit = None
        self._MetaOwner = None
        self._AssetGuid = None
        self._PermissionDetail = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>schema名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Comment(self):
        r"""<p>描述。注意：此字段可能返回null，表示取不到有效值</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Properties(self):
        r"""<p>属性。注意：此字段可能返回null，表示取不到有效值</p>
        :rtype: list of KVPair
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Audit(self):
        r"""<p>审计信息。注意：此字段可能返回null，表示取不到有效值</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.Audit`
        """
        return self._Audit

    @Audit.setter
    def Audit(self, Audit):
        self._Audit = Audit

    @property
    def MetaOwner(self):
        r"""<p>owner信息</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.MetaOwner`
        """
        return self._MetaOwner

    @MetaOwner.setter
    def MetaOwner(self, MetaOwner):
        self._MetaOwner = MetaOwner

    @property
    def AssetGuid(self):
        r"""<p>资产全局唯一ID，通过WedataAssetUIDUtils.generateUID生成</p>
        :rtype: str
        """
        return self._AssetGuid

    @AssetGuid.setter
    def AssetGuid(self, AssetGuid):
        self._AssetGuid = AssetGuid

    @property
    def PermissionDetail(self):
        r"""<p>当前用户对该schema的权限信息。注意：此字段可能返回null，请求中未开启FetchPermissions时不返回</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.PermissionDetail`
        """
        return self._PermissionDetail

    @PermissionDetail.setter
    def PermissionDetail(self, PermissionDetail):
        self._PermissionDetail = PermissionDetail

    @property
    def Tags(self):
        r"""<p>标签信息列表。注意：此字段可能返回null，请求中未开启FetchTags时不返回</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CommonTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = KVPair()
                obj._deserialize(item)
                self._Properties.append(obj)
        if params.get("Audit") is not None:
            self._Audit = Audit()
            self._Audit._deserialize(params.get("Audit"))
        if params.get("MetaOwner") is not None:
            self._MetaOwner = MetaOwner()
            self._MetaOwner._deserialize(params.get("MetaOwner"))
        self._AssetGuid = params.get("AssetGuid")
        if params.get("PermissionDetail") is not None:
            self._PermissionDetail = PermissionDetail()
            self._PermissionDetail._deserialize(params.get("PermissionDetail"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = CommonTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparseCheckoutConfig(AbstractModel):
    r"""git检出规则

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>是否启用稀疏检出</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param _ConeMode: <p>是否使用 cone 模式（推荐 true，按目录匹配更高效）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ConeMode: bool
        :param _Patterns: <p>稀疏检出路径列表（如 [&quot;src/module-a/&quot;, &quot;docs/&quot;]）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Patterns: list of str
        """
        self._Enabled = None
        self._ConeMode = None
        self._Patterns = None

    @property
    def Enabled(self):
        r"""<p>是否启用稀疏检出</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ConeMode(self):
        r"""<p>是否使用 cone 模式（推荐 true，按目录匹配更高效）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ConeMode

    @ConeMode.setter
    def ConeMode(self, ConeMode):
        self._ConeMode = ConeMode

    @property
    def Patterns(self):
        r"""<p>稀疏检出路径列表（如 [&quot;src/module-a/&quot;, &quot;docs/&quot;]）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Patterns

    @Patterns.setter
    def Patterns(self, Patterns):
        self._Patterns = Patterns


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._ConeMode = params.get("ConeMode")
        self._Patterns = params.get("Patterns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardUserInfo(AbstractModel):
    r"""用户基础展示信息

    """

    def __init__(self):
        r"""
        :param _UserUin: 用户UIN
        :type UserUin: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _UserTag: 0: 普通用户 1: entraId用户
        :type UserTag: str
        """
        self._UserUin = None
        self._UserName = None
        self._Nickname = None
        self._UserTag = None

    @property
    def UserUin(self):
        r"""用户UIN
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def UserTag(self):
        r"""0: 普通用户 1: entraId用户
        :rtype: str
        """
        return self._UserTag

    @UserTag.setter
    def UserTag(self, UserTag):
        self._UserTag = UserTag


    def _deserialize(self, params):
        self._UserUin = params.get("UserUin")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        self._UserTag = params.get("UserTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartComputeRequest(AbstractModel):
    r"""StartCompute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 计算资源 ID
        :type ResourceId: str
        :param _WorkspaceId: 工作空间 ID
        :type WorkspaceId: str
        """
        self._ResourceId = None
        self._WorkspaceId = None

    @property
    def ResourceId(self):
        r"""计算资源 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def WorkspaceId(self):
        r"""工作空间 ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartComputeResponse(AbstractModel):
    r"""StartCompute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 启动计算资源返回结果
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.StartComputeRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""启动计算资源返回结果
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.StartComputeRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = StartComputeRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class StartComputeRsp(AbstractModel):
    r"""启动计算资源返回结果

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopComputeRequest(AbstractModel):
    r"""StopCompute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 计算资源 ID
        :type ResourceId: str
        :param _WorkspaceId: 工作空间 ID
        :type WorkspaceId: str
        """
        self._ResourceId = None
        self._WorkspaceId = None

    @property
    def ResourceId(self):
        r"""计算资源 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def WorkspaceId(self):
        r"""工作空间 ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopComputeResponse(AbstractModel):
    r"""StopCompute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 停止计算资源返回结果
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.StopComputeRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""停止计算资源返回结果
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.StopComputeRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = StopComputeRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class StopComputeRsp(AbstractModel):
    r"""停止计算资源返回结果

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskRetryStrategy(AbstractModel):
    r"""任务重试策略

    """

    def __init__(self):
        r"""
        :param _MaxRetryTimes: 最多重试次数，默认3
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetryTimes: int
        :param _RetryBetweenWaitTime: 重试之间等待时间，默认5
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryBetweenWaitTime: int
        :param _RetryBetweenWaitTimeUnit: 重试之间等待时间单位
毫秒：MILLISECOND秒：SECOND分钟（默认）：MINUTE小时：HOUR
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryBetweenWaitTimeUnit: str
        :param _TaskRunFailureRetrySwitch: 任务运行失败时重试开关，默认为true
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRunFailureRetrySwitch: bool
        :param _TaskRunTimeoutRetrySwitch: 任务运行超时时重试开关，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRunTimeoutRetrySwitch: bool
        """
        self._MaxRetryTimes = None
        self._RetryBetweenWaitTime = None
        self._RetryBetweenWaitTimeUnit = None
        self._TaskRunFailureRetrySwitch = None
        self._TaskRunTimeoutRetrySwitch = None

    @property
    def MaxRetryTimes(self):
        r"""最多重试次数，默认3
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def RetryBetweenWaitTime(self):
        r"""重试之间等待时间，默认5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryBetweenWaitTime

    @RetryBetweenWaitTime.setter
    def RetryBetweenWaitTime(self, RetryBetweenWaitTime):
        self._RetryBetweenWaitTime = RetryBetweenWaitTime

    @property
    def RetryBetweenWaitTimeUnit(self):
        r"""重试之间等待时间单位
毫秒：MILLISECOND秒：SECOND分钟（默认）：MINUTE小时：HOUR
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RetryBetweenWaitTimeUnit

    @RetryBetweenWaitTimeUnit.setter
    def RetryBetweenWaitTimeUnit(self, RetryBetweenWaitTimeUnit):
        self._RetryBetweenWaitTimeUnit = RetryBetweenWaitTimeUnit

    @property
    def TaskRunFailureRetrySwitch(self):
        r"""任务运行失败时重试开关，默认为true
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._TaskRunFailureRetrySwitch

    @TaskRunFailureRetrySwitch.setter
    def TaskRunFailureRetrySwitch(self, TaskRunFailureRetrySwitch):
        self._TaskRunFailureRetrySwitch = TaskRunFailureRetrySwitch

    @property
    def TaskRunTimeoutRetrySwitch(self):
        r"""任务运行超时时重试开关，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._TaskRunTimeoutRetrySwitch

    @TaskRunTimeoutRetrySwitch.setter
    def TaskRunTimeoutRetrySwitch(self, TaskRunTimeoutRetrySwitch):
        self._TaskRunTimeoutRetrySwitch = TaskRunTimeoutRetrySwitch


    def _deserialize(self, params):
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._RetryBetweenWaitTime = params.get("RetryBetweenWaitTime")
        self._RetryBetweenWaitTimeUnit = params.get("RetryBetweenWaitTimeUnit")
        self._TaskRunFailureRetrySwitch = params.get("TaskRunFailureRetrySwitch")
        self._TaskRunTimeoutRetrySwitch = params.get("TaskRunTimeoutRetrySwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskRunConditionRule(AbstractModel):
    r"""任务运行条件规则

    """

    def __init__(self):
        r"""
        :param _UpstreamTaskId: <p>上游任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamTaskId: str
        :param _UpstreamTaskName: <p>上游任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamTaskName: str
        :param _AllowedStates: <p>任务可运行条件<br>支持的状态值： - SUCCESS: 成功 - FAILED: 失败 - UPSTREAM_FAILED: 上游失败 - EXCLUDED: 排除运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowedStates: list of str
        """
        self._UpstreamTaskId = None
        self._UpstreamTaskName = None
        self._AllowedStates = None

    @property
    def UpstreamTaskId(self):
        r"""<p>上游任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpstreamTaskId

    @UpstreamTaskId.setter
    def UpstreamTaskId(self, UpstreamTaskId):
        self._UpstreamTaskId = UpstreamTaskId

    @property
    def UpstreamTaskName(self):
        r"""<p>上游任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpstreamTaskName

    @UpstreamTaskName.setter
    def UpstreamTaskName(self, UpstreamTaskName):
        self._UpstreamTaskName = UpstreamTaskName

    @property
    def AllowedStates(self):
        r"""<p>任务可运行条件<br>支持的状态值： - SUCCESS: 成功 - FAILED: 失败 - UPSTREAM_FAILED: 上游失败 - EXCLUDED: 排除运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AllowedStates

    @AllowedStates.setter
    def AllowedStates(self, AllowedStates):
        self._AllowedStates = AllowedStates


    def _deserialize(self, params):
        self._UpstreamTaskId = params.get("UpstreamTaskId")
        self._UpstreamTaskName = params.get("UpstreamTaskName")
        self._AllowedStates = params.get("AllowedStates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSchedulingParameterBrief(AbstractModel):
    r"""任务调度参数（运行/重跑工作流时的自定义参数）

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskType(AbstractModel):
    r"""### `TaskTypePropertyList` 中 `TaskTypeProperty` 针对不同任务类型需要填写不同的 key 和 value；

    ### 1. NOTEBOOK 任务类型

    #### 属性配置

    | 属性键       | 属性名称          | 描述                               | 是否必需                |
    | ------------ | ----------------- | ---------------------------------- | ----------------------- |
    | Source       | 来源              | 只支持填2或5,来源 2:GIT, 5:工作空间    | 是                      |
    | NotebookPath | Notebook 相对路径 | Source为5时，需从（ListFiles）获取 | Source 为 2、5 时，必填 |

    ### 2. DATA_INTEGRATION 任务类型

    #### 属性配置

    | 属性键                | 属性名称             | 描述                                    | 是否必需 |
    | --------------------- | -------------------- | --------------------------------------- | -------- |
    | Source                | 来源                 | 必填:4,表示来源为COS                    | 是       |
    | TemplatePath          | 数据接入任务配置路径 | 需从（ListBatchIngestionTasks）接口获取 | 是       |
    | DataIntegrationTaskId | 数据接入任务ID       | 需从（ListBatchIngestionTasks）接口获取 | 是       |

    ### 3. RUN_WORKFLOW 任务类型

    #### 属性配置

    | 属性键     | 属性名称   | 描述                          | 是否必需 |
    | ---------- | ---------- | ----------------------------- | -------- |
    | WorkflowId | 选择工作流 | 需从（ListWorkflows）接口获取 | 是       |

    ### 4. SQL 任务类型

    #### 属性配置

    | 属性键          | 属性名称    | 描述                                          | 是否必需             |
    | --------------- | ----------- | --------------------------------------------- | -------------------- |
    | Source          | 来源        | 只支持填2或5,来源 2:GIT, 5:工作空间               | 是                   |
    | SqlPath         | SQL脚本路径 | SQL脚本路径                                   | Source 为 2 时，必填 |
    | CodeFileName    | 文件名称    | Source为5时，需从（ListReleasedQueries）接口获取 | 否                |
    | CodeFileId      | 文件ID      | Source为5时，需从（ListReleasedQueries）接口获取 | Source 为 5 时，必填 |
    | CodeFileVersion | 文件版本    | Source为5时，需从（ListReleasedQueries）接口获取 | 否                |

    ### 5. PYTHON 任务类型

    #### 属性配置

    | 属性键     | 属性名称       | 描述                                   | 是否必需 |
    | ---------- | -------------- | -------------------------------------- | -------- |
    | Source     | 来源           | 只支持填2或5,来源 2:GIT, 5:工作空间        | 是       |
    | SourcePath | Python脚本路径 | Source为5时，需从（ListFiles）接口获取 | 是       |

    ### 6. DATA_QUALITY（质量监控）任务类型

    #### 属性配置

    | 属性键         | 属性名称         | 描述                                          | 是否必需 |
    | -------------- | ---------------- | --------------------------------------------- | -------- |
    | Source         | 来源             | 必填:4,表示来源为COS                          | 是       |
    | TemplatePath   | 质量监控配置路径 | 需从（ListDataQualityTaskSummaries）接口获取  | 是       |
    | SourceUniqueId | 质量监控ID       | 需从（ListDataQualityTaskSummaries）接口获取  | 是       |
    | ExecutionType  | 执行类型         | 必填:SQL                                      | 是       |
    | AfterAspect    | 质量任务后置切面 | 需从（ListDataQualityTaskSummaries）接口获取  | 否       |
    | BeforeAspect   | 质量任务前置切面 | 需从（ListDataQualityTaskSummaries）接口获取  | 否       |

    ### 7. IF_ELSE 任务类型

    #### 属性配置

    | 属性键     | 属性名称 | 描述            | 是否必需 |
    | ---------- | -------- | --------------- | -------- |
    | Conditions | 条件列表 | IF-ELSE条件配置 | 是       |

    ### 8. FOR_EACH 任务类型

    #### 属性配置

    | 属性键         | 属性名称     | 描述                               | 是否必需 |
    | -------------- | ------------ | ---------------------------------- | -------- |
    | MaxConcurrency | 最大并发数   | 最大并发数，默认为1                | 是       |
    | MaxIterations  | 最大迭代次数 | 最大迭代次数，默认1000             | 是       |
    | LoopDataArray  | 循环参数     | JSON格式的数组，或 {{}} 包裹的变量 | 是       |

    ### 9. RAY_JOB（Ray作业）任务类型

    #### 属性配置

    | 属性键         | 属性名称             | 描述                               | 是否必需 |
    | -------------- | -------------------- | ---------------------------------- | -------- |
    | RunMode        | 运行方式             | 运行方式，取值：SERVERLESS（按需拉起集群）/ DEDICATED（提交到指定集群）。默认 DEDICATED | 是 |
    | Entrypoint     | 入口指令             | 入口指令                           | 是       |
    | JobConfig      | 任务配置             | 如存储配置 + 计算环境。传值请参考前端页面保存Ray作业任务时调用UpdateWorkflow。Image请调用DLC接口ListImages接口Url字段获取 | RunMode 为 SERVERLESS 时，必填 |
    | ClusterId      | Ray 集群             | 需从所选计算资源下已配置的 Ray 集群（引擎）列表中选择，可通过计算资源相关接口获取 | RunMode 为 DEDICATED 时，必填 |
    | Source         | 任务来源             | 任务来源，取值：1（本地文件）/ 5（工作空间） | 是 |
    | JobPackage     | 任务来源文件地址     | 任务来源路径：Source 为 1 时存本地上传文件的 COS 地址（支持 .zip / .py 文件）；Source 为 5 时存所选工作空间文件/文件夹路径 | 是 |
    | JobPackageName | 任务来源本地文件名   | 任务来源本地文件名                 | Source 为 1 时，必填 |
    | CodeFileId     | 代码文件ID           | Source 为 5 时，需从工作空间文件选择组件获取所选文件/文件夹对应的ID | Source 为 5 时，必填 |
    | WorkspaceEntryType | 工作空间入口类型 | Source 为 5 时，所选工作空间条目的类型：FILE（文件）/ FOLDER（文件夹），由前端选择器随选择目标自动写入 | Source 为 5 时，必填 |

    ### RuntimePropertyList
    <p>任务运行参数列表，用于配置任务运行时的计算资源，与 TaskTypePropertyList（任务扩展属性）区分：TaskTypePropertyList 承载任务自身的业务配置（如脚本来源、路径等），RuntimePropertyList 承载任务运行时的资源配置（如资源模式、CU规格、Executor数量等）。</p>
    <p>主要适用于需要配置计算资源的任务类型（如 NOTEBOOK、PYTHON）。</p>
    <p>具体可填写的属性键以任务类型属性配置为准，可通过 ListWorkflowTaskTypeProperties 接口获取（propertyType 为 RUNTIME 的属性项）。常见运行参数键说明：</p>

    | 属性键 | 属性名称 | 描述 | 必填性（联动条件满足时） | 默认值 |
    | ---------- | -------------- | ---------------------------------- | -------- | -------- |
    | ResourceMode | 资源模式 | 1：分布式；2：单节点 | 是 | 1 |
    | ConfigType | 配置类型 | DEFAULT：默认配置；CUSTOM：自定义配置 | 是 | DEFAULT |
    | ExecutorAllocation | Executor分配模式 | DYNAMIC：动态分配；FIXED：固定分配 | 是（分布式且自定义配置时） | DYNAMIC |
    | ExecutorMinNum | Executor最小个数 | 正整数 | 是（动态分配时） | 1 |
    | ExecutorMaxNum | Executor最大个数 | 正整数 | 是（动态分配时） | 1 |
    | ExecutorFixedNum | Executor固定个数 | 正整数 | 否（固定分配时） | - |
    | ExecutorCU | Executor资源规格 | small / medium / large / xlarge / 4xlarge | 否（分布式且自定义配置时） | - |
    | DriverCU | Driver资源规格 | small / medium / large / xlarge / 4xlarge | 否（分布式且自定义配置时 或者单节点时） | - |
    | ExecutorGPU | Executor GPU数量 | 0表示不使用GPU | 否（分布式且自定义配置时） | - |
    | DriverGPU | Driver GPU数量 | 0表示不使用GPU | 否（分布式且自定义配置时） | - |
    | Style | 配置样式 | UI / JSON | 是（自定义配置时） | UI |

    <p>补充说明：</p>
    <p>1. "必填性"指属性配置中的必填标记，仅当属性联动条件（如 ResourceMode=1 且 ConfigType=CUSTOM）满足时才触发必填校验；</p>
    <p>2. ConfigType 为 DEFAULT（默认配置）时，需调用 ListComputeResourceOptions 接口获取所选计算资源的默认规格值，并将其填充到运行参数（ExecutorCU、DriverCU、ExecutorMinNum、ExecutorMaxNum 等）后传入；ConfigType 为 CUSTOM（自定义配置）时，运行参数由调用方自行指定；</p>

    """

    def __init__(self):
        r"""
        :param _TaskTypeName: <p>任务类型：SQL：用于执行SQL查询和数据处理操作；DATA_INTEGRATION：用于离线数据接入操作；NOTEBOOK：用于运行Notebook脚本；RUN_WORKFLOW：用于执行嵌套工作流；PYTHON：用于运行Python脚本；RAY_JOB：用于运行Ray作业；DATA_QUALITY：用于数据质量监控；IF_ELSE：用于条件分支判断；FOR_EACH：用于循环遍历执行；</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param _Notebook: <p>Notebook 类型扩展信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Notebook: :class:`tencentcloud.databuddy.v20260715.models.TaskTypeNotebookExt`
        :param _TaskTypePropertyList: <p>任务类型属性列表，不同任务类型所需的 PropertyKey 不同，具体取值请参考 ListWorkflowTaskTypeProperties 接口返回</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypePropertyList: list of TaskTypeProperty
        :param _RuntimePropertyList: <p>运行时属性列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimePropertyList: list of TaskTypeProperty
        """
        self._TaskTypeName = None
        self._Notebook = None
        self._TaskTypePropertyList = None
        self._RuntimePropertyList = None

    @property
    def TaskTypeName(self):
        r"""<p>任务类型：SQL：用于执行SQL查询和数据处理操作；DATA_INTEGRATION：用于离线数据接入操作；NOTEBOOK：用于运行Notebook脚本；RUN_WORKFLOW：用于执行嵌套工作流；PYTHON：用于运行Python脚本；RAY_JOB：用于运行Ray作业；DATA_QUALITY：用于数据质量监控；IF_ELSE：用于条件分支判断；FOR_EACH：用于循环遍历执行；</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def Notebook(self):
        r"""<p>Notebook 类型扩展信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.TaskTypeNotebookExt`
        """
        return self._Notebook

    @Notebook.setter
    def Notebook(self, Notebook):
        self._Notebook = Notebook

    @property
    def TaskTypePropertyList(self):
        r"""<p>任务类型属性列表，不同任务类型所需的 PropertyKey 不同，具体取值请参考 ListWorkflowTaskTypeProperties 接口返回</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskTypeProperty
        """
        return self._TaskTypePropertyList

    @TaskTypePropertyList.setter
    def TaskTypePropertyList(self, TaskTypePropertyList):
        self._TaskTypePropertyList = TaskTypePropertyList

    @property
    def RuntimePropertyList(self):
        r"""<p>运行时属性列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskTypeProperty
        """
        return self._RuntimePropertyList

    @RuntimePropertyList.setter
    def RuntimePropertyList(self, RuntimePropertyList):
        self._RuntimePropertyList = RuntimePropertyList


    def _deserialize(self, params):
        self._TaskTypeName = params.get("TaskTypeName")
        if params.get("Notebook") is not None:
            self._Notebook = TaskTypeNotebookExt()
            self._Notebook._deserialize(params.get("Notebook"))
        if params.get("TaskTypePropertyList") is not None:
            self._TaskTypePropertyList = []
            for item in params.get("TaskTypePropertyList"):
                obj = TaskTypeProperty()
                obj._deserialize(item)
                self._TaskTypePropertyList.append(obj)
        if params.get("RuntimePropertyList") is not None:
            self._RuntimePropertyList = []
            for item in params.get("RuntimePropertyList"):
                obj = TaskTypeProperty()
                obj._deserialize(item)
                self._RuntimePropertyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTypeNotebookExt(AbstractModel):
    r"""Notebook 类型任务扩展

    """

    def __init__(self):
        r"""
        :param _Source: <p>脚本来源。取值：SCRIPT_SOURCE_LOCAL（本地）/ SCRIPT_SOURCE_GIT（Git 仓库）/<br>SCRIPT_SOURCE_CFS（CFS 文件系统）/ SCRIPT_SOURCE_COS（COS 对象存储）/<br>SCRIPT_SOURCE_WORKSPACE（工作空间）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _DisplayPath: <p>前端显示使用，对执行平台无意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayPath: str
        :param _NotebookPath: <p>Notebook 相对路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookPath: str
        :param _NotebookAbsolutePath: <p>Notebook 绝对路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookAbsolutePath: str
        """
        self._Source = None
        self._DisplayPath = None
        self._NotebookPath = None
        self._NotebookAbsolutePath = None

    @property
    def Source(self):
        r"""<p>脚本来源。取值：SCRIPT_SOURCE_LOCAL（本地）/ SCRIPT_SOURCE_GIT（Git 仓库）/<br>SCRIPT_SOURCE_CFS（CFS 文件系统）/ SCRIPT_SOURCE_COS（COS 对象存储）/<br>SCRIPT_SOURCE_WORKSPACE（工作空间）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DisplayPath(self):
        r"""<p>前端显示使用，对执行平台无意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayPath

    @DisplayPath.setter
    def DisplayPath(self, DisplayPath):
        self._DisplayPath = DisplayPath

    @property
    def NotebookPath(self):
        r"""<p>Notebook 相对路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NotebookPath

    @NotebookPath.setter
    def NotebookPath(self, NotebookPath):
        self._NotebookPath = NotebookPath

    @property
    def NotebookAbsolutePath(self):
        r"""<p>Notebook 绝对路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NotebookAbsolutePath

    @NotebookAbsolutePath.setter
    def NotebookAbsolutePath(self, NotebookAbsolutePath):
        self._NotebookAbsolutePath = NotebookAbsolutePath


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._DisplayPath = params.get("DisplayPath")
        self._NotebookPath = params.get("NotebookPath")
        self._NotebookAbsolutePath = params.get("NotebookAbsolutePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTypeProperty(AbstractModel):
    r"""任务类型属性键值对

    """

    def __init__(self):
        r"""
        :param _PropertyKey: 属性名
注意：此字段可能返回 null，表示取不到有效值。
        :type PropertyKey: str
        :param _PropertyValue: 属性值
注意：此字段可能返回 null，表示取不到有效值。
        :type PropertyValue: str
        """
        self._PropertyKey = None
        self._PropertyValue = None

    @property
    def PropertyKey(self):
        r"""属性名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def PropertyValue(self):
        r"""属性值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._PropertyValue = params.get("PropertyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkflowBundleRequest(AbstractModel):
    r"""UnbindWorkflowBundle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        """
        self._WorkspaceId = None
        self._WorkflowId = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkflowBundleResponse(AbstractModel):
    r"""UnbindWorkflowBundle返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>解绑工作流Bundle信息响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>解绑工作流Bundle信息响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UnbindWorkflowBundleRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UnbindWorkflowBundleRsp(AbstractModel):
    r"""UnbindWorkflowBundleRsp

    """

    def __init__(self):
        r"""
        :param _Status: 操作状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConsoleGroupRequest(AbstractModel):
    r"""UpdateConsoleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: <p>用户组 ID</p>
        :type GroupId: str
        :param _OperType: <p>修改标识：USER_GROUP_OPER_TYPE_ADD_USER(1)=添加成员、USER_GROUP_OPER_TYPE_DELETE_USER(2)=删除成员、USER_GROUP_OPER_TYPE_BASIC_INFO(3)=基础信息（别名和描述）</p>
        :type OperType: int
        :param _GroupName: <p>用户组名称</p>
        :type GroupName: str
        :param _GroupNickname: <p>用户组别名</p>
        :type GroupNickname: str
        :param _Description: <p>用户组描述</p>
        :type Description: str
        :param _UserUins: <p>成员 UIN 列表（OperType 为添加/删除成员时使用），单次最多100个</p>
        :type UserUins: list of str
        """
        self._GroupId = None
        self._OperType = None
        self._GroupName = None
        self._GroupNickname = None
        self._Description = None
        self._UserUins = None

    @property
    def GroupId(self):
        r"""<p>用户组 ID</p>
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OperType(self):
        r"""<p>修改标识：USER_GROUP_OPER_TYPE_ADD_USER(1)=添加成员、USER_GROUP_OPER_TYPE_DELETE_USER(2)=删除成员、USER_GROUP_OPER_TYPE_BASIC_INFO(3)=基础信息（别名和描述）</p>
        :rtype: int
        """
        return self._OperType

    @OperType.setter
    def OperType(self, OperType):
        self._OperType = OperType

    @property
    def GroupName(self):
        r"""<p>用户组名称</p>
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNickname(self):
        r"""<p>用户组别名</p>
        :rtype: str
        """
        return self._GroupNickname

    @GroupNickname.setter
    def GroupNickname(self, GroupNickname):
        self._GroupNickname = GroupNickname

    @property
    def Description(self):
        r"""<p>用户组描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserUins(self):
        r"""<p>成员 UIN 列表（OperType 为添加/删除成员时使用），单次最多100个</p>
        :rtype: list of str
        """
        return self._UserUins

    @UserUins.setter
    def UserUins(self, UserUins):
        self._UserUins = UserUins


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._OperType = params.get("OperType")
        self._GroupName = params.get("GroupName")
        self._GroupNickname = params.get("GroupNickname")
        self._Description = params.get("Description")
        self._UserUins = params.get("UserUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConsoleGroupResponse(AbstractModel):
    r"""UpdateConsoleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleGroupRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleGroupRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateConsoleGroupRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateConsoleGroupRsp(AbstractModel):
    r"""修改控制台用户组响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConsoleUsersRequest(AbstractModel):
    r"""UpdateConsoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserUins: <p>用户 UIN 列表，单次最多100个</p>
        :type UserUins: list of str
        :param _RoleIds: <p>角色 ID 列表</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul>
        :type RoleIds: list of str
        """
        self._UserUins = None
        self._RoleIds = None

    @property
    def UserUins(self):
        r"""<p>用户 UIN 列表，单次最多100个</p>
        :rtype: list of str
        """
        return self._UserUins

    @UserUins.setter
    def UserUins(self, UserUins):
        self._UserUins = UserUins

    @property
    def RoleIds(self):
        r"""<p>角色 ID 列表</p><p>枚举值：</p><ul><li>2001： 控制台管理员</li><li>2002： 控制台成员</li></ul>
        :rtype: list of str
        """
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        self._UserUins = params.get("UserUins")
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConsoleUsersResponse(AbstractModel):
    r"""UpdateConsoleUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateConsoleUsersRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateConsoleUsersRsp(AbstractModel):
    r"""修改控制台用户响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFileRequest(AbstractModel):
    r"""UpdateFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :type WorkspaceId: str
        :param _FileId: <p>文件 ID。来源：CreateFile / ListFiles / GetFile 接口返回的 FileId</p>
        :type FileId: str
        :param _FileConfig: <p>文件运行配置。不传则不更新配置</p>
        :type FileConfig: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        :param _FileType: <p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :type FileType: str
        :param _BundleId: <p>绑定的 BundleId。来源：ListBundles 接口返回的 BundleId</p>
        :type BundleId: str
        :param _BundleInfo: <p>绑定的 BundleInfo，JSON 字符串</p>
        :type BundleInfo: str
        :param _Storage: <p>文件内容。不传则不更新内容</p>
        :type Storage: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        :param _FileName: <p>目标文件名，非空且与当前文件名不同时执行 rename 动作。长度不超过 SCRIPT_NAME_MAX_LENGTH，禁止以 . 或 .. 开头/结尾，禁止空格、双点、控制字符及 Linux 保留名（参考 docs/linux_filename_rules.md）。与 ExtensionType 一起校验后缀合法性</p>
        :type FileName: str
        :param _ParentFolderPath: <p>目标父目录路径，非空时执行 move 动作。根目录传 /；与 FileName 可同时出现，语义为「移动+重命名」。与 CreateFile 的 ParentFolderPath 保持一致</p>
        :type ParentFolderPath: str
        :param _TargetFileType: <p>目标父目录的 FileType。取值：FOLDER、GIT_FOLDER。仅当 ParentFolderPath 非空时使用；缺省时按解析出的父目录实际类型处理</p>
        :type TargetFileType: str
        :param _UpdateAction: <p>动作类型（必填，未来版本会强制校验）。取值：1 = UPDATE_CONTENT（仅更新 FileConfig / Storage / Bundle*，禁止传 FileName / ParentFolderPath / TargetFileType）；2 = RENAME（仅重命名，必须传 FileName，禁止传 ParentFolderPath / FileConfig / Storage / Bundle*）；3 = MOVE（仅移动，必须传 ParentFolderPath，禁止传 FileName / FileConfig / Storage / Bundle*）。参数互斥校验失败会返回 ParamIllegal 错误</p>
        :type UpdateAction: int
        """
        self._WorkspaceId = None
        self._FileId = None
        self._FileConfig = None
        self._FileType = None
        self._BundleId = None
        self._BundleInfo = None
        self._Storage = None
        self._FileName = None
        self._ParentFolderPath = None
        self._TargetFileType = None
        self._UpdateAction = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID。来源：ListWorkspaces 接口返回的 WorkspaceId</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileId(self):
        r"""<p>文件 ID。来源：CreateFile / ListFiles / GetFile 接口返回的 FileId</p>
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileConfig(self):
        r"""<p>文件运行配置。不传则不更新配置</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileConfig`
        """
        return self._FileConfig

    @FileConfig.setter
    def FileConfig(self, FileConfig):
        self._FileConfig = FileConfig

    @property
    def FileType(self):
        r"""<p>文件类型。取值：FILE（普通文件/脚本）、NOTEBOOK_FILE（Notebook）、SQL_FILE（SQL文件）。对应 common/domain/entity.proto EntityType</p>
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def BundleId(self):
        r"""<p>绑定的 BundleId。来源：ListBundles 接口返回的 BundleId</p>
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>绑定的 BundleInfo，JSON 字符串</p>
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def Storage(self):
        r"""<p>文件内容。不传则不更新内容</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileStorage`
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def FileName(self):
        r"""<p>目标文件名，非空且与当前文件名不同时执行 rename 动作。长度不超过 SCRIPT_NAME_MAX_LENGTH，禁止以 . 或 .. 开头/结尾，禁止空格、双点、控制字符及 Linux 保留名（参考 docs/linux_filename_rules.md）。与 ExtensionType 一起校验后缀合法性</p>
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ParentFolderPath(self):
        r"""<p>目标父目录路径，非空时执行 move 动作。根目录传 /；与 FileName 可同时出现，语义为「移动+重命名」。与 CreateFile 的 ParentFolderPath 保持一致</p>
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def TargetFileType(self):
        r"""<p>目标父目录的 FileType。取值：FOLDER、GIT_FOLDER。仅当 ParentFolderPath 非空时使用；缺省时按解析出的父目录实际类型处理</p>
        :rtype: str
        """
        return self._TargetFileType

    @TargetFileType.setter
    def TargetFileType(self, TargetFileType):
        self._TargetFileType = TargetFileType

    @property
    def UpdateAction(self):
        r"""<p>动作类型（必填，未来版本会强制校验）。取值：1 = UPDATE_CONTENT（仅更新 FileConfig / Storage / Bundle*，禁止传 FileName / ParentFolderPath / TargetFileType）；2 = RENAME（仅重命名，必须传 FileName，禁止传 ParentFolderPath / FileConfig / Storage / Bundle*）；3 = MOVE（仅移动，必须传 ParentFolderPath，禁止传 FileName / FileConfig / Storage / Bundle*）。参数互斥校验失败会返回 ParamIllegal 错误</p>
        :rtype: int
        """
        return self._UpdateAction

    @UpdateAction.setter
    def UpdateAction(self, UpdateAction):
        self._UpdateAction = UpdateAction


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileId = params.get("FileId")
        if params.get("FileConfig") is not None:
            self._FileConfig = FileConfig()
            self._FileConfig._deserialize(params.get("FileConfig"))
        self._FileType = params.get("FileType")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        if params.get("Storage") is not None:
            self._Storage = FileStorage()
            self._Storage._deserialize(params.get("Storage"))
        self._FileName = params.get("FileName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._TargetFileType = params.get("TargetFileType")
        self._UpdateAction = params.get("UpdateAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFileResponse(AbstractModel):
    r"""UpdateFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FileInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = FileInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateFolderRequest(AbstractModel):
    r"""UpdateFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID</p>
        :type WorkspaceId: str
        :param _Folder: <p>待更新文件夹</p>
        :type Folder: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        :param _OperationType: <p>操作类型</p><p>枚举值：</p><ul><li>1： 重命名</li><li>2： 移动</li></ul>
        :type OperationType: str
        :param _FolderName: <p>重命名后的文件名，OperationType = 1时生效</p>
        :type FolderName: str
        :param _TargetParent: <p>移动的目的文件夹，OperationType = 2时生效</p>
        :type TargetParent: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        self._WorkspaceId = None
        self._Folder = None
        self._OperationType = None
        self._FolderName = None
        self._TargetParent = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Folder(self):
        r"""<p>待更新文件夹</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._Folder

    @Folder.setter
    def Folder(self, Folder):
        self._Folder = Folder

    @property
    def OperationType(self):
        r"""<p>操作类型</p><p>枚举值：</p><ul><li>1： 重命名</li><li>2： 移动</li></ul>
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def FolderName(self):
        r"""<p>重命名后的文件名，OperationType = 1时生效</p>
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def TargetParent(self):
        r"""<p>移动的目的文件夹，OperationType = 2时生效</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.FolderLocator`
        """
        return self._TargetParent

    @TargetParent.setter
    def TargetParent(self, TargetParent):
        self._TargetParent = TargetParent


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Folder") is not None:
            self._Folder = FolderLocator()
            self._Folder._deserialize(params.get("Folder"))
        self._OperationType = params.get("OperationType")
        self._FolderName = params.get("FolderName")
        if params.get("TargetParent") is not None:
            self._TargetParent = FolderLocator()
            self._TargetParent._deserialize(params.get("TargetParent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFolderResponse(AbstractModel):
    r"""UpdateFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>更新文件夹结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateFolderRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>更新文件夹结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateFolderRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateFolderRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateFolderRsp(AbstractModel):
    r"""更新文件夹回包

    """

    def __init__(self):
        r"""
        :param _Status: <p>更新文件夹结果，true为成功</p>
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""<p>更新文件夹结果，true为成功</p>
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowRequest(AbstractModel):
    r"""UpdateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :type WorkspaceId: str
        :param _WorkflowId: <p>待更新的工作流ID，可通过 ListWorkflows 获取。必填</p>
        :type WorkflowId: str
        :param _FieldToRemoveList: <p>需要清空的字段名列表，用于将指定字段重置为空</p>
        :type FieldToRemoveList: list of str
        :param _NewSetting: <p>更新后的工作流配置，仅传入需要变更的部分即可</p>
        :type NewSetting: :class:`tencentcloud.databuddy.v20260715.models.Workflow`
        """
        self._WorkspaceId = None
        self._WorkflowId = None
        self._FieldToRemoveList = None
        self._NewSetting = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取。必填</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>待更新的工作流ID，可通过 ListWorkflows 获取。必填</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def FieldToRemoveList(self):
        r"""<p>需要清空的字段名列表，用于将指定字段重置为空</p>
        :rtype: list of str
        """
        return self._FieldToRemoveList

    @FieldToRemoveList.setter
    def FieldToRemoveList(self, FieldToRemoveList):
        self._FieldToRemoveList = FieldToRemoveList

    @property
    def NewSetting(self):
        r"""<p>更新后的工作流配置，仅传入需要变更的部分即可</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.Workflow`
        """
        return self._NewSetting

    @NewSetting.setter
    def NewSetting(self, NewSetting):
        self._NewSetting = NewSetting


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._FieldToRemoveList = params.get("FieldToRemoveList")
        if params.get("NewSetting") is not None:
            self._NewSetting = Workflow()
            self._NewSetting._deserialize(params.get("NewSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowResponse(AbstractModel):
    r"""UpdateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>更新工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>更新工作流响应内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateWorkflowRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkflowRsp(AbstractModel):
    r"""UpdateWorkflowRsp

    """

    def __init__(self):
        r"""
        :param _Status: 更新状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""更新状态，true 表示成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkspaceRequest(AbstractModel):
    r"""UpdateWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID</p>
        :type WorkspaceId: str
        :param _WorkspaceName: <p>工作空间名称，max_len=128</p>
        :type WorkspaceName: str
        :param _Description: <p>工作空间描述，max_len=300</p>
        :type Description: str
        """
        self._WorkspaceId = None
        self._WorkspaceName = None
        self._Description = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkspaceName(self):
        r"""<p>工作空间名称，max_len=128</p>
        :rtype: str
        """
        return self._WorkspaceName

    @WorkspaceName.setter
    def WorkspaceName(self, WorkspaceName):
        self._WorkspaceName = WorkspaceName

    @property
    def Description(self):
        r"""<p>工作空间描述，max_len=300</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkspaceName = params.get("WorkspaceName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkspaceResponse(AbstractModel):
    r"""UpdateWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>操作结果</p>
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>操作结果</p>
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateWorkspaceRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkspaceRoleRequest(AbstractModel):
    r"""UpdateWorkspaceRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _BasicInfo: 角色信息
        :type BasicInfo: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        :param _Permissions: 功能点权限
        :type Permissions: list of RolePermission
        """
        self._WorkspaceId = None
        self._BasicInfo = None
        self._Permissions = None

    @property
    def WorkspaceId(self):
        r"""工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def BasicInfo(self):
        r"""角色信息
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RoleBasicInfo`
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def Permissions(self):
        r"""功能点权限
        :rtype: list of RolePermission
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("BasicInfo") is not None:
            self._BasicInfo = RoleBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = RolePermission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkspaceRoleResponse(AbstractModel):
    r"""UpdateWorkspaceRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 更新工作空间角色结果
        :type Data: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRoleResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""更新工作空间角色结果
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRoleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateWorkspaceRoleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkspaceRoleResult(AbstractModel):
    r"""更新工作空间角色结果

    """

    def __init__(self):
        r"""
        :param _Status: 更新工作空间角色是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""更新工作空间角色是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkspaceRsp(AbstractModel):
    r"""修改工作空间响应

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""操作是否成功
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    r"""用户基本信息

    """

    def __init__(self):
        r"""
        :param _UserUin: <p>uin</p>
        :type UserUin: str
        :param _UserName: <p>子用户名称</p>
        :type UserName: str
        :param _Nickname: <p>子用户昵称</p>
        :type Nickname: str
        :param _UserTag: <p>0: 普通用户 1: entraId用户</p>
        :type UserTag: str
        """
        self._UserUin = None
        self._UserName = None
        self._Nickname = None
        self._UserTag = None

    @property
    def UserUin(self):
        r"""<p>uin</p>
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def UserName(self):
        r"""<p>子用户名称</p>
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        r"""<p>子用户昵称</p>
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def UserTag(self):
        r"""<p>0: 普通用户 1: entraId用户</p>
        :rtype: str
        """
        return self._UserTag

    @UserTag.setter
    def UserTag(self, UserTag):
        self._UserTag = UserTag


    def _deserialize(self, params):
        self._UserUin = params.get("UserUin")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        self._UserTag = params.get("UserTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Workflow(AbstractModel):
    r"""工作流完整配置

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间ID，可通过 ListWorkspaces 获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _BaseInfo: <p>工作流基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfo`
        :param _Trigger: <p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Trigger: list of WorkflowTriggerConfiguration
        :param _ParamList: <p>工作流参数列表 参数名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt; 最长128个字符</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamList: list of ParamInfo
        :param _LabelList: <p>标签 标签名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;'，最长128个字符</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelList: list of LabelBrief
        :param _Alarm: <p>工作流告警配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarm: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        :param _MonitorMetric: <p>监控指标配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorMetric: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        :param _AdvanceConfig: <p>工作流高级设置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceConfig: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        :param _TaskList: <p>工作流任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskList: list of WorkflowTask
        :param _BundleId: <p>BundleId，可通过 Bundle 相关接口获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: <p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        :param _GitConfigId: <p>GIT配置ID，对应GetWorkspaceConfig接口中的ConfigKey</p>    -
注意：此字段可能返回 null，表示取不到有效值。
        :type GitConfigId: str
        :param _GitBranch: <p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitBranch: str
        """
        self._WorkspaceId = None
        self._BaseInfo = None
        self._Trigger = None
        self._ParamList = None
        self._LabelList = None
        self._Alarm = None
        self._MonitorMetric = None
        self._AdvanceConfig = None
        self._TaskList = None
        self._BundleId = None
        self._BundleInfo = None
        self._GitConfigId = None
        self._GitBranch = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID，可通过 ListWorkspaces 获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def BaseInfo(self):
        r"""<p>工作流基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def Trigger(self):
        r"""<p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTriggerConfiguration
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def ParamList(self):
        r"""<p>工作流参数列表 参数名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt; 最长128个字符</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def LabelList(self):
        r"""<p>标签 标签名必填且只能包含数字、大小写字母、空格、.$@#!%^&amp;*()-_+=&gt;'，最长128个字符</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LabelBrief
        """
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def Alarm(self):
        r"""<p>工作流告警配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        """
        return self._Alarm

    @Alarm.setter
    def Alarm(self, Alarm):
        self._Alarm = Alarm

    @property
    def MonitorMetric(self):
        r"""<p>监控指标配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        """
        return self._MonitorMetric

    @MonitorMetric.setter
    def MonitorMetric(self, MonitorMetric):
        self._MonitorMetric = MonitorMetric

    @property
    def AdvanceConfig(self):
        r"""<p>工作流高级设置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowAdvanceConfig`
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig

    @property
    def TaskList(self):
        r"""<p>工作流任务列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTask
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def BundleId(self):
        r"""<p>BundleId，可通过 Bundle 相关接口获取</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def GitConfigId(self):
        r"""<p>GIT配置ID，对应GetWorkspaceConfig接口中的ConfigKey</p>    -
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitConfigId

    @GitConfigId.setter
    def GitConfigId(self, GitConfigId):
        self._GitConfigId = GitConfigId

    @property
    def GitBranch(self):
        r"""<p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("BaseInfo") is not None:
            self._BaseInfo = WorkflowBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("Trigger") is not None:
            self._Trigger = []
            for item in params.get("Trigger"):
                obj = WorkflowTriggerConfiguration()
                obj._deserialize(item)
                self._Trigger.append(obj)
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        if params.get("LabelList") is not None:
            self._LabelList = []
            for item in params.get("LabelList"):
                obj = LabelBrief()
                obj._deserialize(item)
                self._LabelList.append(obj)
        if params.get("Alarm") is not None:
            self._Alarm = AlarmBrief()
            self._Alarm._deserialize(params.get("Alarm"))
        if params.get("MonitorMetric") is not None:
            self._MonitorMetric = MonitorMetricBrief()
            self._MonitorMetric._deserialize(params.get("MonitorMetric"))
        if params.get("AdvanceConfig") is not None:
            self._AdvanceConfig = WorkflowAdvanceConfig()
            self._AdvanceConfig._deserialize(params.get("AdvanceConfig"))
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = WorkflowTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        self._GitConfigId = params.get("GitConfigId")
        self._GitBranch = params.get("GitBranch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowAdvanceConfig(AbstractModel):
    r"""工作流高级设置

    """

    def __init__(self):
        r"""
        :param _QueuingMode: 排队模式，ON（默认）, OFF
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuingMode: str
        :param _MaxConcurrentNum: 	
默认值为1

QueuingMode为ON时，MaxConcurrentNum 设置才生效；只能输入大于0的整数，输入非法值自动转换为1
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConcurrentNum: int
        """
        self._QueuingMode = None
        self._MaxConcurrentNum = None

    @property
    def QueuingMode(self):
        r"""排队模式，ON（默认）, OFF
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueuingMode

    @QueuingMode.setter
    def QueuingMode(self, QueuingMode):
        self._QueuingMode = QueuingMode

    @property
    def MaxConcurrentNum(self):
        r"""	
默认值为1

QueuingMode为ON时，MaxConcurrentNum 设置才生效；只能输入大于0的整数，输入非法值自动转换为1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxConcurrentNum

    @MaxConcurrentNum.setter
    def MaxConcurrentNum(self, MaxConcurrentNum):
        self._MaxConcurrentNum = MaxConcurrentNum


    def _deserialize(self, params):
        self._QueuingMode = params.get("QueuingMode")
        self._MaxConcurrentNum = params.get("MaxConcurrentNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowBaseInfo(AbstractModel):
    r"""工作流基本信息（入参用）

    """

    def __init__(self):
        r"""
        :param _WorkflowName: 工作流名称，长度不超过 1024
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowId: 工作流ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _RunUserUin: 工作流运行人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _OwnerUserName: 工作流负责人用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserName: str
        :param _CreateUserUin: 创建人UIN。系统生成字段，入参传值不生效（服务端忽略且不报错）
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        """
        self._WorkflowName = None
        self._WorkflowId = None
        self._RunUserUin = None
        self._Description = None
        self._OwnerUserName = None
        self._CreateUserUin = None

    @property
    def WorkflowName(self):
        r"""工作流名称，长度不超过 1024
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowId(self):
        r"""工作流ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def RunUserUin(self):
        r"""工作流运行人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OwnerUserName(self):
        r"""工作流负责人用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserName

    @OwnerUserName.setter
    def OwnerUserName(self, OwnerUserName):
        self._OwnerUserName = OwnerUserName

    @property
    def CreateUserUin(self):
        r"""创建人UIN。系统生成字段，入参传值不生效（服务端忽略且不报错）
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowId = params.get("WorkflowId")
        self._RunUserUin = params.get("RunUserUin")
        self._Description = params.get("Description")
        self._OwnerUserName = params.get("OwnerUserName")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowBaseInfoDetail(AbstractModel):
    r"""工作流基本信息（出参用，含系统生成字段与负责人展示信息）

    """

    def __init__(self):
        r"""
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _CreateUserUin: 创建人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _RunUserUin: 工作流运行人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _OwnerUserName: 工作流负责人用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserName: str
        :param _OwnerUserUin: 工作流负责人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserUin: str
        :param _OwnerDisplayName: 工作流负责人展示名
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerDisplayName: str
        :param _CreateTime: 创建时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._WorkflowName = None
        self._WorkflowId = None
        self._CreateUserUin = None
        self._RunUserUin = None
        self._Description = None
        self._OwnerUserName = None
        self._OwnerUserUin = None
        self._OwnerDisplayName = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def CreateUserUin(self):
        r"""创建人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def RunUserUin(self):
        r"""工作流运行人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OwnerUserName(self):
        r"""工作流负责人用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserName

    @OwnerUserName.setter
    def OwnerUserName(self, OwnerUserName):
        self._OwnerUserName = OwnerUserName

    @property
    def OwnerUserUin(self):
        r"""工作流负责人UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserUin

    @OwnerUserUin.setter
    def OwnerUserUin(self, OwnerUserUin):
        self._OwnerUserUin = OwnerUserUin

    @property
    def OwnerDisplayName(self):
        r"""工作流负责人展示名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerDisplayName

    @OwnerDisplayName.setter
    def OwnerDisplayName(self, OwnerDisplayName):
        self._OwnerDisplayName = OwnerDisplayName

    @property
    def CreateTime(self):
        r"""创建时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowId = params.get("WorkflowId")
        self._CreateUserUin = params.get("CreateUserUin")
        self._RunUserUin = params.get("RunUserUin")
        self._Description = params.get("Description")
        self._OwnerUserName = params.get("OwnerUserName")
        self._OwnerUserUin = params.get("OwnerUserUin")
        self._OwnerDisplayName = params.get("OwnerDisplayName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowBrief(AbstractModel):
    r"""工作流列表项

    """

    def __init__(self):
        r"""
        :param _WorkflowName: <p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowId: <p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _Description: <p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateUserUin: <p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _OwnerUserName: <p>工作流负责人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserName: str
        :param _OwnerUserUin: <p>工作流负责人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUserUin: str
        :param _OwnerDisplayName: <p>工作流负责人展示名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerDisplayName: str
        :param _CreateTime: <p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _LabelList: <p>标签列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelList: list of LabelBrief
        :param _Trigger: <p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Trigger: list of WorkflowTriggerConfiguration
        :param _RunUserUin: <p>工作流运行人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _RunUserName: <p>工作流运行人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserName: str
        :param _TaskList: <p>工作流任务节点列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskList: list of WorkflowTaskNodeBrief
        :param _WorkflowRunList: <p>工作流运行情况列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunList: list of WorkflowRunBrief
        :param _ResourceGroupInfoList: <p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupInfoList: list of ResourceGroupInfo
        :param _Permission: <p>授权权限类型<br>PERMISSION_TYPE_UNSPECIFIED：未指定权限<br>MANAGE : 管理权限：包含所有操作权限<br>RUN : 运行权限：可执行实体<br>VIEW : 查看权限：可查看实体内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: str
        :param _BundleId: <p>工作流绑定的 Bundle 唯一标识，未绑定时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: <p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        :param _GitConfigId: <p>Git配置ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitConfigId: str
        :param _GitBranch: <p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type GitBranch: str
        """
        self._WorkflowName = None
        self._WorkflowId = None
        self._Description = None
        self._CreateUserUin = None
        self._OwnerUserName = None
        self._OwnerUserUin = None
        self._OwnerDisplayName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LabelList = None
        self._Trigger = None
        self._RunUserUin = None
        self._RunUserName = None
        self._TaskList = None
        self._WorkflowRunList = None
        self._ResourceGroupInfoList = None
        self._Permission = None
        self._BundleId = None
        self._BundleInfo = None
        self._GitConfigId = None
        self._GitBranch = None

    @property
    def WorkflowName(self):
        r"""<p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Description(self):
        r"""<p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateUserUin(self):
        r"""<p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def OwnerUserName(self):
        r"""<p>工作流负责人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserName

    @OwnerUserName.setter
    def OwnerUserName(self, OwnerUserName):
        self._OwnerUserName = OwnerUserName

    @property
    def OwnerUserUin(self):
        r"""<p>工作流负责人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUserUin

    @OwnerUserUin.setter
    def OwnerUserUin(self, OwnerUserUin):
        self._OwnerUserUin = OwnerUserUin

    @property
    def OwnerDisplayName(self):
        r"""<p>工作流负责人展示名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerDisplayName

    @OwnerDisplayName.setter
    def OwnerDisplayName(self, OwnerDisplayName):
        self._OwnerDisplayName = OwnerDisplayName

    @property
    def CreateTime(self):
        r"""<p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LabelList(self):
        r"""<p>标签列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LabelBrief
        """
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def Trigger(self):
        r"""<p>工作流调度配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTriggerConfiguration
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def RunUserUin(self):
        r"""<p>工作流运行人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def RunUserName(self):
        r"""<p>工作流运行人用户名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserName

    @RunUserName.setter
    def RunUserName(self, RunUserName):
        self._RunUserName = RunUserName

    @property
    def TaskList(self):
        r"""<p>工作流任务节点列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowTaskNodeBrief
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def WorkflowRunList(self):
        r"""<p>工作流运行情况列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowRunBrief
        """
        return self._WorkflowRunList

    @WorkflowRunList.setter
    def WorkflowRunList(self, WorkflowRunList):
        self._WorkflowRunList = WorkflowRunList

    @property
    def ResourceGroupInfoList(self):
        r"""<p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceGroupInfo
        """
        return self._ResourceGroupInfoList

    @ResourceGroupInfoList.setter
    def ResourceGroupInfoList(self, ResourceGroupInfoList):
        self._ResourceGroupInfoList = ResourceGroupInfoList

    @property
    def Permission(self):
        r"""<p>授权权限类型<br>PERMISSION_TYPE_UNSPECIFIED：未指定权限<br>MANAGE : 管理权限：包含所有操作权限<br>RUN : 运行权限：可执行实体<br>VIEW : 查看权限：可查看实体内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def BundleId(self):
        r"""<p>工作流绑定的 Bundle 唯一标识，未绑定时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""<p>Bundle信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def GitConfigId(self):
        r"""<p>Git配置ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitConfigId

    @GitConfigId.setter
    def GitConfigId(self, GitConfigId):
        self._GitConfigId = GitConfigId

    @property
    def GitBranch(self):
        r"""<p>Git分支信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch


    def _deserialize(self, params):
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowId = params.get("WorkflowId")
        self._Description = params.get("Description")
        self._CreateUserUin = params.get("CreateUserUin")
        self._OwnerUserName = params.get("OwnerUserName")
        self._OwnerUserUin = params.get("OwnerUserUin")
        self._OwnerDisplayName = params.get("OwnerDisplayName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("LabelList") is not None:
            self._LabelList = []
            for item in params.get("LabelList"):
                obj = LabelBrief()
                obj._deserialize(item)
                self._LabelList.append(obj)
        if params.get("Trigger") is not None:
            self._Trigger = []
            for item in params.get("Trigger"):
                obj = WorkflowTriggerConfiguration()
                obj._deserialize(item)
                self._Trigger.append(obj)
        self._RunUserUin = params.get("RunUserUin")
        self._RunUserName = params.get("RunUserName")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = WorkflowTaskNodeBrief()
                obj._deserialize(item)
                self._TaskList.append(obj)
        if params.get("WorkflowRunList") is not None:
            self._WorkflowRunList = []
            for item in params.get("WorkflowRunList"):
                obj = WorkflowRunBrief()
                obj._deserialize(item)
                self._WorkflowRunList.append(obj)
        if params.get("ResourceGroupInfoList") is not None:
            self._ResourceGroupInfoList = []
            for item in params.get("ResourceGroupInfoList"):
                obj = ResourceGroupInfo()
                obj._deserialize(item)
                self._ResourceGroupInfoList.append(obj)
        self._Permission = params.get("Permission")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        self._GitConfigId = params.get("GitConfigId")
        self._GitBranch = params.get("GitBranch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRun(AbstractModel):
    r"""工作流运行信息

    """

    def __init__(self):
        r"""
        :param _AppId: <p>主账号ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _WorkflowName: <p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowId: <p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowRunId: <p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _WorkspaceId: <p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _TriggerType: <p>触发方式，Scheduler、ManualTrigger、Event (参考SchedulerTriggerType)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param _RunStartTime: <p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _PendingStartTime: <p>pending 状态开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PendingStartTime: str
        :param _QueueStartTime: <p>queue 状态开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueStartTime: str
        :param _RunEndTime: <p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunEndTime: str
        :param _EndTime: <p>终态时间，运行进入终态时都有值，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _RunCostTime: <p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunCostTime: str
        :param _QueueCostTime: <p>并发排队花费时间，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueCostTime: str
        :param _PendingCostTime: <p>等待资源花费时间，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PendingCostTime: str
        :param _RunState: <p>运行状态。CREATE(&quot;初始化&quot;),     QUEUED(&quot;等待中&quot;),     PENDING(&quot;准备中&quot;),     RUNNING(&quot;运行中&quot;),     SKIPPED(&quot;跳过运行&quot;),     SUCCESS(&quot;成功&quot;),     FAILED(&quot;失败&quot;),     TERMINATING(&quot;终止中&quot;),     TERMINATED(&quot;终止&quot;),     CANCELLED(&quot;被手动终止&quot;)等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _ResourceGroupIds: <p>计算资源（任务的资源组ID集合）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupIds: list of str
        :param _RunUserUin: <p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _RunUserName: <p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserName: str
        :param _ErrorCodeString: <p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        :param _WorkflowParams: <p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowParams: str
        :param _WorkflowVersionId: <p>工作流版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowVersionId: str
        :param _SupportRerun: <p>当前工作流是否支持重跑</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportRerun: bool
        :param _CreateTime: <p>工作流运行创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _RerunTimes: <p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RerunTimes: int
        :param _SelectedTaskIds: <p>运行的任务范围，任务ID列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SelectedTaskIds: list of str
        :param _ResourceGroupInfoList: <p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupInfoList: list of ResourceGroupInfo
        :param _LabelList: <p>标签列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelList: list of LabelBrief
        :param _ParentWorkflowRunId: <p>父工作流运行ID 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentWorkflowRunId: str
        :param _ParentWorkflowTaskRunId: <p>父工作流任务运行ID 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentWorkflowTaskRunId: str
        :param _ParentWorkflowTaskRunName: <p>父工作流任务运行名称 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentWorkflowTaskRunName: str
        :param _Permission: <p>授权权限类型<br>PERMISSION_TYPE_UNSPECIFIED：未指定权限<br>MANAGE : 管理权限：包含所有操作权限<br>RUN : 运行权限：可执行实体<br>VIEW : 查看权限：可查看实体内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: str
        :param _AdvancedParameters: <p>工作流高级运行时用户填入的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedParameters: list of AdvancedParameter
        :param _ScheduledTime: <p>计划调度时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTime: str
        """
        self._AppId = None
        self._WorkflowName = None
        self._WorkflowId = None
        self._WorkflowRunId = None
        self._WorkspaceId = None
        self._TriggerType = None
        self._RunStartTime = None
        self._PendingStartTime = None
        self._QueueStartTime = None
        self._RunEndTime = None
        self._EndTime = None
        self._RunCostTime = None
        self._QueueCostTime = None
        self._PendingCostTime = None
        self._RunState = None
        self._ResourceGroupIds = None
        self._RunUserUin = None
        self._RunUserName = None
        self._ErrorCodeString = None
        self._WorkflowParams = None
        self._WorkflowVersionId = None
        self._SupportRerun = None
        self._CreateTime = None
        self._RerunTimes = None
        self._SelectedTaskIds = None
        self._ResourceGroupInfoList = None
        self._LabelList = None
        self._ParentWorkflowRunId = None
        self._ParentWorkflowTaskRunId = None
        self._ParentWorkflowTaskRunName = None
        self._Permission = None
        self._AdvancedParameters = None
        self._ScheduledTime = None

    @property
    def AppId(self):
        r"""<p>主账号ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def WorkflowName(self):
        r"""<p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def TriggerType(self):
        r"""<p>触发方式，Scheduler、ManualTrigger、Event (参考SchedulerTriggerType)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def RunStartTime(self):
        r"""<p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def PendingStartTime(self):
        r"""<p>pending 状态开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PendingStartTime

    @PendingStartTime.setter
    def PendingStartTime(self, PendingStartTime):
        self._PendingStartTime = PendingStartTime

    @property
    def QueueStartTime(self):
        r"""<p>queue 状态开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueStartTime

    @QueueStartTime.setter
    def QueueStartTime(self, QueueStartTime):
        self._QueueStartTime = QueueStartTime

    @property
    def RunEndTime(self):
        r"""<p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def EndTime(self):
        r"""<p>终态时间，运行进入终态时都有值，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RunCostTime(self):
        r"""<p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunCostTime

    @RunCostTime.setter
    def RunCostTime(self, RunCostTime):
        self._RunCostTime = RunCostTime

    @property
    def QueueCostTime(self):
        r"""<p>并发排队花费时间，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueCostTime

    @QueueCostTime.setter
    def QueueCostTime(self, QueueCostTime):
        self._QueueCostTime = QueueCostTime

    @property
    def PendingCostTime(self):
        r"""<p>等待资源花费时间，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PendingCostTime

    @PendingCostTime.setter
    def PendingCostTime(self, PendingCostTime):
        self._PendingCostTime = PendingCostTime

    @property
    def RunState(self):
        r"""<p>运行状态。CREATE(&quot;初始化&quot;),     QUEUED(&quot;等待中&quot;),     PENDING(&quot;准备中&quot;),     RUNNING(&quot;运行中&quot;),     SKIPPED(&quot;跳过运行&quot;),     SUCCESS(&quot;成功&quot;),     FAILED(&quot;失败&quot;),     TERMINATING(&quot;终止中&quot;),     TERMINATED(&quot;终止&quot;),     CANCELLED(&quot;被手动终止&quot;)等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def ResourceGroupIds(self):
        r"""<p>计算资源（任务的资源组ID集合）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ResourceGroupIds

    @ResourceGroupIds.setter
    def ResourceGroupIds(self, ResourceGroupIds):
        self._ResourceGroupIds = ResourceGroupIds

    @property
    def RunUserUin(self):
        r"""<p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def RunUserName(self):
        r"""<p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserName

    @RunUserName.setter
    def RunUserName(self, RunUserName):
        self._RunUserName = RunUserName

    @property
    def ErrorCodeString(self):
        r"""<p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString

    @property
    def WorkflowParams(self):
        r"""<p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowVersionId(self):
        r"""<p>工作流版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowVersionId

    @WorkflowVersionId.setter
    def WorkflowVersionId(self, WorkflowVersionId):
        self._WorkflowVersionId = WorkflowVersionId

    @property
    def SupportRerun(self):
        r"""<p>当前工作流是否支持重跑</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportRerun

    @SupportRerun.setter
    def SupportRerun(self, SupportRerun):
        self._SupportRerun = SupportRerun

    @property
    def CreateTime(self):
        r"""<p>工作流运行创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RerunTimes(self):
        r"""<p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RerunTimes

    @RerunTimes.setter
    def RerunTimes(self, RerunTimes):
        self._RerunTimes = RerunTimes

    @property
    def SelectedTaskIds(self):
        r"""<p>运行的任务范围，任务ID列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SelectedTaskIds

    @SelectedTaskIds.setter
    def SelectedTaskIds(self, SelectedTaskIds):
        self._SelectedTaskIds = SelectedTaskIds

    @property
    def ResourceGroupInfoList(self):
        r"""<p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceGroupInfo
        """
        return self._ResourceGroupInfoList

    @ResourceGroupInfoList.setter
    def ResourceGroupInfoList(self, ResourceGroupInfoList):
        self._ResourceGroupInfoList = ResourceGroupInfoList

    @property
    def LabelList(self):
        r"""<p>标签列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LabelBrief
        """
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def ParentWorkflowRunId(self):
        r"""<p>父工作流运行ID 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentWorkflowRunId

    @ParentWorkflowRunId.setter
    def ParentWorkflowRunId(self, ParentWorkflowRunId):
        self._ParentWorkflowRunId = ParentWorkflowRunId

    @property
    def ParentWorkflowTaskRunId(self):
        r"""<p>父工作流任务运行ID 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentWorkflowTaskRunId

    @ParentWorkflowTaskRunId.setter
    def ParentWorkflowTaskRunId(self, ParentWorkflowTaskRunId):
        self._ParentWorkflowTaskRunId = ParentWorkflowTaskRunId

    @property
    def ParentWorkflowTaskRunName(self):
        r"""<p>父工作流任务运行名称 【由嵌套工作流触发独有】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentWorkflowTaskRunName

    @ParentWorkflowTaskRunName.setter
    def ParentWorkflowTaskRunName(self, ParentWorkflowTaskRunName):
        self._ParentWorkflowTaskRunName = ParentWorkflowTaskRunName

    @property
    def Permission(self):
        r"""<p>授权权限类型<br>PERMISSION_TYPE_UNSPECIFIED：未指定权限<br>MANAGE : 管理权限：包含所有操作权限<br>RUN : 运行权限：可执行实体<br>VIEW : 查看权限：可查看实体内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def AdvancedParameters(self):
        r"""<p>工作流高级运行时用户填入的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvancedParameter
        """
        return self._AdvancedParameters

    @AdvancedParameters.setter
    def AdvancedParameters(self, AdvancedParameters):
        self._AdvancedParameters = AdvancedParameters

    @property
    def ScheduledTime(self):
        r"""<p>计划调度时间</p><p>参数格式：毫秒时间戳（UTC）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduledTime

    @ScheduledTime.setter
    def ScheduledTime(self, ScheduledTime):
        self._ScheduledTime = ScheduledTime


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._TriggerType = params.get("TriggerType")
        self._RunStartTime = params.get("RunStartTime")
        self._PendingStartTime = params.get("PendingStartTime")
        self._QueueStartTime = params.get("QueueStartTime")
        self._RunEndTime = params.get("RunEndTime")
        self._EndTime = params.get("EndTime")
        self._RunCostTime = params.get("RunCostTime")
        self._QueueCostTime = params.get("QueueCostTime")
        self._PendingCostTime = params.get("PendingCostTime")
        self._RunState = params.get("RunState")
        self._ResourceGroupIds = params.get("ResourceGroupIds")
        self._RunUserUin = params.get("RunUserUin")
        self._RunUserName = params.get("RunUserName")
        self._ErrorCodeString = params.get("ErrorCodeString")
        self._WorkflowParams = params.get("WorkflowParams")
        self._WorkflowVersionId = params.get("WorkflowVersionId")
        self._SupportRerun = params.get("SupportRerun")
        self._CreateTime = params.get("CreateTime")
        self._RerunTimes = params.get("RerunTimes")
        self._SelectedTaskIds = params.get("SelectedTaskIds")
        if params.get("ResourceGroupInfoList") is not None:
            self._ResourceGroupInfoList = []
            for item in params.get("ResourceGroupInfoList"):
                obj = ResourceGroupInfo()
                obj._deserialize(item)
                self._ResourceGroupInfoList.append(obj)
        if params.get("LabelList") is not None:
            self._LabelList = []
            for item in params.get("LabelList"):
                obj = LabelBrief()
                obj._deserialize(item)
                self._LabelList.append(obj)
        self._ParentWorkflowRunId = params.get("ParentWorkflowRunId")
        self._ParentWorkflowTaskRunId = params.get("ParentWorkflowTaskRunId")
        self._ParentWorkflowTaskRunName = params.get("ParentWorkflowTaskRunName")
        self._Permission = params.get("Permission")
        if params.get("AdvancedParameters") is not None:
            self._AdvancedParameters = []
            for item in params.get("AdvancedParameters"):
                obj = AdvancedParameter()
                obj._deserialize(item)
                self._AdvancedParameters.append(obj)
        self._ScheduledTime = params.get("ScheduledTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRunBrief(AbstractModel):
    r"""工作流列表项的运行情况

    """

    def __init__(self):
        r"""
        :param _WorkflowRunId: 工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _RunStartTime: 运行开始时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _RunState: <p>运行状态。CREATE(&quot;初始化&quot;),     QUEUED(&quot;等待中&quot;),     PENDING(&quot;准备中&quot;),     RUNNING(&quot;运行中&quot;),     SKIPPED(&quot;跳过运行&quot;),     SUCCESS(&quot;成功&quot;),     FAILED(&quot;失败&quot;),     TERMINATING(&quot;终止中&quot;),     TERMINATED(&quot;终止&quot;),     CANCELLED(&quot;被手动终止&quot;)等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _ErrorCodeString: 运行错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        """
        self._WorkflowRunId = None
        self._RunStartTime = None
        self._RunState = None
        self._ErrorCodeString = None

    @property
    def WorkflowRunId(self):
        r"""工作流运行ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def RunStartTime(self):
        r"""运行开始时间，单位：毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def RunState(self):
        r"""<p>运行状态。CREATE(&quot;初始化&quot;),     QUEUED(&quot;等待中&quot;),     PENDING(&quot;准备中&quot;),     RUNNING(&quot;运行中&quot;),     SKIPPED(&quot;跳过运行&quot;),     SUCCESS(&quot;成功&quot;),     FAILED(&quot;失败&quot;),     TERMINATING(&quot;终止中&quot;),     TERMINATED(&quot;终止&quot;),     CANCELLED(&quot;被手动终止&quot;)等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def ErrorCodeString(self):
        r"""运行错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString


    def _deserialize(self, params):
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._RunStartTime = params.get("RunStartTime")
        self._RunState = params.get("RunState")
        self._ErrorCodeString = params.get("ErrorCodeString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTask(AbstractModel):
    r"""工作流任务信息。 注意：本结构同时用于入参（CreateWorkflow / UpdateWorkflow）与出参（GetWorkflow）， 其中 CreateTime / UpdateTime / CreateUserUin 为系统生成字段，仅在出参中有值， 入参传值不生效（服务端忽略且不报错）。

    """

    def __init__(self):
        r"""
        :param _ParamList: 任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamList: list of ParamInfo
        :param _DependOnList: 任务依赖
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnList: list of DependOnBrief
        :param _TaskId: 任务ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: :class:`tencentcloud.databuddy.v20260715.models.TaskType`
        :param _ResourceGroupId: 资源组ID，可通过资源组相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _Description: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Alarm: 任务告警
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarm: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        :param _MonitorMetric: 监控指标
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorMetric: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        :param _TaskRetryStrategy: 任务重试策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRetryStrategy: :class:`tencentcloud.databuddy.v20260715.models.TaskRetryStrategy`
        :param _DependOnRunCondition: <p>任依赖运行条件</p><ul><li>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功</li><li>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功</li><li>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中</li><li>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败</li><li>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败</li><li>ALL_FAILED: 全部失败：所有上游依赖任务都失败</li><li>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行</li><li>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行</li><li>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游</li><li>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行</li><li>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行</li><li>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行</li><li>ADVANCED:运行条件为高级模式时配置</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnRunCondition: str
        :param _LeftCoordinate: 任务X坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftCoordinate: float
        :param _TopCoordinate: 任务Y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type TopCoordinate: float
        :param _AdvancedDependencyConfig: <p>任务高级运行参数，当DependOnRunCondition为ADVANCED时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedDependencyConfig: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        :param _InnerTask: <p>内嵌任务（FOR_EACH任务的子任务）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTask: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTask`
        :param _CreateTime: 创建时间，单位：毫秒时间戳。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，单位：毫秒时间戳。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _CreateUserUin: 创建人UIN。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        """
        self._ParamList = None
        self._DependOnList = None
        self._TaskId = None
        self._TaskName = None
        self._TaskType = None
        self._ResourceGroupId = None
        self._Description = None
        self._Alarm = None
        self._MonitorMetric = None
        self._TaskRetryStrategy = None
        self._DependOnRunCondition = None
        self._LeftCoordinate = None
        self._TopCoordinate = None
        self._AdvancedDependencyConfig = None
        self._InnerTask = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CreateUserUin = None

    @property
    def ParamList(self):
        r"""任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def DependOnList(self):
        r"""任务依赖
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DependOnBrief
        """
        return self._DependOnList

    @DependOnList.setter
    def DependOnList(self, DependOnList):
        self._DependOnList = DependOnList

    @property
    def TaskId(self):
        r"""任务ID，创建时无需传入，由服务端生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        r"""任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.TaskType`
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ResourceGroupId(self):
        r"""资源组ID，可通过资源组相关接口获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Description(self):
        r"""任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Alarm(self):
        r"""任务告警
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AlarmBrief`
        """
        return self._Alarm

    @Alarm.setter
    def Alarm(self, Alarm):
        self._Alarm = Alarm

    @property
    def MonitorMetric(self):
        r"""监控指标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.MonitorMetricBrief`
        """
        return self._MonitorMetric

    @MonitorMetric.setter
    def MonitorMetric(self, MonitorMetric):
        self._MonitorMetric = MonitorMetric

    @property
    def TaskRetryStrategy(self):
        r"""任务重试策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.TaskRetryStrategy`
        """
        return self._TaskRetryStrategy

    @TaskRetryStrategy.setter
    def TaskRetryStrategy(self, TaskRetryStrategy):
        self._TaskRetryStrategy = TaskRetryStrategy

    @property
    def DependOnRunCondition(self):
        r"""<p>任依赖运行条件</p><ul><li>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功</li><li>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功</li><li>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中</li><li>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败</li><li>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败</li><li>ALL_FAILED: 全部失败：所有上游依赖任务都失败</li><li>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行</li><li>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行</li><li>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游</li><li>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行</li><li>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行</li><li>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行</li><li>ADVANCED:运行条件为高级模式时配置</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependOnRunCondition

    @DependOnRunCondition.setter
    def DependOnRunCondition(self, DependOnRunCondition):
        self._DependOnRunCondition = DependOnRunCondition

    @property
    def LeftCoordinate(self):
        r"""任务X坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._LeftCoordinate

    @LeftCoordinate.setter
    def LeftCoordinate(self, LeftCoordinate):
        self._LeftCoordinate = LeftCoordinate

    @property
    def TopCoordinate(self):
        r"""任务Y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TopCoordinate

    @TopCoordinate.setter
    def TopCoordinate(self, TopCoordinate):
        self._TopCoordinate = TopCoordinate

    @property
    def AdvancedDependencyConfig(self):
        r"""<p>任务高级运行参数，当DependOnRunCondition为ADVANCED时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        """
        return self._AdvancedDependencyConfig

    @AdvancedDependencyConfig.setter
    def AdvancedDependencyConfig(self, AdvancedDependencyConfig):
        self._AdvancedDependencyConfig = AdvancedDependencyConfig

    @property
    def InnerTask(self):
        r"""<p>内嵌任务（FOR_EACH任务的子任务）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTask`
        """
        return self._InnerTask

    @InnerTask.setter
    def InnerTask(self, InnerTask):
        self._InnerTask = InnerTask

    @property
    def CreateTime(self):
        r"""创建时间，单位：毫秒时间戳。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，单位：毫秒时间戳。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateUserUin(self):
        r"""创建人UIN。出参专用，系统生成，入参传值不生效
【已废弃】服务端忽略传入值，不报错。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        if params.get("DependOnList") is not None:
            self._DependOnList = []
            for item in params.get("DependOnList"):
                obj = DependOnBrief()
                obj._deserialize(item)
                self._DependOnList.append(obj)
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        if params.get("TaskType") is not None:
            self._TaskType = TaskType()
            self._TaskType._deserialize(params.get("TaskType"))
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._Description = params.get("Description")
        if params.get("Alarm") is not None:
            self._Alarm = AlarmBrief()
            self._Alarm._deserialize(params.get("Alarm"))
        if params.get("MonitorMetric") is not None:
            self._MonitorMetric = MonitorMetricBrief()
            self._MonitorMetric._deserialize(params.get("MonitorMetric"))
        if params.get("TaskRetryStrategy") is not None:
            self._TaskRetryStrategy = TaskRetryStrategy()
            self._TaskRetryStrategy._deserialize(params.get("TaskRetryStrategy"))
        self._DependOnRunCondition = params.get("DependOnRunCondition")
        self._LeftCoordinate = params.get("LeftCoordinate")
        self._TopCoordinate = params.get("TopCoordinate")
        if params.get("AdvancedDependencyConfig") is not None:
            self._AdvancedDependencyConfig = AdvancedDependencyConfig()
            self._AdvancedDependencyConfig._deserialize(params.get("AdvancedDependencyConfig"))
        if params.get("InnerTask") is not None:
            self._InnerTask = WorkflowTask()
            self._InnerTask._deserialize(params.get("InnerTask"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTaskNodeBrief(AbstractModel):
    r"""工作流列表项中的工作流任务节点简要信息

    """

    def __init__(self):
        r"""
        :param _WorkflowId: <p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _TaskId: <p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: <p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _TaskTypeName: <p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param _DependOnList: <p>任务依赖列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnList: list of DependOnBrief
        :param _ResourceGroupId: <p>任务资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceGroupName: <p>任务资源组名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _LeftCoordinate: <p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftCoordinate: float
        :param _TopCoordinate: <p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TopCoordinate: float
        :param _TaskRetryStrategy: <p>任务重试策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRetryStrategy: :class:`tencentcloud.databuddy.v20260715.models.TaskRetryStrategy`
        :param _DependOnRunCondition: <p>任务依赖运行条件</p><p>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功<br>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功<br>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中<br>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败<br>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败<br>ALL_FAILED: 全部失败：所有上游依赖任务都失败<br>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行<br>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游<br>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行<br>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行<br>ADVANCED:运行条件为高级模式时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnRunCondition: str
        :param _AdvancedDependencyConfig: <p>高级依赖配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedDependencyConfig: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        :param _InnerTask: <p>内嵌工作流任务节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTask: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTaskNodeBrief`
        """
        self._WorkflowId = None
        self._TaskId = None
        self._TaskName = None
        self._TaskTypeName = None
        self._DependOnList = None
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._LeftCoordinate = None
        self._TopCoordinate = None
        self._TaskRetryStrategy = None
        self._DependOnRunCondition = None
        self._AdvancedDependencyConfig = None
        self._InnerTask = None

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""<p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeName(self):
        r"""<p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def DependOnList(self):
        r"""<p>任务依赖列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DependOnBrief
        """
        return self._DependOnList

    @DependOnList.setter
    def DependOnList(self, DependOnList):
        self._DependOnList = DependOnList

    @property
    def ResourceGroupId(self):
        r"""<p>任务资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        r"""<p>任务资源组名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def LeftCoordinate(self):
        r"""<p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._LeftCoordinate

    @LeftCoordinate.setter
    def LeftCoordinate(self, LeftCoordinate):
        self._LeftCoordinate = LeftCoordinate

    @property
    def TopCoordinate(self):
        r"""<p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TopCoordinate

    @TopCoordinate.setter
    def TopCoordinate(self, TopCoordinate):
        self._TopCoordinate = TopCoordinate

    @property
    def TaskRetryStrategy(self):
        r"""<p>任务重试策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.TaskRetryStrategy`
        """
        return self._TaskRetryStrategy

    @TaskRetryStrategy.setter
    def TaskRetryStrategy(self, TaskRetryStrategy):
        self._TaskRetryStrategy = TaskRetryStrategy

    @property
    def DependOnRunCondition(self):
        r"""<p>任务依赖运行条件</p><p>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功<br>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功<br>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中<br>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败<br>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败<br>ALL_FAILED: 全部失败：所有上游依赖任务都失败<br>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行<br>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游<br>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行<br>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行<br>ADVANCED:运行条件为高级模式时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependOnRunCondition

    @DependOnRunCondition.setter
    def DependOnRunCondition(self, DependOnRunCondition):
        self._DependOnRunCondition = DependOnRunCondition

    @property
    def AdvancedDependencyConfig(self):
        r"""<p>高级依赖配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        """
        return self._AdvancedDependencyConfig

    @AdvancedDependencyConfig.setter
    def AdvancedDependencyConfig(self, AdvancedDependencyConfig):
        self._AdvancedDependencyConfig = AdvancedDependencyConfig

    @property
    def InnerTask(self):
        r"""<p>内嵌工作流任务节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTaskNodeBrief`
        """
        return self._InnerTask

    @InnerTask.setter
    def InnerTask(self, InnerTask):
        self._InnerTask = InnerTask


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskTypeName = params.get("TaskTypeName")
        if params.get("DependOnList") is not None:
            self._DependOnList = []
            for item in params.get("DependOnList"):
                obj = DependOnBrief()
                obj._deserialize(item)
                self._DependOnList.append(obj)
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._LeftCoordinate = params.get("LeftCoordinate")
        self._TopCoordinate = params.get("TopCoordinate")
        if params.get("TaskRetryStrategy") is not None:
            self._TaskRetryStrategy = TaskRetryStrategy()
            self._TaskRetryStrategy._deserialize(params.get("TaskRetryStrategy"))
        self._DependOnRunCondition = params.get("DependOnRunCondition")
        if params.get("AdvancedDependencyConfig") is not None:
            self._AdvancedDependencyConfig = AdvancedDependencyConfig()
            self._AdvancedDependencyConfig._deserialize(params.get("AdvancedDependencyConfig"))
        if params.get("InnerTask") is not None:
            self._InnerTask = WorkflowTaskNodeBrief()
            self._InnerTask._deserialize(params.get("InnerTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTaskRun(AbstractModel):
    r"""工作流任务运行信息

    """

    def __init__(self):
        r"""
        :param _TaskName: <p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _WorkflowTaskRunId: <p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTaskRunId: str
        :param _RunState: <p>运行状态。如CREATE("初始化"), QUEUED("等待中"), PENDING("准备中"), RUNNING("运行中"), SKIPPED("跳过运行"), SUCCESS("成功"), FAILED("失败"), TERMINATING("终止中"), TERMINATED("终止"), CANCELLED("被手动终止")等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunState: str
        :param _WorkspaceId: <p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _WorkflowId: <p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowRunId: <p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowRunId: str
        :param _TaskId: <p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskTypeName: <p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param _TaskVersionId: <p>任务版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskVersionId: str
        :param _TriggerType: <p>触发类型</p><p>枚举值：</p><ul><li>Manual： 手动触发</li><li>Scheduler： 调度触发</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param _ResourceGroupId: <p>所属资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ErrorCodeString: <p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeString: str
        :param _RunUserUin: <p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserUin: str
        :param _RunUserName: <p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunUserName: str
        :param _CreateUserUin: <p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _JobId: <p>执行平台执行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _CreateTime: <p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _DependenceFinishedTime: <p>依赖任务完成时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependenceFinishedTime: str
        :param _RunStartTime: <p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunStartTime: str
        :param _RunEndTime: <p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunEndTime: str
        :param _RunCostTime: <p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunCostTime: str
        :param _WaitTime: <p>等待时长（依赖就绪到开始运行的等待耗时），单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WaitTime: str
        :param _IssueTime: <p>下发执行平台时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueTime: str
        :param _TimeZone: <p>时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeZone: str
        :param _DependOnList: <p>依赖上游任务ID列表。保留字段，暂时返回为[]</p><p>保留字段，暂时返回为[]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnList: list of str
        :param _RunParams: <p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunParams: str
        :param _TaskTypeExtensions: <p>任务扩展信息，包含脚本路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeExtensions: str
        :param _LeftCoordinate: <p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftCoordinate: float
        :param _TopCoordinate: <p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TopCoordinate: float
        :param _RetryTimes: <p>重试次数，为 0 则表示首次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryTimes: int
        :param _WorkflowName: <p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _RerunTimes: <p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RerunTimes: int
        :param _IsLatestRun: <p>是否最新一次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLatestRun: bool
        :param _ResourceGroupInfoList: <p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupInfoList: list of ResourceGroupInfo
        :param _RunResult: <p>运行结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunResult: str
        :param _DependOnRunCondition: <p>任务依赖运行条件</p><p>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功<br>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功<br>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中<br>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败<br>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败<br>ALL_FAILED: 全部失败：所有上游依赖任务都失败<br>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行<br>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游<br>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行<br>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行<br>ADVANCED:运行条件为高级模式时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DependOnRunCondition: str
        :param _AdvancedDependencyConfig: <p>高级依赖配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedDependencyConfig: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        :param _InnerTask: <p>内嵌工作流任务信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerTask: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskBrief`
        :param _ScheduledTime: <p>计划调度时间</p><p>参数格式：毫秒时间戳，UTC</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTime: str
        """
        self._TaskName = None
        self._WorkflowTaskRunId = None
        self._RunState = None
        self._WorkspaceId = None
        self._WorkflowId = None
        self._WorkflowRunId = None
        self._TaskId = None
        self._TaskTypeName = None
        self._TaskVersionId = None
        self._TriggerType = None
        self._ResourceGroupId = None
        self._ErrorCodeString = None
        self._RunUserUin = None
        self._RunUserName = None
        self._CreateUserUin = None
        self._JobId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DependenceFinishedTime = None
        self._RunStartTime = None
        self._RunEndTime = None
        self._RunCostTime = None
        self._WaitTime = None
        self._IssueTime = None
        self._TimeZone = None
        self._DependOnList = None
        self._RunParams = None
        self._TaskTypeExtensions = None
        self._LeftCoordinate = None
        self._TopCoordinate = None
        self._RetryTimes = None
        self._WorkflowName = None
        self._RerunTimes = None
        self._IsLatestRun = None
        self._ResourceGroupInfoList = None
        self._RunResult = None
        self._DependOnRunCondition = None
        self._AdvancedDependencyConfig = None
        self._InnerTask = None
        self._ScheduledTime = None

    @property
    def TaskName(self):
        r"""<p>任务名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowTaskRunId(self):
        r"""<p>任务运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowTaskRunId

    @WorkflowTaskRunId.setter
    def WorkflowTaskRunId(self, WorkflowTaskRunId):
        self._WorkflowTaskRunId = WorkflowTaskRunId

    @property
    def RunState(self):
        r"""<p>运行状态。如CREATE("初始化"), QUEUED("等待中"), PENDING("准备中"), RUNNING("运行中"), SKIPPED("跳过运行"), SUCCESS("成功"), FAILED("失败"), TERMINATING("终止中"), TERMINATED("终止"), CANCELLED("被手动终止")等</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunState

    @RunState.setter
    def RunState(self, RunState):
        self._RunState = RunState

    @property
    def WorkspaceId(self):
        r"""<p>工作空间ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTypeName(self):
        r"""<p>任务类型名称，请参考数据结构TaskType中TaskTypeName字段描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def TaskVersionId(self):
        r"""<p>任务版本ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskVersionId

    @TaskVersionId.setter
    def TaskVersionId(self, TaskVersionId):
        self._TaskVersionId = TaskVersionId

    @property
    def TriggerType(self):
        r"""<p>触发类型</p><p>枚举值：</p><ul><li>Manual： 手动触发</li><li>Scheduler： 调度触发</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ResourceGroupId(self):
        r"""<p>所属资源组ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ErrorCodeString(self):
        r"""<p>错误码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeString

    @ErrorCodeString.setter
    def ErrorCodeString(self, ErrorCodeString):
        self._ErrorCodeString = ErrorCodeString

    @property
    def RunUserUin(self):
        r"""<p>运行用户UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserUin

    @RunUserUin.setter
    def RunUserUin(self, RunUserUin):
        self._RunUserUin = RunUserUin

    @property
    def RunUserName(self):
        r"""<p>运行用户名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunUserName

    @RunUserName.setter
    def RunUserName(self, RunUserName):
        self._RunUserName = RunUserName

    @property
    def CreateUserUin(self):
        r"""<p>创建人UIN</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def JobId(self):
        r"""<p>执行平台执行ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CreateTime(self):
        r"""<p>创建时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DependenceFinishedTime(self):
        r"""<p>依赖任务完成时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependenceFinishedTime

    @DependenceFinishedTime.setter
    def DependenceFinishedTime(self, DependenceFinishedTime):
        self._DependenceFinishedTime = DependenceFinishedTime

    @property
    def RunStartTime(self):
        r"""<p>运行开始时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunStartTime

    @RunStartTime.setter
    def RunStartTime(self, RunStartTime):
        self._RunStartTime = RunStartTime

    @property
    def RunEndTime(self):
        r"""<p>运行结束时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def RunCostTime(self):
        r"""<p>运行时长，单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunCostTime

    @RunCostTime.setter
    def RunCostTime(self, RunCostTime):
        self._RunCostTime = RunCostTime

    @property
    def WaitTime(self):
        r"""<p>等待时长（依赖就绪到开始运行的等待耗时），单位：秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaitTime

    @WaitTime.setter
    def WaitTime(self, WaitTime):
        self._WaitTime = WaitTime

    @property
    def IssueTime(self):
        r"""<p>下发执行平台时间，单位：毫秒时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime

    @property
    def TimeZone(self):
        r"""<p>时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DependOnList(self):
        r"""<p>依赖上游任务ID列表。保留字段，暂时返回为[]</p><p>保留字段，暂时返回为[]</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DependOnList

    @DependOnList.setter
    def DependOnList(self, DependOnList):
        self._DependOnList = DependOnList

    @property
    def RunParams(self):
        r"""<p>运行参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunParams

    @RunParams.setter
    def RunParams(self, RunParams):
        self._RunParams = RunParams

    @property
    def TaskTypeExtensions(self):
        r"""<p>任务扩展信息，包含脚本路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeExtensions

    @TaskTypeExtensions.setter
    def TaskTypeExtensions(self, TaskTypeExtensions):
        self._TaskTypeExtensions = TaskTypeExtensions

    @property
    def LeftCoordinate(self):
        r"""<p>任务X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._LeftCoordinate

    @LeftCoordinate.setter
    def LeftCoordinate(self, LeftCoordinate):
        self._LeftCoordinate = LeftCoordinate

    @property
    def TopCoordinate(self):
        r"""<p>任务Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TopCoordinate

    @TopCoordinate.setter
    def TopCoordinate(self, TopCoordinate):
        self._TopCoordinate = TopCoordinate

    @property
    def RetryTimes(self):
        r"""<p>重试次数，为 0 则表示首次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def WorkflowName(self):
        r"""<p>工作流名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def RerunTimes(self):
        r"""<p>重跑次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RerunTimes

    @RerunTimes.setter
    def RerunTimes(self, RerunTimes):
        self._RerunTimes = RerunTimes

    @property
    def IsLatestRun(self):
        r"""<p>是否最新一次运行</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLatestRun

    @IsLatestRun.setter
    def IsLatestRun(self, IsLatestRun):
        self._IsLatestRun = IsLatestRun

    @property
    def ResourceGroupInfoList(self):
        r"""<p>资源组信息列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceGroupInfo
        """
        return self._ResourceGroupInfoList

    @ResourceGroupInfoList.setter
    def ResourceGroupInfoList(self, ResourceGroupInfoList):
        self._ResourceGroupInfoList = ResourceGroupInfoList

    @property
    def RunResult(self):
        r"""<p>运行结果</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunResult

    @RunResult.setter
    def RunResult(self, RunResult):
        self._RunResult = RunResult

    @property
    def DependOnRunCondition(self):
        r"""<p>任务依赖运行条件</p><p>ALL_SUCCESS: 全部成功：所有上游依赖任务均已执行并成功<br>ONE_SUCCESS: 至少一个成功：至少有一个上游依赖任务成功<br>NONE_FAILED: 目前没有失败：没有依赖任务失败，并且至少有一个依赖任务在运行中<br>ALL_DONE: 全部完成：所有上游依赖任务均已执行并完成（无论成功或失败<br>ONE_FAILED: 至少一个失败：至少有一个上游依赖任务失败<br>ALL_FAILED: 全部失败：所有上游依赖任务都失败<br>ALL_DONE_AT_LEAST_ONE_SUCCESS：上游全部完成至少一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个成功，则依赖判断成功，否则就是跳过运行<br>ALL_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ONE_DONE：至少一个完成：上游只要有一个完成了，就进行依赖判断，且依赖判断成功，否则还是等待上游<br>ALL_DONE_NONE_FAILED_AT_LEAST_ONE_SUCCESS：上游全部完成，没有失败，至少有一个成功: 所有上游依赖任务都达到终态时，进行依赖判断，上游没有一个失败且至少有一个成功的情况下，依赖判断成功，否则就是跳过运行<br>NONE_SKIPPED：上游全部完成，没有跳过运行: 所有上游依赖任务都达到终态时，进行依赖判断, 如果上游状态全部都是成功、失败、上游失败状态，则依赖判断成功，否则为跳过运行<br>ALL_DONE_AT_LEAST_ONE_FAILED：上游全部完成至少一个失败: 所有上游依赖任务都达到终态时，进行依赖判断，至少有一个失败，则依赖判断成功，否则就是跳过运行<br>ADVANCED:运行条件为高级模式时配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependOnRunCondition

    @DependOnRunCondition.setter
    def DependOnRunCondition(self, DependOnRunCondition):
        self._DependOnRunCondition = DependOnRunCondition

    @property
    def AdvancedDependencyConfig(self):
        r"""<p>高级依赖配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AdvancedDependencyConfig`
        """
        return self._AdvancedDependencyConfig

    @AdvancedDependencyConfig.setter
    def AdvancedDependencyConfig(self, AdvancedDependencyConfig):
        self._AdvancedDependencyConfig = AdvancedDependencyConfig

    @property
    def InnerTask(self):
        r"""<p>内嵌工作流任务信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.InnerWorkflowTaskBrief`
        """
        return self._InnerTask

    @InnerTask.setter
    def InnerTask(self, InnerTask):
        self._InnerTask = InnerTask

    @property
    def ScheduledTime(self):
        r"""<p>计划调度时间</p><p>参数格式：毫秒时间戳，UTC</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduledTime

    @ScheduledTime.setter
    def ScheduledTime(self, ScheduledTime):
        self._ScheduledTime = ScheduledTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._WorkflowTaskRunId = params.get("WorkflowTaskRunId")
        self._RunState = params.get("RunState")
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._TaskId = params.get("TaskId")
        self._TaskTypeName = params.get("TaskTypeName")
        self._TaskVersionId = params.get("TaskVersionId")
        self._TriggerType = params.get("TriggerType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ErrorCodeString = params.get("ErrorCodeString")
        self._RunUserUin = params.get("RunUserUin")
        self._RunUserName = params.get("RunUserName")
        self._CreateUserUin = params.get("CreateUserUin")
        self._JobId = params.get("JobId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DependenceFinishedTime = params.get("DependenceFinishedTime")
        self._RunStartTime = params.get("RunStartTime")
        self._RunEndTime = params.get("RunEndTime")
        self._RunCostTime = params.get("RunCostTime")
        self._WaitTime = params.get("WaitTime")
        self._IssueTime = params.get("IssueTime")
        self._TimeZone = params.get("TimeZone")
        self._DependOnList = params.get("DependOnList")
        self._RunParams = params.get("RunParams")
        self._TaskTypeExtensions = params.get("TaskTypeExtensions")
        self._LeftCoordinate = params.get("LeftCoordinate")
        self._TopCoordinate = params.get("TopCoordinate")
        self._RetryTimes = params.get("RetryTimes")
        self._WorkflowName = params.get("WorkflowName")
        self._RerunTimes = params.get("RerunTimes")
        self._IsLatestRun = params.get("IsLatestRun")
        if params.get("ResourceGroupInfoList") is not None:
            self._ResourceGroupInfoList = []
            for item in params.get("ResourceGroupInfoList"):
                obj = ResourceGroupInfo()
                obj._deserialize(item)
                self._ResourceGroupInfoList.append(obj)
        self._RunResult = params.get("RunResult")
        self._DependOnRunCondition = params.get("DependOnRunCondition")
        if params.get("AdvancedDependencyConfig") is not None:
            self._AdvancedDependencyConfig = AdvancedDependencyConfig()
            self._AdvancedDependencyConfig._deserialize(params.get("AdvancedDependencyConfig"))
        if params.get("InnerTask") is not None:
            self._InnerTask = InnerWorkflowTaskBrief()
            self._InnerTask._deserialize(params.get("InnerTask"))
        self._ScheduledTime = params.get("ScheduledTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTriggerAdvancedConfiguration(AbstractModel):
    r"""工作流调度高级配置。

    """

    def __init__(self):
        r"""
        :param _TaskRetryMode: <p>&lt;p&gt;该工作流下的所有任务重试模式，仅当TriggerMode为CONTINUE_RUN时有效。</p><p>枚举值：</p><ul><li>onFailure： 失败时自动重试</li><li>never： 从不重试</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRetryMode: str
        """
        self._TaskRetryMode = None

    @property
    def TaskRetryMode(self):
        r"""<p>&lt;p&gt;该工作流下的所有任务重试模式，仅当TriggerMode为CONTINUE_RUN时有效。</p><p>枚举值：</p><ul><li>onFailure： 失败时自动重试</li><li>never： 从不重试</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskRetryMode

    @TaskRetryMode.setter
    def TaskRetryMode(self, TaskRetryMode):
        self._TaskRetryMode = TaskRetryMode


    def _deserialize(self, params):
        self._TaskRetryMode = params.get("TaskRetryMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTriggerConfiguration(AbstractModel):
    r"""工作流调度配置。

    """

    def __init__(self):
        r"""
        :param _TriggerId: <p>调度配置ID，创建时无需传入，由服务端生成</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerId: str
        :param _SchedulerStatus: <p>调度状态 启动：START，暂停：PAUSE</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerStatus: str
        :param _TriggerMode: <p>触发方式，</p><ul><li>定时触发：TIME_TRIGGER</li><li>持续运行：CONTINUE_RUN</li></ul><p>注意：</p><ul><li>TIME_TRIGGER 模式下，SchedulerStatus、SchedulerTimeZone、StartTime、EndTime、ConfigMode、CycleType、CrontabExpression 必填；</li><li>CONTINUE_RUN 模式下，AdvancedConfig必填；</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerMode: str
        :param _SchedulerTimeZone: <p>调度时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerTimeZone: str
        :param _StartTime: <p>调度生效时间，单位：毫秒时间戳。必须小于 EndTime</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: <p>调度结束时间，单位：毫秒时间戳。必须大于 StartTime</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ConfigMode: <p>配置方式，常规：COMMON，CRON表达式：CRON_EXPRESSION</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigMode: str
        :param _CycleType: <p>周期类型：支持的类型为 ONEOFF_CYCLE: 一次性 YEAR_CYCLE: 年 MONTH_CYCLE: 月 WEEK_CYCLE: 周 DAY_CYCLE: 天<br>HOUR_CYCLE: 小时 MINUTE_CYCLE: 分钟 CRONTAB_CYCLE: crontab表达式类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _CrontabExpression: <p>cron表达式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        :param _ExtraInfo: <p>Json格式，对账使用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: str
        :param _AdvancedConfig: <p>高级配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedConfig: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTriggerAdvancedConfiguration`
        """
        self._TriggerId = None
        self._SchedulerStatus = None
        self._TriggerMode = None
        self._SchedulerTimeZone = None
        self._StartTime = None
        self._EndTime = None
        self._ConfigMode = None
        self._CycleType = None
        self._CrontabExpression = None
        self._ExtraInfo = None
        self._AdvancedConfig = None

    @property
    def TriggerId(self):
        r"""<p>调度配置ID，创建时无需传入，由服务端生成</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def SchedulerStatus(self):
        r"""<p>调度状态 启动：START，暂停：PAUSE</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchedulerStatus

    @SchedulerStatus.setter
    def SchedulerStatus(self, SchedulerStatus):
        self._SchedulerStatus = SchedulerStatus

    @property
    def TriggerMode(self):
        r"""<p>触发方式，</p><ul><li>定时触发：TIME_TRIGGER</li><li>持续运行：CONTINUE_RUN</li></ul><p>注意：</p><ul><li>TIME_TRIGGER 模式下，SchedulerStatus、SchedulerTimeZone、StartTime、EndTime、ConfigMode、CycleType、CrontabExpression 必填；</li><li>CONTINUE_RUN 模式下，AdvancedConfig必填；</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def SchedulerTimeZone(self):
        r"""<p>调度时区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchedulerTimeZone

    @SchedulerTimeZone.setter
    def SchedulerTimeZone(self, SchedulerTimeZone):
        self._SchedulerTimeZone = SchedulerTimeZone

    @property
    def StartTime(self):
        r"""<p>调度生效时间，单位：毫秒时间戳。必须小于 EndTime</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>调度结束时间，单位：毫秒时间戳。必须大于 StartTime</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ConfigMode(self):
        r"""<p>配置方式，常规：COMMON，CRON表达式：CRON_EXPRESSION</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigMode

    @ConfigMode.setter
    def ConfigMode(self, ConfigMode):
        self._ConfigMode = ConfigMode

    @property
    def CycleType(self):
        r"""<p>周期类型：支持的类型为 ONEOFF_CYCLE: 一次性 YEAR_CYCLE: 年 MONTH_CYCLE: 月 WEEK_CYCLE: 周 DAY_CYCLE: 天<br>HOUR_CYCLE: 小时 MINUTE_CYCLE: 分钟 CRONTAB_CYCLE: crontab表达式类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def CrontabExpression(self):
        r"""<p>cron表达式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def ExtraInfo(self):
        r"""<p>Json格式，对账使用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def AdvancedConfig(self):
        r"""<p>高级配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.WorkflowTriggerAdvancedConfiguration`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._TriggerId = params.get("TriggerId")
        self._SchedulerStatus = params.get("SchedulerStatus")
        self._TriggerMode = params.get("TriggerMode")
        self._SchedulerTimeZone = params.get("SchedulerTimeZone")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ConfigMode = params.get("ConfigMode")
        self._CycleType = params.get("CycleType")
        self._CrontabExpression = params.get("CrontabExpression")
        self._ExtraInfo = params.get("ExtraInfo")
        if params.get("AdvancedConfig") is not None:
            self._AdvancedConfig = WorkflowTriggerAdvancedConfiguration()
            self._AdvancedConfig._deserialize(params.get("AdvancedConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfo(AbstractModel):
    r"""工作空间信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _WorkspaceName: 工作空间名称
        :type WorkspaceName: str
        :param _Description: 工作空间描述
        :type Description: str
        :param _WorkspaceRegion: 工作空间地域（如 ap-guangzhou）
        :type WorkspaceRegion: str
        :param _Status: 工作空间状态：0=未指定 1=创建中 2=创建失败 3=正常运行中 4=已删除
        :type Status: int
        :param _ErrorReason: 失败原因（Status=2 创建失败时有值）
        :type ErrorReason: str
        :param _Creator: 创建者信息
        :type Creator: :class:`tencentcloud.databuddy.v20260715.models.StandardUserInfo`
        :param _CreateTime: 创建时间，毫秒时间戳
        :type CreateTime: str
        :param _UpdateTime: 更新时间，毫秒时间戳
        :type UpdateTime: str
        :param _HasAccess: 当前用户是否拥有该工作空间的访问权限
        :type HasAccess: bool
        """
        self._WorkspaceId = None
        self._WorkspaceName = None
        self._Description = None
        self._WorkspaceRegion = None
        self._Status = None
        self._ErrorReason = None
        self._Creator = None
        self._CreateTime = None
        self._UpdateTime = None
        self._HasAccess = None

    @property
    def WorkspaceId(self):
        r"""工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkspaceName(self):
        r"""工作空间名称
        :rtype: str
        """
        return self._WorkspaceName

    @WorkspaceName.setter
    def WorkspaceName(self, WorkspaceName):
        self._WorkspaceName = WorkspaceName

    @property
    def Description(self):
        r"""工作空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkspaceRegion(self):
        r"""工作空间地域（如 ap-guangzhou）
        :rtype: str
        """
        return self._WorkspaceRegion

    @WorkspaceRegion.setter
    def WorkspaceRegion(self, WorkspaceRegion):
        self._WorkspaceRegion = WorkspaceRegion

    @property
    def Status(self):
        r"""工作空间状态：0=未指定 1=创建中 2=创建失败 3=正常运行中 4=已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorReason(self):
        r"""失败原因（Status=2 创建失败时有值）
        :rtype: str
        """
        return self._ErrorReason

    @ErrorReason.setter
    def ErrorReason(self, ErrorReason):
        self._ErrorReason = ErrorReason

    @property
    def Creator(self):
        r"""创建者信息
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.StandardUserInfo`
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        r"""创建时间，毫秒时间戳
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，毫秒时间戳
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def HasAccess(self):
        r"""当前用户是否拥有该工作空间的访问权限
        :rtype: bool
        """
        return self._HasAccess

    @HasAccess.setter
    def HasAccess(self, HasAccess):
        self._HasAccess = HasAccess


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkspaceName = params.get("WorkspaceName")
        self._Description = params.get("Description")
        self._WorkspaceRegion = params.get("WorkspaceRegion")
        self._Status = params.get("Status")
        self._ErrorReason = params.get("ErrorReason")
        if params.get("Creator") is not None:
            self._Creator = StandardUserInfo()
            self._Creator._deserialize(params.get("Creator"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._HasAccess = params.get("HasAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        