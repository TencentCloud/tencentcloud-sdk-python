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


class AdvancedRetentionPolicy(AbstractModel):
    r"""备份高级保留策略

    """

    def __init__(self):
        r"""
        :param _Days: 保留设定天数中的每天最新的一个备份
        :type Days: int
        :param _Weeks: 保留设置周中的每周最新的一个备份
        :type Weeks: int
        :param _Months: 保留设置月内的每月最新的一个备份
        :type Months: int
        :param _Years: 保留设置年内的每年最新的一个备份
        :type Years: int
        """
        self._Days = None
        self._Weeks = None
        self._Months = None
        self._Years = None

    @property
    def Days(self):
        r"""保留设定天数中的每天最新的一个备份
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Weeks(self):
        r"""保留设置周中的每周最新的一个备份
        :rtype: int
        """
        return self._Weeks

    @Weeks.setter
    def Weeks(self, Weeks):
        self._Weeks = Weeks

    @property
    def Months(self):
        r"""保留设置月内的每月最新的一个备份
        :rtype: int
        """
        return self._Months

    @Months.setter
    def Months(self, Months):
        self._Months = Months

    @property
    def Years(self):
        r"""保留设置年内的每年最新的一个备份
        :rtype: int
        """
        return self._Years

    @Years.setter
    def Years(self, Years):
        self._Years = Years


    def _deserialize(self, params):
        self._Days = params.get("Days")
        self._Weeks = params.get("Weeks")
        self._Months = params.get("Months")
        self._Years = params.get("Years")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBackupGroupRequest(AbstractModel):
    r"""ApplyBackupGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupId: 回滚的备份组ID。
        :type BackupGroupId: str
        :param _ApplyDisks: 回滚的备份ID、云硬盘ID列表。
        :type ApplyDisks: list of ApplyDisk
        :param _AutoStopInstance: 回滚备份前是否执行自动关机，如果回滚的盘挂载在实例上且实例处于运行状态，可传入该参数。
        :type AutoStopInstance: bool
        :param _AutoStartInstance: 回滚备份完成后是否执行自动开机。
        :type AutoStartInstance: bool
        """
        self._BackupGroupId = None
        self._ApplyDisks = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def BackupGroupId(self):
        r"""回滚的备份组ID。
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId

    @property
    def ApplyDisks(self):
        r"""回滚的备份ID、云硬盘ID列表。
        :rtype: list of ApplyDisk
        """
        return self._ApplyDisks

    @ApplyDisks.setter
    def ApplyDisks(self, ApplyDisks):
        self._ApplyDisks = ApplyDisks

    @property
    def AutoStopInstance(self):
        r"""回滚备份前是否执行自动关机，如果回滚的盘挂载在实例上且实例处于运行状态，可传入该参数。
        :rtype: bool
        """
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        r"""回滚备份完成后是否执行自动开机。
        :rtype: bool
        """
        return self._AutoStartInstance

    @AutoStartInstance.setter
    def AutoStartInstance(self, AutoStartInstance):
        self._AutoStartInstance = AutoStartInstance


    def _deserialize(self, params):
        self._BackupGroupId = params.get("BackupGroupId")
        if params.get("ApplyDisks") is not None:
            self._ApplyDisks = []
            for item in params.get("ApplyDisks"):
                obj = ApplyDisk()
                obj._deserialize(item)
                self._ApplyDisks.append(obj)
        self._AutoStopInstance = params.get("AutoStopInstance")
        self._AutoStartInstance = params.get("AutoStartInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBackupGroupResponse(AbstractModel):
    r"""ApplyBackupGroup返回参数结构体

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


class ApplyDisk(AbstractModel):
    r"""备份组备份和云盘绑定信息

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份ID
        :type BackupId: str
        :param _DiskId: 云盘ID
        :type DiskId: str
        """
        self._BackupId = None
        self._DiskId = None

    @property
    def BackupId(self):
        r"""备份ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DiskId(self):
        r"""云盘ID
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AspInfo(AbstractModel):
    r"""备份的执行策略信息

    """

    def __init__(self):
        r"""
        :param _AspId: 备份策略ID
        :type AspId: str
        :param _AspName: 备份策略名称
        :type AspName: str
        :param _AspState: 备份策略状态
        :type AspState: str
        :param _Policy: 备份策略执行详情
        :type Policy: list of Policy
        :param _IsActivated: 备份策略是否使能
        :type IsActivated: bool
        :param _IsPermanent: 是否永久保留
        :type IsPermanent: bool
        :param _RetentionDays: 保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionDays: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._AspId = None
        self._AspName = None
        self._AspState = None
        self._Policy = None
        self._IsActivated = None
        self._IsPermanent = None
        self._RetentionDays = None
        self._CreateTime = None

    @property
    def AspId(self):
        r"""备份策略ID
        :rtype: str
        """
        return self._AspId

    @AspId.setter
    def AspId(self, AspId):
        self._AspId = AspId

    @property
    def AspName(self):
        r"""备份策略名称
        :rtype: str
        """
        return self._AspName

    @AspName.setter
    def AspName(self, AspName):
        self._AspName = AspName

    @property
    def AspState(self):
        r"""备份策略状态
        :rtype: str
        """
        return self._AspState

    @AspState.setter
    def AspState(self, AspState):
        self._AspState = AspState

    @property
    def Policy(self):
        r"""备份策略执行详情
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def IsActivated(self):
        r"""备份策略是否使能
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        r"""是否永久保留
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def RetentionDays(self):
        r"""保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AspId = params.get("AspId")
        self._AspName = params.get("AspName")
        self._AspState = params.get("AspState")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._IsActivated = params.get("IsActivated")
        self._IsPermanent = params.get("IsPermanent")
        self._RetentionDays = params.get("RetentionDays")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoBackupPolicy(AbstractModel):
    r"""定期备份策略的详细信息

    """

    def __init__(self):
        r"""
        :param _IsActivated: 定期备份策略是否激活。
        :type IsActivated: bool
        :param _IsPermanent: 使用该定期备份策略创建出来的备份是否永久保留。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPermanent: bool
        :param _NextTriggerTime: 使用该定期备份策略创建出来的备份是否永久保留。
        :type NextTriggerTime: str
        :param _AutoBackupPolicyState: NORMAL
        :type AutoBackupPolicyState: str
        :param _AutoBackupPolicyName: 备份策略的名称。
        :type AutoBackupPolicyName: str
        :param _Policy: 定期备份的执行策略。
        :type Policy: list of Policy
        :param _AutoBackupPolicyId: 备份策略ID。
        :type AutoBackupPolicyId: str
        :param _CreateTime: 备份策略的创建时间。
        :type CreateTime: str
        :param _RetentionDays: 使用该定期备份策略创建出来的备份保留天数。
        :type RetentionDays: int
        :param _AppId: 用户AppId。
        :type AppId: int
        :param _InstanceIdSet: 定期备份策略绑定的实例ID列表。
        :type InstanceIdSet: list of str
        :param _RetentionMonths: 该定期快照创建的快照最大保留月数
        :type RetentionMonths: int
        :param _RetentionAmount: 该定期快照创建的快照最大保留数量
        :type RetentionAmount: int
        :param _AccountName: 创建人。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _AccountUin: 主账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 子账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _StorageType: 策略存储类型
        :type StorageType: str
        :param _VaultId: 备份库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VaultId: str
        :param _AdvancedRetentionPolicy: 高级保留策略
        :type AdvancedRetentionPolicy: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        self._IsActivated = None
        self._IsPermanent = None
        self._NextTriggerTime = None
        self._AutoBackupPolicyState = None
        self._AutoBackupPolicyName = None
        self._Policy = None
        self._AutoBackupPolicyId = None
        self._CreateTime = None
        self._RetentionDays = None
        self._AppId = None
        self._InstanceIdSet = None
        self._RetentionMonths = None
        self._RetentionAmount = None
        self._AccountName = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._StorageType = None
        self._VaultId = None
        self._AdvancedRetentionPolicy = None

    @property
    def IsActivated(self):
        r"""定期备份策略是否激活。
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        r"""使用该定期备份策略创建出来的备份是否永久保留。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def NextTriggerTime(self):
        r"""使用该定期备份策略创建出来的备份是否永久保留。
        :rtype: str
        """
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def AutoBackupPolicyState(self):
        r"""NORMAL
        :rtype: str
        """
        return self._AutoBackupPolicyState

    @AutoBackupPolicyState.setter
    def AutoBackupPolicyState(self, AutoBackupPolicyState):
        self._AutoBackupPolicyState = AutoBackupPolicyState

    @property
    def AutoBackupPolicyName(self):
        r"""备份策略的名称。
        :rtype: str
        """
        return self._AutoBackupPolicyName

    @AutoBackupPolicyName.setter
    def AutoBackupPolicyName(self, AutoBackupPolicyName):
        self._AutoBackupPolicyName = AutoBackupPolicyName

    @property
    def Policy(self):
        r"""定期备份的执行策略。
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def AutoBackupPolicyId(self):
        r"""备份策略ID。
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId

    @property
    def CreateTime(self):
        r"""备份策略的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RetentionDays(self):
        r"""使用该定期备份策略创建出来的备份保留天数。
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def AppId(self):
        r"""用户AppId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def InstanceIdSet(self):
        r"""定期备份策略绑定的实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RetentionMonths(self):
        r"""该定期快照创建的快照最大保留月数
        :rtype: int
        """
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        r"""该定期快照创建的快照最大保留数量
        :rtype: int
        """
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def AccountName(self):
        r"""创建人。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountUin(self):
        r"""主账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""子账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def StorageType(self):
        r"""策略存储类型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VaultId(self):
        r"""备份库ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def AdvancedRetentionPolicy(self):
        r"""高级保留策略
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy


    def _deserialize(self, params):
        self._IsActivated = params.get("IsActivated")
        self._IsPermanent = params.get("IsPermanent")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._AutoBackupPolicyState = params.get("AutoBackupPolicyState")
        self._AutoBackupPolicyName = params.get("AutoBackupPolicyName")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        self._CreateTime = params.get("CreateTime")
        self._RetentionDays = params.get("RetentionDays")
        self._AppId = params.get("AppId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RetentionMonths = params.get("RetentionMonths")
        self._RetentionAmount = params.get("RetentionAmount")
        self._AccountName = params.get("AccountName")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._StorageType = params.get("StorageType")
        self._VaultId = params.get("VaultId")
        if params.get("AdvancedRetentionPolicy") is not None:
            self._AdvancedRetentionPolicy = AdvancedRetentionPolicy()
            self._AdvancedRetentionPolicy._deserialize(params.get("AdvancedRetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutomationServiceEnabled(AbstractModel):
    r"""描述了 “tat-agent” 相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启该服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""是否开启该服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :rtype: bool
        """
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
        


class BackupDeniedAction(AbstractModel):
    r"""单个备份的操作掩码。

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份ID。
        :type BackupId: str
        :param _DeniedActions: 具体的备份操作掩码列表。
        :type DeniedActions: list of DeniedAction
        """
        self._BackupId = None
        self._DeniedActions = None

    @property
    def BackupId(self):
        r"""备份ID。
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DeniedActions(self):
        r"""具体的备份操作掩码列表。
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDetail(AbstractModel):
    r"""备份详情

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份组ID
        :type BackupId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AutoBackupPolicyId: 备份策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupPolicyId: str
        :param _BackupBindDisk: 备份和云盘绑定关系
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupBindDisk: list of ApplyDisk
        """
        self._BackupId = None
        self._InstanceId = None
        self._CreateTime = None
        self._AutoBackupPolicyId = None
        self._BackupBindDisk = None

    @property
    def BackupId(self):
        r"""备份组ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def AutoBackupPolicyId(self):
        r"""备份策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId

    @property
    def BackupBindDisk(self):
        r"""备份和云盘绑定关系
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApplyDisk
        """
        return self._BackupBindDisk

    @BackupBindDisk.setter
    def BackupBindDisk(self, BackupBindDisk):
        self._BackupBindDisk = BackupBindDisk


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        if params.get("BackupBindDisk") is not None:
            self._BackupBindDisk = []
            for item in params.get("BackupBindDisk"):
                obj = ApplyDisk()
                obj._deserialize(item)
                self._BackupBindDisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupGroup(AbstractModel):
    r"""备份组详情

    """

    def __init__(self):
        r"""
        :param _BackupGroupId: 备份组ID。
        :type BackupGroupId: str
        :param _Percent: 备份组创建进度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _BackupBindDisk: 备份和云盘绑定关系
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupBindDisk: list of ApplyDisk
        :param _BackupGroupName: 备份组名称。
        :type BackupGroupName: str
        :param _BackupGroupState: 备份组状态。NORMAL: 正常；CREATING: 创建中；ROLLBACKING: 回滚中
        :type BackupGroupState: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AppId: 用户AppId。
        :type AppId: int
        :param _IsPermanent: 是否为永久备份组。
        :type IsPermanent: bool
        :param _DeadlineTime: 备份组的到期时间。如果为永久备份组，则取值为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadlineTime: str
        :param _InstanceId: 创建备份组的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceDetails: 创建备份组时刻实例的详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceDetails: str
        :param _AccountName: 创建人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _AccountUin: 主账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 创建备份的子账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _AutoBackupPolicyId: 创建当前备份的定期备份策略ID，为null则为手动创建的备份。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupPolicyId: str
        """
        self._BackupGroupId = None
        self._Percent = None
        self._BackupBindDisk = None
        self._BackupGroupName = None
        self._BackupGroupState = None
        self._ModifyTime = None
        self._CreateTime = None
        self._AppId = None
        self._IsPermanent = None
        self._DeadlineTime = None
        self._InstanceId = None
        self._InstanceDetails = None
        self._AccountName = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._AutoBackupPolicyId = None

    @property
    def BackupGroupId(self):
        r"""备份组ID。
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId

    @property
    def Percent(self):
        r"""备份组创建进度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def BackupBindDisk(self):
        r"""备份和云盘绑定关系
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApplyDisk
        """
        return self._BackupBindDisk

    @BackupBindDisk.setter
    def BackupBindDisk(self, BackupBindDisk):
        self._BackupBindDisk = BackupBindDisk

    @property
    def BackupGroupName(self):
        r"""备份组名称。
        :rtype: str
        """
        return self._BackupGroupName

    @BackupGroupName.setter
    def BackupGroupName(self, BackupGroupName):
        self._BackupGroupName = BackupGroupName

    @property
    def BackupGroupState(self):
        r"""备份组状态。NORMAL: 正常；CREATING: 创建中；ROLLBACKING: 回滚中
        :rtype: str
        """
        return self._BackupGroupState

    @BackupGroupState.setter
    def BackupGroupState(self, BackupGroupState):
        self._BackupGroupState = BackupGroupState

    @property
    def ModifyTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
    def AppId(self):
        r"""用户AppId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IsPermanent(self):
        r"""是否为永久备份组。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def DeadlineTime(self):
        r"""备份组的到期时间。如果为永久备份组，则取值为null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def InstanceId(self):
        r"""创建备份组的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceDetails(self):
        r"""创建备份组时刻实例的详情。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def AccountName(self):
        r"""创建人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountUin(self):
        r"""主账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""创建备份的子账号uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def AutoBackupPolicyId(self):
        r"""创建当前备份的定期备份策略ID，为null则为手动创建的备份。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId


    def _deserialize(self, params):
        self._BackupGroupId = params.get("BackupGroupId")
        self._Percent = params.get("Percent")
        if params.get("BackupBindDisk") is not None:
            self._BackupBindDisk = []
            for item in params.get("BackupBindDisk"):
                obj = ApplyDisk()
                obj._deserialize(item)
                self._BackupBindDisk.append(obj)
        self._BackupGroupName = params.get("BackupGroupName")
        self._BackupGroupState = params.get("BackupGroupState")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._IsPermanent = params.get("IsPermanent")
        self._DeadlineTime = params.get("DeadlineTime")
        self._InstanceId = params.get("InstanceId")
        self._InstanceDetails = params.get("InstanceDetails")
        self._AccountName = params.get("AccountName")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupGroupDeniedAction(AbstractModel):
    r"""备份组的操作掩码

    """

    def __init__(self):
        r"""
        :param _BackupGroupId: 备份组ID
        :type BackupGroupId: str
        :param _DeniedActions: 拒绝的操作
        :type DeniedActions: list of DeniedAction
        """
        self._BackupGroupId = None
        self._DeniedActions = None

    @property
    def BackupGroupId(self):
        r"""备份组ID
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId

    @property
    def DeniedActions(self):
        r"""拒绝的操作
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._BackupGroupId = params.get("BackupGroupId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupGroupRollbackTask(AbstractModel):
    r"""备份组回滚任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 备份组回滚任务
        :type TaskId: str
        :param _SourceInstanceId: 源实例ID
        :type SourceInstanceId: str
        :param _TargetInstanceId: 目标实例ID
        :type TargetInstanceId: str
        :param _BackupGroupId: 备份组ID
        :type BackupGroupId: str
        :param _RollbackType: 恢复类型：ORIGINAL-原实例恢复，NEW-新实例恢复
        :type RollbackType: str
        :param _Status: 任务状态。取值包括"init"、"migrating"、"done"、"failed"。
        :type Status: str
        :param _Percent: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _AppId: APP ID
        :type AppId: int
        :param _BackupGroupName: 备份点名称
        :type BackupGroupName: str
        :param _FailReason: 恢复失败原因
        :type FailReason: str
        """
        self._TaskId = None
        self._SourceInstanceId = None
        self._TargetInstanceId = None
        self._BackupGroupId = None
        self._RollbackType = None
        self._Status = None
        self._Percent = None
        self._StartTime = None
        self._EndTime = None
        self._AppId = None
        self._BackupGroupName = None
        self._FailReason = None

    @property
    def TaskId(self):
        r"""备份组回滚任务
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SourceInstanceId(self):
        r"""源实例ID
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def TargetInstanceId(self):
        r"""目标实例ID
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def BackupGroupId(self):
        r"""备份组ID
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId

    @property
    def RollbackType(self):
        r"""恢复类型：ORIGINAL-原实例恢复，NEW-新实例恢复
        :rtype: str
        """
        return self._RollbackType

    @RollbackType.setter
    def RollbackType(self, RollbackType):
        self._RollbackType = RollbackType

    @property
    def Status(self):
        r"""任务状态。取值包括"init"、"migrating"、"done"、"failed"。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        r"""进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def StartTime(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppId(self):
        r"""APP ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BackupGroupName(self):
        r"""备份点名称
        :rtype: str
        """
        return self._BackupGroupName

    @BackupGroupName.setter
    def BackupGroupName(self, BackupGroupName):
        self._BackupGroupName = BackupGroupName

    @property
    def FailReason(self):
        r"""恢复失败原因
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._BackupGroupId = params.get("BackupGroupId")
        self._RollbackType = params.get("RollbackType")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppId = params.get("AppId")
        self._BackupGroupName = params.get("BackupGroupName")
        self._FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    r"""备份点信息

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份点ID
        :type BackupId: str
        :param _BackupName: 备份名称
        :type BackupName: str
        :param _PlanId: 所属计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanId: str
        :param _AspInstanceId: 策略ID
        :type AspInstanceId: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Status: 备份状态，取值如下：
0 备份完成
1 创建中（备份进行中）
2 部分成功（指定的备份路径中部分目录不存在）
3 恢复中（该备份点正在被恢复任务使用）
92  已取消
98 创建失败
99 已删除
100 删除中

        :type Status: int
        :param _BackupPaths: 备份路径
        :type BackupPaths: list of str
        :param _IncludeFileTypes: 包含文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeFileTypes: list of str
        :param _ExcludePatterns: 排除路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePatterns: list of str
        :param _ExcludeSystemDirectories: 是否排除系统目录
        :type ExcludeSystemDirectories: bool
        :param _VaultId: 备份库ID
        :type VaultId: str
        :param _ScannedFileCount: 扫描文件数
        :type ScannedFileCount: int
        :param _ScannedSize: 扫描大小(字节)
        :type ScannedSize: int
        :param _ScannedSizeFormatted: 扫描大小(格式化)
        :type ScannedSizeFormatted: str
        :param _BackupFileCount: 已备份文件数量
        :type BackupFileCount: int
        :param _BackupSize: 已备份大小(字节)
        :type BackupSize: int
        :param _BackupSizeFormatted: 已备份大小(格式化)
        :type BackupSizeFormatted: str
        :param _Progress: 备份进度(0-100)
        :type Progress: float
        :param _JobId: 任务ID
        :type JobId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _IsPermanent: 是否为永久保留
        :type IsPermanent: bool
        :param _Deadline: 到期时间
        :type Deadline: str
        :param _NonExistSourcePaths: 不存在的路径信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NonExistSourcePaths: list of str
        :param _FailReason: 备份失败原因
        :type FailReason: str
        :param _AppId: 备份所属AppId
        :type AppId: int
        :param _ResourceType: 备份类型
        :type ResourceType: str
        """
        self._BackupId = None
        self._BackupName = None
        self._PlanId = None
        self._AspInstanceId = None
        self._ResourceId = None
        self._Status = None
        self._BackupPaths = None
        self._IncludeFileTypes = None
        self._ExcludePatterns = None
        self._ExcludeSystemDirectories = None
        self._VaultId = None
        self._ScannedFileCount = None
        self._ScannedSize = None
        self._ScannedSizeFormatted = None
        self._BackupFileCount = None
        self._BackupSize = None
        self._BackupSizeFormatted = None
        self._Progress = None
        self._JobId = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._IsPermanent = None
        self._Deadline = None
        self._NonExistSourcePaths = None
        self._FailReason = None
        self._AppId = None
        self._ResourceType = None

    @property
    def BackupId(self):
        r"""备份点ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        r"""备份名称
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def PlanId(self):
        r"""所属计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def AspInstanceId(self):
        r"""策略ID
        :rtype: str
        """
        return self._AspInstanceId

    @AspInstanceId.setter
    def AspInstanceId(self, AspInstanceId):
        self._AspInstanceId = AspInstanceId

    @property
    def ResourceId(self):
        r"""资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        r"""备份状态，取值如下：
0 备份完成
1 创建中（备份进行中）
2 部分成功（指定的备份路径中部分目录不存在）
3 恢复中（该备份点正在被恢复任务使用）
92  已取消
98 创建失败
99 已删除
100 删除中

        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BackupPaths(self):
        r"""备份路径
        :rtype: list of str
        """
        return self._BackupPaths

    @BackupPaths.setter
    def BackupPaths(self, BackupPaths):
        self._BackupPaths = BackupPaths

    @property
    def IncludeFileTypes(self):
        r"""包含文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IncludeFileTypes

    @IncludeFileTypes.setter
    def IncludeFileTypes(self, IncludeFileTypes):
        self._IncludeFileTypes = IncludeFileTypes

    @property
    def ExcludePatterns(self):
        r"""排除路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludePatterns

    @ExcludePatterns.setter
    def ExcludePatterns(self, ExcludePatterns):
        self._ExcludePatterns = ExcludePatterns

    @property
    def ExcludeSystemDirectories(self):
        r"""是否排除系统目录
        :rtype: bool
        """
        return self._ExcludeSystemDirectories

    @ExcludeSystemDirectories.setter
    def ExcludeSystemDirectories(self, ExcludeSystemDirectories):
        self._ExcludeSystemDirectories = ExcludeSystemDirectories

    @property
    def VaultId(self):
        r"""备份库ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def ScannedFileCount(self):
        r"""扫描文件数
        :rtype: int
        """
        return self._ScannedFileCount

    @ScannedFileCount.setter
    def ScannedFileCount(self, ScannedFileCount):
        self._ScannedFileCount = ScannedFileCount

    @property
    def ScannedSize(self):
        r"""扫描大小(字节)
        :rtype: int
        """
        return self._ScannedSize

    @ScannedSize.setter
    def ScannedSize(self, ScannedSize):
        self._ScannedSize = ScannedSize

    @property
    def ScannedSizeFormatted(self):
        r"""扫描大小(格式化)
        :rtype: str
        """
        return self._ScannedSizeFormatted

    @ScannedSizeFormatted.setter
    def ScannedSizeFormatted(self, ScannedSizeFormatted):
        self._ScannedSizeFormatted = ScannedSizeFormatted

    @property
    def BackupFileCount(self):
        r"""已备份文件数量
        :rtype: int
        """
        return self._BackupFileCount

    @BackupFileCount.setter
    def BackupFileCount(self, BackupFileCount):
        self._BackupFileCount = BackupFileCount

    @property
    def BackupSize(self):
        r"""已备份大小(字节)
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def BackupSizeFormatted(self):
        r"""已备份大小(格式化)
        :rtype: str
        """
        return self._BackupSizeFormatted

    @BackupSizeFormatted.setter
    def BackupSizeFormatted(self, BackupSizeFormatted):
        self._BackupSizeFormatted = BackupSizeFormatted

    @property
    def Progress(self):
        r"""备份进度(0-100)
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def IsPermanent(self):
        r"""是否为永久保留
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def Deadline(self):
        r"""到期时间
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def NonExistSourcePaths(self):
        r"""不存在的路径信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NonExistSourcePaths

    @NonExistSourcePaths.setter
    def NonExistSourcePaths(self, NonExistSourcePaths):
        self._NonExistSourcePaths = NonExistSourcePaths

    @property
    def FailReason(self):
        r"""备份失败原因
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def AppId(self):
        r"""备份所属AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ResourceType(self):
        r"""备份类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._BackupName = params.get("BackupName")
        self._PlanId = params.get("PlanId")
        self._AspInstanceId = params.get("AspInstanceId")
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        self._BackupPaths = params.get("BackupPaths")
        self._IncludeFileTypes = params.get("IncludeFileTypes")
        self._ExcludePatterns = params.get("ExcludePatterns")
        self._ExcludeSystemDirectories = params.get("ExcludeSystemDirectories")
        self._VaultId = params.get("VaultId")
        self._ScannedFileCount = params.get("ScannedFileCount")
        self._ScannedSize = params.get("ScannedSize")
        self._ScannedSizeFormatted = params.get("ScannedSizeFormatted")
        self._BackupFileCount = params.get("BackupFileCount")
        self._BackupSize = params.get("BackupSize")
        self._BackupSizeFormatted = params.get("BackupSizeFormatted")
        self._Progress = params.get("Progress")
        self._JobId = params.get("JobId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._IsPermanent = params.get("IsPermanent")
        self._Deadline = params.get("Deadline")
        self._NonExistSourcePaths = params.get("NonExistSourcePaths")
        self._FailReason = params.get("FailReason")
        self._AppId = params.get("AppId")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInstance(AbstractModel):
    r"""描述实例的备份信息

    """

    def __init__(self):
        r"""
        :param _AutoBackupPolicyIdSet: 实例绑定的定期备份策略列表。
        :type AutoBackupPolicyIdSet: list of str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AppId: 用户AppId。
        :type AppId: int
        :param _LatestBackupTime: 实例最新备份时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestBackupTime: str
        :param _BackupGroupIdSet: 实例的备份组ID列表。
        :type BackupGroupIdSet: list of str
        :param _ModifyTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        """
        self._AutoBackupPolicyIdSet = None
        self._InstanceId = None
        self._AppId = None
        self._LatestBackupTime = None
        self._BackupGroupIdSet = None
        self._ModifyTime = None
        self._CreateTime = None
        self._InstanceName = None

    @property
    def AutoBackupPolicyIdSet(self):
        r"""实例绑定的定期备份策略列表。
        :rtype: list of str
        """
        return self._AutoBackupPolicyIdSet

    @AutoBackupPolicyIdSet.setter
    def AutoBackupPolicyIdSet(self, AutoBackupPolicyIdSet):
        self._AutoBackupPolicyIdSet = AutoBackupPolicyIdSet

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        r"""用户AppId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def LatestBackupTime(self):
        r"""实例最新备份时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestBackupTime

    @LatestBackupTime.setter
    def LatestBackupTime(self, LatestBackupTime):
        self._LatestBackupTime = LatestBackupTime

    @property
    def BackupGroupIdSet(self):
        r"""实例的备份组ID列表。
        :rtype: list of str
        """
        return self._BackupGroupIdSet

    @BackupGroupIdSet.setter
    def BackupGroupIdSet(self, BackupGroupIdSet):
        self._BackupGroupIdSet = BackupGroupIdSet

    @property
    def ModifyTime(self):
        r"""修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._AutoBackupPolicyIdSet = params.get("AutoBackupPolicyIdSet")
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        self._LatestBackupTime = params.get("LatestBackupTime")
        self._BackupGroupIdSet = params.get("BackupGroupIdSet")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlan(AbstractModel):
    r"""整机备份计划

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AutoBackupPolicyId: 备份策略ID
        :type AutoBackupPolicyId: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AppId: APP ID
        :type AppId: int
        :param _BackupCount: 备份数量
        :type BackupCount: int
        :param _LastTriggerTime: 上次执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerTime: str
        :param _LastTriggerError: 上次执行错误信息，如果为空表示上次执行成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerError: str
        """
        self._InstanceId = None
        self._AutoBackupPolicyId = None
        self._ModifyTime = None
        self._CreateTime = None
        self._AppId = None
        self._BackupCount = None
        self._LastTriggerTime = None
        self._LastTriggerError = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoBackupPolicyId(self):
        r"""备份策略ID
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId

    @property
    def ModifyTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
    def AppId(self):
        r"""APP ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BackupCount(self):
        r"""备份数量
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def LastTriggerTime(self):
        r"""上次执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastTriggerTime

    @LastTriggerTime.setter
    def LastTriggerTime(self, LastTriggerTime):
        self._LastTriggerTime = LastTriggerTime

    @property
    def LastTriggerError(self):
        r"""上次执行错误信息，如果为空表示上次执行成功。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastTriggerError

    @LastTriggerError.setter
    def LastTriggerError(self, LastTriggerError):
        self._LastTriggerError = LastTriggerError


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._BackupCount = params.get("BackupCount")
        self._LastTriggerTime = params.get("LastTriggerTime")
        self._LastTriggerError = params.get("LastTriggerError")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPolicyOverview(AbstractModel):
    r"""备份策略概览

    """

    def __init__(self):
        r"""
        :param _TotalCount: 自动备份策略总数
        :type TotalCount: int
        :param _BoundCount: 已绑定资源的策略数
        :type BoundCount: int
        :param _UnboundCount: 未绑定任何资源的策略数
        :type UnboundCount: int
        """
        self._TotalCount = None
        self._BoundCount = None
        self._UnboundCount = None

    @property
    def TotalCount(self):
        r"""自动备份策略总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BoundCount(self):
        r"""已绑定资源的策略数
        :rtype: int
        """
        return self._BoundCount

    @BoundCount.setter
    def BoundCount(self, BoundCount):
        self._BoundCount = BoundCount

    @property
    def UnboundCount(self):
        r"""未绑定任何资源的策略数
        :rtype: int
        """
        return self._UnboundCount

    @UnboundCount.setter
    def UnboundCount(self, UnboundCount):
        self._UnboundCount = UnboundCount


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._BoundCount = params.get("BoundCount")
        self._UnboundCount = params.get("UnboundCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupVault(AbstractModel):
    r"""备份库信息

    """

    def __init__(self):
        r"""
        :param _VaultId: 备份库ID
        :type VaultId: str
        :param _VaultName: 备份库名称
        :type VaultName: str
        :param _Description: 备份库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 备份库状态：READ_WRITE / READ_ONLY / UNAVAILABLE / DELETING
        :type Status: str
        :param _EncryptType: 加密方式：NONE / SSE-COS / SSE-KMS
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptType: str
        :param _KmsKeyId: KMS密钥ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param _VaultType: 备份库类型：COMMON
        :type VaultType: str
        :param _BackupPolicySet: 关联的备份策略按类型统计
        :type BackupPolicySet: list of TypeCount
        :param _BackupSet: 备份点按类型统计（不含已删除）
        :type BackupSet: list of TypeCount
        :param _Region: 地域信息
        :type Region: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _SourceDataSize: 源端数据量
        :type SourceDataSize: int
        :param _VaultDataSize: 存储库数据量
        :type VaultDataSize: int
        """
        self._VaultId = None
        self._VaultName = None
        self._Description = None
        self._Status = None
        self._EncryptType = None
        self._KmsKeyId = None
        self._VaultType = None
        self._BackupPolicySet = None
        self._BackupSet = None
        self._Region = None
        self._CreateTime = None
        self._SourceDataSize = None
        self._VaultDataSize = None

    @property
    def VaultId(self):
        r"""备份库ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def VaultName(self):
        r"""备份库名称
        :rtype: str
        """
        return self._VaultName

    @VaultName.setter
    def VaultName(self, VaultName):
        self._VaultName = VaultName

    @property
    def Description(self):
        r"""备份库描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""备份库状态：READ_WRITE / READ_ONLY / UNAVAILABLE / DELETING
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EncryptType(self):
        r"""加密方式：NONE / SSE-COS / SSE-KMS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EncryptType

    @EncryptType.setter
    def EncryptType(self, EncryptType):
        self._EncryptType = EncryptType

    @property
    def KmsKeyId(self):
        r"""KMS密钥ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def VaultType(self):
        r"""备份库类型：COMMON
        :rtype: str
        """
        return self._VaultType

    @VaultType.setter
    def VaultType(self, VaultType):
        self._VaultType = VaultType

    @property
    def BackupPolicySet(self):
        r"""关联的备份策略按类型统计
        :rtype: list of TypeCount
        """
        return self._BackupPolicySet

    @BackupPolicySet.setter
    def BackupPolicySet(self, BackupPolicySet):
        self._BackupPolicySet = BackupPolicySet

    @property
    def BackupSet(self):
        r"""备份点按类型统计（不含已删除）
        :rtype: list of TypeCount
        """
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

    @property
    def Region(self):
        r"""地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

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
    def SourceDataSize(self):
        r"""源端数据量
        :rtype: int
        """
        return self._SourceDataSize

    @SourceDataSize.setter
    def SourceDataSize(self, SourceDataSize):
        self._SourceDataSize = SourceDataSize

    @property
    def VaultDataSize(self):
        r"""存储库数据量
        :rtype: int
        """
        return self._VaultDataSize

    @VaultDataSize.setter
    def VaultDataSize(self, VaultDataSize):
        self._VaultDataSize = VaultDataSize


    def _deserialize(self, params):
        self._VaultId = params.get("VaultId")
        self._VaultName = params.get("VaultName")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._EncryptType = params.get("EncryptType")
        self._KmsKeyId = params.get("KmsKeyId")
        self._VaultType = params.get("VaultType")
        if params.get("BackupPolicySet") is not None:
            self._BackupPolicySet = []
            for item in params.get("BackupPolicySet"):
                obj = TypeCount()
                obj._deserialize(item)
                self._BackupPolicySet.append(obj)
        if params.get("BackupSet") is not None:
            self._BackupSet = []
            for item in params.get("BackupSet"):
                obj = TypeCount()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._SourceDataSize = params.get("SourceDataSize")
        self._VaultDataSize = params.get("VaultDataSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupVaultOverview(AbstractModel):
    r"""备份库概览

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份库总数
        :type TotalCount: int
        :param _TotalSizeMb: 备份库总存储量（已用容量），单位 MB
        :type TotalSizeMb: int
        """
        self._TotalCount = None
        self._TotalSizeMb = None

    @property
    def TotalCount(self):
        r"""备份库总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSizeMb(self):
        r"""备份库总存储量（已用容量），单位 MB
        :rtype: int
        """
        return self._TotalSizeMb

    @TotalSizeMb.setter
    def TotalSizeMb(self, TotalSizeMb):
        self._TotalSizeMb = TotalSizeMb


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalSizeMb = params.get("TotalSizeMb")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicServicesSettings(AbstractModel):
    r"""描述了 “基础” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启基础服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""是否开启基础服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :rtype: bool
        """
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
        


class BindAutoBackupPolicyRequest(AbstractModel):
    r"""BindAutoBackupPolicy请求参数结构体

    """


class BindAutoBackupPolicyResponse(AbstractModel):
    r"""BindAutoBackupPolicy返回参数结构体

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


class CommonBackupPoint(AbstractModel):
    r"""共同备份点信息

    """

    def __init__(self):
        r"""
        :param _BackupCommonTime: 共同时间点（精确到小时）
        :type BackupCommonTime: str
        :param _BackupDetailSet: 共同备份点信息
        :type BackupDetailSet: list of BackupDetail
        """
        self._BackupCommonTime = None
        self._BackupDetailSet = None

    @property
    def BackupCommonTime(self):
        r"""共同时间点（精确到小时）
        :rtype: str
        """
        return self._BackupCommonTime

    @BackupCommonTime.setter
    def BackupCommonTime(self, BackupCommonTime):
        self._BackupCommonTime = BackupCommonTime

    @property
    def BackupDetailSet(self):
        r"""共同备份点信息
        :rtype: list of BackupDetail
        """
        return self._BackupDetailSet

    @BackupDetailSet.setter
    def BackupDetailSet(self, BackupDetailSet):
        self._BackupDetailSet = BackupDetailSet


    def _deserialize(self, params):
        self._BackupCommonTime = params.get("BackupCommonTime")
        if params.get("BackupDetailSet") is not None:
            self._BackupDetailSet = []
            for item in params.get("BackupDetailSet"):
                obj = BackupDetail()
                obj._deserialize(item)
                self._BackupDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPair(AbstractModel):
    r"""复制对信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户ID
        :type AppId: int
        :param _CopyPairId: 复制对ID（CVM 类型为 cvmcopypair-xxxxxxxx，DISK/CFS 类型为 copypair-xxxxxxxx）
        :type CopyPairId: str
        :param _CopyPairName: 复制对名称
        :type CopyPairName: str
        :param _SitePairId: 所属容灾站点对ID
        :type SitePairId: str
        :param _SitePairName: 所属容灾站点对名称
        :type SitePairName: str
        :param _ProtectGroupId: 保护组ID
        :type ProtectGroupId: str
        :param _ProtectGroupName: 保护组名称
        :type ProtectGroupName: str
        :param _CopyPairState: 复制对状态。可选值：INIT、RUNNING、FULL_COPYING、INC_COPYING、NORMAL、DOWN、DEGRADE 等
        :type CopyPairState: str
        :param _CopyPairType: 复制对类型。可选值：DISK、INSTANCE、CFS
        :type CopyPairType: str
        :param _SourceRegion: 生产地域
        :type SourceRegion: str
        :param _SourceZone: 生产可用区
        :type SourceZone: str
        :param _SourceVpc: 生产端VPC
        :type SourceVpc: str
        :param _TargetRegion: 容灾地域
        :type TargetRegion: str
        :param _TargetZone: 容灾可用区
        :type TargetZone: str
        :param _TargetVpc: 容灾端VPC
        :type TargetVpc: str
        :param _SourceResourceId: 生产资源ID。CVM 类型为源 InstanceId（ins-xxx）；DISK 类型为源 DiskId（disk-xxx）；CFS 类型为源 FilesystemId（cfs-xxx）
        :type SourceResourceId: str
        :param _TargetResourceId: 容灾资源ID。语义同 SourceResourceId（CVM/DISK/CFS）。延迟创建模式且 CVM 未真实创建时为占位符 drp-xxx，CVM 创建后为真实 ins-xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetResourceId: str
        :param _InstanceId: 生产站点盘挂载的实例ID（DISK 类型时为挂载的 CVM ins-xxx；INSTANCE 类型时与 SourceResourceId 一致）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceCopyPairId: 所属CVM复制对ID（仅 DISK 类型且其 CVM 复制对存在时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCopyPairId: str
        :param _Percent: 复制进度。CVM 类型为所有挂载磁盘进度的平均值；DISK/CFS 类型为本盘进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _LatestProtectionTime: 最新保护时间点。当 CopyPairState=FULL_COPYING 时为 null（首次全量未完成）
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestProtectionTime: str
        :param _RecoveryPointObjective: RPO（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type RecoveryPointObjective: int
        :param _DataDirection: 数据方向。可选值：POSITIVE（正向）、REVERSE（反向，failover 后）。后端在 REVERSE 时已自动轮转 src/target 字段
        :type DataDirection: str
        :param _CreateFrom: 创建来源。可选值：LOCAL（本地侧创建）、PEER（对端创建）
        :type CreateFrom: str
        :param _DisasterRecoveryType: 容灾类型。可选值：CROSS_ZONE（跨可用区）、CROSS_REGION（跨地域）、CROSS_CLOUD（跨云）
        :type DisasterRecoveryType: str
        :param _PeerCloudName: 对端云名称（仅跨云场景）
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerCloudName: str
        :param _Rollbacking: 是否在回滚中（0/1）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rollbacking: int
        :param _RollbackPercent: 回滚进度
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackPercent: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AccountUin: 创建账户 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 创建协作者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _DrillGroupId: 演练组ID（用于演练组内过滤存量复制对，无演练时为 null）
注意：此字段可能返回 null，表示取不到有效值。
        :type DrillGroupId: str
        :param _ProtectionTimeSet: 保护时间点列表（仅当 QueryProtectionTime=true 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectionTimeSet: list of str
        :param _DiskCopyPairSet: CVM下挂载磁盘的复制对列表（仅 CopyPairType=INSTANCE 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCopyPairSet: list of DiskCopyPairForCvm
        :param _DeferredCreate: 是否为延迟创建模式（创建后固定不变）。仅 CVM 复制对返回
        :type DeferredCreate: bool
        :param _TargetCvmCreated: 目标 CVM 是否已真实创建（首次 failover 完成后置 true）。仅 CVM 复制对返回
        :type TargetCvmCreated: bool
        :param _CvmCreateParams: CVM 创建参数（JSON 字符串）。仅当请求传 QueryCvmCreateParams=true 且复制对处于 deferred_create=1 AND target_cvm_created=0 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmCreateParams: str
        """
        self._AppId = None
        self._CopyPairId = None
        self._CopyPairName = None
        self._SitePairId = None
        self._SitePairName = None
        self._ProtectGroupId = None
        self._ProtectGroupName = None
        self._CopyPairState = None
        self._CopyPairType = None
        self._SourceRegion = None
        self._SourceZone = None
        self._SourceVpc = None
        self._TargetRegion = None
        self._TargetZone = None
        self._TargetVpc = None
        self._SourceResourceId = None
        self._TargetResourceId = None
        self._InstanceId = None
        self._InstanceCopyPairId = None
        self._Percent = None
        self._LatestProtectionTime = None
        self._RecoveryPointObjective = None
        self._DataDirection = None
        self._CreateFrom = None
        self._DisasterRecoveryType = None
        self._PeerCloudName = None
        self._Rollbacking = None
        self._RollbackPercent = None
        self._CreateTime = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._DrillGroupId = None
        self._ProtectionTimeSet = None
        self._DiskCopyPairSet = None
        self._DeferredCreate = None
        self._TargetCvmCreated = None
        self._CvmCreateParams = None

    @property
    def AppId(self):
        r"""用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CopyPairId(self):
        r"""复制对ID（CVM 类型为 cvmcopypair-xxxxxxxx，DISK/CFS 类型为 copypair-xxxxxxxx）
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def CopyPairName(self):
        r"""复制对名称
        :rtype: str
        """
        return self._CopyPairName

    @CopyPairName.setter
    def CopyPairName(self, CopyPairName):
        self._CopyPairName = CopyPairName

    @property
    def SitePairId(self):
        r"""所属容灾站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SitePairName(self):
        r"""所属容灾站点对名称
        :rtype: str
        """
        return self._SitePairName

    @SitePairName.setter
    def SitePairName(self, SitePairName):
        self._SitePairName = SitePairName

    @property
    def ProtectGroupId(self):
        r"""保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def ProtectGroupName(self):
        r"""保护组名称
        :rtype: str
        """
        return self._ProtectGroupName

    @ProtectGroupName.setter
    def ProtectGroupName(self, ProtectGroupName):
        self._ProtectGroupName = ProtectGroupName

    @property
    def CopyPairState(self):
        r"""复制对状态。可选值：INIT、RUNNING、FULL_COPYING、INC_COPYING、NORMAL、DOWN、DEGRADE 等
        :rtype: str
        """
        return self._CopyPairState

    @CopyPairState.setter
    def CopyPairState(self, CopyPairState):
        self._CopyPairState = CopyPairState

    @property
    def CopyPairType(self):
        r"""复制对类型。可选值：DISK、INSTANCE、CFS
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType

    @property
    def SourceRegion(self):
        r"""生产地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""生产可用区
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def SourceVpc(self):
        r"""生产端VPC
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def TargetRegion(self):
        r"""容灾地域
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetZone(self):
        r"""容灾可用区
        :rtype: str
        """
        return self._TargetZone

    @TargetZone.setter
    def TargetZone(self, TargetZone):
        self._TargetZone = TargetZone

    @property
    def TargetVpc(self):
        r"""容灾端VPC
        :rtype: str
        """
        return self._TargetVpc

    @TargetVpc.setter
    def TargetVpc(self, TargetVpc):
        self._TargetVpc = TargetVpc

    @property
    def SourceResourceId(self):
        r"""生产资源ID。CVM 类型为源 InstanceId（ins-xxx）；DISK 类型为源 DiskId（disk-xxx）；CFS 类型为源 FilesystemId（cfs-xxx）
        :rtype: str
        """
        return self._SourceResourceId

    @SourceResourceId.setter
    def SourceResourceId(self, SourceResourceId):
        self._SourceResourceId = SourceResourceId

    @property
    def TargetResourceId(self):
        r"""容灾资源ID。语义同 SourceResourceId（CVM/DISK/CFS）。延迟创建模式且 CVM 未真实创建时为占位符 drp-xxx，CVM 创建后为真实 ins-xxx
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetResourceId

    @TargetResourceId.setter
    def TargetResourceId(self, TargetResourceId):
        self._TargetResourceId = TargetResourceId

    @property
    def InstanceId(self):
        r"""生产站点盘挂载的实例ID（DISK 类型时为挂载的 CVM ins-xxx；INSTANCE 类型时与 SourceResourceId 一致）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceCopyPairId(self):
        r"""所属CVM复制对ID（仅 DISK 类型且其 CVM 复制对存在时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceCopyPairId

    @InstanceCopyPairId.setter
    def InstanceCopyPairId(self, InstanceCopyPairId):
        self._InstanceCopyPairId = InstanceCopyPairId

    @property
    def Percent(self):
        r"""复制进度。CVM 类型为所有挂载磁盘进度的平均值；DISK/CFS 类型为本盘进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def LatestProtectionTime(self):
        r"""最新保护时间点。当 CopyPairState=FULL_COPYING 时为 null（首次全量未完成）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestProtectionTime

    @LatestProtectionTime.setter
    def LatestProtectionTime(self, LatestProtectionTime):
        self._LatestProtectionTime = LatestProtectionTime

    @property
    def RecoveryPointObjective(self):
        r"""RPO（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RecoveryPointObjective

    @RecoveryPointObjective.setter
    def RecoveryPointObjective(self, RecoveryPointObjective):
        self._RecoveryPointObjective = RecoveryPointObjective

    @property
    def DataDirection(self):
        r"""数据方向。可选值：POSITIVE（正向）、REVERSE（反向，failover 后）。后端在 REVERSE 时已自动轮转 src/target 字段
        :rtype: str
        """
        return self._DataDirection

    @DataDirection.setter
    def DataDirection(self, DataDirection):
        self._DataDirection = DataDirection

    @property
    def CreateFrom(self):
        r"""创建来源。可选值：LOCAL（本地侧创建）、PEER（对端创建）
        :rtype: str
        """
        return self._CreateFrom

    @CreateFrom.setter
    def CreateFrom(self, CreateFrom):
        self._CreateFrom = CreateFrom

    @property
    def DisasterRecoveryType(self):
        r"""容灾类型。可选值：CROSS_ZONE（跨可用区）、CROSS_REGION（跨地域）、CROSS_CLOUD（跨云）
        :rtype: str
        """
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def PeerCloudName(self):
        r"""对端云名称（仅跨云场景）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerCloudName

    @PeerCloudName.setter
    def PeerCloudName(self, PeerCloudName):
        self._PeerCloudName = PeerCloudName

    @property
    def Rollbacking(self):
        r"""是否在回滚中（0/1）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def RollbackPercent(self):
        r"""回滚进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

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
    def AccountUin(self):
        r"""创建账户 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""创建协作者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def DrillGroupId(self):
        r"""演练组ID（用于演练组内过滤存量复制对，无演练时为 null）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DrillGroupId

    @DrillGroupId.setter
    def DrillGroupId(self, DrillGroupId):
        self._DrillGroupId = DrillGroupId

    @property
    def ProtectionTimeSet(self):
        r"""保护时间点列表（仅当 QueryProtectionTime=true 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ProtectionTimeSet

    @ProtectionTimeSet.setter
    def ProtectionTimeSet(self, ProtectionTimeSet):
        self._ProtectionTimeSet = ProtectionTimeSet

    @property
    def DiskCopyPairSet(self):
        r"""CVM下挂载磁盘的复制对列表（仅 CopyPairType=INSTANCE 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiskCopyPairForCvm
        """
        return self._DiskCopyPairSet

    @DiskCopyPairSet.setter
    def DiskCopyPairSet(self, DiskCopyPairSet):
        self._DiskCopyPairSet = DiskCopyPairSet

    @property
    def DeferredCreate(self):
        r"""是否为延迟创建模式（创建后固定不变）。仅 CVM 复制对返回
        :rtype: bool
        """
        return self._DeferredCreate

    @DeferredCreate.setter
    def DeferredCreate(self, DeferredCreate):
        self._DeferredCreate = DeferredCreate

    @property
    def TargetCvmCreated(self):
        r"""目标 CVM 是否已真实创建（首次 failover 完成后置 true）。仅 CVM 复制对返回
        :rtype: bool
        """
        return self._TargetCvmCreated

    @TargetCvmCreated.setter
    def TargetCvmCreated(self, TargetCvmCreated):
        self._TargetCvmCreated = TargetCvmCreated

    @property
    def CvmCreateParams(self):
        r"""CVM 创建参数（JSON 字符串）。仅当请求传 QueryCvmCreateParams=true 且复制对处于 deferred_create=1 AND target_cvm_created=0 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CvmCreateParams

    @CvmCreateParams.setter
    def CvmCreateParams(self, CvmCreateParams):
        self._CvmCreateParams = CvmCreateParams


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._CopyPairId = params.get("CopyPairId")
        self._CopyPairName = params.get("CopyPairName")
        self._SitePairId = params.get("SitePairId")
        self._SitePairName = params.get("SitePairName")
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._ProtectGroupName = params.get("ProtectGroupName")
        self._CopyPairState = params.get("CopyPairState")
        self._CopyPairType = params.get("CopyPairType")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._SourceVpc = params.get("SourceVpc")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetZone = params.get("TargetZone")
        self._TargetVpc = params.get("TargetVpc")
        self._SourceResourceId = params.get("SourceResourceId")
        self._TargetResourceId = params.get("TargetResourceId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceCopyPairId = params.get("InstanceCopyPairId")
        self._Percent = params.get("Percent")
        self._LatestProtectionTime = params.get("LatestProtectionTime")
        self._RecoveryPointObjective = params.get("RecoveryPointObjective")
        self._DataDirection = params.get("DataDirection")
        self._CreateFrom = params.get("CreateFrom")
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._PeerCloudName = params.get("PeerCloudName")
        self._Rollbacking = params.get("Rollbacking")
        self._RollbackPercent = params.get("RollbackPercent")
        self._CreateTime = params.get("CreateTime")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._DrillGroupId = params.get("DrillGroupId")
        self._ProtectionTimeSet = params.get("ProtectionTimeSet")
        if params.get("DiskCopyPairSet") is not None:
            self._DiskCopyPairSet = []
            for item in params.get("DiskCopyPairSet"):
                obj = DiskCopyPairForCvm()
                obj._deserialize(item)
                self._DiskCopyPairSet.append(obj)
        self._DeferredCreate = params.get("DeferredCreate")
        self._TargetCvmCreated = params.get("TargetCvmCreated")
        self._CvmCreateParams = params.get("CvmCreateParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPairDeniedAction(AbstractModel):
    r"""复制对操作掩码

    """

    def __init__(self):
        r"""
        :param _CopyPairId: 复制对ID
        :type CopyPairId: str
        :param _DeniedActions: 被禁止的操作列表（Action名称数组）
        :type DeniedActions: list of DeniedAction
        """
        self._CopyPairId = None
        self._DeniedActions = None

    @property
    def CopyPairId(self):
        r"""复制对ID
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def DeniedActions(self):
        r"""被禁止的操作列表（Action名称数组）
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._CopyPairId = params.get("CopyPairId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPairPrice(AbstractModel):
    r"""复制对价格信息

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 后付费每小时原价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceHigh: 高精度后付费每小时原价，单位：元（字符串形式，避免精度丢失）
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceHigh: str
        :param _UnitPriceDiscount: 后付费每小时折扣价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _UnitPriceDiscountHigh: 高精度后付费每小时折扣价，单位：元（字符串形式，避免精度丢失）
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountHigh: str
        :param _Discount: 折扣，100 表示无折扣，80 表示 8 折
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: int
        :param _ChargeUnit: 计价单元，固定为 HOUR（按小时计费）
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _DetailPrices: 计费项目明细列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailPrices: list of CopyPairPriceDetail
        """
        self._UnitPrice = None
        self._UnitPriceHigh = None
        self._UnitPriceDiscount = None
        self._UnitPriceDiscountHigh = None
        self._Discount = None
        self._ChargeUnit = None
        self._DetailPrices = None

    @property
    def UnitPrice(self):
        r"""后付费每小时原价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceHigh(self):
        r"""高精度后付费每小时原价，单位：元（字符串形式，避免精度丢失）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def UnitPriceDiscount(self):
        r"""后付费每小时折扣价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceDiscountHigh(self):
        r"""高精度后付费每小时折扣价，单位：元（字符串形式，避免精度丢失）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def Discount(self):
        r"""折扣，100 表示无折扣，80 表示 8 折
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ChargeUnit(self):
        r"""计价单元，固定为 HOUR（按小时计费）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def DetailPrices(self):
        r"""计费项目明细列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CopyPairPriceDetail
        """
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        self._Discount = params.get("Discount")
        self._ChargeUnit = params.get("ChargeUnit")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = CopyPairPriceDetail()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPairPriceDetail(AbstractModel):
    r"""复制对价格明细项

    """

    def __init__(self):
        r"""
        :param _PriceName: 计费项目标识名称。取值：InstanceCount（容灾CVM实例数）、InstanceDataCapacity（容灾CVM实例数据量）
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceName: str
        :param _PriceTitle: 计费项目展示名称（跟随语言环境翻译）
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceTitle: str
        :param _UnitPrice: 该计费项每小时原价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceDiscount: 该计费项每小时折扣价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _Discount: 该计费项的折扣，100 表示无折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: int
        :param _ChargeUnit: 计价单元，固定为 HOUR
        :type ChargeUnit: str
        """
        self._PriceName = None
        self._PriceTitle = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._Discount = None
        self._ChargeUnit = None

    @property
    def PriceName(self):
        r"""计费项目标识名称。取值：InstanceCount（容灾CVM实例数）、InstanceDataCapacity（容灾CVM实例数据量）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def PriceTitle(self):
        r"""计费项目展示名称（跟随语言环境翻译）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PriceTitle

    @PriceTitle.setter
    def PriceTitle(self, PriceTitle):
        self._PriceTitle = PriceTitle

    @property
    def UnitPrice(self):
        r"""该计费项每小时原价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""该计费项每小时折扣价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def Discount(self):
        r"""该计费项的折扣，100 表示无折扣
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ChargeUnit(self):
        r"""计价单元，固定为 HOUR
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit


    def _deserialize(self, params):
        self._PriceName = params.get("PriceName")
        self._PriceTitle = params.get("PriceTitle")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._Discount = params.get("Discount")
        self._ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoBackupPolicyRequest(AbstractModel):
    r"""CreateAutoBackupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Policy: 定期备份的执行策略。
        :type Policy: list of Policy
        :param _IsPermanent: 通过该定期备份策略创建的备份是否永久保留。false表示非永久保留，true表示永久保留，默认为false。
        :type IsPermanent: bool
        :param _AutoBackupPolicyName: 定期备份策略的名称。
        :type AutoBackupPolicyName: str
        :param _IsActivated: 是否激活定期备份策略。
        :type IsActivated: bool
        :param _RetentionDays: 通过定期备份策略创建出的备份保留时间。
        :type RetentionDays: int
        :param _RetentionMonths: 该定期备份策略创建的备份可以保留的月数，该参数不可与IsPermanent/RetentionDays参数冲突。
        :type RetentionMonths: int
        :param _RetentionAmount: 通过该定期备份策略最多保留的备份个数，超过该个数限制后自动删除最先创建的备份，该参数不可与IsPermanent参数冲突。
        :type RetentionAmount: int
        :param _StorageType: 备份存储类型。COMMON表示走普通模式（不需要备份库），VAULT表示走备份库（必须关联一个备份库）。默认为COMMON
        :type StorageType: str
        :param _VaultId: 备份库ID，创建agent备份策略时必须指定。当StorageType为VAULT时必传。
        :type VaultId: str
        :param _AdvancedRetentionPolicy: 定期备份高级保留策略，该参数不可与IsPermanent参数冲突。
        :type AdvancedRetentionPolicy: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        self._Policy = None
        self._IsPermanent = None
        self._AutoBackupPolicyName = None
        self._IsActivated = None
        self._RetentionDays = None
        self._RetentionMonths = None
        self._RetentionAmount = None
        self._StorageType = None
        self._VaultId = None
        self._AdvancedRetentionPolicy = None

    @property
    def Policy(self):
        r"""定期备份的执行策略。
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def IsPermanent(self):
        r"""通过该定期备份策略创建的备份是否永久保留。false表示非永久保留，true表示永久保留，默认为false。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def AutoBackupPolicyName(self):
        r"""定期备份策略的名称。
        :rtype: str
        """
        return self._AutoBackupPolicyName

    @AutoBackupPolicyName.setter
    def AutoBackupPolicyName(self, AutoBackupPolicyName):
        self._AutoBackupPolicyName = AutoBackupPolicyName

    @property
    def IsActivated(self):
        r"""是否激活定期备份策略。
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def RetentionDays(self):
        r"""通过定期备份策略创建出的备份保留时间。
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def RetentionMonths(self):
        r"""该定期备份策略创建的备份可以保留的月数，该参数不可与IsPermanent/RetentionDays参数冲突。
        :rtype: int
        """
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        r"""通过该定期备份策略最多保留的备份个数，超过该个数限制后自动删除最先创建的备份，该参数不可与IsPermanent参数冲突。
        :rtype: int
        """
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def StorageType(self):
        r"""备份存储类型。COMMON表示走普通模式（不需要备份库），VAULT表示走备份库（必须关联一个备份库）。默认为COMMON
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VaultId(self):
        r"""备份库ID，创建agent备份策略时必须指定。当StorageType为VAULT时必传。
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def AdvancedRetentionPolicy(self):
        r"""定期备份高级保留策略，该参数不可与IsPermanent参数冲突。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._IsPermanent = params.get("IsPermanent")
        self._AutoBackupPolicyName = params.get("AutoBackupPolicyName")
        self._IsActivated = params.get("IsActivated")
        self._RetentionDays = params.get("RetentionDays")
        self._RetentionMonths = params.get("RetentionMonths")
        self._RetentionAmount = params.get("RetentionAmount")
        self._StorageType = params.get("StorageType")
        self._VaultId = params.get("VaultId")
        if params.get("AdvancedRetentionPolicy") is not None:
            self._AdvancedRetentionPolicy = AdvancedRetentionPolicy()
            self._AdvancedRetentionPolicy._deserialize(params.get("AdvancedRetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoBackupPolicyResponse(AbstractModel):
    r"""CreateAutoBackupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoBackupPolicyId: 定期备份策略ID。
        :type AutoBackupPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoBackupPolicyId = None
        self._RequestId = None

    @property
    def AutoBackupPolicyId(self):
        r"""定期备份策略ID。
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId

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
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        self._RequestId = params.get("RequestId")


class CreateBackupGroupRequest(AbstractModel):
    r"""CreateBackupGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 需要创建备份组的云硬盘ID列表。
        :type DiskIds: list of str
        :param _BackupGroupName: 备份组的名称
        :type BackupGroupName: str
        :param _Deadline: 指定备份组到期时间，如果未传入该参数，默认为永久保留。
        :type Deadline: str
        """
        self._DiskIds = None
        self._BackupGroupName = None
        self._Deadline = None

    @property
    def DiskIds(self):
        r"""需要创建备份组的云硬盘ID列表。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def BackupGroupName(self):
        r"""备份组的名称
        :rtype: str
        """
        return self._BackupGroupName

    @BackupGroupName.setter
    def BackupGroupName(self, BackupGroupName):
        self._BackupGroupName = BackupGroupName

    @property
    def Deadline(self):
        r"""指定备份组到期时间，如果未传入该参数，默认为永久保留。
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._BackupGroupName = params.get("BackupGroupName")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupGroupResponse(AbstractModel):
    r"""CreateBackupGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupId: 备份组ID。
        :type BackupGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupGroupId = None
        self._RequestId = None

    @property
    def BackupGroupId(self):
        r"""备份组ID。
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId

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
        self._BackupGroupId = params.get("BackupGroupId")
        self._RequestId = params.get("RequestId")


class CreateBackupVaultRequest(AbstractModel):
    r"""CreateBackupVault请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultName: 备份库名称
        :type VaultName: str
        :param _Description: 备份库描述
        :type Description: str
        :param _EncryptType: 加密方式: NONE/SSE-COS/SSE-KMS
        :type EncryptType: str
        :param _KmsKeyId: KMS密钥ID（SSE-KMS时使用）
        :type KmsKeyId: str
        """
        self._VaultName = None
        self._Description = None
        self._EncryptType = None
        self._KmsKeyId = None

    @property
    def VaultName(self):
        r"""备份库名称
        :rtype: str
        """
        return self._VaultName

    @VaultName.setter
    def VaultName(self, VaultName):
        self._VaultName = VaultName

    @property
    def Description(self):
        r"""备份库描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EncryptType(self):
        r"""加密方式: NONE/SSE-COS/SSE-KMS
        :rtype: str
        """
        return self._EncryptType

    @EncryptType.setter
    def EncryptType(self, EncryptType):
        self._EncryptType = EncryptType

    @property
    def KmsKeyId(self):
        r"""KMS密钥ID（SSE-KMS时使用）
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId


    def _deserialize(self, params):
        self._VaultName = params.get("VaultName")
        self._Description = params.get("Description")
        self._EncryptType = params.get("EncryptType")
        self._KmsKeyId = params.get("KmsKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupVaultResponse(AbstractModel):
    r"""CreateBackupVault返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultId: 备份库唯一ID
        :type VaultId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VaultId = None
        self._RequestId = None

    @property
    def VaultId(self):
        r"""备份库唯一ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

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
        self._VaultId = params.get("VaultId")
        self._RequestId = params.get("RequestId")


class CreateDisasterRecoveryProtectGroupRequest(AbstractModel):
    r"""CreateDisasterRecoveryProtectGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 所属容灾站点对id
        :type SitePairId: str
        :param _ProtectGroupType: 容灾保护组的产品类型
        :type ProtectGroupType: str
        :param _RecoveryPointObjective: 容灾保护组预期rpo, 单位分钟（当前仅支持15分钟）
        :type RecoveryPointObjective: int
        :param _ProtectGroupName: 容灾保护组的名称，最大长度不能超60个字符。
        :type ProtectGroupName: str
        :param _DataDirection: 数据复制方向， ['POSITIVE', 'REVERSE']
        :type DataDirection: str
        """
        self._SitePairId = None
        self._ProtectGroupType = None
        self._RecoveryPointObjective = None
        self._ProtectGroupName = None
        self._DataDirection = None

    @property
    def SitePairId(self):
        r"""所属容灾站点对id
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def ProtectGroupType(self):
        r"""容灾保护组的产品类型
        :rtype: str
        """
        return self._ProtectGroupType

    @ProtectGroupType.setter
    def ProtectGroupType(self, ProtectGroupType):
        self._ProtectGroupType = ProtectGroupType

    @property
    def RecoveryPointObjective(self):
        r"""容灾保护组预期rpo, 单位分钟（当前仅支持15分钟）
        :rtype: int
        """
        return self._RecoveryPointObjective

    @RecoveryPointObjective.setter
    def RecoveryPointObjective(self, RecoveryPointObjective):
        self._RecoveryPointObjective = RecoveryPointObjective

    @property
    def ProtectGroupName(self):
        r"""容灾保护组的名称，最大长度不能超60个字符。
        :rtype: str
        """
        return self._ProtectGroupName

    @ProtectGroupName.setter
    def ProtectGroupName(self, ProtectGroupName):
        self._ProtectGroupName = ProtectGroupName

    @property
    def DataDirection(self):
        r"""数据复制方向， ['POSITIVE', 'REVERSE']
        :rtype: str
        """
        return self._DataDirection

    @DataDirection.setter
    def DataDirection(self, DataDirection):
        self._DataDirection = DataDirection


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        self._ProtectGroupType = params.get("ProtectGroupType")
        self._RecoveryPointObjective = params.get("RecoveryPointObjective")
        self._ProtectGroupName = params.get("ProtectGroupName")
        self._DataDirection = params.get("DataDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoveryProtectGroupResponse(AbstractModel):
    r"""CreateDisasterRecoveryProtectGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupId: 创建的容灾保护组ID
        :type ProtectGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectGroupId = None
        self._RequestId = None

    @property
    def ProtectGroupId(self):
        r"""创建的容灾保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

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
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._RequestId = params.get("RequestId")


class CreateDisasterRecoverySitePairRequest(AbstractModel):
    r"""CreateDisasterRecoverySitePair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoveryType: 容灾策略的容灾类型，跨地域：CROSS_REGION，或跨可用区：CROSS_ZONE
        :type DisasterRecoveryType: str
        :param _SourceRegion: 生产站点地域
        :type SourceRegion: str
        :param _SourceZone: 容灾策略生产站点可用区
        :type SourceZone: str
        :param _TargetRegion: 容灾站点地域
        :type TargetRegion: str
        :param _TargetZone: 容灾策略容灾站点可用区
        :type TargetZone: str
        :param _SourceVpc: 容灾策略生产vpc
        :type SourceVpc: str
        :param _TargetVpc: 容灾策略容灾vpc
        :type TargetVpc: str
        :param _SitePairProductType: 容灾策略所属产品类型，包括DISK、CFS、INSTANCE
        :type SitePairProductType: str
        :param _SitePairName: 容灾策略的名称，最大长度为60个字符。
        :type SitePairName: str
        :param _CopyType: 容灾策略复制技术SYN/ASY
        :type CopyType: str
        """
        self._DisasterRecoveryType = None
        self._SourceRegion = None
        self._SourceZone = None
        self._TargetRegion = None
        self._TargetZone = None
        self._SourceVpc = None
        self._TargetVpc = None
        self._SitePairProductType = None
        self._SitePairName = None
        self._CopyType = None

    @property
    def DisasterRecoveryType(self):
        r"""容灾策略的容灾类型，跨地域：CROSS_REGION，或跨可用区：CROSS_ZONE
        :rtype: str
        """
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def SourceRegion(self):
        r"""生产站点地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""容灾策略生产站点可用区
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def TargetRegion(self):
        r"""容灾站点地域
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetZone(self):
        r"""容灾策略容灾站点可用区
        :rtype: str
        """
        return self._TargetZone

    @TargetZone.setter
    def TargetZone(self, TargetZone):
        self._TargetZone = TargetZone

    @property
    def SourceVpc(self):
        r"""容灾策略生产vpc
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def TargetVpc(self):
        r"""容灾策略容灾vpc
        :rtype: str
        """
        return self._TargetVpc

    @TargetVpc.setter
    def TargetVpc(self, TargetVpc):
        self._TargetVpc = TargetVpc

    @property
    def SitePairProductType(self):
        r"""容灾策略所属产品类型，包括DISK、CFS、INSTANCE
        :rtype: str
        """
        return self._SitePairProductType

    @SitePairProductType.setter
    def SitePairProductType(self, SitePairProductType):
        self._SitePairProductType = SitePairProductType

    @property
    def SitePairName(self):
        r"""容灾策略的名称，最大长度为60个字符。
        :rtype: str
        """
        return self._SitePairName

    @SitePairName.setter
    def SitePairName(self, SitePairName):
        self._SitePairName = SitePairName

    @property
    def CopyType(self):
        r"""容灾策略复制技术SYN/ASY
        :rtype: str
        """
        return self._CopyType

    @CopyType.setter
    def CopyType(self, CopyType):
        self._CopyType = CopyType


    def _deserialize(self, params):
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetZone = params.get("TargetZone")
        self._SourceVpc = params.get("SourceVpc")
        self._TargetVpc = params.get("TargetVpc")
        self._SitePairProductType = params.get("SitePairProductType")
        self._SitePairName = params.get("SitePairName")
        self._CopyType = params.get("CopyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverySitePairResponse(AbstractModel):
    r"""CreateDisasterRecoverySitePair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 容灾站点对ID
        :type SitePairId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SitePairId = None
        self._RequestId = None

    @property
    def SitePairId(self):
        r"""容灾站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

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
        self._SitePairId = params.get("SitePairId")
        self._RequestId = params.get("RequestId")


class CreateDisasterRecoveryVpcMappingRequest(AbstractModel):
    r"""CreateDisasterRecoveryVpcMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceVpcId: 源端VPC ID
        :type SourceVpcId: str
        :param _SourceSubnetId: 源端子网ID
        :type SourceSubnetId: str
        :param _TargetVpcId: 目标端VPC ID
        :type TargetVpcId: str
        :param _TargetSubnetId: 目标端子网ID
        :type TargetSubnetId: str
        :param _SitePairId: 站点对ID
        :type SitePairId: str
        """
        self._SourceVpcId = None
        self._SourceSubnetId = None
        self._TargetVpcId = None
        self._TargetSubnetId = None
        self._SitePairId = None

    @property
    def SourceVpcId(self):
        r"""源端VPC ID
        :rtype: str
        """
        return self._SourceVpcId

    @SourceVpcId.setter
    def SourceVpcId(self, SourceVpcId):
        self._SourceVpcId = SourceVpcId

    @property
    def SourceSubnetId(self):
        r"""源端子网ID
        :rtype: str
        """
        return self._SourceSubnetId

    @SourceSubnetId.setter
    def SourceSubnetId(self, SourceSubnetId):
        self._SourceSubnetId = SourceSubnetId

    @property
    def TargetVpcId(self):
        r"""目标端VPC ID
        :rtype: str
        """
        return self._TargetVpcId

    @TargetVpcId.setter
    def TargetVpcId(self, TargetVpcId):
        self._TargetVpcId = TargetVpcId

    @property
    def TargetSubnetId(self):
        r"""目标端子网ID
        :rtype: str
        """
        return self._TargetSubnetId

    @TargetSubnetId.setter
    def TargetSubnetId(self, TargetSubnetId):
        self._TargetSubnetId = TargetSubnetId

    @property
    def SitePairId(self):
        r"""站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId


    def _deserialize(self, params):
        self._SourceVpcId = params.get("SourceVpcId")
        self._SourceSubnetId = params.get("SourceSubnetId")
        self._TargetVpcId = params.get("TargetVpcId")
        self._TargetSubnetId = params.get("TargetSubnetId")
        self._SitePairId = params.get("SitePairId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoveryVpcMappingResponse(AbstractModel):
    r"""CreateDisasterRecoveryVpcMapping返回参数结构体

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


class CreateFileBackupPlanRequest(AbstractModel):
    r"""CreateFileBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: <p>备份策略ID</p>
        :type PolicyId: str
        :param _BackupStorageId: <p>备份库ID</p>
        :type BackupStorageId: str
        :param _PlanName: <p>计划名称</p>
        :type PlanName: str
        :param _Resources: <p>实例配置列表，[1,20]</p>
        :type Resources: list of ResourcePlan
        :param _ResourceType: <p>资源类型</p><p>枚举值：</p><ul><li>CVM_AGENT： CVM文件备份</li><li>CFS_AGENT： 文件系统备份</li><li>COS_AGENT： COS备份</li></ul><p>默认值：CVM_AGENT</p>
        :type ResourceType: str
        """
        self._PolicyId = None
        self._BackupStorageId = None
        self._PlanName = None
        self._Resources = None
        self._ResourceType = None

    @property
    def PolicyId(self):
        r"""<p>备份策略ID</p>
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def BackupStorageId(self):
        r"""<p>备份库ID</p>
        :rtype: str
        """
        return self._BackupStorageId

    @BackupStorageId.setter
    def BackupStorageId(self, BackupStorageId):
        self._BackupStorageId = BackupStorageId

    @property
    def PlanName(self):
        r"""<p>计划名称</p>
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def Resources(self):
        r"""<p>实例配置列表，[1,20]</p>
        :rtype: list of ResourcePlan
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ResourceType(self):
        r"""<p>资源类型</p><p>枚举值：</p><ul><li>CVM_AGENT： CVM文件备份</li><li>CFS_AGENT： 文件系统备份</li><li>COS_AGENT： COS备份</li></ul><p>默认值：CVM_AGENT</p>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._BackupStorageId = params.get("BackupStorageId")
        self._PlanName = params.get("PlanName")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourcePlan()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileBackupPlanResponse(AbstractModel):
    r"""CreateFileBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanIds: <p>备份计划 ID 列表</p>
        :type PlanIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanIds = None
        self._RequestId = None

    @property
    def PlanIds(self):
        r"""<p>备份计划 ID 列表</p>
        :rtype: list of str
        """
        return self._PlanIds

    @PlanIds.setter
    def PlanIds(self, PlanIds):
        self._PlanIds = PlanIds

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
        self._PlanIds = params.get("PlanIds")
        self._RequestId = params.get("RequestId")


class CreateFileBackupRequest(AbstractModel):
    r"""CreateFileBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID列表
        :type ResourceId: str
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _BackupPaths: 备份路径列表，1~20 个
        :type BackupPaths: list of str
        :param _IncludeFileTypes: 包含文件类型，0~20 个
        :type IncludeFileTypes: list of str
        :param _ExcludePatterns: 排除文件路径列表，0~20 个
        :type ExcludePatterns: list of str
        :param _ExcludeSystemDirectories: 是否排除系统目录
        :type ExcludeSystemDirectories: bool
        :param _BackupStorageId: 备份库ID
        :type BackupStorageId: str
        :param _Deadline: 备份到期时间
        :type Deadline: str
        :param _BackupName: 备份名称
        :type BackupName: str
        """
        self._ResourceId = None
        self._PlanId = None
        self._BackupPaths = None
        self._IncludeFileTypes = None
        self._ExcludePatterns = None
        self._ExcludeSystemDirectories = None
        self._BackupStorageId = None
        self._Deadline = None
        self._BackupName = None

    @property
    def ResourceId(self):
        r"""资源ID列表
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PlanId(self):
        r"""计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def BackupPaths(self):
        r"""备份路径列表，1~20 个
        :rtype: list of str
        """
        return self._BackupPaths

    @BackupPaths.setter
    def BackupPaths(self, BackupPaths):
        self._BackupPaths = BackupPaths

    @property
    def IncludeFileTypes(self):
        r"""包含文件类型，0~20 个
        :rtype: list of str
        """
        return self._IncludeFileTypes

    @IncludeFileTypes.setter
    def IncludeFileTypes(self, IncludeFileTypes):
        self._IncludeFileTypes = IncludeFileTypes

    @property
    def ExcludePatterns(self):
        r"""排除文件路径列表，0~20 个
        :rtype: list of str
        """
        return self._ExcludePatterns

    @ExcludePatterns.setter
    def ExcludePatterns(self, ExcludePatterns):
        self._ExcludePatterns = ExcludePatterns

    @property
    def ExcludeSystemDirectories(self):
        r"""是否排除系统目录
        :rtype: bool
        """
        return self._ExcludeSystemDirectories

    @ExcludeSystemDirectories.setter
    def ExcludeSystemDirectories(self, ExcludeSystemDirectories):
        self._ExcludeSystemDirectories = ExcludeSystemDirectories

    @property
    def BackupStorageId(self):
        r"""备份库ID
        :rtype: str
        """
        return self._BackupStorageId

    @BackupStorageId.setter
    def BackupStorageId(self, BackupStorageId):
        self._BackupStorageId = BackupStorageId

    @property
    def Deadline(self):
        r"""备份到期时间
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def BackupName(self):
        r"""备份名称
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._PlanId = params.get("PlanId")
        self._BackupPaths = params.get("BackupPaths")
        self._IncludeFileTypes = params.get("IncludeFileTypes")
        self._ExcludePatterns = params.get("ExcludePatterns")
        self._ExcludeSystemDirectories = params.get("ExcludeSystemDirectories")
        self._BackupStorageId = params.get("BackupStorageId")
        self._Deadline = params.get("Deadline")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileBackupResponse(AbstractModel):
    r"""CreateFileBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份Id
        :type BackupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupId = None
        self._RequestId = None

    @property
    def BackupId(self):
        r"""备份Id
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

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
        self._BackupId = params.get("BackupId")
        self._RequestId = params.get("RequestId")


class CreateFileRestoreTaskRequest(AbstractModel):
    r"""CreateFileRestoreTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConflictStrategy: 冲突处理策略：skip-跳过/"         "overwrite-覆盖/newer-保留较新的版本/"         "if_changed-内容变化时覆盖，默认overwrite
        :type ConflictStrategy: str
        """
        self._ConflictStrategy = None

    @property
    def ConflictStrategy(self):
        r"""冲突处理策略：skip-跳过/"         "overwrite-覆盖/newer-保留较新的版本/"         "if_changed-内容变化时覆盖，默认overwrite
        :rtype: str
        """
        return self._ConflictStrategy

    @ConflictStrategy.setter
    def ConflictStrategy(self, ConflictStrategy):
        self._ConflictStrategy = ConflictStrategy


    def _deserialize(self, params):
        self._ConflictStrategy = params.get("ConflictStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileRestoreTaskResponse(AbstractModel):
    r"""CreateFileRestoreTask返回参数结构体

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


class CreateInstanceCopyPairRequest(AbstractModel):
    r"""CreateInstanceCopyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupId: 所属保护组
        :type ProtectGroupId: str
        :param _CreateTargetInstanceParameters: 目标端CVM创建参数列表（1~10 个）
        :type CreateTargetInstanceParameters: list of CreateInstanceModel
        :param _InstanceCopyPairName: 复制对名称，不传则新名称为"未命名"
        :type InstanceCopyPairName: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性
        :type ClientToken: str
        :param _RecoveryPointObjective: 用户期望的RPO，单位分钟，目前仅支持15分钟
        :type RecoveryPointObjective: int
        """
        self._ProtectGroupId = None
        self._CreateTargetInstanceParameters = None
        self._InstanceCopyPairName = None
        self._ClientToken = None
        self._RecoveryPointObjective = None

    @property
    def ProtectGroupId(self):
        r"""所属保护组
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def CreateTargetInstanceParameters(self):
        r"""目标端CVM创建参数列表（1~10 个）
        :rtype: list of CreateInstanceModel
        """
        return self._CreateTargetInstanceParameters

    @CreateTargetInstanceParameters.setter
    def CreateTargetInstanceParameters(self, CreateTargetInstanceParameters):
        self._CreateTargetInstanceParameters = CreateTargetInstanceParameters

    @property
    def InstanceCopyPairName(self):
        r"""复制对名称，不传则新名称为"未命名"
        :rtype: str
        """
        return self._InstanceCopyPairName

    @InstanceCopyPairName.setter
    def InstanceCopyPairName(self, InstanceCopyPairName):
        self._InstanceCopyPairName = InstanceCopyPairName

    @property
    def ClientToken(self):
        r"""用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def RecoveryPointObjective(self):
        r"""用户期望的RPO，单位分钟，目前仅支持15分钟
        :rtype: int
        """
        return self._RecoveryPointObjective

    @RecoveryPointObjective.setter
    def RecoveryPointObjective(self, RecoveryPointObjective):
        self._RecoveryPointObjective = RecoveryPointObjective


    def _deserialize(self, params):
        self._ProtectGroupId = params.get("ProtectGroupId")
        if params.get("CreateTargetInstanceParameters") is not None:
            self._CreateTargetInstanceParameters = []
            for item in params.get("CreateTargetInstanceParameters"):
                obj = CreateInstanceModel()
                obj._deserialize(item)
                self._CreateTargetInstanceParameters.append(obj)
        self._InstanceCopyPairName = params.get("InstanceCopyPairName")
        self._ClientToken = params.get("ClientToken")
        self._RecoveryPointObjective = params.get("RecoveryPointObjective")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceCopyPairResponse(AbstractModel):
    r"""CreateInstanceCopyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 创建的CVM复制对ID列表
        :type CopyPairIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CopyPairIds = None
        self._RequestId = None

    @property
    def CopyPairIds(self):
        r"""创建的CVM复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

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
        self._CopyPairIds = params.get("CopyPairIds")
        self._RequestId = params.get("RequestId")


class CreateInstanceDrillPairsRequest(AbstractModel):
    r"""CreateInstanceDrillPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupId: 所属容灾保护组
        :type ProtectGroupId: str
        :param _DrillPairGroupVpc: 演练组vpc
        :type DrillPairGroupVpc: str
        :param _DrillPairGroupName: 文件系统复制对名称,不传则新名称为“未命名”
        :type DrillPairGroupName: str
        :param _CreationToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性
        :type CreationToken: str
        :param _DrillPairGroupId: 指定创建入哪个演练组
        :type DrillPairGroupId: str
        :param _CreateTargetInstanceParameters: 创建目标演练实例的参数列表
        :type CreateTargetInstanceParameters: list of CreateInstanceModel
        """
        self._ProtectGroupId = None
        self._DrillPairGroupVpc = None
        self._DrillPairGroupName = None
        self._CreationToken = None
        self._DrillPairGroupId = None
        self._CreateTargetInstanceParameters = None

    @property
    def ProtectGroupId(self):
        r"""所属容灾保护组
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def DrillPairGroupVpc(self):
        r"""演练组vpc
        :rtype: str
        """
        return self._DrillPairGroupVpc

    @DrillPairGroupVpc.setter
    def DrillPairGroupVpc(self, DrillPairGroupVpc):
        self._DrillPairGroupVpc = DrillPairGroupVpc

    @property
    def DrillPairGroupName(self):
        r"""文件系统复制对名称,不传则新名称为“未命名”
        :rtype: str
        """
        return self._DrillPairGroupName

    @DrillPairGroupName.setter
    def DrillPairGroupName(self, DrillPairGroupName):
        self._DrillPairGroupName = DrillPairGroupName

    @property
    def CreationToken(self):
        r"""用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性
        :rtype: str
        """
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def DrillPairGroupId(self):
        r"""指定创建入哪个演练组
        :rtype: str
        """
        return self._DrillPairGroupId

    @DrillPairGroupId.setter
    def DrillPairGroupId(self, DrillPairGroupId):
        self._DrillPairGroupId = DrillPairGroupId

    @property
    def CreateTargetInstanceParameters(self):
        r"""创建目标演练实例的参数列表
        :rtype: list of CreateInstanceModel
        """
        return self._CreateTargetInstanceParameters

    @CreateTargetInstanceParameters.setter
    def CreateTargetInstanceParameters(self, CreateTargetInstanceParameters):
        self._CreateTargetInstanceParameters = CreateTargetInstanceParameters


    def _deserialize(self, params):
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._DrillPairGroupVpc = params.get("DrillPairGroupVpc")
        self._DrillPairGroupName = params.get("DrillPairGroupName")
        self._CreationToken = params.get("CreationToken")
        self._DrillPairGroupId = params.get("DrillPairGroupId")
        if params.get("CreateTargetInstanceParameters") is not None:
            self._CreateTargetInstanceParameters = []
            for item in params.get("CreateTargetInstanceParameters"):
                obj = CreateInstanceModel()
                obj._deserialize(item)
                self._CreateTargetInstanceParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceDrillPairsResponse(AbstractModel):
    r"""CreateInstanceDrillPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairIds: 演练对ID列表
        :type DrillPairIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DrillPairIds = None
        self._RequestId = None

    @property
    def DrillPairIds(self):
        r"""演练对ID列表
        :rtype: list of str
        """
        return self._DrillPairIds

    @DrillPairIds.setter
    def DrillPairIds(self, DrillPairIds):
        self._DrillPairIds = DrillPairIds

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
        self._DrillPairIds = params.get("DrillPairIds")
        self._RequestId = params.get("RequestId")


class CreateInstanceModel(AbstractModel):
    r"""创建cvm参数

    """

    def __init__(self):
        r"""
        :param _SourceInstanceId: 源CVM ID
        :type SourceInstanceId: str
        :param _InstanceChargeType: 实例计费模式
        :type InstanceChargeType: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.bdrc.v20260330.models.Placement`
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _SystemDisk: 指定系统盘规格
        :type SystemDisk: :class:`tencentcloud.bdrc.v20260330.models.DiskModel`
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.bdrc.v20260330.models.InstanceChargePrepaid`
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _DataDisks: 指定数据盘规格列表
        :type DataDisks: list of DiskModel
        :param _VirtualPrivateCloud: 私有网络相关信息配置
        :type VirtualPrivateCloud: :class:`tencentcloud.bdrc.v20260330.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.bdrc.v20260330.models.InternetAccessible`
        :param _InstanceName: 实例显示名称。不传则新实例名为"未命名"。最大长度不能超60个字节。
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置
        :type LoginSettings: :class:`tencentcloud.bdrc.v20260330.models.LoginSettings`
        :param _EnhancedService: 增强服务配置
        :type EnhancedService: :class:`tencentcloud.bdrc.v20260330.models.EnhancedService`
        :param _SpotPrice: 竞价实例最高出价
        :type SpotPrice: str
        :param _HostName: 实例主机名
        :type HostName: str
        :param _UserData: 提供给实例使用的用户数据
        :type UserData: str
        :param _DisasterRecoverGroupIds: 放置群组ID
        :type DisasterRecoverGroupIds: list of str
        :param _StoppedMode: 关机计费模式，默认关机收费（KEEP_CHARGING / STOP_CHARGING），仅 CreateInstanceCopyPair 场景生效
        :type StoppedMode: str
        :param _CopyPairId: 容灾演练使用的复制对ID，仅 CreateInstanceDrillPairs 场景生效
        :type CopyPairId: str
        :param _RecoveryTime: 容灾演练的恢复时间点，仅 CreateInstanceDrillPairs 场景生效
        :type RecoveryTime: str
        """
        self._SourceInstanceId = None
        self._InstanceChargeType = None
        self._Placement = None
        self._ImageId = None
        self._SystemDisk = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._LoginSettings = None
        self._EnhancedService = None
        self._SpotPrice = None
        self._HostName = None
        self._UserData = None
        self._DisasterRecoverGroupIds = None
        self._StoppedMode = None
        self._CopyPairId = None
        self._RecoveryTime = None

    @property
    def SourceInstanceId(self):
        r"""源CVM ID
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def InstanceChargeType(self):
        r"""实例计费模式
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Placement(self):
        r"""实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

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
    def SystemDisk(self):
        r"""指定系统盘规格
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DiskModel`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceChargePrepaid(self):
        r"""预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DataDisks(self):
        r"""指定数据盘规格列表
        :rtype: list of DiskModel
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        r"""私有网络相关信息配置
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        r"""公网带宽相关信息设置
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        r"""实例显示名称。不传则新实例名为"未命名"。最大长度不能超60个字节。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        r"""实例登录设置
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def EnhancedService(self):
        r"""增强服务配置
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def SpotPrice(self):
        r"""竞价实例最高出价
        :rtype: str
        """
        return self._SpotPrice

    @SpotPrice.setter
    def SpotPrice(self, SpotPrice):
        self._SpotPrice = SpotPrice

    @property
    def HostName(self):
        r"""实例主机名
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def UserData(self):
        r"""提供给实例使用的用户数据
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DisasterRecoverGroupIds(self):
        r"""放置群组ID
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def StoppedMode(self):
        r"""关机计费模式，默认关机收费（KEEP_CHARGING / STOP_CHARGING），仅 CreateInstanceCopyPair 场景生效
        :rtype: str
        """
        return self._StoppedMode

    @StoppedMode.setter
    def StoppedMode(self, StoppedMode):
        self._StoppedMode = StoppedMode

    @property
    def CopyPairId(self):
        r"""容灾演练使用的复制对ID，仅 CreateInstanceDrillPairs 场景生效
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def RecoveryTime(self):
        r"""容灾演练的恢复时间点，仅 CreateInstanceDrillPairs 场景生效
        :rtype: str
        """
        return self._RecoveryTime

    @RecoveryTime.setter
    def RecoveryTime(self, RecoveryTime):
        self._RecoveryTime = RecoveryTime


    def _deserialize(self, params):
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = DiskModel()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskModel()
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
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._SpotPrice = params.get("SpotPrice")
        self._HostName = params.get("HostName")
        self._UserData = params.get("UserData")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._StoppedMode = params.get("StoppedMode")
        self._CopyPairId = params.get("CopyPairId")
        self._RecoveryTime = params.get("RecoveryTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupMappingRequest(AbstractModel):
    r"""CreateSecurityGroupMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcSecurityGroupId: 生产端实例绑定的安全组ID
        :type SrcSecurityGroupId: str
        :param _TargetSecurityGroupId: 容灾端实例绑定的安全组ID
        :type TargetSecurityGroupId: str
        :param _SitePairId: 安全组映射所属的站点对ID。
        :type SitePairId: str
        """
        self._SrcSecurityGroupId = None
        self._TargetSecurityGroupId = None
        self._SitePairId = None

    @property
    def SrcSecurityGroupId(self):
        r"""生产端实例绑定的安全组ID
        :rtype: str
        """
        return self._SrcSecurityGroupId

    @SrcSecurityGroupId.setter
    def SrcSecurityGroupId(self, SrcSecurityGroupId):
        self._SrcSecurityGroupId = SrcSecurityGroupId

    @property
    def TargetSecurityGroupId(self):
        r"""容灾端实例绑定的安全组ID
        :rtype: str
        """
        return self._TargetSecurityGroupId

    @TargetSecurityGroupId.setter
    def TargetSecurityGroupId(self, TargetSecurityGroupId):
        self._TargetSecurityGroupId = TargetSecurityGroupId

    @property
    def SitePairId(self):
        r"""安全组映射所属的站点对ID。
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId


    def _deserialize(self, params):
        self._SrcSecurityGroupId = params.get("SrcSecurityGroupId")
        self._TargetSecurityGroupId = params.get("TargetSecurityGroupId")
        self._SitePairId = params.get("SitePairId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupMappingResponse(AbstractModel):
    r"""CreateSecurityGroupMapping返回参数结构体

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


class CrossCloudDetails(AbstractModel):
    r"""跨云信息

    """

    def __init__(self):
        r"""
        :param _SourceCloudName: 源端云名称（跨云对端云名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCloudName: str
        :param _TargetCloudName: 目标端云名称（跨云本端云名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetCloudName: str
        :param _SourceAppId: 源端云AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAppId: int
        :param _SourceUin: 源端云主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceUin: str
        :param _SourceSubAccountUin: 源端云子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceSubAccountUin: str
        :param _SourceUserName: 源端云用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceUserName: str
        :param _TargetAppId: 目标端云AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAppId: int
        :param _TargetUin: 目标端云主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetUin: str
        :param _TargetSubAccountUin: 目标端云子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetSubAccountUin: str
        :param _PeerRegionName: 对端云的地域显示名
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerRegionName: str
        :param _PeerZoneName: 对端云的可用区显示名
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerZoneName: str
        :param _PeerVpcName: 对端云的VPC显示名
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerVpcName: str
        """
        self._SourceCloudName = None
        self._TargetCloudName = None
        self._SourceAppId = None
        self._SourceUin = None
        self._SourceSubAccountUin = None
        self._SourceUserName = None
        self._TargetAppId = None
        self._TargetUin = None
        self._TargetSubAccountUin = None
        self._PeerRegionName = None
        self._PeerZoneName = None
        self._PeerVpcName = None

    @property
    def SourceCloudName(self):
        r"""源端云名称（跨云对端云名称）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceCloudName

    @SourceCloudName.setter
    def SourceCloudName(self, SourceCloudName):
        self._SourceCloudName = SourceCloudName

    @property
    def TargetCloudName(self):
        r"""目标端云名称（跨云本端云名称）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetCloudName

    @TargetCloudName.setter
    def TargetCloudName(self, TargetCloudName):
        self._TargetCloudName = TargetCloudName

    @property
    def SourceAppId(self):
        r"""源端云AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SourceAppId

    @SourceAppId.setter
    def SourceAppId(self, SourceAppId):
        self._SourceAppId = SourceAppId

    @property
    def SourceUin(self):
        r"""源端云主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceUin

    @SourceUin.setter
    def SourceUin(self, SourceUin):
        self._SourceUin = SourceUin

    @property
    def SourceSubAccountUin(self):
        r"""源端云子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceSubAccountUin

    @SourceSubAccountUin.setter
    def SourceSubAccountUin(self, SourceSubAccountUin):
        self._SourceSubAccountUin = SourceSubAccountUin

    @property
    def SourceUserName(self):
        r"""源端云用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceUserName

    @SourceUserName.setter
    def SourceUserName(self, SourceUserName):
        self._SourceUserName = SourceUserName

    @property
    def TargetAppId(self):
        r"""目标端云AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TargetAppId

    @TargetAppId.setter
    def TargetAppId(self, TargetAppId):
        self._TargetAppId = TargetAppId

    @property
    def TargetUin(self):
        r"""目标端云主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetSubAccountUin(self):
        r"""目标端云子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetSubAccountUin

    @TargetSubAccountUin.setter
    def TargetSubAccountUin(self, TargetSubAccountUin):
        self._TargetSubAccountUin = TargetSubAccountUin

    @property
    def PeerRegionName(self):
        r"""对端云的地域显示名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerRegionName

    @PeerRegionName.setter
    def PeerRegionName(self, PeerRegionName):
        self._PeerRegionName = PeerRegionName

    @property
    def PeerZoneName(self):
        r"""对端云的可用区显示名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerZoneName

    @PeerZoneName.setter
    def PeerZoneName(self, PeerZoneName):
        self._PeerZoneName = PeerZoneName

    @property
    def PeerVpcName(self):
        r"""对端云的VPC显示名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerVpcName

    @PeerVpcName.setter
    def PeerVpcName(self, PeerVpcName):
        self._PeerVpcName = PeerVpcName


    def _deserialize(self, params):
        self._SourceCloudName = params.get("SourceCloudName")
        self._TargetCloudName = params.get("TargetCloudName")
        self._SourceAppId = params.get("SourceAppId")
        self._SourceUin = params.get("SourceUin")
        self._SourceSubAccountUin = params.get("SourceSubAccountUin")
        self._SourceUserName = params.get("SourceUserName")
        self._TargetAppId = params.get("TargetAppId")
        self._TargetUin = params.get("TargetUin")
        self._TargetSubAccountUin = params.get("TargetSubAccountUin")
        self._PeerRegionName = params.get("PeerRegionName")
        self._PeerZoneName = params.get("PeerZoneName")
        self._PeerVpcName = params.get("PeerVpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoBackupPoliciesRequest(AbstractModel):
    r"""DeleteAutoBackupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoBackupPolicyIds: 备份策略 ID 列表
        :type AutoBackupPolicyIds: list of str
        """
        self._AutoBackupPolicyIds = None

    @property
    def AutoBackupPolicyIds(self):
        r"""备份策略 ID 列表
        :rtype: list of str
        """
        return self._AutoBackupPolicyIds

    @AutoBackupPolicyIds.setter
    def AutoBackupPolicyIds(self, AutoBackupPolicyIds):
        self._AutoBackupPolicyIds = AutoBackupPolicyIds


    def _deserialize(self, params):
        self._AutoBackupPolicyIds = params.get("AutoBackupPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoBackupPoliciesResponse(AbstractModel):
    r"""DeleteAutoBackupPolicies返回参数结构体

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


class DeleteBackupGroupsRequest(AbstractModel):
    r"""DeleteBackupGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupIds: 备份组ID列表。
        :type BackupGroupIds: list of str
        """
        self._BackupGroupIds = None

    @property
    def BackupGroupIds(self):
        r"""备份组ID列表。
        :rtype: list of str
        """
        return self._BackupGroupIds

    @BackupGroupIds.setter
    def BackupGroupIds(self, BackupGroupIds):
        self._BackupGroupIds = BackupGroupIds


    def _deserialize(self, params):
        self._BackupGroupIds = params.get("BackupGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupGroupsResponse(AbstractModel):
    r"""DeleteBackupGroups返回参数结构体

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


class DeleteBackupVaultsRequest(AbstractModel):
    r"""DeleteBackupVaults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultIds: 备份库 ID 列表
        :type VaultIds: list of str
        """
        self._VaultIds = None

    @property
    def VaultIds(self):
        r"""备份库 ID 列表
        :rtype: list of str
        """
        return self._VaultIds

    @VaultIds.setter
    def VaultIds(self, VaultIds):
        self._VaultIds = VaultIds


    def _deserialize(self, params):
        self._VaultIds = params.get("VaultIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupVaultsResponse(AbstractModel):
    r"""DeleteBackupVaults返回参数结构体

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


class DeleteCopyPairsRequest(AbstractModel):
    r"""DeleteCopyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 要删除的复制对ID列表（长度 1~10）
        :type CopyPairIds: list of str
        :param _CopyPairType: 要删除复制对的类型，可选值：DISK、INSTANCE、CFS
        :type CopyPairType: str
        :param _DeleteTargetResource: 是否一并删除容灾站点云盘，默认 true（容灾盘数据可能处于中间状态，保留也无法正常使用）
        :type DeleteTargetResource: bool
        """
        self._CopyPairIds = None
        self._CopyPairType = None
        self._DeleteTargetResource = None

    @property
    def CopyPairIds(self):
        r"""要删除的复制对ID列表（长度 1~10）
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""要删除复制对的类型，可选值：DISK、INSTANCE、CFS
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType

    @property
    def DeleteTargetResource(self):
        r"""是否一并删除容灾站点云盘，默认 true（容灾盘数据可能处于中间状态，保留也无法正常使用）
        :rtype: bool
        """
        return self._DeleteTargetResource

    @DeleteTargetResource.setter
    def DeleteTargetResource(self, DeleteTargetResource):
        self._DeleteTargetResource = DeleteTargetResource


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        self._DeleteTargetResource = params.get("DeleteTargetResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCopyPairsResponse(AbstractModel):
    r"""DeleteCopyPairs返回参数结构体

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


class DeleteDisasterRecoveryProtectGroupsRequest(AbstractModel):
    r"""DeleteDisasterRecoveryProtectGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroups: 删除容灾保护组ID列表，最多10个
        :type ProtectGroups: list of str
        """
        self._ProtectGroups = None

    @property
    def ProtectGroups(self):
        r"""删除容灾保护组ID列表，最多10个
        :rtype: list of str
        """
        return self._ProtectGroups

    @ProtectGroups.setter
    def ProtectGroups(self, ProtectGroups):
        self._ProtectGroups = ProtectGroups


    def _deserialize(self, params):
        self._ProtectGroups = params.get("ProtectGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoveryProtectGroupsResponse(AbstractModel):
    r"""DeleteDisasterRecoveryProtectGroups返回参数结构体

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


class DeleteDisasterRecoverySitePairsRequest(AbstractModel):
    r"""DeleteDisasterRecoverySitePairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairIds: 删除容灾策略ID列表
        :type SitePairIds: list of str
        """
        self._SitePairIds = None

    @property
    def SitePairIds(self):
        r"""删除容灾策略ID列表
        :rtype: list of str
        """
        return self._SitePairIds

    @SitePairIds.setter
    def SitePairIds(self, SitePairIds):
        self._SitePairIds = SitePairIds


    def _deserialize(self, params):
        self._SitePairIds = params.get("SitePairIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverySitePairsResponse(AbstractModel):
    r"""DeleteDisasterRecoverySitePairs返回参数结构体

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


class DeleteDisasterRecoveryVpcMappingRequest(AbstractModel):
    r"""DeleteDisasterRecoveryVpcMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcMappingIds: 删除容灾vpc映射主键id列表
        :type VpcMappingIds: list of int non-negative
        """
        self._VpcMappingIds = None

    @property
    def VpcMappingIds(self):
        r"""删除容灾vpc映射主键id列表
        :rtype: list of int non-negative
        """
        return self._VpcMappingIds

    @VpcMappingIds.setter
    def VpcMappingIds(self, VpcMappingIds):
        self._VpcMappingIds = VpcMappingIds


    def _deserialize(self, params):
        self._VpcMappingIds = params.get("VpcMappingIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoveryVpcMappingResponse(AbstractModel):
    r"""DeleteDisasterRecoveryVpcMapping返回参数结构体

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


class DeleteDrillPairResult(AbstractModel):
    r"""删除演练对结果

    """

    def __init__(self):
        r"""
        :param _DrillPairId: 演练对ID。
        :type DrillPairId: str
        :param _Code: 删除结果码。成功为 Success，失败为对应错误码（如 InternalError.ComponentError）。
        :type Code: str
        :param _Message: 删除结果描述信息，成功时为空串。
        :type Message: str
        """
        self._DrillPairId = None
        self._Code = None
        self._Message = None

    @property
    def DrillPairId(self):
        r"""演练对ID。
        :rtype: str
        """
        return self._DrillPairId

    @DrillPairId.setter
    def DrillPairId(self, DrillPairId):
        self._DrillPairId = DrillPairId

    @property
    def Code(self):
        r"""删除结果码。成功为 Success，失败为对应错误码（如 InternalError.ComponentError）。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""删除结果描述信息，成功时为空串。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DrillPairId = params.get("DrillPairId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDrillPairsRequest(AbstractModel):
    r"""DeleteDrillPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairType: 要删除演练对的类型，其类型枚举跟复制对保持一致。枚举值：DISK / INSTANCE / CFS。
        :type DrillPairType: str
        :param _DrillPairIds: 要删除的演练对列表。长度范围 [1, 10]。
        :type DrillPairIds: list of str
        :param _DrillGroupIds: 要删除的演练组id列表。
        :type DrillGroupIds: list of str
        :param _DeleteDrillResource: 是否一并删除演练CFS/CVM/DISK演练资源。
        :type DeleteDrillResource: bool
        """
        self._DrillPairType = None
        self._DrillPairIds = None
        self._DrillGroupIds = None
        self._DeleteDrillResource = None

    @property
    def DrillPairType(self):
        r"""要删除演练对的类型，其类型枚举跟复制对保持一致。枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._DrillPairType

    @DrillPairType.setter
    def DrillPairType(self, DrillPairType):
        self._DrillPairType = DrillPairType

    @property
    def DrillPairIds(self):
        r"""要删除的演练对列表。长度范围 [1, 10]。
        :rtype: list of str
        """
        return self._DrillPairIds

    @DrillPairIds.setter
    def DrillPairIds(self, DrillPairIds):
        self._DrillPairIds = DrillPairIds

    @property
    def DrillGroupIds(self):
        r"""要删除的演练组id列表。
        :rtype: list of str
        """
        return self._DrillGroupIds

    @DrillGroupIds.setter
    def DrillGroupIds(self, DrillGroupIds):
        self._DrillGroupIds = DrillGroupIds

    @property
    def DeleteDrillResource(self):
        r"""是否一并删除演练CFS/CVM/DISK演练资源。
        :rtype: bool
        """
        return self._DeleteDrillResource

    @DeleteDrillResource.setter
    def DeleteDrillResource(self, DeleteDrillResource):
        self._DeleteDrillResource = DeleteDrillResource


    def _deserialize(self, params):
        self._DrillPairType = params.get("DrillPairType")
        self._DrillPairIds = params.get("DrillPairIds")
        self._DrillGroupIds = params.get("DrillGroupIds")
        self._DeleteDrillResource = params.get("DeleteDrillResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDrillPairsResponse(AbstractModel):
    r"""DeleteDrillPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteDrillPairResultSet: 删除演练对的逐条结果列表。
        :type DeleteDrillPairResultSet: list of DeleteDrillPairResult
        :param _DeleteDrillPairGroupSet: 成功标记为删除的演练组ID列表。
        :type DeleteDrillPairGroupSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteDrillPairResultSet = None
        self._DeleteDrillPairGroupSet = None
        self._RequestId = None

    @property
    def DeleteDrillPairResultSet(self):
        r"""删除演练对的逐条结果列表。
        :rtype: list of DeleteDrillPairResult
        """
        return self._DeleteDrillPairResultSet

    @DeleteDrillPairResultSet.setter
    def DeleteDrillPairResultSet(self, DeleteDrillPairResultSet):
        self._DeleteDrillPairResultSet = DeleteDrillPairResultSet

    @property
    def DeleteDrillPairGroupSet(self):
        r"""成功标记为删除的演练组ID列表。
        :rtype: list of str
        """
        return self._DeleteDrillPairGroupSet

    @DeleteDrillPairGroupSet.setter
    def DeleteDrillPairGroupSet(self, DeleteDrillPairGroupSet):
        self._DeleteDrillPairGroupSet = DeleteDrillPairGroupSet

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
        if params.get("DeleteDrillPairResultSet") is not None:
            self._DeleteDrillPairResultSet = []
            for item in params.get("DeleteDrillPairResultSet"):
                obj = DeleteDrillPairResult()
                obj._deserialize(item)
                self._DeleteDrillPairResultSet.append(obj)
        self._DeleteDrillPairGroupSet = params.get("DeleteDrillPairGroupSet")
        self._RequestId = params.get("RequestId")


class DeleteFileBackupPlansRequest(AbstractModel):
    r"""DeleteFileBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanIds: 备份点 ID 列表
        :type PlanIds: list of str
        """
        self._PlanIds = None

    @property
    def PlanIds(self):
        r"""备份点 ID 列表
        :rtype: list of str
        """
        return self._PlanIds

    @PlanIds.setter
    def PlanIds(self, PlanIds):
        self._PlanIds = PlanIds


    def _deserialize(self, params):
        self._PlanIds = params.get("PlanIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileBackupPlansResponse(AbstractModel):
    r"""DeleteFileBackupPlans返回参数结构体

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


class DeleteFileBackupsRequest(AbstractModel):
    r"""DeleteFileBackups请求参数结构体

    """


class DeleteFileBackupsResponse(AbstractModel):
    r"""DeleteFileBackups返回参数结构体

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


class DeleteSecurityGroupMappingRequest(AbstractModel):
    r"""DeleteSecurityGroupMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 要删除安全组映射所属的站点对ID
        :type SitePairId: str
        :param _SecurityGroupMappingIds: 要删除的安全组映射ID列表
        :type SecurityGroupMappingIds: list of str
        """
        self._SitePairId = None
        self._SecurityGroupMappingIds = None

    @property
    def SitePairId(self):
        r"""要删除安全组映射所属的站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SecurityGroupMappingIds(self):
        r"""要删除的安全组映射ID列表
        :rtype: list of str
        """
        return self._SecurityGroupMappingIds

    @SecurityGroupMappingIds.setter
    def SecurityGroupMappingIds(self, SecurityGroupMappingIds):
        self._SecurityGroupMappingIds = SecurityGroupMappingIds


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        self._SecurityGroupMappingIds = params.get("SecurityGroupMappingIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupMappingResponse(AbstractModel):
    r"""DeleteSecurityGroupMapping返回参数结构体

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


class DeniedAction(AbstractModel):
    r"""备份不能执行的接口。

    """

    def __init__(self):
        r"""
        :param _Action: 不能操作的接口名。
        :type Action: str
        :param _Message: 接口不能操作的原因。
        :type Message: str
        :param _Code: 接口不能操作对应提示的错误码。
        :type Code: str
        """
        self._Action = None
        self._Message = None
        self._Code = None

    @property
    def Action(self):
        r"""不能操作的接口名。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Message(self):
        r"""接口不能操作的原因。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""接口不能操作对应提示的错误码。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoBackupPoliciesRequest(AbstractModel):
    r"""DescribeAutoBackupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。支持以下过滤条件：\n"              "auto-backup-policy-id - 定期快照策略ID，如asp-xxx。\n"              "auto-backup-policy-state - 定期快照策略状态。\n"              "auto-backup-policy-name - 定期快照策略名称，支持模糊匹配。\n"              "tag - 按标签键值对过滤，需包含Key和/或Value。\n"              "tag-key - 按标签键过滤。\n"              "tag-value - 按标签值过滤。\n"              "tag:tag-key - 按指定标签键的标签值过滤。\n"              "vault-id - 备份库ID过滤。\n"              "storage-type - 存储类型过滤"              "（COMMON：普通模式，VAULT：备份库模式）。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大1000
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件。支持以下过滤条件：\n"              "auto-backup-policy-id - 定期快照策略ID，如asp-xxx。\n"              "auto-backup-policy-state - 定期快照策略状态。\n"              "auto-backup-policy-name - 定期快照策略名称，支持模糊匹配。\n"              "tag - 按标签键值对过滤，需包含Key和/或Value。\n"              "tag-key - 按标签键过滤。\n"              "tag-value - 按标签值过滤。\n"              "tag:tag-key - 按指定标签键的标签值过滤。\n"              "vault-id - 备份库ID过滤。\n"              "storage-type - 存储类型过滤"              "（COMMON：普通模式，VAULT：备份库模式）。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoBackupPoliciesResponse(AbstractModel):
    r"""DescribeAutoBackupPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _AutoBackupPolicySet: 备份策略列表详情。
        :type AutoBackupPolicySet: list of AutoBackupPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoBackupPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoBackupPolicySet(self):
        r"""备份策略列表详情。
        :rtype: list of AutoBackupPolicy
        """
        return self._AutoBackupPolicySet

    @AutoBackupPolicySet.setter
    def AutoBackupPolicySet(self, AutoBackupPolicySet):
        self._AutoBackupPolicySet = AutoBackupPolicySet

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
        if params.get("AutoBackupPolicySet") is not None:
            self._AutoBackupPolicySet = []
            for item in params.get("AutoBackupPolicySet"):
                obj = AutoBackupPolicy()
                obj._deserialize(item)
                self._AutoBackupPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupGroupRollbackTasksRequest(AbstractModel):
    r"""DescribeBackupGroupRollbackTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，支持恢复任务ID（task-id）、备份组ID（backup-group-id）、源实例ID（source-instance-id）、目标实例ID（target-instance-id）、恢复状态（status）和回滚类型（rollback-type）过滤
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大1000
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件，支持恢复任务ID（task-id）、备份组ID（backup-group-id）、源实例ID（source-instance-id）、目标实例ID（target-instance-id）、恢复状态（status）和回滚类型（rollback-type）过滤
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupGroupRollbackTasksResponse(AbstractModel):
    r"""DescribeBackupGroupRollbackTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _RollbackTaskSet: 备份组恢复详情。
        :type RollbackTaskSet: list of BackupGroupRollbackTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RollbackTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RollbackTaskSet(self):
        r"""备份组恢复详情。
        :rtype: list of BackupGroupRollbackTask
        """
        return self._RollbackTaskSet

    @RollbackTaskSet.setter
    def RollbackTaskSet(self, RollbackTaskSet):
        self._RollbackTaskSet = RollbackTaskSet

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
        if params.get("RollbackTaskSet") is not None:
            self._RollbackTaskSet = []
            for item in params.get("RollbackTaskSet"):
                obj = BackupGroupRollbackTask()
                obj._deserialize(item)
                self._RollbackTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupGroupsDeniedActionsRequest(AbstractModel):
    r"""DescribeBackupGroupsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupIds: 备份组列表
        :type BackupGroupIds: list of str
        """
        self._BackupGroupIds = None

    @property
    def BackupGroupIds(self):
        r"""备份组列表
        :rtype: list of str
        """
        return self._BackupGroupIds

    @BackupGroupIds.setter
    def BackupGroupIds(self, BackupGroupIds):
        self._BackupGroupIds = BackupGroupIds


    def _deserialize(self, params):
        self._BackupGroupIds = params.get("BackupGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupGroupsDeniedActionsResponse(AbstractModel):
    r"""DescribeBackupGroupsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupDeniedActionSet: 备份组不允许操作信息
        :type BackupGroupDeniedActionSet: list of BackupGroupDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupGroupDeniedActionSet = None
        self._RequestId = None

    @property
    def BackupGroupDeniedActionSet(self):
        r"""备份组不允许操作信息
        :rtype: list of BackupGroupDeniedAction
        """
        return self._BackupGroupDeniedActionSet

    @BackupGroupDeniedActionSet.setter
    def BackupGroupDeniedActionSet(self, BackupGroupDeniedActionSet):
        self._BackupGroupDeniedActionSet = BackupGroupDeniedActionSet

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
        if params.get("BackupGroupDeniedActionSet") is not None:
            self._BackupGroupDeniedActionSet = []
            for item in params.get("BackupGroupDeniedActionSet"):
                obj = BackupGroupDeniedAction()
                obj._deserialize(item)
                self._BackupGroupDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupGroupsRequest(AbstractModel):
    r"""DescribeBackupGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。backup-group-id - Array of String - 是否必填：否 -（过滤条件）按备份组ID过滤 ;backup-group-state - Array of String - 是否必填：否 -（过滤条件）按备份组状态过滤。(NORMAL: 正常 | CREATING:创建中 | ROLLBACKING:回滚中) ;backup-group-name - Array of String - 是否必填：否 -（过滤条件）按备份组名称过滤 ;backup-id - Array of String - 是否必填：否 -（过滤条件）按备份组内的备份ID过滤
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段。目前支持CREATE_TIME。
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件。backup-group-id - Array of String - 是否必填：否 -（过滤条件）按备份组ID过滤 ;backup-group-state - Array of String - 是否必填：否 -（过滤条件）按备份组状态过滤。(NORMAL: 正常 | CREATING:创建中 | ROLLBACKING:回滚中) ;backup-group-name - Array of String - 是否必填：否 -（过滤条件）按备份组名称过滤 ;backup-id - Array of String - 是否必填：否 -（过滤条件）按备份组内的备份ID过滤
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段。目前支持CREATE_TIME。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupGroupsResponse(AbstractModel):
    r"""DescribeBackupGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _BackupGroupSet: 备份列表详情。
        :type BackupGroupSet: list of BackupGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupGroupSet(self):
        r"""备份列表详情。
        :rtype: list of BackupGroup
        """
        return self._BackupGroupSet

    @BackupGroupSet.setter
    def BackupGroupSet(self, BackupGroupSet):
        self._BackupGroupSet = BackupGroupSet

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
        if params.get("BackupGroupSet") is not None:
            self._BackupGroupSet = []
            for item in params.get("BackupGroupSet"):
                obj = BackupGroup()
                obj._deserialize(item)
                self._BackupGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupInstancesRequest(AbstractModel):
    r"""DescribeBackupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。;instance-id - Array of String - 是否必填：否 -（过滤条件）按实例ID过滤。;auto-backup-policy-id - Array of String - 是否必填：否 -（过滤条件）按照实例绑定的定期备份策略过滤。;auto-backup-policy-name - Array of String - 是否必填：否 -（过滤条件）按照云硬盘绑定的定期备份策略名称过滤。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件。;instance-id - Array of String - 是否必填：否 -（过滤条件）按实例ID过滤。;auto-backup-policy-id - Array of String - 是否必填：否 -（过滤条件）按照实例绑定的定期备份策略过滤。;auto-backup-policy-name - Array of String - 是否必填：否 -（过滤条件）按照云硬盘绑定的定期备份策略名称过滤。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupInstancesResponse(AbstractModel):
    r"""DescribeBackupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的受保护实例总数量
        :type TotalCount: int
        :param _BackupInstanceSet: 符合条件的受保护实例详情
        :type BackupInstanceSet: list of BackupInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的受保护实例总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupInstanceSet(self):
        r"""符合条件的受保护实例详情
        :rtype: list of BackupInstance
        """
        return self._BackupInstanceSet

    @BackupInstanceSet.setter
    def BackupInstanceSet(self, BackupInstanceSet):
        self._BackupInstanceSet = BackupInstanceSet

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
        if params.get("BackupInstanceSet") is not None:
            self._BackupInstanceSet = []
            for item in params.get("BackupInstanceSet"):
                obj = BackupInstance()
                obj._deserialize(item)
                self._BackupInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupOverviewGeneralRequest(AbstractModel):
    r"""DescribeBackupOverviewGeneral请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AllRegions: <p>是否查询全部地域。false-仅当前地域（默认），true-全部地域汇总</p>
        :type AllRegions: bool
        """
        self._AllRegions = None

    @property
    def AllRegions(self):
        r"""<p>是否查询全部地域。false-仅当前地域（默认），true-全部地域汇总</p>
        :rtype: bool
        """
        return self._AllRegions

    @AllRegions.setter
    def AllRegions(self, AllRegions):
        self._AllRegions = AllRegions


    def _deserialize(self, params):
        self._AllRegions = params.get("AllRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupOverviewGeneralResponse(AbstractModel):
    r"""DescribeBackupOverviewGeneral返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceBackupOverview: <p>整机备份（CVM 备份组）概览数据</p>
        :type InstanceBackupOverview: :class:`tencentcloud.bdrc.v20260330.models.InstanceBackupOverview`
        :param _FileBackupOverview: <p>文件备份概览数据</p>
        :type FileBackupOverview: :class:`tencentcloud.bdrc.v20260330.models.FileBackupOverview`
        :param _BackupPolicyOverview: <p>备份策略概览</p>
        :type BackupPolicyOverview: :class:`tencentcloud.bdrc.v20260330.models.BackupPolicyOverview`
        :param _BackupVaultOverview: <p>备份库概览</p>
        :type BackupVaultOverview: :class:`tencentcloud.bdrc.v20260330.models.BackupVaultOverview`
        :param _ProtectedResourceOverview: <p>受保护资源概览</p>
        :type ProtectedResourceOverview: :class:`tencentcloud.bdrc.v20260330.models.ProtectedResourceOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceBackupOverview = None
        self._FileBackupOverview = None
        self._BackupPolicyOverview = None
        self._BackupVaultOverview = None
        self._ProtectedResourceOverview = None
        self._RequestId = None

    @property
    def InstanceBackupOverview(self):
        r"""<p>整机备份（CVM 备份组）概览数据</p>
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.InstanceBackupOverview`
        """
        return self._InstanceBackupOverview

    @InstanceBackupOverview.setter
    def InstanceBackupOverview(self, InstanceBackupOverview):
        self._InstanceBackupOverview = InstanceBackupOverview

    @property
    def FileBackupOverview(self):
        r"""<p>文件备份概览数据</p>
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.FileBackupOverview`
        """
        return self._FileBackupOverview

    @FileBackupOverview.setter
    def FileBackupOverview(self, FileBackupOverview):
        self._FileBackupOverview = FileBackupOverview

    @property
    def BackupPolicyOverview(self):
        r"""<p>备份策略概览</p>
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.BackupPolicyOverview`
        """
        return self._BackupPolicyOverview

    @BackupPolicyOverview.setter
    def BackupPolicyOverview(self, BackupPolicyOverview):
        self._BackupPolicyOverview = BackupPolicyOverview

    @property
    def BackupVaultOverview(self):
        r"""<p>备份库概览</p>
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.BackupVaultOverview`
        """
        return self._BackupVaultOverview

    @BackupVaultOverview.setter
    def BackupVaultOverview(self, BackupVaultOverview):
        self._BackupVaultOverview = BackupVaultOverview

    @property
    def ProtectedResourceOverview(self):
        r"""<p>受保护资源概览</p>
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ProtectedResourceOverview`
        """
        return self._ProtectedResourceOverview

    @ProtectedResourceOverview.setter
    def ProtectedResourceOverview(self, ProtectedResourceOverview):
        self._ProtectedResourceOverview = ProtectedResourceOverview

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
        if params.get("InstanceBackupOverview") is not None:
            self._InstanceBackupOverview = InstanceBackupOverview()
            self._InstanceBackupOverview._deserialize(params.get("InstanceBackupOverview"))
        if params.get("FileBackupOverview") is not None:
            self._FileBackupOverview = FileBackupOverview()
            self._FileBackupOverview._deserialize(params.get("FileBackupOverview"))
        if params.get("BackupPolicyOverview") is not None:
            self._BackupPolicyOverview = BackupPolicyOverview()
            self._BackupPolicyOverview._deserialize(params.get("BackupPolicyOverview"))
        if params.get("BackupVaultOverview") is not None:
            self._BackupVaultOverview = BackupVaultOverview()
            self._BackupVaultOverview._deserialize(params.get("BackupVaultOverview"))
        if params.get("ProtectedResourceOverview") is not None:
            self._ProtectedResourceOverview = ProtectedResourceOverview()
            self._ProtectedResourceOverview._deserialize(params.get("ProtectedResourceOverview"))
        self._RequestId = params.get("RequestId")


class DescribeBackupPlansRequest(AbstractModel):
    r"""DescribeBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，支持instance-id和auto-backup-policy-id
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大100
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件，支持instance-id和auto-backup-policy-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlansResponse(AbstractModel):
    r"""DescribeBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _BackupPlanSet: 备份列表详情。
        :type BackupPlanSet: list of BackupPlan
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupPlanSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupPlanSet(self):
        r"""备份列表详情。
        :rtype: list of BackupPlan
        """
        return self._BackupPlanSet

    @BackupPlanSet.setter
    def BackupPlanSet(self, BackupPlanSet):
        self._BackupPlanSet = BackupPlanSet

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
        if params.get("BackupPlanSet") is not None:
            self._BackupPlanSet = []
            for item in params.get("BackupPlanSet"):
                obj = BackupPlan()
                obj._deserialize(item)
                self._BackupPlanSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupVaultsDeniedActionsRequest(AbstractModel):
    r"""DescribeBackupVaultsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultIds: 备份库ID列表
        :type VaultIds: list of str
        """
        self._VaultIds = None

    @property
    def VaultIds(self):
        r"""备份库ID列表
        :rtype: list of str
        """
        return self._VaultIds

    @VaultIds.setter
    def VaultIds(self, VaultIds):
        self._VaultIds = VaultIds


    def _deserialize(self, params):
        self._VaultIds = params.get("VaultIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupVaultsDeniedActionsResponse(AbstractModel):
    r"""DescribeBackupVaultsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupVaultDeniedActionSet: 备份库不允许操作信息
        :type BackupVaultDeniedActionSet: list of VaultDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupVaultDeniedActionSet = None
        self._RequestId = None

    @property
    def BackupVaultDeniedActionSet(self):
        r"""备份库不允许操作信息
        :rtype: list of VaultDeniedAction
        """
        return self._BackupVaultDeniedActionSet

    @BackupVaultDeniedActionSet.setter
    def BackupVaultDeniedActionSet(self, BackupVaultDeniedActionSet):
        self._BackupVaultDeniedActionSet = BackupVaultDeniedActionSet

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
        if params.get("BackupVaultDeniedActionSet") is not None:
            self._BackupVaultDeniedActionSet = []
            for item in params.get("BackupVaultDeniedActionSet"):
                obj = VaultDeniedAction()
                obj._deserialize(item)
                self._BackupVaultDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupVaultsRequest(AbstractModel):
    r"""DescribeBackupVaults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultIds: 备份库ID列表
        :type VaultIds: list of str
        :param _Filters: 过滤条件，支持instance-id和auto-backup-policy-id
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大1000
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._VaultIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def VaultIds(self):
        r"""备份库ID列表
        :rtype: list of str
        """
        return self._VaultIds

    @VaultIds.setter
    def VaultIds(self, VaultIds):
        self._VaultIds = VaultIds

    @property
    def Filters(self):
        r"""过滤条件，支持instance-id和auto-backup-policy-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._VaultIds = params.get("VaultIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupVaultsResponse(AbstractModel):
    r"""DescribeBackupVaults返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _BackupVaultSet: 备份库列表详情。
        :type BackupVaultSet: list of BackupVault
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupVaultSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupVaultSet(self):
        r"""备份库列表详情。
        :rtype: list of BackupVault
        """
        return self._BackupVaultSet

    @BackupVaultSet.setter
    def BackupVaultSet(self, BackupVaultSet):
        self._BackupVaultSet = BackupVaultSet

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
        if params.get("BackupVaultSet") is not None:
            self._BackupVaultSet = []
            for item in params.get("BackupVaultSet"):
                obj = BackupVault()
                obj._deserialize(item)
                self._BackupVaultSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCommonBackupPointsRequest(AbstractModel):
    r"""DescribeCommonBackupPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例列表
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例列表
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
        


class DescribeCommonBackupPointsResponse(AbstractModel):
    r"""DescribeCommonBackupPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _CommonBackupPointSet: 共同备份点详情。
        :type CommonBackupPointSet: list of CommonBackupPoint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CommonBackupPointSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CommonBackupPointSet(self):
        r"""共同备份点详情。
        :rtype: list of CommonBackupPoint
        """
        return self._CommonBackupPointSet

    @CommonBackupPointSet.setter
    def CommonBackupPointSet(self, CommonBackupPointSet):
        self._CommonBackupPointSet = CommonBackupPointSet

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
        if params.get("CommonBackupPointSet") is not None:
            self._CommonBackupPointSet = []
            for item in params.get("CommonBackupPointSet"):
                obj = CommonBackupPoint()
                obj._deserialize(item)
                self._CommonBackupPointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCopyPairsDeniedActionsRequest(AbstractModel):
    r"""DescribeCopyPairsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 复制对ID列表
        :type CopyPairIds: list of str
        :param _CopyPairType: 要查询复制对的类型，枚举值：DISK（云硬盘）、INSTANCE（云服务器）、CFS（文件存储）
        :type CopyPairType: str
        """
        self._CopyPairIds = None
        self._CopyPairType = None

    @property
    def CopyPairIds(self):
        r"""复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""要查询复制对的类型，枚举值：DISK（云硬盘）、INSTANCE（云服务器）、CFS（文件存储）
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCopyPairsDeniedActionsResponse(AbstractModel):
    r"""DescribeCopyPairsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairDeniedActionSet: 复制对操作掩码列表，返回每个复制对被禁止执行的操作
        :type CopyPairDeniedActionSet: list of CopyPairDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CopyPairDeniedActionSet = None
        self._RequestId = None

    @property
    def CopyPairDeniedActionSet(self):
        r"""复制对操作掩码列表，返回每个复制对被禁止执行的操作
        :rtype: list of CopyPairDeniedAction
        """
        return self._CopyPairDeniedActionSet

    @CopyPairDeniedActionSet.setter
    def CopyPairDeniedActionSet(self, CopyPairDeniedActionSet):
        self._CopyPairDeniedActionSet = CopyPairDeniedActionSet

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
        if params.get("CopyPairDeniedActionSet") is not None:
            self._CopyPairDeniedActionSet = []
            for item in params.get("CopyPairDeniedActionSet"):
                obj = CopyPairDeniedAction()
                obj._deserialize(item)
                self._CopyPairDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCopyPairsRequest(AbstractModel):
    r"""DescribeCopyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairType: <p>要查询复制对的类型，可选值：DISK、INSTANCE、CFS</p>
        :type CopyPairType: str
        :param _CopyPairIds: <p>要查询复制对ID列表</p>
        :type CopyPairIds: list of str
        :param _Filters: <p>过滤条件，详见过滤条件表。支持的Name：disaster-recovery-site-pair-id、target-resource-id、source-resource-id、copy-pair-id、copy-pair-name</p>
        :type Filters: list of FilterModel
        :param _Offset: <p>偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认为20，最大值为100。</p>
        :type Limit: int
        :param _Order: <p>输出结果按升序还是降序，可选值：ASC、DESC</p>
        :type Order: str
        :param _OrderField: <p>输出结果的排序字段，可选值：CREATE_TIME</p>
        :type OrderField: str
        :param _QueryProtectionTime: <p>是否要查询保护时间点列表，默认 false。当设置为 true 时，必须同时传入 CopyPairIds 参数。</p>
        :type QueryProtectionTime: bool
        :param _GetAllCopyPair: <p>是否查询跨云+非跨云全部复制对，默认 false</p>
        :type GetAllCopyPair: bool
        :param _QueryCvmCreateParams: <p>是否要查询 CVM 创建参数（仅对延迟创建模式且目标 CVM 未创建的复制对生效），默认为true。为 true 时，每条 deferred_create=1 AND target_cvm_created=0 的 CVM 复制对出参会附带 CvmCreateParams 字段</p>
        :type QueryCvmCreateParams: bool
        :param _CreateFrom: <p>复制对创建来源过滤。不传则查询所有；传 LOCAL 仅查本端创建的复制对，传 PEER 仅查对端创建的复制对。</p><p>枚举值：</p><ul><li>LOCAL： 仅查本端创建的复制对</li><li>PEER： 仅查对端创建的复制对</li></ul>
        :type CreateFrom: str
        """
        self._CopyPairType = None
        self._CopyPairIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._QueryProtectionTime = None
        self._GetAllCopyPair = None
        self._QueryCvmCreateParams = None
        self._CreateFrom = None

    @property
    def CopyPairType(self):
        r"""<p>要查询复制对的类型，可选值：DISK、INSTANCE、CFS</p>
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType

    @property
    def CopyPairIds(self):
        r"""<p>要查询复制对ID列表</p>
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def Filters(self):
        r"""<p>过滤条件，详见过滤条件表。支持的Name：disaster-recovery-site-pair-id、target-resource-id、source-resource-id、copy-pair-id、copy-pair-name</p>
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认为20，最大值为100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""<p>输出结果按升序还是降序，可选值：ASC、DESC</p>
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""<p>输出结果的排序字段，可选值：CREATE_TIME</p>
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def QueryProtectionTime(self):
        r"""<p>是否要查询保护时间点列表，默认 false。当设置为 true 时，必须同时传入 CopyPairIds 参数。</p>
        :rtype: bool
        """
        return self._QueryProtectionTime

    @QueryProtectionTime.setter
    def QueryProtectionTime(self, QueryProtectionTime):
        self._QueryProtectionTime = QueryProtectionTime

    @property
    def GetAllCopyPair(self):
        r"""<p>是否查询跨云+非跨云全部复制对，默认 false</p>
        :rtype: bool
        """
        return self._GetAllCopyPair

    @GetAllCopyPair.setter
    def GetAllCopyPair(self, GetAllCopyPair):
        self._GetAllCopyPair = GetAllCopyPair

    @property
    def QueryCvmCreateParams(self):
        r"""<p>是否要查询 CVM 创建参数（仅对延迟创建模式且目标 CVM 未创建的复制对生效），默认为true。为 true 时，每条 deferred_create=1 AND target_cvm_created=0 的 CVM 复制对出参会附带 CvmCreateParams 字段</p>
        :rtype: bool
        """
        return self._QueryCvmCreateParams

    @QueryCvmCreateParams.setter
    def QueryCvmCreateParams(self, QueryCvmCreateParams):
        self._QueryCvmCreateParams = QueryCvmCreateParams

    @property
    def CreateFrom(self):
        r"""<p>复制对创建来源过滤。不传则查询所有；传 LOCAL 仅查本端创建的复制对，传 PEER 仅查对端创建的复制对。</p><p>枚举值：</p><ul><li>LOCAL： 仅查本端创建的复制对</li><li>PEER： 仅查对端创建的复制对</li></ul>
        :rtype: str
        """
        return self._CreateFrom

    @CreateFrom.setter
    def CreateFrom(self, CreateFrom):
        self._CreateFrom = CreateFrom


    def _deserialize(self, params):
        self._CopyPairType = params.get("CopyPairType")
        self._CopyPairIds = params.get("CopyPairIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._QueryProtectionTime = params.get("QueryProtectionTime")
        self._GetAllCopyPair = params.get("GetAllCopyPair")
        self._QueryCvmCreateParams = params.get("QueryCvmCreateParams")
        self._CreateFrom = params.get("CreateFrom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCopyPairsResponse(AbstractModel):
    r"""DescribeCopyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的复制对总数</p>
        :type TotalCount: int
        :param _CopyPairSet: <p>复制对列表。</p>
        :type CopyPairSet: list of CopyPair
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CopyPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的复制对总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CopyPairSet(self):
        r"""<p>复制对列表。</p>
        :rtype: list of CopyPair
        """
        return self._CopyPairSet

    @CopyPairSet.setter
    def CopyPairSet(self, CopyPairSet):
        self._CopyPairSet = CopyPairSet

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
        if params.get("CopyPairSet") is not None:
            self._CopyPairSet = []
            for item in params.get("CopyPairSet"):
                obj = CopyPair()
                obj._deserialize(item)
                self._CopyPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoveryDrillGroupsRequest(AbstractModel):
    r"""DescribeDisasterRecoveryDrillGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillGroupType: 要查询的容灾演练组产品类型。枚举值：DISK / INSTANCE / CFS。
        :type DrillGroupType: str
        :param _DrillGroupIds: 要查询的容灾演练组ID列表。
        :type DrillGroupIds: list of str
        :param _Filters: 过滤条件，详见定期快照过滤条件表。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Order: 输出结果按升序还是降序。枚举值：ASC / DESC。
        :type Order: str
        :param _OrderField: 输出结果的排序字段。枚举值：CREATE_TIME。
        :type OrderField: str
        """
        self._DrillGroupType = None
        self._DrillGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def DrillGroupType(self):
        r"""要查询的容灾演练组产品类型。枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._DrillGroupType

    @DrillGroupType.setter
    def DrillGroupType(self, DrillGroupType):
        self._DrillGroupType = DrillGroupType

    @property
    def DrillGroupIds(self):
        r"""要查询的容灾演练组ID列表。
        :rtype: list of str
        """
        return self._DrillGroupIds

    @DrillGroupIds.setter
    def DrillGroupIds(self, DrillGroupIds):
        self._DrillGroupIds = DrillGroupIds

    @property
    def Filters(self):
        r"""过滤条件，详见定期快照过滤条件表。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""输出结果按升序还是降序。枚举值：ASC / DESC。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""输出结果的排序字段。枚举值：CREATE_TIME。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._DrillGroupType = params.get("DrillGroupType")
        self._DrillGroupIds = params.get("DrillGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoveryDrillGroupsResponse(AbstractModel):
    r"""DescribeDisasterRecoveryDrillGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 有效的容灾演练组数量。
        :type TotalCount: int
        :param _DrillGroupSet: 容灾演练组列表。
        :type DrillGroupSet: list of DisasterRecoveryDrillGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DrillGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""有效的容灾演练组数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DrillGroupSet(self):
        r"""容灾演练组列表。
        :rtype: list of DisasterRecoveryDrillGroup
        """
        return self._DrillGroupSet

    @DrillGroupSet.setter
    def DrillGroupSet(self, DrillGroupSet):
        self._DrillGroupSet = DrillGroupSet

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
        if params.get("DrillGroupSet") is not None:
            self._DrillGroupSet = []
            for item in params.get("DrillGroupSet"):
                obj = DisasterRecoveryDrillGroup()
                obj._deserialize(item)
                self._DrillGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoveryOverviewRequest(AbstractModel):
    r"""DescribeDisasterRecoveryOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairType: 要查询的产品/复制对的类型，枚举值：• DISK：云硬盘类型复制对• INSTANCE：CVM 实例复制对• CFS：文件存储复制对• ALL：聚合当前支持的类型；默认为CFS
        :type CopyPairType: str
        """
        self._CopyPairType = None

    @property
    def CopyPairType(self):
        r"""要查询的产品/复制对的类型，枚举值：• DISK：云硬盘类型复制对• INSTANCE：CVM 实例复制对• CFS：文件存储复制对• ALL：聚合当前支持的类型；默认为CFS
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType


    def _deserialize(self, params):
        self._CopyPairType = params.get("CopyPairType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoveryOverviewResponse(AbstractModel):
    r"""DescribeDisasterRecoveryOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoveryOverview: 跨所有地域聚合后的容灾总览数据
        :type DisasterRecoveryOverview: :class:`tencentcloud.bdrc.v20260330.models.DisasterRecoveryOverview`
        :param _OverviewInRegionSet: 按地域拆分的容灾总览列表
        :type OverviewInRegionSet: list of DisasterRecoveryOverview
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DisasterRecoveryOverview = None
        self._OverviewInRegionSet = None
        self._RequestId = None

    @property
    def DisasterRecoveryOverview(self):
        r"""跨所有地域聚合后的容灾总览数据
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DisasterRecoveryOverview`
        """
        return self._DisasterRecoveryOverview

    @DisasterRecoveryOverview.setter
    def DisasterRecoveryOverview(self, DisasterRecoveryOverview):
        self._DisasterRecoveryOverview = DisasterRecoveryOverview

    @property
    def OverviewInRegionSet(self):
        r"""按地域拆分的容灾总览列表
        :rtype: list of DisasterRecoveryOverview
        """
        return self._OverviewInRegionSet

    @OverviewInRegionSet.setter
    def OverviewInRegionSet(self, OverviewInRegionSet):
        self._OverviewInRegionSet = OverviewInRegionSet

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
        if params.get("DisasterRecoveryOverview") is not None:
            self._DisasterRecoveryOverview = DisasterRecoveryOverview()
            self._DisasterRecoveryOverview._deserialize(params.get("DisasterRecoveryOverview"))
        if params.get("OverviewInRegionSet") is not None:
            self._OverviewInRegionSet = []
            for item in params.get("OverviewInRegionSet"):
                obj = DisasterRecoveryOverview()
                obj._deserialize(item)
                self._OverviewInRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoveryProtectGroupsRequest(AbstractModel):
    r"""DescribeDisasterRecoveryProtectGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupType: 要查询的容灾保护组产品类型，枚举值：DISK / INSTANCE / CFS。
        :type ProtectGroupType: str
        :param _ProtectGroupIds: 要查询的容灾保护组ID列表。
        :type ProtectGroupIds: list of str
        :param _Filters: 过滤条件（过滤项由 core handler 定义，如 disaster-recovery-protect-group-id 等）。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Order: 输出结果按升序还是降序
        :type Order: str
        :param _OrderField: 输出结果的排序字段
        :type OrderField: str
        """
        self._ProtectGroupType = None
        self._ProtectGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def ProtectGroupType(self):
        r"""要查询的容灾保护组产品类型，枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._ProtectGroupType

    @ProtectGroupType.setter
    def ProtectGroupType(self, ProtectGroupType):
        self._ProtectGroupType = ProtectGroupType

    @property
    def ProtectGroupIds(self):
        r"""要查询的容灾保护组ID列表。
        :rtype: list of str
        """
        return self._ProtectGroupIds

    @ProtectGroupIds.setter
    def ProtectGroupIds(self, ProtectGroupIds):
        self._ProtectGroupIds = ProtectGroupIds

    @property
    def Filters(self):
        r"""过滤条件（过滤项由 core handler 定义，如 disaster-recovery-protect-group-id 等）。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""输出结果按升序还是降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""输出结果的排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._ProtectGroupType = params.get("ProtectGroupType")
        self._ProtectGroupIds = params.get("ProtectGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoveryProtectGroupsResponse(AbstractModel):
    r"""DescribeDisasterRecoveryProtectGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的容灾保护组总数
        :type TotalCount: int
        :param _ProtectGroupSet: 容灾保护组列表
        :type ProtectGroupSet: list of ProtectGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProtectGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的容灾保护组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProtectGroupSet(self):
        r"""容灾保护组列表
        :rtype: list of ProtectGroup
        """
        return self._ProtectGroupSet

    @ProtectGroupSet.setter
    def ProtectGroupSet(self, ProtectGroupSet):
        self._ProtectGroupSet = ProtectGroupSet

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
        if params.get("ProtectGroupSet") is not None:
            self._ProtectGroupSet = []
            for item in params.get("ProtectGroupSet"):
                obj = ProtectGroup()
                obj._deserialize(item)
                self._ProtectGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverySitePairsDeniedActionsRequest(AbstractModel):
    r"""DescribeDisasterRecoverySitePairsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairIds: 要查询的容灾策略ID列表，单个ID格式为 sitepair-xxxxxxxx
        :type SitePairIds: list of str
        """
        self._SitePairIds = None

    @property
    def SitePairIds(self):
        r"""要查询的容灾策略ID列表，单个ID格式为 sitepair-xxxxxxxx
        :rtype: list of str
        """
        return self._SitePairIds

    @SitePairIds.setter
    def SitePairIds(self, SitePairIds):
        self._SitePairIds = SitePairIds


    def _deserialize(self, params):
        self._SitePairIds = params.get("SitePairIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverySitePairsDeniedActionsResponse(AbstractModel):
    r"""DescribeDisasterRecoverySitePairsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairDeniedActionSet: 每个容灾策略对应的禁止操作集合，返回顺序与入参 SitePairIds 一致
        :type SitePairDeniedActionSet: list of SitePairDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SitePairDeniedActionSet = None
        self._RequestId = None

    @property
    def SitePairDeniedActionSet(self):
        r"""每个容灾策略对应的禁止操作集合，返回顺序与入参 SitePairIds 一致
        :rtype: list of SitePairDeniedAction
        """
        return self._SitePairDeniedActionSet

    @SitePairDeniedActionSet.setter
    def SitePairDeniedActionSet(self, SitePairDeniedActionSet):
        self._SitePairDeniedActionSet = SitePairDeniedActionSet

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
        if params.get("SitePairDeniedActionSet") is not None:
            self._SitePairDeniedActionSet = []
            for item in params.get("SitePairDeniedActionSet"):
                obj = SitePairDeniedAction()
                obj._deserialize(item)
                self._SitePairDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverySitePairsRequest(AbstractModel):
    r"""DescribeDisasterRecoverySitePairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairType: 要查询的容灾策略产品类型。取值范围：DISK / INSTANCE / CFS。
        :type SitePairType: str
        :param _SitePairIds: 要查询的容灾策略ID列表。
        :type SitePairIds: list of str
        :param _Filters: 过滤条件，详见定期快照过滤条件表。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Order: 输出结果按升序还是降序，DESC表示降序，ASC表示升序
        :type Order: str
        :param _OrderField: 输出结果的排序字段
        :type OrderField: str
        """
        self._SitePairType = None
        self._SitePairIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def SitePairType(self):
        r"""要查询的容灾策略产品类型。取值范围：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._SitePairType

    @SitePairType.setter
    def SitePairType(self, SitePairType):
        self._SitePairType = SitePairType

    @property
    def SitePairIds(self):
        r"""要查询的容灾策略ID列表。
        :rtype: list of str
        """
        return self._SitePairIds

    @SitePairIds.setter
    def SitePairIds(self, SitePairIds):
        self._SitePairIds = SitePairIds

    @property
    def Filters(self):
        r"""过滤条件，详见定期快照过滤条件表。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""输出结果按升序还是降序，DESC表示降序，ASC表示升序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""输出结果的排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._SitePairType = params.get("SitePairType")
        self._SitePairIds = params.get("SitePairIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverySitePairsResponse(AbstractModel):
    r"""DescribeDisasterRecoverySitePairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 有效的容灾策略数量。
        :type TotalCount: int
        :param _SitePairSet: 容灾策略列表。
        :type SitePairSet: list of SitePair
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SitePairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""有效的容灾策略数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SitePairSet(self):
        r"""容灾策略列表。
        :rtype: list of SitePair
        """
        return self._SitePairSet

    @SitePairSet.setter
    def SitePairSet(self, SitePairSet):
        self._SitePairSet = SitePairSet

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
        if params.get("SitePairSet") is not None:
            self._SitePairSet = []
            for item in params.get("SitePairSet"):
                obj = SitePair()
                obj._deserialize(item)
                self._SitePairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverySupportRegionRequest(AbstractModel):
    r"""DescribeDisasterRecoverySupportRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>状态过滤：valid（生效）/ invalid（停用）；为空则同时返回生效与停用的全部记录。</p>
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        r"""<p>状态过滤：valid（生效）/ invalid（停用）；为空则同时返回生效与停用的全部记录。</p>
        :rtype: str
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
        


class DescribeDisasterRecoverySupportRegionResponse(AbstractModel):
    r"""DescribeDisasterRecoverySupportRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的支持的生产地域配置总数。</p>
        :type TotalCount: int
        :param _SupportRegionSet: <p>支持的生产地域配置详情列表。</p>
        :type SupportRegionSet: list of SupportRegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SupportRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的支持的生产地域配置总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SupportRegionSet(self):
        r"""<p>支持的生产地域配置详情列表。</p>
        :rtype: list of SupportRegionInfo
        """
        return self._SupportRegionSet

    @SupportRegionSet.setter
    def SupportRegionSet(self, SupportRegionSet):
        self._SupportRegionSet = SupportRegionSet

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
        if params.get("SupportRegionSet") is not None:
            self._SupportRegionSet = []
            for item in params.get("SupportRegionSet"):
                obj = SupportRegionInfo()
                obj._deserialize(item)
                self._SupportRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    r"""DescribeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 要查询信息的云盘ID列表
        :type DiskIds: list of str
        :param _DiskRegion: 云盘所在地域
        :type DiskRegion: str
        """
        self._DiskIds = None
        self._DiskRegion = None

    @property
    def DiskIds(self):
        r"""要查询信息的云盘ID列表
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskRegion(self):
        r"""云盘所在地域
        :rtype: str
        """
        return self._DiskRegion

    @DiskRegion.setter
    def DiskRegion(self, DiskRegion):
        self._DiskRegion = DiskRegion


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskRegion = params.get("DiskRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    r"""DescribeDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的云盘总数
        :type TotalCount: int
        :param _DiskInfoSet: 云盘详情列表
        :type DiskInfoSet: list of DiskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的云盘总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskInfoSet(self):
        r"""云盘详情列表
        :rtype: list of DiskInfo
        """
        return self._DiskInfoSet

    @DiskInfoSet.setter
    def DiskInfoSet(self, DiskInfoSet):
        self._DiskInfoSet = DiskInfoSet

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
        if params.get("DiskInfoSet") is not None:
            self._DiskInfoSet = []
            for item in params.get("DiskInfoSet"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DiskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDrillPairsDeniedActionsRequest(AbstractModel):
    r"""DescribeDrillPairsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairType: 要查询演练对的类型，枚举值：DISK（云硬盘）、INSTANCE（云服务器）、CFS（文件存储）
        :type DrillPairType: str
        :param _DrillPairIds: 演练对ID列表
        :type DrillPairIds: list of str
        """
        self._DrillPairType = None
        self._DrillPairIds = None

    @property
    def DrillPairType(self):
        r"""要查询演练对的类型，枚举值：DISK（云硬盘）、INSTANCE（云服务器）、CFS（文件存储）
        :rtype: str
        """
        return self._DrillPairType

    @DrillPairType.setter
    def DrillPairType(self, DrillPairType):
        self._DrillPairType = DrillPairType

    @property
    def DrillPairIds(self):
        r"""演练对ID列表
        :rtype: list of str
        """
        return self._DrillPairIds

    @DrillPairIds.setter
    def DrillPairIds(self, DrillPairIds):
        self._DrillPairIds = DrillPairIds


    def _deserialize(self, params):
        self._DrillPairType = params.get("DrillPairType")
        self._DrillPairIds = params.get("DrillPairIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDrillPairsDeniedActionsResponse(AbstractModel):
    r"""DescribeDrillPairsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairDeniedActionSet: 演练对操作掩码列表，返回每个演练对被禁止执行的操作
        :type DrillPairDeniedActionSet: list of DrillPairDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DrillPairDeniedActionSet = None
        self._RequestId = None

    @property
    def DrillPairDeniedActionSet(self):
        r"""演练对操作掩码列表，返回每个演练对被禁止执行的操作
        :rtype: list of DrillPairDeniedAction
        """
        return self._DrillPairDeniedActionSet

    @DrillPairDeniedActionSet.setter
    def DrillPairDeniedActionSet(self, DrillPairDeniedActionSet):
        self._DrillPairDeniedActionSet = DrillPairDeniedActionSet

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
        if params.get("DrillPairDeniedActionSet") is not None:
            self._DrillPairDeniedActionSet = []
            for item in params.get("DrillPairDeniedActionSet"):
                obj = DrillPairDeniedAction()
                obj._deserialize(item)
                self._DrillPairDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDrillPairsRequest(AbstractModel):
    r"""DescribeDrillPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairType: 要查询演练对的类型。枚举值：DISK / INSTANCE / CFS。
        :type DrillPairType: str
        :param _DrillPairIds: 要查询演练对ID列表。
        :type DrillPairIds: list of str
        :param _Filters: 过滤条件，详见定期快照过滤条件表。
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Order: 输出结果按升序还是降序。枚举值：ASC / DESC。
        :type Order: str
        :param _OrderField: 输出结果的排序字段。枚举值：CREATE_TIME / END_TIME。
        :type OrderField: str
        """
        self._DrillPairType = None
        self._DrillPairIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def DrillPairType(self):
        r"""要查询演练对的类型。枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._DrillPairType

    @DrillPairType.setter
    def DrillPairType(self, DrillPairType):
        self._DrillPairType = DrillPairType

    @property
    def DrillPairIds(self):
        r"""要查询演练对ID列表。
        :rtype: list of str
        """
        return self._DrillPairIds

    @DrillPairIds.setter
    def DrillPairIds(self, DrillPairIds):
        self._DrillPairIds = DrillPairIds

    @property
    def Filters(self):
        r"""过滤条件，详见定期快照过滤条件表。
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""输出结果按升序还是降序。枚举值：ASC / DESC。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""输出结果的排序字段。枚举值：CREATE_TIME / END_TIME。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._DrillPairType = params.get("DrillPairType")
        self._DrillPairIds = params.get("DrillPairIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDrillPairsResponse(AbstractModel):
    r"""DescribeDrillPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 有效的容灾演练对数量。
        :type TotalCount: int
        :param _DrillPairSet: 容灾演练对列表。
        :type DrillPairSet: list of DrillPair
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DrillPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""有效的容灾演练对数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DrillPairSet(self):
        r"""容灾演练对列表。
        :rtype: list of DrillPair
        """
        return self._DrillPairSet

    @DrillPairSet.setter
    def DrillPairSet(self, DrillPairSet):
        self._DrillPairSet = DrillPairSet

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
        if params.get("DrillPairSet") is not None:
            self._DrillPairSet = []
            for item in params.get("DrillPairSet"):
                obj = DrillPair()
                obj._deserialize(item)
                self._DrillPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileBackupObjectsRequest(AbstractModel):
    r"""DescribeFileBackupObjects请求参数结构体

    """


class DescribeFileBackupObjectsResponse(AbstractModel):
    r"""DescribeFileBackupObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 当前路径下包含的目录及文件总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""当前路径下包含的目录及文件总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._RequestId = params.get("RequestId")


class DescribeFileBackupPlansRequest(AbstractModel):
    r"""DescribeFileBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _Order: 排序方式
        :type Order: str
        :param _Filters: 过滤条件。支持: instance-id, plan-id, plan-name, status, auto-backup-policy-id
        :type Filters: list of FilterModel
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        r"""过滤条件。支持: instance-id, plan-id, plan-name, status, auto-backup-policy-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileBackupPlansResponse(AbstractModel):
    r"""DescribeFileBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的计划总数量
        :type TotalCount: int
        :param _PlanSet: 符合条件的计划详情
        :type PlanSet: list of PlanInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PlanSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的计划总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PlanSet(self):
        r"""符合条件的计划详情
        :rtype: list of PlanInfo
        """
        return self._PlanSet

    @PlanSet.setter
    def PlanSet(self, PlanSet):
        self._PlanSet = PlanSet

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
        if params.get("PlanSet") is not None:
            self._PlanSet = []
            for item in params.get("PlanSet"):
                obj = PlanInfo()
                obj._deserialize(item)
                self._PlanSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileBackupsDeniedActionsRequest(AbstractModel):
    r"""DescribeFileBackupsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupIds: 要查询的文件备份ID列表
        :type BackupIds: list of str
        """
        self._BackupIds = None

    @property
    def BackupIds(self):
        r"""要查询的文件备份ID列表
        :rtype: list of str
        """
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds


    def _deserialize(self, params):
        self._BackupIds = params.get("BackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileBackupsDeniedActionsResponse(AbstractModel):
    r"""DescribeFileBackupsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupDeniedActionSet: 备份的操作掩码。
        :type BackupDeniedActionSet: list of BackupDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupDeniedActionSet = None
        self._RequestId = None

    @property
    def BackupDeniedActionSet(self):
        r"""备份的操作掩码。
        :rtype: list of BackupDeniedAction
        """
        return self._BackupDeniedActionSet

    @BackupDeniedActionSet.setter
    def BackupDeniedActionSet(self, BackupDeniedActionSet):
        self._BackupDeniedActionSet = BackupDeniedActionSet

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
        if params.get("BackupDeniedActionSet") is not None:
            self._BackupDeniedActionSet = []
            for item in params.get("BackupDeniedActionSet"):
                obj = BackupDeniedAction()
                obj._deserialize(item)
                self._BackupDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileBackupsRequest(AbstractModel):
    r"""DescribeFileBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _Order: 排序方式
        :type Order: str
        :param _Filters: 过滤条件。支持: backup-id, plan-id, instance-id, status, backup-type, auto-backup-policy-id
        :type Filters: list of FilterModel
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        r"""过滤条件。支持: backup-id, plan-id, instance-id, status, backup-type, auto-backup-policy-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileBackupsResponse(AbstractModel):
    r"""DescribeFileBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的备份点总数量
        :type TotalCount: int
        :param _BackupSet: 符合条件的备份点详情
        :type BackupSet: list of BackupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的备份点总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupSet(self):
        r"""符合条件的备份点详情
        :rtype: list of BackupInfo
        """
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

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
        if params.get("BackupSet") is not None:
            self._BackupSet = []
            for item in params.get("BackupSet"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileRestoreTasksRequest(AbstractModel):
    r"""DescribeFileRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。支持: backup-id, task-id, instance-id, "         "target-instance-id, status
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        r"""过滤条件。支持: backup-id, task-id, instance-id, "         "target-instance-id, status
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileRestoreTasksResponse(AbstractModel):
    r"""DescribeFileRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数量。
        :type TotalCount: int
        :param _RestoreTaskSet: 恢复任务列表详情。
        :type RestoreTaskSet: list of RestoreTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RestoreTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RestoreTaskSet(self):
        r"""恢复任务列表详情。
        :rtype: list of RestoreTask
        """
        return self._RestoreTaskSet

    @RestoreTaskSet.setter
    def RestoreTaskSet(self, RestoreTaskSet):
        self._RestoreTaskSet = RestoreTaskSet

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
        if params.get("RestoreTaskSet") is not None:
            self._RestoreTaskSet = []
            for item in params.get("RestoreTaskSet"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._RestoreTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    r"""DescribeJobs请求参数结构体

    """


class DescribeJobsResponse(AbstractModel):
    r"""DescribeJobs返回参数结构体

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


class DescribePriceCreateCopyPairsRequest(AbstractModel):
    r"""DescribePriceCreateCopyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataCapacities: 每个复制对的容量列表，长度 1~10。数组长度即为询价的复制对个数，每个元素对应一个复制对的容量
        :type DataCapacities: list of int
        """
        self._DataCapacities = None

    @property
    def DataCapacities(self):
        r"""每个复制对的容量列表，长度 1~10。数组长度即为询价的复制对个数，每个元素对应一个复制对的容量
        :rtype: list of int
        """
        return self._DataCapacities

    @DataCapacities.setter
    def DataCapacities(self, DataCapacities):
        self._DataCapacities = DataCapacities


    def _deserialize(self, params):
        self._DataCapacities = params.get("DataCapacities")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceCreateCopyPairsResponse(AbstractModel):
    r"""DescribePriceCreateCopyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairPrices: 复制对价格列表，与入参一一对应
        :type CopyPairPrices: list of CopyPairPrice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CopyPairPrices = None
        self._RequestId = None

    @property
    def CopyPairPrices(self):
        r"""复制对价格列表，与入参一一对应
        :rtype: list of CopyPairPrice
        """
        return self._CopyPairPrices

    @CopyPairPrices.setter
    def CopyPairPrices(self, CopyPairPrices):
        self._CopyPairPrices = CopyPairPrices

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
        if params.get("CopyPairPrices") is not None:
            self._CopyPairPrices = []
            for item in params.get("CopyPairPrices"):
                obj = CopyPairPrice()
                obj._deserialize(item)
                self._CopyPairPrices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProtectGroupsDeniedActionsRequest(AbstractModel):
    r"""DescribeProtectGroupsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupIds: 保护组ID列表
        :type ProtectGroupIds: list of str
        """
        self._ProtectGroupIds = None

    @property
    def ProtectGroupIds(self):
        r"""保护组ID列表
        :rtype: list of str
        """
        return self._ProtectGroupIds

    @ProtectGroupIds.setter
    def ProtectGroupIds(self, ProtectGroupIds):
        self._ProtectGroupIds = ProtectGroupIds


    def _deserialize(self, params):
        self._ProtectGroupIds = params.get("ProtectGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectGroupsDeniedActionsResponse(AbstractModel):
    r"""DescribeProtectGroupsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupDeniedActionSet: 保护组操作掩码列表，返回每个保护组被禁止执行的操作
        :type ProtectGroupDeniedActionSet: list of ProtectGroupDeniedAction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectGroupDeniedActionSet = None
        self._RequestId = None

    @property
    def ProtectGroupDeniedActionSet(self):
        r"""保护组操作掩码列表，返回每个保护组被禁止执行的操作
        :rtype: list of ProtectGroupDeniedAction
        """
        return self._ProtectGroupDeniedActionSet

    @ProtectGroupDeniedActionSet.setter
    def ProtectGroupDeniedActionSet(self, ProtectGroupDeniedActionSet):
        self._ProtectGroupDeniedActionSet = ProtectGroupDeniedActionSet

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
        if params.get("ProtectGroupDeniedActionSet") is not None:
            self._ProtectGroupDeniedActionSet = []
            for item in params.get("ProtectGroupDeniedActionSet"):
                obj = ProtectGroupDeniedAction()
                obj._deserialize(item)
                self._ProtectGroupDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProtectedInstancesRequest(AbstractModel):
    r"""DescribeProtectedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大500
        :type Limit: int
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _Order: 排序方式
        :type Order: str
        :param _Filters: 过滤条件。支持: instance-id, agent-status
        :type Filters: list of FilterModel
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        r"""过滤条件。支持: instance-id, agent-status
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectedInstancesResponse(AbstractModel):
    r"""DescribeProtectedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的受保护实例总数量
        :type TotalCount: int
        :param _InstanceSet: 符合条件的受保护实例详情
        :type InstanceSet: list of ProtectInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的受保护实例总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        r"""符合条件的受保护实例详情
        :rtype: list of ProtectInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ProtectInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupMappingsRequest(AbstractModel):
    r"""DescribeSecurityGroupMappings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 安全组映射所属的站点对ID。
        :type SitePairId: str
        :param _Filters: 过滤条件，详见过滤条件表。支持的Name：src-security-group-id、target-security-group-id
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为500。关于Limit的更进一步介绍请参考 API 简介中的相关小节
        :type Limit: int
        :param _Order: 输出结果按升序还是降序，可选值：ASC、DESC
        :type Order: str
        :param _OrderField: 输出结果的排序字段，可选值：CREATE_TIME
        :type OrderField: str
        """
        self._SitePairId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def SitePairId(self):
        r"""安全组映射所属的站点对ID。
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def Filters(self):
        r"""过滤条件，详见过滤条件表。支持的Name：src-security-group-id、target-security-group-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为500。关于Limit的更进一步介绍请参考 API 简介中的相关小节
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""输出结果按升序还是降序，可选值：ASC、DESC
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""输出结果的排序字段，可选值：CREATE_TIME
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupMappingsResponse(AbstractModel):
    r"""DescribeSecurityGroupMappings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _SecurityGroupMappingSet: 安全组映射详情。
        :type SecurityGroupMappingSet: list of SecurityGroupMapping
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecurityGroupMappingSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityGroupMappingSet(self):
        r"""安全组映射详情。
        :rtype: list of SecurityGroupMapping
        """
        return self._SecurityGroupMappingSet

    @SecurityGroupMappingSet.setter
    def SecurityGroupMappingSet(self, SecurityGroupMappingSet):
        self._SecurityGroupMappingSet = SecurityGroupMappingSet

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
        if params.get("SecurityGroupMappingSet") is not None:
            self._SecurityGroupMappingSet = []
            for item in params.get("SecurityGroupMappingSet"):
                obj = SecurityGroupMapping()
                obj._deserialize(item)
                self._SecurityGroupMappingSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcMappingsRequest(AbstractModel):
    r"""DescribeVpcMappings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 要查询的站点对id
        :type SitePairId: str
        :param _Filters: 过滤条件。支持: source-vpc-id, target-vpc-id, source-subnet-id, target-subnet-id
        :type Filters: list of FilterModel
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        """
        self._SitePairId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SitePairId(self):
        r"""要查询的站点对id
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def Filters(self):
        r"""过滤条件。支持: source-vpc-id, target-vpc-id, source-subnet-id, target-subnet-id
        :rtype: list of FilterModel
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterModel()
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
        


class DescribeVpcMappingsResponse(AbstractModel):
    r"""DescribeVpcMappings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的VPC映射规则总数
        :type TotalCount: int
        :param _VpcMappingSet: VPC映射规则列表
        :type VpcMappingSet: list of VpcMapping
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcMappingSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的VPC映射规则总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcMappingSet(self):
        r"""VPC映射规则列表
        :rtype: list of VpcMapping
        """
        return self._VpcMappingSet

    @VpcMappingSet.setter
    def VpcMappingSet(self, VpcMappingSet):
        self._VpcMappingSet = VpcMappingSet

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
        if params.get("VpcMappingSet") is not None:
            self._VpcMappingSet = []
            for item in params.get("VpcMappingSet"):
                obj = VpcMapping()
                obj._deserialize(item)
                self._VpcMappingSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisasterRecoveryDrillGroup(AbstractModel):
    r"""容灾演练组

    """

    def __init__(self):
        r"""
        :param _Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _AppId: 用户ID
        :type AppId: int
        :param _AccountUin: 账户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 子账户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _SitePairId: 容灾站点对ID
        :type SitePairId: str
        :param _ProtectGroupId: 保护组ID
        :type ProtectGroupId: str
        :param _DrillGroupId: 演练组ID
        :type DrillGroupId: str
        :param _DrillGroupName: 演练组名称
        :type DrillGroupName: str
        :param _DrillGroupType: 演练组类型。枚举值：DISK / INSTANCE / CFS。
        :type DrillGroupType: str
        :param _RecoveryTime: 恢复时间点
注意：此字段可能返回 null，表示取不到有效值。
        :type RecoveryTime: str
        :param _DrillVpc: 演练VPC
        :type DrillVpc: str
        :param _DrillSecurityGroup: 演练安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type DrillSecurityGroup: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _LifeState: 生命周期状态。枚举值：NORMAL / DELETED。
        :type LifeState: str
        :param _DisasterRecoveryType: 容灾类型。枚举值：CROSS_ZONE / CROSS_REGION 等。
        :type DisasterRecoveryType: str
        :param _CopyType: 复制技术。枚举值：SYN（同步）/ ASYN（异步）。
        :type CopyType: str
        :param _PeerCloudName: 对端云名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerCloudName: str
        :param _LocalCloudName: 本地云名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalCloudName: str
        :param _SourceRegion: 生产地域
        :type SourceRegion: str
        :param _SourceZone: 生产可用区
        :type SourceZone: str
        :param _SourceVpc: 生产端VPC
        :type SourceVpc: str
        :param _DrillRegion: 演练地域
        :type DrillRegion: str
        :param _DrillZone: 演练可用区
        :type DrillZone: str
        :param _DataDirection: 数据方向。枚举值：POSITIVE（正向）/ REVERSE（反向）。
        :type DataDirection: str
        :param _BindDrilledResourceCount: 绑定的演练资源数量。
        :type BindDrilledResourceCount: int
        :param _DrilledResourceStatusSet: 演练资源状态分布（key 为状态名如 FAILED / SUCCESS，value 为该状态数量）。
        :type DrilledResourceStatusSet: list of DrilledResourceStatus
        """
        self._Id = None
        self._AppId = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._SitePairId = None
        self._ProtectGroupId = None
        self._DrillGroupId = None
        self._DrillGroupName = None
        self._DrillGroupType = None
        self._RecoveryTime = None
        self._DrillVpc = None
        self._DrillSecurityGroup = None
        self._CreateTime = None
        self._ModifyTime = None
        self._LifeState = None
        self._DisasterRecoveryType = None
        self._CopyType = None
        self._PeerCloudName = None
        self._LocalCloudName = None
        self._SourceRegion = None
        self._SourceZone = None
        self._SourceVpc = None
        self._DrillRegion = None
        self._DrillZone = None
        self._DataDirection = None
        self._BindDrilledResourceCount = None
        self._DrilledResourceStatusSet = None

    @property
    def Id(self):
        r"""资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AccountUin(self):
        r"""账户uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""子账户uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def SitePairId(self):
        r"""容灾站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def ProtectGroupId(self):
        r"""保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def DrillGroupId(self):
        r"""演练组ID
        :rtype: str
        """
        return self._DrillGroupId

    @DrillGroupId.setter
    def DrillGroupId(self, DrillGroupId):
        self._DrillGroupId = DrillGroupId

    @property
    def DrillGroupName(self):
        r"""演练组名称
        :rtype: str
        """
        return self._DrillGroupName

    @DrillGroupName.setter
    def DrillGroupName(self, DrillGroupName):
        self._DrillGroupName = DrillGroupName

    @property
    def DrillGroupType(self):
        r"""演练组类型。枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._DrillGroupType

    @DrillGroupType.setter
    def DrillGroupType(self, DrillGroupType):
        self._DrillGroupType = DrillGroupType

    @property
    def RecoveryTime(self):
        r"""恢复时间点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecoveryTime

    @RecoveryTime.setter
    def RecoveryTime(self, RecoveryTime):
        self._RecoveryTime = RecoveryTime

    @property
    def DrillVpc(self):
        r"""演练VPC
        :rtype: str
        """
        return self._DrillVpc

    @DrillVpc.setter
    def DrillVpc(self, DrillVpc):
        self._DrillVpc = DrillVpc

    @property
    def DrillSecurityGroup(self):
        r"""演练安全组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DrillSecurityGroup

    @DrillSecurityGroup.setter
    def DrillSecurityGroup(self, DrillSecurityGroup):
        self._DrillSecurityGroup = DrillSecurityGroup

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
    def ModifyTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def LifeState(self):
        r"""生命周期状态。枚举值：NORMAL / DELETED。
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def DisasterRecoveryType(self):
        r"""容灾类型。枚举值：CROSS_ZONE / CROSS_REGION 等。
        :rtype: str
        """
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def CopyType(self):
        r"""复制技术。枚举值：SYN（同步）/ ASYN（异步）。
        :rtype: str
        """
        return self._CopyType

    @CopyType.setter
    def CopyType(self, CopyType):
        self._CopyType = CopyType

    @property
    def PeerCloudName(self):
        r"""对端云名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerCloudName

    @PeerCloudName.setter
    def PeerCloudName(self, PeerCloudName):
        self._PeerCloudName = PeerCloudName

    @property
    def LocalCloudName(self):
        r"""本地云名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LocalCloudName

    @LocalCloudName.setter
    def LocalCloudName(self, LocalCloudName):
        self._LocalCloudName = LocalCloudName

    @property
    def SourceRegion(self):
        r"""生产地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""生产可用区
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def SourceVpc(self):
        r"""生产端VPC
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def DrillRegion(self):
        r"""演练地域
        :rtype: str
        """
        return self._DrillRegion

    @DrillRegion.setter
    def DrillRegion(self, DrillRegion):
        self._DrillRegion = DrillRegion

    @property
    def DrillZone(self):
        r"""演练可用区
        :rtype: str
        """
        return self._DrillZone

    @DrillZone.setter
    def DrillZone(self, DrillZone):
        self._DrillZone = DrillZone

    @property
    def DataDirection(self):
        r"""数据方向。枚举值：POSITIVE（正向）/ REVERSE（反向）。
        :rtype: str
        """
        return self._DataDirection

    @DataDirection.setter
    def DataDirection(self, DataDirection):
        self._DataDirection = DataDirection

    @property
    def BindDrilledResourceCount(self):
        r"""绑定的演练资源数量。
        :rtype: int
        """
        return self._BindDrilledResourceCount

    @BindDrilledResourceCount.setter
    def BindDrilledResourceCount(self, BindDrilledResourceCount):
        self._BindDrilledResourceCount = BindDrilledResourceCount

    @property
    def DrilledResourceStatusSet(self):
        r"""演练资源状态分布（key 为状态名如 FAILED / SUCCESS，value 为该状态数量）。
        :rtype: list of DrilledResourceStatus
        """
        return self._DrilledResourceStatusSet

    @DrilledResourceStatusSet.setter
    def DrilledResourceStatusSet(self, DrilledResourceStatusSet):
        self._DrilledResourceStatusSet = DrilledResourceStatusSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._SitePairId = params.get("SitePairId")
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._DrillGroupId = params.get("DrillGroupId")
        self._DrillGroupName = params.get("DrillGroupName")
        self._DrillGroupType = params.get("DrillGroupType")
        self._RecoveryTime = params.get("RecoveryTime")
        self._DrillVpc = params.get("DrillVpc")
        self._DrillSecurityGroup = params.get("DrillSecurityGroup")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._LifeState = params.get("LifeState")
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._CopyType = params.get("CopyType")
        self._PeerCloudName = params.get("PeerCloudName")
        self._LocalCloudName = params.get("LocalCloudName")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._SourceVpc = params.get("SourceVpc")
        self._DrillRegion = params.get("DrillRegion")
        self._DrillZone = params.get("DrillZone")
        self._DataDirection = params.get("DataDirection")
        self._BindDrilledResourceCount = params.get("BindDrilledResourceCount")
        if params.get("DrilledResourceStatusSet") is not None:
            self._DrilledResourceStatusSet = []
            for item in params.get("DrilledResourceStatusSet"):
                obj = DrilledResourceStatus()
                obj._deserialize(item)
                self._DrilledResourceStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisasterRecoveryOverview(AbstractModel):
    r"""容灾总览数据

    """

    def __init__(self):
        r"""
        :param _Region: 地域 ID
        :type Region: str
        :param _SitePairCount: 站点对总数
        :type SitePairCount: int
        :param _SitePairCrossRegionCount: 跨地域站点对数
        :type SitePairCrossRegionCount: int
        :param _SitePairCrossZoneCount: 跨可用区站点对数
        :type SitePairCrossZoneCount: int
        :param _SitePairCrossCloudCount: 跨云站点对数
        :type SitePairCrossCloudCount: int
        :param _ProtectGroupCount: 保护组总数
        :type ProtectGroupCount: int
        :param _ProtectGroupCrossRegionCount: 跨地域保护组数
        :type ProtectGroupCrossRegionCount: int
        :param _ProtectGroupCrossZoneCount: 跨可用区保护组数
        :type ProtectGroupCrossZoneCount: int
        :param _ProtectGroupCrossCloudCount: 跨云保护组数
        :type ProtectGroupCrossCloudCount: int
        :param _CopyPairCount: 复制对总数
        :type CopyPairCount: int
        :param _CopyPairSuccessRPOCount: RPO 正常的复制对数
        :type CopyPairSuccessRPOCount: int
        :param _CopyPairErrorRPOCount: RPO 异常的复制对数
        :type CopyPairErrorRPOCount: int
        :param _DrillPairCount: 演练对总数
        :type DrillPairCount: int
        :param _DrillPairDrillingCount: 演练中
        :type DrillPairDrillingCount: int
        :param _DrillPairFailedCount: 演练失败
        :type DrillPairFailedCount: int
        :param _DrillPairSuccessCount: 演练成功
        :type DrillPairSuccessCount: int
        :param _ProtectedResourceCount: 受保护资源总数
        :type ProtectedResourceCount: int
        :param _ProtectedResourceCopyingCount: 受保护资源-复制中
        :type ProtectedResourceCopyingCount: int
        :param _ProtectedResourceStoppedCount: 受保护资源-已停止/初始化
        :type ProtectedResourceStoppedCount: int
        :param _FailoverFailedCount: 切换失败
        :type FailoverFailedCount: int
        """
        self._Region = None
        self._SitePairCount = None
        self._SitePairCrossRegionCount = None
        self._SitePairCrossZoneCount = None
        self._SitePairCrossCloudCount = None
        self._ProtectGroupCount = None
        self._ProtectGroupCrossRegionCount = None
        self._ProtectGroupCrossZoneCount = None
        self._ProtectGroupCrossCloudCount = None
        self._CopyPairCount = None
        self._CopyPairSuccessRPOCount = None
        self._CopyPairErrorRPOCount = None
        self._DrillPairCount = None
        self._DrillPairDrillingCount = None
        self._DrillPairFailedCount = None
        self._DrillPairSuccessCount = None
        self._ProtectedResourceCount = None
        self._ProtectedResourceCopyingCount = None
        self._ProtectedResourceStoppedCount = None
        self._FailoverFailedCount = None

    @property
    def Region(self):
        r"""地域 ID
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SitePairCount(self):
        r"""站点对总数
        :rtype: int
        """
        return self._SitePairCount

    @SitePairCount.setter
    def SitePairCount(self, SitePairCount):
        self._SitePairCount = SitePairCount

    @property
    def SitePairCrossRegionCount(self):
        r"""跨地域站点对数
        :rtype: int
        """
        return self._SitePairCrossRegionCount

    @SitePairCrossRegionCount.setter
    def SitePairCrossRegionCount(self, SitePairCrossRegionCount):
        self._SitePairCrossRegionCount = SitePairCrossRegionCount

    @property
    def SitePairCrossZoneCount(self):
        r"""跨可用区站点对数
        :rtype: int
        """
        return self._SitePairCrossZoneCount

    @SitePairCrossZoneCount.setter
    def SitePairCrossZoneCount(self, SitePairCrossZoneCount):
        self._SitePairCrossZoneCount = SitePairCrossZoneCount

    @property
    def SitePairCrossCloudCount(self):
        r"""跨云站点对数
        :rtype: int
        """
        return self._SitePairCrossCloudCount

    @SitePairCrossCloudCount.setter
    def SitePairCrossCloudCount(self, SitePairCrossCloudCount):
        self._SitePairCrossCloudCount = SitePairCrossCloudCount

    @property
    def ProtectGroupCount(self):
        r"""保护组总数
        :rtype: int
        """
        return self._ProtectGroupCount

    @ProtectGroupCount.setter
    def ProtectGroupCount(self, ProtectGroupCount):
        self._ProtectGroupCount = ProtectGroupCount

    @property
    def ProtectGroupCrossRegionCount(self):
        r"""跨地域保护组数
        :rtype: int
        """
        return self._ProtectGroupCrossRegionCount

    @ProtectGroupCrossRegionCount.setter
    def ProtectGroupCrossRegionCount(self, ProtectGroupCrossRegionCount):
        self._ProtectGroupCrossRegionCount = ProtectGroupCrossRegionCount

    @property
    def ProtectGroupCrossZoneCount(self):
        r"""跨可用区保护组数
        :rtype: int
        """
        return self._ProtectGroupCrossZoneCount

    @ProtectGroupCrossZoneCount.setter
    def ProtectGroupCrossZoneCount(self, ProtectGroupCrossZoneCount):
        self._ProtectGroupCrossZoneCount = ProtectGroupCrossZoneCount

    @property
    def ProtectGroupCrossCloudCount(self):
        r"""跨云保护组数
        :rtype: int
        """
        return self._ProtectGroupCrossCloudCount

    @ProtectGroupCrossCloudCount.setter
    def ProtectGroupCrossCloudCount(self, ProtectGroupCrossCloudCount):
        self._ProtectGroupCrossCloudCount = ProtectGroupCrossCloudCount

    @property
    def CopyPairCount(self):
        r"""复制对总数
        :rtype: int
        """
        return self._CopyPairCount

    @CopyPairCount.setter
    def CopyPairCount(self, CopyPairCount):
        self._CopyPairCount = CopyPairCount

    @property
    def CopyPairSuccessRPOCount(self):
        r"""RPO 正常的复制对数
        :rtype: int
        """
        return self._CopyPairSuccessRPOCount

    @CopyPairSuccessRPOCount.setter
    def CopyPairSuccessRPOCount(self, CopyPairSuccessRPOCount):
        self._CopyPairSuccessRPOCount = CopyPairSuccessRPOCount

    @property
    def CopyPairErrorRPOCount(self):
        r"""RPO 异常的复制对数
        :rtype: int
        """
        return self._CopyPairErrorRPOCount

    @CopyPairErrorRPOCount.setter
    def CopyPairErrorRPOCount(self, CopyPairErrorRPOCount):
        self._CopyPairErrorRPOCount = CopyPairErrorRPOCount

    @property
    def DrillPairCount(self):
        r"""演练对总数
        :rtype: int
        """
        return self._DrillPairCount

    @DrillPairCount.setter
    def DrillPairCount(self, DrillPairCount):
        self._DrillPairCount = DrillPairCount

    @property
    def DrillPairDrillingCount(self):
        r"""演练中
        :rtype: int
        """
        return self._DrillPairDrillingCount

    @DrillPairDrillingCount.setter
    def DrillPairDrillingCount(self, DrillPairDrillingCount):
        self._DrillPairDrillingCount = DrillPairDrillingCount

    @property
    def DrillPairFailedCount(self):
        r"""演练失败
        :rtype: int
        """
        return self._DrillPairFailedCount

    @DrillPairFailedCount.setter
    def DrillPairFailedCount(self, DrillPairFailedCount):
        self._DrillPairFailedCount = DrillPairFailedCount

    @property
    def DrillPairSuccessCount(self):
        r"""演练成功
        :rtype: int
        """
        return self._DrillPairSuccessCount

    @DrillPairSuccessCount.setter
    def DrillPairSuccessCount(self, DrillPairSuccessCount):
        self._DrillPairSuccessCount = DrillPairSuccessCount

    @property
    def ProtectedResourceCount(self):
        r"""受保护资源总数
        :rtype: int
        """
        return self._ProtectedResourceCount

    @ProtectedResourceCount.setter
    def ProtectedResourceCount(self, ProtectedResourceCount):
        self._ProtectedResourceCount = ProtectedResourceCount

    @property
    def ProtectedResourceCopyingCount(self):
        r"""受保护资源-复制中
        :rtype: int
        """
        return self._ProtectedResourceCopyingCount

    @ProtectedResourceCopyingCount.setter
    def ProtectedResourceCopyingCount(self, ProtectedResourceCopyingCount):
        self._ProtectedResourceCopyingCount = ProtectedResourceCopyingCount

    @property
    def ProtectedResourceStoppedCount(self):
        r"""受保护资源-已停止/初始化
        :rtype: int
        """
        return self._ProtectedResourceStoppedCount

    @ProtectedResourceStoppedCount.setter
    def ProtectedResourceStoppedCount(self, ProtectedResourceStoppedCount):
        self._ProtectedResourceStoppedCount = ProtectedResourceStoppedCount

    @property
    def FailoverFailedCount(self):
        r"""切换失败
        :rtype: int
        """
        return self._FailoverFailedCount

    @FailoverFailedCount.setter
    def FailoverFailedCount(self, FailoverFailedCount):
        self._FailoverFailedCount = FailoverFailedCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._SitePairCount = params.get("SitePairCount")
        self._SitePairCrossRegionCount = params.get("SitePairCrossRegionCount")
        self._SitePairCrossZoneCount = params.get("SitePairCrossZoneCount")
        self._SitePairCrossCloudCount = params.get("SitePairCrossCloudCount")
        self._ProtectGroupCount = params.get("ProtectGroupCount")
        self._ProtectGroupCrossRegionCount = params.get("ProtectGroupCrossRegionCount")
        self._ProtectGroupCrossZoneCount = params.get("ProtectGroupCrossZoneCount")
        self._ProtectGroupCrossCloudCount = params.get("ProtectGroupCrossCloudCount")
        self._CopyPairCount = params.get("CopyPairCount")
        self._CopyPairSuccessRPOCount = params.get("CopyPairSuccessRPOCount")
        self._CopyPairErrorRPOCount = params.get("CopyPairErrorRPOCount")
        self._DrillPairCount = params.get("DrillPairCount")
        self._DrillPairDrillingCount = params.get("DrillPairDrillingCount")
        self._DrillPairFailedCount = params.get("DrillPairFailedCount")
        self._DrillPairSuccessCount = params.get("DrillPairSuccessCount")
        self._ProtectedResourceCount = params.get("ProtectedResourceCount")
        self._ProtectedResourceCopyingCount = params.get("ProtectedResourceCopyingCount")
        self._ProtectedResourceStoppedCount = params.get("ProtectedResourceStoppedCount")
        self._FailoverFailedCount = params.get("FailoverFailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskCopyPairForCvm(AbstractModel):
    r"""cvm的盘复制对信息

    """

    def __init__(self):
        r"""
        :param _CopyPairId: 云硬盘复制对ID
        :type CopyPairId: str
        :param _CopyPairName: 云硬盘复制对名称
        :type CopyPairName: str
        :param _SourceResourceId: 生产端云硬盘ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceResourceId: str
        :param _TargetResourceId: 容灾端云硬盘ID（延迟创建模式且 CVM 未真实创建时被脱敏为空字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetResourceId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._CopyPairId = None
        self._CopyPairName = None
        self._SourceResourceId = None
        self._TargetResourceId = None
        self._CreateTime = None

    @property
    def CopyPairId(self):
        r"""云硬盘复制对ID
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def CopyPairName(self):
        r"""云硬盘复制对名称
        :rtype: str
        """
        return self._CopyPairName

    @CopyPairName.setter
    def CopyPairName(self, CopyPairName):
        self._CopyPairName = CopyPairName

    @property
    def SourceResourceId(self):
        r"""生产端云硬盘ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceResourceId

    @SourceResourceId.setter
    def SourceResourceId(self, SourceResourceId):
        self._SourceResourceId = SourceResourceId

    @property
    def TargetResourceId(self):
        r"""容灾端云硬盘ID（延迟创建模式且 CVM 未真实创建时被脱敏为空字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetResourceId

    @TargetResourceId.setter
    def TargetResourceId(self, TargetResourceId):
        self._TargetResourceId = TargetResourceId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._CopyPairId = params.get("CopyPairId")
        self._CopyPairName = params.get("CopyPairName")
        self._SourceResourceId = params.get("SourceResourceId")
        self._TargetResourceId = params.get("TargetResourceId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    r"""描述容灾云硬盘的详情，如云硬盘的镜像格式。

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID
        :type DiskId: str
        :param _ImageFormat: 云盘的镜像格式。QCOW2:  qcow2格式，这种格式的云盘不能用于容灾；RAW：raw格式，可以用于容灾。
        :type ImageFormat: str
        """
        self._DiskId = None
        self._ImageFormat = None

    @property
    def DiskId(self):
        r"""云硬盘ID
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def ImageFormat(self):
        r"""云盘的镜像格式。QCOW2:  qcow2格式，这种格式的云盘不能用于容灾；RAW：raw格式，可以用于容灾。
        :rtype: str
        """
        return self._ImageFormat

    @ImageFormat.setter
    def ImageFormat(self, ImageFormat):
        self._ImageFormat = ImageFormat


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._ImageFormat = params.get("ImageFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskModel(AbstractModel):
    r"""云盘信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 云盘类型
        :type DiskType: str
        :param _DiskSize: 云盘大小（单位GB，范围 (0, 32000]）
        :type DiskSize: int
        :param _DeleteWithInstance: 是否随实例删除（仅 DataDisks 元素能传）
        :type DeleteWithInstance: bool
        """
        self._DiskType = None
        self._DiskSize = None
        self._DeleteWithInstance = None

    @property
    def DiskType(self):
        r"""云盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""云盘大小（单位GB，范围 (0, 32000]）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DeleteWithInstance(self):
        r"""是否随实例删除（仅 DataDisks 元素能传）
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrillPair(AbstractModel):
    r"""演练对

    """

    def __init__(self):
        r"""
        :param _AppId: 用户ID
        :type AppId: int
        :param _DrillPairId: 演练对ID
        :type DrillPairId: str
        :param _DrillPairName: 演练对名称
        :type DrillPairName: str
        :param _DrillPairState: 演练对状态。枚举值：RUNNING / SUCCESS / FAILED 等。
        :type DrillPairState: str
        :param _SitePairId: 容灾站点对ID
        :type SitePairId: str
        :param _CopyPairId: 云硬盘复制对ID
        :type CopyPairId: str
        :param _SourceRegion: 生产地域
        :type SourceRegion: str
        :param _SourceZone: 生产可用区
        :type SourceZone: str
        :param _TargetRegion: 容灾地域
        :type TargetRegion: str
        :param _TargetZone: 容灾可用区
        :type TargetZone: str
        :param _SourceResourceId: 生产站点盘ID
        :type SourceResourceId: str
        :param _TargetResourceId: 演练资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetResourceId: str
        :param _DrillPairType: 演练对的类型。枚举值：DISK / INSTANCE / CFS。
        :type DrillPairType: str
        :param _Size: 演练资源容量（GB）。
        :type Size: int
        :param _RecoveryTime: 演练的容灾点
注意：此字段可能返回 null，表示取不到有效值。
        :type RecoveryTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _EndTime: 演练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Rollbacking: 是否正在回滚。0 - 未回滚，1 - 回滚中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rollbacking: int
        :param _RollbackPercent: 回滚进度百分比（0-100）。
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackPercent: int
        :param _AccountUin: 创建定期备份策略的账户uin ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 创建定期备份策略的子账户uin ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _ProtectGroupId: 保护组ID
        :type ProtectGroupId: str
        :param _DrillGroupId: 演练组ID
        :type DrillGroupId: str
        :param _CopyPairName: 复制对名称。
        :type CopyPairName: str
        :param _DrillGroupName: 演练组名称。
        :type DrillGroupName: str
        """
        self._AppId = None
        self._DrillPairId = None
        self._DrillPairName = None
        self._DrillPairState = None
        self._SitePairId = None
        self._CopyPairId = None
        self._SourceRegion = None
        self._SourceZone = None
        self._TargetRegion = None
        self._TargetZone = None
        self._SourceResourceId = None
        self._TargetResourceId = None
        self._DrillPairType = None
        self._Size = None
        self._RecoveryTime = None
        self._CreateTime = None
        self._EndTime = None
        self._Rollbacking = None
        self._RollbackPercent = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._ProtectGroupId = None
        self._DrillGroupId = None
        self._CopyPairName = None
        self._DrillGroupName = None

    @property
    def AppId(self):
        r"""用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def DrillPairId(self):
        r"""演练对ID
        :rtype: str
        """
        return self._DrillPairId

    @DrillPairId.setter
    def DrillPairId(self, DrillPairId):
        self._DrillPairId = DrillPairId

    @property
    def DrillPairName(self):
        r"""演练对名称
        :rtype: str
        """
        return self._DrillPairName

    @DrillPairName.setter
    def DrillPairName(self, DrillPairName):
        self._DrillPairName = DrillPairName

    @property
    def DrillPairState(self):
        r"""演练对状态。枚举值：RUNNING / SUCCESS / FAILED 等。
        :rtype: str
        """
        return self._DrillPairState

    @DrillPairState.setter
    def DrillPairState(self, DrillPairState):
        self._DrillPairState = DrillPairState

    @property
    def SitePairId(self):
        r"""容灾站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def CopyPairId(self):
        r"""云硬盘复制对ID
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def SourceRegion(self):
        r"""生产地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""生产可用区
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def TargetRegion(self):
        r"""容灾地域
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetZone(self):
        r"""容灾可用区
        :rtype: str
        """
        return self._TargetZone

    @TargetZone.setter
    def TargetZone(self, TargetZone):
        self._TargetZone = TargetZone

    @property
    def SourceResourceId(self):
        r"""生产站点盘ID
        :rtype: str
        """
        return self._SourceResourceId

    @SourceResourceId.setter
    def SourceResourceId(self, SourceResourceId):
        self._SourceResourceId = SourceResourceId

    @property
    def TargetResourceId(self):
        r"""演练资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetResourceId

    @TargetResourceId.setter
    def TargetResourceId(self, TargetResourceId):
        self._TargetResourceId = TargetResourceId

    @property
    def DrillPairType(self):
        r"""演练对的类型。枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._DrillPairType

    @DrillPairType.setter
    def DrillPairType(self, DrillPairType):
        self._DrillPairType = DrillPairType

    @property
    def Size(self):
        r"""演练资源容量（GB）。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def RecoveryTime(self):
        r"""演练的容灾点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecoveryTime

    @RecoveryTime.setter
    def RecoveryTime(self, RecoveryTime):
        self._RecoveryTime = RecoveryTime

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
    def EndTime(self):
        r"""演练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Rollbacking(self):
        r"""是否正在回滚。0 - 未回滚，1 - 回滚中。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def RollbackPercent(self):
        r"""回滚进度百分比（0-100）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

    @property
    def AccountUin(self):
        r"""创建定期备份策略的账户uin ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""创建定期备份策略的子账户uin ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def ProtectGroupId(self):
        r"""保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def DrillGroupId(self):
        r"""演练组ID
        :rtype: str
        """
        return self._DrillGroupId

    @DrillGroupId.setter
    def DrillGroupId(self, DrillGroupId):
        self._DrillGroupId = DrillGroupId

    @property
    def CopyPairName(self):
        r"""复制对名称。
        :rtype: str
        """
        return self._CopyPairName

    @CopyPairName.setter
    def CopyPairName(self, CopyPairName):
        self._CopyPairName = CopyPairName

    @property
    def DrillGroupName(self):
        r"""演练组名称。
        :rtype: str
        """
        return self._DrillGroupName

    @DrillGroupName.setter
    def DrillGroupName(self, DrillGroupName):
        self._DrillGroupName = DrillGroupName


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._DrillPairId = params.get("DrillPairId")
        self._DrillPairName = params.get("DrillPairName")
        self._DrillPairState = params.get("DrillPairState")
        self._SitePairId = params.get("SitePairId")
        self._CopyPairId = params.get("CopyPairId")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetZone = params.get("TargetZone")
        self._SourceResourceId = params.get("SourceResourceId")
        self._TargetResourceId = params.get("TargetResourceId")
        self._DrillPairType = params.get("DrillPairType")
        self._Size = params.get("Size")
        self._RecoveryTime = params.get("RecoveryTime")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._Rollbacking = params.get("Rollbacking")
        self._RollbackPercent = params.get("RollbackPercent")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._DrillGroupId = params.get("DrillGroupId")
        self._CopyPairName = params.get("CopyPairName")
        self._DrillGroupName = params.get("DrillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrillPairDeniedAction(AbstractModel):
    r"""演练对操作掩码

    """

    def __init__(self):
        r"""
        :param _DrillPairId: 演练对ID
        :type DrillPairId: str
        :param _DeniedActions: 被禁止的操作列表（Action名称数组）
        :type DeniedActions: list of DeniedAction
        """
        self._DrillPairId = None
        self._DeniedActions = None

    @property
    def DrillPairId(self):
        r"""演练对ID
        :rtype: str
        """
        return self._DrillPairId

    @DrillPairId.setter
    def DrillPairId(self, DrillPairId):
        self._DrillPairId = DrillPairId

    @property
    def DeniedActions(self):
        r"""被禁止的操作列表（Action名称数组）
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._DrillPairId = params.get("DrillPairId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrilledResourceStatus(AbstractModel):
    r"""演练组关联的演练资源的状态数量统计

    """

    def __init__(self):
        r"""
        :param _ResourceStatus: 演练组关联的演练资源的状态
        :type ResourceStatus: str
        :param _ResourceCount: 演练组关联演练资源处于某个状态的数量
        :type ResourceCount: int
        """
        self._ResourceStatus = None
        self._ResourceCount = None

    @property
    def ResourceStatus(self):
        r"""演练组关联的演练资源的状态
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceCount(self):
        r"""演练组关联演练资源处于某个状态的数量
        :rtype: int
        """
        return self._ResourceCount

    @ResourceCount.setter
    def ResourceCount(self, ResourceCount):
        self._ResourceCount = ResourceCount


    def _deserialize(self, params):
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceCount = params.get("ResourceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    r"""描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        r"""
        :param _SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.bdrc.v20260330.models.RunSecurityServiceEnabled`
        :param _MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.bdrc.v20260330.models.RunSecurityServiceEnabled`
        :param _AutomationService: 安装 tat-agent。若不指定该参数，则默认逻辑与 CVM 控制台一致：境外地域不安装、境内非 GPU 机型默认安装、境内 GPU 机型默认不安装。
        :type AutomationService: :class:`tencentcloud.bdrc.v20260330.models.AutomationServiceEnabled`
        :param _BasicService: 开启基础服务。
        :type BasicService: :class:`tencentcloud.bdrc.v20260330.models.BasicServicesSettings`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None
        self._BasicService = None

    @property
    def SecurityService(self):
        r"""开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        r"""开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.RunSecurityServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        r"""安装 tat-agent。若不指定该参数，则默认逻辑与 CVM 控制台一致：境外地域不安装、境内非 GPU 机型默认安装、境内 GPU 机型默认不安装。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.AutomationServiceEnabled`
        """
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService

    @property
    def BasicService(self):
        r"""开启基础服务。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.BasicServicesSettings`
        """
        return self._BasicService

    @BasicService.setter
    def BasicService(self, BasicService):
        self._BasicService = BasicService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunSecurityServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = AutomationServiceEnabled()
            self._AutomationService._deserialize(params.get("AutomationService"))
        if params.get("BasicService") is not None:
            self._BasicService = BasicServicesSettings()
            self._BasicService._deserialize(params.get("BasicService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileBackupOverview(AbstractModel):
    r"""文件备份概览数据

    """

    def __init__(self):
        r"""
        :param _BackupCount: 整机备份点总数
        :type BackupCount: int
        :param _CreatingBackupCount: 创建中数量
        :type CreatingBackupCount: int
        :param _FailedBackupCount: 失败数量
        :type FailedBackupCount: int
        :param _SuccessBackupCount: 已完成数量
        :type SuccessBackupCount: int
        :param _RestoringBackupCount: 恢复中的总数量
        :type RestoringBackupCount: int
        :param _BackupSizeMb: 整机备份总容量
        :type BackupSizeMb: int
        :param _BackupResourceCount: 受保护 CVM 资源数
        :type BackupResourceCount: int
        """
        self._BackupCount = None
        self._CreatingBackupCount = None
        self._FailedBackupCount = None
        self._SuccessBackupCount = None
        self._RestoringBackupCount = None
        self._BackupSizeMb = None
        self._BackupResourceCount = None

    @property
    def BackupCount(self):
        r"""整机备份点总数
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def CreatingBackupCount(self):
        r"""创建中数量
        :rtype: int
        """
        return self._CreatingBackupCount

    @CreatingBackupCount.setter
    def CreatingBackupCount(self, CreatingBackupCount):
        self._CreatingBackupCount = CreatingBackupCount

    @property
    def FailedBackupCount(self):
        r"""失败数量
        :rtype: int
        """
        return self._FailedBackupCount

    @FailedBackupCount.setter
    def FailedBackupCount(self, FailedBackupCount):
        self._FailedBackupCount = FailedBackupCount

    @property
    def SuccessBackupCount(self):
        r"""已完成数量
        :rtype: int
        """
        return self._SuccessBackupCount

    @SuccessBackupCount.setter
    def SuccessBackupCount(self, SuccessBackupCount):
        self._SuccessBackupCount = SuccessBackupCount

    @property
    def RestoringBackupCount(self):
        r"""恢复中的总数量
        :rtype: int
        """
        return self._RestoringBackupCount

    @RestoringBackupCount.setter
    def RestoringBackupCount(self, RestoringBackupCount):
        self._RestoringBackupCount = RestoringBackupCount

    @property
    def BackupSizeMb(self):
        r"""整机备份总容量
        :rtype: int
        """
        return self._BackupSizeMb

    @BackupSizeMb.setter
    def BackupSizeMb(self, BackupSizeMb):
        self._BackupSizeMb = BackupSizeMb

    @property
    def BackupResourceCount(self):
        r"""受保护 CVM 资源数
        :rtype: int
        """
        return self._BackupResourceCount

    @BackupResourceCount.setter
    def BackupResourceCount(self, BackupResourceCount):
        self._BackupResourceCount = BackupResourceCount


    def _deserialize(self, params):
        self._BackupCount = params.get("BackupCount")
        self._CreatingBackupCount = params.get("CreatingBackupCount")
        self._FailedBackupCount = params.get("FailedBackupCount")
        self._SuccessBackupCount = params.get("SuccessBackupCount")
        self._RestoringBackupCount = params.get("RestoringBackupCount")
        self._BackupSizeMb = params.get("BackupSizeMb")
        self._BackupResourceCount = params.get("BackupResourceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterModel(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤器名
        :type Name: str
        :param _Values: 过滤器值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤器名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤器值
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
        


class FinishFailoverCopyPairsRequest(AbstractModel):
    r"""FinishFailoverCopyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: <p>复制对ID列表。长度范围 [1, 50]。当 CopyPairType=INSTANCE 时传 CVM 复制对ID，否则传云盘/CFS 复制对ID。</p>
        :type CopyPairIds: list of str
        :param _CopyPairType: <p>要完成切换的复制对类型。枚举值：DISK / INSTANCE / CFS。</p>
        :type CopyPairType: str
        """
        self._CopyPairIds = None
        self._CopyPairType = None

    @property
    def CopyPairIds(self):
        r"""<p>复制对ID列表。长度范围 [1, 50]。当 CopyPairType=INSTANCE 时传 CVM 复制对ID，否则传云盘/CFS 复制对ID。</p>
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""<p>要完成切换的复制对类型。枚举值：DISK / INSTANCE / CFS。</p>
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinishFailoverCopyPairsResponse(AbstractModel):
    r"""FinishFailoverCopyPairs返回参数结构体

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


class FlowControlRule(AbstractModel):
    r"""流控规则

    """

    def __init__(self):
        r"""
        :param _StartTime: 流控开始时间
        :type StartTime: str
        :param _EndTime: 流控结束时间
        :type EndTime: str
        :param _MaxBandwidthMBps: 流控规则最大带宽，单位MB/s
        :type MaxBandwidthMBps: int
        """
        self._StartTime = None
        self._EndTime = None
        self._MaxBandwidthMBps = None

    @property
    def StartTime(self):
        r"""流控开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""流控结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MaxBandwidthMBps(self):
        r"""流控规则最大带宽，单位MB/s
        :rtype: int
        """
        return self._MaxBandwidthMBps

    @MaxBandwidthMBps.setter
    def MaxBandwidthMBps(self, MaxBandwidthMBps):
        self._MaxBandwidthMBps = MaxBandwidthMBps


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MaxBandwidthMBps = params.get("MaxBandwidthMBps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBackupOverview(AbstractModel):
    r"""整机备份（CVM 备份组）概览数据

    """

    def __init__(self):
        r"""
        :param _BackupCount: 整机备份点总数
        :type BackupCount: int
        :param _CreatingBackupCount: 创建中数量
        :type CreatingBackupCount: int
        :param _FailedBackupCount: 失败数量
        :type FailedBackupCount: int
        :param _SuccessBackupCount: 已完成数量
        :type SuccessBackupCount: int
        :param _RestoringBackupCount: 恢复中的总数量
        :type RestoringBackupCount: int
        :param _BackupSizeMb: 整机备份总容量
        :type BackupSizeMb: int
        :param _BackupResourceCount: 受保护 CVM 资源数
        :type BackupResourceCount: int
        """
        self._BackupCount = None
        self._CreatingBackupCount = None
        self._FailedBackupCount = None
        self._SuccessBackupCount = None
        self._RestoringBackupCount = None
        self._BackupSizeMb = None
        self._BackupResourceCount = None

    @property
    def BackupCount(self):
        r"""整机备份点总数
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def CreatingBackupCount(self):
        r"""创建中数量
        :rtype: int
        """
        return self._CreatingBackupCount

    @CreatingBackupCount.setter
    def CreatingBackupCount(self, CreatingBackupCount):
        self._CreatingBackupCount = CreatingBackupCount

    @property
    def FailedBackupCount(self):
        r"""失败数量
        :rtype: int
        """
        return self._FailedBackupCount

    @FailedBackupCount.setter
    def FailedBackupCount(self, FailedBackupCount):
        self._FailedBackupCount = FailedBackupCount

    @property
    def SuccessBackupCount(self):
        r"""已完成数量
        :rtype: int
        """
        return self._SuccessBackupCount

    @SuccessBackupCount.setter
    def SuccessBackupCount(self, SuccessBackupCount):
        self._SuccessBackupCount = SuccessBackupCount

    @property
    def RestoringBackupCount(self):
        r"""恢复中的总数量
        :rtype: int
        """
        return self._RestoringBackupCount

    @RestoringBackupCount.setter
    def RestoringBackupCount(self, RestoringBackupCount):
        self._RestoringBackupCount = RestoringBackupCount

    @property
    def BackupSizeMb(self):
        r"""整机备份总容量
        :rtype: int
        """
        return self._BackupSizeMb

    @BackupSizeMb.setter
    def BackupSizeMb(self, BackupSizeMb):
        self._BackupSizeMb = BackupSizeMb

    @property
    def BackupResourceCount(self):
        r"""受保护 CVM 资源数
        :rtype: int
        """
        return self._BackupResourceCount

    @BackupResourceCount.setter
    def BackupResourceCount(self, BackupResourceCount):
        self._BackupResourceCount = BackupResourceCount


    def _deserialize(self, params):
        self._BackupCount = params.get("BackupCount")
        self._CreatingBackupCount = params.get("CreatingBackupCount")
        self._FailedBackupCount = params.get("FailedBackupCount")
        self._SuccessBackupCount = params.get("SuccessBackupCount")
        self._RestoringBackupCount = params.get("RestoringBackupCount")
        self._BackupSizeMb = params.get("BackupSizeMb")
        self._BackupResourceCount = params.get("BackupResourceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    r"""描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：NOTIFY_AND_AUTO_RENEW（通知过期且自动续费）、NOTIFY_AND_MANUAL_RENEW（通知过期不自动续费）、DISABLE_NOTIFY_AND_MANUAL_RENEW（不通知过期不自动续费）。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        r"""购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：NOTIFY_AND_AUTO_RENEW（通知过期且自动续费）、NOTIFY_AND_MANUAL_RENEW（通知过期不自动续费）、DISABLE_NOTIFY_AND_MANUAL_RENEW（不通知过期不自动续费）。
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
        


class InternetAccessible(AbstractModel):
    r"""描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：BANDWIDTH_PREPAID（预付费按带宽结算）、TRAFFIC_POSTPAID_BY_HOUR（流量按小时后付费）、BANDWIDTH_POSTPAID_BY_HOUR（带宽按小时后付费）、BANDWIDTH_PACKAGE（带宽包用户）。默认取值：非带宽包用户默认与子机付费类型保持一致。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网IP。取值范围：true（表示分配公网IP）/false（表示不分配公网IP）。当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。该参数仅在 RunInstances 接口中作为入参使用。
        :type PublicIpAssigned: bool
        :param _InternetServiceProvider: 网络模式：移动:"CMCC"、电信:"CTCC"、联通:"CUCC"。
        :type InternetServiceProvider: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._InternetServiceProvider = None

    @property
    def InternetChargeType(self):
        r"""网络计费类型。取值范围：BANDWIDTH_PREPAID（预付费按带宽结算）、TRAFFIC_POSTPAID_BY_HOUR（流量按小时后付费）、BANDWIDTH_POSTPAID_BY_HOUR（带宽按小时后付费）、BANDWIDTH_PACKAGE（带宽包用户）。默认取值：非带宽包用户默认与子机付费类型保持一致。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        r"""公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        r"""是否分配公网IP。取值范围：true（表示分配公网IP）/false（表示不分配公网IP）。当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。该参数仅在 RunInstances 接口中作为入参使用。
        :rtype: bool
        """
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def InternetServiceProvider(self):
        r"""网络模式：移动:"CMCC"、电信:"CTCC"、联通:"CUCC"。
        :rtype: str
        """
        return self._InternetServiceProvider

    @InternetServiceProvider.setter
    def InternetServiceProvider(self, InternetServiceProvider):
        self._InternetServiceProvider = InternetServiceProvider


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._InternetServiceProvider = params.get("InternetServiceProvider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    r"""描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：Linux 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能以"/"开头，至少包含以下字符中的三种不同字符，字符种类：小写字母 a-z、大写字母 A-Z、数字 0-9、特殊字符 ()`~!@#$%^&*-+=_|{}[]:;'<>,.?/。Windows 实例密码必须 12-30 位，不能以"/"开头且不包括用户名，至少包含以下字符中的三种不同字符，字符种类：小写字母 a-z、大写字母 A-Z、数字 0-9、特殊字符 ()`~!@#$%^&*-+=_|{}[]:;' <>,.?/。若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param _KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) 获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :type KeyIds: list of str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与 Password 或 KeyIds.N 不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为 TRUE。取值范围：TRUE（表示保持镜像的登录设置）/FALSE（表示不保持镜像的登录设置）。默认取值：FALSE。
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        r"""实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：Linux 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能以"/"开头，至少包含以下字符中的三种不同字符，字符种类：小写字母 a-z、大写字母 A-Z、数字 0-9、特殊字符 ()`~!@#$%^&*-+=_|{}[]:;'<>,.?/。Windows 实例密码必须 12-30 位，不能以"/"开头且不包括用户名，至少包含以下字符中的三种不同字符，字符种类：小写字母 a-z、大写字母 A-Z、数字 0-9、特殊字符 ()`~!@#$%^&*-+=_|{}[]:;' <>,.?/。若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        r"""密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) 获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        r"""保持镜像的原始设置。该参数与 Password 或 KeyIds.N 不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为 TRUE。取值范围：TRUE（表示保持镜像的登录设置）/FALSE（表示不保持镜像的登录设置）。默认取值：FALSE。
        :rtype: str
        """
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
        


class ModifyAutoBackupPolicyAttributeRequest(AbstractModel):
    r"""ModifyAutoBackupPolicyAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoBackupPolicyId: 备份策略id
        :type AutoBackupPolicyId: str
        :param _Policy: 定期备份的执行策略。
        :type Policy: list of Policy
        :param _IsPermanent: 通过该定期备份策略创建的备份是否永久保留。false表示非永久保留，true表示永久保留，默认为false。
        :type IsPermanent: bool
        :param _AutoBackupPolicyName: 定期备份策略的名称。
        :type AutoBackupPolicyName: str
        :param _IsActivated: 是否激活定期备份策略。
        :type IsActivated: bool
        :param _RetentionDays: 通过定期备份策略创建出的备份保留时间。
        :type RetentionDays: int
        :param _RetentionMonths: 该定期备份策略创建的备份可以保留的月数，该参数不可与IsPermanent/RetentionDays参数冲突。
        :type RetentionMonths: int
        :param _RetentionAmount: 通过该定期备份策略最多保留的备份个数，超过该个数限制后自动删除最先创建的备份，该参数不可与IsPermanent参数冲突。
        :type RetentionAmount: int
        :param _StorageType: 备份存储类型。SNAPSHOT表示走快照（不需要备份库），VAULT表示走备份库（必须关联一个备份库）。默认为SNAPSHOT
        :type StorageType: str
        :param _VaultId: 备份库ID，创建agent备份策略时必须指定。当StorageType为VAULT时必传。
        :type VaultId: str
        :param _AdvancedRetentionPolicy: 定期备份高级保留策略，该参数不可与IsPermanent参数冲突。
        :type AdvancedRetentionPolicy: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        self._AutoBackupPolicyId = None
        self._Policy = None
        self._IsPermanent = None
        self._AutoBackupPolicyName = None
        self._IsActivated = None
        self._RetentionDays = None
        self._RetentionMonths = None
        self._RetentionAmount = None
        self._StorageType = None
        self._VaultId = None
        self._AdvancedRetentionPolicy = None

    @property
    def AutoBackupPolicyId(self):
        r"""备份策略id
        :rtype: str
        """
        return self._AutoBackupPolicyId

    @AutoBackupPolicyId.setter
    def AutoBackupPolicyId(self, AutoBackupPolicyId):
        self._AutoBackupPolicyId = AutoBackupPolicyId

    @property
    def Policy(self):
        r"""定期备份的执行策略。
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def IsPermanent(self):
        r"""通过该定期备份策略创建的备份是否永久保留。false表示非永久保留，true表示永久保留，默认为false。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def AutoBackupPolicyName(self):
        r"""定期备份策略的名称。
        :rtype: str
        """
        return self._AutoBackupPolicyName

    @AutoBackupPolicyName.setter
    def AutoBackupPolicyName(self, AutoBackupPolicyName):
        self._AutoBackupPolicyName = AutoBackupPolicyName

    @property
    def IsActivated(self):
        r"""是否激活定期备份策略。
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def RetentionDays(self):
        r"""通过定期备份策略创建出的备份保留时间。
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def RetentionMonths(self):
        r"""该定期备份策略创建的备份可以保留的月数，该参数不可与IsPermanent/RetentionDays参数冲突。
        :rtype: int
        """
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        r"""通过该定期备份策略最多保留的备份个数，超过该个数限制后自动删除最先创建的备份，该参数不可与IsPermanent参数冲突。
        :rtype: int
        """
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def StorageType(self):
        r"""备份存储类型。SNAPSHOT表示走快照（不需要备份库），VAULT表示走备份库（必须关联一个备份库）。默认为SNAPSHOT
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VaultId(self):
        r"""备份库ID，创建agent备份策略时必须指定。当StorageType为VAULT时必传。
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def AdvancedRetentionPolicy(self):
        r"""定期备份高级保留策略，该参数不可与IsPermanent参数冲突。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.AdvancedRetentionPolicy`
        """
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy


    def _deserialize(self, params):
        self._AutoBackupPolicyId = params.get("AutoBackupPolicyId")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._IsPermanent = params.get("IsPermanent")
        self._AutoBackupPolicyName = params.get("AutoBackupPolicyName")
        self._IsActivated = params.get("IsActivated")
        self._RetentionDays = params.get("RetentionDays")
        self._RetentionMonths = params.get("RetentionMonths")
        self._RetentionAmount = params.get("RetentionAmount")
        self._StorageType = params.get("StorageType")
        self._VaultId = params.get("VaultId")
        if params.get("AdvancedRetentionPolicy") is not None:
            self._AdvancedRetentionPolicy = AdvancedRetentionPolicy()
            self._AdvancedRetentionPolicy._deserialize(params.get("AdvancedRetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupPolicyAttributeResponse(AbstractModel):
    r"""ModifyAutoBackupPolicyAttribute返回参数结构体

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


class ModifyBackupAttributeRequest(AbstractModel):
    r"""ModifyBackupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份ID。该字段的取值取决于ResourceType：当ResourceType=CVM（默认）时，需传入备份组ID（BackupGroupId），可通过DescribeBackupGroups（查询备份组列表）查询
        :type BackupId: str
        :param _BackupName: 备份的名称。
        :type BackupName: str
        :param _IsPermanent: 是否为永久保留的备份。
        :type IsPermanent: bool
        :param _Deadline: 备份到期时间。
        :type Deadline: str
        """
        self._BackupId = None
        self._BackupName = None
        self._IsPermanent = None
        self._Deadline = None

    @property
    def BackupId(self):
        r"""备份ID。该字段的取值取决于ResourceType：当ResourceType=CVM（默认）时，需传入备份组ID（BackupGroupId），可通过DescribeBackupGroups（查询备份组列表）查询
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        r"""备份的名称。
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def IsPermanent(self):
        r"""是否为永久保留的备份。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def Deadline(self):
        r"""备份到期时间。
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._BackupName = params.get("BackupName")
        self._IsPermanent = params.get("IsPermanent")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupAttributeResponse(AbstractModel):
    r"""ModifyBackupAttribute返回参数结构体

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


class ModifyBackupVaultAttributeRequest(AbstractModel):
    r"""ModifyBackupVaultAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VaultId: 备份库ID
        :type VaultId: str
        :param _VaultName: 备份库名称
        :type VaultName: str
        :param _Description: 备份库描述
        :type Description: str
        """
        self._VaultId = None
        self._VaultName = None
        self._Description = None

    @property
    def VaultId(self):
        r"""备份库ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def VaultName(self):
        r"""备份库名称
        :rtype: str
        """
        return self._VaultName

    @VaultName.setter
    def VaultName(self, VaultName):
        self._VaultName = VaultName

    @property
    def Description(self):
        r"""备份库描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VaultId = params.get("VaultId")
        self._VaultName = params.get("VaultName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupVaultAttributeResponse(AbstractModel):
    r"""ModifyBackupVaultAttribute返回参数结构体

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


class ModifyCopyPairAttributeRequest(AbstractModel):
    r"""ModifyCopyPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairId: 要修改属性的复制对id
        :type CopyPairId: str
        :param _CopyPairType: 要修改的复制对类型，可选值：DISK、INSTANCE、CFS，默认 INSTANCE
        :type CopyPairType: str
        :param _CopyPairName: 修改复制对名称（长度最大支持 64 个字符）
        :type CopyPairName: str
        """
        self._CopyPairId = None
        self._CopyPairType = None
        self._CopyPairName = None

    @property
    def CopyPairId(self):
        r"""要修改属性的复制对id
        :rtype: str
        """
        return self._CopyPairId

    @CopyPairId.setter
    def CopyPairId(self, CopyPairId):
        self._CopyPairId = CopyPairId

    @property
    def CopyPairType(self):
        r"""要修改的复制对类型，可选值：DISK、INSTANCE、CFS，默认 INSTANCE
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType

    @property
    def CopyPairName(self):
        r"""修改复制对名称（长度最大支持 64 个字符）
        :rtype: str
        """
        return self._CopyPairName

    @CopyPairName.setter
    def CopyPairName(self, CopyPairName):
        self._CopyPairName = CopyPairName


    def _deserialize(self, params):
        self._CopyPairId = params.get("CopyPairId")
        self._CopyPairType = params.get("CopyPairType")
        self._CopyPairName = params.get("CopyPairName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCopyPairAttributeResponse(AbstractModel):
    r"""ModifyCopyPairAttribute返回参数结构体

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


class ModifyDrillGroupAttributeRequest(AbstractModel):
    r"""ModifyDrillGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillGroupId: 要修改属性的容灾演练组id。
        :type DrillGroupId: str
        :param _DrillGroupName: 修改容灾演练组名称（长度最大支持 64 个字符）
        :type DrillGroupName: str
        """
        self._DrillGroupId = None
        self._DrillGroupName = None

    @property
    def DrillGroupId(self):
        r"""要修改属性的容灾演练组id。
        :rtype: str
        """
        return self._DrillGroupId

    @DrillGroupId.setter
    def DrillGroupId(self, DrillGroupId):
        self._DrillGroupId = DrillGroupId

    @property
    def DrillGroupName(self):
        r"""修改容灾演练组名称（长度最大支持 64 个字符）
        :rtype: str
        """
        return self._DrillGroupName

    @DrillGroupName.setter
    def DrillGroupName(self, DrillGroupName):
        self._DrillGroupName = DrillGroupName


    def _deserialize(self, params):
        self._DrillGroupId = params.get("DrillGroupId")
        self._DrillGroupName = params.get("DrillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDrillGroupAttributeResponse(AbstractModel):
    r"""ModifyDrillGroupAttribute返回参数结构体

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


class ModifyDrillPairAttributeRequest(AbstractModel):
    r"""ModifyDrillPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrillPairId: 要修改属性的容灾演练对id
        :type DrillPairId: str
        :param _DrillPairName: 修改容灾演练对名称（长度最大支持 64 个字符）
        :type DrillPairName: str
        """
        self._DrillPairId = None
        self._DrillPairName = None

    @property
    def DrillPairId(self):
        r"""要修改属性的容灾演练对id
        :rtype: str
        """
        return self._DrillPairId

    @DrillPairId.setter
    def DrillPairId(self, DrillPairId):
        self._DrillPairId = DrillPairId

    @property
    def DrillPairName(self):
        r"""修改容灾演练对名称（长度最大支持 64 个字符）
        :rtype: str
        """
        return self._DrillPairName

    @DrillPairName.setter
    def DrillPairName(self, DrillPairName):
        self._DrillPairName = DrillPairName


    def _deserialize(self, params):
        self._DrillPairId = params.get("DrillPairId")
        self._DrillPairName = params.get("DrillPairName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDrillPairAttributeResponse(AbstractModel):
    r"""ModifyDrillPairAttribute返回参数结构体

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


class ModifyFileBackupAttributeRequest(AbstractModel):
    r"""ModifyFileBackupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份ID
        :type BackupId: str
        :param _BackupName: 备份的名称。
        :type BackupName: str
        :param _IsPermanent: 是否为永久保留的备份。
        :type IsPermanent: bool
        :param _Deadline: 备份到期时间。
        :type Deadline: str
        """
        self._BackupId = None
        self._BackupName = None
        self._IsPermanent = None
        self._Deadline = None

    @property
    def BackupId(self):
        r"""备份ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        r"""备份的名称。
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def IsPermanent(self):
        r"""是否为永久保留的备份。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def Deadline(self):
        r"""备份到期时间。
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._BackupName = params.get("BackupName")
        self._IsPermanent = params.get("IsPermanent")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileBackupAttributeResponse(AbstractModel):
    r"""ModifyFileBackupAttribute返回参数结构体

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


class ModifyFileBackupPlanRequest(AbstractModel):
    r"""ModifyFileBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 备份计划ID
        :type PlanId: str
        :param _PolicyId: 备份策略ID
        :type PolicyId: str
        :param _PlanName: 计划名称
        :type PlanName: str
        :param _BackupPaths: 备份路径列表，1~20 个
        :type BackupPaths: list of str
        :param _IncludeFileTypes: 包含文件类型，0~20 个
        :type IncludeFileTypes: list of str
        :param _ExcludePatterns: 排除文件路径列表，0~20 个
        :type ExcludePatterns: list of str
        :param _ExcludeSystemDirectories: 是否排除系统目录
        :type ExcludeSystemDirectories: bool
        :param _BackupStorageId: 备份库ID
        :type BackupStorageId: str
        :param _Status: 计划状态，可选值：normal（正常）、paused（暂停）
        :type Status: str
        """
        self._PlanId = None
        self._PolicyId = None
        self._PlanName = None
        self._BackupPaths = None
        self._IncludeFileTypes = None
        self._ExcludePatterns = None
        self._ExcludeSystemDirectories = None
        self._BackupStorageId = None
        self._Status = None

    @property
    def PlanId(self):
        r"""备份计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PolicyId(self):
        warnings.warn("parameter `PolicyId` is deprecated", DeprecationWarning) 

        r"""备份策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        warnings.warn("parameter `PolicyId` is deprecated", DeprecationWarning) 

        self._PolicyId = PolicyId

    @property
    def PlanName(self):
        r"""计划名称
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def BackupPaths(self):
        r"""备份路径列表，1~20 个
        :rtype: list of str
        """
        return self._BackupPaths

    @BackupPaths.setter
    def BackupPaths(self, BackupPaths):
        self._BackupPaths = BackupPaths

    @property
    def IncludeFileTypes(self):
        r"""包含文件类型，0~20 个
        :rtype: list of str
        """
        return self._IncludeFileTypes

    @IncludeFileTypes.setter
    def IncludeFileTypes(self, IncludeFileTypes):
        self._IncludeFileTypes = IncludeFileTypes

    @property
    def ExcludePatterns(self):
        r"""排除文件路径列表，0~20 个
        :rtype: list of str
        """
        return self._ExcludePatterns

    @ExcludePatterns.setter
    def ExcludePatterns(self, ExcludePatterns):
        self._ExcludePatterns = ExcludePatterns

    @property
    def ExcludeSystemDirectories(self):
        r"""是否排除系统目录
        :rtype: bool
        """
        return self._ExcludeSystemDirectories

    @ExcludeSystemDirectories.setter
    def ExcludeSystemDirectories(self, ExcludeSystemDirectories):
        self._ExcludeSystemDirectories = ExcludeSystemDirectories

    @property
    def BackupStorageId(self):
        warnings.warn("parameter `BackupStorageId` is deprecated", DeprecationWarning) 

        r"""备份库ID
        :rtype: str
        """
        return self._BackupStorageId

    @BackupStorageId.setter
    def BackupStorageId(self, BackupStorageId):
        warnings.warn("parameter `BackupStorageId` is deprecated", DeprecationWarning) 

        self._BackupStorageId = BackupStorageId

    @property
    def Status(self):
        r"""计划状态，可选值：normal（正常）、paused（暂停）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PolicyId = params.get("PolicyId")
        self._PlanName = params.get("PlanName")
        self._BackupPaths = params.get("BackupPaths")
        self._IncludeFileTypes = params.get("IncludeFileTypes")
        self._ExcludePatterns = params.get("ExcludePatterns")
        self._ExcludeSystemDirectories = params.get("ExcludeSystemDirectories")
        self._BackupStorageId = params.get("BackupStorageId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileBackupPlanResponse(AbstractModel):
    r"""ModifyFileBackupPlan返回参数结构体

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


class ModifyProtectGroupAttributeRequest(AbstractModel):
    r"""ModifyProtectGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectGroupId: 要修改属性的保护组id
        :type ProtectGroupId: str
        :param _ProtectGroupName: 保护组名称
        :type ProtectGroupName: str
        """
        self._ProtectGroupId = None
        self._ProtectGroupName = None

    @property
    def ProtectGroupId(self):
        r"""要修改属性的保护组id
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def ProtectGroupName(self):
        r"""保护组名称
        :rtype: str
        """
        return self._ProtectGroupName

    @ProtectGroupName.setter
    def ProtectGroupName(self, ProtectGroupName):
        self._ProtectGroupName = ProtectGroupName


    def _deserialize(self, params):
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._ProtectGroupName = params.get("ProtectGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProtectGroupAttributeResponse(AbstractModel):
    r"""ModifyProtectGroupAttribute返回参数结构体

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


class ModifySitePairAttributeRequest(AbstractModel):
    r"""ModifySitePairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SitePairId: 要修改属性的容灾站点id
        :type SitePairId: str
        :param _SitePairName: 容灾站点名称
        :type SitePairName: str
        """
        self._SitePairId = None
        self._SitePairName = None

    @property
    def SitePairId(self):
        r"""要修改属性的容灾站点id
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SitePairName(self):
        r"""容灾站点名称
        :rtype: str
        """
        return self._SitePairName

    @SitePairName.setter
    def SitePairName(self, SitePairName):
        self._SitePairName = SitePairName


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        self._SitePairName = params.get("SitePairName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySitePairAttributeResponse(AbstractModel):
    r"""ModifySitePairAttribute返回参数结构体

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


class Placement(AbstractModel):
    r"""描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机等（仅CDH产品可用）

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区 ID。该参数也可以通过调用 [DescribeZones]的返回值中的Zone字段来获取。
        :type Zone: str
        :param _ProjectId: 实例所属项目ID。
        :type ProjectId: int
        :param _HostId: 实例所属的专用宿主机ID列表。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。仅用于出参，当前暂不支持。
        :type HostId: str
        :param _HostIds: 实例所属的专用宿主机ID列表，仅用于入参。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :type HostIds: list of str
        :param _ProjectName: 实例所属项目名。
        :type ProjectName: str
        """
        self._Zone = None
        self._ProjectId = None
        self._HostId = None
        self._HostIds = None
        self._ProjectName = None

    @property
    def Zone(self):
        r"""实例所属的可用区 ID。该参数也可以通过调用 [DescribeZones]的返回值中的Zone字段来获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        r"""实例所属项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def HostId(self):
        r"""实例所属的专用宿主机ID列表。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。仅用于出参，当前暂不支持。
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def HostIds(self):
        r"""实例所属的专用宿主机ID列表，仅用于入参。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :rtype: list of str
        """
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def ProjectName(self):
        r"""实例所属项目名。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._HostId = params.get("HostId")
        self._HostIds = params.get("HostIds")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    r"""备份计划详情

    """

    def __init__(self):
        r"""
        :param _PlanId: 备份计划ID
        :type PlanId: str
        :param _ResourceIds: 计划关联的实例ID
        :type ResourceIds: list of str
        :param _PlanName: 计划名称
        :type PlanName: str
        :param _BackupPaths: 备份路径列表，1~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupPaths: list of str
        :param _IncludeFileTypes: 包含文件类型，0~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeFileTypes: list of str
        :param _ExcludePatterns: 排除文件路径列表，0~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePatterns: list of str
        :param _ExcludeSystemDirectories: 是否排除系统目录
        :type ExcludeSystemDirectories: bool
        :param _VaultId: 备份库ID
        :type VaultId: str
        :param _Status: 备份计划状态
        :type Status: str
        :param _AspId: 策略ID
        :type AspId: str
        :param _AspName: 策略名称
        :type AspName: str
        :param _AspPolicy: 策略详情
        :type AspPolicy: :class:`tencentcloud.bdrc.v20260330.models.AspInfo`
        :param _LastExecuteTime: 最近一次执行时间
        :type LastExecuteTime: str
        :param _NextTriggerTime: 下次触发时间
        :type NextTriggerTime: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _LastTriggerError: 最近一次执行错误信息
        :type LastTriggerError: str
        :param _BackupCount: 备份数量
        :type BackupCount: int
        :param _FlowControlSettings: 流控信息
        :type FlowControlSettings: list of FlowControlRule
        """
        self._PlanId = None
        self._ResourceIds = None
        self._PlanName = None
        self._BackupPaths = None
        self._IncludeFileTypes = None
        self._ExcludePatterns = None
        self._ExcludeSystemDirectories = None
        self._VaultId = None
        self._Status = None
        self._AspId = None
        self._AspName = None
        self._AspPolicy = None
        self._LastExecuteTime = None
        self._NextTriggerTime = None
        self._CreatedTime = None
        self._LastTriggerError = None
        self._BackupCount = None
        self._FlowControlSettings = None

    @property
    def PlanId(self):
        r"""备份计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def ResourceIds(self):
        r"""计划关联的实例ID
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def PlanName(self):
        r"""计划名称
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def BackupPaths(self):
        r"""备份路径列表，1~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._BackupPaths

    @BackupPaths.setter
    def BackupPaths(self, BackupPaths):
        self._BackupPaths = BackupPaths

    @property
    def IncludeFileTypes(self):
        r"""包含文件类型，0~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IncludeFileTypes

    @IncludeFileTypes.setter
    def IncludeFileTypes(self, IncludeFileTypes):
        self._IncludeFileTypes = IncludeFileTypes

    @property
    def ExcludePatterns(self):
        r"""排除文件路径列表，0~20 个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludePatterns

    @ExcludePatterns.setter
    def ExcludePatterns(self, ExcludePatterns):
        self._ExcludePatterns = ExcludePatterns

    @property
    def ExcludeSystemDirectories(self):
        r"""是否排除系统目录
        :rtype: bool
        """
        return self._ExcludeSystemDirectories

    @ExcludeSystemDirectories.setter
    def ExcludeSystemDirectories(self, ExcludeSystemDirectories):
        self._ExcludeSystemDirectories = ExcludeSystemDirectories

    @property
    def VaultId(self):
        r"""备份库ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def Status(self):
        r"""备份计划状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AspId(self):
        r"""策略ID
        :rtype: str
        """
        return self._AspId

    @AspId.setter
    def AspId(self, AspId):
        self._AspId = AspId

    @property
    def AspName(self):
        r"""策略名称
        :rtype: str
        """
        return self._AspName

    @AspName.setter
    def AspName(self, AspName):
        self._AspName = AspName

    @property
    def AspPolicy(self):
        r"""策略详情
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.AspInfo`
        """
        return self._AspPolicy

    @AspPolicy.setter
    def AspPolicy(self, AspPolicy):
        self._AspPolicy = AspPolicy

    @property
    def LastExecuteTime(self):
        r"""最近一次执行时间
        :rtype: str
        """
        return self._LastExecuteTime

    @LastExecuteTime.setter
    def LastExecuteTime(self, LastExecuteTime):
        self._LastExecuteTime = LastExecuteTime

    @property
    def NextTriggerTime(self):
        r"""下次触发时间
        :rtype: str
        """
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LastTriggerError(self):
        r"""最近一次执行错误信息
        :rtype: str
        """
        return self._LastTriggerError

    @LastTriggerError.setter
    def LastTriggerError(self, LastTriggerError):
        self._LastTriggerError = LastTriggerError

    @property
    def BackupCount(self):
        r"""备份数量
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def FlowControlSettings(self):
        r"""流控信息
        :rtype: list of FlowControlRule
        """
        return self._FlowControlSettings

    @FlowControlSettings.setter
    def FlowControlSettings(self, FlowControlSettings):
        self._FlowControlSettings = FlowControlSettings


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._ResourceIds = params.get("ResourceIds")
        self._PlanName = params.get("PlanName")
        self._BackupPaths = params.get("BackupPaths")
        self._IncludeFileTypes = params.get("IncludeFileTypes")
        self._ExcludePatterns = params.get("ExcludePatterns")
        self._ExcludeSystemDirectories = params.get("ExcludeSystemDirectories")
        self._VaultId = params.get("VaultId")
        self._Status = params.get("Status")
        self._AspId = params.get("AspId")
        self._AspName = params.get("AspName")
        if params.get("AspPolicy") is not None:
            self._AspPolicy = AspInfo()
            self._AspPolicy._deserialize(params.get("AspPolicy"))
        self._LastExecuteTime = params.get("LastExecuteTime")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._CreatedTime = params.get("CreatedTime")
        self._LastTriggerError = params.get("LastTriggerError")
        self._BackupCount = params.get("BackupCount")
        if params.get("FlowControlSettings") is not None:
            self._FlowControlSettings = []
            for item in params.get("FlowControlSettings"):
                obj = FlowControlRule()
                obj._deserialize(item)
                self._FlowControlSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    r"""备份的执行策略详情

    """

    def __init__(self):
        r"""
        :param _DayOfWeek: 选定周一到周日中需要创建备份的日期，取值范围：[0, 6]。0表示周日触发，1表示周一触发，依次类推。
        :type DayOfWeek: list of int non-negative
        :param _Hour: 指定定期备份策略的触发时间。单位为小时，取值范围：[0, 23]。00:00 ~ 23:00 共 24 个时间点可选，1表示 01:00，依此类推。
        :type Hour: list of int non-negative
        :param _DayOfMonth: 指定每月从月初到月底需要触发定期备份的日期,取值范围：[1, 31]，1-31分别表示每月的具体日期，比如5表示每月的5号。注：若设置29、30、31等部分月份不存在的日期，则对应不存在日期的月份会跳过不打定期备份。
        :type DayOfMonth: list of int non-negative
        :param _IntervalDays: 指定创建定期备份的间隔天数，取值范围：[1, 365]，例如设置为5，则间隔5天即触发定期备份创建。注：当选择按天备份时，理论上第一次备份的时间为备份策略创建当天。如果当天备份策略创建的时间已经晚于设置的备份时间，那么将会等到第二个备份周期再进行第一次备份。
        :type IntervalDays: int
        """
        self._DayOfWeek = None
        self._Hour = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def DayOfWeek(self):
        r"""选定周一到周日中需要创建备份的日期，取值范围：[0, 6]。0表示周日触发，1表示周一触发，依次类推。
        :rtype: list of int non-negative
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        r"""指定定期备份策略的触发时间。单位为小时，取值范围：[0, 23]。00:00 ~ 23:00 共 24 个时间点可选，1表示 01:00，依此类推。
        :rtype: list of int non-negative
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def DayOfMonth(self):
        r"""指定每月从月初到月底需要触发定期备份的日期,取值范围：[1, 31]，1-31分别表示每月的具体日期，比如5表示每月的5号。注：若设置29、30、31等部分月份不存在的日期，则对应不存在日期的月份会跳过不打定期备份。
        :rtype: list of int non-negative
        """
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        r"""指定创建定期备份的间隔天数，取值范围：[1, 365]，例如设置为5，则间隔5天即触发定期备份创建。注：当选择按天备份时，理论上第一次备份的时间为备份策略创建当天。如果当天备份策略创建的时间已经晚于设置的备份时间，那么将会等到第二个备份周期再进行第一次备份。
        :rtype: int
        """
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._DayOfWeek = params.get("DayOfWeek")
        self._Hour = params.get("Hour")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectGroup(AbstractModel):
    r"""容灾保护组信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户AppId
        :type AppId: int
        :param _ProtectGroupId: 保护组ID
        :type ProtectGroupId: str
        :param _ProtectGroupName: 保护组名称
        :type ProtectGroupName: str
        :param _ProtectGroupType: 保护组类型（产品类型，如 DISK/CFS/INSTANCE）
        :type ProtectGroupType: str
        :param _SitePairId: 所属容灾策略ID
        :type SitePairId: str
        :param _SitePairName: 所属容灾策略名称
        :type SitePairName: str
        :param _RecoveryPointObjective: RPO时间（单位秒）
        :type RecoveryPointObjective: int
        :param _SourceRegion: 生产地域（当 DataDirection=REVERSE 时会与 TargetRegion 自动轮转，保持用户视角一致）
        :type SourceRegion: str
        :param _SourceZone: 生产可用区（REVERSE 时与 TargetZone 自动轮转）
        :type SourceZone: str
        :param _SourceVpc: 生产端VPC（REVERSE 时与 TargetVpc 自动轮转）
        :type SourceVpc: str
        :param _TargetRegion: 容灾地域（REVERSE 时与 SourceRegion 自动轮转）
        :type TargetRegion: str
        :param _TargetZone: 容灾可用区
        :type TargetZone: str
        :param _TargetVpc: 容灾端VPC
        :type TargetVpc: str
        :param _CopyType: 复制技术（SYN 同步 / ASY 异步）
        :type CopyType: str
        :param _DisasterRecoveryType: 容灾类型（CROSS_ZONE 跨可用区 / CROSS_REGION 跨地域 / CROSS_CLOUD 跨云）
        :type DisasterRecoveryType: str
        :param _DataDirection: 数据复制方向（POSITIVE 正向 / REVERSE 反向）
        :type DataDirection: str
        :param _PeerCloudName: 跨云场景对端云名称（仅 DisasterRecoveryType=CROSS_CLOUD 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerCloudName: str
        :param _CreateFrom: 创建来源（LOCAL 本端创建 / PEER 对端创建）
        :type CreateFrom: str
        :param _LifeState: 生命周期状态
        :type LifeState: str
        :param _AccountUin: 创建保护组的账户主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 创建保护组的子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _BindProtectedResourceCount: 绑定的已保护资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BindProtectedResourceCount: int
        :param _ErrorRecoveryPointObjectiveCount: RPO 异常（超过 15 分钟未同步）的复制对数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorRecoveryPointObjectiveCount: int
        :param _ProtectedResourceStatusSet: 已保护资源状态统计，key 为复制对状态，value 为该状态下的资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedResourceStatusSet: list of ProtectedResourceStatus
        """
        self._AppId = None
        self._ProtectGroupId = None
        self._ProtectGroupName = None
        self._ProtectGroupType = None
        self._SitePairId = None
        self._SitePairName = None
        self._RecoveryPointObjective = None
        self._SourceRegion = None
        self._SourceZone = None
        self._SourceVpc = None
        self._TargetRegion = None
        self._TargetZone = None
        self._TargetVpc = None
        self._CopyType = None
        self._DisasterRecoveryType = None
        self._DataDirection = None
        self._PeerCloudName = None
        self._CreateFrom = None
        self._LifeState = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._CreateTime = None
        self._ModifyTime = None
        self._BindProtectedResourceCount = None
        self._ErrorRecoveryPointObjectiveCount = None
        self._ProtectedResourceStatusSet = None

    @property
    def AppId(self):
        r"""用户AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProtectGroupId(self):
        r"""保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def ProtectGroupName(self):
        r"""保护组名称
        :rtype: str
        """
        return self._ProtectGroupName

    @ProtectGroupName.setter
    def ProtectGroupName(self, ProtectGroupName):
        self._ProtectGroupName = ProtectGroupName

    @property
    def ProtectGroupType(self):
        r"""保护组类型（产品类型，如 DISK/CFS/INSTANCE）
        :rtype: str
        """
        return self._ProtectGroupType

    @ProtectGroupType.setter
    def ProtectGroupType(self, ProtectGroupType):
        self._ProtectGroupType = ProtectGroupType

    @property
    def SitePairId(self):
        r"""所属容灾策略ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SitePairName(self):
        r"""所属容灾策略名称
        :rtype: str
        """
        return self._SitePairName

    @SitePairName.setter
    def SitePairName(self, SitePairName):
        self._SitePairName = SitePairName

    @property
    def RecoveryPointObjective(self):
        r"""RPO时间（单位秒）
        :rtype: int
        """
        return self._RecoveryPointObjective

    @RecoveryPointObjective.setter
    def RecoveryPointObjective(self, RecoveryPointObjective):
        self._RecoveryPointObjective = RecoveryPointObjective

    @property
    def SourceRegion(self):
        r"""生产地域（当 DataDirection=REVERSE 时会与 TargetRegion 自动轮转，保持用户视角一致）
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""生产可用区（REVERSE 时与 TargetZone 自动轮转）
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def SourceVpc(self):
        r"""生产端VPC（REVERSE 时与 TargetVpc 自动轮转）
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def TargetRegion(self):
        r"""容灾地域（REVERSE 时与 SourceRegion 自动轮转）
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetZone(self):
        r"""容灾可用区
        :rtype: str
        """
        return self._TargetZone

    @TargetZone.setter
    def TargetZone(self, TargetZone):
        self._TargetZone = TargetZone

    @property
    def TargetVpc(self):
        r"""容灾端VPC
        :rtype: str
        """
        return self._TargetVpc

    @TargetVpc.setter
    def TargetVpc(self, TargetVpc):
        self._TargetVpc = TargetVpc

    @property
    def CopyType(self):
        r"""复制技术（SYN 同步 / ASY 异步）
        :rtype: str
        """
        return self._CopyType

    @CopyType.setter
    def CopyType(self, CopyType):
        self._CopyType = CopyType

    @property
    def DisasterRecoveryType(self):
        r"""容灾类型（CROSS_ZONE 跨可用区 / CROSS_REGION 跨地域 / CROSS_CLOUD 跨云）
        :rtype: str
        """
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def DataDirection(self):
        r"""数据复制方向（POSITIVE 正向 / REVERSE 反向）
        :rtype: str
        """
        return self._DataDirection

    @DataDirection.setter
    def DataDirection(self, DataDirection):
        self._DataDirection = DataDirection

    @property
    def PeerCloudName(self):
        r"""跨云场景对端云名称（仅 DisasterRecoveryType=CROSS_CLOUD 时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerCloudName

    @PeerCloudName.setter
    def PeerCloudName(self, PeerCloudName):
        self._PeerCloudName = PeerCloudName

    @property
    def CreateFrom(self):
        r"""创建来源（LOCAL 本端创建 / PEER 对端创建）
        :rtype: str
        """
        return self._CreateFrom

    @CreateFrom.setter
    def CreateFrom(self, CreateFrom):
        self._CreateFrom = CreateFrom

    @property
    def LifeState(self):
        r"""生命周期状态
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def AccountUin(self):
        r"""创建保护组的账户主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""创建保护组的子账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

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
    def ModifyTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def BindProtectedResourceCount(self):
        r"""绑定的已保护资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BindProtectedResourceCount

    @BindProtectedResourceCount.setter
    def BindProtectedResourceCount(self, BindProtectedResourceCount):
        self._BindProtectedResourceCount = BindProtectedResourceCount

    @property
    def ErrorRecoveryPointObjectiveCount(self):
        r"""RPO 异常（超过 15 分钟未同步）的复制对数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrorRecoveryPointObjectiveCount

    @ErrorRecoveryPointObjectiveCount.setter
    def ErrorRecoveryPointObjectiveCount(self, ErrorRecoveryPointObjectiveCount):
        self._ErrorRecoveryPointObjectiveCount = ErrorRecoveryPointObjectiveCount

    @property
    def ProtectedResourceStatusSet(self):
        r"""已保护资源状态统计，key 为复制对状态，value 为该状态下的资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProtectedResourceStatus
        """
        return self._ProtectedResourceStatusSet

    @ProtectedResourceStatusSet.setter
    def ProtectedResourceStatusSet(self, ProtectedResourceStatusSet):
        self._ProtectedResourceStatusSet = ProtectedResourceStatusSet


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ProtectGroupId = params.get("ProtectGroupId")
        self._ProtectGroupName = params.get("ProtectGroupName")
        self._ProtectGroupType = params.get("ProtectGroupType")
        self._SitePairId = params.get("SitePairId")
        self._SitePairName = params.get("SitePairName")
        self._RecoveryPointObjective = params.get("RecoveryPointObjective")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._SourceVpc = params.get("SourceVpc")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetZone = params.get("TargetZone")
        self._TargetVpc = params.get("TargetVpc")
        self._CopyType = params.get("CopyType")
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._DataDirection = params.get("DataDirection")
        self._PeerCloudName = params.get("PeerCloudName")
        self._CreateFrom = params.get("CreateFrom")
        self._LifeState = params.get("LifeState")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._BindProtectedResourceCount = params.get("BindProtectedResourceCount")
        self._ErrorRecoveryPointObjectiveCount = params.get("ErrorRecoveryPointObjectiveCount")
        if params.get("ProtectedResourceStatusSet") is not None:
            self._ProtectedResourceStatusSet = []
            for item in params.get("ProtectedResourceStatusSet"):
                obj = ProtectedResourceStatus()
                obj._deserialize(item)
                self._ProtectedResourceStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectGroupDeniedAction(AbstractModel):
    r"""保护组操作掩码

    """

    def __init__(self):
        r"""
        :param _ProtectGroupId: 保护组ID
        :type ProtectGroupId: str
        :param _DeniedActions: 被禁止的操作列表（Action名称数组）
        :type DeniedActions: list of DeniedAction
        """
        self._ProtectGroupId = None
        self._DeniedActions = None

    @property
    def ProtectGroupId(self):
        r"""保护组ID
        :rtype: str
        """
        return self._ProtectGroupId

    @ProtectGroupId.setter
    def ProtectGroupId(self, ProtectGroupId):
        self._ProtectGroupId = ProtectGroupId

    @property
    def DeniedActions(self):
        r"""被禁止的操作列表（Action名称数组）
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._ProtectGroupId = params.get("ProtectGroupId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectInstance(AbstractModel):
    r"""受保护实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AgentId: 客户端ID
        :type AgentId: str
        :param _AgentVersion: 客户端版本
        :type AgentVersion: str
        :param _AgentStatus: 客户端状态
        :type AgentStatus: str
        :param _LastHeartbeatTime: 最后心跳时间
        :type LastHeartbeatTime: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ExtraInfo: 最新备份点中记录的 CVM 基础信息
        :type ExtraInfo: str
        :param _BackupCount: 该实例可用备份点数量
        :type BackupCount: int
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _LatestBackupTime: 最近一次备份时间
        :type LatestBackupTime: str
        :param _OfflineReason: 离线原因
        :type OfflineReason: str
        """
        self._InstanceId = None
        self._AgentId = None
        self._AgentVersion = None
        self._AgentStatus = None
        self._LastHeartbeatTime = None
        self._CreatedTime = None
        self._ExtraInfo = None
        self._BackupCount = None
        self._InstanceName = None
        self._LatestBackupTime = None
        self._OfflineReason = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        r"""客户端ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentVersion(self):
        r"""客户端版本
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def AgentStatus(self):
        r"""客户端状态
        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def LastHeartbeatTime(self):
        r"""最后心跳时间
        :rtype: str
        """
        return self._LastHeartbeatTime

    @LastHeartbeatTime.setter
    def LastHeartbeatTime(self, LastHeartbeatTime):
        self._LastHeartbeatTime = LastHeartbeatTime

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExtraInfo(self):
        r"""最新备份点中记录的 CVM 基础信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def BackupCount(self):
        r"""该实例可用备份点数量
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

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
    def LatestBackupTime(self):
        r"""最近一次备份时间
        :rtype: str
        """
        return self._LatestBackupTime

    @LatestBackupTime.setter
    def LatestBackupTime(self, LatestBackupTime):
        self._LatestBackupTime = LatestBackupTime

    @property
    def OfflineReason(self):
        r"""离线原因
        :rtype: str
        """
        return self._OfflineReason

    @OfflineReason.setter
    def OfflineReason(self, OfflineReason):
        self._OfflineReason = OfflineReason


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._AgentVersion = params.get("AgentVersion")
        self._AgentStatus = params.get("AgentStatus")
        self._LastHeartbeatTime = params.get("LastHeartbeatTime")
        self._CreatedTime = params.get("CreatedTime")
        self._ExtraInfo = params.get("ExtraInfo")
        self._BackupCount = params.get("BackupCount")
        self._InstanceName = params.get("InstanceName")
        self._LatestBackupTime = params.get("LatestBackupTime")
        self._OfflineReason = params.get("OfflineReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectedResource(AbstractModel):
    r"""受保护资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型（与请求 SitePairType 一致，如 DISK/CFS/INSTANCE）
        :type ResourceType: str
        :param _ResourceIdSet: 该类型下被保护的源端资源ID列表（DISK:disk-xxx / CFS:cfs-xxx / INSTANCE:ins-xxx）
        :type ResourceIdSet: list of str
        """
        self._ResourceType = None
        self._ResourceIdSet = None

    @property
    def ResourceType(self):
        r"""资源类型（与请求 SitePairType 一致，如 DISK/CFS/INSTANCE）
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceIdSet(self):
        r"""该类型下被保护的源端资源ID列表（DISK:disk-xxx / CFS:cfs-xxx / INSTANCE:ins-xxx）
        :rtype: list of str
        """
        return self._ResourceIdSet

    @ResourceIdSet.setter
    def ResourceIdSet(self, ResourceIdSet):
        self._ResourceIdSet = ResourceIdSet


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceIdSet = params.get("ResourceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectedResourceOverview(AbstractModel):
    r"""受保护资源概览

    """

    def __init__(self):
        r"""
        :param _TotalProtectedCount: 受保护资源总数
        :type TotalProtectedCount: int
        :param _TotalResourceCount: 总资源数
        :type TotalResourceCount: int
        :param _Cvm: CVM 受保护统计
        :type Cvm: :class:`tencentcloud.bdrc.v20260330.models.ResourceProtectStat`
        :param _CFS: CFS 受保护统计
        :type CFS: :class:`tencentcloud.bdrc.v20260330.models.ResourceProtectStat`
        """
        self._TotalProtectedCount = None
        self._TotalResourceCount = None
        self._Cvm = None
        self._CFS = None

    @property
    def TotalProtectedCount(self):
        r"""受保护资源总数
        :rtype: int
        """
        return self._TotalProtectedCount

    @TotalProtectedCount.setter
    def TotalProtectedCount(self, TotalProtectedCount):
        self._TotalProtectedCount = TotalProtectedCount

    @property
    def TotalResourceCount(self):
        r"""总资源数
        :rtype: int
        """
        return self._TotalResourceCount

    @TotalResourceCount.setter
    def TotalResourceCount(self, TotalResourceCount):
        self._TotalResourceCount = TotalResourceCount

    @property
    def Cvm(self):
        r"""CVM 受保护统计
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ResourceProtectStat`
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def CFS(self):
        r"""CFS 受保护统计
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ResourceProtectStat`
        """
        return self._CFS

    @CFS.setter
    def CFS(self, CFS):
        self._CFS = CFS


    def _deserialize(self, params):
        self._TotalProtectedCount = params.get("TotalProtectedCount")
        self._TotalResourceCount = params.get("TotalResourceCount")
        if params.get("Cvm") is not None:
            self._Cvm = ResourceProtectStat()
            self._Cvm._deserialize(params.get("Cvm"))
        if params.get("CFS") is not None:
            self._CFS = ResourceProtectStat()
            self._CFS._deserialize(params.get("CFS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectedResourceStatus(AbstractModel):
    r"""保护资源类型个数统计

    """

    def __init__(self):
        r"""
        :param _Status: 状态
        :type Status: str
        :param _Count: 数量
        :type Count: int
        """
        self._Status = None
        self._Count = None

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        r"""数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAgentMetricsRequest(AbstractModel):
    r"""ReportAgentMetrics请求参数结构体

    """


class ReportAgentMetricsResponse(AbstractModel):
    r"""ReportAgentMetrics返回参数结构体

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


class ReportGatewayHeartbeatRequest(AbstractModel):
    r"""ReportGatewayHeartbeat请求参数结构体

    """


class ReportGatewayHeartbeatResponse(AbstractModel):
    r"""ReportGatewayHeartbeat返回参数结构体

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


class ReportJobProgressRequest(AbstractModel):
    r"""ReportJobProgress请求参数结构体

    """


class ReportJobProgressResponse(AbstractModel):
    r"""ReportJobProgress返回参数结构体

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


class ResourcePlan(AbstractModel):
    r"""实例Id与备份计划映射信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 云服务器实例 ID
        :type ResourceId: str
        :param _BackupPaths: 备份路径，[0,20]
        :type BackupPaths: list of str
        :param _IncludeFileTypes: 包含文件类型，[0,20]
        :type IncludeFileTypes: list of str
        :param _ExcludePatterns: 排除路径，[0,20]
        :type ExcludePatterns: list of str
        :param _ExcludeSystemDirectories: 是否排除系统目录
        :type ExcludeSystemDirectories: bool
        :param _ExecuteImmediately: 是否立即触发全量备份
        :type ExecuteImmediately: bool
        """
        self._ResourceId = None
        self._BackupPaths = None
        self._IncludeFileTypes = None
        self._ExcludePatterns = None
        self._ExcludeSystemDirectories = None
        self._ExecuteImmediately = None

    @property
    def ResourceId(self):
        r"""云服务器实例 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def BackupPaths(self):
        r"""备份路径，[0,20]
        :rtype: list of str
        """
        return self._BackupPaths

    @BackupPaths.setter
    def BackupPaths(self, BackupPaths):
        self._BackupPaths = BackupPaths

    @property
    def IncludeFileTypes(self):
        r"""包含文件类型，[0,20]
        :rtype: list of str
        """
        return self._IncludeFileTypes

    @IncludeFileTypes.setter
    def IncludeFileTypes(self, IncludeFileTypes):
        self._IncludeFileTypes = IncludeFileTypes

    @property
    def ExcludePatterns(self):
        r"""排除路径，[0,20]
        :rtype: list of str
        """
        return self._ExcludePatterns

    @ExcludePatterns.setter
    def ExcludePatterns(self, ExcludePatterns):
        self._ExcludePatterns = ExcludePatterns

    @property
    def ExcludeSystemDirectories(self):
        r"""是否排除系统目录
        :rtype: bool
        """
        return self._ExcludeSystemDirectories

    @ExcludeSystemDirectories.setter
    def ExcludeSystemDirectories(self, ExcludeSystemDirectories):
        self._ExcludeSystemDirectories = ExcludeSystemDirectories

    @property
    def ExecuteImmediately(self):
        r"""是否立即触发全量备份
        :rtype: bool
        """
        return self._ExecuteImmediately

    @ExecuteImmediately.setter
    def ExecuteImmediately(self, ExecuteImmediately):
        self._ExecuteImmediately = ExecuteImmediately


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._BackupPaths = params.get("BackupPaths")
        self._IncludeFileTypes = params.get("IncludeFileTypes")
        self._ExcludePatterns = params.get("ExcludePatterns")
        self._ExcludeSystemDirectories = params.get("ExcludeSystemDirectories")
        self._ExecuteImmediately = params.get("ExecuteImmediately")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceProtectStat(AbstractModel):
    r"""产品受保护统计信息

    """

    def __init__(self):
        r"""
        :param _ProtectedCount: 受保护资源数
        :type ProtectedCount: int
        :param _TotalCount: 资源总数
        :type TotalCount: int
        """
        self._ProtectedCount = None
        self._TotalCount = None

    @property
    def ProtectedCount(self):
        r"""受保护资源数
        :rtype: int
        """
        return self._ProtectedCount

    @ProtectedCount.setter
    def ProtectedCount(self, ProtectedCount):
        self._ProtectedCount = ProtectedCount

    @property
    def TotalCount(self):
        r"""资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ProtectedCount = params.get("ProtectedCount")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    r"""恢复任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 恢复任务 ID
        :type TaskId: str
        :param _BackupId: 关联备份点 ID
        :type BackupId: str
        :param _ResourceId: 源实例 ID
        :type ResourceId: str
        :param _TargetResourceId: 目标实例 ID
        :type TargetResourceId: str
        :param _RestorePaths: 恢复路径列表
        :type RestorePaths: list of str
        :param _TargetLocation: 目标恢复位置
        :type TargetLocation: str
        :param _Status: 任务状态
        :type Status: str
        :param _TotalFileCount: 需恢复文件总数
        :type TotalFileCount: int
        :param _TotalSize: 需恢复数据总量（字节）
        :type TotalSize: int
        :param _TotalSizeFormatted: 需恢复数据总量（格式化，如 "1.5 GB"）
        :type TotalSizeFormatted: str
        :param _RestoreFileCount: 已恢复文件数
        :type RestoreFileCount: int
        :param _RestoreSize: 已恢复数据量（字节）
        :type RestoreSize: int
        :param _RestoreSizeFormatted: 已恢复数据量（格式化）
        :type RestoreSizeFormatted: str
        :param _Progress: 恢复进度（0-100）
        :type Progress: float
        :param _JobId: 关联 Job ID
        :type JobId: str
        :param _StartTime: 任务开始时间（ISO 格式）
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _CreatedTime: 任务创建时间
        :type CreatedTime: str
        :param _FailReason: 恢复任务失败原因
        :type FailReason: str
        :param _ConflictStrategy: 冲突处理策略：skip-跳过/overwrite-覆盖/newer-保留最新版本/if_changed-内容变化时覆盖
        :type ConflictStrategy: str
        """
        self._TaskId = None
        self._BackupId = None
        self._ResourceId = None
        self._TargetResourceId = None
        self._RestorePaths = None
        self._TargetLocation = None
        self._Status = None
        self._TotalFileCount = None
        self._TotalSize = None
        self._TotalSizeFormatted = None
        self._RestoreFileCount = None
        self._RestoreSize = None
        self._RestoreSizeFormatted = None
        self._Progress = None
        self._JobId = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._FailReason = None
        self._ConflictStrategy = None

    @property
    def TaskId(self):
        r"""恢复任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BackupId(self):
        r"""关联备份点 ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def ResourceId(self):
        r"""源实例 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TargetResourceId(self):
        r"""目标实例 ID
        :rtype: str
        """
        return self._TargetResourceId

    @TargetResourceId.setter
    def TargetResourceId(self, TargetResourceId):
        self._TargetResourceId = TargetResourceId

    @property
    def RestorePaths(self):
        r"""恢复路径列表
        :rtype: list of str
        """
        return self._RestorePaths

    @RestorePaths.setter
    def RestorePaths(self, RestorePaths):
        self._RestorePaths = RestorePaths

    @property
    def TargetLocation(self):
        r"""目标恢复位置
        :rtype: str
        """
        return self._TargetLocation

    @TargetLocation.setter
    def TargetLocation(self, TargetLocation):
        self._TargetLocation = TargetLocation

    @property
    def Status(self):
        r"""任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalFileCount(self):
        r"""需恢复文件总数
        :rtype: int
        """
        return self._TotalFileCount

    @TotalFileCount.setter
    def TotalFileCount(self, TotalFileCount):
        self._TotalFileCount = TotalFileCount

    @property
    def TotalSize(self):
        r"""需恢复数据总量（字节）
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def TotalSizeFormatted(self):
        r"""需恢复数据总量（格式化，如 "1.5 GB"）
        :rtype: str
        """
        return self._TotalSizeFormatted

    @TotalSizeFormatted.setter
    def TotalSizeFormatted(self, TotalSizeFormatted):
        self._TotalSizeFormatted = TotalSizeFormatted

    @property
    def RestoreFileCount(self):
        r"""已恢复文件数
        :rtype: int
        """
        return self._RestoreFileCount

    @RestoreFileCount.setter
    def RestoreFileCount(self, RestoreFileCount):
        self._RestoreFileCount = RestoreFileCount

    @property
    def RestoreSize(self):
        r"""已恢复数据量（字节）
        :rtype: int
        """
        return self._RestoreSize

    @RestoreSize.setter
    def RestoreSize(self, RestoreSize):
        self._RestoreSize = RestoreSize

    @property
    def RestoreSizeFormatted(self):
        r"""已恢复数据量（格式化）
        :rtype: str
        """
        return self._RestoreSizeFormatted

    @RestoreSizeFormatted.setter
    def RestoreSizeFormatted(self, RestoreSizeFormatted):
        self._RestoreSizeFormatted = RestoreSizeFormatted

    @property
    def Progress(self):
        r"""恢复进度（0-100）
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def JobId(self):
        r"""关联 Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StartTime(self):
        r"""任务开始时间（ISO 格式）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def FailReason(self):
        r"""恢复任务失败原因
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def ConflictStrategy(self):
        r"""冲突处理策略：skip-跳过/overwrite-覆盖/newer-保留最新版本/if_changed-内容变化时覆盖
        :rtype: str
        """
        return self._ConflictStrategy

    @ConflictStrategy.setter
    def ConflictStrategy(self, ConflictStrategy):
        self._ConflictStrategy = ConflictStrategy


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BackupId = params.get("BackupId")
        self._ResourceId = params.get("ResourceId")
        self._TargetResourceId = params.get("TargetResourceId")
        self._RestorePaths = params.get("RestorePaths")
        self._TargetLocation = params.get("TargetLocation")
        self._Status = params.get("Status")
        self._TotalFileCount = params.get("TotalFileCount")
        self._TotalSize = params.get("TotalSize")
        self._TotalSizeFormatted = params.get("TotalSizeFormatted")
        self._RestoreFileCount = params.get("RestoreFileCount")
        self._RestoreSize = params.get("RestoreSize")
        self._RestoreSizeFormatted = params.get("RestoreSizeFormatted")
        self._Progress = params.get("Progress")
        self._JobId = params.get("JobId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._FailReason = params.get("FailReason")
        self._ConflictStrategy = params.get("ConflictStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCopyPairTasksRequest(AbstractModel):
    r"""RunCopyPairTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 复制对ID列表
        :type CopyPairIds: list of str
        :param _CopyPairType: 要启动复制对的类型（DISK/INSTANCE/CFS）
        :type CopyPairType: str
        """
        self._CopyPairIds = None
        self._CopyPairType = None

    @property
    def CopyPairIds(self):
        r"""复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""要启动复制对的类型（DISK/INSTANCE/CFS）
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCopyPairTasksResponse(AbstractModel):
    r"""RunCopyPairTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 已启动复制任务的复制对ID列表
        :type CopyPairIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CopyPairIds = None
        self._RequestId = None

    @property
    def CopyPairIds(self):
        r"""已启动复制任务的复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

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
        self._CopyPairIds = params.get("CopyPairIds")
        self._RequestId = params.get("RequestId")


class RunFailoverCopyPairsRequest(AbstractModel):
    r"""RunFailoverCopyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 复制对ID列表
        :type CopyPairIds: list of str
        :param _CopyPairType: 复制对类型，枚举值：DISK / INSTANCE / CFS。
        :type CopyPairType: str
        :param _FailoverType: 切换类型，支持WAIT和NOW
        :type FailoverType: str
        """
        self._CopyPairIds = None
        self._CopyPairType = None
        self._FailoverType = None

    @property
    def CopyPairIds(self):
        r"""复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""复制对类型，枚举值：DISK / INSTANCE / CFS。
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType

    @property
    def FailoverType(self):
        r"""切换类型，支持WAIT和NOW
        :rtype: str
        """
        return self._FailoverType

    @FailoverType.setter
    def FailoverType(self, FailoverType):
        self._FailoverType = FailoverType


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        self._FailoverType = params.get("FailoverType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunFailoverCopyPairsResponse(AbstractModel):
    r"""RunFailoverCopyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 故障切换任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""故障切换任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RunInstancesWithBackupGroupRequest(AbstractModel):
    r"""RunInstancesWithBackupGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupGroupId: 备份组ID
        :type BackupGroupId: str
        """
        self._BackupGroupId = None

    @property
    def BackupGroupId(self):
        r"""备份组ID
        :rtype: str
        """
        return self._BackupGroupId

    @BackupGroupId.setter
    def BackupGroupId(self, BackupGroupId):
        self._BackupGroupId = BackupGroupId


    def _deserialize(self, params):
        self._BackupGroupId = params.get("BackupGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesWithBackupGroupResponse(AbstractModel):
    r"""RunInstancesWithBackupGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 创建的实例ID
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""创建的实例ID
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


class RunSecurityServiceEnabled(AbstractModel):
    r"""描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启该服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""是否开启该服务。取值范围：TRUE（开启）/FALSE（不开启）。默认取值：TRUE。
        :rtype: bool
        """
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
        


class SecurityGroupMapping(AbstractModel):
    r"""安全组映射详情

    """

    def __init__(self):
        r"""
        :param _SecurityGroupMappingId: 安全组映射ID
        :type SecurityGroupMappingId: str
        :param _SitePairId: 安全组映射所属的站点对ID
        :type SitePairId: str
        :param _SourceSecurityGroupId: 生产端安全组ID
        :type SourceSecurityGroupId: str
        :param _TargetSecurityGroupId: 容灾端安全组ID
        :type TargetSecurityGroupId: str
        :param _LifeState: 安全组映射的生命状态；NORMAL:正常。
        :type LifeState: str
        """
        self._SecurityGroupMappingId = None
        self._SitePairId = None
        self._SourceSecurityGroupId = None
        self._TargetSecurityGroupId = None
        self._LifeState = None

    @property
    def SecurityGroupMappingId(self):
        r"""安全组映射ID
        :rtype: str
        """
        return self._SecurityGroupMappingId

    @SecurityGroupMappingId.setter
    def SecurityGroupMappingId(self, SecurityGroupMappingId):
        self._SecurityGroupMappingId = SecurityGroupMappingId

    @property
    def SitePairId(self):
        r"""安全组映射所属的站点对ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SourceSecurityGroupId(self):
        r"""生产端安全组ID
        :rtype: str
        """
        return self._SourceSecurityGroupId

    @SourceSecurityGroupId.setter
    def SourceSecurityGroupId(self, SourceSecurityGroupId):
        self._SourceSecurityGroupId = SourceSecurityGroupId

    @property
    def TargetSecurityGroupId(self):
        r"""容灾端安全组ID
        :rtype: str
        """
        return self._TargetSecurityGroupId

    @TargetSecurityGroupId.setter
    def TargetSecurityGroupId(self, TargetSecurityGroupId):
        self._TargetSecurityGroupId = TargetSecurityGroupId

    @property
    def LifeState(self):
        r"""安全组映射的生命状态；NORMAL:正常。
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState


    def _deserialize(self, params):
        self._SecurityGroupMappingId = params.get("SecurityGroupMappingId")
        self._SitePairId = params.get("SitePairId")
        self._SourceSecurityGroupId = params.get("SourceSecurityGroupId")
        self._TargetSecurityGroupId = params.get("TargetSecurityGroupId")
        self._LifeState = params.get("LifeState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SitePair(AbstractModel):
    r"""站点对信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户AppId
        :type AppId: int
        :param _SitePairId: 容灾策略ID
        :type SitePairId: str
        :param _SitePairName: 容灾策略名称
        :type SitePairName: str
        :param _SitePairType: 容灾策略类型（产品类型，如 DISK/CFS/INSTANCE 等）
        :type SitePairType: str
        :param _SitePairState: 容灾策略状态
        :type SitePairState: str
        :param _SourceRegion: 生产地域
        :type SourceRegion: str
        :param _SourceZone: 生产可用区
        :type SourceZone: str
        :param _TargetRegion: 容灾地域
        :type TargetRegion: str
        :param _TargetZone: 容灾可用区
        :type TargetZone: str
        :param _SourceVpc: 生产端VPC
        :type SourceVpc: str
        :param _TargetVpc: 容灾端VPC
        :type TargetVpc: str
        :param _CopyType: 复制技术（SYN 同步 / ASY 异步）
        :type CopyType: str
        :param _DisasterRecoveryType: 容灾类型（CROSS_ZONE 跨可用区 / CROSS_REGION 跨地域 / CROSS_CLOUD 跨云）
        :type DisasterRecoveryType: str
        :param _CreateFrom: 创建来源（LOCAL 本端创建 / PEER 对端创建）
        :type CreateFrom: str
        :param _AccountUin: 创建容灾策略的账户主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUin: str
        :param _SubAccountUin: 创建容灾策略的子账户 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _BindProtectGroupCount: 已绑定的保护组数量
        :type BindProtectGroupCount: int
        :param _ErrorRecoveryPointObjectiveCopyPairSet: RPO 异常的复制对ID列表（最近一次保护点距今超过15分钟的复制对）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorRecoveryPointObjectiveCopyPairSet: list of str
        :param _ProtectedResourceSet: 已保护的资源列表（按资源类型分组）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedResourceSet: list of ProtectedResource
        :param _ProtectedResourceStatusSet: 已保护资源的状态统计，key 为复制对状态，value 为该状态下的资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedResourceStatusSet: list of ProtectedResourceStatus
        :param _CrossCloudDetails: 跨云场景下的额外信息（仅 IsCrossCloud=true 时返回，非跨云为 null）
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossCloudDetails: :class:`tencentcloud.bdrc.v20260330.models.CrossCloudDetails`
        """
        self._AppId = None
        self._SitePairId = None
        self._SitePairName = None
        self._SitePairType = None
        self._SitePairState = None
        self._SourceRegion = None
        self._SourceZone = None
        self._TargetRegion = None
        self._TargetZone = None
        self._SourceVpc = None
        self._TargetVpc = None
        self._CopyType = None
        self._DisasterRecoveryType = None
        self._CreateFrom = None
        self._AccountUin = None
        self._SubAccountUin = None
        self._CreateTime = None
        self._BindProtectGroupCount = None
        self._ErrorRecoveryPointObjectiveCopyPairSet = None
        self._ProtectedResourceSet = None
        self._ProtectedResourceStatusSet = None
        self._CrossCloudDetails = None

    @property
    def AppId(self):
        r"""用户AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SitePairId(self):
        r"""容灾策略ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SitePairName(self):
        r"""容灾策略名称
        :rtype: str
        """
        return self._SitePairName

    @SitePairName.setter
    def SitePairName(self, SitePairName):
        self._SitePairName = SitePairName

    @property
    def SitePairType(self):
        r"""容灾策略类型（产品类型，如 DISK/CFS/INSTANCE 等）
        :rtype: str
        """
        return self._SitePairType

    @SitePairType.setter
    def SitePairType(self, SitePairType):
        self._SitePairType = SitePairType

    @property
    def SitePairState(self):
        r"""容灾策略状态
        :rtype: str
        """
        return self._SitePairState

    @SitePairState.setter
    def SitePairState(self, SitePairState):
        self._SitePairState = SitePairState

    @property
    def SourceRegion(self):
        r"""生产地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SourceZone(self):
        r"""生产可用区
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def TargetRegion(self):
        r"""容灾地域
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetZone(self):
        r"""容灾可用区
        :rtype: str
        """
        return self._TargetZone

    @TargetZone.setter
    def TargetZone(self, TargetZone):
        self._TargetZone = TargetZone

    @property
    def SourceVpc(self):
        r"""生产端VPC
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def TargetVpc(self):
        r"""容灾端VPC
        :rtype: str
        """
        return self._TargetVpc

    @TargetVpc.setter
    def TargetVpc(self, TargetVpc):
        self._TargetVpc = TargetVpc

    @property
    def CopyType(self):
        r"""复制技术（SYN 同步 / ASY 异步）
        :rtype: str
        """
        return self._CopyType

    @CopyType.setter
    def CopyType(self, CopyType):
        self._CopyType = CopyType

    @property
    def DisasterRecoveryType(self):
        r"""容灾类型（CROSS_ZONE 跨可用区 / CROSS_REGION 跨地域 / CROSS_CLOUD 跨云）
        :rtype: str
        """
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def CreateFrom(self):
        r"""创建来源（LOCAL 本端创建 / PEER 对端创建）
        :rtype: str
        """
        return self._CreateFrom

    @CreateFrom.setter
    def CreateFrom(self, CreateFrom):
        self._CreateFrom = CreateFrom

    @property
    def AccountUin(self):
        r"""创建容灾策略的账户主账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def SubAccountUin(self):
        r"""创建容灾策略的子账户 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

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
    def BindProtectGroupCount(self):
        r"""已绑定的保护组数量
        :rtype: int
        """
        return self._BindProtectGroupCount

    @BindProtectGroupCount.setter
    def BindProtectGroupCount(self, BindProtectGroupCount):
        self._BindProtectGroupCount = BindProtectGroupCount

    @property
    def ErrorRecoveryPointObjectiveCopyPairSet(self):
        r"""RPO 异常的复制对ID列表（最近一次保护点距今超过15分钟的复制对）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ErrorRecoveryPointObjectiveCopyPairSet

    @ErrorRecoveryPointObjectiveCopyPairSet.setter
    def ErrorRecoveryPointObjectiveCopyPairSet(self, ErrorRecoveryPointObjectiveCopyPairSet):
        self._ErrorRecoveryPointObjectiveCopyPairSet = ErrorRecoveryPointObjectiveCopyPairSet

    @property
    def ProtectedResourceSet(self):
        r"""已保护的资源列表（按资源类型分组）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProtectedResource
        """
        return self._ProtectedResourceSet

    @ProtectedResourceSet.setter
    def ProtectedResourceSet(self, ProtectedResourceSet):
        self._ProtectedResourceSet = ProtectedResourceSet

    @property
    def ProtectedResourceStatusSet(self):
        r"""已保护资源的状态统计，key 为复制对状态，value 为该状态下的资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProtectedResourceStatus
        """
        return self._ProtectedResourceStatusSet

    @ProtectedResourceStatusSet.setter
    def ProtectedResourceStatusSet(self, ProtectedResourceStatusSet):
        self._ProtectedResourceStatusSet = ProtectedResourceStatusSet

    @property
    def CrossCloudDetails(self):
        r"""跨云场景下的额外信息（仅 IsCrossCloud=true 时返回，非跨云为 null）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CrossCloudDetails`
        """
        return self._CrossCloudDetails

    @CrossCloudDetails.setter
    def CrossCloudDetails(self, CrossCloudDetails):
        self._CrossCloudDetails = CrossCloudDetails


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._SitePairId = params.get("SitePairId")
        self._SitePairName = params.get("SitePairName")
        self._SitePairType = params.get("SitePairType")
        self._SitePairState = params.get("SitePairState")
        self._SourceRegion = params.get("SourceRegion")
        self._SourceZone = params.get("SourceZone")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetZone = params.get("TargetZone")
        self._SourceVpc = params.get("SourceVpc")
        self._TargetVpc = params.get("TargetVpc")
        self._CopyType = params.get("CopyType")
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._CreateFrom = params.get("CreateFrom")
        self._AccountUin = params.get("AccountUin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._CreateTime = params.get("CreateTime")
        self._BindProtectGroupCount = params.get("BindProtectGroupCount")
        self._ErrorRecoveryPointObjectiveCopyPairSet = params.get("ErrorRecoveryPointObjectiveCopyPairSet")
        if params.get("ProtectedResourceSet") is not None:
            self._ProtectedResourceSet = []
            for item in params.get("ProtectedResourceSet"):
                obj = ProtectedResource()
                obj._deserialize(item)
                self._ProtectedResourceSet.append(obj)
        if params.get("ProtectedResourceStatusSet") is not None:
            self._ProtectedResourceStatusSet = []
            for item in params.get("ProtectedResourceStatusSet"):
                obj = ProtectedResourceStatus()
                obj._deserialize(item)
                self._ProtectedResourceStatusSet.append(obj)
        if params.get("CrossCloudDetails") is not None:
            self._CrossCloudDetails = CrossCloudDetails()
            self._CrossCloudDetails._deserialize(params.get("CrossCloudDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SitePairDeniedAction(AbstractModel):
    r"""单个容灾策略的禁止操作集合

    """

    def __init__(self):
        r"""
        :param _SitePairId: 容灾策略ID
        :type SitePairId: str
        :param _DeniedActions: 该容灾策略当前被禁止执行的操作列表
        :type DeniedActions: list of DeniedAction
        """
        self._SitePairId = None
        self._DeniedActions = None

    @property
    def SitePairId(self):
        r"""容灾策略ID
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def DeniedActions(self):
        r"""该容灾策略当前被禁止执行的操作列表
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._SitePairId = params.get("SitePairId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCopyPairTasksRequest(AbstractModel):
    r"""StopCopyPairTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CopyPairIds: 复制对ID列表
        :type CopyPairIds: list of str
        :param _CopyPairType: 复制对类型（DISK/INSTANCE/CFS）
        :type CopyPairType: str
        """
        self._CopyPairIds = None
        self._CopyPairType = None

    @property
    def CopyPairIds(self):
        r"""复制对ID列表
        :rtype: list of str
        """
        return self._CopyPairIds

    @CopyPairIds.setter
    def CopyPairIds(self, CopyPairIds):
        self._CopyPairIds = CopyPairIds

    @property
    def CopyPairType(self):
        r"""复制对类型（DISK/INSTANCE/CFS）
        :rtype: str
        """
        return self._CopyPairType

    @CopyPairType.setter
    def CopyPairType(self, CopyPairType):
        self._CopyPairType = CopyPairType


    def _deserialize(self, params):
        self._CopyPairIds = params.get("CopyPairIds")
        self._CopyPairType = params.get("CopyPairType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCopyPairTasksResponse(AbstractModel):
    r"""StopCopyPairTasks返回参数结构体

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


class SupportRegionInfo(AbstractModel):
    r"""支持的生产地域配置详情，包含支持类型与可用区粒度规则。

    """

    def __init__(self):
        r"""
        :param _SourceRegion: 生产地域。
        :type SourceRegion: str
        :param _SupportType: 支持类型：REGION（地域级，整个生产地域均支持容灾）；ZONE（可用区级，按 SupportZoneRules 控制粒度）。
        :type SupportType: str
        :param _Status: 配置状态：valid（生效）/ invalid（停用）。
        :type Status: str
        :param _SupportZoneRules: 可用区级容灾规则列表。仅当 SupportType=ZONE 时有效；REGION 类型时该字段返回空数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportZoneRules: list of SupportZoneRule
        """
        self._SourceRegion = None
        self._SupportType = None
        self._Status = None
        self._SupportZoneRules = None

    @property
    def SourceRegion(self):
        r"""生产地域。
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion

    @property
    def SupportType(self):
        r"""支持类型：REGION（地域级，整个生产地域均支持容灾）；ZONE（可用区级，按 SupportZoneRules 控制粒度）。
        :rtype: str
        """
        return self._SupportType

    @SupportType.setter
    def SupportType(self, SupportType):
        self._SupportType = SupportType

    @property
    def Status(self):
        r"""配置状态：valid（生效）/ invalid（停用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SupportZoneRules(self):
        r"""可用区级容灾规则列表。仅当 SupportType=ZONE 时有效；REGION 类型时该字段返回空数组。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SupportZoneRule
        """
        return self._SupportZoneRules

    @SupportZoneRules.setter
    def SupportZoneRules(self, SupportZoneRules):
        self._SupportZoneRules = SupportZoneRules


    def _deserialize(self, params):
        self._SourceRegion = params.get("SourceRegion")
        self._SupportType = params.get("SupportType")
        self._Status = params.get("Status")
        if params.get("SupportZoneRules") is not None:
            self._SupportZoneRules = []
            for item in params.get("SupportZoneRules"):
                obj = SupportZoneRule()
                obj._deserialize(item)
                self._SupportZoneRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportZoneRule(AbstractModel):
    r"""可用区级容灾规则，描述某个生产可用区可容灾到的目标可用区集合。

    """

    def __init__(self):
        r"""
        :param _SourceZone: 生产可用区。
        :type SourceZone: str
        :param _IsAllZoneSupport: 是否支持容灾到生产地域内的全部可用区。true 时 TargetZones 可忽略。
        :type IsAllZoneSupport: bool
        :param _TargetZones: 目标可用区列表。当 IsAllZoneSupport=false 时枚举具体可容灾到的可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetZones: list of str
        """
        self._SourceZone = None
        self._IsAllZoneSupport = None
        self._TargetZones = None

    @property
    def SourceZone(self):
        r"""生产可用区。
        :rtype: str
        """
        return self._SourceZone

    @SourceZone.setter
    def SourceZone(self, SourceZone):
        self._SourceZone = SourceZone

    @property
    def IsAllZoneSupport(self):
        r"""是否支持容灾到生产地域内的全部可用区。true 时 TargetZones 可忽略。
        :rtype: bool
        """
        return self._IsAllZoneSupport

    @IsAllZoneSupport.setter
    def IsAllZoneSupport(self, IsAllZoneSupport):
        self._IsAllZoneSupport = IsAllZoneSupport

    @property
    def TargetZones(self):
        r"""目标可用区列表。当 IsAllZoneSupport=false 时枚举具体可容灾到的可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TargetZones

    @TargetZones.setter
    def TargetZones(self, TargetZones):
        self._TargetZones = TargetZones


    def _deserialize(self, params):
        self._SourceZone = params.get("SourceZone")
        self._IsAllZoneSupport = params.get("IsAllZoneSupport")
        self._TargetZones = params.get("TargetZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TypeCount(AbstractModel):
    r"""备份库类型统计

    """

    def __init__(self):
        r"""
        :param _Type: 备份库类型
        :type Type: str
        :param _Count: 备份库数量
        :type Count: int
        """
        self._Type = None
        self._Count = None

    @property
    def Type(self):
        r"""备份库类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""备份库数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoBackupPolicyRequest(AbstractModel):
    r"""UnbindAutoBackupPolicy请求参数结构体

    """


class UnbindAutoBackupPolicyResponse(AbstractModel):
    r"""UnbindAutoBackupPolicy返回参数结构体

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


class VaultDeniedAction(AbstractModel):
    r"""备份库操作掩码

    """

    def __init__(self):
        r"""
        :param _VaultId: 备份库实例ID
        :type VaultId: str
        :param _DeniedActions: 被禁止的操作列表
        :type DeniedActions: list of DeniedAction
        """
        self._VaultId = None
        self._DeniedActions = None

    @property
    def VaultId(self):
        r"""备份库实例ID
        :rtype: str
        """
        return self._VaultId

    @VaultId.setter
    def VaultId(self, VaultId):
        self._VaultId = VaultId

    @property
    def DeniedActions(self):
        r"""被禁止的操作列表
        :rtype: list of DeniedAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._VaultId = params.get("VaultId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualPrivateCloud(AbstractModel):
    r"""描述了VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如 vpc-xxxxxxxx。私有网络ID可通过登录控制台查询，也可通过调用接口 [DescribeVpcEx]的返回值中的unVpcId字段获取。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如 subnet-xxxxxxxx。私有网络子网ID可通过登录控制台查询，也可通过调用接口 [DescribeSubnets](https://cloud.tencent.com/document/api/215/15784) 的返回值中的 unSubnetId 字段获取。
        :type SubnetId: str
        :param _SubnetName: 私有网络子网名称。
        :type SubnetName: str
        :param _AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：true（用作公网网关）/false（不作为公网网关），默认取值：false。
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例 vpc 属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :type PrivateIpAddresses: list of str
        :param _VpcName: 私有网络名称，仅做展示用。
        :type VpcName: str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._VpcName = None
        self._Ipv6AddressCount = None

    @property
    def VpcId(self):
        r"""私有网络ID，形如 vpc-xxxxxxxx。私有网络ID可通过登录控制台查询，也可通过调用接口 [DescribeVpcEx]的返回值中的unVpcId字段获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络子网ID，形如 subnet-xxxxxxxx。私有网络子网ID可通过登录控制台查询，也可通过调用接口 [DescribeSubnets](https://cloud.tencent.com/document/api/215/15784) 的返回值中的 unSubnetId 字段获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""私有网络子网名称。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def AsVpcGateway(self):
        r"""是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：true（用作公网网关）/false（不作为公网网关），默认取值：false。
        :rtype: bool
        """
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        r"""私有网络子网 IP 数组，在创建实例、修改实例 vpc 属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def VpcName(self):
        r"""私有网络名称，仅做展示用。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Ipv6AddressCount(self):
        r"""为弹性网卡指定随机生成的 IPv6 地址数量。
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._VpcName = params.get("VpcName")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcMapping(AbstractModel):
    r"""站点对vpc映射信息

    """

    def __init__(self):
        r"""
        :param _Id: 映射规则主键ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _SitePairId: 所属容灾策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SitePairId: str
        :param _SourceVpc: 源端VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceVpc: str
        :param _SourceSubnet: 源端子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceSubnet: str
        :param _TargetVpc: 目标端VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVpc: str
        :param _TargetSubnet: 目标端子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetSubnet: str
        :param _Status: 映射状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _LifeState: 生命周期状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeState: str
        """
        self._Id = None
        self._SitePairId = None
        self._SourceVpc = None
        self._SourceSubnet = None
        self._TargetVpc = None
        self._TargetSubnet = None
        self._Status = None
        self._LifeState = None

    @property
    def Id(self):
        r"""映射规则主键ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SitePairId(self):
        r"""所属容灾策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SitePairId

    @SitePairId.setter
    def SitePairId(self, SitePairId):
        self._SitePairId = SitePairId

    @property
    def SourceVpc(self):
        r"""源端VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceVpc

    @SourceVpc.setter
    def SourceVpc(self, SourceVpc):
        self._SourceVpc = SourceVpc

    @property
    def SourceSubnet(self):
        r"""源端子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceSubnet

    @SourceSubnet.setter
    def SourceSubnet(self, SourceSubnet):
        self._SourceSubnet = SourceSubnet

    @property
    def TargetVpc(self):
        r"""目标端VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetVpc

    @TargetVpc.setter
    def TargetVpc(self, TargetVpc):
        self._TargetVpc = TargetVpc

    @property
    def TargetSubnet(self):
        r"""目标端子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetSubnet

    @TargetSubnet.setter
    def TargetSubnet(self, TargetSubnet):
        self._TargetSubnet = TargetSubnet

    @property
    def Status(self):
        r"""映射状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LifeState(self):
        r"""生命周期状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SitePairId = params.get("SitePairId")
        self._SourceVpc = params.get("SourceVpc")
        self._SourceSubnet = params.get("SourceSubnet")
        self._TargetVpc = params.get("TargetVpc")
        self._TargetSubnet = params.get("TargetSubnet")
        self._Status = params.get("Status")
        self._LifeState = params.get("LifeState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        