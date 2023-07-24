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


class AdvancedRetentionPolicy(AbstractModel):
    """定期快照高级保留策略，四个参数都为必选参数

    """

    def __init__(self):
        r"""
        :param _Days: 保留最新快照Days天内的每天最新的一个快照，取值范围：[0, 100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Days: int
        :param _Weeks: 保留最新快照Weeks周内的每周最新的一个快照，取值范围：[0, 100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Weeks: int
        :param _Months: 保留最新快照Months月内的每月最新的一个快照， 取值范围：[0, 100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Months: int
        :param _Years: 保留最新快照Years年内的每年最新的一个快照，取值范围：[0, 100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Years: int
        """
        self._Days = None
        self._Weeks = None
        self._Months = None
        self._Years = None

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Weeks(self):
        return self._Weeks

    @Weeks.setter
    def Weeks(self, Weeks):
        self._Weeks = Weeks

    @property
    def Months(self):
        return self._Months

    @Months.setter
    def Months(self, Months):
        self._Months = Months

    @property
    def Years(self):
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
        


class ApplyDiskBackupRequest(AbstractModel):
    """ApplyDiskBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 云硬盘备份点ID，可通过 DescribeDiskBackups 查询。
        :type DiskBackupId: str
        :param _DiskId: 云硬盘备份点原云硬盘ID，可通过DescribeDisks接口查询。
        :type DiskId: str
        """
        self._DiskBackupId = None
        self._DiskId = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupResponse(AbstractModel):
    """ApplyDiskBackup返回参数结构体

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


class ApplySnapshotRequest(AbstractModel):
    """ApplySnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID, 可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotId: str
        :param _DiskId: 快照原云硬盘ID，可通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param _AutoStopInstance: 回滚前是否执行自动关机
        :type AutoStopInstance: bool
        :param _AutoStartInstance: 回滚完成后是否自动开机
        :type AutoStartInstance: bool
        """
        self._SnapshotId = None
        self._DiskId = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def AutoStopInstance(self):
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        return self._AutoStartInstance

    @AutoStartInstance.setter
    def AutoStartInstance(self, AutoStartInstance):
        self._AutoStartInstance = AutoStartInstance


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskId = params.get("DiskId")
        self._AutoStopInstance = params.get("AutoStopInstance")
        self._AutoStartInstance = params.get("AutoStartInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySnapshotResponse(AbstractModel):
    """ApplySnapshot返回参数结构体

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


class AttachDetail(AbstractModel):
    """描述一个实例已挂载和可挂载数据盘的数量。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AttachedDiskCount: 实例已挂载数据盘的数量。
        :type AttachedDiskCount: int
        :param _MaxAttachCount: 实例最大可挂载数据盘的数量。
        :type MaxAttachCount: int
        """
        self._InstanceId = None
        self._AttachedDiskCount = None
        self._MaxAttachCount = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachedDiskCount(self):
        return self._AttachedDiskCount

    @AttachedDiskCount.setter
    def AttachedDiskCount(self, AttachedDiskCount):
        self._AttachedDiskCount = AttachedDiskCount

    @property
    def MaxAttachCount(self):
        return self._MaxAttachCount

    @MaxAttachCount.setter
    def MaxAttachCount(self, MaxAttachCount):
        self._MaxAttachCount = MaxAttachCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AttachedDiskCount = params.get("AttachedDiskCount")
        self._MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    """AttachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云服务器实例ID。云盘将被挂载到此云服务器上，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :type InstanceId: str
        :param _DiskIds: 将要被挂载的弹性云盘ID。通过[DescribeDisks](/document/product/362/16315)接口查询。单次最多可挂载10块弹性云盘。
        :type DiskIds: list of str
        :param _DeleteWithInstance: 可选参数，不传该参数则仅执行挂载操作。传入`True`时，会在挂载成功后将云硬盘设置为随云主机销毁模式，仅对按量计费云硬盘有效。
        :type DeleteWithInstance: bool
        :param _AttachMode: 可选参数，用于控制云盘挂载时使用的挂载模式，目前仅对黑石裸金属机型有效。取值范围：<br><li>PF<br><li>VF
        :type AttachMode: str
        """
        self._InstanceId = None
        self._DiskIds = None
        self._DeleteWithInstance = None
        self._AttachMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def AttachMode(self):
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskIds = params.get("DiskIds")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._AttachMode = params.get("AttachMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks返回参数结构体

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


class AutoMountConfiguration(AbstractModel):
    """描述了新购云硬盘时自动将云硬盘初始化并挂载至云服务器内部的配置。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 要挂载到的实例ID。
        :type InstanceId: list of str
        :param _MountPoint: 子机内的挂载点。
        :type MountPoint: list of str
        :param _FileSystemType: 文件系统类型，支持的有 ext4、xfs。
        :type FileSystemType: str
        """
        self._InstanceId = None
        self._MountPoint = None
        self._FileSystemType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def FileSystemType(self):
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MountPoint = params.get("MountPoint")
        self._FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSnapshotPolicy(AbstractModel):
    """描述了定期快照策略的详细信息

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: 已绑定当前定期快照策略的云盘ID列表。
        :type DiskIdSet: list of str
        :param _IsActivated: 定期快照策略是否激活。
        :type IsActivated: bool
        :param _AutoSnapshotPolicyState: 定期快照策略的状态。取值范围：<br><li>NORMAL：正常<br><li>ISOLATED：已隔离。
        :type AutoSnapshotPolicyState: str
        :param _IsCopyToRemote: 是否是跨账号复制快照快照, 1：是, 0: 不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCopyToRemote: int
        :param _IsPermanent: 使用该定期快照策略创建出来的快照是否永久保留。
        :type IsPermanent: bool
        :param _NextTriggerTime: 定期快照下次触发的时间。
        :type NextTriggerTime: str
        :param _AutoSnapshotPolicyName: 定期快照策略名称。
        :type AutoSnapshotPolicyName: str
        :param _AutoSnapshotPolicyId: 定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param _Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param _CreateTime: 定期快照策略的创建时间。
        :type CreateTime: str
        :param _RetentionDays: 使用该定期快照策略创建出来的快照保留天数。
        :type RetentionDays: int
        :param _CopyToAccountUin: 复制的目标账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CopyToAccountUin: str
        :param _InstanceIdSet: 已绑定当前定期快照策略的实例ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIdSet: list of str
        :param _RetentionMonths: 该定期快照创建的快照可以保留的月数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionMonths: int
        :param _RetentionAmount: 该定期快照创建的快照最大保留数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionAmount: int
        :param _AdvancedRetentionPolicy: 定期快照高级保留策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedRetentionPolicy: :class:`tencentcloud.cbs.v20170312.models.AdvancedRetentionPolicy`
        :param _CopyFromAccountUin: 该复制快照策略的源端账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CopyFromAccountUin: str
        :param _Tags: 标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._DiskIdSet = None
        self._IsActivated = None
        self._AutoSnapshotPolicyState = None
        self._IsCopyToRemote = None
        self._IsPermanent = None
        self._NextTriggerTime = None
        self._AutoSnapshotPolicyName = None
        self._AutoSnapshotPolicyId = None
        self._Policy = None
        self._CreateTime = None
        self._RetentionDays = None
        self._CopyToAccountUin = None
        self._InstanceIdSet = None
        self._RetentionMonths = None
        self._RetentionAmount = None
        self._AdvancedRetentionPolicy = None
        self._CopyFromAccountUin = None
        self._Tags = None

    @property
    def DiskIdSet(self):
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def AutoSnapshotPolicyState(self):
        return self._AutoSnapshotPolicyState

    @AutoSnapshotPolicyState.setter
    def AutoSnapshotPolicyState(self, AutoSnapshotPolicyState):
        self._AutoSnapshotPolicyState = AutoSnapshotPolicyState

    @property
    def IsCopyToRemote(self):
        return self._IsCopyToRemote

    @IsCopyToRemote.setter
    def IsCopyToRemote(self, IsCopyToRemote):
        self._IsCopyToRemote = IsCopyToRemote

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def NextTriggerTime(self):
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def CopyToAccountUin(self):
        return self._CopyToAccountUin

    @CopyToAccountUin.setter
    def CopyToAccountUin(self, CopyToAccountUin):
        self._CopyToAccountUin = CopyToAccountUin

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RetentionMonths(self):
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def AdvancedRetentionPolicy(self):
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy

    @property
    def CopyFromAccountUin(self):
        return self._CopyFromAccountUin

    @CopyFromAccountUin.setter
    def CopyFromAccountUin(self, CopyFromAccountUin):
        self._CopyFromAccountUin = CopyFromAccountUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._IsActivated = params.get("IsActivated")
        self._AutoSnapshotPolicyState = params.get("AutoSnapshotPolicyState")
        self._IsCopyToRemote = params.get("IsCopyToRemote")
        self._IsPermanent = params.get("IsPermanent")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._RetentionDays = params.get("RetentionDays")
        self._CopyToAccountUin = params.get("CopyToAccountUin")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RetentionMonths = params.get("RetentionMonths")
        self._RetentionAmount = params.get("RetentionAmount")
        if params.get("AdvancedRetentionPolicy") is not None:
            self._AdvancedRetentionPolicy = AdvancedRetentionPolicy()
            self._AdvancedRetentionPolicy._deserialize(params.get("AdvancedRetentionPolicy"))
        self._CopyFromAccountUin = params.get("CopyFromAccountUin")
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
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 要绑定的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param _DiskIds: 要绑定的云硬盘ID列表，一次请求最多绑定80块云盘。
        :type DiskIds: list of str
        """
        self._AutoSnapshotPolicyId = None
        self._DiskIds = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy返回参数结构体

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


class Cdc(AbstractModel):
    """描述独享集群的详细信息。

    """

    def __init__(self):
        r"""
        :param _CageId: 独享集群围笼ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        :param _CdcState: 独享集群状态。取值范围：<br><li>NORMAL：正常；<br><li>CLOSED：关闭，此时将不可使用该独享集群创建新的云硬盘；<br><li>FAULT：独享集群状态异常，此时独享集群将不可操作，腾讯云运维团队将会及时修复该集群；<br><li>ISOLATED：因未及时续费导致独享集群被隔离，此时将不可使用该独享集群创建新的云硬盘，对应的云硬盘也将不可操作。
        :type CdcState: str
        :param _Zone: 独享集群所属的[可用区](/document/product/213/15753#ZoneInfo)ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _CdcName: 独享集群实例名称。
        :type CdcName: str
        :param _CdcResource: 独享集群的资源容量大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcResource: :class:`tencentcloud.cbs.v20170312.models.CdcSize`
        :param _CdcId: 独享集群实例id。
        :type CdcId: str
        :param _DiskType: 独享集群类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘集群<br><li>CLOUD_PREMIUM：表示高性能云硬盘集群<br><li>CLOUD_SSD：SSD表示SSD云硬盘集群。
        :type DiskType: str
        :param _ExpiredTime: 独享集群到期时间。
        :type ExpiredTime: str
        :param _CreatedTime: 存储池创建时间。
        :type CreatedTime: str
        :param _DiskNumber: 当前集群中已创建的云盘数量。
        :type DiskNumber: int
        """
        self._CageId = None
        self._CdcState = None
        self._Zone = None
        self._CdcName = None
        self._CdcResource = None
        self._CdcId = None
        self._DiskType = None
        self._ExpiredTime = None
        self._CreatedTime = None
        self._DiskNumber = None

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def CdcState(self):
        return self._CdcState

    @CdcState.setter
    def CdcState(self, CdcState):
        self._CdcState = CdcState

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CdcName(self):
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcResource(self):
        return self._CdcResource

    @CdcResource.setter
    def CdcResource(self, CdcResource):
        self._CdcResource = CdcResource

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DiskNumber(self):
        return self._DiskNumber

    @DiskNumber.setter
    def DiskNumber(self, DiskNumber):
        self._DiskNumber = DiskNumber


    def _deserialize(self, params):
        self._CageId = params.get("CageId")
        self._CdcState = params.get("CdcState")
        self._Zone = params.get("Zone")
        self._CdcName = params.get("CdcName")
        if params.get("CdcResource") is not None:
            self._CdcResource = CdcSize()
            self._CdcResource._deserialize(params.get("CdcResource"))
        self._CdcId = params.get("CdcId")
        self._DiskType = params.get("DiskType")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CreatedTime = params.get("CreatedTime")
        self._DiskNumber = params.get("DiskNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcSize(AbstractModel):
    """显示独享集群的大小

    """

    def __init__(self):
        r"""
        :param _DiskAavilable: 独享集群的可用容量大小，单位GiB
        :type DiskAavilable: int
        :param _DiskTotal: 独享集群的总容量大小，单位GiB
        :type DiskTotal: int
        """
        self._DiskAavilable = None
        self._DiskTotal = None

    @property
    def DiskAavilable(self):
        return self._DiskAavilable

    @DiskAavilable.setter
    def DiskAavilable(self, DiskAavilable):
        self._DiskAavilable = DiskAavilable

    @property
    def DiskTotal(self):
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal


    def _deserialize(self, params):
        self._DiskAavilable = params.get("DiskAavilable")
        self._DiskTotal = params.get("DiskTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopySnapshotCrossRegionsRequest(AbstractModel):
    """CopySnapshotCrossRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DestinationRegions: 快照需要复制到的目标地域，各地域的标准取值可通过接口[DescribeRegions](https://cloud.tencent.com/document/product/213/9456)查询，且只能传入支持快照的地域。
        :type DestinationRegions: list of str
        :param _SnapshotId: 需要跨地域复制的源快照ID，可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotId: str
        :param _SnapshotName: 新复制快照的名称，如果不传，则默认取值为“Copied 源快照ID from 地域名”。
        :type SnapshotName: str
        """
        self._DestinationRegions = None
        self._SnapshotId = None
        self._SnapshotName = None

    @property
    def DestinationRegions(self):
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._DestinationRegions = params.get("DestinationRegions")
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopySnapshotCrossRegionsResponse(AbstractModel):
    """CopySnapshotCrossRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotCopyResultSet: 快照跨地域复制的结果，如果请求下发成功，则返回相应地地域的新快照ID，否则返回Error。
        :type SnapshotCopyResultSet: list of SnapshotCopyResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotCopyResultSet = None
        self._RequestId = None

    @property
    def SnapshotCopyResultSet(self):
        return self._SnapshotCopyResultSet

    @SnapshotCopyResultSet.setter
    def SnapshotCopyResultSet(self, SnapshotCopyResultSet):
        self._SnapshotCopyResultSet = SnapshotCopyResultSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotCopyResultSet") is not None:
            self._SnapshotCopyResultSet = []
            for item in params.get("SnapshotCopyResultSet"):
                obj = SnapshotCopyResult()
                obj._deserialize(item)
                self._SnapshotCopyResultSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param _DryRun: 是否创建定期快照的执行策略。TRUE表示只需获取首次开始备份的时间，不实际创建定期快照策略，FALSE表示创建，默认为FALSE。
        :type DryRun: bool
        :param _IsActivated: 是否激活定期快照策略，FALSE表示未激活，TRUE表示激活，默认为TRUE。
        :type IsActivated: bool
        :param _AutoSnapshotPolicyName: 要创建的定期快照策略名。不传则默认为“未命名”。最大长度不能超60个字节。
        :type AutoSnapshotPolicyName: str
        :param _IsPermanent: 通过该定期快照策略创建的快照是否永久保留。FALSE表示非永久保留，TRUE表示永久保留，默认为FALSE。
        :type IsPermanent: bool
        :param _RetentionDays: 通过该定期快照策略创建的快照保留天数，默认保留7天。如果指定本参数，则IsPermanent入参不可指定为TRUE，否则会产生冲突。
        :type RetentionDays: int
        """
        self._Policy = None
        self._DryRun = None
        self._IsActivated = None
        self._AutoSnapshotPolicyName = None
        self._IsPermanent = None
        self._RetentionDays = None

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._DryRun = params.get("DryRun")
        self._IsActivated = params.get("IsActivated")
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self._IsPermanent = params.get("IsPermanent")
        self._RetentionDays = params.get("RetentionDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 新创建的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param _NextTriggerTime: 首次开始备份的时间。
        :type NextTriggerTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._NextTriggerTime = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def NextTriggerTime(self):
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._RequestId = params.get("RequestId")


class CreateDiskBackupRequest(AbstractModel):
    """CreateDiskBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 要创建备份点的云硬盘名称。
        :type DiskId: str
        :param _DiskBackupName: 云硬盘备份点名称。长度不能超过100个字符。
        :type DiskBackupName: str
        """
        self._DiskId = None
        self._DiskBackupName = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupName(self):
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupName = params.get("DiskBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDiskBackupResponse(AbstractModel):
    """CreateDiskBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 云硬盘备份点的ID。
        :type DiskBackupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskBackupId = None
        self._RequestId = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    """CreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目。若不指定项目，将在默认项目下进行创建。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _DiskChargeType: 云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDCPAID：独享集群付费<br>各类型价格请参考云硬盘[价格总览](/document/product/362/2413)。
        :type DiskChargeType: str
        :param _DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_BSSD：表示通用型SSD云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :type DiskType: str
        :param _DiskName: 云盘显示名称。不传则默认为“未命名”。最大长度不能超60个字节。
        :type DiskName: str
        :param _Tags: 云盘绑定的标签。
        :type Tags: list of Tag
        :param _SnapshotId: 快照ID，如果传入则根据此快照创建云硬盘，快照类型必须为数据盘快照，可通过[DescribeSnapshots](/document/product/362/15647)接口查询快照，见输出参数DiskUsage解释。
        :type SnapshotId: str
        :param _DiskCount: 创建云硬盘数量，不传则默认为1。单次请求最多可创建的云盘数有限制，具体参见[云硬盘使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        :type DiskCount: int
        :param _ThroughputPerformance: 可选参数。使用此参数可给云硬盘购买额外的性能。<br>当前仅支持极速型云盘（CLOUD_TSSD）和增强型SSD云硬盘（CLOUD_HSSD）
        :type ThroughputPerformance: int
        :param _DiskSize: 云硬盘大小，单位为GB。<br><li>如果传入`SnapshotId`则可不传`DiskSize`，此时新建云盘的大小为快照大小<br><li>如果传入`SnapshotId`同时传入`DiskSize`，则云盘大小必须大于或等于快照大小<br><li>云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param _Shareable: 可选参数，默认为False。传入True时，云盘将创建为共享型云盘。
        :type Shareable: bool
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _Encrypt: 传入该参数用于创建加密云盘，取值固定为ENCRYPT。
        :type Encrypt: str
        :param _DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DeleteSnapshot: 销毁云盘时删除关联的非永久保留快照。0 表示非永久快照不随云盘销毁而销毁，1表示非永久快照随云盘销毁而销毁，默认取0。快照是否永久保留可以通过DescribeSnapshots接口返回的快照详情的IsPermanent字段来判断，true表示永久快照，false表示非永久快照。
        :type DeleteSnapshot: int
        :param _AutoMountConfiguration: 创建云盘时指定自动挂载并初始化该数据盘。
        :type AutoMountConfiguration: :class:`tencentcloud.cbs.v20170312.models.AutoMountConfiguration`
        :param _DiskBackupQuota: 指定云硬盘备份点配额。
        :type DiskBackupQuota: int
        :param _BurstPerformance: 创建云盘时是否开启性能突发
        :type BurstPerformance: bool
        """
        self._Placement = None
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskName = None
        self._Tags = None
        self._SnapshotId = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._DiskSize = None
        self._Shareable = None
        self._ClientToken = None
        self._Encrypt = None
        self._DiskChargePrepaid = None
        self._DeleteSnapshot = None
        self._AutoMountConfiguration = None
        self._DiskBackupQuota = None
        self._BurstPerformance = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Shareable(self):
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def AutoMountConfiguration(self):
        return self._AutoMountConfiguration

    @AutoMountConfiguration.setter
    def AutoMountConfiguration(self, AutoMountConfiguration):
        self._AutoMountConfiguration = AutoMountConfiguration

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def BurstPerformance(self):
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskType = params.get("DiskType")
        self._DiskName = params.get("DiskName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SnapshotId = params.get("SnapshotId")
        self._DiskCount = params.get("DiskCount")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskSize = params.get("DiskSize")
        self._Shareable = params.get("Shareable")
        self._ClientToken = params.get("ClientToken")
        self._Encrypt = params.get("Encrypt")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        if params.get("AutoMountConfiguration") is not None:
            self._AutoMountConfiguration = AutoMountConfiguration()
            self._AutoMountConfiguration._deserialize(params.get("AutoMountConfiguration"))
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    """CreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: 创建的云硬盘ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskIdSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskIdSet = None
        self._RequestId = None

    @property
    def DiskIdSet(self):
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 需要创建快照的云硬盘ID，可通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param _SnapshotName: 快照名称，不传则新快照名称默认为“未命名”。
        :type SnapshotName: str
        :param _Deadline: 快照的到期时间，到期后该快照将会自动删除,需要传入UTC时间下的ISO-8601标准时间格式,例如:2022-01-08T09:47:55+00:00,。到期时间最小可设置为一天后的当前时间。
        :type Deadline: str
        :param _DiskBackupId: 云硬盘备份点ID。传入此参数时，将通过备份点创建快照。
        :type DiskBackupId: str
        :param _Tags: 快照绑定的标签。
        :type Tags: list of Tag
        """
        self._DiskId = None
        self._SnapshotName = None
        self._Deadline = None
        self._DiskBackupId = None
        self._Tags = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._SnapshotName = params.get("SnapshotName")
        self._Deadline = params.get("Deadline")
        self._DiskBackupId = params.get("DiskBackupId")
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
        


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 新创建的快照ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    """DeleteAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyIds: 要删除的定期快照策略ID列表。
        :type AutoSnapshotPolicyIds: list of str
        """
        self._AutoSnapshotPolicyIds = None

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    """DeleteAutoSnapshotPolicies返回参数结构体

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


class DeleteDiskBackupsRequest(AbstractModel):
    """DeleteDiskBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 待删除的云硬盘备份点ID。
        :type DiskBackupIds: list of str
        """
        self._DiskBackupIds = None

    @property
    def DiskBackupIds(self):
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDiskBackupsResponse(AbstractModel):
    """DeleteDiskBackups返回参数结构体

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


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要删除的快照ID列表，可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotIds: list of str
        :param _DeleteBindImages: 是否强制删除快照关联的镜像
        :type DeleteBindImages: bool
        """
        self._SnapshotIds = None
        self._DeleteBindImages = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DeleteBindImages(self):
        return self._DeleteBindImages

    @DeleteBindImages.setter
    def DeleteBindImages(self, DeleteBindImages):
        self._DeleteBindImages = DeleteBindImages


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        self._DeleteBindImages = params.get("DeleteBindImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回参数结构体

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


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyIds: 要查询的定期快照策略ID列表。参数不支持同时指定`AutoSnapshotPolicyIds`和`Filters`。
        :type AutoSnapshotPolicyIds: list of str
        :param _Filters: 过滤条件。参数不支持同时指定`AutoSnapshotPolicyIds`和`Filters`。<br><li>auto-snapshot-policy-id - Array of String - 是否必填：否 -（过滤条件）按定期快照策略ID进行过滤。定期快照策略ID形如：`asp-11112222`。<br><li>auto-snapshot-policy-state - Array of String - 是否必填：否 -（过滤条件）按定期快照策略的状态进行过滤。定期快照策略ID形如：`asp-11112222`。(NORMAL：正常 | ISOLATED：已隔离。)<br><li>auto-snapshot-policy-name - Array of String - 是否必填：否 -（过滤条件）按定期快照策略名称进行过滤。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _Order: 输出定期快照列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param _OrderField: 定期快照列表排序的依据字段。取值范围：<br><li>CREATETIME：依据定期快照的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        """
        self._AutoSnapshotPolicyIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._OrderField = None

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 有效的定期快照策略数量。
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: 定期快照策略列表。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self._AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self._AutoSnapshotPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskAssociatedAutoSnapshotPolicyRequest(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 要查询的云硬盘ID。
        :type DiskId: str
        """
        self._DiskId = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskAssociatedAutoSnapshotPolicyResponse(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 云盘绑定的定期快照数量。
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: 云盘绑定的定期快照列表。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self._AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self._AutoSnapshotPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskBackupsRequest(AbstractModel):
    """DescribeDiskBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: 要查询备份点的ID列表。参数不支持同时指定 DiskBackupIds 和 Filters。
        :type DiskBackupIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定 DiskBackupIds 和 Filters。过滤条件：<br><li>disk-backup-id - Array of String - 是否必填：否 -（过滤条件）按照备份点的ID过滤。备份点ID形如：dbp-11112222。
<br><li>disk-id - Array of String - 是否必填：否 -（过滤条件）按照创建备份点的云硬盘ID过滤。
<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按创建备份点的云硬盘类型过滤。 (SYSTEM_DISK：代表系统盘 | DATA_DISK：代表数据盘。)
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _Order: 输出云硬盘备份点列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param _OrderField: 云硬盘备份点列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云硬盘备份点的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        """
        self._DiskBackupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def DiskBackupIds(self):
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
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
        


class DescribeDiskBackupsResponse(AbstractModel):
    """DescribeDiskBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的云硬盘备份点数量。
        :type TotalCount: int
        :param _DiskBackupSet: 云硬盘备份点的详细信息列表。
        :type DiskBackupSet: list of DiskBackup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskBackupSet(self):
        return self._DiskBackupSet

    @DiskBackupSet.setter
    def DiskBackupSet(self, DiskBackupSet):
        self._DiskBackupSet = DiskBackupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DiskBackupSet") is not None:
            self._DiskBackupSet = []
            for item in params.get("DiskBackupSet"):
                obj = DiskBackup()
                obj._deserialize(item)
                self._DiskBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskConfigQuotaRequest(AbstractModel):
    """DescribeDiskConfigQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InquiryType: 查询类别，取值范围。<br><li>INQUIRY_CBS_CONFIG：查询云盘配置列表<br><li>INQUIRY_CVM_CONFIG：查询云盘与实例搭配的配置列表。
        :type InquiryType: str
        :param _DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：预付费<br><li>POSTPAID_BY_HOUR：后付费。
        :type DiskChargeType: str
        :param _InstanceFamilies: 按照实例机型系列过滤。实例机型系列形如：S1、I1、M1等。详见[实例类型](https://cloud.tencent.com/document/product/213/11518)
        :type InstanceFamilies: list of str
        :param _DiskTypes: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘。
        :type DiskTypes: list of str
        :param _Zones: 查询一个或多个[可用区](/document/product/213/15753#ZoneInfo)下的配置。
        :type Zones: list of str
        :param _Memory: 实例内存大小。
        :type Memory: int
        :param _DiskUsage: 系统盘或数据盘。取值范围：<br><li>SYSTEM_DISK：表示系统盘<br><li>DATA_DISK：表示数据盘。
        :type DiskUsage: str
        :param _CPU: 实例CPU核数。
        :type CPU: int
        """
        self._InquiryType = None
        self._DiskChargeType = None
        self._InstanceFamilies = None
        self._DiskTypes = None
        self._Zones = None
        self._Memory = None
        self._DiskUsage = None
        self._CPU = None

    @property
    def InquiryType(self):
        return self._InquiryType

    @InquiryType.setter
    def InquiryType(self, InquiryType):
        self._InquiryType = InquiryType

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def InstanceFamilies(self):
        return self._InstanceFamilies

    @InstanceFamilies.setter
    def InstanceFamilies(self, InstanceFamilies):
        self._InstanceFamilies = InstanceFamilies

    @property
    def DiskTypes(self):
        return self._DiskTypes

    @DiskTypes.setter
    def DiskTypes(self, DiskTypes):
        self._DiskTypes = DiskTypes

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU


    def _deserialize(self, params):
        self._InquiryType = params.get("InquiryType")
        self._DiskChargeType = params.get("DiskChargeType")
        self._InstanceFamilies = params.get("InstanceFamilies")
        self._DiskTypes = params.get("DiskTypes")
        self._Zones = params.get("Zones")
        self._Memory = params.get("Memory")
        self._DiskUsage = params.get("DiskUsage")
        self._CPU = params.get("CPU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskConfigQuotaResponse(AbstractModel):
    """DescribeDiskConfigQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskConfigSet: 云盘配置列表。
        :type DiskConfigSet: list of DiskConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskConfigSet = None
        self._RequestId = None

    @property
    def DiskConfigSet(self):
        return self._DiskConfigSet

    @DiskConfigSet.setter
    def DiskConfigSet(self, DiskConfigSet):
        self._DiskConfigSet = DiskConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self._DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self._DiskConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskStoragePoolRequest(AbstractModel):
    """DescribeDiskStoragePool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _CdcIds: 指定需要查询的独享集群ID列表，该入参不能与Filters一起使用。
        :type CdcIds: list of str
        :param _Filters: 过滤条件。参数不支持同时指定`CdcIds`和`Filters`。<br><li>cdc-id - Array of String - 是否必填：否 -（过滤条件）按独享集群ID过滤。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按独享集群所在[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>cage-id - Array of String - 是否必填：否 -（过滤条件）按独享集群所在围笼的ID过滤。<br><li>disk-type - Array of String - 是否必填：否 -（过滤条件）按照云盘介质类型过滤。(CLOUD_BASIC：表示普通云硬盘 | CLOUD_PREMIUM：表示高性能云硬盘。| CLOUD_SSD：SSD表示SSD云硬盘。)
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        """
        self._Limit = None
        self._CdcIds = None
        self._Filters = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CdcIds(self):
        return self._CdcIds

    @CdcIds.setter
    def CdcIds(self, CdcIds):
        self._CdcIds = CdcIds

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


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._CdcIds = params.get("CdcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskStoragePoolResponse(AbstractModel):
    """DescribeDiskStoragePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的独享集群的数量
        :type TotalCount: int
        :param _CdcSet: 独享集群的详细信息列表
        :type CdcSet: list of Cdc
        :param _DiskStoragePoolSet: 独享集群的详细信息列表
        :type DiskStoragePoolSet: list of Cdc
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CdcSet = None
        self._DiskStoragePoolSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CdcSet(self):
        return self._CdcSet

    @CdcSet.setter
    def CdcSet(self, CdcSet):
        self._CdcSet = CdcSet

    @property
    def DiskStoragePoolSet(self):
        return self._DiskStoragePoolSet

    @DiskStoragePoolSet.setter
    def DiskStoragePoolSet(self, DiskStoragePoolSet):
        self._DiskStoragePoolSet = DiskStoragePoolSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CdcSet") is not None:
            self._CdcSet = []
            for item in params.get("CdcSet"):
                obj = Cdc()
                obj._deserialize(item)
                self._CdcSet.append(obj)
        if params.get("DiskStoragePoolSet") is not None:
            self._DiskStoragePoolSet = []
            for item in params.get("DiskStoragePoolSet"):
                obj = Cdc()
                obj._deserialize(item)
                self._DiskStoragePoolSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。参数不支持同时指定`DiskIds`和`Filters`。<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按云盘类型过滤。 (SYSTEM_DISK：表示系统盘 | DATA_DISK：表示数据盘)<br><li>disk-charge-type - Array of String - 是否必填：否 -（过滤条件）按照云硬盘计费模式过滤。 (PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费。)<br><li>portable - Array of String - 是否必填：否 -（过滤条件）按是否为弹性云盘过滤。 (TRUE：表示弹性云盘 | FALSE：表示非弹性云盘。)<br><li>project-id - Array of Integer - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id - Array of String - 是否必填：否 -（过滤条件）按照云硬盘ID过滤。云盘ID形如：`disk-11112222`。<br><li>disk-name - Array of String - 是否必填：否 -（过滤条件）按照云盘名称过滤。<br><li>disk-type - Array of String - 是否必填：否 -（过滤条件）按照云盘介质类型过滤。(CLOUD_BASIC：表示普通云硬盘 | CLOUD_PREMIUM：表示高性能云硬盘。| CLOUD_SSD：表示SSD云硬盘 | CLOUD_HSSD：表示增强型SSD云硬盘。| CLOUD_TSSD：表示极速型云硬盘。)<br><li>disk-state - Array of String - 是否必填：否 -（过滤条件）按照云盘状态过滤。(UNATTACHED：未挂载 | ATTACHING：挂载中 | ATTACHED：已挂载 | DETACHING：解挂中 | EXPANDING：扩容中 | ROLLBACKING：回滚中 | TORECYCLE：待回收。)<br><li>instance-id - Array of String - 是否必填：否 -（过滤条件）按照云盘挂载的云主机实例ID过滤。可根据此参数查询挂载在指定云主机下的云硬盘。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>instance-ip-address - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载云主机的内网或外网IP过滤。<br><li>instance-name - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载的实例名称过滤。<br><li>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。<br><li>tag-value - Array of String - 是否必填：否 -（过滤条件）照标签值进行过滤。<br><li>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。<br><li>dedicated-cluster-id - Array of String - 是否必填：否 -（过滤条件）按照 CDC 独享集群 ID 进行过滤。<br><li>cluster-group-id - String - 是否必填：否 -（过滤条件）按照 集群群组 ID 进行过滤。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _OrderField: 云盘列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云盘的创建时间排序<br><li>DEADLINE：依据云盘的到期时间排序<br>默认按云盘创建时间排序。
        :type OrderField: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _ReturnBindAutoSnapshotPolicy: 云盘详情中是否需要返回云盘绑定的定期快照策略ID，TRUE表示需要返回，FALSE表示不返回。
        :type ReturnBindAutoSnapshotPolicy: bool
        :param _DiskIds: 按照一个或者多个云硬盘ID查询。云硬盘ID形如：`disk-11112222`，此参数的具体格式可参考API[简介](/document/product/362/15633)的ids.N一节）。参数不支持同时指定`DiskIds`和`Filters`。
        :type DiskIds: list of str
        :param _Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        """
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._ReturnBindAutoSnapshotPolicy = None
        self._DiskIds = None
        self._Order = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ReturnBindAutoSnapshotPolicy(self):
        return self._ReturnBindAutoSnapshotPolicy

    @ReturnBindAutoSnapshotPolicy.setter
    def ReturnBindAutoSnapshotPolicy(self, ReturnBindAutoSnapshotPolicy):
        self._ReturnBindAutoSnapshotPolicy = ReturnBindAutoSnapshotPolicy

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")
        self._DiskIds = params.get("DiskIds")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的云硬盘数量。
        :type TotalCount: int
        :param _DiskSet: 云硬盘的详细信息列表。
        :type DiskSet: list of Disk
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskSet(self):
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DiskSet") is not None:
            self._DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self._DiskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 云服务器实例ID，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
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
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttachDetail: 各个云服务器已挂载和可挂载弹性云盘的数量。
        :type AttachDetail: list of AttachDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttachDetail = None
        self._RequestId = None

    @property
    def AttachDetail(self):
        return self._AttachDetail

    @AttachDetail.setter
    def AttachDetail(self, AttachDetail):
        self._AttachDetail = AttachDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AttachDetail") is not None:
            self._AttachDetail = []
            for item in params.get("AttachDetail"):
                obj = AttachDetail()
                obj._deserialize(item)
                self._AttachDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotSharePermissionRequest(AbstractModel):
    """DescribeSnapshotSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 要查询快照的ID。可通过[DescribeSnapshots](https://cloud.tencent.com/document/api/362/15647)查询获取。
        :type SnapshotId: str
        """
        self._SnapshotId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotSharePermissionResponse(AbstractModel):
    """DescribeSnapshotSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SharePermissionSet: 快照的分享信息的集合
        :type SharePermissionSet: list of SharePermission
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SharePermissionSet = None
        self._RequestId = None

    @property
    def SharePermissionSet(self):
        return self._SharePermissionSet

    @SharePermissionSet.setter
    def SharePermissionSet(self, SharePermissionSet):
        self._SharePermissionSet = SharePermissionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self._SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self._SharePermissionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要查询快照的ID列表。参数不支持同时指定`SnapshotIds`和`Filters`。
        :type SnapshotIds: list of str
        :param _Filters: 过滤条件。参数不支持同时指定`SnapshotIds`和`Filters`。<br><li>snapshot-id - Array of String - 是否必填：否 -（过滤条件）按照快照的ID过滤。快照ID形如：`snap-11112222`。<br><li>snapshot-name - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。<br><li>snapshot-state - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。 (NORMAL：正常 | CREATING：创建中 | ROLLBACKING：回滚中。)<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按创建快照的云盘类型过滤。 (SYSTEM_DISK：代表系统盘 | DATA_DISK：代表数据盘。)<br><li>project-id  - Array of String - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id  - Array of String - 是否必填：否 -（过滤条件）按照创建快照的云硬盘ID过滤。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>encrypt - Array of String - 是否必填：否 -（过滤条件）按是否加密盘快照过滤。 (TRUE：表示加密盘快照 | FALSE：表示非加密盘快照。)
<li>snapshot-type- Array of String - 是否必填：否 -（过滤条件）根据snapshot-type指定的快照类型查询对应的快照。
(SHARED_SNAPSHOT：表示共享过来的快照 | PRIVATE_SNAPSHOT：表示自己私有快照。)
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _OrderField: 快照列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据快照的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._Order = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 快照的数量。
        :type TotalCount: int
        :param _SnapshotSet: 快照的详情列表。
        :type SnapshotSet: list of Snapshot
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachDisksRequest(AbstractModel):
    """DetachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 将要卸载的云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询，单次请求最多可卸载10块弹性云盘。
        :type DiskIds: list of str
        :param _InstanceId: 对于非共享型云盘，会忽略该参数；对于共享型云盘，该参数表示要从哪个CVM实例上卸载云盘。
        :type InstanceId: str
        """
        self._DiskIds = None
        self._InstanceId = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks返回参数结构体

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


class DetailPrice(AbstractModel):
    """描述购买云盘时的费用明细。

    """

    def __init__(self):
        r"""
        :param _PriceTitle: 描述计费项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceTitle: str
        :param _PriceName: 描述计费项目显示名称，用户控制台展示。
        :type PriceName: str
        :param _OriginalPrice: 预付费云盘预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 预付费云盘预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _UnitPrice: 后付费云盘原单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceDiscount: 后付费云盘折扣单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _ChargeUnit: 后付费云盘的计价单元，取值范围：HOUR：表示后付费云盘的计价单元是按小时计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _OriginalPriceHigh: 高精度预付费云盘预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceHigh: str
        :param _DiscountPriceHigh: 高精度预付费云盘预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceHigh: str
        :param _UnitPriceHigh: 高精度后付费云盘原单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceHigh: str
        :param _UnitPriceDiscountHigh: 高精度后付费云盘折扣单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountHigh: str
        """
        self._PriceTitle = None
        self._PriceName = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._ChargeUnit = None
        self._OriginalPriceHigh = None
        self._DiscountPriceHigh = None
        self._UnitPriceHigh = None
        self._UnitPriceDiscountHigh = None

    @property
    def PriceTitle(self):
        return self._PriceTitle

    @PriceTitle.setter
    def PriceTitle(self, PriceTitle):
        self._PriceTitle = PriceTitle

    @property
    def PriceName(self):
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

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
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh


    def _deserialize(self, params):
        self._PriceTitle = params.get("PriceTitle")
        self._PriceName = params.get("PriceName")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Disk(AbstractModel):
    """描述了云硬盘的详细信息

    """

    def __init__(self):
        r"""
        :param _DeleteWithInstance: 云盘是否与挂载的实例一起销毁。<br><li>true:销毁实例时会同时销毁云盘，只支持按小时后付费云盘。<br><li>false：销毁实例时不销毁云盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param _DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_BSSD：表示通用型SSD云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :type DiskType: str
        :param _DiskState: 云盘状态。取值范围：<br><li>UNATTACHED：未挂载<br><li>ATTACHING：挂载中<br><li>ATTACHED：已挂载<br><li>DETACHING：解挂中<br><li>EXPANDING：扩容中<br><li>ROLLBACKING：回滚中<br><li>TORECYCLE：待回收<br><li>DUMPING：拷贝硬盘中。
        :type DiskState: str
        :param _SnapshotCount: 云盘拥有的快照总数。
        :type SnapshotCount: int
        :param _AutoRenewFlagError: 云盘已挂载到子机，且子机与云盘都是包年包月。<br><li>true：子机设置了自动续费标识，但云盘未设置<br><li>false：云盘自动续费标识正常。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlagError: bool
        :param _Rollbacking: 云盘是否处于快照回滚状态。取值范围：<br><li>false:表示不处于快照回滚状态<br><li>true:表示处于快照回滚状态。
        :type Rollbacking: bool
        :param _InstanceIdList: 对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
        :type InstanceIdList: list of str
        :param _Encrypt: 云盘是否为加密盘。取值范围：<br><li>false:表示非加密盘<br><li>true:表示加密盘。
        :type Encrypt: bool
        :param _DiskName: 云硬盘名称。
        :type DiskName: str
        :param _BackupDisk: 云硬盘因欠费销毁或者到期销毁时， 是否使用快照备份数据的标识。true表示销毁时创建快照进行数据备份。false表示直接销毁，不进行数据备份。
        :type BackupDisk: bool
        :param _Tags: 与云盘绑定的标签，云盘未绑定标签则取值为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceId: 云硬盘挂载的云主机ID。
        :type InstanceId: str
        :param _AttachMode: 云盘的挂载类型。取值范围：<br><li>PF: PF挂载<br><li>VF: VF挂载
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachMode: str
        :param _AutoSnapshotPolicyIds: 云盘关联的定期快照ID。只有在调用DescribeDisks接口时，入参ReturnBindAutoSnapshotPolicy取值为TRUE才会返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSnapshotPolicyIds: list of str
        :param _ThroughputPerformance: 云硬盘额外性能值，单位MB/s。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param _Migrating: 云盘是否处于类型变更中。取值范围：<br><li>false:表示云盘不处于类型变更中<br><li>true:表示云盘已发起类型变更，正处于迁移中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Migrating: bool
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _SnapshotSize: 云盘拥有的快照总容量，单位为MB。
        :type SnapshotSize: int
        :param _Placement: 云硬盘所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _IsReturnable: 判断预付费的云盘是否支持主动退还。<br><li>true:支持主动退还<br><li>false:不支持主动退还。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReturnable: bool
        :param _DeadlineTime: 云硬盘的到期时间。
        :type DeadlineTime: str
        :param _Attached: 云盘是否挂载到云主机上。取值范围：<br><li>false:表示未挂载<br><li>true:表示已挂载。
        :type Attached: bool
        :param _DiskSize: 云硬盘大小，单位GB。
        :type DiskSize: int
        :param _MigratePercent: 云盘类型变更的迁移进度，取值0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type MigratePercent: int
        :param _DiskUsage: 云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：后付费，即按量计费。
        :type DiskChargeType: str
        :param _Portable: 是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
        :type Portable: bool
        :param _SnapshotAbility: 云盘是否具备创建快照的能力。取值范围：<br><li>false表示不具备<br><li>true表示具备。
        :type SnapshotAbility: bool
        :param _DeadlineError: 在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义。<br><li>true:云盘到期时间早于实例。<br><li>false：云盘到期时间晚于实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadlineError: bool
        :param _RollbackPercent: 云盘快照回滚的进度。
        :type RollbackPercent: int
        :param _DifferDaysOfDeadline: 当前时间距离盘到期的天数（仅对预付费盘有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferDaysOfDeadline: int
        :param _ReturnFailCode: 预付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因。取值范围：<br><li>1：云硬盘已经退还<br><li>2：云硬盘已过期<br><li>3：云盘不支持退还<br><li>8：超过可退还数量的限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnFailCode: int
        :param _Shareable: 云盘是否为共享型云盘。
        :type Shareable: bool
        :param _CreateTime: 云硬盘的创建时间。
        :type CreateTime: str
        :param _DeleteSnapshot: 销毁云盘时删除关联的非永久保留快照。0 表示非永久快照不随云盘销毁而销毁，1表示非永久快照随云盘销毁而销毁，默认取0。快照是否永久保留可以通过DescribeSnapshots接口返回的快照详情的IsPermanent字段来判断，true表示永久快照，false表示非永久快照。
        :type DeleteSnapshot: int
        :param _DiskBackupQuota: 云硬盘备份点配额。表示最大可以保留的备份点数量。
        :type DiskBackupQuota: int
        :param _DiskBackupCount: 云硬盘备份点已使用的数量。
        :type DiskBackupCount: int
        :param _InstanceType: 云硬盘挂载实例的类型。取值范围：<br><li>CVM<br><li>EKS
        :type InstanceType: str
        :param _LastAttachInsId: 云硬盘最后一次挂载的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAttachInsId: str
        :param _ErrorPrompt: 云硬盘最后一次操作错误提示
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPrompt: str
        :param _BurstPerformance: 云盘是否开启性能突发
注意：此字段可能返回 null，表示取不到有效值。
        :type BurstPerformance: bool
        """
        self._DeleteWithInstance = None
        self._RenewFlag = None
        self._DiskType = None
        self._DiskState = None
        self._SnapshotCount = None
        self._AutoRenewFlagError = None
        self._Rollbacking = None
        self._InstanceIdList = None
        self._Encrypt = None
        self._DiskName = None
        self._BackupDisk = None
        self._Tags = None
        self._InstanceId = None
        self._AttachMode = None
        self._AutoSnapshotPolicyIds = None
        self._ThroughputPerformance = None
        self._Migrating = None
        self._DiskId = None
        self._SnapshotSize = None
        self._Placement = None
        self._IsReturnable = None
        self._DeadlineTime = None
        self._Attached = None
        self._DiskSize = None
        self._MigratePercent = None
        self._DiskUsage = None
        self._DiskChargeType = None
        self._Portable = None
        self._SnapshotAbility = None
        self._DeadlineError = None
        self._RollbackPercent = None
        self._DifferDaysOfDeadline = None
        self._ReturnFailCode = None
        self._Shareable = None
        self._CreateTime = None
        self._DeleteSnapshot = None
        self._DiskBackupQuota = None
        self._DiskBackupCount = None
        self._InstanceType = None
        self._LastAttachInsId = None
        self._ErrorPrompt = None
        self._BurstPerformance = None

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskState(self):
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def SnapshotCount(self):
        return self._SnapshotCount

    @SnapshotCount.setter
    def SnapshotCount(self, SnapshotCount):
        self._SnapshotCount = SnapshotCount

    @property
    def AutoRenewFlagError(self):
        return self._AutoRenewFlagError

    @AutoRenewFlagError.setter
    def AutoRenewFlagError(self, AutoRenewFlagError):
        self._AutoRenewFlagError = AutoRenewFlagError

    @property
    def Rollbacking(self):
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def BackupDisk(self):
        return self._BackupDisk

    @BackupDisk.setter
    def BackupDisk(self, BackupDisk):
        self._BackupDisk = BackupDisk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachMode(self):
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def Migrating(self):
        return self._Migrating

    @Migrating.setter
    def Migrating(self, Migrating):
        self._Migrating = Migrating

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotSize(self):
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def IsReturnable(self):
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Attached(self):
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MigratePercent(self):
        return self._MigratePercent

    @MigratePercent.setter
    def MigratePercent(self, MigratePercent):
        self._MigratePercent = MigratePercent

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Portable(self):
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def SnapshotAbility(self):
        return self._SnapshotAbility

    @SnapshotAbility.setter
    def SnapshotAbility(self, SnapshotAbility):
        self._SnapshotAbility = SnapshotAbility

    @property
    def DeadlineError(self):
        return self._DeadlineError

    @DeadlineError.setter
    def DeadlineError(self, DeadlineError):
        self._DeadlineError = DeadlineError

    @property
    def RollbackPercent(self):
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

    @property
    def DifferDaysOfDeadline(self):
        return self._DifferDaysOfDeadline

    @DifferDaysOfDeadline.setter
    def DifferDaysOfDeadline(self, DifferDaysOfDeadline):
        self._DifferDaysOfDeadline = DifferDaysOfDeadline

    @property
    def ReturnFailCode(self):
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def Shareable(self):
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def DiskBackupCount(self):
        return self._DiskBackupCount

    @DiskBackupCount.setter
    def DiskBackupCount(self, DiskBackupCount):
        self._DiskBackupCount = DiskBackupCount

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LastAttachInsId(self):
        return self._LastAttachInsId

    @LastAttachInsId.setter
    def LastAttachInsId(self, LastAttachInsId):
        self._LastAttachInsId = LastAttachInsId

    @property
    def ErrorPrompt(self):
        return self._ErrorPrompt

    @ErrorPrompt.setter
    def ErrorPrompt(self, ErrorPrompt):
        self._ErrorPrompt = ErrorPrompt

    @property
    def BurstPerformance(self):
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._RenewFlag = params.get("RenewFlag")
        self._DiskType = params.get("DiskType")
        self._DiskState = params.get("DiskState")
        self._SnapshotCount = params.get("SnapshotCount")
        self._AutoRenewFlagError = params.get("AutoRenewFlagError")
        self._Rollbacking = params.get("Rollbacking")
        self._InstanceIdList = params.get("InstanceIdList")
        self._Encrypt = params.get("Encrypt")
        self._DiskName = params.get("DiskName")
        self._BackupDisk = params.get("BackupDisk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._AttachMode = params.get("AttachMode")
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._Migrating = params.get("Migrating")
        self._DiskId = params.get("DiskId")
        self._SnapshotSize = params.get("SnapshotSize")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._IsReturnable = params.get("IsReturnable")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Attached = params.get("Attached")
        self._DiskSize = params.get("DiskSize")
        self._MigratePercent = params.get("MigratePercent")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskChargeType = params.get("DiskChargeType")
        self._Portable = params.get("Portable")
        self._SnapshotAbility = params.get("SnapshotAbility")
        self._DeadlineError = params.get("DeadlineError")
        self._RollbackPercent = params.get("RollbackPercent")
        self._DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._Shareable = params.get("Shareable")
        self._CreateTime = params.get("CreateTime")
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        self._DiskBackupCount = params.get("DiskBackupCount")
        self._InstanceType = params.get("InstanceType")
        self._LastAttachInsId = params.get("LastAttachInsId")
        self._ErrorPrompt = params.get("ErrorPrompt")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackup(AbstractModel):
    """云硬盘备份点。

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: 云硬盘备份点的ID。
        :type DiskBackupId: str
        :param _DiskId: 云硬盘备份点关联的云硬盘ID。
        :type DiskId: str
        :param _DiskSize: 云硬盘大小，单位GB。
        :type DiskSize: int
        :param _DiskUsage: 云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _DiskBackupName: 备份点名称。
        :type DiskBackupName: str
        :param _DiskBackupState: 云硬盘备份点状态。取值范围：<br><li>NORMAL：正常<br><li>CREATING：创建中<br><li>ROLLBACKING：回滚中
        :type DiskBackupState: str
        :param _Percent: 云硬盘创建进度百分比。
        :type Percent: int
        :param _CreateTime: 云硬盘备份点的创建时间。
        :type CreateTime: str
        :param _Encrypt: 云盘是否为加密盘。取值范围：<br><li>false:表示非加密盘<br><li>true:表示加密盘。
        :type Encrypt: bool
        """
        self._DiskBackupId = None
        self._DiskId = None
        self._DiskSize = None
        self._DiskUsage = None
        self._DiskBackupName = None
        self._DiskBackupState = None
        self._Percent = None
        self._CreateTime = None
        self._Encrypt = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

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
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskBackupName(self):
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName

    @property
    def DiskBackupState(self):
        return self._DiskBackupState

    @DiskBackupState.setter
    def DiskBackupState(self, DiskBackupState):
        self._DiskBackupState = DiskBackupState

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskBackupName = params.get("DiskBackupName")
        self._DiskBackupState = params.get("DiskBackupState")
        self._Percent = params.get("Percent")
        self._CreateTime = params.get("CreateTime")
        self._Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买云盘的时长，默认单位为月，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。
        :type RenewFlag: str
        :param _CurInstanceDeadline: 需要将云盘的到期时间与挂载的子机对齐时，可传入该参数。该参数表示子机当前的到期时间，此时Period如果传入，则表示子机需要续费的时长，云盘会自动按对齐到子机续费后的到期时间续费，示例取值：2018-03-30 20:15:03。
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._CurInstanceDeadline = None

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

    @property
    def CurInstanceDeadline(self):
        return self._CurInstanceDeadline

    @CurInstanceDeadline.setter
    def CurInstanceDeadline(self, CurInstanceDeadline):
        self._CurInstanceDeadline = CurInstanceDeadline


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    """云盘配置。

    """

    def __init__(self):
        r"""
        :param _Available: 配置是否可用。
        :type Available: bool
        :param _DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：表示预付费，即包年包月<br><li>POSTPAID_BY_HOUR：表示后付费，即按量计费。
        :type DiskChargeType: str
        :param _Zone: 云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。
        :type Zone: str
        :param _InstanceFamily: 实例机型系列。详见[实例类型](https://cloud.tencent.com/document/product/213/11518)
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceFamily: str
        :param _DiskType: 云盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：SSD表示SSD云硬盘。
        :type DiskType: str
        :param _StepSize: 云盘大小变化的最小步长，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type StepSize: int
        :param _ExtraPerformanceRange: 额外的性能区间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraPerformanceRange: list of int
        :param _DeviceClass: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param _DiskUsage: 云盘类型。取值范围：<br><li>SYSTEM_DISK：表示系统盘<br><li>DATA_DISK：表示数据盘。
        :type DiskUsage: str
        :param _MinDiskSize: 最小可配置云盘大小，单位GB。
        :type MinDiskSize: int
        :param _MaxDiskSize: 最大可配置云盘大小，单位GB。
        :type MaxDiskSize: int
        :param _Price: 描述预付费或后付费云盘的价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
        self._Available = None
        self._DiskChargeType = None
        self._Zone = None
        self._InstanceFamily = None
        self._DiskType = None
        self._StepSize = None
        self._ExtraPerformanceRange = None
        self._DeviceClass = None
        self._DiskUsage = None
        self._MinDiskSize = None
        self._MaxDiskSize = None
        self._Price = None

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

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

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def StepSize(self):
        return self._StepSize

    @StepSize.setter
    def StepSize(self, StepSize):
        self._StepSize = StepSize

    @property
    def ExtraPerformanceRange(self):
        return self._ExtraPerformanceRange

    @ExtraPerformanceRange.setter
    def ExtraPerformanceRange(self, ExtraPerformanceRange):
        self._ExtraPerformanceRange = ExtraPerformanceRange

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MinDiskSize(self):
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price


    def _deserialize(self, params):
        self._Available = params.get("Available")
        self._DiskChargeType = params.get("DiskChargeType")
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        self._DiskType = params.get("DiskType")
        self._StepSize = params.get("StepSize")
        self._ExtraPerformanceRange = params.get("ExtraPerformanceRange")
        self._DeviceClass = params.get("DeviceClass")
        self._DiskUsage = params.get("DiskUsage")
        self._MinDiskSize = params.get("MinDiskSize")
        self._MaxDiskSize = params.get("MaxDiskSize")
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    """

    def __init__(self):
        r"""
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _Name: 过滤键的名称。
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSnapOverviewRequest(AbstractModel):
    """GetSnapOverview请求参数结构体

    """


class GetSnapOverviewResponse(AbstractModel):
    """GetSnapOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalSize: 用户快照总大小
        :type TotalSize: float
        :param _RealTradeSize: 用户快照总大小（用于计费）
        :type RealTradeSize: float
        :param _FreeQuota: 快照免费额度
        :type FreeQuota: float
        :param _TotalNums: 快照总个数
        :type TotalNums: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalSize = None
        self._RealTradeSize = None
        self._FreeQuota = None
        self._TotalNums = None
        self._RequestId = None

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RealTradeSize(self):
        return self._RealTradeSize

    @RealTradeSize.setter
    def RealTradeSize(self, RealTradeSize):
        self._RealTradeSize = RealTradeSize

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def TotalNums(self):
        return self._TotalNums

    @TotalNums.setter
    def TotalNums(self, TotalNums):
        self._TotalNums = TotalNums

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalSize = params.get("TotalSize")
        self._RealTradeSize = params.get("RealTradeSize")
        self._FreeQuota = params.get("FreeQuota")
        self._TotalNums = params.get("TotalNums")
        self._RequestId = params.get("RequestId")


class Image(AbstractModel):
    """镜像。

    """

    def __init__(self):
        r"""
        :param _ImageName: 镜像名称。
        :type ImageName: str
        :param _ImageId: 镜像实例ID。
        :type ImageId: str
        """
        self._ImageName = None
        self._ImageId = None

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksRequest(AbstractModel):
    """InitializeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 待重新初始化的云硬盘ID列表， 单次初始化限制20块以内
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksResponse(AbstractModel):
    """InitializeDisks返回参数结构体

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


class InquirePriceModifyDiskBackupQuotaRequest(AbstractModel):
    """InquirePriceModifyDiskBackupQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID， 通过DescribeDisks（查询云硬盘信息）接口查询。
        :type DiskId: str
        :param _DiskBackupQuota: 修改后的云硬盘备份点配额，即云盘可以拥有的备份点数量，单位为个。
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskBackupQuotaResponse(AbstractModel):
    """InquirePriceModifyDiskBackupQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 描述了修改云硬盘备份点之后的云盘价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceModifyDiskExtraPerformanceRequest(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThroughputPerformance: 额外购买的云硬盘性能值，单位MB/s。
        :type ThroughputPerformance: int
        :param _DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self._ThroughputPerformance = None
        self._DiskId = None

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskExtraPerformanceResponse(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 描述了调整云盘额外性能时对应的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceCreateDisksRequest(AbstractModel):
    """InquiryPriceCreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskChargeType: 云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费
        :type DiskChargeType: str
        :param _DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :type DiskType: str
        :param _DiskSize: 云硬盘大小，单位为GB。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param _ProjectId: 云盘所属项目ID。
        :type ProjectId: int
        :param _DiskCount: 购买云盘的数量。不填则默认为1。
        :type DiskCount: int
        :param _ThroughputPerformance: 额外购买的云硬盘性能值，单位MB/s。<br>目前仅支持增强型SSD云硬盘（CLOUD_HSSD）和极速型SSD云硬盘（CLOUD_TSSD）
        :type ThroughputPerformance: int
        :param _DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DiskBackupQuota: 指定云硬盘备份点配额。
        :type DiskBackupQuota: int
        """
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskSize = None
        self._ProjectId = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._DiskChargePrepaid = None
        self._DiskBackupQuota = None

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._ProjectId = params.get("ProjectId")
        self._DiskCount = params.get("DiskCount")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDisksResponse(AbstractModel):
    """InquiryPriceCreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 描述了新购云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewDisksRequest(AbstractModel):
    """InquiryPriceRenewDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskIds: list of str
        :param _DiskChargePrepaids: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月云盘的购买时长。如果在该参数中指定CurInstanceDeadline，则会按对齐到子机到期时间来续费。如果是批量续费询价，该参数与Disks参数一一对应，元素数量需保持一致。
        :type DiskChargePrepaids: list of DiskChargePrepaid
        :param _NewDeadline: 指定云盘新的到期时间，形式如：2017-12-17 00:00:00。参数`NewDeadline`和`DiskChargePrepaids`是两种指定询价时长的方式，两者必传一个。
        :type NewDeadline: str
        :param _ProjectId: 云盘所属项目ID。 如传入则仅用于鉴权。
        :type ProjectId: int
        """
        self._DiskIds = None
        self._DiskChargePrepaids = None
        self._NewDeadline = None
        self._ProjectId = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskChargePrepaids(self):
        return self._DiskChargePrepaids

    @DiskChargePrepaids.setter
    def DiskChargePrepaids(self, DiskChargePrepaids):
        self._DiskChargePrepaids = DiskChargePrepaids

    @property
    def NewDeadline(self):
        return self._NewDeadline

    @NewDeadline.setter
    def NewDeadline(self, NewDeadline):
        self._NewDeadline = NewDeadline

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("DiskChargePrepaids") is not None:
            self._DiskChargePrepaids = []
            for item in params.get("DiskChargePrepaids"):
                obj = DiskChargePrepaid()
                obj._deserialize(item)
                self._DiskChargePrepaids.append(obj)
        self._NewDeadline = params.get("NewDeadline")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDisksResponse(AbstractModel):
    """InquiryPriceRenewDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 描述了续费云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = PrepayPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    """InquiryPriceResizeDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskSize: 云硬盘扩容后的大小，单位为GB，不得小于当前云硬盘大小。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param _DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        :param _ProjectId: 云盘所属项目ID。 如传入则仅用于鉴权。
        :type ProjectId: int
        """
        self._DiskSize = None
        self._DiskId = None
        self._ProjectId = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeDiskResponse(AbstractModel):
    """InquiryPriceResizeDisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskPrice: 描述了扩容云盘的价格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = PrepayPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class ModifyAutoSnapshotPolicyAttributeRequest(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param _IsActivated: 是否激活定期快照策略，FALSE表示未激活，TRUE表示激活，默认为TRUE。
        :type IsActivated: bool
        :param _IsPermanent: 通过该定期快照策略创建的快照是否永久保留。FALSE表示非永久保留，TRUE表示永久保留，默认为FALSE。
        :type IsPermanent: bool
        :param _AutoSnapshotPolicyName: 要创建的定期快照策略名。不传则默认为“未命名”。最大长度不能超60个字节。
        :type AutoSnapshotPolicyName: str
        :param _Policy: 定期快照的执行策略。
        :type Policy: list of Policy
        :param _RetentionDays: 通过该定期快照策略创建的快照保留天数。如果指定本参数，则IsPermanent入参不可指定为TRUE，否则会产生冲突。
        :type RetentionDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._IsActivated = None
        self._IsPermanent = None
        self._AutoSnapshotPolicyName = None
        self._Policy = None
        self._RetentionDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._IsActivated = params.get("IsActivated")
        self._IsPermanent = params.get("IsPermanent")
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._RetentionDays = params.get("RetentionDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoSnapshotPolicyAttributeResponse(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute返回参数结构体

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


class ModifyDiskAttributesRequest(AbstractModel):
    """ModifyDiskAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 一个或多个待操作的云硬盘ID。如果传入多个云盘ID，仅支持所有云盘修改为同一属性。
        :type DiskIds: list of str
        :param _DiskName: 新的云硬盘名称。
        :type DiskName: str
        :param _Portable: 是否为弹性云盘，FALSE表示非弹性云盘，TRUE表示弹性云盘。仅支持非弹性云盘修改为弹性云盘。
        :type Portable: bool
        :param _ProjectId: 新的云硬盘项目ID，只支持修改弹性云盘的项目ID。通过[DescribeProject](/document/api/378/4400)接口查询可用项目及其ID。
        :type ProjectId: int
        :param _DeleteWithInstance: 成功挂载到云主机后该云硬盘是否随云主机销毁，TRUE表示随云主机销毁，FALSE表示不随云主机销毁。仅支持按量计费云硬盘数据盘。
        :type DeleteWithInstance: bool
        :param _DiskType: 变更云盘类型时，可传入该参数，表示变更的目标类型，取值范围：<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘。<br>当前不支持批量变更类型，即传入DiskType时，DiskIds仅支持传入一块云盘；<br>变更云盘类型时不支持同时变更其他属性。
        :type DiskType: str
        :param _BurstPerformanceOperation: 开启/关闭云盘性能突发功能
        :type BurstPerformanceOperation: str
        """
        self._DiskIds = None
        self._DiskName = None
        self._Portable = None
        self._ProjectId = None
        self._DeleteWithInstance = None
        self._DiskType = None
        self._BurstPerformanceOperation = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Portable(self):
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BurstPerformanceOperation(self):
        return self._BurstPerformanceOperation

    @BurstPerformanceOperation.setter
    def BurstPerformanceOperation(self, BurstPerformanceOperation):
        self._BurstPerformanceOperation = BurstPerformanceOperation


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskName = params.get("DiskName")
        self._Portable = params.get("Portable")
        self._ProjectId = params.get("ProjectId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._DiskType = params.get("DiskType")
        self._BurstPerformanceOperation = params.get("BurstPerformanceOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskAttributesResponse(AbstractModel):
    """ModifyDiskAttributes返回参数结构体

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


class ModifyDiskBackupQuotaRequest(AbstractModel):
    """ModifyDiskBackupQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _DiskBackupQuota: 调整之后的云硬盘备份点配额。
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskBackupQuotaResponse(AbstractModel):
    """ModifyDiskBackupQuota返回参数结构体

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


class ModifyDiskExtraPerformanceRequest(AbstractModel):
    """ModifyDiskExtraPerformance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThroughputPerformance: 额外购买的云硬盘性能值，单位MB/s。
        :type ThroughputPerformance: int
        :param _DiskId: 需要创建快照的云硬盘ID，可通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self._ThroughputPerformance = None
        self._DiskId = None

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskExtraPerformanceResponse(AbstractModel):
    """ModifyDiskExtraPerformance返回参数结构体

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


class ModifyDisksChargeTypeRequest(AbstractModel):
    """ModifyDisksChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 一个或多个待操作的云硬盘ID。每次请求批量云硬盘上限为100。
        :type DiskIds: list of str
        :param _DiskChargePrepaid: 设置为预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DiskChargePostpaid: 设置为后付费模式
        :type DiskChargePostpaid: bool
        """
        self._DiskIds = None
        self._DiskChargePrepaid = None
        self._DiskChargePostpaid = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskChargePostpaid(self):
        return self._DiskChargePostpaid

    @DiskChargePostpaid.setter
    def DiskChargePostpaid(self, DiskChargePostpaid):
        self._DiskChargePostpaid = DiskChargePostpaid


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskChargePostpaid = params.get("DiskChargePostpaid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksChargeTypeResponse(AbstractModel):
    """ModifyDisksChargeType返回参数结构体

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


class ModifyDisksRenewFlagRequest(AbstractModel):
    """ModifyDisksRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 一个或多个待操作的云硬盘ID。
        :type DiskIds: list of str
        :param _RenewFlag: 云盘的续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
        :type RenewFlag: str
        """
        self._DiskIds = None
        self._RenewFlag = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksRenewFlagResponse(AbstractModel):
    """ModifyDisksRenewFlag返回参数结构体

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


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID, 可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotId: str
        :param _IsPermanent: 快照的保留方式，FALSE表示非永久保留，TRUE表示永久保留。
        :type IsPermanent: bool
        :param _SnapshotName: 新的快照名称。最长为60个字符。
        :type SnapshotName: str
        :param _Deadline: 快照的到期时间；设置好快照将会被同时设置为非永久保留方式；超过到期时间后快照将会被自动删除。
        :type Deadline: str
        """
        self._SnapshotId = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._Deadline = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute返回参数结构体

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


class ModifySnapshotsSharePermissionRequest(AbstractModel):
    """ModifySnapshotsSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 快照ID, 可通过[DescribeSnapshots](https://cloud.tencent.com/document/api/362/15647)查询获取。
        :type SnapshotIds: list of str
        :param _AccountIds: 接收分享快照的账号Id列表，array型参数的格式可以参考[API简介](https://cloud.tencent.com/document/api/213/568)。帐号ID不同于QQ号，查询用户帐号ID请查看[帐号信息](https://console.cloud.tencent.com/developer)中的帐号ID栏。
        :type AccountIds: list of str
        :param _Permission: 操作，包括 SHARE，CANCEL。其中SHARE代表分享操作，CANCEL代表取消分享操作。
        :type Permission: str
        """
        self._SnapshotIds = None
        self._AccountIds = None
        self._Permission = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        self._AccountIds = params.get("AccountIds")
        self._Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsSharePermissionResponse(AbstractModel):
    """ModifySnapshotsSharePermission返回参数结构体

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


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，以及所属的独享集群的ID和名字。

    """

    def __init__(self):
        r"""
        :param _Zone: 云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。该参数也可以通过调用  [DescribeZones](/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _CageId: 围笼Id。作为入参时，表示对指定的CageId的资源进行操作，可为空。 作为出参时，表示资源所属围笼ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _ProjectName: 实例所属项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _CdcName: 独享集群名字。作为入参时，忽略。作为出参时，表示云硬盘所属的独享集群名，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcName: str
        :param _CdcId: 实例所属的独享集群ID。作为入参时，表示对指定的CdcId独享集群的资源进行操作，可为空。 作为出参时，表示资源所属的独享集群的ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        :param _DedicatedClusterId: 独享集群id。
        :type DedicatedClusterId: str
        """
        self._Zone = None
        self._CageId = None
        self._ProjectId = None
        self._ProjectName = None
        self._CdcName = None
        self._CdcId = None
        self._DedicatedClusterId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CdcName(self):
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DedicatedClusterId(self):
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._CdcName = params.get("CdcName")
        self._CdcId = params.get("CdcId")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """描述了定期快照的执行策略。可理解为在DayOfWeek/DayOfMonth指定的几天中，或者是IntervalDays设定的间隔的几天，在Hour指定的时刻点执行该条定期快照策。注：DayOfWeek/DayOfMonth/IntervalDays为互斥规则，仅可设置其中一条策略规则。

    """

    def __init__(self):
        r"""
        :param _Hour: 指定定期快照策略的触发时间。单位为小时，取值范围：[0, 23]。00:00 ~ 23:00 共 24 个时间点可选，1表示 01:00，依此类推。
        :type Hour: list of int non-negative
        :param _DayOfWeek: 指定每周从周一到周日需要触发定期快照的日期，取值范围：[0, 6]。0表示周日触发，1-6分别表示周一至周六。
        :type DayOfWeek: list of int non-negative
        :param _DayOfMonth: 指定每月从月初到月底需要触发定期快照的日期,取值范围：[1, 31]，1-31分别表示每月的具体日期，比如5表示每月的5号。注：若设置29、30、31等部分月份不存在的日期，则对应不存在日期的月份会跳过不打定期快照。
        :type DayOfMonth: list of int non-negative
        :param _IntervalDays: 指定创建定期快照的间隔天数，取值范围：[1, 365]，例如设置为5，则间隔5天即触发定期快照创建。注：当选择按天备份时，理论上第一次备份的时间为备份策略创建当天。如果当天备份策略创建的时间已经晚于设置的备份时间，那么将会等到第二个备份周期再进行第一次备份。
        :type IntervalDays: int
        """
        self._Hour = None
        self._DayOfWeek = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._Hour = params.get("Hour")
        self._DayOfWeek = params.get("DayOfWeek")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepayPrice(AbstractModel):
    """预付费订单的费用。

    """

    def __init__(self):
        r"""
        :param _DiscountPrice: 预付费云盘或快照预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _ChargeUnit: 后付费云盘的计价单元，取值范围：<br><li>HOUR：表示后付费云盘的计价单元是按小时计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _UnitPriceHigh: 高精度后付费云盘原单价, 单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceHigh: str
        :param _OriginalPriceHigh: 高精度预付费云盘或快照预支费用的原价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceHigh: str
        :param _OriginalPrice: 预付费云盘或快照预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _UnitPriceDiscount: 后付费云盘折扣单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _UnitPriceDiscountHigh: 高精度后付费云盘折扣单价, 单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountHigh: str
        :param _DiscountPriceHigh: 高精度预付费云盘或快照预支费用的折扣价，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceHigh: str
        :param _UnitPrice: 后付费云盘原单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _DetailPrices: 计费项目明细列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailPrices: list of DetailPrice
        """
        self._DiscountPrice = None
        self._ChargeUnit = None
        self._UnitPriceHigh = None
        self._OriginalPriceHigh = None
        self._OriginalPrice = None
        self._UnitPriceDiscount = None
        self._UnitPriceDiscountHigh = None
        self._DiscountPriceHigh = None
        self._UnitPrice = None
        self._DetailPrices = None

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def DetailPrices(self):
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._DiscountPrice = params.get("DiscountPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._OriginalPrice = params.get("OriginalPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPrice = params.get("UnitPrice")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = DetailPrice()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """描述预付费或后付费云盘的价格。

    """

    def __init__(self):
        r"""
        :param _UnitPriceDiscount: 后付费云盘折扣单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _DiscountPrice: 预付费云盘预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _UnitPrice: 后付费云盘原单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceHigh: 高精度后付费云盘原单价, 单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceHigh: str
        :param _OriginalPriceHigh: 高精度预付费云盘预支费用的原价, 单位：元	。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceHigh: str
        :param _OriginalPrice: 预付费云盘预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPriceHigh: 高精度预付费云盘预支费用的折扣价, 单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceHigh: str
        :param _UnitPriceDiscountHigh: 高精度后付费云盘折扣单价, 单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountHigh: str
        :param _ChargeUnit: 后付费云盘的计价单元，取值范围：<br><li>HOUR：表示后付费云盘的计价单元是按小时计算。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        """
        self._UnitPriceDiscount = None
        self._DiscountPrice = None
        self._UnitPrice = None
        self._UnitPriceHigh = None
        self._OriginalPriceHigh = None
        self._OriginalPrice = None
        self._DiscountPriceHigh = None
        self._UnitPriceDiscountHigh = None
        self._ChargeUnit = None

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit


    def _deserialize(self, params):
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        self._ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskRequest(AbstractModel):
    """RenewDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月云硬盘的续费时长。<br>在云硬盘与挂载的实例一起续费的场景下，可以指定参数CurInstanceDeadline，此时云硬盘会按对齐到实例续费后的到期时间来续费。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self._DiskChargePrepaid = None
        self._DiskId = None

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskResponse(AbstractModel):
    """RenewDisk返回参数结构体

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


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskSize: 云硬盘扩容后的大小，单位为GB，必须大于当前云硬盘大小。云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param _DiskId: 云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询。
        :type DiskId: str
        """
        self._DiskSize = None
        self._DiskId = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk返回参数结构体

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


class SharePermission(AbstractModel):
    """快照分享信息集合

    """

    def __init__(self):
        r"""
        :param _CreatedTime: 快照分享的时间
        :type CreatedTime: str
        :param _AccountId: 分享的账号Id
        :type AccountId: str
        """
        self._CreatedTime = None
        self._AccountId = None

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._CreatedTime = params.get("CreatedTime")
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """描述了快照的详细信息

    """

    def __init__(self):
        r"""
        :param _Placement: 快照所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _CopyFromRemote: 是否为跨地域复制的快照。取值范围：<br><li>true：表示为跨地域复制的快照。<br><li>false:本地域的快照。
        :type CopyFromRemote: bool
        :param _SnapshotState: 快照的状态。取值范围：<br><li>NORMAL：正常<br><li>CREATING：创建中<br><li>ROLLBACKING：回滚中<br><li>COPYING_FROM_REMOTE：跨地域复制中<br><li>CHECKING_COPIED：复制校验中<br><li>TORECYCLE：待回收。
        :type SnapshotState: str
        :param _IsPermanent: 是否为永久快照。取值范围：<br><li>true：永久快照<br><li>false：非永久快照。
        :type IsPermanent: bool
        :param _SnapshotName: 快照名称，用户自定义的快照别名。调用[ModifySnapshotAttribute](/document/product/362/15650)可修改此字段。
        :type SnapshotName: str
        :param _DeadlineTime: 快照到期时间。如果快照为永久保留，此字段为空。
        :type DeadlineTime: str
        :param _Percent: 快照创建进度百分比，快照创建成功后此字段恒为100。
        :type Percent: int
        :param _Images: 快照关联的镜像列表。
        :type Images: list of Image
        :param _ShareReference: 快照当前被共享数。
        :type ShareReference: int
        :param _SnapshotType: 快照类型，目前该项取值可以为PRIVATE_SNAPSHOT或者SHARED_SNAPSHOT
        :type SnapshotType: str
        :param _DiskSize: 创建此快照的云硬盘大小，单位GB。
        :type DiskSize: int
        :param _DiskId: 创建此快照的云硬盘ID。
        :type DiskId: str
        :param _CopyingToRegions: 快照正在跨地域复制的目的地域，默认取值为[]。
        :type CopyingToRegions: list of str
        :param _Encrypt: 是否为加密盘创建的快照。取值范围：<br><li>true：该快照为加密盘创建的<br><li>false:非加密盘创建的快照。
        :type Encrypt: bool
        :param _CreateTime: 快照的创建时间。
        :type CreateTime: str
        :param _ImageCount: 快照关联的镜像个数。
        :type ImageCount: int
        :param _DiskUsage: 创建此快照的云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _SnapshotId: 快照ID。
        :type SnapshotId: str
        :param _TimeStartShare: 快照开始共享的时间。
        :type TimeStartShare: str
        :param _Tags: 快照绑定的标签列表。
        :type Tags: list of Tag
        """
        self._Placement = None
        self._CopyFromRemote = None
        self._SnapshotState = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._DeadlineTime = None
        self._Percent = None
        self._Images = None
        self._ShareReference = None
        self._SnapshotType = None
        self._DiskSize = None
        self._DiskId = None
        self._CopyingToRegions = None
        self._Encrypt = None
        self._CreateTime = None
        self._ImageCount = None
        self._DiskUsage = None
        self._SnapshotId = None
        self._TimeStartShare = None
        self._Tags = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CopyFromRemote(self):
        return self._CopyFromRemote

    @CopyFromRemote.setter
    def CopyFromRemote(self, CopyFromRemote):
        self._CopyFromRemote = CopyFromRemote

    @property
    def SnapshotState(self):
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Images(self):
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ShareReference(self):
        return self._ShareReference

    @ShareReference.setter
    def ShareReference(self, ShareReference):
        self._ShareReference = ShareReference

    @property
    def SnapshotType(self):
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def CopyingToRegions(self):
        return self._CopyingToRegions

    @CopyingToRegions.setter
    def CopyingToRegions(self, CopyingToRegions):
        self._CopyingToRegions = CopyingToRegions

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ImageCount(self):
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def TimeStartShare(self):
        return self._TimeStartShare

    @TimeStartShare.setter
    def TimeStartShare(self, TimeStartShare):
        self._TimeStartShare = TimeStartShare

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CopyFromRemote = params.get("CopyFromRemote")
        self._SnapshotState = params.get("SnapshotState")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Percent = params.get("Percent")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._ShareReference = params.get("ShareReference")
        self._SnapshotType = params.get("SnapshotType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        self._CopyingToRegions = params.get("CopyingToRegions")
        self._Encrypt = params.get("Encrypt")
        self._CreateTime = params.get("CreateTime")
        self._ImageCount = params.get("ImageCount")
        self._DiskUsage = params.get("DiskUsage")
        self._SnapshotId = params.get("SnapshotId")
        self._TimeStartShare = params.get("TimeStartShare")
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
        


class SnapshotCopyResult(AbstractModel):
    """描述快照跨地域复制的结果。

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 复制到目标地域的新快照ID。
        :type SnapshotId: str
        :param _Message: 指示具体错误信息，成功时为空字符串。
        :type Message: str
        :param _Code: 错误码，成功时取值为“Success”。
        :type Code: str
        :param _DestinationRegion: 跨地复制的目标地域。
        :type DestinationRegion: str
        """
        self._SnapshotId = None
        self._Message = None
        self._Code = None
        self._DestinationRegion = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def DestinationRegion(self):
        return self._DestinationRegion

    @DestinationRegion.setter
    def DestinationRegion(self, DestinationRegion):
        self._DestinationRegion = DestinationRegion


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._DestinationRegion = params.get("DestinationRegion")
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
        :param _Key: 标签健。
        :type Key: str
        :param _Value: 标签值。
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
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 需退还的云盘ID列表。
        :type DiskIds: list of str
        :param _DeleteSnapshot: 销毁云盘时删除关联的非永久保留快照。0 表示非永久快照不随云盘销毁而销毁，1表示非永久快照随云盘销毁而销毁，默认取0。快照是否永久保留可以通过DescribeSnapshots接口返回的快照详情的IsPermanent字段来判断，true表示永久快照，false表示非永久快照。
        :type DeleteSnapshot: int
        """
        self._DiskIds = None
        self._DeleteSnapshot = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks返回参数结构体

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


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 要解绑的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param _DiskIds: 要解绑定期快照策略的云盘ID列表。
        :type DiskIds: list of str
        """
        self._AutoSnapshotPolicyId = None
        self._DiskIds = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy返回参数结构体

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