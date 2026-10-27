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


class AssociateSecurityGroupRequest(AbstractModel):
    r"""AssociateSecurityGroup请求参数结构体

    """


class AssociateSecurityGroupResponse(AbstractModel):
    r"""AssociateSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessSet: 关联成功的桌面列表
        :type SuccessSet: list of str
        :param _FailureSet: 关联失败的桌面列表
        :type FailureSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessSet = None
        self._FailureSet = None
        self._RequestId = None

    @property
    def SuccessSet(self):
        r"""关联成功的桌面列表
        :rtype: list of str
        """
        return self._SuccessSet

    @SuccessSet.setter
    def SuccessSet(self, SuccessSet):
        self._SuccessSet = SuccessSet

    @property
    def FailureSet(self):
        r"""关联失败的桌面列表
        :rtype: list of str
        """
        return self._FailureSet

    @FailureSet.setter
    def FailureSet(self, FailureSet):
        self._FailureSet = FailureSet

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
        self._SuccessSet = params.get("SuccessSet")
        self._FailureSet = params.get("FailureSet")
        self._RequestId = params.get("RequestId")


class AttributeInfo(AbstractModel):
    r"""实例属性key--value结构

    """

    def __init__(self):
        r"""
        :param _Name: <p>实例属性名</p>
        :type Name: str
        :param _Value: <p>实例属性值</p>
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""<p>实例属性名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""<p>实例属性值</p>
        :rtype: str
        """
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
        


class BindInfo(AbstractModel):
    r"""绑定关系

    """

    def __init__(self):
        r"""
        :param _UserId: <p>实例绑定的用户ID</p>
        :type UserId: str
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        """
        self._UserId = None
        self._InstanceId = None

    @property
    def UserId(self):
        r"""<p>实例绑定的用户ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindInstancesRequest(AbstractModel):
    r"""BindInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: <p>指定得到云桌面用户id</p>
        :type UserIds: list of str
        :param _InstanceIds: <p>待分配桌面实例id</p>
        :type InstanceIds: list of str
        :param _InstanceType: <p>待分配桌面类型</p>
        :type InstanceType: str
        :param _InstanceRegion: <p>待分配桌面所在区域</p>
        :type InstanceRegion: str
        """
        self._UserIds = None
        self._InstanceIds = None
        self._InstanceType = None
        self._InstanceRegion = None

    @property
    def UserIds(self):
        r"""<p>指定得到云桌面用户id</p>
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def InstanceIds(self):
        r"""<p>待分配桌面实例id</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        r"""<p>待分配桌面类型</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRegion(self):
        r"""<p>待分配桌面所在区域</p>
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._InstanceRegion = params.get("InstanceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindInstancesResponse(AbstractModel):
    r"""BindInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindInfoList: <p>待分配桌面状态</p>
        :type BindInfoList: list of BindStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindInfoList = None
        self._RequestId = None

    @property
    def BindInfoList(self):
        r"""<p>待分配桌面状态</p>
        :rtype: list of BindStatusInfo
        """
        return self._BindInfoList

    @BindInfoList.setter
    def BindInfoList(self, BindInfoList):
        self._BindInfoList = BindInfoList

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
        if params.get("BindInfoList") is not None:
            self._BindInfoList = []
            for item in params.get("BindInfoList"):
                obj = BindStatusInfo()
                obj._deserialize(item)
                self._BindInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class BindStatusInfo(AbstractModel):
    r"""桌面实例绑定状态详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>桌面实例id</p>
        :type InstanceId: str
        :param _BindStatus: <p>实例的绑定状态。取值：<br>UNBOUND - 未绑定<br>BINDING - 绑定中<br>BOUND - 绑定<br>UNBINDING-解绑中</p>
        :type BindStatus: str
        :param _UserId: <p>绑定的用户id【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _UserName: <p>绑定用户名称【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _DisplayName: <p>绑定用户显示名称【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        """
        self._InstanceId = None
        self._BindStatus = None
        self._UserId = None
        self._UserName = None
        self._DisplayName = None

    @property
    def InstanceId(self):
        r"""<p>桌面实例id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BindStatus(self):
        r"""<p>实例的绑定状态。取值：<br>UNBOUND - 未绑定<br>BINDING - 绑定中<br>BOUND - 绑定<br>UNBINDING-解绑中</p>
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def UserId(self):
        r"""<p>绑定的用户id【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""<p>绑定用户名称【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DisplayName(self):
        r"""<p>绑定用户显示名称【BOUND状态不允许为空】</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BindStatus = params.get("BindStatus")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._DisplayName = params.get("DisplayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargePrepaid(AbstractModel):
    r"""预付费模式，即包年包月相关参数。包括购买时长和自动续费逻辑等。

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        r"""购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
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
        


class CommandDetail(AbstractModel):
    r"""任务详情

    """

    def __init__(self):
        r"""
        :param _Uin: 租户 Uin
        :type Uin: str
        :param _AppId: 租户 APPID
        :type AppId: int
        :param _Type: 任务类型，取值有：
PowerShellScript
Bat
        :type Type: str
        :param _Status: RUNNING - 执行中；FINISHED - 执行完成
        :type Status: str
        :param _Command: 任务脚本，Base64 编码
        :type Command: str
        :param _CommandId: 任务唯一 ID
        :type CommandId: str
        :param _CreateTime: 任务完成时间
        :type CreateTime: str
        :param _FinishTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param _Invocations: 各实例运行结果集
        :type Invocations: list of InvocationDetail
        :param _RunAsBoundUser: 是否以绑定用户运行任务，默认 false：system 用户执行
        :type RunAsBoundUser: bool
        :param _RunForeground: 是否前台运行任务，默认 false：后台运行任务
        :type RunForeground: bool
        """
        self._Uin = None
        self._AppId = None
        self._Type = None
        self._Status = None
        self._Command = None
        self._CommandId = None
        self._CreateTime = None
        self._FinishTime = None
        self._Invocations = None
        self._RunAsBoundUser = None
        self._RunForeground = None

    @property
    def Uin(self):
        r"""租户 Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        r"""租户 APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Type(self):
        r"""任务类型，取值有：
PowerShellScript
Bat
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""RUNNING - 执行中；FINISHED - 执行完成
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Command(self):
        r"""任务脚本，Base64 编码
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandId(self):
        r"""任务唯一 ID
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CreateTime(self):
        r"""任务完成时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FinishTime(self):
        r"""任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Invocations(self):
        r"""各实例运行结果集
        :rtype: list of InvocationDetail
        """
        return self._Invocations

    @Invocations.setter
    def Invocations(self, Invocations):
        self._Invocations = Invocations

    @property
    def RunAsBoundUser(self):
        r"""是否以绑定用户运行任务，默认 false：system 用户执行
        :rtype: bool
        """
        return self._RunAsBoundUser

    @RunAsBoundUser.setter
    def RunAsBoundUser(self, RunAsBoundUser):
        self._RunAsBoundUser = RunAsBoundUser

    @property
    def RunForeground(self):
        r"""是否前台运行任务，默认 false：后台运行任务
        :rtype: bool
        """
        return self._RunForeground

    @RunForeground.setter
    def RunForeground(self, RunForeground):
        self._RunForeground = RunForeground


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Command = params.get("Command")
        self._CommandId = params.get("CommandId")
        self._CreateTime = params.get("CreateTime")
        self._FinishTime = params.get("FinishTime")
        if params.get("Invocations") is not None:
            self._Invocations = []
            for item in params.get("Invocations"):
                obj = InvocationDetail()
                obj._deserialize(item)
                self._Invocations.append(obj)
        self._RunAsBoundUser = params.get("RunAsBoundUser")
        self._RunForeground = params.get("RunForeground")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandTaskRequest(AbstractModel):
    r"""CreateCommandTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Command: 脚本任务，需要 Base64 编码
        :type Command: str
        :param _Type: 脚本任务类型：windows 桌面可选有：    PowerShellScript — powershell脚本    BatScript — Bat 脚本
        :type Type: str
        :param _InstanceIds: 执行脚本任务的实例列表
        :type InstanceIds: list of str
        :param _RunAsBoundUser: 是否以绑定用户身份执行，默认 System身份运行false： System身份运行，默认行为true：以绑定用户身份执行
        :type RunAsBoundUser: bool
        :param _RunForeground: 是否前台运行false：后台运行，默认行为true：前台运行
        :type RunForeground: bool
        """
        self._Command = None
        self._Type = None
        self._InstanceIds = None
        self._RunAsBoundUser = None
        self._RunForeground = None

    @property
    def Command(self):
        r"""脚本任务，需要 Base64 编码
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Type(self):
        r"""脚本任务类型：windows 桌面可选有：    PowerShellScript — powershell脚本    BatScript — Bat 脚本
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceIds(self):
        r"""执行脚本任务的实例列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RunAsBoundUser(self):
        r"""是否以绑定用户身份执行，默认 System身份运行false： System身份运行，默认行为true：以绑定用户身份执行
        :rtype: bool
        """
        return self._RunAsBoundUser

    @RunAsBoundUser.setter
    def RunAsBoundUser(self, RunAsBoundUser):
        self._RunAsBoundUser = RunAsBoundUser

    @property
    def RunForeground(self):
        r"""是否前台运行false：后台运行，默认行为true：前台运行
        :rtype: bool
        """
        return self._RunForeground

    @RunForeground.setter
    def RunForeground(self, RunForeground):
        self._RunForeground = RunForeground


    def _deserialize(self, params):
        self._Command = params.get("Command")
        self._Type = params.get("Type")
        self._InstanceIds = params.get("InstanceIds")
        self._RunAsBoundUser = params.get("RunAsBoundUser")
        self._RunForeground = params.get("RunForeground")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandTaskResponse(AbstractModel):
    r"""CreateCommandTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 脚本任务唯一 ID
        :type CommandId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommandId = None
        self._RequestId = None

    @property
    def CommandId(self):
        r"""脚本任务唯一 ID
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

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
        self._CommandId = params.get("CommandId")
        self._RequestId = params.get("RequestId")


class CreateDataDiskRequest(AbstractModel):
    r"""CreateDataDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _DiskType: 数据盘类型，有效值CLOUD_SSD/CLOUD_PREMIUM
        :type DiskType: str
        :param _DiskSize: 数据盘大小
        :type DiskSize: int
        :param _SnapShotId: 硬盘快照id
        :type SnapShotId: str
        """
        self._InstanceId = None
        self._DiskType = None
        self._DiskSize = None
        self._SnapShotId = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskType(self):
        r"""数据盘类型，有效值CLOUD_SSD/CLOUD_PREMIUM
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""数据盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapShotId(self):
        r"""硬盘快照id
        :rtype: str
        """
        return self._SnapShotId

    @SnapShotId.setter
    def SnapShotId(self, SnapShotId):
        self._SnapShotId = SnapShotId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._SnapShotId = params.get("SnapShotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataDiskResponse(AbstractModel):
    r"""CreateDataDisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateDomainControlPolicyRequest(AbstractModel):
    r"""CreateDomainControlPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>策略名称</p>
        :type Name: str
        :param _Description: <p>策略描述</p>
        :type Description: str
        :param _Type: <p>策略类型，取值范围[&quot;WHITE&quot;,&quot;BLACK&quot;]，WHITE - 白名单策略；BLACK - 黑名单策略；默认 值为BLACK</p>
        :type Type: str
        :param _DetailSet: <p>域名控制规则详情</p>
        :type DetailSet: list of DomainControlDetail
        :param _IpDetailSet: <p>IP控制规则详情</p>
        :type IpDetailSet: list of IpControlDetail
        :param _InstanceIds: <p>作用到的实例列表</p>
        :type InstanceIds: list of str
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._DetailSet = None
        self._IpDetailSet = None
        self._InstanceIds = None

    @property
    def Name(self):
        r"""<p>策略名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>策略描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""<p>策略类型，取值范围[&quot;WHITE&quot;,&quot;BLACK&quot;]，WHITE - 白名单策略；BLACK - 黑名单策略；默认 值为BLACK</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DetailSet(self):
        r"""<p>域名控制规则详情</p>
        :rtype: list of DomainControlDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def IpDetailSet(self):
        r"""<p>IP控制规则详情</p>
        :rtype: list of IpControlDetail
        """
        return self._IpDetailSet

    @IpDetailSet.setter
    def IpDetailSet(self, IpDetailSet):
        self._IpDetailSet = IpDetailSet

    @property
    def InstanceIds(self):
        r"""<p>作用到的实例列表</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = DomainControlDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        if params.get("IpDetailSet") is not None:
            self._IpDetailSet = []
            for item in params.get("IpDetailSet"):
                obj = IpControlDetail()
                obj._deserialize(item)
                self._IpDetailSet.append(obj)
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainControlPolicyResponse(AbstractModel):
    r"""CreateDomainControlPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: <p>策略唯一ID</p>
        :type PolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        r"""<p>策略唯一ID</p>
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    r"""CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>云桌面实例ID。</p>
        :type InstanceId: str
        :param _ImageName: <p>镜像名称。只支持中文、字母、数字或连接符号&quot;-&quot;，且最多60个字符。<br>默认值：空。</p>
        :type ImageName: str
        :param _Description: <p>镜像的描述信息。支持英文或中文字符，最多60个字符。<br>默认值：空。</p>
        :type Description: str
        :param _DataDiskIds: <p>基于实例创建整机镜像时，指定包含在镜像里的数据盘ID。</p>
        :type DataDiskIds: list of str
        """
        self._InstanceId = None
        self._ImageName = None
        self._Description = None
        self._DataDiskIds = None

    @property
    def InstanceId(self):
        r"""<p>云桌面实例ID。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageName(self):
        r"""<p>镜像名称。只支持中文、字母、数字或连接符号&quot;-&quot;，且最多60个字符。<br>默认值：空。</p>
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def Description(self):
        r"""<p>镜像的描述信息。支持英文或中文字符，最多60个字符。<br>默认值：空。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DataDiskIds(self):
        r"""<p>基于实例创建整机镜像时，指定包含在镜像里的数据盘ID。</p>
        :rtype: list of str
        """
        return self._DataDiskIds

    @DataDiskIds.setter
    def DataDiskIds(self, DataDiskIds):
        self._DataDiskIds = DataDiskIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageName = params.get("ImageName")
        self._Description = params.get("Description")
        self._DataDiskIds = params.get("DataDiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    r"""CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: <p>镜像ID。</p>
        :type ImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageId = None
        self._RequestId = None

    @property
    def ImageId(self):
        r"""<p>镜像ID。</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

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
        self._ImageId = params.get("ImageId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型。<li>  S3L.MEDIUM4: 云桌面-标准S3_2核4G </li><li> S3L.LARGE8: 云桌面-标准S3_4核8G </li><li> S3L.LARGE16: 云桌面-标准S3_4核16G </li><li> S3L.2XLARGE16: 云桌面-标准S3_8核16G </li><li> S1L.LARGE8：云桌面-标准S1_4核8G </li><li> S1L.LARGE16：标准S1_4核16G </li><li> S2L.2XLARGE16：标准S2_8核16G </li><li> G1L.LARGE16：图形G1_4核16G  </li><li> G1L.2XLARGE32：图形G1_8核32G </li><li> G1L.4XLARGE64：图形G1_16核64G </li><li> G2L.LARGE24: 云桌面-图形G2_6核24G </li><li> G2L.3XLARGE58: 云桌面-图形G2_14核58G </li><li> G2L.3XLARGE44: 云桌面-图形G2_12核44G </li><li> G3L.LARGE16: 云桌面-图形G3_4核16G </li><li> G3L.5XMEDIUM40: 云桌面-图形G3_10核40G </li><li> G3L.5XLARGE80: 云桌面-图形G3_20核80G </li><li> G4L.5XMEDIUM40: 云桌面-图形G4_10核40G </li><li> G4L.11XMEDIUM80: 云桌面-图形G4_22核80G </li><li> G4L.11XLARGE160: 云桌面-图形G4_44核160G </li><li> G5L.5XMEDIUM40: 云桌面-图形G5_10核40G </li><li> G5L.5XLARGE80: 云桌面-图形G5_22核80G </li><li> G5L.21XMEDIUM160: 云桌面-图形G5_42核160G </li><li> G5L.21XLARGE320: 云桌面-图形G5_84核320G </li>
        :type InstanceType: str
        :param _SystemDisk: 系统盘信息
        :type SystemDisk: :class:`tencentcloud.cvd.v20201104.models.Disk`
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvd.v20201104.models.VirtualPrivateCloud`
        :param _InstanceName: 实例显示名称。
<li> 如果该字段为空，则采用默认格式：云桌面型号+月日+三位随机数+镜像ID。</li>
<li> 购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server_{R:3}，购买1台时，实例显示名称为server_3；购买2台时，实例显示名称分别为server_3，server_4。支持指定多个模式串{R:x}。</li>
<li> 购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server_1，server_2。</li>
<li> 最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _InstanceCount: 购买实例数量。取值范围[1,50]。默认为1
        :type InstanceCount: int
        :param _DataDisks: 数据盘信息。目前只支持一块数据盘。
        :type DataDisks: list of Disk
        :param _ChargeType: 实例计费类型。
<li> PREPAID：预付费，即包年包月</li>
<li> POSTPAID_BY_HOUR：按小时后付费</li>
默认为PREPAID
        :type ChargeType: str
        :param _ChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type ChargePrepaid: :class:`tencentcloud.cvd.v20201104.models.ChargePrepaid`
        :param _DryRun: 是否只预检此次请求。
<li> true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和库存。
如果检查通过，则返回的错误码为DryRunOperation；如果返回其他错误码表示检查没有通过；</li>
<li> false（默认）：发送正常请求，通过检查后直接创建实例</li>
        :type DryRun: bool
        :param _AnonymousAccess: 允许绑定用户前的匿名访问。默认值：false。
        :type AnonymousAccess: bool
        :param _SecurityGroups: 关联的安全组ID列表
        :type SecurityGroups: list of str
        :param _PoolId: 桌面池ID
        :type PoolId: str
        :param _DomainControlPolicies: 域名管控策略ID
        :type DomainControlPolicies: list of str
        :param _Tags: 标签，最多10个
        :type Tags: list of Tag
        :param _Zone: 可用区
        :type Zone: str
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._ImageId = None
        self._VirtualPrivateCloud = None
        self._InstanceName = None
        self._InstanceCount = None
        self._DataDisks = None
        self._ChargeType = None
        self._ChargePrepaid = None
        self._DryRun = None
        self._AnonymousAccess = None
        self._SecurityGroups = None
        self._PoolId = None
        self._DomainControlPolicies = None
        self._Tags = None
        self._Zone = None

    @property
    def InstanceType(self):
        r"""实例类型。<li>  S3L.MEDIUM4: 云桌面-标准S3_2核4G </li><li> S3L.LARGE8: 云桌面-标准S3_4核8G </li><li> S3L.LARGE16: 云桌面-标准S3_4核16G </li><li> S3L.2XLARGE16: 云桌面-标准S3_8核16G </li><li> S1L.LARGE8：云桌面-标准S1_4核8G </li><li> S1L.LARGE16：标准S1_4核16G </li><li> S2L.2XLARGE16：标准S2_8核16G </li><li> G1L.LARGE16：图形G1_4核16G  </li><li> G1L.2XLARGE32：图形G1_8核32G </li><li> G1L.4XLARGE64：图形G1_16核64G </li><li> G2L.LARGE24: 云桌面-图形G2_6核24G </li><li> G2L.3XLARGE58: 云桌面-图形G2_14核58G </li><li> G2L.3XLARGE44: 云桌面-图形G2_12核44G </li><li> G3L.LARGE16: 云桌面-图形G3_4核16G </li><li> G3L.5XMEDIUM40: 云桌面-图形G3_10核40G </li><li> G3L.5XLARGE80: 云桌面-图形G3_20核80G </li><li> G4L.5XMEDIUM40: 云桌面-图形G4_10核40G </li><li> G4L.11XMEDIUM80: 云桌面-图形G4_22核80G </li><li> G4L.11XLARGE160: 云桌面-图形G4_44核160G </li><li> G5L.5XMEDIUM40: 云桌面-图形G5_10核40G </li><li> G5L.5XLARGE80: 云桌面-图形G5_22核80G </li><li> G5L.21XMEDIUM160: 云桌面-图形G5_42核160G </li><li> G5L.21XLARGE320: 云桌面-图形G5_84核320G </li>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        r"""系统盘信息
        :rtype: :class:`tencentcloud.cvd.v20201104.models.Disk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def ImageId(self):
        r"""镜像ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VirtualPrivateCloud(self):
        r"""私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :rtype: :class:`tencentcloud.cvd.v20201104.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InstanceName(self):
        r"""实例显示名称。
<li> 如果该字段为空，则采用默认格式：云桌面型号+月日+三位随机数+镜像ID。</li>
<li> 购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server_{R:3}，购买1台时，实例显示名称为server_3；购买2台时，实例显示名称分别为server_3，server_4。支持指定多个模式串{R:x}。</li>
<li> 购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server_1，server_2。</li>
<li> 最多支持60个字符（包含模式串）。</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCount(self):
        r"""购买实例数量。取值范围[1,50]。默认为1
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def DataDisks(self):
        r"""数据盘信息。目前只支持一块数据盘。
        :rtype: list of Disk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ChargeType(self):
        r"""实例计费类型。
<li> PREPAID：预付费，即包年包月</li>
<li> POSTPAID_BY_HOUR：按小时后付费</li>
默认为PREPAID
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ChargePrepaid`
        """
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid

    @property
    def DryRun(self):
        r"""是否只预检此次请求。
<li> true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和库存。
如果检查通过，则返回的错误码为DryRunOperation；如果返回其他错误码表示检查没有通过；</li>
<li> false（默认）：发送正常请求，通过检查后直接创建实例</li>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def AnonymousAccess(self):
        r"""允许绑定用户前的匿名访问。默认值：false。
        :rtype: bool
        """
        return self._AnonymousAccess

    @AnonymousAccess.setter
    def AnonymousAccess(self, AnonymousAccess):
        self._AnonymousAccess = AnonymousAccess

    @property
    def SecurityGroups(self):
        r"""关联的安全组ID列表
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def PoolId(self):
        r"""桌面池ID
        :rtype: str
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def DomainControlPolicies(self):
        r"""域名管控策略ID
        :rtype: list of str
        """
        return self._DomainControlPolicies

    @DomainControlPolicies.setter
    def DomainControlPolicies(self, DomainControlPolicies):
        self._DomainControlPolicies = DomainControlPolicies

    @property
    def Tags(self):
        r"""标签，最多10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._ImageId = params.get("ImageId")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._InstanceName = params.get("InstanceName")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = Disk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._ChargeType = params.get("ChargeType")
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaid()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self._DryRun = params.get("DryRun")
        self._AnonymousAccess = params.get("AnonymousAccess")
        self._SecurityGroups = params.get("SecurityGroups")
        self._PoolId = params.get("PoolId")
        self._DomainControlPolicies = params.get("DomainControlPolicies")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    r"""CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 当通过本接口来创建实例时会返回该参数，表示一个或多个实例ID。返回实例ID列表并不代表实例创建成功。通过进一步查询返回的InstancesSet中对应实例的ID的状态来判断创建是否完成；如果实例状态由“准备中”变为“正在运行”，则为创建成功。
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""当通过本接口来创建实例时会返回该参数，表示一个或多个实例ID。返回实例ID列表并不代表实例创建成功。通过进一步查询返回的InstancesSet中对应实例的ID的状态来判断创建是否完成；如果实例状态由“准备中”变为“正在运行”，则为创建成功。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

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
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    r"""CreatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>策略名称</p>
        :type Name: str
        :param _PolicyInfoList: <p>策略详情</p>
        :type PolicyInfoList: list of PolicyInfo
        :param _Description: <p>策略描述</p>
        :type Description: str
        :param _UserIds: <p>策略作用的用户id</p>
        :type UserIds: list of str
        """
        self._Name = None
        self._PolicyInfoList = None
        self._Description = None
        self._UserIds = None

    @property
    def Name(self):
        r"""<p>策略名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PolicyInfoList(self):
        r"""<p>策略详情</p>
        :rtype: list of PolicyInfo
        """
        return self._PolicyInfoList

    @PolicyInfoList.setter
    def PolicyInfoList(self, PolicyInfoList):
        self._PolicyInfoList = PolicyInfoList

    @property
    def Description(self):
        r"""<p>策略描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserIds(self):
        r"""<p>策略作用的用户id</p>
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("PolicyInfoList") is not None:
            self._PolicyInfoList = []
            for item in params.get("PolicyInfoList"):
                obj = PolicyInfo()
                obj._deserialize(item)
                self._PolicyInfoList.append(obj)
        self._Description = params.get("Description")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    r"""CreatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    r"""监控数据

    """

    def __init__(self):
        r"""
        :param _Dimensions: <p>实例对象维度组合</p>
        :type Dimensions: list of Dimension
        :param _Timestamps: <p>时间戳数组</p>
        :type Timestamps: list of float
        :param _Values: <p>监控值数组，与Timestamps一一对应</p>
        :type Values: list of float
        :param _MaxValues: <p>MaxValues 最大值数组，与Timestamps一一对应</p>
        :type MaxValues: list of float
        :param _MinValues: <p>MinValues 最小值数组，与Timestamps一一对应</p>
        :type MinValues: list of float
        :param _AvgValues: <p>AvgValues 平均值数组，与Timestamps一一对应</p>
        :type AvgValues: list of float
        """
        self._Dimensions = None
        self._Timestamps = None
        self._Values = None
        self._MaxValues = None
        self._MinValues = None
        self._AvgValues = None

    @property
    def Dimensions(self):
        r"""<p>实例对象维度组合</p>
        :rtype: list of Dimension
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Timestamps(self):
        r"""<p>时间戳数组</p>
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        r"""<p>监控值数组，与Timestamps一一对应</p>
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def MaxValues(self):
        r"""<p>MaxValues 最大值数组，与Timestamps一一对应</p>
        :rtype: list of float
        """
        return self._MaxValues

    @MaxValues.setter
    def MaxValues(self, MaxValues):
        self._MaxValues = MaxValues

    @property
    def MinValues(self):
        r"""<p>MinValues 最小值数组，与Timestamps一一对应</p>
        :rtype: list of float
        """
        return self._MinValues

    @MinValues.setter
    def MinValues(self, MinValues):
        self._MinValues = MinValues

    @property
    def AvgValues(self):
        r"""<p>AvgValues 平均值数组，与Timestamps一一对应</p>
        :rtype: list of float
        """
        return self._AvgValues

    @AvgValues.setter
    def AvgValues(self, AvgValues):
        self._AvgValues = AvgValues


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        self._MaxValues = params.get("MaxValues")
        self._MinValues = params.get("MinValues")
        self._AvgValues = params.get("AvgValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandTasksRequest(AbstractModel):
    r"""DeleteCommandTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <p>删除命令任务条件<br>Filter.name 目前支持 CommandId</p>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""<p>删除命令任务条件<br>Filter.name 目前支持 CommandId</p>
        :rtype: list of Filter
        """
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
        


class DeleteCommandTasksResponse(AbstractModel):
    r"""DeleteCommandTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDomainControlPolicyRequest(AbstractModel):
    r"""DeleteDomainControlPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略唯一ID
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        r"""策略唯一ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainControlPolicyResponse(AbstractModel):
    r"""DeleteDomainControlPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    r"""DeleteImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: <p>准备删除的镜像Id列表</p>
        :type ImageIds: list of str
        """
        self._ImageIds = None

    @property
    def ImageIds(self):
        r"""<p>准备删除的镜像Id列表</p>
        :rtype: list of str
        """
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    r"""DeleteImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeCommandTasksRequest(AbstractModel):
    r"""DescribeCommandTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页号</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，默认 20，最大 100</p>
        :type PageSize: int
        :param _Filters: <p>拉取任务的过滤器 ，Filter.Name 取值：CommandId - 任务 lD；Staus - 任务状态， RUNNING - 执行中；FINISHED - 执行完成（不代表成功，只表示任务执行完成）</p>
        :type Filters: list of Filter
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def PageNumber(self):
        r"""<p>页号</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，默认 20，最大 100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""<p>拉取任务的过滤器 ，Filter.Name 取值：CommandId - 任务 lD；Staus - 任务状态， RUNNING - 执行中；FINISHED - 执行完成（不代表成功，只表示任务执行完成）</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeCommandTasksResponse(AbstractModel):
    r"""DescribeCommandTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: <p>拉取任务详情数</p>
        :type Total: int
        :param _CommandDetails: <p>任务描述</p>
        :type CommandDetails: list of CommandDetail
        :param _Status: <p>任务状态，RUNNING -执行中；FINISHED-执行完成； STOPPED-终止任务</p>
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._CommandDetails = None
        self._Status = None
        self._RequestId = None

    @property
    def Total(self):
        r"""<p>拉取任务详情数</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CommandDetails(self):
        r"""<p>任务描述</p>
        :rtype: list of CommandDetail
        """
        return self._CommandDetails

    @CommandDetails.setter
    def CommandDetails(self, CommandDetails):
        self._CommandDetails = CommandDetails

    @property
    def Status(self):
        r"""<p>任务状态，RUNNING -执行中；FINISHED-执行完成； STOPPED-终止任务</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Total = params.get("Total")
        if params.get("CommandDetails") is not None:
            self._CommandDetails = []
            for item in params.get("CommandDetails"):
                obj = CommandDetail()
                obj._deserialize(item)
                self._CommandDetails.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    r"""DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>拉取页号</p>
        :type PageNumber: int
        :param _PageSize: <p>每页拉取个数</p>
        :type PageSize: int
        :param _Filters: <p>Name取值：[&quot;ImageID&quot;,&quot;Name&quot;,&quot;ImageType&quot;,&quot;ImageState&quot;,&quot;Region&quot;,&quot;InstanceType&quot;]<br>注意：filter中没有ImageID或ImageState过滤条件，后台默认不返回INVISIBLE的镜像信息</p>
        :type Filters: list of Filter
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def PageNumber(self):
        r"""<p>拉取页号</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页拉取个数</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""<p>Name取值：[&quot;ImageID&quot;,&quot;Name&quot;,&quot;ImageType&quot;,&quot;ImageState&quot;,&quot;Region&quot;,&quot;InstanceType&quot;]<br>注意：filter中没有ImageID或ImageState过滤条件，后台默认不返回INVISIBLE的镜像信息</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeImagesResponse(AbstractModel):
    r"""DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Images: <p>返回查询到的所有镜像信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Images: list of ImageInfo
        :param _Total: <p>返回当前查询到的镜像总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Images = None
        self._Total = None
        self._RequestId = None

    @property
    def Images(self):
        r"""<p>返回查询到的所有镜像信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageInfo
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Total(self):
        r"""<p>返回当前查询到的镜像总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._Images.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstanceFetchMsgRequest(AbstractModel):
    r"""DescribeInstanceFetchMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _UserId: 绑定实例的UserID，为后续多会话预留参数
        :type UserId: str
        :param _DesktopName: 拉取桌面title，用户可自行定义，默认为云桌面实例名称
        :type DesktopName: str
        :param _Force: 是否抢占桌面，即桌面使用过程中，抢占登录。
true：抢占登录
false：非抢占登录
默认为抢占登录
        :type Force: bool
        :param _IsInternal: 是否内网登录桌面
        :type IsInternal: bool
        """
        self._InstanceId = None
        self._UserId = None
        self._DesktopName = None
        self._Force = None
        self._IsInternal = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        r"""绑定实例的UserID，为后续多会话预留参数
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DesktopName(self):
        r"""拉取桌面title，用户可自行定义，默认为云桌面实例名称
        :rtype: str
        """
        return self._DesktopName

    @DesktopName.setter
    def DesktopName(self, DesktopName):
        self._DesktopName = DesktopName

    @property
    def Force(self):
        r"""是否抢占桌面，即桌面使用过程中，抢占登录。
true：抢占登录
false：非抢占登录
默认为抢占登录
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def IsInternal(self):
        r"""是否内网登录桌面
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        self._DesktopName = params.get("DesktopName")
        self._Force = params.get("Force")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceFetchMsgResponse(AbstractModel):
    r"""DescribeInstanceFetchMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FetchStatusTicket: 桌面登录ticket状态描述
        :type FetchStatusTicket: str
        :param _FetchTicket: 桌面登录ticket描述
        :type FetchTicket: str
        :param _FetchUrl: 桌面登录launch url
        :type FetchUrl: str
        :param _ProtocolVersion: 桌面传输协议
        :type ProtocolVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FetchStatusTicket = None
        self._FetchTicket = None
        self._FetchUrl = None
        self._ProtocolVersion = None
        self._RequestId = None

    @property
    def FetchStatusTicket(self):
        r"""桌面登录ticket状态描述
        :rtype: str
        """
        return self._FetchStatusTicket

    @FetchStatusTicket.setter
    def FetchStatusTicket(self, FetchStatusTicket):
        self._FetchStatusTicket = FetchStatusTicket

    @property
    def FetchTicket(self):
        r"""桌面登录ticket描述
        :rtype: str
        """
        return self._FetchTicket

    @FetchTicket.setter
    def FetchTicket(self, FetchTicket):
        self._FetchTicket = FetchTicket

    @property
    def FetchUrl(self):
        r"""桌面登录launch url
        :rtype: str
        """
        return self._FetchUrl

    @FetchUrl.setter
    def FetchUrl(self, FetchUrl):
        self._FetchUrl = FetchUrl

    @property
    def ProtocolVersion(self):
        r"""桌面传输协议
        :rtype: str
        """
        return self._ProtocolVersion

    @ProtocolVersion.setter
    def ProtocolVersion(self, ProtocolVersion):
        self._ProtocolVersion = ProtocolVersion

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
        self._FetchStatusTicket = params.get("FetchStatusTicket")
        self._FetchTicket = params.get("FetchTicket")
        self._FetchUrl = params.get("FetchUrl")
        self._ProtocolVersion = params.get("ProtocolVersion")
        self._RequestId = params.get("RequestId")


class DescribeInstanceGraphDataRequest(AbstractModel):
    r"""DescribeInstanceGraphData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云桌面实例ID
        :type InstanceId: str
        :param _StartTime: 查询起始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        r"""云桌面实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""查询起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
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
        


class DescribeInstanceGraphDataResponse(AbstractModel):
    r"""DescribeInstanceGraphData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _Period: 周期
        :type Period: int
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Partitions: 实例磁盘数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of Partition
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._MetricName = None
        self._Partitions = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""查询起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MetricName(self):
        r"""指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Partitions(self):
        r"""实例磁盘数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Partition
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._MetricName = params.get("MetricName")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = Partition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceLoginMsgRequest(AbstractModel):
    r"""DescribeInstanceLoginMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _UserId: 绑定实例的UserID，为后续多会话预留参数
        :type UserId: str
        :param _DesktopName: 拉取桌面title，用户可自行定义，默认为云桌面实例名称
        :type DesktopName: str
        :param _Force: 是否抢占桌面，即桌面使用过程中，抢占登录。
true：抢占登录
false：非抢占登录
默认为抢占登录
        :type Force: bool
        :param _IsInternal: 是否内网方式
        :type IsInternal: bool
        """
        self._InstanceId = None
        self._UserId = None
        self._DesktopName = None
        self._Force = None
        self._IsInternal = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        r"""绑定实例的UserID，为后续多会话预留参数
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DesktopName(self):
        r"""拉取桌面title，用户可自行定义，默认为云桌面实例名称
        :rtype: str
        """
        return self._DesktopName

    @DesktopName.setter
    def DesktopName(self, DesktopName):
        self._DesktopName = DesktopName

    @property
    def Force(self):
        r"""是否抢占桌面，即桌面使用过程中，抢占登录。
true：抢占登录
false：非抢占登录
默认为抢占登录
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def IsInternal(self):
        r"""是否内网方式
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        self._DesktopName = params.get("DesktopName")
        self._Force = params.get("Force")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLoginMsgResponse(AbstractModel):
    r"""DescribeInstanceLoginMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginMsg: 桌面登录login信息
        :type LoginMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginMsg = None
        self._RequestId = None

    @property
    def LoginMsg(self):
        r"""桌面登录login信息
        :rtype: str
        """
        return self._LoginMsg

    @LoginMsg.setter
    def LoginMsg(self, LoginMsg):
        self._LoginMsg = LoginMsg

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
        self._LoginMsg = params.get("LoginMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorDataRequest(AbstractModel):
    r"""DescribeInstanceMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: <p>实例维度组合数组</p>
        :type Instances: list of Instance
        :param _NameSpace: <p>命名空间。如QCE/CVM、QCE/BLOCK_STORAGE等</p>
        :type NameSpace: str
        :param _MetricName: <p>指标名</p>
        :type MetricName: str
        :param _Period: <p>统计周期(时间粒度), 单位s。</p>
        :type Period: int
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _SpecifyStatistics: <p>多种统计方式数据。avg, max, min (1,2,4)可以自由组合</p>
        :type SpecifyStatistics: int
        """
        self._Instances = None
        self._NameSpace = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._SpecifyStatistics = None

    @property
    def Instances(self):
        r"""<p>实例维度组合数组</p>
        :rtype: list of Instance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def NameSpace(self):
        r"""<p>命名空间。如QCE/CVM、QCE/BLOCK_STORAGE等</p>
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def MetricName(self):
        r"""<p>指标名</p>
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        r"""<p>统计周期(时间粒度), 单位s。</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SpecifyStatistics(self):
        r"""<p>多种统计方式数据。avg, max, min (1,2,4)可以自由组合</p>
        :rtype: int
        """
        return self._SpecifyStatistics

    @SpecifyStatistics.setter
    def SpecifyStatistics(self, SpecifyStatistics):
        self._SpecifyStatistics = SpecifyStatistics


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._NameSpace = params.get("NameSpace")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SpecifyStatistics = params.get("SpecifyStatistics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorDataResponse(AbstractModel):
    r"""DescribeInstanceMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricName: <p>指标名</p>
        :type MetricName: str
        :param _Period: <p>统计周期</p>
        :type Period: int
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _DataPoints: <p>数据点数组</p>
        :type DataPoints: list of DataPoint
        :param _Msg: <p>message信息</p>
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._DataPoints = None
        self._Msg = None
        self._RequestId = None

    @property
    def MetricName(self):
        r"""<p>指标名</p>
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        r"""<p>统计周期</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DataPoints(self):
        r"""<p>数据点数组</p>
        :rtype: list of DataPoint
        """
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

    @property
    def Msg(self):
        r"""<p>message信息</p>
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("DataPoints") is not None:
            self._DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self._DataPoints.append(obj)
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceRegionDistributionRequest(AbstractModel):
    r"""DescribeInstanceRegionDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: <p>查询区域列表</p>
        :type Regions: list of str
        :param _Types: <p>查询实例类型列表</p>
        :type Types: list of str
        :param _UserId: <p>查询用户拥有的云桌面地域分布信息</p>
        :type UserId: str
        """
        self._Regions = None
        self._Types = None
        self._UserId = None

    @property
    def Regions(self):
        r"""<p>查询区域列表</p>
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Types(self):
        r"""<p>查询实例类型列表</p>
        :rtype: list of str
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def UserId(self):
        r"""<p>查询用户拥有的云桌面地域分布信息</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._Types = params.get("Types")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceRegionDistributionResponse(AbstractModel):
    r"""DescribeInstanceRegionDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DistributionInfo: <p>各区域实例个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributionInfo: list of DistributionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DistributionInfo = None
        self._RequestId = None

    @property
    def DistributionInfo(self):
        r"""<p>各区域实例个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DistributionInfo
        """
        return self._DistributionInfo

    @DistributionInfo.setter
    def DistributionInfo(self, DistributionInfo):
        self._DistributionInfo = DistributionInfo

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
        if params.get("DistributionInfo") is not None:
            self._DistributionInfo = []
            for item in params.get("DistributionInfo"):
                obj = DistributionInfo()
                obj._deserialize(item)
                self._DistributionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesBindStatusRequest(AbstractModel):
    r"""DescribeInstancesBindStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>拉取的桌面id列表</p>
        :type InstanceIds: list of str
        :param _InstanceRegion: <p>实例所在区域</p>
        :type InstanceRegion: str
        """
        self._InstanceIds = None
        self._InstanceRegion = None

    @property
    def InstanceIds(self):
        r"""<p>拉取的桌面id列表</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceRegion(self):
        r"""<p>实例所在区域</p>
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceRegion = params.get("InstanceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesBindStatusResponse(AbstractModel):
    r"""DescribeInstancesBindStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceBindStatusList: <p>桌面实例状态列表</p>
        :type InstanceBindStatusList: list of BindStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceBindStatusList = None
        self._RequestId = None

    @property
    def InstanceBindStatusList(self):
        r"""<p>桌面实例状态列表</p>
        :rtype: list of BindStatusInfo
        """
        return self._InstanceBindStatusList

    @InstanceBindStatusList.setter
    def InstanceBindStatusList(self, InstanceBindStatusList):
        self._InstanceBindStatusList = InstanceBindStatusList

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
        if params.get("InstanceBindStatusList") is not None:
            self._InstanceBindStatusList = []
            for item in params.get("InstanceBindStatusList"):
                obj = BindStatusInfo()
                obj._deserialize(item)
                self._InstanceBindStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 拉取页号
        :type PageNumber: int
        :param _PageSize: 每页拉取个数
        :type PageSize: int
        :param _Filters: Name取值范围："InstanceId"      按照云桌面ID搜索，云桌面ID示例：cdi-l0dfy594htvbn37"Name"     按照云桌面名称搜索 "Region"     按照云桌面所在地域搜索，目前云桌面所支持的地域：        ap-beijing：北京        ap-shanghai：上海        ap-guangzhou：广州        ap-shanghai-adc：上海自动驾驶云"Type"    按照云桌面类型搜索，类型取值：        S3L.MEDIUM4：云桌面-标准S3_2核4G        S3L.LARGE8：云桌面-标准S3_4核8G        S3L.LARGE16：云桌面-标准S3_4核16G        S3L.2XLARGE16：云桌面-标准S3_8核16G        S1L.LARGE8：云桌面-标准S1_4核8G        S1L.LARGE16：云桌面-标准S1_4核16G        S2L.2XLARGE16：云桌面-标准S2_8核16G        G1L.LARGE16：云桌面-图形G1_4核16G        G1L.2XLARGE32：云桌面-图形G1_8核32G        G1L.4XLARGE64：云桌面-图形G1_16核64G        G2L.LARGE24：云桌面-图形G2_6核24G        G2L.3XLARGE58：云桌面-图形G2_14核58G	        G2L.3XLARGE44：云桌面-图形G2_12核44G         G3L.LARGE16：云桌面-图形G3_4核16G	        G3L.5XMEDIUM40：云桌面-图形G3_10核40G	        G3L.5XLARGE80：云桌面-图形G3_20核80G        G4L.5XMEDIUM40：云桌面-图形G4_10核40G        G4L.11XMEDIUM80：云桌面-图形G4_22核80G        G4L.11XLARGE160：云桌面-图形G4_44核160G        G5L.5XMEDIUM40：云桌面-图形G5_10核40G	        G5L.5XLARGE80：云桌面-图形G5_22核80G        G5L.21XMEDIUM160：云桌面-图形G5_42核160G        G5L.21XLARGE320：云桌面-图形G5_84核320G	"ImageId"    按照镜像ID搜索，镜像ID示例：img-ed892xcd2"ChargeType"    按着计费模式搜索，目前支持的计费模式为：         PREPAID：包年包月        POSTPAID_BY_HOUR：按量计费 "HostName"    按照云桌面机器名称搜索，云桌面机器名示例：l0dfy594htvbn37"Status"    按照桌面状态搜索，云桌面状态：        PENDING：创建中        STARTING：开机中        REBOOTING：重启中        ROLLBACKING：回滚中        RESETTING：重置中        STOPPING：关机中        TERMINATING：销毁中        RUNNING：运行中        USING：使用中        STOPPED：关机        ISOLATING ：隔离中，只返回最近24小时数据        SHUTDOWN：销毁，只返回最近24小时数据        DELETED：销毁和SHUTDOWN意义一致，只返回最近24小时数据        LAUNCH_FAILED：创建失败，只返回最近24小时数据"UserId"    按照绑定的用户ID搜索，用户ID示例: us-6b36f283c302481bb83bsdswdefqdqwerqw"UserVpcId"    按照云桌面所属vpc搜索，VPCID示例: vpc-0ji679xf"UserSubnetId"    按照云桌面所属子网搜索，SubnetID示例: subnet-0ji679xf"UserPrivateIp"    按照云桌面IP搜索"Keyword"    按照云桌面绑定的用户名搜索，Values每次只取第一个值"SecurityGroupId"    按照云桌面关联安全组搜索，Values每次只取第一个值,安全组ID实例：sg-0ji679xf"AssociateSG"    按照可以关联安全组搜索，Values每次只取第一个值,安全组ID实例：sg-0ji679xf"DomainControlPolicyId"    按照云桌面关联域名管控策略搜索，Values每次只取第一个值,安全组ID实例：domain-0ji679xf "AssociateDomainControlPolicy"    按照可以关联域名策略搜索        ①若已有域名策略关联桌面情况：Values每次只取第一个值,安全组ID实例：domain-0ji679xf         ②若新建域名策略关联桌面情况，Values传空"Uin"    外部租户请勿使用"AppId"    外部租户请勿使用"ImageName"    废弃
        :type Filters: list of Filter
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def PageNumber(self):
        r"""拉取页号
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页拉取个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""Name取值范围："InstanceId"      按照云桌面ID搜索，云桌面ID示例：cdi-l0dfy594htvbn37"Name"     按照云桌面名称搜索 "Region"     按照云桌面所在地域搜索，目前云桌面所支持的地域：        ap-beijing：北京        ap-shanghai：上海        ap-guangzhou：广州        ap-shanghai-adc：上海自动驾驶云"Type"    按照云桌面类型搜索，类型取值：        S3L.MEDIUM4：云桌面-标准S3_2核4G        S3L.LARGE8：云桌面-标准S3_4核8G        S3L.LARGE16：云桌面-标准S3_4核16G        S3L.2XLARGE16：云桌面-标准S3_8核16G        S1L.LARGE8：云桌面-标准S1_4核8G        S1L.LARGE16：云桌面-标准S1_4核16G        S2L.2XLARGE16：云桌面-标准S2_8核16G        G1L.LARGE16：云桌面-图形G1_4核16G        G1L.2XLARGE32：云桌面-图形G1_8核32G        G1L.4XLARGE64：云桌面-图形G1_16核64G        G2L.LARGE24：云桌面-图形G2_6核24G        G2L.3XLARGE58：云桌面-图形G2_14核58G	        G2L.3XLARGE44：云桌面-图形G2_12核44G         G3L.LARGE16：云桌面-图形G3_4核16G	        G3L.5XMEDIUM40：云桌面-图形G3_10核40G	        G3L.5XLARGE80：云桌面-图形G3_20核80G        G4L.5XMEDIUM40：云桌面-图形G4_10核40G        G4L.11XMEDIUM80：云桌面-图形G4_22核80G        G4L.11XLARGE160：云桌面-图形G4_44核160G        G5L.5XMEDIUM40：云桌面-图形G5_10核40G	        G5L.5XLARGE80：云桌面-图形G5_22核80G        G5L.21XMEDIUM160：云桌面-图形G5_42核160G        G5L.21XLARGE320：云桌面-图形G5_84核320G	"ImageId"    按照镜像ID搜索，镜像ID示例：img-ed892xcd2"ChargeType"    按着计费模式搜索，目前支持的计费模式为：         PREPAID：包年包月        POSTPAID_BY_HOUR：按量计费 "HostName"    按照云桌面机器名称搜索，云桌面机器名示例：l0dfy594htvbn37"Status"    按照桌面状态搜索，云桌面状态：        PENDING：创建中        STARTING：开机中        REBOOTING：重启中        ROLLBACKING：回滚中        RESETTING：重置中        STOPPING：关机中        TERMINATING：销毁中        RUNNING：运行中        USING：使用中        STOPPED：关机        ISOLATING ：隔离中，只返回最近24小时数据        SHUTDOWN：销毁，只返回最近24小时数据        DELETED：销毁和SHUTDOWN意义一致，只返回最近24小时数据        LAUNCH_FAILED：创建失败，只返回最近24小时数据"UserId"    按照绑定的用户ID搜索，用户ID示例: us-6b36f283c302481bb83bsdswdefqdqwerqw"UserVpcId"    按照云桌面所属vpc搜索，VPCID示例: vpc-0ji679xf"UserSubnetId"    按照云桌面所属子网搜索，SubnetID示例: subnet-0ji679xf"UserPrivateIp"    按照云桌面IP搜索"Keyword"    按照云桌面绑定的用户名搜索，Values每次只取第一个值"SecurityGroupId"    按照云桌面关联安全组搜索，Values每次只取第一个值,安全组ID实例：sg-0ji679xf"AssociateSG"    按照可以关联安全组搜索，Values每次只取第一个值,安全组ID实例：sg-0ji679xf"DomainControlPolicyId"    按照云桌面关联域名管控策略搜索，Values每次只取第一个值,安全组ID实例：domain-0ji679xf "AssociateDomainControlPolicy"    按照可以关联域名策略搜索        ①若已有域名策略关联桌面情况：Values每次只取第一个值,安全组ID实例：domain-0ji679xf         ②若新建域名策略关联桌面情况，Values传空"Uin"    外部租户请勿使用"AppId"    外部租户请勿使用"ImageName"    废弃
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: 返回查询到的所有实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of InstanceInfo
        :param _Total: 返回当前查询到的实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._Total = None
        self._RequestId = None

    @property
    def InstanceList(self):
        r"""返回查询到的所有实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceInfo
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Total(self):
        r"""返回当前查询到的实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    r"""DescribeInstancesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>查询的实例id列表</p>
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""<p>查询的实例id列表</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesStatusResponse(AbstractModel):
    r"""DescribeInstancesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceStatusList: <p>实例状态列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatusList: list of InstanceStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceStatusList = None
        self._RequestId = None

    @property
    def InstanceStatusList(self):
        r"""<p>实例状态列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceStatus
        """
        return self._InstanceStatusList

    @InstanceStatusList.setter
    def InstanceStatusList(self, InstanceStatusList):
        self._InstanceStatusList = InstanceStatusList

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
        if params.get("InstanceStatusList") is not None:
            self._InstanceStatusList = []
            for item in params.get("InstanceStatusList"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self._InstanceStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvocationDetailRequest(AbstractModel):
    r"""DescribeInvocationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>云桌面实例ID。</p>
        :type InstanceId: str
        :param _InvokeId: <p>任务ID。</p>
        :type InvokeId: str
        :param _OutputLinesOffset: <p>需要返回的任务输出行号起始索引。</p>
        :type OutputLinesOffset: int
        :param _OutputLinesLimit: <p>需要返回的任务输出行数。</p>
        :type OutputLinesLimit: int
        :param _MergeOutputLines: <p>任务的输出内容是否合并成一个字符串。默认为true。</p>
        :type MergeOutputLines: bool
        """
        self._InstanceId = None
        self._InvokeId = None
        self._OutputLinesOffset = None
        self._OutputLinesLimit = None
        self._MergeOutputLines = None

    @property
    def InstanceId(self):
        r"""<p>云桌面实例ID。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvokeId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId

    @property
    def OutputLinesOffset(self):
        r"""<p>需要返回的任务输出行号起始索引。</p>
        :rtype: int
        """
        return self._OutputLinesOffset

    @OutputLinesOffset.setter
    def OutputLinesOffset(self, OutputLinesOffset):
        self._OutputLinesOffset = OutputLinesOffset

    @property
    def OutputLinesLimit(self):
        r"""<p>需要返回的任务输出行数。</p>
        :rtype: int
        """
        return self._OutputLinesLimit

    @OutputLinesLimit.setter
    def OutputLinesLimit(self, OutputLinesLimit):
        self._OutputLinesLimit = OutputLinesLimit

    @property
    def MergeOutputLines(self):
        r"""<p>任务的输出内容是否合并成一个字符串。默认为true。</p>
        :rtype: bool
        """
        return self._MergeOutputLines

    @MergeOutputLines.setter
    def MergeOutputLines(self, MergeOutputLines):
        self._MergeOutputLines = MergeOutputLines


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InvokeId = params.get("InvokeId")
        self._OutputLinesOffset = params.get("OutputLinesOffset")
        self._OutputLinesLimit = params.get("OutputLinesLimit")
        self._MergeOutputLines = params.get("MergeOutputLines")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationDetailResponse(AbstractModel):
    r"""DescribeInvocationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Detail: <p>实例上任务执行的详细情况。</p>
        :type Detail: :class:`tencentcloud.cvd.v20201104.models.Invocation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        r"""<p>实例上任务执行的详细情况。</p>
        :rtype: :class:`tencentcloud.cvd.v20201104.models.Invocation`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        if params.get("Detail") is not None:
            self._Detail = Invocation()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeInvocationsRequest(AbstractModel):
    r"""DescribeInvocations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>云桌面实例ID。</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>云桌面实例ID。</p>
        :rtype: str
        """
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
        


class DescribeInvocationsResponse(AbstractModel):
    r"""DescribeInvocations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Invocations: <p>该实例上的任务列表。不会返回Output字段。</p>
        :type Invocations: list of Invocation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Invocations = None
        self._RequestId = None

    @property
    def Invocations(self):
        r"""<p>该实例上的任务列表。不会返回Output字段。</p>
        :rtype: list of Invocation
        """
        return self._Invocations

    @Invocations.setter
    def Invocations(self, Invocations):
        self._Invocations = Invocations

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
        if params.get("Invocations") is not None:
            self._Invocations = []
            for item in params.get("Invocations"):
                obj = Invocation()
                obj._deserialize(item)
                self._Invocations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicyDetailRequest(AbstractModel):
    r"""DescribePolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>拉取页号</p>
        :type PageNumber: int
        :param _PageSize: <p>每页最大显示个数，最大值不超过100</p>
        :type PageSize: int
        :param _Filters: <p>查询条件（暂时无效，保留字段）</p>
        :type Filters: list of Filter
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def PageNumber(self):
        r"""<p>拉取页号</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页最大显示个数，最大值不超过100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""<p>查询条件（暂时无效，保留字段）</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePolicyDetailResponse(AbstractModel):
    r"""DescribePolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyList: <p>策略详细信息列表</p>
        :type PolicyList: list of PolicyDetail
        :param _Total: <p>当前查询到的策略总数</p>
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyList = None
        self._Total = None
        self._RequestId = None

    @property
    def PolicyList(self):
        r"""<p>策略详细信息列表</p>
        :rtype: list of PolicyDetail
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList

    @property
    def Total(self):
        r"""<p>当前查询到的策略总数</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = PolicyDetail()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    r"""DescribeSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页号，从1开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页最大展示数量，默认20，最大100</p>
        :type PageSize: int
        :param _SecurityGroupRegion: <p>地域</p>
        :type SecurityGroupRegion: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._SecurityGroupRegion = None

    @property
    def PageNumber(self):
        r"""<p>页号，从1开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页最大展示数量，默认20，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SecurityGroupRegion(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._SecurityGroupRegion

    @SecurityGroupRegion.setter
    def SecurityGroupRegion(self, SecurityGroupRegion):
        self._SecurityGroupRegion = SecurityGroupRegion


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SecurityGroupRegion = params.get("SecurityGroupRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupsResponse(AbstractModel):
    r"""DescribeSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    r"""DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotRegion: <p>快照所在的地域</p>
        :type SnapshotRegion: str
        :param _PageNumber: <p>页号</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小，最大100，默认20</p>
        :type PageSize: int
        :param _Filters: <p>检索条件，Filter的name取值：<br>InstanceId：实例ID，返回当前实例挂载的云硬盘关联的快照信息<br>DiskId：云硬盘ID，返回当前云硬盘关联的快照信息</p>
        :type Filters: list of Filter
        """
        self._SnapshotRegion = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None

    @property
    def SnapshotRegion(self):
        r"""<p>快照所在的地域</p>
        :rtype: str
        """
        return self._SnapshotRegion

    @SnapshotRegion.setter
    def SnapshotRegion(self, SnapshotRegion):
        self._SnapshotRegion = SnapshotRegion

    @property
    def PageNumber(self):
        r"""<p>页号</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小，最大100，默认20</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""<p>检索条件，Filter的name取值：<br>InstanceId：实例ID，返回当前实例挂载的云硬盘关联的快照信息<br>DiskId：云硬盘ID，返回当前云硬盘关联的快照信息</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SnapshotRegion = params.get("SnapshotRegion")
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
        


class DescribeSnapshotsResponse(AbstractModel):
    r"""DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>当前检索条件可查询到的快照总数</p>
        :type TotalCount: int
        :param _SnapshotList: <p>快照明细列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotList: list of SnapshotInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>当前检索条件可查询到的快照总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotList(self):
        r"""<p>快照明细列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SnapshotInfo
        """
        return self._SnapshotList

    @SnapshotList.setter
    def SnapshotList(self, SnapshotList):
        self._SnapshotList = SnapshotList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SnapshotList") is not None:
            self._SnapshotList = []
            for item in params.get("SnapshotList"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._SnapshotList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsageRequest(AbstractModel):
    r"""DescribeUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，最小不能超过当前时间 90 天前，取 unix 时间戳
        :type StartTime: int
        :param _EndTime: 查询截止时间，取 unix 时间戳
        :type EndTime: int
        :param _PageSize: 每页查询信息条数，默认 20，最大 100
        :type PageSize: int
        :param _PageNumber: 页号，起始页为 1，不填默认为 1
        :type PageNumber: int
        :param _QueryKey: 查询key，每次查询会返回
        :type QueryKey: str
        :param _Filters: 查询条件，Name可选为：
InstanceId按照实例ID搜索
UserName按照绑定的用户搜索，只取Values的第一个值
ChareType按照计费类型搜索
InstanceType按照实例类型搜索
        :type Filters: list of Filter
        :param _SortType: 指定的排序方式，默认不排序
1:使用时间，升序
2:使用时间，降序
3:空闲时间，升序
4:空闲时间，降序
        :type SortType: int
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNumber = None
        self._QueryKey = None
        self._Filters = None
        self._SortType = None

    @property
    def StartTime(self):
        r"""查询起始时间，最小不能超过当前时间 90 天前，取 unix 时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询截止时间，取 unix 时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        r"""每页查询信息条数，默认 20，最大 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""页号，起始页为 1，不填默认为 1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def QueryKey(self):
        r"""查询key，每次查询会返回
        :rtype: str
        """
        return self._QueryKey

    @QueryKey.setter
    def QueryKey(self, QueryKey):
        self._QueryKey = QueryKey

    @property
    def Filters(self):
        r"""查询条件，Name可选为：
InstanceId按照实例ID搜索
UserName按照绑定的用户搜索，只取Values的第一个值
ChareType按照计费类型搜索
InstanceType按照实例类型搜索
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortType(self):
        r"""指定的排序方式，默认不排序
1:使用时间，升序
2:使用时间，降序
3:空闲时间，升序
4:空闲时间，降序
        :rtype: int
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._QueryKey = params.get("QueryKey")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageResponse(AbstractModel):
    r"""DescribeUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 检索出相关使用详情总数
        :type Total: int
        :param _QueryKey: 查询 key，作为翻页查询入参
        :type QueryKey: str
        :param _UsageSet: 使用时长详情
        :type UsageSet: list of Usage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._QueryKey = None
        self._UsageSet = None
        self._RequestId = None

    @property
    def Total(self):
        r"""检索出相关使用详情总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QueryKey(self):
        r"""查询 key，作为翻页查询入参
        :rtype: str
        """
        return self._QueryKey

    @QueryKey.setter
    def QueryKey(self, QueryKey):
        self._QueryKey = QueryKey

    @property
    def UsageSet(self):
        r"""使用时长详情
        :rtype: list of Usage
        """
        return self._UsageSet

    @UsageSet.setter
    def UsageSet(self, UsageSet):
        self._UsageSet = UsageSet

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
        self._Total = params.get("Total")
        self._QueryKey = params.get("QueryKey")
        if params.get("UsageSet") is not None:
            self._UsageSet = []
            for item in params.get("UsageSet"):
                obj = Usage()
                obj._deserialize(item)
                self._UsageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    r"""DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Keyword: <p>搜索关键字。</p>
        :type Keyword: str
        :param _PageNumber: <p>页面编号。从1开始</p>
        :type PageNumber: int
        :param _PageSize: <p>页面大小。默认20，不超过100。</p>
        :type PageSize: int
        :param _DepartmentId: <p>部门ID。</p>
        :type DepartmentId: str
        """
        self._Keyword = None
        self._PageNumber = None
        self._PageSize = None
        self._DepartmentId = None

    @property
    def Keyword(self):
        r"""<p>搜索关键字。</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PageNumber(self):
        r"""<p>页面编号。从1开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>页面大小。默认20，不超过100。</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DepartmentId(self):
        r"""<p>部门ID。</p>
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    r"""DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的用户个数。</p>
        :type TotalCount: int
        :param _Users: <p>用户列表。</p>
        :type Users: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Users = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的用户个数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Users(self):
        r"""<p>用户列表。</p>
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    r"""实例对象的维度组合

    """

    def __init__(self):
        r"""
        :param _Name: 实例维度名称
        :type Name: str
        :param _Value: 实例维度值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""实例维度名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""实例维度值
        :rtype: str
        """
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
        


class DisassociateSecurityGroupRequest(AbstractModel):
    r"""DisassociateSecurityGroup请求参数结构体

    """


class DisassociateSecurityGroupResponse(AbstractModel):
    r"""DisassociateSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailureSet: 解关联失败的云桌面列表
        :type FailureSet: list of str
        :param _SuccessSet: 解关联成功的云桌面列表
        :type SuccessSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailureSet = None
        self._SuccessSet = None
        self._RequestId = None

    @property
    def FailureSet(self):
        r"""解关联失败的云桌面列表
        :rtype: list of str
        """
        return self._FailureSet

    @FailureSet.setter
    def FailureSet(self, FailureSet):
        self._FailureSet = FailureSet

    @property
    def SuccessSet(self):
        r"""解关联成功的云桌面列表
        :rtype: list of str
        """
        return self._SuccessSet

    @SuccessSet.setter
    def SuccessSet(self, SuccessSet):
        self._SuccessSet = SuccessSet

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
        self._FailureSet = params.get("FailureSet")
        self._SuccessSet = params.get("SuccessSet")
        self._RequestId = params.get("RequestId")


class Disk(AbstractModel):
    r"""桌面实例挂载磁盘信息

    """

    def __init__(self):
        r"""
        :param _DiskType: <p>磁盘类型：<br>CLOUD_SSD：SSD云硬盘<br>CLOUD_PREMIUM：高性能云硬盘</p>
        :type DiskType: str
        :param _DiskSize: <p>磁盘大小（单位G）<br>系统盘最小值50，最大值500<br>数据盘最小值10，最大值32000。最小调整步长为10G</p>
        :type DiskSize: int
        :param _DiskId: <p>磁盘id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskId: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskId = None

    @property
    def DiskType(self):
        r"""<p>磁盘类型：<br>CLOUD_SSD：SSD云硬盘<br>CLOUD_PREMIUM：高性能云硬盘</p>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>磁盘大小（单位G）<br>系统盘最小值50，最大值500<br>数据盘最小值10，最大值32000。最小调整步长为10G</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        r"""<p>磁盘id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributionInfo(AbstractModel):
    r"""各地域实例个数信息

    """

    def __init__(self):
        r"""
        :param _Region: <p>地域描述</p>
        :type Region: str
        :param _Count: <p>实例个数</p>
        :type Count: int
        """
        self._Region = None
        self._Count = None

    @property
    def Region(self):
        r"""<p>地域描述</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Count(self):
        r"""<p>实例个数</p>
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainControlDetail(AbstractModel):
    r"""域名控制策略详情

    """

    def __init__(self):
        r"""
        :param _Domain: 配置域名
        :type Domain: str
        :param _Address: 此参数必填，新版本无异议，请求包和回包强制填写空字符串,做校验
        :type Address: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Domain = None
        self._Address = None
        self._Description = None

    @property
    def Domain(self):
        r"""配置域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Address(self):
        r"""此参数必填，新版本无异议，请求包和回包强制填写空字符串,做校验
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Description(self):
        r"""规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Address = params.get("Address")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""查询因子

    """

    def __init__(self):
        r"""
        :param _Name: 要匹配的参数名
        :type Name: str
        :param _Values: 要匹配的参数值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""要匹配的参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""要匹配的参数值
        :rtype: list of str
        """
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
        


class ImageInfo(AbstractModel):
    r"""云桌面镜像信息

    """

    def __init__(self):
        r"""
        :param _ImageID: <p>镜像id</p>
        :type ImageID: str
        :param _ImageName: <p>镜像名称</p>
        :type ImageName: str
        :param _ImageType: <p>镜像类型：<br>PUBLIC_IMAGE-公共镜像<br>PRIVATE_IMAGE-自定义镜像<br>TENCENT_OFFICE_IMAGE-腾讯办公镜像</p>
        :type ImageType: str
        :param _ImageState: <p>镜像状态：<br>CREATING-创建中<br>NORMAL-正常<br>CREATEFAILED-创建失败<br>USING-使用中<br>SYNCING-同步中<br>IMPORTING-导入中<br>IMPORTFAILED-导入失败<br>INVISIBLE-淘汰的镜像<br>DELETIING-删除中<br>DELETED-删除的</p>
        :type ImageState: str
        :param _OsName: <p>镜像操作系统</p>
        :type OsName: str
        :param _ImageSize: <p>镜像大小（单位G）</p>
        :type ImageSize: int
        :param _Description: <p>镜像描述</p>
        :type Description: str
        :param _Region: <p>镜像所在区域</p>
        :type Region: str
        :param _CoreType: <p>内核类型：<br>CPU<br>GPU<br>GPU_A10<br>GPU_RTX6000<br>GPU_2080Ti<br>GPU_3080Ti</p>
        :type CoreType: str
        :param _CvmImageId: <p>cvm侧镜像id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmImageId: str
        :param _IsWhole: <p>是否是整机镜像，整机镜像无法用于桌面重置<br>true：整机镜像<br>false: 不是整机镜像</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWhole: bool
        :param _DataDiskSize: <p>整机镜像中数据盘大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskSize: int
        :param _CreateTime: <p>镜像创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._ImageID = None
        self._ImageName = None
        self._ImageType = None
        self._ImageState = None
        self._OsName = None
        self._ImageSize = None
        self._Description = None
        self._Region = None
        self._CoreType = None
        self._CvmImageId = None
        self._IsWhole = None
        self._DataDiskSize = None
        self._CreateTime = None

    @property
    def ImageID(self):
        r"""<p>镜像id</p>
        :rtype: str
        """
        return self._ImageID

    @ImageID.setter
    def ImageID(self, ImageID):
        self._ImageID = ImageID

    @property
    def ImageName(self):
        r"""<p>镜像名称</p>
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageType(self):
        r"""<p>镜像类型：<br>PUBLIC_IMAGE-公共镜像<br>PRIVATE_IMAGE-自定义镜像<br>TENCENT_OFFICE_IMAGE-腾讯办公镜像</p>
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageState(self):
        r"""<p>镜像状态：<br>CREATING-创建中<br>NORMAL-正常<br>CREATEFAILED-创建失败<br>USING-使用中<br>SYNCING-同步中<br>IMPORTING-导入中<br>IMPORTFAILED-导入失败<br>INVISIBLE-淘汰的镜像<br>DELETIING-删除中<br>DELETED-删除的</p>
        :rtype: str
        """
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def OsName(self):
        r"""<p>镜像操作系统</p>
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageSize(self):
        r"""<p>镜像大小（单位G）</p>
        :rtype: int
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def Description(self):
        r"""<p>镜像描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        r"""<p>镜像所在区域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CoreType(self):
        r"""<p>内核类型：<br>CPU<br>GPU<br>GPU_A10<br>GPU_RTX6000<br>GPU_2080Ti<br>GPU_3080Ti</p>
        :rtype: str
        """
        return self._CoreType

    @CoreType.setter
    def CoreType(self, CoreType):
        self._CoreType = CoreType

    @property
    def CvmImageId(self):
        r"""<p>cvm侧镜像id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CvmImageId

    @CvmImageId.setter
    def CvmImageId(self, CvmImageId):
        self._CvmImageId = CvmImageId

    @property
    def IsWhole(self):
        r"""<p>是否是整机镜像，整机镜像无法用于桌面重置<br>true：整机镜像<br>false: 不是整机镜像</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsWhole

    @IsWhole.setter
    def IsWhole(self, IsWhole):
        self._IsWhole = IsWhole

    @property
    def DataDiskSize(self):
        r"""<p>整机镜像中数据盘大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def CreateTime(self):
        r"""<p>镜像创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ImageID = params.get("ImageID")
        self._ImageName = params.get("ImageName")
        self._ImageType = params.get("ImageType")
        self._ImageState = params.get("ImageState")
        self._OsName = params.get("OsName")
        self._ImageSize = params.get("ImageSize")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._CoreType = params.get("CoreType")
        self._CvmImageId = params.get("CvmImageId")
        self._IsWhole = params.get("IsWhole")
        self._DataDiskSize = params.get("DataDiskSize")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    r"""实例维度组合数组

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例的维度组合

        :type Dimensions: list of Dimension
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        r"""实例的维度组合

        :rtype: list of Dimension
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    r"""云桌面实例详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例id</p>
        :type InstanceId: str
        :param _Name: <p>实例名称</p>
        :type Name: str
        :param _Status: <p>实例状态<br>PENDING：表示创建中<br>LAUNCH_FAILED：表示创建失败<br>RUNNING：表示运行中<br>STOPPED：表示关机<br>STARTING：表示开机中<br>STOPPING：表示关机中<br>REBOOTING：表示重启中<br>SHUTDOWN：表示停止待销毁<br>TERMINATING：表示销毁中<br>DELETED：表示资源已经销毁，这个状态是业务层面的状态，cvm如果销毁了，在cvm侧资源已经不存在了<br>FAILED：表示资源创建失败.这个是业务层面的状态<br>ROLLBACKING：表示回滚中<br>USING：表示使用中<br>RESETTING：表示重置中.</p>
        :type Status: str
        :param _UserName: <p>实例拥有者名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _UserId: <p>实例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _InstanceType: <p>实例规格<br>S1.LARGE8：4VCPU 2.5GHZ主频 8G内存 无显卡<br>S1.LARGE16：4VCPU 2.5GHZ主频 16G内存 无显卡<br>S2.2XLARGE16：8VCPU 3.2GHZ主频 16G内存 无显卡<br>G1.LARGE16：4VCPU 2.5GHZ主频 16G内存 1/4 NVIDIA T4<br>G1.2XLARGE32：8VCPU 2.5GHZ主频 32G内存 1/2 NVIDIA T4<br>G1.4XLARGE64：16VCPU 2.5GHZ主频 64G内存 1 NVIDIA T4</p>
        :type InstanceType: str
        :param _SysDisk: <p>系统盘信息</p>
        :type SysDisk: :class:`tencentcloud.cvd.v20201104.models.Disk`
        :param _DataDiskList: <p>挂载的数据盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskList: list of Disk
        :param _Region: <p>桌面实例所在的区域</p>
        :type Region: str
        :param _ChargeType: <p>桌面计费类型</p>
        :type ChargeType: str
        :param _AutoRenewFlag: <p>自动续费标识。取值范围：<br>NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费<br>NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费<br>DISABLE_NOTIFY_AND_MANUAL_RENEW：表示不通知即将过期，也不自动续费。</p><p>注意：后付费模式本项为null</p>
        :type AutoRenewFlag: str
        :param _CreateTime: <p>桌面创建时间</p>
        :type CreateTime: str
        :param _ExpiredTime: <p>桌面过期时间</p>
        :type ExpiredTime: str
        :param _Description: <p>桌面描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _HostName: <p>桌面hostname</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _DisplayName: <p>桌面拥有者显示名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _BindStatus: <p>桌面绑定状态。取值：<br>UNBOUND - 未绑定<br>BINDING - 绑定中<br>BOUND - 绑定</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BindStatus: str
        :param _ImageId: <p>创建桌面的镜像id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _UserVpcId: <p>用户桌面vpc id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVpcId: str
        :param _UserSubnetId: <p>用户桌面子网 id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubnetId: str
        :param _UserPrivateIp: <p>用户桌面ip</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserPrivateIp: str
        :param _IsolatedTime: <p>机器回收站到期时间，只有机器状态为SHUTDOWN该值才有意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _LastStatusChangeReason: <p>最近一次状态变更原因, AUTO:被动变更,如欠费,如包月实例到期, MANUAL:主动变更,如主动退还实例，当前只有机器处于ISOLATING、SHUTDOWN、TERMINATING、DELETED该字段有意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LastStatusChangeReason: str
        :param _LatestOperation: <p>机器最近一次操作</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param _LatestOperationState: <p>机器最近一次操作状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param _LatestOperationRequestID: <p>机器最近一次操作请求ReqId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationRequestID: str
        :param _OsName: <p>机器操作系统名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param _SetId: <p>实例逻辑set</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: str
        :param _AppId: <p>应用id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: <p>账号id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SecurityGroups: <p>关联的安全组ID列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param _DownGradeTimes: <p>预付费实例降配次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DownGradeTimes: int
        :param _DomainControlPolicies: <p>桌面绑定的域名策略ID列表，最多五个</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainControlPolicies: list of str
        :param _WaterMarkPolicy: <p>桌面绑定的水印策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterMarkPolicy: str
        :param _ScreenRecordingPolicy: <p>桌面绑定的录屏策略ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ScreenRecordingPolicy: str
        :param _DomainControlPolicyType: <p>WHITE --- 白名单策略<br>BLACK --- 黑名单策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainControlPolicyType: str
        :param _RunControlPolicy: <p>桌面绑定的运行管控策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RunControlPolicy: str
        :param _InstallControlPolicy: <p>桌面绑定的安装管控策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstallControlPolicy: str
        :param _AnonymousAccess: <p>桌面是否绑定匿名用户</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AnonymousAccess: bool
        :param _Tags: <p>实例绑定的标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._InstanceId = None
        self._Name = None
        self._Status = None
        self._UserName = None
        self._UserId = None
        self._InstanceType = None
        self._SysDisk = None
        self._DataDiskList = None
        self._Region = None
        self._ChargeType = None
        self._AutoRenewFlag = None
        self._CreateTime = None
        self._ExpiredTime = None
        self._Description = None
        self._HostName = None
        self._DisplayName = None
        self._BindStatus = None
        self._ImageId = None
        self._UserVpcId = None
        self._UserSubnetId = None
        self._UserPrivateIp = None
        self._IsolatedTime = None
        self._LastStatusChangeReason = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestID = None
        self._OsName = None
        self._SetId = None
        self._AppId = None
        self._Uin = None
        self._SecurityGroups = None
        self._DownGradeTimes = None
        self._DomainControlPolicies = None
        self._WaterMarkPolicy = None
        self._ScreenRecordingPolicy = None
        self._DomainControlPolicyType = None
        self._RunControlPolicy = None
        self._InstallControlPolicy = None
        self._AnonymousAccess = None
        self._Tags = None

    @property
    def InstanceId(self):
        r"""<p>实例id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""<p>实例名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>实例状态<br>PENDING：表示创建中<br>LAUNCH_FAILED：表示创建失败<br>RUNNING：表示运行中<br>STOPPED：表示关机<br>STARTING：表示开机中<br>STOPPING：表示关机中<br>REBOOTING：表示重启中<br>SHUTDOWN：表示停止待销毁<br>TERMINATING：表示销毁中<br>DELETED：表示资源已经销毁，这个状态是业务层面的状态，cvm如果销毁了，在cvm侧资源已经不存在了<br>FAILED：表示资源创建失败.这个是业务层面的状态<br>ROLLBACKING：表示回滚中<br>USING：表示使用中<br>RESETTING：表示重置中.</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        r"""<p>实例拥有者名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        r"""<p>实例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def InstanceType(self):
        r"""<p>实例规格<br>S1.LARGE8：4VCPU 2.5GHZ主频 8G内存 无显卡<br>S1.LARGE16：4VCPU 2.5GHZ主频 16G内存 无显卡<br>S2.2XLARGE16：8VCPU 3.2GHZ主频 16G内存 无显卡<br>G1.LARGE16：4VCPU 2.5GHZ主频 16G内存 1/4 NVIDIA T4<br>G1.2XLARGE32：8VCPU 2.5GHZ主频 32G内存 1/2 NVIDIA T4<br>G1.4XLARGE64：16VCPU 2.5GHZ主频 64G内存 1 NVIDIA T4</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SysDisk(self):
        r"""<p>系统盘信息</p>
        :rtype: :class:`tencentcloud.cvd.v20201104.models.Disk`
        """
        return self._SysDisk

    @SysDisk.setter
    def SysDisk(self, SysDisk):
        self._SysDisk = SysDisk

    @property
    def DataDiskList(self):
        r"""<p>挂载的数据盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Disk
        """
        return self._DataDiskList

    @DataDiskList.setter
    def DataDiskList(self, DataDiskList):
        self._DataDiskList = DataDiskList

    @property
    def Region(self):
        r"""<p>桌面实例所在的区域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ChargeType(self):
        r"""<p>桌面计费类型</p>
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def AutoRenewFlag(self):
        r"""<p>自动续费标识。取值范围：<br>NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费<br>NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费<br>DISABLE_NOTIFY_AND_MANUAL_RENEW：表示不通知即将过期，也不自动续费。</p><p>注意：后付费模式本项为null</p>
        :rtype: str
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CreateTime(self):
        r"""<p>桌面创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpiredTime(self):
        r"""<p>桌面过期时间</p>
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Description(self):
        r"""<p>桌面描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def HostName(self):
        r"""<p>桌面hostname</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def DisplayName(self):
        r"""<p>桌面拥有者显示名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def BindStatus(self):
        r"""<p>桌面绑定状态。取值：<br>UNBOUND - 未绑定<br>BINDING - 绑定中<br>BOUND - 绑定</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ImageId(self):
        r"""<p>创建桌面的镜像id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def UserVpcId(self):
        r"""<p>用户桌面vpc id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserVpcId

    @UserVpcId.setter
    def UserVpcId(self, UserVpcId):
        self._UserVpcId = UserVpcId

    @property
    def UserSubnetId(self):
        r"""<p>用户桌面子网 id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def UserPrivateIp(self):
        r"""<p>用户桌面ip</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserPrivateIp

    @UserPrivateIp.setter
    def UserPrivateIp(self, UserPrivateIp):
        self._UserPrivateIp = UserPrivateIp

    @property
    def IsolatedTime(self):
        r"""<p>机器回收站到期时间，只有机器状态为SHUTDOWN该值才有意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def LastStatusChangeReason(self):
        r"""<p>最近一次状态变更原因, AUTO:被动变更,如欠费,如包月实例到期, MANUAL:主动变更,如主动退还实例，当前只有机器处于ISOLATING、SHUTDOWN、TERMINATING、DELETED该字段有意义</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastStatusChangeReason

    @LastStatusChangeReason.setter
    def LastStatusChangeReason(self, LastStatusChangeReason):
        self._LastStatusChangeReason = LastStatusChangeReason

    @property
    def LatestOperation(self):
        r"""<p>机器最近一次操作</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""<p>机器最近一次操作状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestID(self):
        r"""<p>机器最近一次操作请求ReqId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationRequestID

    @LatestOperationRequestID.setter
    def LatestOperationRequestID(self, LatestOperationRequestID):
        self._LatestOperationRequestID = LatestOperationRequestID

    @property
    def OsName(self):
        r"""<p>机器操作系统名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def SetId(self):
        r"""<p>实例逻辑set</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def AppId(self):
        r"""<p>应用id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""<p>账号id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SecurityGroups(self):
        r"""<p>关联的安全组ID列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def DownGradeTimes(self):
        r"""<p>预付费实例降配次数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DownGradeTimes

    @DownGradeTimes.setter
    def DownGradeTimes(self, DownGradeTimes):
        self._DownGradeTimes = DownGradeTimes

    @property
    def DomainControlPolicies(self):
        r"""<p>桌面绑定的域名策略ID列表，最多五个</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DomainControlPolicies

    @DomainControlPolicies.setter
    def DomainControlPolicies(self, DomainControlPolicies):
        self._DomainControlPolicies = DomainControlPolicies

    @property
    def WaterMarkPolicy(self):
        r"""<p>桌面绑定的水印策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaterMarkPolicy

    @WaterMarkPolicy.setter
    def WaterMarkPolicy(self, WaterMarkPolicy):
        self._WaterMarkPolicy = WaterMarkPolicy

    @property
    def ScreenRecordingPolicy(self):
        r"""<p>桌面绑定的录屏策略ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScreenRecordingPolicy

    @ScreenRecordingPolicy.setter
    def ScreenRecordingPolicy(self, ScreenRecordingPolicy):
        self._ScreenRecordingPolicy = ScreenRecordingPolicy

    @property
    def DomainControlPolicyType(self):
        r"""<p>WHITE --- 白名单策略<br>BLACK --- 黑名单策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DomainControlPolicyType

    @DomainControlPolicyType.setter
    def DomainControlPolicyType(self, DomainControlPolicyType):
        self._DomainControlPolicyType = DomainControlPolicyType

    @property
    def RunControlPolicy(self):
        r"""<p>桌面绑定的运行管控策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunControlPolicy

    @RunControlPolicy.setter
    def RunControlPolicy(self, RunControlPolicy):
        self._RunControlPolicy = RunControlPolicy

    @property
    def InstallControlPolicy(self):
        r"""<p>桌面绑定的安装管控策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstallControlPolicy

    @InstallControlPolicy.setter
    def InstallControlPolicy(self, InstallControlPolicy):
        self._InstallControlPolicy = InstallControlPolicy

    @property
    def AnonymousAccess(self):
        r"""<p>桌面是否绑定匿名用户</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AnonymousAccess

    @AnonymousAccess.setter
    def AnonymousAccess(self, AnonymousAccess):
        self._AnonymousAccess = AnonymousAccess

    @property
    def Tags(self):
        r"""<p>实例绑定的标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        self._InstanceType = params.get("InstanceType")
        if params.get("SysDisk") is not None:
            self._SysDisk = Disk()
            self._SysDisk._deserialize(params.get("SysDisk"))
        if params.get("DataDiskList") is not None:
            self._DataDiskList = []
            for item in params.get("DataDiskList"):
                obj = Disk()
                obj._deserialize(item)
                self._DataDiskList.append(obj)
        self._Region = params.get("Region")
        self._ChargeType = params.get("ChargeType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CreateTime = params.get("CreateTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Description = params.get("Description")
        self._HostName = params.get("HostName")
        self._DisplayName = params.get("DisplayName")
        self._BindStatus = params.get("BindStatus")
        self._ImageId = params.get("ImageId")
        self._UserVpcId = params.get("UserVpcId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._UserPrivateIp = params.get("UserPrivateIp")
        self._IsolatedTime = params.get("IsolatedTime")
        self._LastStatusChangeReason = params.get("LastStatusChangeReason")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestID = params.get("LatestOperationRequestID")
        self._OsName = params.get("OsName")
        self._SetId = params.get("SetId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SecurityGroups = params.get("SecurityGroups")
        self._DownGradeTimes = params.get("DownGradeTimes")
        self._DomainControlPolicies = params.get("DomainControlPolicies")
        self._WaterMarkPolicy = params.get("WaterMarkPolicy")
        self._ScreenRecordingPolicy = params.get("ScreenRecordingPolicy")
        self._DomainControlPolicyType = params.get("DomainControlPolicyType")
        self._RunControlPolicy = params.get("RunControlPolicy")
        self._InstallControlPolicy = params.get("InstallControlPolicy")
        self._AnonymousAccess = params.get("AnonymousAccess")
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
        


class InstanceStatus(AbstractModel):
    r"""实例状态

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Status: 实例状态
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中
DELETED：表示资源已经销毁，这个状态是业务层面的状态，cvm如果销毁了，在cvm测资源已经不存在了
FAILED：表示资源创建失败.这个是业务层面的状态
ROLLBACKING：表示机器正在回滚中
RESETTING：表示机器正在重置中
USING：表示机器正在使用中
        :type Status: str
        :param _SessionState: 只有在Status为RUNNING时候，当前值才有意义
取值范围：
0:Unknown
1:Connected 
2:Disconnected 
3:Terminated
4:PreparingSession
5:Active
6:Reconnecting
7:NonBrokeredSession
8:Other
9:Pending
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionState: int
        :param _IdleSeconds: 此字段只有在Status为USING时，才有效。
字段意义：表示桌面当前session空闲时间（客户没有鼠标，键盘等操作），单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleSeconds: float
        :param _StatusChangeTime: 当前状态改变的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusChangeTime: int
        :param _LatestOperation: 实例最近一次操作类型
        :type LatestOperation: str
        :param _LatestOperationState: 实例最近一次操作状态
        :type LatestOperationState: str
        """
        self._InstanceId = None
        self._Status = None
        self._SessionState = None
        self._IdleSeconds = None
        self._StatusChangeTime = None
        self._LatestOperation = None
        self._LatestOperationState = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        r"""实例状态
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中
DELETED：表示资源已经销毁，这个状态是业务层面的状态，cvm如果销毁了，在cvm测资源已经不存在了
FAILED：表示资源创建失败.这个是业务层面的状态
ROLLBACKING：表示机器正在回滚中
RESETTING：表示机器正在重置中
USING：表示机器正在使用中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SessionState(self):
        r"""只有在Status为RUNNING时候，当前值才有意义
取值范围：
0:Unknown
1:Connected 
2:Disconnected 
3:Terminated
4:PreparingSession
5:Active
6:Reconnecting
7:NonBrokeredSession
8:Other
9:Pending
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SessionState

    @SessionState.setter
    def SessionState(self, SessionState):
        self._SessionState = SessionState

    @property
    def IdleSeconds(self):
        r"""此字段只有在Status为USING时，才有效。
字段意义：表示桌面当前session空闲时间（客户没有鼠标，键盘等操作），单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._IdleSeconds

    @IdleSeconds.setter
    def IdleSeconds(self, IdleSeconds):
        self._IdleSeconds = IdleSeconds

    @property
    def StatusChangeTime(self):
        r"""当前状态改变的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StatusChangeTime

    @StatusChangeTime.setter
    def StatusChangeTime(self, StatusChangeTime):
        self._StatusChangeTime = StatusChangeTime

    @property
    def LatestOperation(self):
        r"""实例最近一次操作类型
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""实例最近一次操作状态
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._SessionState = params.get("SessionState")
        self._IdleSeconds = params.get("IdleSeconds")
        self._StatusChangeTime = params.get("StatusChangeTime")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invocation(AbstractModel):
    r"""脚本执行情况。

    """

    def __init__(self):
        r"""
        :param _InvokeId: <p>脚本执行ID。</p>
        :type InvokeId: str
        :param _Status: <p>运行状态。<li> Running：正在执行</li> <li>Finished：已经完成</li> <li>Failed：失败</li>  <li> Stopped：已停止</li></p>
        :type Status: str
        :param _Output: <p>任务输出。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.cvd.v20201104.models.InvocationOutput`
        :param _ErrorCode: <p>任务失败时的错误码。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _ErrorInfo: <p>任务失败时的错误信息描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: str
        :param _ExitCode: <p>任务退出状态码</p>
        :type ExitCode: int
        """
        self._InvokeId = None
        self._Status = None
        self._Output = None
        self._ErrorCode = None
        self._ErrorInfo = None
        self._ExitCode = None

    @property
    def InvokeId(self):
        r"""<p>脚本执行ID。</p>
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId

    @property
    def Status(self):
        r"""<p>运行状态。<li> Running：正在执行</li> <li>Finished：已经完成</li> <li>Failed：失败</li>  <li> Stopped：已停止</li></p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
        r"""<p>任务输出。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cvd.v20201104.models.InvocationOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ErrorCode(self):
        r"""<p>任务失败时的错误码。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        r"""<p>任务失败时的错误信息描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def ExitCode(self):
        r"""<p>任务退出状态码</p>
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode


    def _deserialize(self, params):
        self._InvokeId = params.get("InvokeId")
        self._Status = params.get("Status")
        if params.get("Output") is not None:
            self._Output = InvocationOutput()
            self._Output._deserialize(params.get("Output"))
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        self._ExitCode = params.get("ExitCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationDetail(AbstractModel):
    r"""实例执行脚本任务结果详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Region: 实例所在区域，目前支持的区域有：ap-beijing、ap-shanghai、ap-guangzhou、ap-shanghai-adc
        :type Region: str
        :param _Status: 脚本任务执行状态，取值有：
Running-执行中
Finished-完成
Failed-失败
Stopped-终止
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _InvokeId: 实例上任务唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeId: str
        :param _Output: 脚本任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _ExitCode: 任务退出码
注意：此字段可能返回 null，表示取不到有效值。
        :type ExitCode: int
        :param _ErrorCode: 任务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _ErrorInfo: 执行任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Status = None
        self._InvokeId = None
        self._Output = None
        self._ExitCode = None
        self._ErrorCode = None
        self._ErrorInfo = None

    @property
    def InstanceId(self):
        r"""实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""实例所在区域，目前支持的区域有：ap-beijing、ap-shanghai、ap-guangzhou、ap-shanghai-adc
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        r"""脚本任务执行状态，取值有：
Running-执行中
Finished-完成
Failed-失败
Stopped-终止
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InvokeId(self):
        r"""实例上任务唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId

    @property
    def Output(self):
        r"""脚本任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ExitCode(self):
        r"""任务退出码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def ErrorCode(self):
        r"""任务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        r"""执行任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._InvokeId = params.get("InvokeId")
        self._Output = params.get("Output")
        self._ExitCode = params.get("ExitCode")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationOutput(AbstractModel):
    r"""任务执行的标准输出。

    """

    def __init__(self):
        r"""
        :param _Lines: <p>任务的标准输出。</p>
        :type Lines: list of str
        :param _LinesOffset: <p>本次返回的输出第一行对应的索引编号。</p>
        :type LinesOffset: int
        :param _LinesNum: <p>本次返回的输出的行数。</p>
        :type LinesNum: int
        :param _Encoding: <p>输出的编码方式：<br>&lt;li&gt;PlainText 未经过Base64编码。</p>
        :type Encoding: str
        :param _AllLinesOffset: <p>当前有效的输出起始编号，从0开始。输出过多，会冲掉旧的输出。</p>
        :type AllLinesOffset: int
        :param _AllLinesNum: <p>当前有效的标准输出总行数。</p>
        :type AllLinesNum: int
        """
        self._Lines = None
        self._LinesOffset = None
        self._LinesNum = None
        self._Encoding = None
        self._AllLinesOffset = None
        self._AllLinesNum = None

    @property
    def Lines(self):
        r"""<p>任务的标准输出。</p>
        :rtype: list of str
        """
        return self._Lines

    @Lines.setter
    def Lines(self, Lines):
        self._Lines = Lines

    @property
    def LinesOffset(self):
        r"""<p>本次返回的输出第一行对应的索引编号。</p>
        :rtype: int
        """
        return self._LinesOffset

    @LinesOffset.setter
    def LinesOffset(self, LinesOffset):
        self._LinesOffset = LinesOffset

    @property
    def LinesNum(self):
        r"""<p>本次返回的输出的行数。</p>
        :rtype: int
        """
        return self._LinesNum

    @LinesNum.setter
    def LinesNum(self, LinesNum):
        self._LinesNum = LinesNum

    @property
    def Encoding(self):
        r"""<p>输出的编码方式：<br>&lt;li&gt;PlainText 未经过Base64编码。</p>
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def AllLinesOffset(self):
        r"""<p>当前有效的输出起始编号，从0开始。输出过多，会冲掉旧的输出。</p>
        :rtype: int
        """
        return self._AllLinesOffset

    @AllLinesOffset.setter
    def AllLinesOffset(self, AllLinesOffset):
        self._AllLinesOffset = AllLinesOffset

    @property
    def AllLinesNum(self):
        r"""<p>当前有效的标准输出总行数。</p>
        :rtype: int
        """
        return self._AllLinesNum

    @AllLinesNum.setter
    def AllLinesNum(self, AllLinesNum):
        self._AllLinesNum = AllLinesNum


    def _deserialize(self, params):
        self._Lines = params.get("Lines")
        self._LinesOffset = params.get("LinesOffset")
        self._LinesNum = params.get("LinesNum")
        self._Encoding = params.get("Encoding")
        self._AllLinesOffset = params.get("AllLinesOffset")
        self._AllLinesNum = params.get("AllLinesNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpControlDetail(AbstractModel):
    r"""IP控制策略详情

    """

    def __init__(self):
        r"""
        :param _Ip: <p>配置的IP。支持单IP和CIDR，暂不支持IP范围</p>
        :type Ip: str
        :param _Description: <p>IP的描述</p>
        :type Description: str
        """
        self._Ip = None
        self._Description = None

    @property
    def Ip(self):
        r"""<p>配置的IP。支持单IP和CIDR，暂不支持IP范围</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Description(self):
        r"""<p>IP的描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskConfigurationRequest(AbstractModel):
    r"""ModifyDiskConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _NewSystemDisk: <p>新系统盘配置</p>
        :type NewSystemDisk: :class:`tencentcloud.cvd.v20201104.models.Disk`
        :param _NewDataDisks: <p>新数据盘配置</p>
        :type NewDataDisks: list of Disk
        """
        self._InstanceId = None
        self._NewSystemDisk = None
        self._NewDataDisks = None

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewSystemDisk(self):
        r"""<p>新系统盘配置</p>
        :rtype: :class:`tencentcloud.cvd.v20201104.models.Disk`
        """
        return self._NewSystemDisk

    @NewSystemDisk.setter
    def NewSystemDisk(self, NewSystemDisk):
        self._NewSystemDisk = NewSystemDisk

    @property
    def NewDataDisks(self):
        r"""<p>新数据盘配置</p>
        :rtype: list of Disk
        """
        return self._NewDataDisks

    @NewDataDisks.setter
    def NewDataDisks(self, NewDataDisks):
        self._NewDataDisks = NewDataDisks


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("NewSystemDisk") is not None:
            self._NewSystemDisk = Disk()
            self._NewSystemDisk._deserialize(params.get("NewSystemDisk"))
        if params.get("NewDataDisks") is not None:
            self._NewDataDisks = []
            for item in params.get("NewDataDisks"):
                obj = Disk()
                obj._deserialize(item)
                self._NewDataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskConfigurationResponse(AbstractModel):
    r"""ModifyDiskConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyImageAttrsRequest(AbstractModel):
    r"""ModifyImageAttrs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: <p>镜像id</p>
        :type ImageId: str
        :param _Attrs: <p>支持修改的属性列表为：{ImageName}</p>
        :type Attrs: list of AttributeInfo
        """
        self._ImageId = None
        self._Attrs = None

    @property
    def ImageId(self):
        r"""<p>镜像id</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Attrs(self):
        r"""<p>支持修改的属性列表为：{ImageName}</p>
        :rtype: list of AttributeInfo
        """
        return self._Attrs

    @Attrs.setter
    def Attrs(self, Attrs):
        self._Attrs = Attrs


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        if params.get("Attrs") is not None:
            self._Attrs = []
            for item in params.get("Attrs"):
                obj = AttributeInfo()
                obj._deserialize(item)
                self._Attrs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttrsResponse(AbstractModel):
    r"""ModifyImageAttrs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyInstanceBasicAttributeRequest(AbstractModel):
    r"""ModifyInstanceBasicAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云桌面实例id
        :type InstanceId: str
        :param _AttributeInfoList: 修改云桌面实例的属性信息
        :type AttributeInfoList: list of AttributeInfo
        """
        self._InstanceId = None
        self._AttributeInfoList = None

    @property
    def InstanceId(self):
        r"""云桌面实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttributeInfoList(self):
        r"""修改云桌面实例的属性信息
        :rtype: list of AttributeInfo
        """
        return self._AttributeInfoList

    @AttributeInfoList.setter
    def AttributeInfoList(self, AttributeInfoList):
        self._AttributeInfoList = AttributeInfoList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AttributeInfoList") is not None:
            self._AttributeInfoList = []
            for item in params.get("AttributeInfoList"):
                obj = AttributeInfo()
                obj._deserialize(item)
                self._AttributeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceBasicAttributeResponse(AbstractModel):
    r"""ModifyInstanceBasicAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyInstancesTypeRequest(AbstractModel):
    r"""ModifyInstancesType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>实例id数组</p>
        :type InstanceIds: list of str
        :param _InstanceType: <p>变更的实例类型</p>
        :type InstanceType: str
        :param _ChargeType: <p>付费类型</p>
        :type ChargeType: str
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ChargeType = None

    @property
    def InstanceIds(self):
        r"""<p>实例id数组</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        r"""<p>变更的实例类型</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ChargeType(self):
        r"""<p>付费类型</p>
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesTypeResponse(AbstractModel):
    r"""ModifyInstancesType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyInstancesVpcRequest(AbstractModel):
    r"""ModifyInstancesVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>实例ID数组</p>
        :type InstanceIds: list of str
        :param _VpcId: <p>私有网络ID</p>
        :type VpcId: str
        :param _SubnetId: <p>子网ID</p>
        :type SubnetId: str
        :param _DnsServerSet: <p>租户vpc的dns</p><p>参数格式：“189.0.01”</p>
        :type DnsServerSet: list of str
        """
        self._InstanceIds = None
        self._VpcId = None
        self._SubnetId = None
        self._DnsServerSet = None

    @property
    def InstanceIds(self):
        r"""<p>实例ID数组</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def VpcId(self):
        r"""<p>私有网络ID</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>子网ID</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DnsServerSet(self):
        r"""<p>租户vpc的dns</p><p>参数格式：“189.0.01”</p>
        :rtype: list of str
        """
        return self._DnsServerSet

    @DnsServerSet.setter
    def DnsServerSet(self, DnsServerSet):
        self._DnsServerSet = DnsServerSet


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DnsServerSet = params.get("DnsServerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesVpcResponse(AbstractModel):
    r"""ModifyInstancesVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Partition(AbstractModel):
    r"""磁盘分区数据

    """

    def __init__(self):
        r"""
        :param _Name: 磁盘名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Total: 总容量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: float
        :param _Usage: 使用量,39.31%
注意：此字段可能返回 null，表示取不到有效值。
        :type Usage: float
        """
        self._Name = None
        self._Total = None
        self._Usage = None

    @property
    def Name(self):
        r"""磁盘名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        r"""总容量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Usage(self):
        r"""使用量,39.31%
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyDetail(AbstractModel):
    r"""策略详细信息

    """

    def __init__(self):
        r"""
        :param _PolicyId: <p>策略id</p>
        :type PolicyId: str
        :param _PolicyName: <p>策略名称</p>
        :type PolicyName: str
        :param _Description: <p>策略描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _UserIds: <p>策略作用用户id列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of str
        :param _Uin: <p>策略的租户uin</p>
        :type Uin: str
        :param _FilePolicyId: <p>文件重定向策略id。取值范围：<br>1：读写<br>2：只读<br>3：禁止读写</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePolicyId: int
        :param _ClipPolicyId: <p>剪切板重定向策略id。取值范围：<br>1：开启云桌面到客户端<br>2：开启客户端到云桌面<br>3：双向开启<br>4：禁用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ClipPolicyId: int
        :param _DrivePolicyId: <p>外设重定向策略id。取值范围：<br>1：允许usb重定向<br>2：允许端口重定向<br>3：允许usb和端口重定向<br>4：禁用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DrivePolicyId: int
        :param _WaterMarkPolicyId: <p>水印重定向策略id。取值范围（离散值）：<br>4:   当前时间，居中策略<br>10: 当前时间，平铺策略<br>15:  云桌面ID， 居中策略<br>16:  云桌面ID+当前时间， 居中策略<br>17:  云桌面ID， 平铺策略<br>18:  云桌面ID+当前时间， 平铺策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterMarkPolicyId: int
        :param _IsDefault: <p>是否是默认策略</p>
        :type IsDefault: bool
        :param _TotalUser: <p>注意：默认策略的当前值无效</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUser: int
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Description = None
        self._UserIds = None
        self._Uin = None
        self._FilePolicyId = None
        self._ClipPolicyId = None
        self._DrivePolicyId = None
        self._WaterMarkPolicyId = None
        self._IsDefault = None
        self._TotalUser = None

    @property
    def PolicyId(self):
        r"""<p>策略id</p>
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""<p>策略名称</p>
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        r"""<p>策略描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserIds(self):
        r"""<p>策略作用用户id列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Uin(self):
        r"""<p>策略的租户uin</p>
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def FilePolicyId(self):
        r"""<p>文件重定向策略id。取值范围：<br>1：读写<br>2：只读<br>3：禁止读写</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FilePolicyId

    @FilePolicyId.setter
    def FilePolicyId(self, FilePolicyId):
        self._FilePolicyId = FilePolicyId

    @property
    def ClipPolicyId(self):
        r"""<p>剪切板重定向策略id。取值范围：<br>1：开启云桌面到客户端<br>2：开启客户端到云桌面<br>3：双向开启<br>4：禁用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClipPolicyId

    @ClipPolicyId.setter
    def ClipPolicyId(self, ClipPolicyId):
        self._ClipPolicyId = ClipPolicyId

    @property
    def DrivePolicyId(self):
        r"""<p>外设重定向策略id。取值范围：<br>1：允许usb重定向<br>2：允许端口重定向<br>3：允许usb和端口重定向<br>4：禁用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DrivePolicyId

    @DrivePolicyId.setter
    def DrivePolicyId(self, DrivePolicyId):
        self._DrivePolicyId = DrivePolicyId

    @property
    def WaterMarkPolicyId(self):
        r"""<p>水印重定向策略id。取值范围（离散值）：<br>4:   当前时间，居中策略<br>10: 当前时间，平铺策略<br>15:  云桌面ID， 居中策略<br>16:  云桌面ID+当前时间， 居中策略<br>17:  云桌面ID， 平铺策略<br>18:  云桌面ID+当前时间， 平铺策略</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WaterMarkPolicyId

    @WaterMarkPolicyId.setter
    def WaterMarkPolicyId(self, WaterMarkPolicyId):
        self._WaterMarkPolicyId = WaterMarkPolicyId

    @property
    def IsDefault(self):
        r"""<p>是否是默认策略</p>
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def TotalUser(self):
        r"""<p>注意：默认策略的当前值无效</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalUser

    @TotalUser.setter
    def TotalUser(self, TotalUser):
        self._TotalUser = TotalUser


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._UserIds = params.get("UserIds")
        self._Uin = params.get("Uin")
        self._FilePolicyId = params.get("FilePolicyId")
        self._ClipPolicyId = params.get("ClipPolicyId")
        self._DrivePolicyId = params.get("DrivePolicyId")
        self._WaterMarkPolicyId = params.get("WaterMarkPolicyId")
        self._IsDefault = params.get("IsDefault")
        self._TotalUser = params.get("TotalUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyInfo(AbstractModel):
    r"""创建策略详细信息

    """

    def __init__(self):
        r"""
        :param _PolicyType: 策略类型。取值：
1：文件重定向策略
2：剪切板重定向策略
3：外设重定向策略
4：水印策略
        :type PolicyType: int
        :param _PolicyValue: 策略值。取值：
PolicyType对应个子取值范围：
	①：PolicyType为1-文件重定向策略	
					1：读写
					2：只读
					3：禁止读写
	②：剪切板重定向策略
					1：开启云桌面到客户端
					2：开启客户端到云桌面
					3：双向开启
					4：禁用
	③：外设重定向策略
					1：允许usb重定向
					2：允许端口重定向
					3：允许usb和端口重定向
					4：禁用
	④：水印策略
					4:   当前时间，居中策略
					10: 当前时间，平铺策略
					15:  云桌面ID， 居中策略
                                        16:  云桌面ID+当前时间， 居中策略
                                        17:  云桌面ID， 平铺策略
                                        18:  云桌面ID+当前时间， 平铺策略
        :type PolicyValue: int
        """
        self._PolicyType = None
        self._PolicyValue = None

    @property
    def PolicyType(self):
        r"""策略类型。取值：
1：文件重定向策略
2：剪切板重定向策略
3：外设重定向策略
4：水印策略
        :rtype: int
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyValue(self):
        r"""策略值。取值：
PolicyType对应个子取值范围：
	①：PolicyType为1-文件重定向策略	
					1：读写
					2：只读
					3：禁止读写
	②：剪切板重定向策略
					1：开启云桌面到客户端
					2：开启客户端到云桌面
					3：双向开启
					4：禁用
	③：外设重定向策略
					1：允许usb重定向
					2：允许端口重定向
					3：允许usb和端口重定向
					4：禁用
	④：水印策略
					4:   当前时间，居中策略
					10: 当前时间，平铺策略
					15:  云桌面ID， 居中策略
                                        16:  云桌面ID+当前时间， 居中策略
                                        17:  云桌面ID， 平铺策略
                                        18:  云桌面ID+当前时间， 平铺策略
        :rtype: int
        """
        return self._PolicyValue

    @PolicyValue.setter
    def PolicyValue(self, PolicyValue):
        self._PolicyValue = PolicyValue


    def _deserialize(self, params):
        self._PolicyType = params.get("PolicyType")
        self._PolicyValue = params.get("PolicyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    r"""RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 重启实例id列表
        :type InstanceIds: list of str
        :param _InstanceRegion: 实例所在区域，保证传入的列表在统一区域，否则报错
        :type InstanceRegion: str
        :param _Force: 是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启
FALSE：表示在正常重启失败后不进行强制重启

默认取值：FALSE。
        :type Force: bool
        :param _PreLogin: 重启是否需要预登录
        :type PreLogin: bool
        """
        self._InstanceIds = None
        self._InstanceRegion = None
        self._Force = None
        self._PreLogin = None

    @property
    def InstanceIds(self):
        r"""重启实例id列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceRegion(self):
        r"""实例所在区域，保证传入的列表在统一区域，否则报错
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def Force(self):
        r"""是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启
FALSE：表示在正常重启失败后不进行强制重启

默认取值：FALSE。
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def PreLogin(self):
        r"""重启是否需要预登录
        :rtype: bool
        """
        return self._PreLogin

    @PreLogin.setter
    def PreLogin(self, PreLogin):
        self._PreLogin = PreLogin


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceRegion = params.get("InstanceRegion")
        self._Force = params.get("Force")
        self._PreLogin = params.get("PreLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    r"""RebootInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemoveDataDisksRequest(AbstractModel):
    r"""RemoveDataDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _DataDiskIds: 数据盘磁盘 ID，可以通过 DescribeInstances 查下实例数据盘
        :type DataDiskIds: list of str
        """
        self._InstanceId = None
        self._DataDiskIds = None

    @property
    def InstanceId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDiskIds(self):
        r"""数据盘磁盘 ID，可以通过 DescribeInstances 查下实例数据盘
        :rtype: list of str
        """
        return self._DataDiskIds

    @DataDiskIds.setter
    def DataDiskIds(self, DataDiskIds):
        self._DataDiskIds = DataDiskIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DataDiskIds = params.get("DataDiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDataDisksResponse(AbstractModel):
    r"""RemoveDataDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemovePolicyRequest(AbstractModel):
    r"""RemovePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: <p>待删除策略id</p>
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        r"""<p>待删除策略id</p>
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePolicyResponse(AbstractModel):
    r"""RemovePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RenewInstancesRequest(AbstractModel):
    r"""RenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。每次请求批量实例的上限为50。
        :type InstanceIds: list of str
        :param _ChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。包年包月实例该参数为必传参数。
        :type ChargePrepaid: :class:`tencentcloud.cvd.v20201104.models.ChargePrepaid`
        """
        self._InstanceIds = None
        self._ChargePrepaid = None

    @property
    def InstanceIds(self):
        r"""一个或多个待操作的实例ID。每次请求批量实例的上限为50。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。包年包月实例该参数为必传参数。
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ChargePrepaid`
        """
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaid()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesResponse(AbstractModel):
    r"""RenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    r"""ResetInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要重置的实例id列表
        :type InstanceIds: list of str
        :param _ImageId: 重置的目标镜像id
        :type ImageId: str
        :param _InstanceRegion: 重置实例的区域
        :type InstanceRegion: str
        :param _IsUnbind: 是否解绑机器原有绑定关系
        :type IsUnbind: bool
        """
        self._InstanceIds = None
        self._ImageId = None
        self._InstanceRegion = None
        self._IsUnbind = None

    @property
    def InstanceIds(self):
        r"""需要重置的实例id列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ImageId(self):
        r"""重置的目标镜像id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceRegion(self):
        r"""重置实例的区域
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def IsUnbind(self):
        r"""是否解绑机器原有绑定关系
        :rtype: bool
        """
        return self._IsUnbind

    @IsUnbind.setter
    def IsUnbind(self, IsUnbind):
        self._IsUnbind = IsUnbind


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ImageId = params.get("ImageId")
        self._InstanceRegion = params.get("InstanceRegion")
        self._IsUnbind = params.get("IsUnbind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesResponse(AbstractModel):
    r"""ResetInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunCommandRequest(AbstractModel):
    r"""RunCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>云桌面实例ID。</p>
        :type InstanceId: str
        :param _Content: <p>执行的脚本内容，编码方式由ContentEncoding指定。<br>&lt;li&gt;脚本内容在Base64编码后的大小不能超过16 KB。</p>
        :type Content: str
        :param _Type: <p>脚本种类。取值有：&lt;li&gt;PowerShellScript Powershell脚本 &lt;li&gt;BatScript Bat脚本</p>
        :type Type: str
        :param _WaitUntilDone: <p>是否同步等待脚本的执行结果。&lt;li&gt;false为异步模式，通过此接口触发任务的执行，之后异步获取执行结果。默认为false。此为推荐的模式。&lt;li&gt;true为同步等待执行结果，只有当脚本执行时间在4秒之内时，才适合将该参数置为true。如果接口返回时任务尚未执行完毕的话，也需要通过异步接口来获取执行结果。</p>
        :type WaitUntilDone: bool
        :param _ContentEncoding: <p>Content的编码。&lt;li&gt;Base64 Base64编码。 默认为Base64</p>
        :type ContentEncoding: str
        :param _MergeOutputLines: <p>任务的输出内容是否合并成一个字符串。&lt;li&gt;true表示所有的输出行拼接在一起。默认为true。&lt;li&gt;false表示输出内容通过数组返回,数组的每一个元素为一行。</p>
        :type MergeOutputLines: bool
        :param _RunAs: <p>执行任务的用户ID。&lt;li&gt;由SYSTEM身份执行。此场景下不需要指定该字段，这是默认情况。&lt;li&gt;需要以绑定到实例的用户执行任务，通过该字段指定用户ID。 &lt;li&gt;匿名访问，需要以实际登录系统的用户执行的场景，该字段填实例ID。</p>
        :type RunAs: str
        :param _RunForeground: <p>任务是否为前台运行。仅在RunAs场景下有效。仅当任务会呼起图形界面时有意义。&lt;li&gt;true表示用户可以看到图形窗口。&lt;li&gt;false表示图形窗口不可见。默认为false。</p>
        :type RunForeground: bool
        """
        self._InstanceId = None
        self._Content = None
        self._Type = None
        self._WaitUntilDone = None
        self._ContentEncoding = None
        self._MergeOutputLines = None
        self._RunAs = None
        self._RunForeground = None

    @property
    def InstanceId(self):
        r"""<p>云桌面实例ID。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Content(self):
        r"""<p>执行的脚本内容，编码方式由ContentEncoding指定。<br>&lt;li&gt;脚本内容在Base64编码后的大小不能超过16 KB。</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Type(self):
        r"""<p>脚本种类。取值有：&lt;li&gt;PowerShellScript Powershell脚本 &lt;li&gt;BatScript Bat脚本</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WaitUntilDone(self):
        r"""<p>是否同步等待脚本的执行结果。&lt;li&gt;false为异步模式，通过此接口触发任务的执行，之后异步获取执行结果。默认为false。此为推荐的模式。&lt;li&gt;true为同步等待执行结果，只有当脚本执行时间在4秒之内时，才适合将该参数置为true。如果接口返回时任务尚未执行完毕的话，也需要通过异步接口来获取执行结果。</p>
        :rtype: bool
        """
        return self._WaitUntilDone

    @WaitUntilDone.setter
    def WaitUntilDone(self, WaitUntilDone):
        self._WaitUntilDone = WaitUntilDone

    @property
    def ContentEncoding(self):
        r"""<p>Content的编码。&lt;li&gt;Base64 Base64编码。 默认为Base64</p>
        :rtype: str
        """
        return self._ContentEncoding

    @ContentEncoding.setter
    def ContentEncoding(self, ContentEncoding):
        self._ContentEncoding = ContentEncoding

    @property
    def MergeOutputLines(self):
        r"""<p>任务的输出内容是否合并成一个字符串。&lt;li&gt;true表示所有的输出行拼接在一起。默认为true。&lt;li&gt;false表示输出内容通过数组返回,数组的每一个元素为一行。</p>
        :rtype: bool
        """
        return self._MergeOutputLines

    @MergeOutputLines.setter
    def MergeOutputLines(self, MergeOutputLines):
        self._MergeOutputLines = MergeOutputLines

    @property
    def RunAs(self):
        r"""<p>执行任务的用户ID。&lt;li&gt;由SYSTEM身份执行。此场景下不需要指定该字段，这是默认情况。&lt;li&gt;需要以绑定到实例的用户执行任务，通过该字段指定用户ID。 &lt;li&gt;匿名访问，需要以实际登录系统的用户执行的场景，该字段填实例ID。</p>
        :rtype: str
        """
        return self._RunAs

    @RunAs.setter
    def RunAs(self, RunAs):
        self._RunAs = RunAs

    @property
    def RunForeground(self):
        r"""<p>任务是否为前台运行。仅在RunAs场景下有效。仅当任务会呼起图形界面时有意义。&lt;li&gt;true表示用户可以看到图形窗口。&lt;li&gt;false表示图形窗口不可见。默认为false。</p>
        :rtype: bool
        """
        return self._RunForeground

    @RunForeground.setter
    def RunForeground(self, RunForeground):
        self._RunForeground = RunForeground


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Content = params.get("Content")
        self._Type = params.get("Type")
        self._WaitUntilDone = params.get("WaitUntilDone")
        self._ContentEncoding = params.get("ContentEncoding")
        self._MergeOutputLines = params.get("MergeOutputLines")
        self._RunAs = params.get("RunAs")
        self._RunForeground = params.get("RunForeground")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandResponse(AbstractModel):
    r"""RunCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokeId: <p>本次任务对应的任务ID。方便异步查询执行状态。</p>
        :type InvokeId: str
        :param _Detail: <p>执行详细情况。WaitUntilDone为true，在接口返回时的执行状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.cvd.v20201104.models.Invocation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvokeId = None
        self._Detail = None
        self._RequestId = None

    @property
    def InvokeId(self):
        r"""<p>本次任务对应的任务ID。方便异步查询执行状态。</p>
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId

    @property
    def Detail(self):
        r"""<p>执行详细情况。WaitUntilDone为true，在接口返回时的执行状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cvd.v20201104.models.Invocation`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._InvokeId = params.get("InvokeId")
        if params.get("Detail") is not None:
            self._Detail = Invocation()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    r"""快照信息

    """

    def __init__(self):
        r"""
        :param _SnapshotId: <p>快照唯一ID</p>
        :type SnapshotId: str
        :param _DiskId: <p>快照对应的云硬盘ID</p>
        :type DiskId: str
        :param _SnapshotState: <p>快照状态，取值如下：<br>NORMAL：正常<br>CREATING：创建中<br>ROLLBACKING：回滚中<br>COPYING_FROM_REMOTE：跨地域复制中<br>CHECKING_COPIED：复制校验中<br>TORECYCLE：待回收。</p>
        :type SnapshotState: str
        :param _DiskUsage: <p>创建此快照的云硬盘类型。取值范围：<br>SYSTEM_DISK：系统盘<br>DATA_DISK：数据盘。</p>
        :type DiskUsage: str
        :param _CreateTime: <p>快照创建的时间</p>
        :type CreateTime: str
        :param _DeadlineTime: <p>快照到期时间。如果快照为永久保留，此字段为空。</p>
        :type DeadlineTime: str
        :param _Percent: <p>快照创建进度百分比，快照创建成功后此字段恒为100。</p>
        :type Percent: int
        :param _IsPermanent: <p>是否为永久快照。取值范围：<br>true：永久快照<br>false：非永久快照。</p>
        :type IsPermanent: bool
        :param _CreateType: <p>快照创建方式，取值:<br>ManualSnapshot：手动创建<br>AutoSnapshot：快照策略自动创建</p>
        :type CreateType: str
        :param _LastRollbackTime: <p>上一次快照回滚完成时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LastRollbackTime: str
        :param _LastRollbackState: <p>上一次快照回滚状态，取值：<br>成功：SUCCESS<br>失败：FAILED</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LastRollbackState: str
        """
        self._SnapshotId = None
        self._DiskId = None
        self._SnapshotState = None
        self._DiskUsage = None
        self._CreateTime = None
        self._DeadlineTime = None
        self._Percent = None
        self._IsPermanent = None
        self._CreateType = None
        self._LastRollbackTime = None
        self._LastRollbackState = None

    @property
    def SnapshotId(self):
        r"""<p>快照唯一ID</p>
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskId(self):
        r"""<p>快照对应的云硬盘ID</p>
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotState(self):
        r"""<p>快照状态，取值如下：<br>NORMAL：正常<br>CREATING：创建中<br>ROLLBACKING：回滚中<br>COPYING_FROM_REMOTE：跨地域复制中<br>CHECKING_COPIED：复制校验中<br>TORECYCLE：待回收。</p>
        :rtype: str
        """
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def DiskUsage(self):
        r"""<p>创建此快照的云硬盘类型。取值范围：<br>SYSTEM_DISK：系统盘<br>DATA_DISK：数据盘。</p>
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def CreateTime(self):
        r"""<p>快照创建的时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeadlineTime(self):
        r"""<p>快照到期时间。如果快照为永久保留，此字段为空。</p>
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Percent(self):
        r"""<p>快照创建进度百分比，快照创建成功后此字段恒为100。</p>
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def IsPermanent(self):
        r"""<p>是否为永久快照。取值范围：<br>true：永久快照<br>false：非永久快照。</p>
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def CreateType(self):
        r"""<p>快照创建方式，取值:<br>ManualSnapshot：手动创建<br>AutoSnapshot：快照策略自动创建</p>
        :rtype: str
        """
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def LastRollbackTime(self):
        r"""<p>上一次快照回滚完成时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastRollbackTime

    @LastRollbackTime.setter
    def LastRollbackTime(self, LastRollbackTime):
        self._LastRollbackTime = LastRollbackTime

    @property
    def LastRollbackState(self):
        r"""<p>上一次快照回滚状态，取值：<br>成功：SUCCESS<br>失败：FAILED</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastRollbackState

    @LastRollbackState.setter
    def LastRollbackState(self, LastRollbackState):
        self._LastRollbackState = LastRollbackState


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskId = params.get("DiskId")
        self._SnapshotState = params.get("SnapshotState")
        self._DiskUsage = params.get("DiskUsage")
        self._CreateTime = params.get("CreateTime")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Percent = params.get("Percent")
        self._IsPermanent = params.get("IsPermanent")
        self._CreateType = params.get("CreateType")
        self._LastRollbackTime = params.get("LastRollbackTime")
        self._LastRollbackState = params.get("LastRollbackState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    r"""StartInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要开启的实例id列表
        :type InstanceIds: list of str
        :param _InstanceRegion: 实例所在区域，保证传入的列表再统一区域，否则报错
        :type InstanceRegion: str
        """
        self._InstanceIds = None
        self._InstanceRegion = None

    @property
    def InstanceIds(self):
        r"""需要开启的实例id列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceRegion(self):
        r"""实例所在区域，保证传入的列表再统一区域，否则报错
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceRegion = params.get("InstanceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    r"""StartInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopCommandTasksRequest(AbstractModel):
    r"""StopCommandTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <p>删除命令任务条件<br>Filter.name 目前支持 CommandId</p>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""<p>删除命令任务条件<br>Filter.name 目前支持 CommandId</p>
        :rtype: list of Filter
        """
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
        


class StopCommandTasksResponse(AbstractModel):
    r"""StopCommandTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    r"""StopInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要重启的实例id列表
        :type InstanceIds: list of str
        :param _InstanceRegion: 实例所在区域，保证传入的列表在统一区域，否则报错
        :type InstanceRegion: str
        :param _Force: 是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启
FALSE：表示在正常重启失败后不进行强制重启

默认取值：FALSE。
        :type Force: bool
        """
        self._InstanceIds = None
        self._InstanceRegion = None
        self._Force = None

    @property
    def InstanceIds(self):
        r"""需要重启的实例id列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceRegion(self):
        r"""实例所在区域，保证传入的列表在统一区域，否则报错
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def Force(self):
        r"""是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启
FALSE：表示在正常重启失败后不进行强制重启

默认取值：FALSE。
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceRegion = params.get("InstanceRegion")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    r"""StopInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopInvocationRequest(AbstractModel):
    r"""StopInvocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>云桌面实例ID。</p>
        :type InstanceId: str
        :param _InvokeId: <p>任务ID。</p>
        :type InvokeId: str
        """
        self._InstanceId = None
        self._InvokeId = None

    @property
    def InstanceId(self):
        r"""<p>云桌面实例ID。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvokeId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InvokeId = params.get("InvokeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInvocationResponse(AbstractModel):
    r"""StopInvocation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopSessionRequest(AbstractModel):
    r"""StopSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceRegion: <p>机器所在区域</p>
        :type InstanceRegion: str
        :param _HostName: <p>机器hostname</p>
        :type HostName: str
        :param _IsDisconnect: <p>IsDisconnect为true，表示断开当前会话<br>IsDisconnect为false，表示注销当前会话</p>
        :type IsDisconnect: bool
        :param _UserId: <p>选填，为多会话预留字段</p>
        :type UserId: str
        """
        self._InstanceRegion = None
        self._HostName = None
        self._IsDisconnect = None
        self._UserId = None

    @property
    def InstanceRegion(self):
        r"""<p>机器所在区域</p>
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def HostName(self):
        r"""<p>机器hostname</p>
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def IsDisconnect(self):
        r"""<p>IsDisconnect为true，表示断开当前会话<br>IsDisconnect为false，表示注销当前会话</p>
        :rtype: bool
        """
        return self._IsDisconnect

    @IsDisconnect.setter
    def IsDisconnect(self, IsDisconnect):
        self._IsDisconnect = IsDisconnect

    @property
    def UserId(self):
        r"""<p>选填，为多会话预留字段</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._InstanceRegion = params.get("InstanceRegion")
        self._HostName = params.get("HostName")
        self._IsDisconnect = params.get("IsDisconnect")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSessionResponse(AbstractModel):
    r"""StopSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""Tag

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
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
        


class TerminateInstancesRequest(AbstractModel):
    r"""TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>一个或多个待操作的实例ID。每次请求批量实例的上限为10。</p>
        :type InstanceIds: list of str
        :param _DestroyImmediately: <p>是否立即销毁实例。默认false。 立即销毁的实例不会进入隔离期。</p>
        :type DestroyImmediately: bool
        """
        self._InstanceIds = None
        self._DestroyImmediately = None

    @property
    def InstanceIds(self):
        r"""<p>一个或多个待操作的实例ID。每次请求批量实例的上限为10。</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DestroyImmediately(self):
        r"""<p>是否立即销毁实例。默认false。 立即销毁的实例不会进入隔离期。</p>
        :rtype: bool
        """
        return self._DestroyImmediately

    @DestroyImmediately.setter
    def DestroyImmediately(self, DestroyImmediately):
        self._DestroyImmediately = DestroyImmediately


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._DestroyImmediately = params.get("DestroyImmediately")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    r"""TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UnbindInstancesRequest(AbstractModel):
    r"""UnbindInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceRegion: 实例所在地域
        :type InstanceRegion: str
        :param _BindInfos: 解除绑定关系列表
        :type BindInfos: list of BindInfo
        """
        self._InstanceRegion = None
        self._BindInfos = None

    @property
    def InstanceRegion(self):
        r"""实例所在地域
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def BindInfos(self):
        r"""解除绑定关系列表
        :rtype: list of BindInfo
        """
        return self._BindInfos

    @BindInfos.setter
    def BindInfos(self, BindInfos):
        self._BindInfos = BindInfos


    def _deserialize(self, params):
        self._InstanceRegion = params.get("InstanceRegion")
        if params.get("BindInfos") is not None:
            self._BindInfos = []
            for item in params.get("BindInfos"):
                obj = BindInfo()
                obj._deserialize(item)
                self._BindInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindInstancesResponse(AbstractModel):
    r"""UnbindInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    r"""UpdatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: <p>待更新策略id</p>
        :type PolicyId: str
        :param _Name: <p>更新策略后策略名称</p>
        :type Name: str
        :param _Description: <p>更新策略后策略描述</p>
        :type Description: str
        :param _PolicyInfoList: <p>更新策略的具体修改值（全集）</p>
        :type PolicyInfoList: list of PolicyInfo
        :param _BindUserIds: <p>新增绑定用户列表</p>
        :type BindUserIds: list of str
        :param _RemoveUserIds: <p>移除绑定的用户列表</p>
        :type RemoveUserIds: list of str
        """
        self._PolicyId = None
        self._Name = None
        self._Description = None
        self._PolicyInfoList = None
        self._BindUserIds = None
        self._RemoveUserIds = None

    @property
    def PolicyId(self):
        r"""<p>待更新策略id</p>
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Name(self):
        r"""<p>更新策略后策略名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>更新策略后策略描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PolicyInfoList(self):
        r"""<p>更新策略的具体修改值（全集）</p>
        :rtype: list of PolicyInfo
        """
        return self._PolicyInfoList

    @PolicyInfoList.setter
    def PolicyInfoList(self, PolicyInfoList):
        self._PolicyInfoList = PolicyInfoList

    @property
    def BindUserIds(self):
        r"""<p>新增绑定用户列表</p>
        :rtype: list of str
        """
        return self._BindUserIds

    @BindUserIds.setter
    def BindUserIds(self, BindUserIds):
        self._BindUserIds = BindUserIds

    @property
    def RemoveUserIds(self):
        r"""<p>移除绑定的用户列表</p>
        :rtype: list of str
        """
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("PolicyInfoList") is not None:
            self._PolicyInfoList = []
            for item in params.get("PolicyInfoList"):
                obj = PolicyInfo()
                obj._deserialize(item)
                self._PolicyInfoList.append(obj)
        self._BindUserIds = params.get("BindUserIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    r"""UpdatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Usage(AbstractModel):
    r"""桌面使用时长详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 桌面实例 ID
        :type InstanceId: str
        :param _Name: 桌面名称
        :type Name: str
        :param _Status: 桌面当前状态
        :type Status: str
        :param _UserName: 桌面绑定的用户名，若未绑定，为空
        :type UserName: str
        :param _ChargeType: 桌面计费类型
        :type ChargeType: str
        :param _InstanceType: 桌面类型
        :type InstanceType: str
        :param _OsName: 桌面操作系统
        :type OsName: str
        :param _ActiveTime: 桌面使用时长，h:m:s
        :type ActiveTime: str
        :param _IdleTime: 桌面空闲时长，h:m:s
        :type IdleTime: str
        :param _AnonymousAccess: 是否匿名访问
        :type AnonymousAccess: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Status = None
        self._UserName = None
        self._ChargeType = None
        self._InstanceType = None
        self._OsName = None
        self._ActiveTime = None
        self._IdleTime = None
        self._AnonymousAccess = None

    @property
    def InstanceId(self):
        r"""桌面实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""桌面名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""桌面当前状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        r"""桌面绑定的用户名，若未绑定，为空
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ChargeType(self):
        r"""桌面计费类型
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def InstanceType(self):
        r"""桌面类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OsName(self):
        r"""桌面操作系统
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ActiveTime(self):
        r"""桌面使用时长，h:m:s
        :rtype: str
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def IdleTime(self):
        r"""桌面空闲时长，h:m:s
        :rtype: str
        """
        return self._IdleTime

    @IdleTime.setter
    def IdleTime(self, IdleTime):
        self._IdleTime = IdleTime

    @property
    def AnonymousAccess(self):
        r"""是否匿名访问
        :rtype: bool
        """
        return self._AnonymousAccess

    @AnonymousAccess.setter
    def AnonymousAccess(self, AnonymousAccess):
        self._AnonymousAccess = AnonymousAccess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._ChargeType = params.get("ChargeType")
        self._InstanceType = params.get("InstanceType")
        self._OsName = params.get("OsName")
        self._ActiveTime = params.get("ActiveTime")
        self._IdleTime = params.get("IdleTime")
        self._AnonymousAccess = params.get("AnonymousAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _Id: <p>用户ID。</p>
        :type Id: str
        :param _Name: <p>名字。</p>
        :type Name: str
        :param _DisplayName: <p>显示名字。</p>
        :type DisplayName: str
        :param _Mail: <p>邮箱。</p>
        :type Mail: str
        :param _PhoneNum: <p>手机号。</p>
        :type PhoneNum: str
        :param _Status: <p>状态。<br>ACTIVE:启用<br>PENDING_ACTIVATE:待激活<br>PENDING_ONBOARD:待启用<br>SUSPENDED:已停用<br>INACTIVE:已离职<br>PASSWORD_RESET:重置密码<br>LOCKED_OUT:锁定</p>
        :type Status: str
        :param _DepartmentId: <p>部门ID。</p>
        :type DepartmentId: str
        :param _StrategyId: <p>策略ID。</p>
        :type StrategyId: str
        :param _StrategyName: <p>策略名称。</p>
        :type StrategyName: str
        :param _BindStatus: <p>当前用户是否绑定桌面，true：绑定，false：未绑定任何桌面</p>
        :type BindStatus: bool
        """
        self._Id = None
        self._Name = None
        self._DisplayName = None
        self._Mail = None
        self._PhoneNum = None
        self._Status = None
        self._DepartmentId = None
        self._StrategyId = None
        self._StrategyName = None
        self._BindStatus = None

    @property
    def Id(self):
        r"""<p>用户ID。</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>名字。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DisplayName(self):
        r"""<p>显示名字。</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Mail(self):
        r"""<p>邮箱。</p>
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def PhoneNum(self):
        r"""<p>手机号。</p>
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Status(self):
        r"""<p>状态。<br>ACTIVE:启用<br>PENDING_ACTIVATE:待激活<br>PENDING_ONBOARD:待启用<br>SUSPENDED:已停用<br>INACTIVE:已离职<br>PASSWORD_RESET:重置密码<br>LOCKED_OUT:锁定</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DepartmentId(self):
        r"""<p>部门ID。</p>
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def StrategyId(self):
        r"""<p>策略ID。</p>
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        r"""<p>策略名称。</p>
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def BindStatus(self):
        r"""<p>当前用户是否绑定桌面，true：绑定，false：未绑定任何桌面</p>
        :rtype: bool
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._DisplayName = params.get("DisplayName")
        self._Mail = params.get("Mail")
        self._PhoneNum = params.get("PhoneNum")
        self._Status = params.get("Status")
        self._DepartmentId = params.get("DepartmentId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._BindStatus = params.get("BindStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualPrivateCloud(AbstractModel):
    r"""私有网络相关信息

    """

    def __init__(self):
        r"""
        :param _VpcId: <p>私有网络ID。</p>
        :type VpcId: str
        :param _SubnetId: <p>私有网络子网ID。</p>
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        r"""<p>私有网络ID。</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>私有网络子网ID。</p>
        :rtype: str
        """
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
        