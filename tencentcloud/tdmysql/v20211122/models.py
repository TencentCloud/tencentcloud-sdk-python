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


class ArchiveLogInterval(AbstractModel):
    r"""可恢复时间区间

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _MajorVersion: 大版本
注意：此字段可能返回 null，表示取不到有效值。
        :type MajorVersion: str
        :param _MinorVersion: 小版本
注意：此字段可能返回 null，表示取不到有效值。
        :type MinorVersion: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        """
        self._EndTime = None
        self._MajorVersion = None
        self._MinorVersion = None
        self._StartTime = None

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
    def MajorVersion(self):
        r"""大版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MajorVersion

    @MajorVersion.setter
    def MajorVersion(self, MajorVersion):
        self._MajorVersion = MajorVersion

    @property
    def MinorVersion(self):
        r"""小版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MinorVersion

    @MinorVersion.setter
    def MinorVersion(self, MinorVersion):
        self._MinorVersion = MinorVersion

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


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._MajorVersion = params.get("MajorVersion")
        self._MinorVersion = params.get("MinorVersion")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPolicyModelInput(AbstractModel):
    r"""修改备份策略对象

    """

    def __init__(self):
        r"""
        :param _BackupEndTime: <p>备份结束时间</p>
        :type BackupEndTime: str
        :param _BackupMethod: <p>备份方式  physical 物理备份 snapshot 快照备份</p>
        :type BackupMethod: str
        :param _BackupStartTime: <p>备份开始时间</p>
        :type BackupStartTime: str
        :param _EnableFull: <p>是否开启全量备份</p>
        :type EnableFull: int
        :param _EnableLog: <p>是否开启日志备份</p>
        :type EnableLog: int
        :param _FullRetentionPeriod: <p>全备保留时间,目前只能设置7天</p>
        :type FullRetentionPeriod: int
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _LogRetentionPeriod: <p>日志保留天数，目前只能设置保留7天</p>
        :type LogRetentionPeriod: int
        :param _PeriodTime: <p>一周的哪几天进行备份</p>
        :type PeriodTime: str
        :param _StorageType: <p>存储类型:COS,SNAPSHOT</p>枚举值：<ul><li> COS： COS存储</li><li> SNAPSHOT： 云盘快照</li></ul>
        :type StorageType: str
        """
        self._BackupEndTime = None
        self._BackupMethod = None
        self._BackupStartTime = None
        self._EnableFull = None
        self._EnableLog = None
        self._FullRetentionPeriod = None
        self._InstanceId = None
        self._LogRetentionPeriod = None
        self._PeriodTime = None
        self._StorageType = None

    @property
    def BackupEndTime(self):
        r"""<p>备份结束时间</p>
        :rtype: str
        """
        return self._BackupEndTime

    @BackupEndTime.setter
    def BackupEndTime(self, BackupEndTime):
        self._BackupEndTime = BackupEndTime

    @property
    def BackupMethod(self):
        r"""<p>备份方式  physical 物理备份 snapshot 快照备份</p>
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStartTime(self):
        r"""<p>备份开始时间</p>
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def EnableFull(self):
        r"""<p>是否开启全量备份</p>
        :rtype: int
        """
        return self._EnableFull

    @EnableFull.setter
    def EnableFull(self, EnableFull):
        self._EnableFull = EnableFull

    @property
    def EnableLog(self):
        r"""<p>是否开启日志备份</p>
        :rtype: int
        """
        return self._EnableLog

    @EnableLog.setter
    def EnableLog(self, EnableLog):
        self._EnableLog = EnableLog

    @property
    def FullRetentionPeriod(self):
        r"""<p>全备保留时间,目前只能设置7天</p>
        :rtype: int
        """
        return self._FullRetentionPeriod

    @FullRetentionPeriod.setter
    def FullRetentionPeriod(self, FullRetentionPeriod):
        self._FullRetentionPeriod = FullRetentionPeriod

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
    def LogRetentionPeriod(self):
        r"""<p>日志保留天数，目前只能设置保留7天</p>
        :rtype: int
        """
        return self._LogRetentionPeriod

    @LogRetentionPeriod.setter
    def LogRetentionPeriod(self, LogRetentionPeriod):
        self._LogRetentionPeriod = LogRetentionPeriod

    @property
    def PeriodTime(self):
        r"""<p>一周的哪几天进行备份</p>
        :rtype: str
        """
        return self._PeriodTime

    @PeriodTime.setter
    def PeriodTime(self, PeriodTime):
        self._PeriodTime = PeriodTime

    @property
    def StorageType(self):
        r"""<p>存储类型:COS,SNAPSHOT</p>枚举值：<ul><li> COS： COS存储</li><li> SNAPSHOT： 云盘快照</li></ul>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._BackupEndTime = params.get("BackupEndTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStartTime = params.get("BackupStartTime")
        self._EnableFull = params.get("EnableFull")
        self._EnableLog = params.get("EnableLog")
        self._FullRetentionPeriod = params.get("FullRetentionPeriod")
        self._InstanceId = params.get("InstanceId")
        self._LogRetentionPeriod = params.get("LogRetentionPeriod")
        self._PeriodTime = params.get("PeriodTime")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIsolateDBInstancesRequest(AbstractModel):
    r"""CancelIsolateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要隔离的实例ID列表
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""需要隔离的实例ID列表
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
        


class CancelIsolateDBInstancesResponse(AbstractModel):
    r"""CancelIsolateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 解除隔离成功实例Id列表
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 解除隔离失败实例Id列表
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""解除隔离成功实例Id列表
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""解除隔离失败实例Id列表
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class CloneInstanceModel(AbstractModel):
    r"""克隆实例对象

    """

    def __init__(self):
        r"""
        :param _CloneEndTime: 克隆任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneEndTime: str
        :param _CloneId: 克隆记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneId: int
        :param _CloneInsType: 克隆实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneInsType: str
        :param _CloneInstanceId: 克隆实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneInstanceId: str
        :param _CloneInstanceIsDeleted: 克隆实例是否已经删除
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneInstanceIsDeleted: bool
        :param _CloneProgress: 克隆任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneProgress: float
        :param _CloneStartTime: 克隆任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneStartTime: str
        :param _CloneStatus: 克隆任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneStatus: str
        :param _CloneTime: 克隆时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneTime: str
        :param _CloneType: 克隆类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CloneType: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DBType: 引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DBType: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _SourceInstanceId: 源实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceInstanceId: str
        """
        self._CloneEndTime = None
        self._CloneId = None
        self._CloneInsType = None
        self._CloneInstanceId = None
        self._CloneInstanceIsDeleted = None
        self._CloneProgress = None
        self._CloneStartTime = None
        self._CloneStatus = None
        self._CloneTime = None
        self._CloneType = None
        self._CreateTime = None
        self._DBType = None
        self._Region = None
        self._SourceInstanceId = None

    @property
    def CloneEndTime(self):
        r"""克隆任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneEndTime

    @CloneEndTime.setter
    def CloneEndTime(self, CloneEndTime):
        self._CloneEndTime = CloneEndTime

    @property
    def CloneId(self):
        r"""克隆记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CloneId

    @CloneId.setter
    def CloneId(self, CloneId):
        self._CloneId = CloneId

    @property
    def CloneInsType(self):
        r"""克隆实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneInsType

    @CloneInsType.setter
    def CloneInsType(self, CloneInsType):
        self._CloneInsType = CloneInsType

    @property
    def CloneInstanceId(self):
        r"""克隆实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneInstanceId

    @CloneInstanceId.setter
    def CloneInstanceId(self, CloneInstanceId):
        self._CloneInstanceId = CloneInstanceId

    @property
    def CloneInstanceIsDeleted(self):
        r"""克隆实例是否已经删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CloneInstanceIsDeleted

    @CloneInstanceIsDeleted.setter
    def CloneInstanceIsDeleted(self, CloneInstanceIsDeleted):
        self._CloneInstanceIsDeleted = CloneInstanceIsDeleted

    @property
    def CloneProgress(self):
        r"""克隆任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CloneProgress

    @CloneProgress.setter
    def CloneProgress(self, CloneProgress):
        self._CloneProgress = CloneProgress

    @property
    def CloneStartTime(self):
        r"""克隆任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneStartTime

    @CloneStartTime.setter
    def CloneStartTime(self, CloneStartTime):
        self._CloneStartTime = CloneStartTime

    @property
    def CloneStatus(self):
        r"""克隆任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneStatus

    @CloneStatus.setter
    def CloneStatus(self, CloneStatus):
        self._CloneStatus = CloneStatus

    @property
    def CloneTime(self):
        r"""克隆时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneTime

    @CloneTime.setter
    def CloneTime(self, CloneTime):
        self._CloneTime = CloneTime

    @property
    def CloneType(self):
        r"""克隆类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloneType

    @CloneType.setter
    def CloneType(self, CloneType):
        self._CloneType = CloneType

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DBType(self):
        r"""引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

    @property
    def Region(self):
        r"""地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceInstanceId(self):
        r"""源实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId


    def _deserialize(self, params):
        self._CloneEndTime = params.get("CloneEndTime")
        self._CloneId = params.get("CloneId")
        self._CloneInsType = params.get("CloneInsType")
        self._CloneInstanceId = params.get("CloneInstanceId")
        self._CloneInstanceIsDeleted = params.get("CloneInstanceIsDeleted")
        self._CloneProgress = params.get("CloneProgress")
        self._CloneStartTime = params.get("CloneStartTime")
        self._CloneStatus = params.get("CloneStatus")
        self._CloneTime = params.get("CloneTime")
        self._CloneType = params.get("CloneType")
        self._CreateTime = params.get("CreateTime")
        self._DBType = params.get("DBType")
        self._Region = params.get("Region")
        self._SourceInstanceId = params.get("SourceInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    r"""约束类型值的范围

    """

    def __init__(self):
        r"""
        :param _Min: 约束类型为section时的最小值
        :type Min: str
        :param _Max: 约束类型为section时的最大值
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        r"""约束类型为section时的最小值
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""约束类型为section时的最大值
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBSBackupRequest(AbstractModel):
    r"""CreateDBSBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>备份方式：physical、snapshot 这个值和DescribeDBSBackupPolicy接口返回的backupMethod保持一致</p>枚举值：<ul><li> physical： 物理备份</li><li> snapshot： 快照备份</li></ul>
        :type BackupMethod: str
        :param _BackupType: <p>备份类型：暂时只支持full</p>
        :type BackupType: str
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _BackupName: <p>备份备注</p>
        :type BackupName: str
        """
        self._BackupMethod = None
        self._BackupType = None
        self._InstanceId = None
        self._BackupName = None

    @property
    def BackupMethod(self):
        r"""<p>备份方式：physical、snapshot 这个值和DescribeDBSBackupPolicy接口返回的backupMethod保持一致</p>枚举值：<ul><li> physical： 物理备份</li><li> snapshot： 快照备份</li></ul>
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupType(self):
        r"""<p>备份类型：暂时只支持full</p>
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

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
    def BackupName(self):
        r"""<p>备份备注</p>
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._BackupMethod = params.get("BackupMethod")
        self._BackupType = params.get("BackupType")
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBSBackupResponse(AbstractModel):
    r"""CreateDBSBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupSetId: <p>备份集ID</p>
        :type BackupSetId: int
        :param _IsSuccess: <p>是否成功</p>
        :type IsSuccess: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupSetId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def BackupSetId(self):
        r"""<p>备份集ID</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def IsSuccess(self):
        r"""<p>是否成功</p>
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

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
        self._BackupSetId = params.get("BackupSetId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class DBParamValue(AbstractModel):
    r"""云数据库参数信息。

    """

    def __init__(self):
        r"""
        :param _Param: 参数名称
        :type Param: str
        :param _Value: 参数值
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        r"""参数名称
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    r"""数据库函数信息

    """

    def __init__(self):
        r"""
        :param _Func: 函数名称
        :type Func: str
        """
        self._Func = None

    @property
    def Func(self):
        r"""函数名称
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    r"""数据库存储过程信息

    """

    def __init__(self):
        r"""
        :param _Proc: 存储过程名称
        :type Proc: str
        """
        self._Proc = None

    @property
    def Proc(self):
        r"""存储过程名称
        :rtype: str
        """
        return self._Proc

    @Proc.setter
    def Proc(self, Proc):
        self._Proc = Proc


    def _deserialize(self, params):
        self._Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    r"""数据库表信息

    """

    def __init__(self):
        r"""
        :param _Table: 表名
        :type Table: str
        """
        self._Table = None

    @property
    def Table(self):
        r"""表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    r"""数据库视图信息

    """

    def __init__(self):
        r"""
        :param _View: 视图名称
        :type View: str
        """
        self._View = None

    @property
    def View(self):
        r"""视图名称
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View


    def _deserialize(self, params):
        self._View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBSBackupSetsRequest(AbstractModel):
    r"""DeleteDBSBackupSets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _BackupSetIdList: <p>备份集列表 ,值来自 DescribeDBSBackupSets 接口返回</p>
        :type BackupSetIdList: list of int
        """
        self._InstanceId = None
        self._BackupSetIdList = None

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
    def BackupSetIdList(self):
        r"""<p>备份集列表 ,值来自 DescribeDBSBackupSets 接口返回</p>
        :rtype: list of int
        """
        return self._BackupSetIdList

    @BackupSetIdList.setter
    def BackupSetIdList(self, BackupSetIdList):
        self._BackupSetIdList = BackupSetIdList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetIdList = params.get("BackupSetIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBSBackupSetsResponse(AbstractModel):
    r"""DeleteDBSBackupSets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deleted: <p>本次实际删除的备份数量</p>
        :type Deleted: int
        :param _IsSuccess: <p>是否全部删除成功</p>
        :type IsSuccess: bool
        :param _Total: <p>需要删除的备份总数</p>
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deleted = None
        self._IsSuccess = None
        self._Total = None
        self._RequestId = None

    @property
    def Deleted(self):
        r"""<p>本次实际删除的备份数量</p>
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def IsSuccess(self):
        r"""<p>是否全部删除成功</p>
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Total(self):
        r"""<p>需要删除的备份总数</p>
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
        self._Deleted = params.get("Deleted")
        self._IsSuccess = params.get("IsSuccess")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillingEnableRequest(AbstractModel):
    r"""DescribeBillingEnable请求参数结构体

    """


class DescribeBillingEnableResponse(AbstractModel):
    r"""DescribeBillingEnable返回参数结构体

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


class DescribeDBParametersRequest(AbstractModel):
    r"""DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-ow728lmc。
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
        


class DescribeDBParametersResponse(AbstractModel):
    r"""DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-ow728lmc。
        :type InstanceId: str
        :param _Params: 请求实例的当前参数值
        :type Params: list of ParamDesc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Params = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        r"""请求实例的当前参数值
        :rtype: list of ParamDesc
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self._Params.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>db实例ID</p>
        :type InstanceId: str
        :param _BackupSetId: <p>备份集ID,值来自 DescribeDBSBackupSets 接口返回</p>
        :type BackupSetId: int
        """
        self._InstanceId = None
        self._BackupSetId = None

    @property
    def InstanceId(self):
        r"""<p>db实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupSetId(self):
        r"""<p>备份集ID,值来自 DescribeDBSBackupSets 接口返回</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSAvailableRecoveryTimeResponse(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: <p>结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Intervals: <p>可恢复时间区间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Intervals: list of ArchiveLogInterval
        :param _StartTime: <p>开始时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EndTime = None
        self._Intervals = None
        self._StartTime = None
        self._RequestId = None

    @property
    def EndTime(self):
        r"""<p>结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Intervals(self):
        r"""<p>可恢复时间区间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ArchiveLogInterval
        """
        return self._Intervals

    @Intervals.setter
    def Intervals(self, Intervals):
        self._Intervals = Intervals

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

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
        self._EndTime = params.get("EndTime")
        if params.get("Intervals") is not None:
            self._Intervals = []
            for item in params.get("Intervals"):
                obj = ArchiveLogInterval()
                obj._deserialize(item)
                self._Intervals.append(obj)
        self._StartTime = params.get("StartTime")
        self._RequestId = params.get("RequestId")


class DescribeDBSCloneInstancesRequest(AbstractModel):
    r"""DescribeDBSCloneInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceInstanceId: <p>源实例ID</p>
        :type SourceInstanceId: str
        :param _DBType: <p>引擎类型</p>
        :type DBType: str
        :param _EndCreateTime: <p>结束创建时间</p>
        :type EndCreateTime: str
        :param _FilterCloneType: <p>克隆类型: PITR 时间点 BackupSet 备份集</p>
        :type FilterCloneType: str
        :param _Limit: <p>查询数量[0,200]</p>
        :type Limit: int
        :param _Offset: <p>查询偏移量[0,INF]</p>
        :type Offset: int
        :param _OrderBy: <p>排序字段: CloneTime,CreateTime</p>
        :type OrderBy: str
        :param _OrderType: <p>排序类型:ASC,DESC</p>
        :type OrderType: str
        :param _StartCreateTime: <p>开始创建时间</p>
        :type StartCreateTime: str
        """
        self._SourceInstanceId = None
        self._DBType = None
        self._EndCreateTime = None
        self._FilterCloneType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartCreateTime = None

    @property
    def SourceInstanceId(self):
        r"""<p>源实例ID</p>
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def DBType(self):
        r"""<p>引擎类型</p>
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

    @property
    def EndCreateTime(self):
        r"""<p>结束创建时间</p>
        :rtype: str
        """
        return self._EndCreateTime

    @EndCreateTime.setter
    def EndCreateTime(self, EndCreateTime):
        self._EndCreateTime = EndCreateTime

    @property
    def FilterCloneType(self):
        r"""<p>克隆类型: PITR 时间点 BackupSet 备份集</p>
        :rtype: str
        """
        return self._FilterCloneType

    @FilterCloneType.setter
    def FilterCloneType(self, FilterCloneType):
        self._FilterCloneType = FilterCloneType

    @property
    def Limit(self):
        r"""<p>查询数量[0,200]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>查询偏移量[0,INF]</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>排序字段: CloneTime,CreateTime</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>排序类型:ASC,DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartCreateTime(self):
        r"""<p>开始创建时间</p>
        :rtype: str
        """
        return self._StartCreateTime

    @StartCreateTime.setter
    def StartCreateTime(self, StartCreateTime):
        self._StartCreateTime = StartCreateTime


    def _deserialize(self, params):
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._DBType = params.get("DBType")
        self._EndCreateTime = params.get("EndCreateTime")
        self._FilterCloneType = params.get("FilterCloneType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartCreateTime = params.get("StartCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSCloneInstancesResponse(AbstractModel):
    r"""DescribeDBSCloneInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: <p>克隆列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of CloneInstanceModel
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        r"""<p>克隆列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CloneInstanceModel
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""<p>总数</p>
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CloneInstanceModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID。
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    r"""DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param _VIP: 实例VIP
注意：此字段可能返回 null，表示取不到有效值。
        :type VIP: str
        :param _VPort: 实例端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        r"""安全组详情。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        r"""实例VIP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        r"""实例端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    r"""DescribeDatabaseObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-42f40429.
        :type InstanceId: str
        :param _DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-42f40429.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""数据库名称，通过 DescribeDatabases 接口获取。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    r"""DescribeDatabaseObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 透传入参。
        :type InstanceId: str
        :param _DbName: 数据库名称。
        :type DbName: str
        :param _Tables: 表列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of DatabaseTable
        :param _Views: 视图列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of DatabaseView
        :param _Procs: 存储过程列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Procs: list of DatabaseProcedure
        :param _Funcs: 函数列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Funcs: list of DatabaseFunction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Tables = None
        self._Views = None
        self._Procs = None
        self._Funcs = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""透传入参。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""数据库名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        r"""表列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        r"""视图列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        r"""存储过程列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        r"""函数列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseFunction
        """
        return self._Funcs

    @Funcs.setter
    def Funcs(self, Funcs):
        self._Funcs = Funcs

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
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self._Views.append(obj)
        if params.get("Procs") is not None:
            self._Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self._Procs.append(obj)
        if params.get("Funcs") is not None:
            self._Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self._Funcs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    r"""DescribeDatabaseTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-ow7t8lmc。
        :type InstanceId: str
        :param _DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        :param _Table: 表名称，通过 DescribeDatabaseObjects 接口获取。
        :type Table: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""数据库名称，通过 DescribeDatabases 接口获取。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        r"""表名称，通过 DescribeDatabaseObjects 接口获取。
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    r"""DescribeDatabaseTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称。
        :type InstanceId: str
        :param _DbName: 数据库名称。
        :type DbName: str
        :param _Table: 表名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Cols: 列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cols: list of TableColumn
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None
        self._Cols = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例名称。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""数据库名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        r"""表名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Cols(self):
        r"""列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TableColumn
        """
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

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
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        if params.get("Cols") is not None:
            self._Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Cols.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    r"""DescribeFlow请求参数结构体

    """


class DescribeFlowResponse(AbstractModel):
    r"""DescribeFlow返回参数结构体

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


class DestroyInstancesRequest(AbstractModel):
    r"""DestroyInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要隔离的实例ID列表
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""需要隔离的实例ID列表
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
        


class DestroyInstancesResponse(AbstractModel):
    r"""DestroyInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 解除隔离成功实例Id列表
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 解除隔离失败实例Id列表
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""解除隔离成功实例Id列表
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""解除隔离失败实例Id列表
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class IsolateDBInstanceRequest(AbstractModel):
    r"""IsolateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要隔离的实例ID列表
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""需要隔离的实例ID列表
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
        


class IsolateDBInstanceResponse(AbstractModel):
    r"""IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 隔离成功实例Id列表
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 隔离失败实例Id列表
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""隔离成功实例Id列表
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""隔离失败实例Id列表
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    r"""ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要修改的实例列表
        :type InstanceIds: list of str
        :param _AutoRenewFlag: 1表示开启自动续费，0为关闭自动续费
        :type AutoRenewFlag: int
        """
        self._InstanceIds = None
        self._AutoRenewFlag = None

    @property
    def InstanceIds(self):
        r"""需要修改的实例列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenewFlag(self):
        r"""1表示开启自动续费，0为关闭自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    r"""ModifyAutoRenewFlag返回参数结构体

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


class ModifyBinlogStatusRequest(AbstractModel):
    r"""ModifyBinlogStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Status: 1打开0关闭
        :type Status: int
        """
        self._InstanceId = None
        self._Status = None

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
        r"""1打开0关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBinlogStatusResponse(AbstractModel):
    r"""ModifyBinlogStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: flow的流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""flow的流程id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None

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
    def SecurityGroupIds(self):
        r"""要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups返回参数结构体

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


class ModifyDBParametersRequest(AbstractModel):
    r"""ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-ow728lmc。
        :type InstanceId: str
        :param _Params: 参数列表，每一个元素是Param和Value的组合
        :type Params: list of DBParamValue
        """
        self._InstanceId = None
        self._Params = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        r"""参数列表，每一个元素是Param和Value的组合
        :rtype: list of DBParamValue
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    r"""ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 123
        :type TaskID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._RequestId = None

    @property
    def TaskID(self):
        r"""123
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

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
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class ModifyDBSBackupPolicyRequest(AbstractModel):
    r"""ModifyDBSBackupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPolicy: 备份策略
        :type BackupPolicy: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._BackupPolicy = None
        self._InstanceId = None

    @property
    def BackupPolicy(self):
        r"""备份策略
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        """
        return self._BackupPolicy

    @BackupPolicy.setter
    def BackupPolicy(self, BackupPolicy):
        self._BackupPolicy = BackupPolicy

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("BackupPolicy") is not None:
            self._BackupPolicy = BackupPolicyModelInput()
            self._BackupPolicy._deserialize(params.get("BackupPolicy"))
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSBackupPolicyResponse(AbstractModel):
    r"""ModifyDBSBackupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否成功
        :type IsSuccess: bool
        :param _Msg: 消息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._Msg = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        r"""是否成功
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Msg(self):
        r"""消息
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
        self._IsSuccess = params.get("IsSuccess")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyDBSBackupSetCommentRequest(AbstractModel):
    r"""ModifyDBSBackupSetComment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _BackupSetId: <p>备份集ID,值来自 DescribeDBSBackupSets 接口返回</p>
        :type BackupSetId: int
        :param _NewBackupName: <p>备份备注</p>
        :type NewBackupName: str
        """
        self._InstanceId = None
        self._BackupSetId = None
        self._NewBackupName = None

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
    def BackupSetId(self):
        r"""<p>备份集ID,值来自 DescribeDBSBackupSets 接口返回</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def NewBackupName(self):
        r"""<p>备份备注</p>
        :rtype: str
        """
        return self._NewBackupName

    @NewBackupName.setter
    def NewBackupName(self, NewBackupName):
        self._NewBackupName = NewBackupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._NewBackupName = params.get("NewBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSBackupSetCommentResponse(AbstractModel):
    r"""ModifyDBSBackupSetComment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: <p>是否成功</p>
        :type IsSuccess: bool
        :param _Msg: <p>修改信息</p>
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._Msg = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        r"""<p>是否成功</p>
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Msg(self):
        r"""<p>修改信息</p>
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
        self._IsSuccess = params.get("IsSuccess")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyInstanceNameRequest(AbstractModel):
    r"""ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要修改的实例id
        :type InstanceId: str
        :param _InstanceName: 修改的实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""需要修改的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""修改的实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    r"""ModifyInstanceName返回参数结构体

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


class ParamConstraint(AbstractModel):
    r"""参数约束

    """

    def __init__(self):
        r"""
        :param _Type: 约束类型,如枚举enum，区间section
        :type Type: str
        :param _Enum: 约束类型为enum时的可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Enum: str
        :param _Range: 约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.tdmysql.v20211122.models.ConstraintRange`
        :param _String: 约束类型为string时的可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type String: str
        """
        self._Type = None
        self._Enum = None
        self._Range = None
        self._String = None

    @property
    def Type(self):
        r"""约束类型,如枚举enum，区间section
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enum(self):
        r"""约束类型为enum时的可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Range(self):
        r"""约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ConstraintRange`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def String(self):
        r"""约束类型为string时的可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Enum = params.get("Enum")
        if params.get("Range") is not None:
            self._Range = ConstraintRange()
            self._Range._deserialize(params.get("Range"))
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    r"""DB参数描述

    """

    def __init__(self):
        r"""
        :param _Param: 参数名字
        :type Param: str
        :param _Value: 当前参数值
        :type Value: str
        :param _SetValue: 设置过的值，参数生效后，该值和value一样。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetValue: str
        :param _Default: 系统默认值
        :type Default: str
        :param _Constraint: 参数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type Constraint: :class:`tencentcloud.tdmysql.v20211122.models.ParamConstraint`
        :param _HaveSetValue: 是否有设置过值，false:没有设置过值，true:有设置过值。
        :type HaveSetValue: bool
        :param _NeedRestart: true:需要重启
        :type NeedRestart: bool
        :param _Description: 参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Param = None
        self._Value = None
        self._SetValue = None
        self._Default = None
        self._Constraint = None
        self._HaveSetValue = None
        self._NeedRestart = None
        self._Description = None

    @property
    def Param(self):
        r"""参数名字
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""当前参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SetValue(self):
        r"""设置过的值，参数生效后，该值和value一样。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SetValue

    @SetValue.setter
    def SetValue(self, SetValue):
        self._SetValue = SetValue

    @property
    def Default(self):
        r"""系统默认值
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        r"""参数限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ParamConstraint`
        """
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint

    @property
    def HaveSetValue(self):
        r"""是否有设置过值，false:没有设置过值，true:有设置过值。
        :rtype: bool
        """
        return self._HaveSetValue

    @HaveSetValue.setter
    def HaveSetValue(self, HaveSetValue):
        self._HaveSetValue = HaveSetValue

    @property
    def NeedRestart(self):
        r"""true:需要重启
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def Description(self):
        r"""参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        self._SetValue = params.get("SetValue")
        self._Default = params.get("Default")
        if params.get("Constraint") is not None:
            self._Constraint = ParamConstraint()
            self._Constraint._deserialize(params.get("Constraint"))
        self._HaveSetValue = params.get("HaveSetValue")
        self._NeedRestart = params.get("NeedRestart")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    r"""安全组详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        :param _Inbound: 入站规则
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: 出站规则
        :type Outbound: list of SecurityGroupBound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Inbound = None
        self._Outbound = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        r"""安全组ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""安全组名称
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""安全组备注
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Inbound(self):
        r"""入站规则
        :rtype: list of SecurityGroupBound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        r"""出站规则
        :rtype: list of SecurityGroupBound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    r"""安全出入口规则

    """

    def __init__(self):
        r"""
        :param _CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _PortRange: 端口
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        """
        self._CidrIp = None
        self._Action = None
        self._PortRange = None
        self._IpProtocol = None

    @property
    def CidrIp(self):
        r"""来源 IP 或 IP 段，例如192.168.0.0/16
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Action(self):
        r"""策略，ACCEPT 或者 DROP
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PortRange(self):
        r"""端口
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""网络协议，支持 UDP、TCP 等
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol


    def _deserialize(self, params):
        self._CidrIp = params.get("CidrIp")
        self._Action = params.get("Action")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    r"""数据库列信息

    """

    def __init__(self):
        r"""
        :param _Col: 列名称
        :type Col: str
        :param _Type: 列类型
        :type Type: str
        """
        self._Col = None
        self._Type = None

    @property
    def Col(self):
        r"""列名称
        :rtype: str
        """
        return self._Col

    @Col.setter
    def Col(self, Col):
        self._Col = Col

    @property
    def Type(self):
        r"""列类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Col = params.get("Col")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        