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


class AnalysisInstanceInfo(AbstractModel):
    r"""分析引擎实例信息

    """

    def __init__(self):
        r"""
        :param _ReplicasNum: <p>副本数</p>
        :type ReplicasNum: int
        """
        self._ReplicasNum = None

    @property
    def ReplicasNum(self):
        r"""<p>副本数</p>
        :rtype: int
        """
        return self._ReplicasNum

    @ReplicasNum.setter
    def ReplicasNum(self, ReplicasNum):
        self._ReplicasNum = ReplicasNum


    def _deserialize(self, params):
        self._ReplicasNum = params.get("ReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisRelationInfo(AbstractModel):
    r"""分析引擎关联关系

    """

    def __init__(self):
        r"""
        :param _PrimaryInstanceId: <p>源实例Id</p>
        :type PrimaryInstanceId: str
        :param _AnalysisInstanceId: <p>分析引擎实例Id</p>
        :type AnalysisInstanceId: str
        :param _Status: <p>分析引擎关系状态</p><p>枚举值：</p><ul><li>creating： 创建中</li><li>running： 运行中</li><li>destroyed： 已销毁</li></ul>
        :type Status: str
        :param _CreateAt: <p>创建时间</p>
        :type CreateAt: str
        :param _UpdateAt: <p>更新时间</p>
        :type UpdateAt: str
        """
        self._PrimaryInstanceId = None
        self._AnalysisInstanceId = None
        self._Status = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PrimaryInstanceId(self):
        r"""<p>源实例Id</p>
        :rtype: str
        """
        return self._PrimaryInstanceId

    @PrimaryInstanceId.setter
    def PrimaryInstanceId(self, PrimaryInstanceId):
        self._PrimaryInstanceId = PrimaryInstanceId

    @property
    def AnalysisInstanceId(self):
        r"""<p>分析引擎实例Id</p>
        :rtype: str
        """
        return self._AnalysisInstanceId

    @AnalysisInstanceId.setter
    def AnalysisInstanceId(self, AnalysisInstanceId):
        self._AnalysisInstanceId = AnalysisInstanceId

    @property
    def Status(self):
        r"""<p>分析引擎关系状态</p><p>枚举值：</p><ul><li>creating： 创建中</li><li>running： 运行中</li><li>destroyed： 已销毁</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PrimaryInstanceId = params.get("PrimaryInstanceId")
        self._AnalysisInstanceId = params.get("AnalysisInstanceId")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ArchiveLogModel(AbstractModel):
    r"""归档日志对象

    """

    def __init__(self):
        r"""
        :param _ArchiveLogId: 归档日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchiveLogId: int
        :param _BackupDuration: 备份耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupDuration: int
        :param _BackupStatus: 备份集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: str
        :param _EndTime: 备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _ExpiredTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _FileName: 备份文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 备份集文件大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _StartTime: 备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        """
        self._ArchiveLogId = None
        self._BackupDuration = None
        self._BackupStatus = None
        self._EndTime = None
        self._ErrorMessage = None
        self._ExpiredTime = None
        self._FileName = None
        self._FileSize = None
        self._InstanceId = None
        self._StartTime = None

    @property
    def ArchiveLogId(self):
        r"""归档日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ArchiveLogId

    @ArchiveLogId.setter
    def ArchiveLogId(self, ArchiveLogId):
        self._ArchiveLogId = ArchiveLogId

    @property
    def BackupDuration(self):
        r"""备份耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupDuration

    @BackupDuration.setter
    def BackupDuration(self, BackupDuration):
        self._BackupDuration = BackupDuration

    @property
    def BackupStatus(self):
        r"""备份集状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def EndTime(self):
        r"""备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ErrorMessage(self):
        r"""错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ExpiredTime(self):
        r"""过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FileName(self):
        r"""备份文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""备份集文件大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def InstanceId(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._ArchiveLogId = params.get("ArchiveLogId")
        self._BackupDuration = params.get("BackupDuration")
        self._BackupStatus = params.get("BackupStatus")
        self._EndTime = params.get("EndTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingConfig(AbstractModel):
    r"""serverless实例的ccu范围

    """

    def __init__(self):
        r"""
        :param _RangeMin: <p>ccu最小值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeMin: float
        :param _RangeMax: <p>ccu最大值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeMax: float
        """
        self._RangeMin = None
        self._RangeMax = None

    @property
    def RangeMin(self):
        r"""<p>ccu最小值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RangeMin

    @RangeMin.setter
    def RangeMin(self, RangeMin):
        self._RangeMin = RangeMin

    @property
    def RangeMax(self):
        r"""<p>ccu最大值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RangeMax

    @RangeMax.setter
    def RangeMax(self, RangeMax):
        self._RangeMax = RangeMax


    def _deserialize(self, params):
        self._RangeMin = params.get("RangeMin")
        self._RangeMax = params.get("RangeMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupMethodStatisticsModel(AbstractModel):
    r"""备份方式统计对象-提供给备份空间统计接口

    """

    def __init__(self):
        r"""
        :param _AutoBackupSize: <p>自动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupSize: int
        :param _AverageSizePerDay: <p>总备份每天平均大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerDay: int
        :param _ManualBackupSize: <p>手动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackupSize: int
        :param _TotalSize: <p>总备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self._AutoBackupSize = None
        self._AverageSizePerDay = None
        self._ManualBackupSize = None
        self._TotalSize = None

    @property
    def AutoBackupSize(self):
        r"""<p>自动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def AverageSizePerDay(self):
        r"""<p>总备份每天平均大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def ManualBackupSize(self):
        r"""<p>手动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize

    @property
    def TotalSize(self):
        r"""<p>总备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._ManualBackupSize = params.get("ManualBackupSize")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupMethodStatisticsOutPut(AbstractModel):
    r"""备份方式统计对象，提供给 备份集统计详情 接口

    """

    def __init__(self):
        r"""
        :param _AutoBackupSize: <p>自动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupSize: list of int
        :param _ManualBackupSize: <p>手动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackupSize: list of int
        """
        self._AutoBackupSize = None
        self._ManualBackupSize = None

    @property
    def AutoBackupSize(self):
        r"""<p>自动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def ManualBackupSize(self):
        r"""<p>手动备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize


    def _deserialize(self, params):
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._ManualBackupSize = params.get("ManualBackupSize")
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
        


class BackupPolicyModelOutPut(AbstractModel):
    r"""备份策略对象

    """

    def __init__(self):
        r"""
        :param _BackupEndTime: <p>备份结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupEndTime: str
        :param _BackupMethod: <p>备份方式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethod: str
        :param _BackupStartTime: <p>备份开始时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStartTime: str
        :param _DBType: <p>引擎类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DBType: str
        :param _DBVersion: <p>引擎版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DBVersion: str
        :param _EnableFull: <p>是否开启全量备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableFull: int
        :param _EnableLog: <p>是否开启日志备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableLog: int
        :param _ExpectedNextBackupPeriod: <p>预计下次备份时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectedNextBackupPeriod: str
        :param _FullRetentionPeriod: <p>全备保留时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FullRetentionPeriod: int
        :param _ID: <p>策略ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceId: <p>实例ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _LogRetentionPeriod: <p>日志保留天数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRetentionPeriod: int
        :param _PeriodTime: <p>一周的哪几天进行备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodTime: str
        :param _Region: <p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _PeriodType: <p>备份周期类型  0:Weekly</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodType: int
        """
        self._BackupEndTime = None
        self._BackupMethod = None
        self._BackupStartTime = None
        self._DBType = None
        self._DBVersion = None
        self._EnableFull = None
        self._EnableLog = None
        self._ExpectedNextBackupPeriod = None
        self._FullRetentionPeriod = None
        self._ID = None
        self._InstanceId = None
        self._LogRetentionPeriod = None
        self._PeriodTime = None
        self._Region = None
        self._PeriodType = None

    @property
    def BackupEndTime(self):
        r"""<p>备份结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupEndTime

    @BackupEndTime.setter
    def BackupEndTime(self, BackupEndTime):
        self._BackupEndTime = BackupEndTime

    @property
    def BackupMethod(self):
        r"""<p>备份方式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStartTime(self):
        r"""<p>备份开始时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def DBType(self):
        r"""<p>引擎类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

    @property
    def DBVersion(self):
        r"""<p>引擎版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def EnableFull(self):
        r"""<p>是否开启全量备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableFull

    @EnableFull.setter
    def EnableFull(self, EnableFull):
        self._EnableFull = EnableFull

    @property
    def EnableLog(self):
        r"""<p>是否开启日志备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableLog

    @EnableLog.setter
    def EnableLog(self, EnableLog):
        self._EnableLog = EnableLog

    @property
    def ExpectedNextBackupPeriod(self):
        r"""<p>预计下次备份时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpectedNextBackupPeriod

    @ExpectedNextBackupPeriod.setter
    def ExpectedNextBackupPeriod(self, ExpectedNextBackupPeriod):
        self._ExpectedNextBackupPeriod = ExpectedNextBackupPeriod

    @property
    def FullRetentionPeriod(self):
        r"""<p>全备保留时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FullRetentionPeriod

    @FullRetentionPeriod.setter
    def FullRetentionPeriod(self, FullRetentionPeriod):
        self._FullRetentionPeriod = FullRetentionPeriod

    @property
    def ID(self):
        r"""<p>策略ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogRetentionPeriod(self):
        r"""<p>日志保留天数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogRetentionPeriod

    @LogRetentionPeriod.setter
    def LogRetentionPeriod(self, LogRetentionPeriod):
        self._LogRetentionPeriod = LogRetentionPeriod

    @property
    def PeriodTime(self):
        r"""<p>一周的哪几天进行备份</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeriodTime

    @PeriodTime.setter
    def PeriodTime(self, PeriodTime):
        self._PeriodTime = PeriodTime

    @property
    def Region(self):
        r"""<p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PeriodType(self):
        r"""<p>备份周期类型  0:Weekly</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType


    def _deserialize(self, params):
        self._BackupEndTime = params.get("BackupEndTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStartTime = params.get("BackupStartTime")
        self._DBType = params.get("DBType")
        self._DBVersion = params.get("DBVersion")
        self._EnableFull = params.get("EnableFull")
        self._EnableLog = params.get("EnableLog")
        self._ExpectedNextBackupPeriod = params.get("ExpectedNextBackupPeriod")
        self._FullRetentionPeriod = params.get("FullRetentionPeriod")
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._LogRetentionPeriod = params.get("LogRetentionPeriod")
        self._PeriodTime = params.get("PeriodTime")
        self._Region = params.get("Region")
        self._PeriodType = params.get("PeriodType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSetModel(AbstractModel):
    r"""备份集对象

    """

    def __init__(self):
        r"""
        :param _BackupDuration: 备份集耗时，单位 sec
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupDuration: int
        :param _BackupMethod: 备份方式
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethod: str
        :param _BackupName: 备份备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupName: str
        :param _BackupProgress: 备份集进度百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupProgress: float
        :param _BackupSetId: 备份集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSetId: int
        :param _BackupStatus: 备份集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: str
        :param _BackupType: 备份集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupType: str
        :param _DBVersion: 实例版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type DBVersion: str
        :param _EndTime: 备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _EndTrxTime: 事务commit结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTrxTime: str
        :param _ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _ExpiredTime: 备份过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _FileName: 备份文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 备份集文件大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ManualBackup: 备份触发，0 - autobackup, 1 - manual
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackup: int
        :param _StartTime: 备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        """
        self._BackupDuration = None
        self._BackupMethod = None
        self._BackupName = None
        self._BackupProgress = None
        self._BackupSetId = None
        self._BackupStatus = None
        self._BackupType = None
        self._DBVersion = None
        self._EndTime = None
        self._EndTrxTime = None
        self._ErrorMessage = None
        self._ExpiredTime = None
        self._FileName = None
        self._FileSize = None
        self._InstanceId = None
        self._ManualBackup = None
        self._StartTime = None

    @property
    def BackupDuration(self):
        r"""备份集耗时，单位 sec
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupDuration

    @BackupDuration.setter
    def BackupDuration(self, BackupDuration):
        self._BackupDuration = BackupDuration

    @property
    def BackupMethod(self):
        r"""备份方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupName(self):
        r"""备份备注名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupProgress(self):
        r"""备份集进度百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._BackupProgress

    @BackupProgress.setter
    def BackupProgress(self, BackupProgress):
        self._BackupProgress = BackupProgress

    @property
    def BackupSetId(self):
        r"""备份集ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def BackupStatus(self):
        r"""备份集状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupType(self):
        r"""备份集类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def DBVersion(self):
        r"""实例版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def EndTime(self):
        r"""备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EndTrxTime(self):
        r"""事务commit结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTrxTime

    @EndTrxTime.setter
    def EndTrxTime(self, EndTrxTime):
        self._EndTrxTime = EndTrxTime

    @property
    def ErrorMessage(self):
        r"""错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ExpiredTime(self):
        r"""备份过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FileName(self):
        r"""备份文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""备份集文件大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def InstanceId(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ManualBackup(self):
        r"""备份触发，0 - autobackup, 1 - manual
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup

    @property
    def StartTime(self):
        r"""备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._BackupDuration = params.get("BackupDuration")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupName = params.get("BackupName")
        self._BackupProgress = params.get("BackupProgress")
        self._BackupSetId = params.get("BackupSetId")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupType = params.get("BackupType")
        self._DBVersion = params.get("DBVersion")
        self._EndTime = params.get("EndTime")
        self._EndTrxTime = params.get("EndTrxTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._InstanceId = params.get("InstanceId")
        self._ManualBackup = params.get("ManualBackup")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSetsReqFilter(AbstractModel):
    r"""备份集查询的filter

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>备份方式,多个值用逗号隔开</p><p>枚举值：</p><ul><li>physical： 物理备份</li><li>snapshot： 快照备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethod: str
        :param _BackupStatus: <p>备份状态，多个值用逗号隔开，含义说明：等待调度pending， 运行中 running, 成功success,失败 failed</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: str
        :param _BackupType: <p>备份类型，多个值用逗号隔开，含义说明：全量备份 full</p><p>枚举值：</p><ul><li>full： 全量备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupType: str
        :param _ManualBackup: <p>备份触发方式</p><p>枚举值：</p><ul><li>0： 自动备份</li><li>1： 手工备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackup: str
        """
        self._BackupMethod = None
        self._BackupStatus = None
        self._BackupType = None
        self._ManualBackup = None

    @property
    def BackupMethod(self):
        r"""<p>备份方式,多个值用逗号隔开</p><p>枚举值：</p><ul><li>physical： 物理备份</li><li>snapshot： 快照备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStatus(self):
        r"""<p>备份状态，多个值用逗号隔开，含义说明：等待调度pending， 运行中 running, 成功success,失败 failed</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupType(self):
        r"""<p>备份类型，多个值用逗号隔开，含义说明：全量备份 full</p><p>枚举值：</p><ul><li>full： 全量备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def ManualBackup(self):
        r"""<p>备份触发方式</p><p>枚举值：</p><ul><li>0： 自动备份</li><li>1： 手工备份</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup


    def _deserialize(self, params):
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupType = params.get("BackupType")
        self._ManualBackup = params.get("ManualBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStatisticsModel(AbstractModel):
    r"""备份统计对象

    """

    def __init__(self):
        r"""
        :param _AverageSizePerDay: <p>总备份每天平均大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerDay: int
        :param _DataBackupSize: <p>数据备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBackupSize: int
        :param _LogBackupSize: <p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBackupSize: int
        :param _TotalCount: <p>总备份集个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalSize: <p>总备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self._AverageSizePerDay = None
        self._DataBackupSize = None
        self._LogBackupSize = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AverageSizePerDay(self):
        r"""<p>总备份每天平均大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def DataBackupSize(self):
        r"""<p>数据备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataBackupSize

    @DataBackupSize.setter
    def DataBackupSize(self, DataBackupSize):
        self._DataBackupSize = DataBackupSize

    @property
    def LogBackupSize(self):
        r"""<p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def TotalCount(self):
        r"""<p>总备份集个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""<p>总备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._DataBackupSize = params.get("DataBackupSize")
        self._LogBackupSize = params.get("LogBackupSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTypeStatisticsModel(AbstractModel):
    r"""备份方式统计对象，提供给 备份集统计详情 接口

    """

    def __init__(self):
        r"""
        :param _DataBackupSize: <p>数据备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBackupSize: list of int
        :param _LogBackupSize: <p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBackupSize: list of int
        """
        self._DataBackupSize = None
        self._LogBackupSize = None

    @property
    def DataBackupSize(self):
        r"""<p>数据备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._DataBackupSize

    @DataBackupSize.setter
    def DataBackupSize(self, DataBackupSize):
        self._DataBackupSize = DataBackupSize

    @property
    def LogBackupSize(self):
        r"""<p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize


    def _deserialize(self, params):
        self._DataBackupSize = params.get("DataBackupSize")
        self._LogBackupSize = params.get("LogBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    r"""用于展示该节点的 Binlog 信息。

    """

    def __init__(self):
        r"""
        :param _Sid: 日志服务的唯一 ID
        :type Sid: str
        :param _Type: 日志服务的类型
        :type Type: str
        :param _InstanceId: 实例的唯一 ID
        :type InstanceId: str
        """
        self._Sid = None
        self._Type = None
        self._InstanceId = None

    @property
    def Sid(self):
        r"""日志服务的唯一 ID
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Type(self):
        r"""日志服务的类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        r"""实例的唯一 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
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
        


class CreateCloneInstanceRequest(AbstractModel):
    r"""CreateCloneInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: <p>创建实例区域</p>
        :type Zone: str
        :param _VpcId: <p>字符型vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>字符型subnetid</p>
        :type SubnetId: str
        :param _SpecCode: <p>购买规格</p>
        :type SpecCode: str
        :param _Disk: <p>存储节点磁盘容量，单位GB</p>
        :type Disk: int
        :param _StorageNodeNum: <p>存储节点数量</p>
        :type StorageNodeNum: int
        :param _InstanceId: <p>源实例id</p>
        :type InstanceId: str
        :param _InstanceName: <p>实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_</p>
        :type InstanceName: str
        :param _ResourceTags: <p>标签键值对数组</p>
        :type ResourceTags: list of ResourceTag
        :param _BackupName: <p>备份回档名称</p>
        :type BackupName: str
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
        :type StorageNodeMem: int
        :param _CreateVersion: <p>创建版本</p>
        :type CreateVersion: str
        :param _Vport: <p>创建端口号</p>
        :type Vport: int
        :param _RecoverTime: <p>恢复时间点</p>
        :type RecoverTime: str
        :param _InstanceType: <p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
        :type InstanceType: str
        :param _StorageType: <p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
        :type StorageType: str
        :param _Zones: <p>多可用区列表，Zones[0]表示主可用区</p>
        :type Zones: list of str
        :param _FullReplications: <p>全能型副本数</p>
        :type FullReplications: int
        :param _InstanceMode: <p>实例模式，normal：标准型；enhanced:加强型</p>
        :type InstanceMode: str
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeNum = None
        self._InstanceId = None
        self._InstanceName = None
        self._ResourceTags = None
        self._BackupName = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._CreateVersion = None
        self._Vport = None
        self._RecoverTime = None
        self._InstanceType = None
        self._StorageType = None
        self._Zones = None
        self._FullReplications = None
        self._InstanceMode = None

    @property
    def Zone(self):
        r"""<p>创建实例区域</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>字符型vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>字符型subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SpecCode(self):
        r"""<p>购买规格</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>存储节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>存储节点数量</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def InstanceId(self):
        r"""<p>源实例id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        r"""<p>标签键值对数组</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def BackupName(self):
        r"""<p>备份回档名称</p>
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def CreateVersion(self):
        r"""<p>创建版本</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def Vport(self):
        r"""<p>创建端口号</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def RecoverTime(self):
        r"""<p>恢复时间点</p>
        :rtype: str
        """
        return self._RecoverTime

    @RecoverTime.setter
    def RecoverTime(self, RecoverTime):
        self._RecoverTime = RecoverTime

    @property
    def InstanceType(self):
        r"""<p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zones(self):
        r"""<p>多可用区列表，Zones[0]表示主可用区</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def FullReplications(self):
        r"""<p>全能型副本数</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def InstanceMode(self):
        r"""<p>实例模式，normal：标准型；enhanced:加强型</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._BackupName = params.get("BackupName")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._CreateVersion = params.get("CreateVersion")
        self._Vport = params.get("Vport")
        self._RecoverTime = params.get("RecoverTime")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._Zones = params.get("Zones")
        self._FullReplications = params.get("FullReplications")
        self._InstanceMode = params.get("InstanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    r"""CreateCloneInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>克隆实例ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _FlowId: <p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>克隆实例ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        r"""<p>任务ID</p>
注意：此字段可能返回 null，表示取不到有效值。
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
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    r"""CreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: <p>创建实例区域</p>
        :type Zone: str
        :param _VpcId: <p>字符型vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>字符型subnetid</p>
        :type SubnetId: str
        :param _SpecCode: <p>购买规格</p>
        :type SpecCode: str
        :param _Disk: <p>存储节点磁盘容量，单位GB</p>
        :type Disk: int
        :param _StorageNodeNum: <p>存储节点数量</p>
        :type StorageNodeNum: int
        :param _Replications: <p>存储节点副本数量，最大为5，要求为奇数</p>
        :type Replications: int
        :param _InstanceCount: <p>创建实例个数，上限为10</p>
        :type InstanceCount: int
        :param _FullReplications: <p>全能型副本数量</p>
        :type FullReplications: int
        :param _CreateVersion: <p>创建实例版本，默认使用当前最新版本</p>
        :type CreateVersion: str
        :param _InstanceName: <p>实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_</p>
        :type InstanceName: str
        :param _ResourceTags: <p>标签键值对数组</p>
        :type ResourceTags: list of ResourceTag
        :param _InitParams: <p>初始化实例参数。比如：<br>character_set_server（字符集，默认为utf8），<br>lower_case_table_names（表名大小写敏感，0 - 敏感；1-不敏感，默认为0）</p>
        :type InitParams: list of InstanceParam
        :param _TimeUnit: <p>时间单位，m：月</p>
        :type TimeUnit: str
        :param _TimeSpan: <p>商品的时间大小</p>
        :type TimeSpan: int
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
        :type StorageNodeMem: int
        :param _PayMode: <p>付费模式，0表示按需计费/后付费，1表示预付费</p>
        :type PayMode: str
        :param _MCNum: <p>管控节点数量</p>
        :type MCNum: int
        :param _Vport: <p>自定义端口</p>
        :type Vport: int
        :param _Zones: <p>多AZ可用区列表</p>
        :type Zones: list of str
        :param _AutoVoucher: <p>是否使用优惠卷</p>
        :type AutoVoucher: bool
        :param _VoucherIds: <p>优惠卷列表</p>
        :type VoucherIds: list of str
        :param _InstanceType: <p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
        :type InstanceType: str
        :param _StorageType: <p>磁盘类型,CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
        :type StorageType: str
        :param _AZMode: <p>AZ模式，1:单AZ，2:多AZ非主AZ，3:多AZ主AZ</p>
        :type AZMode: int
        :param _InstanceMode: <p>实例模式</p>
        :type InstanceMode: str
        :param _TemplateId: <p>参数模板id</p>
        :type TemplateId: str
        :param _SQLMode: <p>兼容模式，enum:MySQL,HBase</p>
        :type SQLMode: str
        :param _AutoScaleConfig: <p>svls实例的ccu变配配置</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeNum = None
        self._Replications = None
        self._InstanceCount = None
        self._FullReplications = None
        self._CreateVersion = None
        self._InstanceName = None
        self._ResourceTags = None
        self._InitParams = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._PayMode = None
        self._MCNum = None
        self._Vport = None
        self._Zones = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._InstanceType = None
        self._StorageType = None
        self._AZMode = None
        self._InstanceMode = None
        self._TemplateId = None
        self._SQLMode = None
        self._AutoScaleConfig = None

    @property
    def Zone(self):
        r"""<p>创建实例区域</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>字符型vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>字符型subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SpecCode(self):
        r"""<p>购买规格</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>存储节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>存储节点数量</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def Replications(self):
        r"""<p>存储节点副本数量，最大为5，要求为奇数</p>
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def InstanceCount(self):
        r"""<p>创建实例个数，上限为10</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def FullReplications(self):
        r"""<p>全能型副本数量</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def CreateVersion(self):
        r"""<p>创建实例版本，默认使用当前最新版本</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def InstanceName(self):
        r"""<p>实例名称，要求长度1-60，允许包含中文、英文大小写、数字、-、_</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        r"""<p>标签键值对数组</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InitParams(self):
        r"""<p>初始化实例参数。比如：<br>character_set_server（字符集，默认为utf8），<br>lower_case_table_names（表名大小写敏感，0 - 敏感；1-不敏感，默认为0）</p>
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def TimeUnit(self):
        r"""<p>时间单位，m：月</p>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        r"""<p>商品的时间大小</p>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def PayMode(self):
        r"""<p>付费模式，0表示按需计费/后付费，1表示预付费</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def MCNum(self):
        r"""<p>管控节点数量</p>
        :rtype: int
        """
        return self._MCNum

    @MCNum.setter
    def MCNum(self, MCNum):
        self._MCNum = MCNum

    @property
    def Vport(self):
        r"""<p>自定义端口</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Zones(self):
        r"""<p>多AZ可用区列表</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def AutoVoucher(self):
        r"""<p>是否使用优惠卷</p>
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>优惠卷列表</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def InstanceType(self):
        r"""<p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>磁盘类型,CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def AZMode(self):
        r"""<p>AZ模式，1:单AZ，2:多AZ非主AZ，3:多AZ主AZ</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def InstanceMode(self):
        r"""<p>实例模式</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def TemplateId(self):
        r"""<p>参数模板id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SQLMode(self):
        r"""<p>兼容模式，enum:MySQL,HBase</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def AutoScaleConfig(self):
        r"""<p>svls实例的ccu变配配置</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._Replications = params.get("Replications")
        self._InstanceCount = params.get("InstanceCount")
        self._FullReplications = params.get("FullReplications")
        self._CreateVersion = params.get("CreateVersion")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._PayMode = params.get("PayMode")
        self._MCNum = params.get("MCNum")
        self._Vport = params.get("Vport")
        self._Zones = params.get("Zones")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._AZMode = params.get("AZMode")
        self._InstanceMode = params.get("InstanceMode")
        self._TemplateId = params.get("TemplateId")
        self._SQLMode = params.get("SQLMode")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    r"""CreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>实例ID</p>
        :type InstanceIds: list of str
        :param _FlowId: <p>任务ID</p>
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIds = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        r"""<p>实例ID</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        r"""<p>任务ID</p>
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
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateDBSBackupRequest(AbstractModel):
    r"""CreateDBSBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>备份方式：physical、snapshot 这个值和DescribeDBSBackupPolicy接口返回的backupMethod保持一致</p><p>枚举值：</p><ul><li>physical： 物理备份</li><li>snapshot： 快照备份</li></ul>
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
        r"""<p>备份方式：physical、snapshot 这个值和DescribeDBSBackupPolicy接口返回的backupMethod保持一致</p><p>枚举值：</p><ul><li>physical： 物理备份</li><li>snapshot： 快照备份</li></ul>
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
        


class DataBackupStatisticsModel(AbstractModel):
    r"""数据备份统计对象

    """

    def __init__(self):
        r"""
        :param _AutoBackupCount: 自动备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupCount: int
        :param _AutoBackupSize: 自动备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoBackupSize: int
        :param _AverageSizePerBackup: 平均每个备份大小,单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerBackup: int
        :param _AverageSizePerDay: 平均每天备份大小,单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerDay: int
        :param _ManualBackupCount: 手工备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackupCount: int
        :param _ManualBackupSize: 手工备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackupSize: int
        :param _TotalCount: 数据备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalSize: 数据备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self._AutoBackupCount = None
        self._AutoBackupSize = None
        self._AverageSizePerBackup = None
        self._AverageSizePerDay = None
        self._ManualBackupCount = None
        self._ManualBackupSize = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AutoBackupCount(self):
        r"""自动备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def AutoBackupSize(self):
        r"""自动备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def AverageSizePerBackup(self):
        r"""平均每个备份大小,单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerBackup

    @AverageSizePerBackup.setter
    def AverageSizePerBackup(self, AverageSizePerBackup):
        self._AverageSizePerBackup = AverageSizePerBackup

    @property
    def AverageSizePerDay(self):
        r"""平均每天备份大小,单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def ManualBackupCount(self):
        r"""手工备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def ManualBackupSize(self):
        r"""手工备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize

    @property
    def TotalCount(self):
        r"""数据备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""数据备份大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._AverageSizePerBackup = params.get("AverageSizePerBackup")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._ManualBackupSize = params.get("ManualBackupSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    r"""数据库信息

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        r"""数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
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
        


class DatabasePrivileges(AbstractModel):
    r"""Database级别权限列表

    """

    def __init__(self):
        r"""
        :param _Database: database名
        :type Database: str
        :param _Privileges: 权限列表
        :type Privileges: list of str
        """
        self._Database = None
        self._Privileges = None

    @property
    def Database(self):
        r"""database名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Privileges(self):
        r"""权限列表
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Privileges = params.get("Privileges")
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


class DescribeDBInstanceDetailRequest(AbstractModel):
    r"""DescribeDBInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        """
        self._InstanceId = None

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
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDetailResponse(AbstractModel):
    r"""DescribeDBInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: <p>实例名称</p>
        :type InstanceName: str
        :param _Zone: <p>区域</p>
        :type Zone: str
        :param _VpcId: <p>字符型vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>字符型subnetid</p>
        :type SubnetId: str
        :param _CreateVersion: <p>创建实例版本</p>
        :type CreateVersion: str
        :param _Vip: <p>子网IP</p>
        :type Vip: str
        :param _Vport: <p>子网端口</p>
        :type Vport: int
        :param _Status: <p>实例状态</p>
        :type Status: str
        :param _Disk: <p>存储节点磁盘容量，单位GB</p>
        :type Disk: int
        :param _StorageNodeNum: <p>存储节点数量</p>
        :type StorageNodeNum: int
        :param _InitParams: <p>初始化实例参数</p>
        :type InitParams: list of InstanceParam
        :param _ResourceTags: <p>实例标签信息</p>
        :type ResourceTags: list of ResourceTag
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间</p>
        :type UpdateTime: str
        :param _Replications: <p>存储节点副本数量</p>
        :type Replications: int
        :param _FullReplications: <p>全能型副本数</p>
        :type FullReplications: int
        :param _CharSet: <p>字符集</p>
        :type CharSet: str
        :param _Node: <p>节点信息</p>
        :type Node: list of NodeInfo
        :param _Region: <p>实例所属地域</p>
        :type Region: str
        :param _SpecCode: <p>实例规格</p>
        :type SpecCode: str
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _StatusDesc: <p>实例状态中文描述</p>
        :type StatusDesc: str
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
        :type StorageNodeMem: int
        :param _RenewFlag: <p>续费标志</p>
        :type RenewFlag: int
        :param _PayMode: <p>付费模式，0后付费，1预付费</p>
        :type PayMode: str
        :param _ExpireAt: <p>过期时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireAt: str
        :param _IsolatedAt: <p>隔离时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedAt: str
        :param _InstanceType: <p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _StorageType: <p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _Zones: <p>实例节点可用区列表。Zones[0]表示主可用区</p>
        :type Zones: list of str
        :param _DiskUsage: <p>最大节点磁盘使用量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskUsage: int
        :param _BinlogStatus: <p>binlog是否开启</p>
        :type BinlogStatus: int
        :param _AZMode: <p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
        :type AZMode: int
        :param _StandbyFlag: <p>灾备标志位，1: 无灾备关系；2: 灾备主实例；3: 灾备备实例</p>
        :type StandbyFlag: int
        :param _BinlogType: <p>cdc节点类型</p>
        :type BinlogType: str
        :param _TimingModifyInstanceFlag: <p>1表示支持，0表示不支持</p>
        :type TimingModifyInstanceFlag: int
        :param _ColumnarNodeCpu: <p>列存节点cpu核数</p>
        :type ColumnarNodeCpu: int
        :param _ColumnarNodeMem: <p>列存节点mem内存大小</p>
        :type ColumnarNodeMem: int
        :param _ColumnarNodeNum: <p>列存节点个数</p>
        :type ColumnarNodeNum: int
        :param _ColumnarNodeDisk: <p>列存节点磁盘大小</p>
        :type ColumnarNodeDisk: int
        :param _ColumnarNodeStorageType: <p>列存节点磁盘类型</p>
        :type ColumnarNodeStorageType: str
        :param _ColumnarNodeSpecCode: <p>列存节点规格</p>
        :type ColumnarNodeSpecCode: str
        :param _ColumnarVip: <p>列存 vip</p>
        :type ColumnarVip: str
        :param _ColumnarVport: <p>列存 vport</p>
        :type ColumnarVport: int
        :param _IsSupportColumnar: <p>实例是否支持列存</p>
        :type IsSupportColumnar: bool
        :param _InstanceCategory: <p>实例类型</p>
        :type InstanceCategory: int
        :param _SQLMode: <p>兼容模式</p>
        :type SQLMode: str
        :param _IsSwitchFullReplicationsEnable: <p>是否支持修改全能型副本数量</p>
        :type IsSwitchFullReplicationsEnable: bool
        :param _InstanceMode: <p>实例类型</p>
        :type InstanceMode: str
        :param _DumperVip: <p>dumper vip</p>
        :type DumperVip: str
        :param _DumperVport: <p>dumper vport</p>
        :type DumperVport: int
        :param _AutoScaleConfig: <p>svls实例的ccu变配范围</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        :param _TemplateId: <p>参数模板id</p>
        :type TemplateId: str
        :param _TemplateName: <p>参数模板名称</p>
        :type TemplateName: str
        :param _AnalysisMode: <p>实例分析引擎模式</p><p>枚举值：</p><ul><li>libra： LibraDB分析引擎实例</li></ul>
        :type AnalysisMode: str
        :param _AnalysisRelationInfos: <p>分析引擎实例关系</p>
        :type AnalysisRelationInfos: list of AnalysisRelationInfo
        :param _AnalysisInstanceInfo: <p>分析引擎实例信息</p><p>Cpu、Memory、Disk复用顶层字段</p>
        :type AnalysisInstanceInfo: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        :param _MaintenanceWindow: <p>维护窗口配置</p>
        :type MaintenanceWindow: :class:`tencentcloud.tdmysql.v20211122.models.MaintenanceWindowInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceName = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._CreateVersion = None
        self._Vip = None
        self._Vport = None
        self._Status = None
        self._Disk = None
        self._StorageNodeNum = None
        self._InitParams = None
        self._ResourceTags = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Replications = None
        self._FullReplications = None
        self._CharSet = None
        self._Node = None
        self._Region = None
        self._SpecCode = None
        self._InstanceId = None
        self._StatusDesc = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpireAt = None
        self._IsolatedAt = None
        self._InstanceType = None
        self._StorageType = None
        self._Zones = None
        self._DiskUsage = None
        self._BinlogStatus = None
        self._AZMode = None
        self._StandbyFlag = None
        self._BinlogType = None
        self._TimingModifyInstanceFlag = None
        self._ColumnarNodeCpu = None
        self._ColumnarNodeMem = None
        self._ColumnarNodeNum = None
        self._ColumnarNodeDisk = None
        self._ColumnarNodeStorageType = None
        self._ColumnarNodeSpecCode = None
        self._ColumnarVip = None
        self._ColumnarVport = None
        self._IsSupportColumnar = None
        self._InstanceCategory = None
        self._SQLMode = None
        self._IsSwitchFullReplicationsEnable = None
        self._InstanceMode = None
        self._DumperVip = None
        self._DumperVport = None
        self._AutoScaleConfig = None
        self._TemplateId = None
        self._TemplateName = None
        self._AnalysisMode = None
        self._AnalysisRelationInfos = None
        self._AnalysisInstanceInfo = None
        self._MaintenanceWindow = None
        self._RequestId = None

    @property
    def InstanceName(self):
        r"""<p>实例名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        r"""<p>区域</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>字符型vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>字符型subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateVersion(self):
        r"""<p>创建实例版本</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def Vip(self):
        r"""<p>子网IP</p>
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""<p>子网端口</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        r"""<p>实例状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Disk(self):
        r"""<p>存储节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>存储节点数量</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def InitParams(self):
        r"""<p>初始化实例参数</p>
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def ResourceTags(self):
        r"""<p>实例标签信息</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Replications(self):
        r"""<p>存储节点副本数量</p>
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def FullReplications(self):
        r"""<p>全能型副本数</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def CharSet(self):
        r"""<p>字符集</p>
        :rtype: str
        """
        return self._CharSet

    @CharSet.setter
    def CharSet(self, CharSet):
        self._CharSet = CharSet

    @property
    def Node(self):
        r"""<p>节点信息</p>
        :rtype: list of NodeInfo
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Region(self):
        r"""<p>实例所属地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SpecCode(self):
        r"""<p>实例规格</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

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
    def StatusDesc(self):
        r"""<p>实例状态中文描述</p>
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def RenewFlag(self):
        r"""<p>续费标志</p>
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        r"""<p>付费模式，0后付费，1预付费</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpireAt(self):
        r"""<p>过期时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def IsolatedAt(self):
        r"""<p>隔离时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def InstanceType(self):
        r"""<p>实例架构类型，separate:分离架构；hybrid:对等架构</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zones(self):
        r"""<p>实例节点可用区列表。Zones[0]表示主可用区</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def DiskUsage(self):
        r"""<p>最大节点磁盘使用量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def BinlogStatus(self):
        r"""<p>binlog是否开启</p>
        :rtype: int
        """
        return self._BinlogStatus

    @BinlogStatus.setter
    def BinlogStatus(self, BinlogStatus):
        self._BinlogStatus = BinlogStatus

    @property
    def AZMode(self):
        r"""<p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def StandbyFlag(self):
        r"""<p>灾备标志位，1: 无灾备关系；2: 灾备主实例；3: 灾备备实例</p>
        :rtype: int
        """
        return self._StandbyFlag

    @StandbyFlag.setter
    def StandbyFlag(self, StandbyFlag):
        self._StandbyFlag = StandbyFlag

    @property
    def BinlogType(self):
        r"""<p>cdc节点类型</p>
        :rtype: str
        """
        return self._BinlogType

    @BinlogType.setter
    def BinlogType(self, BinlogType):
        self._BinlogType = BinlogType

    @property
    def TimingModifyInstanceFlag(self):
        r"""<p>1表示支持，0表示不支持</p>
        :rtype: int
        """
        return self._TimingModifyInstanceFlag

    @TimingModifyInstanceFlag.setter
    def TimingModifyInstanceFlag(self, TimingModifyInstanceFlag):
        self._TimingModifyInstanceFlag = TimingModifyInstanceFlag

    @property
    def ColumnarNodeCpu(self):
        r"""<p>列存节点cpu核数</p>
        :rtype: int
        """
        return self._ColumnarNodeCpu

    @ColumnarNodeCpu.setter
    def ColumnarNodeCpu(self, ColumnarNodeCpu):
        self._ColumnarNodeCpu = ColumnarNodeCpu

    @property
    def ColumnarNodeMem(self):
        r"""<p>列存节点mem内存大小</p>
        :rtype: int
        """
        return self._ColumnarNodeMem

    @ColumnarNodeMem.setter
    def ColumnarNodeMem(self, ColumnarNodeMem):
        self._ColumnarNodeMem = ColumnarNodeMem

    @property
    def ColumnarNodeNum(self):
        r"""<p>列存节点个数</p>
        :rtype: int
        """
        return self._ColumnarNodeNum

    @ColumnarNodeNum.setter
    def ColumnarNodeNum(self, ColumnarNodeNum):
        self._ColumnarNodeNum = ColumnarNodeNum

    @property
    def ColumnarNodeDisk(self):
        r"""<p>列存节点磁盘大小</p>
        :rtype: int
        """
        return self._ColumnarNodeDisk

    @ColumnarNodeDisk.setter
    def ColumnarNodeDisk(self, ColumnarNodeDisk):
        self._ColumnarNodeDisk = ColumnarNodeDisk

    @property
    def ColumnarNodeStorageType(self):
        r"""<p>列存节点磁盘类型</p>
        :rtype: str
        """
        return self._ColumnarNodeStorageType

    @ColumnarNodeStorageType.setter
    def ColumnarNodeStorageType(self, ColumnarNodeStorageType):
        self._ColumnarNodeStorageType = ColumnarNodeStorageType

    @property
    def ColumnarNodeSpecCode(self):
        r"""<p>列存节点规格</p>
        :rtype: str
        """
        return self._ColumnarNodeSpecCode

    @ColumnarNodeSpecCode.setter
    def ColumnarNodeSpecCode(self, ColumnarNodeSpecCode):
        self._ColumnarNodeSpecCode = ColumnarNodeSpecCode

    @property
    def ColumnarVip(self):
        r"""<p>列存 vip</p>
        :rtype: str
        """
        return self._ColumnarVip

    @ColumnarVip.setter
    def ColumnarVip(self, ColumnarVip):
        self._ColumnarVip = ColumnarVip

    @property
    def ColumnarVport(self):
        r"""<p>列存 vport</p>
        :rtype: int
        """
        return self._ColumnarVport

    @ColumnarVport.setter
    def ColumnarVport(self, ColumnarVport):
        self._ColumnarVport = ColumnarVport

    @property
    def IsSupportColumnar(self):
        r"""<p>实例是否支持列存</p>
        :rtype: bool
        """
        return self._IsSupportColumnar

    @IsSupportColumnar.setter
    def IsSupportColumnar(self, IsSupportColumnar):
        self._IsSupportColumnar = IsSupportColumnar

    @property
    def InstanceCategory(self):
        r"""<p>实例类型</p>
        :rtype: int
        """
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def SQLMode(self):
        r"""<p>兼容模式</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def IsSwitchFullReplicationsEnable(self):
        r"""<p>是否支持修改全能型副本数量</p>
        :rtype: bool
        """
        return self._IsSwitchFullReplicationsEnable

    @IsSwitchFullReplicationsEnable.setter
    def IsSwitchFullReplicationsEnable(self, IsSwitchFullReplicationsEnable):
        self._IsSwitchFullReplicationsEnable = IsSwitchFullReplicationsEnable

    @property
    def InstanceMode(self):
        r"""<p>实例类型</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def DumperVip(self):
        r"""<p>dumper vip</p>
        :rtype: str
        """
        return self._DumperVip

    @DumperVip.setter
    def DumperVip(self, DumperVip):
        self._DumperVip = DumperVip

    @property
    def DumperVport(self):
        r"""<p>dumper vport</p>
        :rtype: int
        """
        return self._DumperVport

    @DumperVport.setter
    def DumperVport(self, DumperVport):
        self._DumperVport = DumperVport

    @property
    def AutoScaleConfig(self):
        r"""<p>svls实例的ccu变配范围</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig

    @property
    def TemplateId(self):
        r"""<p>参数模板id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>参数模板名称</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def AnalysisMode(self):
        r"""<p>实例分析引擎模式</p><p>枚举值：</p><ul><li>libra： LibraDB分析引擎实例</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def AnalysisRelationInfos(self):
        r"""<p>分析引擎实例关系</p>
        :rtype: list of AnalysisRelationInfo
        """
        return self._AnalysisRelationInfos

    @AnalysisRelationInfos.setter
    def AnalysisRelationInfos(self, AnalysisRelationInfos):
        self._AnalysisRelationInfos = AnalysisRelationInfos

    @property
    def AnalysisInstanceInfo(self):
        r"""<p>分析引擎实例信息</p><p>Cpu、Memory、Disk复用顶层字段</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        """
        return self._AnalysisInstanceInfo

    @AnalysisInstanceInfo.setter
    def AnalysisInstanceInfo(self, AnalysisInstanceInfo):
        self._AnalysisInstanceInfo = AnalysisInstanceInfo

    @property
    def MaintenanceWindow(self):
        r"""<p>维护窗口配置</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.MaintenanceWindowInfo`
        """
        return self._MaintenanceWindow

    @MaintenanceWindow.setter
    def MaintenanceWindow(self, MaintenanceWindow):
        self._MaintenanceWindow = MaintenanceWindow

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
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreateVersion = params.get("CreateVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Replications = params.get("Replications")
        self._FullReplications = params.get("FullReplications")
        self._CharSet = params.get("CharSet")
        if params.get("Node") is not None:
            self._Node = []
            for item in params.get("Node"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._Node.append(obj)
        self._Region = params.get("Region")
        self._SpecCode = params.get("SpecCode")
        self._InstanceId = params.get("InstanceId")
        self._StatusDesc = params.get("StatusDesc")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpireAt = params.get("ExpireAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._Zones = params.get("Zones")
        self._DiskUsage = params.get("DiskUsage")
        self._BinlogStatus = params.get("BinlogStatus")
        self._AZMode = params.get("AZMode")
        self._StandbyFlag = params.get("StandbyFlag")
        self._BinlogType = params.get("BinlogType")
        self._TimingModifyInstanceFlag = params.get("TimingModifyInstanceFlag")
        self._ColumnarNodeCpu = params.get("ColumnarNodeCpu")
        self._ColumnarNodeMem = params.get("ColumnarNodeMem")
        self._ColumnarNodeNum = params.get("ColumnarNodeNum")
        self._ColumnarNodeDisk = params.get("ColumnarNodeDisk")
        self._ColumnarNodeStorageType = params.get("ColumnarNodeStorageType")
        self._ColumnarNodeSpecCode = params.get("ColumnarNodeSpecCode")
        self._ColumnarVip = params.get("ColumnarVip")
        self._ColumnarVport = params.get("ColumnarVport")
        self._IsSupportColumnar = params.get("IsSupportColumnar")
        self._InstanceCategory = params.get("InstanceCategory")
        self._SQLMode = params.get("SQLMode")
        self._IsSwitchFullReplicationsEnable = params.get("IsSwitchFullReplicationsEnable")
        self._InstanceMode = params.get("InstanceMode")
        self._DumperVip = params.get("DumperVip")
        self._DumperVport = params.get("DumperVport")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("AnalysisRelationInfos") is not None:
            self._AnalysisRelationInfos = []
            for item in params.get("AnalysisRelationInfos"):
                obj = AnalysisRelationInfo()
                obj._deserialize(item)
                self._AnalysisRelationInfos.append(obj)
        if params.get("AnalysisInstanceInfo") is not None:
            self._AnalysisInstanceInfo = AnalysisInstanceInfo()
            self._AnalysisInstanceInfo._deserialize(params.get("AnalysisInstanceInfo"))
        if params.get("MaintenanceWindow") is not None:
            self._MaintenanceWindow = MaintenanceWindowInfo()
            self._MaintenanceWindow._deserialize(params.get("MaintenanceWindow"))
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤参数
        :type Filters: list of InstanceFilter
        :param _Limit: 最大返回个数，默认为20，上限为100
        :type Limit: int
        :param _Offset: 偏移量，取Limit整数倍
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        r"""过滤参数
        :rtype: list of InstanceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""最大返回个数，默认为20，上限为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，取Limit整数倍
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = InstanceFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 返回实例列表信息
        :type Instances: list of InstanceInfo
        :param _TotalCount: 满足条件总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""返回实例列表信息
        :rtype: list of InstanceInfo
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""满足条件总数量
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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
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


class DescribeDBSArchiveLogsRequest(AbstractModel):
    r"""DescribeDBSArchiveLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _ArchiveLogId: <p>日志记录ID</p>
        :type ArchiveLogId: int
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _FilterStatus: <p>备份状态：pending,running,success,failed</p>
        :type FilterStatus: str
        :param _Limit: <p>条数限制</p>
        :type Limit: int
        :param _Offset: <p>偏移量</p>
        :type Offset: int
        :param _OrderBy: <p>排序字段，枚举：StartTime,EndTime,ExpiredTime,FileSize,BackupDuration</p>
        :type OrderBy: str
        :param _OrderType: <p>排序方式：ASC：顺序, DESC：倒序</p>
        :type OrderType: str
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._ArchiveLogId = None
        self._EndTime = None
        self._FilterStatus = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None

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
    def ArchiveLogId(self):
        r"""<p>日志记录ID</p>
        :rtype: int
        """
        return self._ArchiveLogId

    @ArchiveLogId.setter
    def ArchiveLogId(self, ArchiveLogId):
        self._ArchiveLogId = ArchiveLogId

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
    def FilterStatus(self):
        r"""<p>备份状态：pending,running,success,failed</p>
        :rtype: str
        """
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def Limit(self):
        r"""<p>条数限制</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>排序字段，枚举：StartTime,EndTime,ExpiredTime,FileSize,BackupDuration</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>排序方式：ASC：顺序, DESC：倒序</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ArchiveLogId = params.get("ArchiveLogId")
        self._EndTime = params.get("EndTime")
        self._FilterStatus = params.get("FilterStatus")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSArchiveLogsResponse(AbstractModel):
    r"""DescribeDBSArchiveLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: <p>归档日志列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ArchiveLogModel
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
        r"""<p>归档日志列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ArchiveLogModel
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
                obj = ArchiveLogModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        """
        self._InstanceId = None

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
        self._InstanceId = params.get("InstanceId")
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


class DescribeDBSBackupPolicyRequest(AbstractModel):
    r"""DescribeDBSBackupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        """
        self._InstanceId = None

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
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupPolicyResponse(AbstractModel):
    r"""DescribeDBSBackupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: <p>备份策略列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of BackupPolicyModelOutPut
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
        r"""<p>备份策略列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackupPolicyModelOutPut
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
                obj = BackupPolicyModelOutPut()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupSetsRequest(AbstractModel):
    r"""DescribeDBSBackupSets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _BackupSetId: <p>实例备份集ID</p>
        :type BackupSetId: int
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _FilterBy: <p>过滤条件</p>
        :type FilterBy: :class:`tencentcloud.tdmysql.v20211122.models.BackupSetsReqFilter`
        :param _Limit: <p>单次查询数量[0,200]</p>
        :type Limit: int
        :param _Offset: <p>本次查询偏移[0,INF]</p>
        :type Offset: int
        :param _OrderBy: <p>StartTime,EndTime,ExpiredTime,BackupSetId,BackupDuration</p>
        :type OrderBy: str
        :param _OrderType: <p>ASC,DESC</p>
        :type OrderType: str
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._BackupSetId = None
        self._EndTime = None
        self._FilterBy = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None

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
        r"""<p>实例备份集ID</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

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
    def FilterBy(self):
        r"""<p>过滤条件</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupSetsReqFilter`
        """
        return self._FilterBy

    @FilterBy.setter
    def FilterBy(self, FilterBy):
        self._FilterBy = FilterBy

    @property
    def Limit(self):
        r"""<p>单次查询数量[0,200]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>本次查询偏移[0,INF]</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>StartTime,EndTime,ExpiredTime,BackupSetId,BackupDuration</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>ASC,DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._EndTime = params.get("EndTime")
        if params.get("FilterBy") is not None:
            self._FilterBy = BackupSetsReqFilter()
            self._FilterBy._deserialize(params.get("FilterBy"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupSetsResponse(AbstractModel):
    r"""DescribeDBSBackupSets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: <p>备份集列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of BackupSetModel
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
        r"""<p>备份集列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackupSetModel
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
                obj = BackupSetModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupStatisticsDetailRequest(AbstractModel):
    r"""DescribeDBSBackupStatisticsDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._EndTime = None
        self._StartTime = None

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
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupStatisticsDetailResponse(AbstractModel):
    r"""DescribeDBSBackupStatisticsDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMethodStatistics: <p>按备份方式统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethodStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsOutPut`
        :param _BackupTime: <p>备份时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupTime: list of str
        :param _BackupTypeStatistics: <p>按备份数据类型统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupTypeStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupTypeStatisticsModel`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupMethodStatistics = None
        self._BackupTime = None
        self._BackupTypeStatistics = None
        self._RequestId = None

    @property
    def BackupMethodStatistics(self):
        r"""<p>按备份方式统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsOutPut`
        """
        return self._BackupMethodStatistics

    @BackupMethodStatistics.setter
    def BackupMethodStatistics(self, BackupMethodStatistics):
        self._BackupMethodStatistics = BackupMethodStatistics

    @property
    def BackupTime(self):
        r"""<p>备份时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupTypeStatistics(self):
        r"""<p>按备份数据类型统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupTypeStatisticsModel`
        """
        return self._BackupTypeStatistics

    @BackupTypeStatistics.setter
    def BackupTypeStatistics(self, BackupTypeStatistics):
        self._BackupTypeStatistics = BackupTypeStatistics

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
        if params.get("BackupMethodStatistics") is not None:
            self._BackupMethodStatistics = BackupMethodStatisticsOutPut()
            self._BackupMethodStatistics._deserialize(params.get("BackupMethodStatistics"))
        self._BackupTime = params.get("BackupTime")
        if params.get("BackupTypeStatistics") is not None:
            self._BackupTypeStatistics = BackupTypeStatisticsModel()
            self._BackupTypeStatistics._deserialize(params.get("BackupTypeStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupStatisticsRequest(AbstractModel):
    r"""DescribeDBSBackupStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._EndTime = None
        self._StartTime = None

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
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupStatisticsResponse(AbstractModel):
    r"""DescribeDBSBackupStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMethodStatistics: <p>备份方式统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethodStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsModel`
        :param _BackupStatistics: <p>总备份集统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupStatisticsModel`
        :param _DataBackupStatistics: <p>数据备份统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.DataBackupStatisticsModel`
        :param _LogBackupStatistics: <p>日志备份统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.LogBackupStatisticsModel`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupMethodStatistics = None
        self._BackupStatistics = None
        self._DataBackupStatistics = None
        self._LogBackupStatistics = None
        self._RequestId = None

    @property
    def BackupMethodStatistics(self):
        r"""<p>备份方式统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsModel`
        """
        return self._BackupMethodStatistics

    @BackupMethodStatistics.setter
    def BackupMethodStatistics(self, BackupMethodStatistics):
        self._BackupMethodStatistics = BackupMethodStatistics

    @property
    def BackupStatistics(self):
        r"""<p>总备份集统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupStatisticsModel`
        """
        return self._BackupStatistics

    @BackupStatistics.setter
    def BackupStatistics(self, BackupStatistics):
        self._BackupStatistics = BackupStatistics

    @property
    def DataBackupStatistics(self):
        r"""<p>数据备份统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DataBackupStatisticsModel`
        """
        return self._DataBackupStatistics

    @DataBackupStatistics.setter
    def DataBackupStatistics(self, DataBackupStatistics):
        self._DataBackupStatistics = DataBackupStatistics

    @property
    def LogBackupStatistics(self):
        r"""<p>日志备份统计</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.LogBackupStatisticsModel`
        """
        return self._LogBackupStatistics

    @LogBackupStatistics.setter
    def LogBackupStatistics(self, LogBackupStatistics):
        self._LogBackupStatistics = LogBackupStatistics

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
        if params.get("BackupMethodStatistics") is not None:
            self._BackupMethodStatistics = BackupMethodStatisticsModel()
            self._BackupMethodStatistics._deserialize(params.get("BackupMethodStatistics"))
        if params.get("BackupStatistics") is not None:
            self._BackupStatistics = BackupStatisticsModel()
            self._BackupStatistics._deserialize(params.get("BackupStatistics"))
        if params.get("DataBackupStatistics") is not None:
            self._DataBackupStatistics = DataBackupStatisticsModel()
            self._DataBackupStatistics._deserialize(params.get("DataBackupStatistics"))
        if params.get("LogBackupStatistics") is not None:
            self._LogBackupStatistics = LogBackupStatisticsModel()
            self._LogBackupStatistics._deserialize(params.get("LogBackupStatistics"))
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
        :param _InstanceId: <p>实例 ID，形如：tdsql3-42f40429.</p>
        :type InstanceId: str
        :param _DbName: <p>数据库名称，通过 DescribeDatabases 接口获取。</p>
        :type DbName: str
        :param _Offset: <p>分页索引</p>
        :type Offset: int
        :param _Limit: <p>每页数量</p>
        :type Limit: int
        :param _TableRegexp: <p>数据表名称匹配表达式</p>
        :type TableRegexp: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Offset = None
        self._Limit = None
        self._TableRegexp = None

    @property
    def InstanceId(self):
        r"""<p>实例 ID，形如：tdsql3-42f40429.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""<p>数据库名称，通过 DescribeDatabases 接口获取。</p>
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Offset(self):
        r"""<p>分页索引</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TableRegexp(self):
        r"""<p>数据表名称匹配表达式</p>
        :rtype: str
        """
        return self._TableRegexp

    @TableRegexp.setter
    def TableRegexp(self, TableRegexp):
        self._TableRegexp = TableRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TableRegexp = params.get("TableRegexp")
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
        :param _InstanceId: <p>透传入参。</p>
        :type InstanceId: str
        :param _DbName: <p>数据库名称。</p>
        :type DbName: str
        :param _Tables: <p>表列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of DatabaseTable
        :param _Views: <p>视图列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Views: list of DatabaseView
        :param _Procs: <p>存储过程列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Procs: list of DatabaseProcedure
        :param _Funcs: <p>函数列表。</p>
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
        r"""<p>透传入参。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""<p>数据库名称。</p>
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        r"""<p>表列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        r"""<p>视图列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        r"""<p>存储过程列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        r"""<p>函数列表。</p>
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


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例 ID，形如：tdsql3-ow7t8lmc。</p>
        :type InstanceId: str
        :param _Offset: <p>分页索引</p>
        :type Offset: int
        :param _Limit: <p>每页数量</p>
        :type Limit: int
        :param _DatabaseRegexp: <p>数据库名称匹配表达式</p>
        :type DatabaseRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._DatabaseRegexp = None

    @property
    def InstanceId(self):
        r"""<p>实例 ID，形如：tdsql3-ow7t8lmc。</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""<p>分页索引</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页数量</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DatabaseRegexp(self):
        r"""<p>数据库名称匹配表达式</p>
        :rtype: str
        """
        return self._DatabaseRegexp

    @DatabaseRegexp.setter
    def DatabaseRegexp(self, DatabaseRegexp):
        self._DatabaseRegexp = DatabaseRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DatabaseRegexp = params.get("DatabaseRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    r"""DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>透传实例ID</p>
        :type InstanceId: str
        :param _Databases: <p>该实例上的数据库列表。</p>
        :type Databases: list of Database
        :param _TotalCount: <p>总数量</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Databases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>透传实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Databases(self):
        r"""<p>该实例上的数据库列表。</p>
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def TotalCount(self):
        r"""<p>总数量</p>
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
        self._InstanceId = params.get("InstanceId")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._TotalCount = params.get("TotalCount")
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


class DescribeSaleInfoRequest(AbstractModel):
    r"""DescribeSaleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcRegion: <p>灾备主实例地域</p>
        :type SrcRegion: str
        :param _InstanceId: <p>实例id</p><p>传入此参数表示返回这个实例所在的地域可用区的售卖信息</p>
        :type InstanceId: str
        :param _InstanceType: <p>指定支持某种类型实例的 sale 信息</p><p>枚举值：</p><ul><li>serverless： 返回支持 serverless 型实例的所有 region</li></ul><p>默认值：无</p><p>当前仅支持指定 serverless，传入其他信息或者不传则默认返回所有售卖地域信息</p>
        :type InstanceType: str
        """
        self._SrcRegion = None
        self._InstanceId = None
        self._InstanceType = None

    @property
    def SrcRegion(self):
        r"""<p>灾备主实例地域</p>
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def InstanceId(self):
        r"""<p>实例id</p><p>传入此参数表示返回这个实例所在的地域可用区的售卖信息</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        r"""<p>指定支持某种类型实例的 sale 信息</p><p>枚举值：</p><ul><li>serverless： 返回支持 serverless 型实例的所有 region</li></ul><p>默认值：无</p><p>当前仅支持指定 serverless，传入其他信息或者不传则默认返回所有售卖地域信息</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._SrcRegion = params.get("SrcRegion")
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleInfoResponse(AbstractModel):
    r"""DescribeSaleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionList: <p>返回可售卖region信息</p>
        :type RegionList: list of DescribeSaleRegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        r"""<p>返回可售卖region信息</p>
        :rtype: list of DescribeSaleRegionInfo
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = DescribeSaleRegionInfo()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSaleRegionInfo(AbstractModel):
    r"""查询售卖接口，region信息返回类型

    """

    def __init__(self):
        r"""
        :param _Region: <p>Region英文字符串</p>
        :type Region: str
        :param _ZoneList: <p>售卖Zone列表</p>
        :type ZoneList: list of DescribeSaleZonesInfo
        :param _RegionName: <p>Region中文字符串</p>
        :type RegionName: str
        :param _Enable: <p>是否售卖。1:售卖，0不售卖</p>
        :type Enable: int
        :param _AvailableZoneNum: <p>多可用可选数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableZoneNum: int
        :param _IsSupportedLogReplica: <p>是否允许使用日志副本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportedLogReplica: bool
        :param _ZoneGroup: <p>可用区组合</p>
        :type ZoneGroup: list of DescribeSaleZonesGroup
        :param _IsSupportServerless: <p>是否支持serverless</p>
        :type IsSupportServerless: bool
        """
        self._Region = None
        self._ZoneList = None
        self._RegionName = None
        self._Enable = None
        self._AvailableZoneNum = None
        self._IsSupportedLogReplica = None
        self._ZoneGroup = None
        self._IsSupportServerless = None

    @property
    def Region(self):
        r"""<p>Region英文字符串</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ZoneList(self):
        r"""<p>售卖Zone列表</p>
        :rtype: list of DescribeSaleZonesInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def RegionName(self):
        r"""<p>Region中文字符串</p>
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Enable(self):
        r"""<p>是否售卖。1:售卖，0不售卖</p>
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AvailableZoneNum(self):
        r"""<p>多可用可选数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AvailableZoneNum

    @AvailableZoneNum.setter
    def AvailableZoneNum(self, AvailableZoneNum):
        self._AvailableZoneNum = AvailableZoneNum

    @property
    def IsSupportedLogReplica(self):
        r"""<p>是否允许使用日志副本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsSupportedLogReplica

    @IsSupportedLogReplica.setter
    def IsSupportedLogReplica(self, IsSupportedLogReplica):
        self._IsSupportedLogReplica = IsSupportedLogReplica

    @property
    def ZoneGroup(self):
        r"""<p>可用区组合</p>
        :rtype: list of DescribeSaleZonesGroup
        """
        return self._ZoneGroup

    @ZoneGroup.setter
    def ZoneGroup(self, ZoneGroup):
        self._ZoneGroup = ZoneGroup

    @property
    def IsSupportServerless(self):
        r"""<p>是否支持serverless</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = DescribeSaleZonesInfo()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RegionName = params.get("RegionName")
        self._Enable = params.get("Enable")
        self._AvailableZoneNum = params.get("AvailableZoneNum")
        self._IsSupportedLogReplica = params.get("IsSupportedLogReplica")
        if params.get("ZoneGroup") is not None:
            self._ZoneGroup = []
            for item in params.get("ZoneGroup"):
                obj = DescribeSaleZonesGroup()
                obj._deserialize(item)
                self._ZoneGroup.append(obj)
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleZonesGroup(AbstractModel):
    r"""查询售卖地域，提供推荐的可用区组合

    """

    def __init__(self):
        r"""
        :param _ZoneNum: <p>可用区数</p>
        :type ZoneNum: int
        :param _Zones: <p>可用区组合</p>
        :type Zones: list of str
        :param _SupportTypes: <p>支持的类型</p>
        :type SupportTypes: list of str
        :param _AvailableDiskTypes: <p>支持的磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_TCS： 本地盘</li><li>CLOUD_HSSD： 增强型云盘</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableDiskTypes: list of str
        :param _IsSupportServerless: <p>是否支持serverless</p>
        :type IsSupportServerless: bool
        """
        self._ZoneNum = None
        self._Zones = None
        self._SupportTypes = None
        self._AvailableDiskTypes = None
        self._IsSupportServerless = None

    @property
    def ZoneNum(self):
        r"""<p>可用区数</p>
        :rtype: int
        """
        return self._ZoneNum

    @ZoneNum.setter
    def ZoneNum(self, ZoneNum):
        self._ZoneNum = ZoneNum

    @property
    def Zones(self):
        r"""<p>可用区组合</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SupportTypes(self):
        r"""<p>支持的类型</p>
        :rtype: list of str
        """
        return self._SupportTypes

    @SupportTypes.setter
    def SupportTypes(self, SupportTypes):
        self._SupportTypes = SupportTypes

    @property
    def AvailableDiskTypes(self):
        r"""<p>支持的磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_TCS： 本地盘</li><li>CLOUD_HSSD： 增强型云盘</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AvailableDiskTypes

    @AvailableDiskTypes.setter
    def AvailableDiskTypes(self, AvailableDiskTypes):
        self._AvailableDiskTypes = AvailableDiskTypes

    @property
    def IsSupportServerless(self):
        r"""<p>是否支持serverless</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._ZoneNum = params.get("ZoneNum")
        self._Zones = params.get("Zones")
        self._SupportTypes = params.get("SupportTypes")
        self._AvailableDiskTypes = params.get("AvailableDiskTypes")
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleZonesInfo(AbstractModel):
    r"""查询售卖接口，zone信息返回类型

    """

    def __init__(self):
        r"""
        :param _Zone: <p>Zone英文字符串</p>
        :type Zone: str
        :param _ZoneName: <p>Zone中文字符串</p>
        :type ZoneName: str
        :param _Enable: <p>是否售卖，1：售卖；0：不售卖</p>
        :type Enable: int
        :param _IsDefaultMaster: <p>是否是默认主可用区,0不是，1是</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultMaster: int
        :param _AvailableDiskTypes: <p>可用区可选磁盘类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableDiskTypes: list of str
        :param _SupportTypes: <p>是否是独享可用区</p>
        :type SupportTypes: list of str
        :param _IsSupportServerless: <p>是否支持serverless</p>
        :type IsSupportServerless: bool
        """
        self._Zone = None
        self._ZoneName = None
        self._Enable = None
        self._IsDefaultMaster = None
        self._AvailableDiskTypes = None
        self._SupportTypes = None
        self._IsSupportServerless = None

    @property
    def Zone(self):
        r"""<p>Zone英文字符串</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""<p>Zone中文字符串</p>
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Enable(self):
        r"""<p>是否售卖，1：售卖；0：不售卖</p>
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def IsDefaultMaster(self):
        r"""<p>是否是默认主可用区,0不是，1是</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDefaultMaster

    @IsDefaultMaster.setter
    def IsDefaultMaster(self, IsDefaultMaster):
        self._IsDefaultMaster = IsDefaultMaster

    @property
    def AvailableDiskTypes(self):
        r"""<p>可用区可选磁盘类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AvailableDiskTypes

    @AvailableDiskTypes.setter
    def AvailableDiskTypes(self, AvailableDiskTypes):
        self._AvailableDiskTypes = AvailableDiskTypes

    @property
    def SupportTypes(self):
        r"""<p>是否是独享可用区</p>
        :rtype: list of str
        """
        return self._SupportTypes

    @SupportTypes.setter
    def SupportTypes(self, SupportTypes):
        self._SupportTypes = SupportTypes

    @property
    def IsSupportServerless(self):
        r"""<p>是否支持serverless</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._Enable = params.get("Enable")
        self._IsDefaultMaster = params.get("IsDefaultMaster")
        self._AvailableDiskTypes = params.get("AvailableDiskTypes")
        self._SupportTypes = params.get("SupportTypes")
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecsRequest(AbstractModel):
    r"""DescribeSpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FullReplications: <p>全能型副本数，当前支持范围：1-3，默认为3</p>
        :type FullReplications: int
        :param _IsExclusiveInstance: <p>独享实例</p>
        :type IsExclusiveInstance: int
        """
        self._FullReplications = None
        self._IsExclusiveInstance = None

    @property
    def FullReplications(self):
        r"""<p>全能型副本数，当前支持范围：1-3，默认为3</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def IsExclusiveInstance(self):
        r"""<p>独享实例</p>
        :rtype: int
        """
        return self._IsExclusiveInstance

    @IsExclusiveInstance.setter
    def IsExclusiveInstance(self, IsExclusiveInstance):
        self._IsExclusiveInstance = IsExclusiveInstance


    def _deserialize(self, params):
        self._FullReplications = params.get("FullReplications")
        self._IsExclusiveInstance = params.get("IsExclusiveInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecsResponse(AbstractModel):
    r"""DescribeSpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HybridNodeSpecs: <p>对等节点售卖规格列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type HybridNodeSpecs: list of StorageNodeSpec
        :param _ServerlessCcuSpec: <p>svls节点售卖规格列表</p>
        :type ServerlessCcuSpec: list of ServerlessCcu
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HybridNodeSpecs = None
        self._ServerlessCcuSpec = None
        self._RequestId = None

    @property
    def HybridNodeSpecs(self):
        r"""<p>对等节点售卖规格列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StorageNodeSpec
        """
        return self._HybridNodeSpecs

    @HybridNodeSpecs.setter
    def HybridNodeSpecs(self, HybridNodeSpecs):
        self._HybridNodeSpecs = HybridNodeSpecs

    @property
    def ServerlessCcuSpec(self):
        r"""<p>svls节点售卖规格列表</p>
        :rtype: list of ServerlessCcu
        """
        return self._ServerlessCcuSpec

    @ServerlessCcuSpec.setter
    def ServerlessCcuSpec(self, ServerlessCcuSpec):
        self._ServerlessCcuSpec = ServerlessCcuSpec

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
        if params.get("HybridNodeSpecs") is not None:
            self._HybridNodeSpecs = []
            for item in params.get("HybridNodeSpecs"):
                obj = StorageNodeSpec()
                obj._deserialize(item)
                self._HybridNodeSpecs.append(obj)
        if params.get("ServerlessCcuSpec") is not None:
            self._ServerlessCcuSpec = []
            for item in params.get("ServerlessCcuSpec"):
                obj = ServerlessCcu()
                obj._deserialize(item)
                self._ServerlessCcuSpec.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserPrivilegesRequest(AbstractModel):
    r"""DescribeUserPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-5baee8df。
        :type InstanceId: str
        :param _Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param _UserName: 登录用户名。
        :type UserName: str
        :param _DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param _Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param _ObjectType: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :type ObjectType: str
        :param _ColName: 当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限
        :type ColName: str
        """
        self._InstanceId = None
        self._Host = None
        self._UserName = None
        self._DbName = None
        self._Object = None
        self._ObjectType = None
        self._ColName = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-5baee8df。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Host(self):
        r"""用户允许的访问 host，用户名+host唯一确定一个账号。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def UserName(self):
        r"""登录用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DbName(self):
        r"""数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Object(self):
        r"""具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ObjectType(self):
        r"""类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def ColName(self):
        r"""当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Host = params.get("Host")
        self._UserName = params.get("UserName")
        self._DbName = params.get("DbName")
        self._Object = params.get("Object")
        self._ObjectType = params.get("ObjectType")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserPrivilegesResponse(AbstractModel):
    r"""DescribeUserPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Privileges: 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Privileges: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Privileges = None
        self._RequestId = None

    @property
    def Privileges(self):
        r"""权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

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
        self._Privileges = params.get("Privileges")
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    r"""DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

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
        self._InstanceId = params.get("InstanceId")
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
        :param _Users: 用户列表
        :type Users: list of UserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        r"""用户列表
        :rtype: list of UserInfo
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
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
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


class ExpandInstanceRequest(AbstractModel):
    r"""ExpandInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _StorageNodeNum: <p>存储节点扩容至多少个节点，如果没有变化，传当前节点数</p>
        :type StorageNodeNum: int
        :param _Zones: <p>可用区列表</p>
        :type Zones: list of str
        :param _AZMode: <p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
        :type AZMode: int
        :param _PrimaryAZ: <p>AZMode传3时，表示主AZ</p>
        :type PrimaryAZ: str
        :param _FullReplications: <p>全能型副本数，取值范围包括1-3</p>
        :type FullReplications: int
        """
        self._InstanceId = None
        self._StorageNodeNum = None
        self._Zones = None
        self._AZMode = None
        self._PrimaryAZ = None
        self._FullReplications = None

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
    def StorageNodeNum(self):
        r"""<p>存储节点扩容至多少个节点，如果没有变化，传当前节点数</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def Zones(self):
        r"""<p>可用区列表</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def AZMode(self):
        r"""<p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def PrimaryAZ(self):
        r"""<p>AZMode传3时，表示主AZ</p>
        :rtype: str
        """
        return self._PrimaryAZ

    @PrimaryAZ.setter
    def PrimaryAZ(self, PrimaryAZ):
        self._PrimaryAZ = PrimaryAZ

    @property
    def FullReplications(self):
        r"""<p>全能型副本数，取值范围包括1-3</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._Zones = params.get("Zones")
        self._AZMode = params.get("AZMode")
        self._PrimaryAZ = params.get("PrimaryAZ")
        self._FullReplications = params.get("FullReplications")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandInstanceResponse(AbstractModel):
    r"""ExpandInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>异步任务ID，根据此ID可以调用查询任务接口获取任务状态</p>
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>异步任务ID，根据此ID可以调用查询任务接口获取任务状态</p>
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


class InstanceFilter(AbstractModel):
    r"""实例列表过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤key，支持InstanceId、VpcId、SubnetId、Vip、Vport、Status、InstanceName、TagKey
        :type Name: str
        :param _Values: 过滤value
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤key，支持InstanceId、VpcId、SubnetId、Vip、Vport、Status、InstanceName、TagKey
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤value
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
        


class InstanceInfo(AbstractModel):
    r"""实例信息类型

    """

    def __init__(self):
        r"""
        :param _ComputeNodeNum: <p>计算节点数量</p>
        :type ComputeNodeNum: int
        :param _Zone: <p>区域</p>
        :type Zone: str
        :param _CreateVersion: <p>创建实例版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateVersion: str
        :param _InitParams: <p>初始化实例参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InitParams: list of InstanceParam
        :param _Status: <p>实例状态：creating、created、initializing、running、modifying、isolating、isolated、destroying、destroyed</p>
        :type Status: str
        :param _InstanceId: <p>实例id</p>
        :type InstanceId: str
        :param _StorageNodeNum: <p>存储节点数量</p>
        :type StorageNodeNum: int
        :param _ResourceTags: <p>实例标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of ResourceTag
        :param _InstanceName: <p>实例名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Cpu: <p>计算节点cpu核数</p>
        :type Cpu: int
        :param _VpcId: <p>字符型vpcid</p>
        :type VpcId: str
        :param _Mem: <p>计算节点mem，单位GB</p>
        :type Mem: int
        :param _Vip: <p>子网IP</p>
        :type Vip: str
        :param _SubnetId: <p>字符型subnetid</p>
        :type SubnetId: str
        :param _Vport: <p>子网端口</p>
        :type Vport: int
        :param _Disk: <p>存储节点磁盘容量，单位GB</p>
        :type Disk: int
        :param _CreateTime: <p>实例创建时间</p>
        :type CreateTime: str
        :param _Region: <p>实例所属地域</p>
        :type Region: str
        :param _StatusDesc: <p>实例状态中文描述</p>
        :type StatusDesc: str
        :param _MCCpu: <p>管控节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCCpu: int
        :param _MCMem: <p>管控节点CPU大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCMem: int
        :param _ComputerNodeCpu: <p>计算节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputerNodeCpu: int
        :param _ComputerNodeMem: <p>计算节点内存大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputerNodeMem: int
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageNodeMem: int
        :param _MCNum: <p>管控节点数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MCNum: int
        :param _RenewFlag: <p>续费标志</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _PayMode: <p>付费模式，0按量付费；1包年包月</p>
        :type PayMode: str
        :param _AccountTag: <p>用户标签，inner：内部用户；external：外部用户</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountTag: str
        :param _InstanceType: <p>实例架构类型，separate:分离架构；hyper:对等架构</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _StorageType: <p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _DestroyedAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyedAt: str
        :param _ExpireAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireAt: str
        :param _IsolatedAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedAt: str
        :param _IsolatedFrom: <p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedFrom: str
        :param _Replications: <p>1</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Replications: int
        :param _FullReplications: <p>全能型副本数</p>
        :type FullReplications: int
        :param _AppId: <p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _SubAccountUin: <p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _Uin: <p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Zones: <p>AZ信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param _Nodes: <p>实例节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of InstanceNode
        :param _BinlogStatus: <p>binlog是否打开</p>
        :type BinlogStatus: int
        :param _CdcNodeCpu: <p>cdc节点核数</p>
        :type CdcNodeCpu: int
        :param _CdcNodeMem: <p>cdc节点内存大小</p>
        :type CdcNodeMem: int
        :param _CdcNodeNum: <p>cdc节点数</p>
        :type CdcNodeNum: int
        :param _AZMode: <p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AZMode: int
        :param _StandbyFlag: <p>灾备标志位，1: 无灾备关系；2: 灾备主实例；3: 灾备备实例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StandbyFlag: int
        :param _StandbySecondaryNum: <p>连接的备实例数量（仅当 StandbyFlag == 2 时有效）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StandbySecondaryNum: int
        :param _ColumnarNodeCpu: <p>列存节点 cpu 核数</p>
        :type ColumnarNodeCpu: int
        :param _ColumnarNodeMem: <p>列存节点内存大小</p>
        :type ColumnarNodeMem: int
        :param _ColumnarNodeNum: <p>列存节点数</p>
        :type ColumnarNodeNum: int
        :param _ColumnarNodeDisk: <p>列存节点磁盘容量，单位GB</p>
        :type ColumnarNodeDisk: int
        :param _ColumnarNodeStorageType: <p>列存节点磁盘类型</p>
        :type ColumnarNodeStorageType: str
        :param _InstanceCategory: <p>独享标志位，1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）</p>
        :type InstanceCategory: int
        :param _ExclusiveClusterId: <p>dbdc-xxxxx</p>
        :type ExclusiveClusterId: str
        :param _SQLMode: <p>兼容模式</p>
        :type SQLMode: str
        :param _InstanceMode: <p>实例模式</p>
        :type InstanceMode: str
        :param _ClusterId: <p>实例发货平台</p>
        :type ClusterId: str
        :param _AutoScaleConfig: <p>自动扩容配置</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        :param _AnalysisMode: <p>分析引擎模式</p><p>枚举值：</p><ul><li>libra： LibraDB分析引擎模式</li></ul>
        :type AnalysisMode: str
        :param _AnalysisRelationInfos: <p>分析引擎关系信息</p>
        :type AnalysisRelationInfos: list of AnalysisRelationInfo
        """
        self._ComputeNodeNum = None
        self._Zone = None
        self._CreateVersion = None
        self._InitParams = None
        self._Status = None
        self._InstanceId = None
        self._StorageNodeNum = None
        self._ResourceTags = None
        self._InstanceName = None
        self._Cpu = None
        self._VpcId = None
        self._Mem = None
        self._Vip = None
        self._SubnetId = None
        self._Vport = None
        self._Disk = None
        self._CreateTime = None
        self._Region = None
        self._StatusDesc = None
        self._MCCpu = None
        self._MCMem = None
        self._ComputerNodeCpu = None
        self._ComputerNodeMem = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._MCNum = None
        self._RenewFlag = None
        self._PayMode = None
        self._AccountTag = None
        self._InstanceType = None
        self._StorageType = None
        self._DestroyedAt = None
        self._ExpireAt = None
        self._IsolatedAt = None
        self._IsolatedFrom = None
        self._Replications = None
        self._FullReplications = None
        self._AppId = None
        self._SubAccountUin = None
        self._Uin = None
        self._Zones = None
        self._Nodes = None
        self._BinlogStatus = None
        self._CdcNodeCpu = None
        self._CdcNodeMem = None
        self._CdcNodeNum = None
        self._AZMode = None
        self._StandbyFlag = None
        self._StandbySecondaryNum = None
        self._ColumnarNodeCpu = None
        self._ColumnarNodeMem = None
        self._ColumnarNodeNum = None
        self._ColumnarNodeDisk = None
        self._ColumnarNodeStorageType = None
        self._InstanceCategory = None
        self._ExclusiveClusterId = None
        self._SQLMode = None
        self._InstanceMode = None
        self._ClusterId = None
        self._AutoScaleConfig = None
        self._AnalysisMode = None
        self._AnalysisRelationInfos = None

    @property
    def ComputeNodeNum(self):
        warnings.warn("parameter `ComputeNodeNum` is deprecated", DeprecationWarning) 

        r"""<p>计算节点数量</p>
        :rtype: int
        """
        return self._ComputeNodeNum

    @ComputeNodeNum.setter
    def ComputeNodeNum(self, ComputeNodeNum):
        warnings.warn("parameter `ComputeNodeNum` is deprecated", DeprecationWarning) 

        self._ComputeNodeNum = ComputeNodeNum

    @property
    def Zone(self):
        r"""<p>区域</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreateVersion(self):
        r"""<p>创建实例版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def InitParams(self):
        r"""<p>初始化实例参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def Status(self):
        r"""<p>实例状态：creating、created、initializing、running、modifying、isolating、isolated、destroying、destroyed</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def StorageNodeNum(self):
        r"""<p>存储节点数量</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def ResourceTags(self):
        r"""<p>实例标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InstanceName(self):
        r"""<p>实例名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Cpu(self):
        warnings.warn("parameter `Cpu` is deprecated", DeprecationWarning) 

        r"""<p>计算节点cpu核数</p>
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        warnings.warn("parameter `Cpu` is deprecated", DeprecationWarning) 

        self._Cpu = Cpu

    @property
    def VpcId(self):
        r"""<p>字符型vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Mem(self):
        warnings.warn("parameter `Mem` is deprecated", DeprecationWarning) 

        r"""<p>计算节点mem，单位GB</p>
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        warnings.warn("parameter `Mem` is deprecated", DeprecationWarning) 

        self._Mem = Mem

    @property
    def Vip(self):
        r"""<p>子网IP</p>
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def SubnetId(self):
        r"""<p>字符型subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vport(self):
        r"""<p>子网端口</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Disk(self):
        r"""<p>存储节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def CreateTime(self):
        r"""<p>实例创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        r"""<p>实例所属地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def StatusDesc(self):
        r"""<p>实例状态中文描述</p>
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def MCCpu(self):
        warnings.warn("parameter `MCCpu` is deprecated", DeprecationWarning) 

        r"""<p>管控节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MCCpu

    @MCCpu.setter
    def MCCpu(self, MCCpu):
        warnings.warn("parameter `MCCpu` is deprecated", DeprecationWarning) 

        self._MCCpu = MCCpu

    @property
    def MCMem(self):
        warnings.warn("parameter `MCMem` is deprecated", DeprecationWarning) 

        r"""<p>管控节点CPU大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MCMem

    @MCMem.setter
    def MCMem(self, MCMem):
        warnings.warn("parameter `MCMem` is deprecated", DeprecationWarning) 

        self._MCMem = MCMem

    @property
    def ComputerNodeCpu(self):
        warnings.warn("parameter `ComputerNodeCpu` is deprecated", DeprecationWarning) 

        r"""<p>计算节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ComputerNodeCpu

    @ComputerNodeCpu.setter
    def ComputerNodeCpu(self, ComputerNodeCpu):
        warnings.warn("parameter `ComputerNodeCpu` is deprecated", DeprecationWarning) 

        self._ComputerNodeCpu = ComputerNodeCpu

    @property
    def ComputerNodeMem(self):
        warnings.warn("parameter `ComputerNodeMem` is deprecated", DeprecationWarning) 

        r"""<p>计算节点内存大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ComputerNodeMem

    @ComputerNodeMem.setter
    def ComputerNodeMem(self, ComputerNodeMem):
        warnings.warn("parameter `ComputerNodeMem` is deprecated", DeprecationWarning) 

        self._ComputerNodeMem = ComputerNodeMem

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def MCNum(self):
        warnings.warn("parameter `MCNum` is deprecated", DeprecationWarning) 

        r"""<p>管控节点数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MCNum

    @MCNum.setter
    def MCNum(self, MCNum):
        warnings.warn("parameter `MCNum` is deprecated", DeprecationWarning) 

        self._MCNum = MCNum

    @property
    def RenewFlag(self):
        r"""<p>续费标志</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        r"""<p>付费模式，0按量付费；1包年包月</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AccountTag(self):
        r"""<p>用户标签，inner：内部用户；external：外部用户</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountTag

    @AccountTag.setter
    def AccountTag(self, AccountTag):
        self._AccountTag = AccountTag

    @property
    def InstanceType(self):
        r"""<p>实例架构类型，separate:分离架构；hyper:对等架构</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DestroyedAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestroyedAt

    @DestroyedAt.setter
    def DestroyedAt(self, DestroyedAt):
        self._DestroyedAt = DestroyedAt

    @property
    def ExpireAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def IsolatedAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def IsolatedFrom(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedFrom

    @IsolatedFrom.setter
    def IsolatedFrom(self, IsolatedFrom):
        self._IsolatedFrom = IsolatedFrom

    @property
    def Replications(self):
        r"""<p>1</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def FullReplications(self):
        r"""<p>全能型副本数</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def AppId(self):
        r"""<p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SubAccountUin(self):
        r"""<p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def Uin(self):
        r"""<p>账号信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Zones(self):
        r"""<p>AZ信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Nodes(self):
        r"""<p>实例节点</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNode
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def BinlogStatus(self):
        r"""<p>binlog是否打开</p>
        :rtype: int
        """
        return self._BinlogStatus

    @BinlogStatus.setter
    def BinlogStatus(self, BinlogStatus):
        self._BinlogStatus = BinlogStatus

    @property
    def CdcNodeCpu(self):
        warnings.warn("parameter `CdcNodeCpu` is deprecated", DeprecationWarning) 

        r"""<p>cdc节点核数</p>
        :rtype: int
        """
        return self._CdcNodeCpu

    @CdcNodeCpu.setter
    def CdcNodeCpu(self, CdcNodeCpu):
        warnings.warn("parameter `CdcNodeCpu` is deprecated", DeprecationWarning) 

        self._CdcNodeCpu = CdcNodeCpu

    @property
    def CdcNodeMem(self):
        warnings.warn("parameter `CdcNodeMem` is deprecated", DeprecationWarning) 

        r"""<p>cdc节点内存大小</p>
        :rtype: int
        """
        return self._CdcNodeMem

    @CdcNodeMem.setter
    def CdcNodeMem(self, CdcNodeMem):
        warnings.warn("parameter `CdcNodeMem` is deprecated", DeprecationWarning) 

        self._CdcNodeMem = CdcNodeMem

    @property
    def CdcNodeNum(self):
        warnings.warn("parameter `CdcNodeNum` is deprecated", DeprecationWarning) 

        r"""<p>cdc节点数</p>
        :rtype: int
        """
        return self._CdcNodeNum

    @CdcNodeNum.setter
    def CdcNodeNum(self, CdcNodeNum):
        warnings.warn("parameter `CdcNodeNum` is deprecated", DeprecationWarning) 

        self._CdcNodeNum = CdcNodeNum

    @property
    def AZMode(self):
        r"""<p>az模式，1: 单AZ 2: 多AZ非主AZ模式 3: 多AZ主AZ模式</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def StandbyFlag(self):
        r"""<p>灾备标志位，1: 无灾备关系；2: 灾备主实例；3: 灾备备实例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StandbyFlag

    @StandbyFlag.setter
    def StandbyFlag(self, StandbyFlag):
        self._StandbyFlag = StandbyFlag

    @property
    def StandbySecondaryNum(self):
        r"""<p>连接的备实例数量（仅当 StandbyFlag == 2 时有效）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StandbySecondaryNum

    @StandbySecondaryNum.setter
    def StandbySecondaryNum(self, StandbySecondaryNum):
        self._StandbySecondaryNum = StandbySecondaryNum

    @property
    def ColumnarNodeCpu(self):
        r"""<p>列存节点 cpu 核数</p>
        :rtype: int
        """
        return self._ColumnarNodeCpu

    @ColumnarNodeCpu.setter
    def ColumnarNodeCpu(self, ColumnarNodeCpu):
        self._ColumnarNodeCpu = ColumnarNodeCpu

    @property
    def ColumnarNodeMem(self):
        r"""<p>列存节点内存大小</p>
        :rtype: int
        """
        return self._ColumnarNodeMem

    @ColumnarNodeMem.setter
    def ColumnarNodeMem(self, ColumnarNodeMem):
        self._ColumnarNodeMem = ColumnarNodeMem

    @property
    def ColumnarNodeNum(self):
        r"""<p>列存节点数</p>
        :rtype: int
        """
        return self._ColumnarNodeNum

    @ColumnarNodeNum.setter
    def ColumnarNodeNum(self, ColumnarNodeNum):
        self._ColumnarNodeNum = ColumnarNodeNum

    @property
    def ColumnarNodeDisk(self):
        r"""<p>列存节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._ColumnarNodeDisk

    @ColumnarNodeDisk.setter
    def ColumnarNodeDisk(self, ColumnarNodeDisk):
        self._ColumnarNodeDisk = ColumnarNodeDisk

    @property
    def ColumnarNodeStorageType(self):
        r"""<p>列存节点磁盘类型</p>
        :rtype: str
        """
        return self._ColumnarNodeStorageType

    @ColumnarNodeStorageType.setter
    def ColumnarNodeStorageType(self, ColumnarNodeStorageType):
        self._ColumnarNodeStorageType = ColumnarNodeStorageType

    @property
    def InstanceCategory(self):
        r"""<p>独享标志位，1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）</p>
        :rtype: int
        """
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def ExclusiveClusterId(self):
        r"""<p>dbdc-xxxxx</p>
        :rtype: str
        """
        return self._ExclusiveClusterId

    @ExclusiveClusterId.setter
    def ExclusiveClusterId(self, ExclusiveClusterId):
        self._ExclusiveClusterId = ExclusiveClusterId

    @property
    def SQLMode(self):
        r"""<p>兼容模式</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def InstanceMode(self):
        r"""<p>实例模式</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def ClusterId(self):
        warnings.warn("parameter `ClusterId` is deprecated", DeprecationWarning) 

        r"""<p>实例发货平台</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        warnings.warn("parameter `ClusterId` is deprecated", DeprecationWarning) 

        self._ClusterId = ClusterId

    @property
    def AutoScaleConfig(self):
        r"""<p>自动扩容配置</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig

    @property
    def AnalysisMode(self):
        r"""<p>分析引擎模式</p><p>枚举值：</p><ul><li>libra： LibraDB分析引擎模式</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def AnalysisRelationInfos(self):
        r"""<p>分析引擎关系信息</p>
        :rtype: list of AnalysisRelationInfo
        """
        return self._AnalysisRelationInfos

    @AnalysisRelationInfos.setter
    def AnalysisRelationInfos(self, AnalysisRelationInfos):
        self._AnalysisRelationInfos = AnalysisRelationInfos


    def _deserialize(self, params):
        self._ComputeNodeNum = params.get("ComputeNodeNum")
        self._Zone = params.get("Zone")
        self._CreateVersion = params.get("CreateVersion")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._StorageNodeNum = params.get("StorageNodeNum")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._InstanceName = params.get("InstanceName")
        self._Cpu = params.get("Cpu")
        self._VpcId = params.get("VpcId")
        self._Mem = params.get("Mem")
        self._Vip = params.get("Vip")
        self._SubnetId = params.get("SubnetId")
        self._Vport = params.get("Vport")
        self._Disk = params.get("Disk")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._StatusDesc = params.get("StatusDesc")
        self._MCCpu = params.get("MCCpu")
        self._MCMem = params.get("MCMem")
        self._ComputerNodeCpu = params.get("ComputerNodeCpu")
        self._ComputerNodeMem = params.get("ComputerNodeMem")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._MCNum = params.get("MCNum")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._AccountTag = params.get("AccountTag")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._DestroyedAt = params.get("DestroyedAt")
        self._ExpireAt = params.get("ExpireAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._IsolatedFrom = params.get("IsolatedFrom")
        self._Replications = params.get("Replications")
        self._FullReplications = params.get("FullReplications")
        self._AppId = params.get("AppId")
        self._SubAccountUin = params.get("SubAccountUin")
        self._Uin = params.get("Uin")
        self._Zones = params.get("Zones")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._BinlogStatus = params.get("BinlogStatus")
        self._CdcNodeCpu = params.get("CdcNodeCpu")
        self._CdcNodeMem = params.get("CdcNodeMem")
        self._CdcNodeNum = params.get("CdcNodeNum")
        self._AZMode = params.get("AZMode")
        self._StandbyFlag = params.get("StandbyFlag")
        self._StandbySecondaryNum = params.get("StandbySecondaryNum")
        self._ColumnarNodeCpu = params.get("ColumnarNodeCpu")
        self._ColumnarNodeMem = params.get("ColumnarNodeMem")
        self._ColumnarNodeNum = params.get("ColumnarNodeNum")
        self._ColumnarNodeDisk = params.get("ColumnarNodeDisk")
        self._ColumnarNodeStorageType = params.get("ColumnarNodeStorageType")
        self._InstanceCategory = params.get("InstanceCategory")
        self._ExclusiveClusterId = params.get("ExclusiveClusterId")
        self._SQLMode = params.get("SQLMode")
        self._InstanceMode = params.get("InstanceMode")
        self._ClusterId = params.get("ClusterId")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("AnalysisRelationInfos") is not None:
            self._AnalysisRelationInfos = []
            for item in params.get("AnalysisRelationInfos"):
                obj = AnalysisRelationInfo()
                obj._deserialize(item)
                self._AnalysisRelationInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    r"""节点信息

    """

    def __init__(self):
        r"""
        :param _ID: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _NodeId: Node Id
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _Ip: 实例Ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _EniIp: 实例EniIp
注意：此字段可能返回 null，表示取不到有效值。
        :type EniIp: str
        :param _Port: 实例Port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _SpecCode: 实例SpecCode
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecCode: str
        :param _NodeName: 实例NodeName
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _Cpu: 实例Cpu
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Mem: 实例Mem
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param _Disk: 实例Disk
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: int
        :param _Type: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Version: 实例版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Zone: 实例地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _LocalDNS: 实例LocalDNS
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDNS: str
        :param _Region: 实例Region
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _LogDisk: 实例日志盘
注意：此字段可能返回 null，表示取不到有效值。
        :type LogDisk: int
        :param _DataDisk: 实例数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisk: int
        :param _ZoneID: 实例ZoneID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneID: str
        :param _SpecName: 实例SpecName
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _Replicas: 实例Replicas
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _Shards: 实例Shards
注意：此字段可能返回 null，表示取不到有效值。
        :type Shards: int
        :param _DataReplicas: 实例数据副本
注意：此字段可能返回 null，表示取不到有效值。
        :type DataReplicas: int
        :param _Params: 实例初始化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _StorageType: 存储介质, CLOUD_PREMIUM:高性能云盘，CLOUD_SSD: SSD 云盘，CLOUD_HSSD: HSSD 云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        """
        self._ID = None
        self._InstanceId = None
        self._NodeId = None
        self._Ip = None
        self._EniIp = None
        self._Port = None
        self._SpecCode = None
        self._NodeName = None
        self._Cpu = None
        self._Mem = None
        self._Disk = None
        self._Type = None
        self._Status = None
        self._Version = None
        self._Zone = None
        self._LocalDNS = None
        self._Region = None
        self._LogDisk = None
        self._DataDisk = None
        self._ZoneID = None
        self._SpecName = None
        self._Replicas = None
        self._Shards = None
        self._DataReplicas = None
        self._Params = None
        self._StorageType = None

    @property
    def ID(self):
        r"""主键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeId(self):
        r"""Node Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Ip(self):
        r"""实例Ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def EniIp(self):
        r"""实例EniIp
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Port(self):
        r"""实例Port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SpecCode(self):
        r"""实例SpecCode
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def NodeName(self):
        r"""实例NodeName
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Cpu(self):
        r"""实例Cpu
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""实例Mem
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Disk(self):
        r"""实例Disk
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def Type(self):
        r"""实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        r"""实例版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Zone(self):
        r"""实例地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def LocalDNS(self):
        r"""实例LocalDNS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LocalDNS

    @LocalDNS.setter
    def LocalDNS(self, LocalDNS):
        self._LocalDNS = LocalDNS

    @property
    def Region(self):
        r"""实例Region
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def LogDisk(self):
        r"""实例日志盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogDisk

    @LogDisk.setter
    def LogDisk(self, LogDisk):
        self._LogDisk = LogDisk

    @property
    def DataDisk(self):
        r"""实例数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def ZoneID(self):
        r"""实例ZoneID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneID

    @ZoneID.setter
    def ZoneID(self, ZoneID):
        self._ZoneID = ZoneID

    @property
    def SpecName(self):
        r"""实例SpecName
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Replicas(self):
        r"""实例Replicas
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Shards(self):
        r"""实例Shards
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def DataReplicas(self):
        r"""实例数据副本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataReplicas

    @DataReplicas.setter
    def DataReplicas(self, DataReplicas):
        self._DataReplicas = DataReplicas

    @property
    def Params(self):
        r"""实例初始化参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def StorageType(self):
        r"""存储介质, CLOUD_PREMIUM:高性能云盘，CLOUD_SSD: SSD 云盘，CLOUD_HSSD: HSSD 云盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._NodeId = params.get("NodeId")
        self._Ip = params.get("Ip")
        self._EniIp = params.get("EniIp")
        self._Port = params.get("Port")
        self._SpecCode = params.get("SpecCode")
        self._NodeName = params.get("NodeName")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Disk = params.get("Disk")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        self._Zone = params.get("Zone")
        self._LocalDNS = params.get("LocalDNS")
        self._Region = params.get("Region")
        self._LogDisk = params.get("LogDisk")
        self._DataDisk = params.get("DataDisk")
        self._ZoneID = params.get("ZoneID")
        self._SpecName = params.get("SpecName")
        self._Replicas = params.get("Replicas")
        self._Shards = params.get("Shards")
        self._DataReplicas = params.get("DataReplicas")
        self._Params = params.get("Params")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    r"""初始化实例参数

    """

    def __init__(self):
        r"""
        :param _Param: 配置参数key
        :type Param: str
        :param _Value: 配置参数value
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        r"""配置参数key
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""配置参数value
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


class LogBackupStatisticsModel(AbstractModel):
    r"""日志备份统计对象

    """

    def __init__(self):
        r"""
        :param _AverageSizePerBackup: <p>平均每个日志备份大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerBackup: int
        :param _AverageSizePerDay: <p>平均每天日志备份大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageSizePerDay: int
        :param _TotalCount: <p>日志备份个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalSize: <p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self._AverageSizePerBackup = None
        self._AverageSizePerDay = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AverageSizePerBackup(self):
        r"""<p>平均每个日志备份大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerBackup

    @AverageSizePerBackup.setter
    def AverageSizePerBackup(self, AverageSizePerBackup):
        self._AverageSizePerBackup = AverageSizePerBackup

    @property
    def AverageSizePerDay(self):
        r"""<p>平均每天日志备份大小,单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def TotalCount(self):
        r"""<p>日志备份个数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""<p>日志备份大小，单位Byte</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AverageSizePerBackup = params.get("AverageSizePerBackup")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaintenanceWindowInfo(AbstractModel):
    r"""维护窗口配置

    """

    def __init__(self):
        r"""
        :param _StartTime: 
        :type StartTime: int
        :param _Duration: 
        :type Duration: int
        :param _WeekDays: 
        :type WeekDays: list of str
        """
        self._StartTime = None
        self._Duration = None
        self._WeekDays = None

    @property
    def StartTime(self):
        r"""
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        r"""
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def WeekDays(self):
        r"""
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagRequest(AbstractModel):
    r"""ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>需要修改的实例列表</p>
        :type InstanceIds: list of str
        :param _AutoRenewFlag: <p>1表示开启自动续费，0为关闭自动续费</p>
        :type AutoRenewFlag: int
        """
        self._InstanceIds = None
        self._AutoRenewFlag = None

    @property
    def InstanceIds(self):
        r"""<p>需要修改的实例列表</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenewFlag(self):
        r"""<p>1表示开启自动续费，0为关闭自动续费</p>
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
        :param _BackupPolicy: <p>备份策略</p>
        :type BackupPolicy: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        """
        self._BackupPolicy = None
        self._InstanceId = None

    @property
    def BackupPolicy(self):
        r"""<p>备份策略</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        """
        return self._BackupPolicy

    @BackupPolicy.setter
    def BackupPolicy(self, BackupPolicy):
        self._BackupPolicy = BackupPolicy

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
        :param _IsSuccess: <p>是否成功</p>
        :type IsSuccess: bool
        :param _Msg: <p>消息</p>
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
        r"""<p>消息</p>
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


class ModifyUserPrivilegesRequest(AbstractModel):
    r"""ModifyUserPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql3-5baee8df。
        :type InstanceId: str
        :param _Users: 登录用户名和主机信息
        :type Users: list of User
        :param _GlobalPrivileges: 全局权限
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Database级别权限
        :type DatabasePrivileges: list of DatabasePrivileges
        :param _TablePrivileges: Table级别权限
        :type TablePrivileges: list of TablePrivileges
        """
        self._InstanceId = None
        self._Users = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None

    @property
    def InstanceId(self):
        r"""实例 ID，形如：tdsql3-5baee8df。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        r"""登录用户名和主机信息
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def GlobalPrivileges(self):
        r"""全局权限
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        r"""Database级别权限
        :rtype: list of DatabasePrivileges
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        r"""Table级别权限
        :rtype: list of TablePrivileges
        """
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPrivilegesResponse(AbstractModel):
    r"""ModifyUserPrivileges返回参数结构体

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


class NodeInfo(AbstractModel):
    r"""节点信息类型

    """

    def __init__(self):
        r"""
        :param _IP: <p>节点IP信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _Type: <p>节点类型，如sqlengine，tdstore，mc</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _NodeId: <p>节点唯一标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _Port: <p>节点端口信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Zone: <p>节点所属可用区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Host: <p>节点所属机器ip</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _BinlogInfo: <p>节点日志服务信息</p>
        :type BinlogInfo: list of BinlogInfo
        :param _Cpu: <p>节点cpu个数</p>
        :type Cpu: int
        :param _Mem: <p>节点mem大小</p>
        :type Mem: int
        :param _DataDisk: <p>节点磁盘大小</p>
        :type DataDisk: int
        """
        self._IP = None
        self._Type = None
        self._NodeId = None
        self._Port = None
        self._Zone = None
        self._Host = None
        self._BinlogInfo = None
        self._Cpu = None
        self._Mem = None
        self._DataDisk = None

    @property
    def IP(self):
        r"""<p>节点IP信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Type(self):
        r"""<p>节点类型，如sqlengine，tdstore，mc</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeId(self):
        r"""<p>节点唯一标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Port(self):
        r"""<p>节点端口信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Zone(self):
        r"""<p>节点所属可用区</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Host(self):
        r"""<p>节点所属机器ip</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def BinlogInfo(self):
        r"""<p>节点日志服务信息</p>
        :rtype: list of BinlogInfo
        """
        return self._BinlogInfo

    @BinlogInfo.setter
    def BinlogInfo(self, BinlogInfo):
        self._BinlogInfo = BinlogInfo

    @property
    def Cpu(self):
        r"""<p>节点cpu个数</p>
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""<p>节点mem大小</p>
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def DataDisk(self):
        r"""<p>节点磁盘大小</p>
        :rtype: int
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Type = params.get("Type")
        self._NodeId = params.get("NodeId")
        self._Port = params.get("Port")
        self._Zone = params.get("Zone")
        self._Host = params.get("Host")
        if params.get("BinlogInfo") is not None:
            self._BinlogInfo = []
            for item in params.get("BinlogInfo"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self._BinlogInfo.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._DataDisk = params.get("DataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ResourceTag(AbstractModel):
    r"""tag参数

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键key
        :type TagKey: str
        :param _TagValue: 标签值value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值value
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
        


class RestartDBInstancesRequest(AbstractModel):
    r"""RestartDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>需要重启的实例ID的数组</p>
        :type InstanceIds: list of str
        :param _RestartTime: <p>重启时间，不传表示立即重启</p>
        :type RestartTime: str
        """
        self._InstanceIds = None
        self._RestartTime = None

    @property
    def InstanceIds(self):
        r"""<p>需要重启的实例ID的数组</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RestartTime(self):
        r"""<p>重启时间，不传表示立即重启</p>
        :rtype: str
        """
        return self._RestartTime

    @RestartTime.setter
    def RestartTime(self, RestartTime):
        self._RestartTime = RestartTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RestartTime = params.get("RestartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    r"""RestartDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>异步任务id</p>
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>异步任务id</p>
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
        


class ServerlessCcu(AbstractModel):
    r"""serverless实例的ccu规格

    """

    def __init__(self):
        r"""
        :param _MinCcu: <p>ccu最小值</p>
        :type MinCcu: int
        :param _MaxCcu: <p>ccu最大值范围</p>
        :type MaxCcu: list of int
        """
        self._MinCcu = None
        self._MaxCcu = None

    @property
    def MinCcu(self):
        r"""<p>ccu最小值</p>
        :rtype: int
        """
        return self._MinCcu

    @MinCcu.setter
    def MinCcu(self, MinCcu):
        self._MinCcu = MinCcu

    @property
    def MaxCcu(self):
        r"""<p>ccu最大值范围</p>
        :rtype: list of int
        """
        return self._MaxCcu

    @MaxCcu.setter
    def MaxCcu(self, MaxCcu):
        self._MaxCcu = MaxCcu


    def _deserialize(self, params):
        self._MinCcu = params.get("MinCcu")
        self._MaxCcu = params.get("MaxCcu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageNodeSpec(AbstractModel):
    r"""存储节点规格

    """

    def __init__(self):
        r"""
        :param _SpecCode: <p>规格码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecCode: str
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
        :type StorageNodeMem: int
        :param _StorageNodeMaxNum: <p>存储节点最大数量</p>
        :type StorageNodeMaxNum: int
        :param _StorageNodeMaxDisk: <p>存储节点磁盘大小上限</p>
        :type StorageNodeMaxDisk: int
        :param _StorageNodeMinNum: <p>存储节点最小数量</p>
        :type StorageNodeMinNum: int
        :param _StorageNodeMinDisk: <p>存储节点磁盘大小下限</p>
        :type StorageNodeMinDisk: int
        :param _StorageType: <p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _StorageNodeDefaultDisk: <p>存储节点默认磁盘大小，用于前端展示</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageNodeDefaultDisk: int
        :param _InstanceMode: <p>规格支持计费模式列表</p>
        :type InstanceMode: list of str
        :param _DiskTypeCategory: <p>磁盘类型CLOUD_DISK：云盘LOCAL_DISK：本地盘</p>
        :type DiskTypeCategory: str
        """
        self._SpecCode = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._StorageNodeMaxNum = None
        self._StorageNodeMaxDisk = None
        self._StorageNodeMinNum = None
        self._StorageNodeMinDisk = None
        self._StorageType = None
        self._StorageNodeDefaultDisk = None
        self._InstanceMode = None
        self._DiskTypeCategory = None

    @property
    def SpecCode(self):
        r"""<p>规格码</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def StorageNodeMaxNum(self):
        r"""<p>存储节点最大数量</p>
        :rtype: int
        """
        return self._StorageNodeMaxNum

    @StorageNodeMaxNum.setter
    def StorageNodeMaxNum(self, StorageNodeMaxNum):
        self._StorageNodeMaxNum = StorageNodeMaxNum

    @property
    def StorageNodeMaxDisk(self):
        r"""<p>存储节点磁盘大小上限</p>
        :rtype: int
        """
        return self._StorageNodeMaxDisk

    @StorageNodeMaxDisk.setter
    def StorageNodeMaxDisk(self, StorageNodeMaxDisk):
        self._StorageNodeMaxDisk = StorageNodeMaxDisk

    @property
    def StorageNodeMinNum(self):
        r"""<p>存储节点最小数量</p>
        :rtype: int
        """
        return self._StorageNodeMinNum

    @StorageNodeMinNum.setter
    def StorageNodeMinNum(self, StorageNodeMinNum):
        self._StorageNodeMinNum = StorageNodeMinNum

    @property
    def StorageNodeMinDisk(self):
        r"""<p>存储节点磁盘大小下限</p>
        :rtype: int
        """
        return self._StorageNodeMinDisk

    @StorageNodeMinDisk.setter
    def StorageNodeMinDisk(self, StorageNodeMinDisk):
        self._StorageNodeMinDisk = StorageNodeMinDisk

    @property
    def StorageType(self):
        r"""<p>磁盘类型，CLOUD_HSSD增强型SSD,CLOUD_TCS本地SSD盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageNodeDefaultDisk(self):
        r"""<p>存储节点默认磁盘大小，用于前端展示</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageNodeDefaultDisk

    @StorageNodeDefaultDisk.setter
    def StorageNodeDefaultDisk(self, StorageNodeDefaultDisk):
        self._StorageNodeDefaultDisk = StorageNodeDefaultDisk

    @property
    def InstanceMode(self):
        r"""<p>规格支持计费模式列表</p>
        :rtype: list of str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def DiskTypeCategory(self):
        r"""<p>磁盘类型CLOUD_DISK：云盘LOCAL_DISK：本地盘</p>
        :rtype: str
        """
        return self._DiskTypeCategory

    @DiskTypeCategory.setter
    def DiskTypeCategory(self, DiskTypeCategory):
        self._DiskTypeCategory = DiskTypeCategory


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._StorageNodeMaxNum = params.get("StorageNodeMaxNum")
        self._StorageNodeMaxDisk = params.get("StorageNodeMaxDisk")
        self._StorageNodeMinNum = params.get("StorageNodeMinNum")
        self._StorageNodeMinDisk = params.get("StorageNodeMinDisk")
        self._StorageType = params.get("StorageType")
        self._StorageNodeDefaultDisk = params.get("StorageNodeDefaultDisk")
        self._InstanceMode = params.get("InstanceMode")
        self._DiskTypeCategory = params.get("DiskTypeCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivileges(AbstractModel):
    r"""表级别权限

    """

    def __init__(self):
        r"""
        :param _Database: DATABASE名
        :type Database: str
        :param _Table: 表名
        :type Table: str
        :param _Privileges: 权限列表
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        r"""DATABASE名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        r"""表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        r"""权限列表
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _SpecCode: <p>实例规格码</p>
        :type SpecCode: str
        :param _Disk: <p>存储节点磁盘容量，单位GB</p>
        :type Disk: int
        :param _StorageNodeCpu: <p>存储节点CPU核数</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>存储节点内存大小</p>
        :type StorageNodeMem: int
        :param _StorageType: <p>磁盘类型，需要修改磁盘类型时传</p>
        :type StorageType: str
        """
        self._InstanceId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._StorageType = None

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
    def SpecCode(self):
        r"""<p>实例规格码</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>存储节点磁盘容量，单位GB</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeCpu(self):
        r"""<p>存储节点CPU核数</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>存储节点内存大小</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def StorageType(self):
        r"""<p>磁盘类型，需要修改磁盘类型时传</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    r"""UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>任务ID</p>
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>任务ID</p>
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


class User(AbstractModel):
    r"""数据库账号信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Host: 主机
        :type Host: str
        """
        self._UserName = None
        self._Host = None

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
    def Host(self):
        r"""主机
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    r"""用户信息类型

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Description: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Host: 主机IP，IP段以%结尾，表示允许该IP段的所有IP
        :type Host: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._UserName = None
        self._Description = None
        self._Host = None
        self._CreateTime = None
        self._UpdateTime = None

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
    def Description(self):
        r"""用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Host(self):
        r"""主机IP，IP段以%结尾，表示允许该IP段的所有IP
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

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
        self._UserName = params.get("UserName")
        self._Description = params.get("Description")
        self._Host = params.get("Host")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        