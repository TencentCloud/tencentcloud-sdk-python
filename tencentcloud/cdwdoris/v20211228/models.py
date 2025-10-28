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


class ActionAlterUserRequest(AbstractModel):
    r"""ActionAlterUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.cdwdoris.v20211228.models.UserInfo`
        :param _ApiType: api接口类型
        :type ApiType: str
        :param _UserPrivilege: 用户权限类型 0:普通用户 1:管理员
        :type UserPrivilege: int
        :param _ComputeGroups: 计算组列表
        :type ComputeGroups: list of str
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._UserInfo = None
        self._ApiType = None
        self._UserPrivilege = None
        self._ComputeGroups = None
        self._InstanceId = None

    @property
    def UserInfo(self):
        r"""用户信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def ApiType(self):
        r"""api接口类型
        :rtype: str
        """
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def UserPrivilege(self):
        r"""用户权限类型 0:普通用户 1:管理员
        :rtype: int
        """
        return self._UserPrivilege

    @UserPrivilege.setter
    def UserPrivilege(self, UserPrivilege):
        self._UserPrivilege = UserPrivilege

    @property
    def ComputeGroups(self):
        r"""计算组列表
        :rtype: list of str
        """
        return self._ComputeGroups

    @ComputeGroups.setter
    def ComputeGroups(self, ComputeGroups):
        self._ComputeGroups = ComputeGroups

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._ApiType = params.get("ApiType")
        self._UserPrivilege = params.get("UserPrivilege")
        self._ComputeGroups = params.get("ComputeGroups")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterUserResponse(AbstractModel):
    r"""ActionAlterUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class AttachCBSSpec(AbstractModel):
    r"""集群内节点的规格磁盘规格描述

    """

    def __init__(self):
        r"""
        :param _DiskType: 节点磁盘类型，例如“CLOUD_SSD”\"CLOUD_PREMIUM"
        :type DiskType: str
        :param _DiskSize: 磁盘容量，单位G
        :type DiskSize: int
        :param _DiskCount: 磁盘总数
        :type DiskCount: int
        :param _DiskDesc: 描述
        :type DiskDesc: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None
        self._DiskDesc = None

    @property
    def DiskType(self):
        r"""节点磁盘类型，例如“CLOUD_SSD”\"CLOUD_PREMIUM"
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""磁盘容量，单位G
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        r"""磁盘总数
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskDesc(self):
        r"""描述
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        self._DiskDesc = params.get("DiskDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackUpJobDisplay(AbstractModel):
    r"""备份实例详情

    """

    def __init__(self):
        r"""
        :param _JobId: 备份实例id
        :type JobId: int
        :param _Snapshot: 备份实例名
        :type Snapshot: str
        :param _BackUpSize: 备份数据量
        :type BackUpSize: int
        :param _BackUpSingleSize: 备份单副本数据量
        :type BackUpSingleSize: int
        :param _BackUpTime: 实例创建时间
        :type BackUpTime: str
        :param _ExpireTime: 实例过期时间
        :type ExpireTime: str
        :param _JobStatus: 实例状态
        :type JobStatus: str
        :param _BackupType: 0为默认。1时是对远端的doris进行备份，不周期，一次性
        :type BackupType: int
        :param _BackupTimeType: 0为默认。1时是立即备份。2时是迁移
        :type BackupTimeType: int
        :param _DorisSourceInfo: 远端doris的连接信息
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _JobStatusNum: 实例状态对应的数值
        :type JobStatusNum: int
        :param _BackupCosInfo: 备份实例中关于cos的信息	
        :type BackupCosInfo: :class:`tencentcloud.cdwdoris.v20211228.models.BackupCosInfo`
        :param _IsUserDefineBucket: 是否使用的自定义桶
        :type IsUserDefineBucket: bool
        :param _ErrorReason: 错误原因
        :type ErrorReason: str
        :param _SnapshotRemainPolicy: 快照保留策略
        :type SnapshotRemainPolicy: :class:`tencentcloud.cdwdoris.v20211228.models.SnapshotRemainPolicy`
        :param _IsolationCount: 隔离次数
        :type IsolationCount: int
        """
        self._JobId = None
        self._Snapshot = None
        self._BackUpSize = None
        self._BackUpSingleSize = None
        self._BackUpTime = None
        self._ExpireTime = None
        self._JobStatus = None
        self._BackupType = None
        self._BackupTimeType = None
        self._DorisSourceInfo = None
        self._JobStatusNum = None
        self._BackupCosInfo = None
        self._IsUserDefineBucket = None
        self._ErrorReason = None
        self._SnapshotRemainPolicy = None
        self._IsolationCount = None

    @property
    def JobId(self):
        r"""备份实例id
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Snapshot(self):
        r"""备份实例名
        :rtype: str
        """
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def BackUpSize(self):
        r"""备份数据量
        :rtype: int
        """
        return self._BackUpSize

    @BackUpSize.setter
    def BackUpSize(self, BackUpSize):
        self._BackUpSize = BackUpSize

    @property
    def BackUpSingleSize(self):
        r"""备份单副本数据量
        :rtype: int
        """
        return self._BackUpSingleSize

    @BackUpSingleSize.setter
    def BackUpSingleSize(self, BackUpSingleSize):
        self._BackUpSingleSize = BackUpSingleSize

    @property
    def BackUpTime(self):
        r"""实例创建时间
        :rtype: str
        """
        return self._BackUpTime

    @BackUpTime.setter
    def BackUpTime(self, BackUpTime):
        self._BackUpTime = BackUpTime

    @property
    def ExpireTime(self):
        r"""实例过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def JobStatus(self):
        r"""实例状态
        :rtype: str
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def BackupType(self):
        r"""0为默认。1时是对远端的doris进行备份，不周期，一次性
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupTimeType(self):
        r"""0为默认。1时是立即备份。2时是迁移
        :rtype: int
        """
        return self._BackupTimeType

    @BackupTimeType.setter
    def BackupTimeType(self, BackupTimeType):
        self._BackupTimeType = BackupTimeType

    @property
    def DorisSourceInfo(self):
        r"""远端doris的连接信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        self._DorisSourceInfo = DorisSourceInfo

    @property
    def JobStatusNum(self):
        r"""实例状态对应的数值
        :rtype: int
        """
        return self._JobStatusNum

    @JobStatusNum.setter
    def JobStatusNum(self, JobStatusNum):
        self._JobStatusNum = JobStatusNum

    @property
    def BackupCosInfo(self):
        r"""备份实例中关于cos的信息	
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.BackupCosInfo`
        """
        return self._BackupCosInfo

    @BackupCosInfo.setter
    def BackupCosInfo(self, BackupCosInfo):
        self._BackupCosInfo = BackupCosInfo

    @property
    def IsUserDefineBucket(self):
        r"""是否使用的自定义桶
        :rtype: bool
        """
        return self._IsUserDefineBucket

    @IsUserDefineBucket.setter
    def IsUserDefineBucket(self, IsUserDefineBucket):
        self._IsUserDefineBucket = IsUserDefineBucket

    @property
    def ErrorReason(self):
        r"""错误原因
        :rtype: str
        """
        return self._ErrorReason

    @ErrorReason.setter
    def ErrorReason(self, ErrorReason):
        self._ErrorReason = ErrorReason

    @property
    def SnapshotRemainPolicy(self):
        r"""快照保留策略
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.SnapshotRemainPolicy`
        """
        return self._SnapshotRemainPolicy

    @SnapshotRemainPolicy.setter
    def SnapshotRemainPolicy(self, SnapshotRemainPolicy):
        self._SnapshotRemainPolicy = SnapshotRemainPolicy

    @property
    def IsolationCount(self):
        r"""隔离次数
        :rtype: int
        """
        return self._IsolationCount

    @IsolationCount.setter
    def IsolationCount(self, IsolationCount):
        self._IsolationCount = IsolationCount


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Snapshot = params.get("Snapshot")
        self._BackUpSize = params.get("BackUpSize")
        self._BackUpSingleSize = params.get("BackUpSingleSize")
        self._BackUpTime = params.get("BackUpTime")
        self._ExpireTime = params.get("ExpireTime")
        self._JobStatus = params.get("JobStatus")
        self._BackupType = params.get("BackupType")
        self._BackupTimeType = params.get("BackupTimeType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        self._JobStatusNum = params.get("JobStatusNum")
        if params.get("BackupCosInfo") is not None:
            self._BackupCosInfo = BackupCosInfo()
            self._BackupCosInfo._deserialize(params.get("BackupCosInfo"))
        self._IsUserDefineBucket = params.get("IsUserDefineBucket")
        self._ErrorReason = params.get("ErrorReason")
        if params.get("SnapshotRemainPolicy") is not None:
            self._SnapshotRemainPolicy = SnapshotRemainPolicy()
            self._SnapshotRemainPolicy._deserialize(params.get("SnapshotRemainPolicy"))
        self._IsolationCount = params.get("IsolationCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupCosInfo(AbstractModel):
    r"""备份实例中关于cos的信息

    """

    def __init__(self):
        r"""
        :param _CosBucket: 备份文件所在的cos桶
        :type CosBucket: str
        :param _CosPath: 备份文件所在的完整cos路径
        :type CosPath: str
        :param _SnapShotPath: 备份文件名称
        :type SnapShotPath: str
        :param _Region: cos桶所在地域
        :type Region: str
        """
        self._CosBucket = None
        self._CosPath = None
        self._SnapShotPath = None
        self._Region = None

    @property
    def CosBucket(self):
        r"""备份文件所在的cos桶
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosPath(self):
        r"""备份文件所在的完整cos路径
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def SnapShotPath(self):
        r"""备份文件名称
        :rtype: str
        """
        return self._SnapShotPath

    @SnapShotPath.setter
    def SnapShotPath(self, SnapShotPath):
        self._SnapShotPath = SnapShotPath

    @property
    def Region(self):
        r"""cos桶所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._CosPath = params.get("CosPath")
        self._SnapShotPath = params.get("SnapShotPath")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStatus(AbstractModel):
    r"""备份任务的进度详情

    """

    def __init__(self):
        r"""
        :param _JobId: 备份任务id
        :type JobId: int
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _DbName: 库名
        :type DbName: str
        :param _State: 状态
        :type State: str
        :param _BackupObjects: 备份对象
        :type BackupObjects: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _SnapshotFinishedTime: 快照结束时间
        :type SnapshotFinishedTime: str
        :param _UploadFinishedTime: 上传结束时间
        :type UploadFinishedTime: str
        :param _FinishedTime: 结束时间
        :type FinishedTime: str
        :param _UnfinishedTasks: 未完成任务
        :type UnfinishedTasks: str
        :param _Progress: 进度
        :type Progress: str
        :param _TaskErrMsg: 错误信息
        :type TaskErrMsg: str
        :param _Status: 状态
        :type Status: str
        :param _Timeout: 超时信息
        :type Timeout: int
        :param _BackupJobId: 备份实例id
        :type BackupJobId: int
        :param _TaskId: 实例对应Snapshot的id
        :type TaskId: int
        """
        self._JobId = None
        self._SnapshotName = None
        self._DbName = None
        self._State = None
        self._BackupObjects = None
        self._CreateTime = None
        self._SnapshotFinishedTime = None
        self._UploadFinishedTime = None
        self._FinishedTime = None
        self._UnfinishedTasks = None
        self._Progress = None
        self._TaskErrMsg = None
        self._Status = None
        self._Timeout = None
        self._BackupJobId = None
        self._TaskId = None

    @property
    def JobId(self):
        r"""备份任务id
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def DbName(self):
        r"""库名
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def State(self):
        r"""状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def BackupObjects(self):
        r"""备份对象
        :rtype: str
        """
        return self._BackupObjects

    @BackupObjects.setter
    def BackupObjects(self, BackupObjects):
        self._BackupObjects = BackupObjects

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
    def SnapshotFinishedTime(self):
        r"""快照结束时间
        :rtype: str
        """
        return self._SnapshotFinishedTime

    @SnapshotFinishedTime.setter
    def SnapshotFinishedTime(self, SnapshotFinishedTime):
        self._SnapshotFinishedTime = SnapshotFinishedTime

    @property
    def UploadFinishedTime(self):
        r"""上传结束时间
        :rtype: str
        """
        return self._UploadFinishedTime

    @UploadFinishedTime.setter
    def UploadFinishedTime(self, UploadFinishedTime):
        self._UploadFinishedTime = UploadFinishedTime

    @property
    def FinishedTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def UnfinishedTasks(self):
        r"""未完成任务
        :rtype: str
        """
        return self._UnfinishedTasks

    @UnfinishedTasks.setter
    def UnfinishedTasks(self, UnfinishedTasks):
        self._UnfinishedTasks = UnfinishedTasks

    @property
    def Progress(self):
        r"""进度
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskErrMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._TaskErrMsg

    @TaskErrMsg.setter
    def TaskErrMsg(self, TaskErrMsg):
        self._TaskErrMsg = TaskErrMsg

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
    def Timeout(self):
        r"""超时信息
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def BackupJobId(self):
        r"""备份实例id
        :rtype: int
        """
        return self._BackupJobId

    @BackupJobId.setter
    def BackupJobId(self, BackupJobId):
        self._BackupJobId = BackupJobId

    @property
    def TaskId(self):
        r"""实例对应Snapshot的id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._SnapshotName = params.get("SnapshotName")
        self._DbName = params.get("DbName")
        self._State = params.get("State")
        self._BackupObjects = params.get("BackupObjects")
        self._CreateTime = params.get("CreateTime")
        self._SnapshotFinishedTime = params.get("SnapshotFinishedTime")
        self._UploadFinishedTime = params.get("UploadFinishedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._UnfinishedTasks = params.get("UnfinishedTasks")
        self._Progress = params.get("Progress")
        self._TaskErrMsg = params.get("TaskErrMsg")
        self._Status = params.get("Status")
        self._Timeout = params.get("Timeout")
        self._BackupJobId = params.get("BackupJobId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTableContent(AbstractModel):
    r"""备份表信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库
        :type Database: str
        :param _Table: 表
        :type Table: str
        :param _TotalBytes: 表总字节数
        :type TotalBytes: int
        :param _SingleReplicaBytes: 表单个副本的大小
        :type SingleReplicaBytes: str
        :param _BackupStatus: 备份状态
        :type BackupStatus: int
        :param _BackupErrorMsg: 备份的错误信息
        :type BackupErrorMsg: str
        :param _IsOpenCoolDown: 该库表是否绑定降冷策略
        :type IsOpenCoolDown: bool
        """
        self._Database = None
        self._Table = None
        self._TotalBytes = None
        self._SingleReplicaBytes = None
        self._BackupStatus = None
        self._BackupErrorMsg = None
        self._IsOpenCoolDown = None

    @property
    def Database(self):
        r"""数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        r"""表
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TotalBytes(self):
        r"""表总字节数
        :rtype: int
        """
        return self._TotalBytes

    @TotalBytes.setter
    def TotalBytes(self, TotalBytes):
        self._TotalBytes = TotalBytes

    @property
    def SingleReplicaBytes(self):
        r"""表单个副本的大小
        :rtype: str
        """
        return self._SingleReplicaBytes

    @SingleReplicaBytes.setter
    def SingleReplicaBytes(self, SingleReplicaBytes):
        self._SingleReplicaBytes = SingleReplicaBytes

    @property
    def BackupStatus(self):
        r"""备份状态
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupErrorMsg(self):
        r"""备份的错误信息
        :rtype: str
        """
        return self._BackupErrorMsg

    @BackupErrorMsg.setter
    def BackupErrorMsg(self, BackupErrorMsg):
        self._BackupErrorMsg = BackupErrorMsg

    @property
    def IsOpenCoolDown(self):
        r"""该库表是否绑定降冷策略
        :rtype: bool
        """
        return self._IsOpenCoolDown

    @IsOpenCoolDown.setter
    def IsOpenCoolDown(self, IsOpenCoolDown):
        self._IsOpenCoolDown = IsOpenCoolDown


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._TotalBytes = params.get("TotalBytes")
        self._SingleReplicaBytes = params.get("SingleReplicaBytes")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupErrorMsg = params.get("BackupErrorMsg")
        self._IsOpenCoolDown = params.get("IsOpenCoolDown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindUser(AbstractModel):
    r"""资源组绑定的用户信息，需要username和host信息进行授权

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Host: 主机信息
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
        r"""主机信息
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
        


class CancelBackupJobRequest(AbstractModel):
    r"""CancelBackupJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 需要取消的备份实例id
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""需要取消的备份实例id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelBackupJobResponse(AbstractModel):
    r"""CancelBackupJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ChargeProperties(AbstractModel):
    r"""集群计费相关信息

    """

    def __init__(self):
        r"""
        :param _ChargeType: 计费类型，“PREPAID” 预付费，“POSTPAID_BY_HOUR” 后付费
        :type ChargeType: str
        :param _RenewFlag: 是否自动续费，1表示自动续费开启
        :type RenewFlag: int
        :param _TimeSpan: 计费时间长度
        :type TimeSpan: int
        :param _TimeUnit: 计费时间单位，“m”表示月等
        :type TimeUnit: str
        """
        self._ChargeType = None
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def ChargeType(self):
        r"""计费类型，“PREPAID” 预付费，“POSTPAID_BY_HOUR” 后付费
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RenewFlag(self):
        r"""是否自动续费，1表示自动续费开启
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        r"""计费时间长度
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""计费时间单位，“m”表示月等
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCoolDownWorkingVariableConfigCorrectRequest(AbstractModel):
    r"""CheckCoolDownWorkingVariableConfigCorrect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class CheckCoolDownWorkingVariableConfigCorrectResponse(AbstractModel):
    r"""CheckCoolDownWorkingVariableConfigCorrect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ClusterConfigsHistory(AbstractModel):
    r"""集群的配置文件的修改历史

    """

    def __init__(self):
        r"""
        :param _ComputeGroupId: 计算组id
        :type ComputeGroupId: str
        :param _FileName: 配置文件名称
        :type FileName: str
        :param _NewConfValue: 修改后的配置文件内容，base64编码
        :type NewConfValue: str
        :param _OldConfValue: 修改前的配置文件内容，base64编码
        :type OldConfValue: str
        :param _Remark: 修改原因
        :type Remark: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _UserUin: 修改子账号id
        :type UserUin: str
        """
        self._ComputeGroupId = None
        self._FileName = None
        self._NewConfValue = None
        self._OldConfValue = None
        self._Remark = None
        self._ModifyTime = None
        self._UserUin = None

    @property
    def ComputeGroupId(self):
        r"""计算组id
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId

    @property
    def FileName(self):
        r"""配置文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewConfValue(self):
        r"""修改后的配置文件内容，base64编码
        :rtype: str
        """
        return self._NewConfValue

    @NewConfValue.setter
    def NewConfValue(self, NewConfValue):
        self._NewConfValue = NewConfValue

    @property
    def OldConfValue(self):
        r"""修改前的配置文件内容，base64编码
        :rtype: str
        """
        return self._OldConfValue

    @OldConfValue.setter
    def OldConfValue(self, OldConfValue):
        self._OldConfValue = OldConfValue

    @property
    def Remark(self):
        r"""修改原因
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
    def UserUin(self):
        r"""修改子账号id
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin


    def _deserialize(self, params):
        self._ComputeGroupId = params.get("ComputeGroupId")
        self._FileName = params.get("FileName")
        self._NewConfValue = params.get("NewConfValue")
        self._OldConfValue = params.get("OldConfValue")
        self._Remark = params.get("Remark")
        self._ModifyTime = params.get("ModifyTime")
        self._UserUin = params.get("UserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfigsInfoFromEMR(AbstractModel):
    r"""用于返回XML格式的配置文件和内容以及其他配置文件有关的信息

    """

    def __init__(self):
        r"""
        :param _ComputeGroupId: 计算组id
        :type ComputeGroupId: str
        :param _FileName: 配置文件名称
        :type FileName: str
        :param _FileConf: 配置文件对应的相关属性信息
        :type FileConf: str
        :param _KeyConf: 配置文件对应的其他属性信息
        :type KeyConf: str
        :param _OriParam: 配置文件的内容，base64编码
        :type OriParam: str
        :param _NeedRestart: 用于表示当前配置文件是不是有过修改后没有重启，提醒用户需要重启
        :type NeedRestart: int
        :param _FilePath: 配置文件路径
        :type FilePath: str
        :param _FileKeyValues: 配置文件kv值
注意：此字段可能返回 null，表示取不到有效值。
        :type FileKeyValues: str
        :param _FileKeyValuesNew: 配置文件kv值
        :type FileKeyValuesNew: list of ConfigKeyValue
        """
        self._ComputeGroupId = None
        self._FileName = None
        self._FileConf = None
        self._KeyConf = None
        self._OriParam = None
        self._NeedRestart = None
        self._FilePath = None
        self._FileKeyValues = None
        self._FileKeyValuesNew = None

    @property
    def ComputeGroupId(self):
        r"""计算组id
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId

    @property
    def FileName(self):
        r"""配置文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileConf(self):
        r"""配置文件对应的相关属性信息
        :rtype: str
        """
        return self._FileConf

    @FileConf.setter
    def FileConf(self, FileConf):
        self._FileConf = FileConf

    @property
    def KeyConf(self):
        r"""配置文件对应的其他属性信息
        :rtype: str
        """
        return self._KeyConf

    @KeyConf.setter
    def KeyConf(self, KeyConf):
        self._KeyConf = KeyConf

    @property
    def OriParam(self):
        r"""配置文件的内容，base64编码
        :rtype: str
        """
        return self._OriParam

    @OriParam.setter
    def OriParam(self, OriParam):
        self._OriParam = OriParam

    @property
    def NeedRestart(self):
        r"""用于表示当前配置文件是不是有过修改后没有重启，提醒用户需要重启
        :rtype: int
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def FilePath(self):
        r"""配置文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileKeyValues(self):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        r"""配置文件kv值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileKeyValues

    @FileKeyValues.setter
    def FileKeyValues(self, FileKeyValues):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        self._FileKeyValues = FileKeyValues

    @property
    def FileKeyValuesNew(self):
        r"""配置文件kv值
        :rtype: list of ConfigKeyValue
        """
        return self._FileKeyValuesNew

    @FileKeyValuesNew.setter
    def FileKeyValuesNew(self, FileKeyValuesNew):
        self._FileKeyValuesNew = FileKeyValuesNew


    def _deserialize(self, params):
        self._ComputeGroupId = params.get("ComputeGroupId")
        self._FileName = params.get("FileName")
        self._FileConf = params.get("FileConf")
        self._KeyConf = params.get("KeyConf")
        self._OriParam = params.get("OriParam")
        self._NeedRestart = params.get("NeedRestart")
        self._FilePath = params.get("FilePath")
        self._FileKeyValues = params.get("FileKeyValues")
        if params.get("FileKeyValuesNew") is not None:
            self._FileKeyValuesNew = []
            for item in params.get("FileKeyValuesNew"):
                obj = ConfigKeyValue()
                obj._deserialize(item)
                self._FileKeyValuesNew.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigKeyValue(AbstractModel):
    r"""返回配置的文件内容（key-value）

    """

    def __init__(self):
        r"""
        :param _KeyName: key
        :type KeyName: str
        :param _Value: 值
        :type Value: str
        :param _Message: 备注
        :type Message: str
        :param _Display: 1-只读，2-可修改但不可删除，3-可删除
        :type Display: int
        :param _SupportHotUpdate: 0不支持 1支持热更新
        :type SupportHotUpdate: int
        """
        self._KeyName = None
        self._Value = None
        self._Message = None
        self._Display = None
        self._SupportHotUpdate = None

    @property
    def KeyName(self):
        r"""key
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Value(self):
        r"""值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Message(self):
        r"""备注
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Display(self):
        r"""1-只读，2-可修改但不可删除，3-可删除
        :rtype: int
        """
        return self._Display

    @Display.setter
    def Display(self, Display):
        self._Display = Display

    @property
    def SupportHotUpdate(self):
        r"""0不支持 1支持热更新
        :rtype: int
        """
        return self._SupportHotUpdate

    @SupportHotUpdate.setter
    def SupportHotUpdate(self, SupportHotUpdate):
        self._SupportHotUpdate = SupportHotUpdate


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._Value = params.get("Value")
        self._Message = params.get("Message")
        self._Display = params.get("Display")
        self._SupportHotUpdate = params.get("SupportHotUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSubmitContext(AbstractModel):
    r"""配置文件修改信息

    """

    def __init__(self):
        r"""
        :param _FileName: 配置文件名称
        :type FileName: str
        :param _NewConfValue: 配置文件新内容，base64编码
        :type NewConfValue: str
        :param _OldConfValue: 配置文件旧内容，base64编码
        :type OldConfValue: str
        :param _FilePath: 文件路径
        :type FilePath: str
        """
        self._FileName = None
        self._NewConfValue = None
        self._OldConfValue = None
        self._FilePath = None

    @property
    def FileName(self):
        r"""配置文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewConfValue(self):
        r"""配置文件新内容，base64编码
        :rtype: str
        """
        return self._NewConfValue

    @NewConfValue.setter
    def NewConfValue(self, NewConfValue):
        self._NewConfValue = NewConfValue

    @property
    def OldConfValue(self):
        r"""配置文件旧内容，base64编码
        :rtype: str
        """
        return self._OldConfValue

    @OldConfValue.setter
    def OldConfValue(self, OldConfValue):
        self._OldConfValue = OldConfValue

    @property
    def FilePath(self):
        r"""文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._NewConfValue = params.get("NewConfValue")
        self._OldConfValue = params.get("OldConfValue")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownBackend(AbstractModel):
    r"""冷热分层backend节点信息

    """

    def __init__(self):
        r"""
        :param _Host: 字段：Host
        :type Host: str
        :param _DataUsedCapacity: 字段：DataUsedCapacity
        :type DataUsedCapacity: str
        :param _TotalCapacity: 字段：TotalCapacity
        :type TotalCapacity: str
        :param _RemoteUsedCapacity: 字段：RemoteUsedCapacity
        :type RemoteUsedCapacity: str
        """
        self._Host = None
        self._DataUsedCapacity = None
        self._TotalCapacity = None
        self._RemoteUsedCapacity = None

    @property
    def Host(self):
        r"""字段：Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DataUsedCapacity(self):
        r"""字段：DataUsedCapacity
        :rtype: str
        """
        return self._DataUsedCapacity

    @DataUsedCapacity.setter
    def DataUsedCapacity(self, DataUsedCapacity):
        self._DataUsedCapacity = DataUsedCapacity

    @property
    def TotalCapacity(self):
        r"""字段：TotalCapacity
        :rtype: str
        """
        return self._TotalCapacity

    @TotalCapacity.setter
    def TotalCapacity(self, TotalCapacity):
        self._TotalCapacity = TotalCapacity

    @property
    def RemoteUsedCapacity(self):
        r"""字段：RemoteUsedCapacity
        :rtype: str
        """
        return self._RemoteUsedCapacity

    @RemoteUsedCapacity.setter
    def RemoteUsedCapacity(self, RemoteUsedCapacity):
        self._RemoteUsedCapacity = RemoteUsedCapacity


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._DataUsedCapacity = params.get("DataUsedCapacity")
        self._TotalCapacity = params.get("TotalCapacity")
        self._RemoteUsedCapacity = params.get("RemoteUsedCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownPolicyInfo(AbstractModel):
    r"""冷热分层策略

    """

    def __init__(self):
        r"""
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _CooldownDatetime: cooldown_ttl
        :type CooldownDatetime: str
        :param _CooldownTtl: cooldown_datetime
        :type CooldownTtl: str
        """
        self._PolicyName = None
        self._CooldownDatetime = None
        self._CooldownTtl = None

    @property
    def PolicyName(self):
        r"""策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CooldownDatetime(self):
        r"""cooldown_ttl
        :rtype: str
        """
        return self._CooldownDatetime

    @CooldownDatetime.setter
    def CooldownDatetime(self, CooldownDatetime):
        self._CooldownDatetime = CooldownDatetime

    @property
    def CooldownTtl(self):
        r"""cooldown_datetime
        :rtype: str
        """
        return self._CooldownTtl

    @CooldownTtl.setter
    def CooldownTtl(self, CooldownTtl):
        self._CooldownTtl = CooldownTtl


    def _deserialize(self, params):
        self._PolicyName = params.get("PolicyName")
        self._CooldownDatetime = params.get("CooldownDatetime")
        self._CooldownTtl = params.get("CooldownTtl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownTableDataInfo(AbstractModel):
    r"""冷热分层Table数据信息

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 列：DatabaseName
        :type DatabaseName: str
        :param _TableName: 列：TableName
        :type TableName: str
        :param _Size: 列：Size
        :type Size: str
        :param _RemoteSize: 列：RemoteSize
        :type RemoteSize: str
        """
        self._DatabaseName = None
        self._TableName = None
        self._Size = None
        self._RemoteSize = None

    @property
    def DatabaseName(self):
        r"""列：DatabaseName
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""列：TableName
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Size(self):
        r"""列：Size
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def RemoteSize(self):
        r"""列：RemoteSize
        :rtype: str
        """
        return self._RemoteSize

    @RemoteSize.setter
    def RemoteSize(self, RemoteSize):
        self._RemoteSize = RemoteSize


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._Size = params.get("Size")
        self._RemoteSize = params.get("RemoteSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosSourceInfo(AbstractModel):
    r"""客户提供cos认证信息。

    """

    def __init__(self):
        r"""
        :param _SecretId: cos认证中的Id
        :type SecretId: str
        :param _SecretKey: cos认证中的key
        :type SecretKey: str
        :param _CosPath: cos认证中的路径
        :type CosPath: str
        """
        self._SecretId = None
        self._SecretKey = None
        self._CosPath = None

    @property
    def SecretId(self):
        r"""cos认证中的Id
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        r"""cos认证中的key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def CosPath(self):
        r"""cos认证中的路径
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._CosPath = params.get("CosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleRequest(AbstractModel):
    r"""CreateBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _OperationType: 操作类型 create(创建) update(编辑修改)
        :type OperationType: str
        :param _ScheduleId: 编辑时需要传
        :type ScheduleId: int
        :param _WeekDays: 选择的星期 逗号分隔
废弃：使用ScheduleInfo
        :type WeekDays: str
        :param _ExecuteHour: 执行小时
废弃：使用ScheduleInfo
        :type ExecuteHour: int
        :param _BackUpTables: 备份表列表
        :type BackUpTables: list of BackupTableContent
        :param _BackupType: 0为默认。1时是对远端的doris进行备份，不周期，一次性
        :type BackupType: int
        :param _DorisSourceInfo: 远端doris集群的连接信息
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _BackupTimeType: 0为周期备份。1时是立即备份。3时是定时备份。
        :type BackupTimeType: int
        :param _RestoreType: 0为默认。1时是备份完成后立即恢复
        :type RestoreType: int
        :param _AuthType: 0为默认。1时是提供自定义的secret连接cos
        :type AuthType: int
        :param _CosSourceInfo: cos认证的信息
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        :param _ScheduleName: 调度任务名
        :type ScheduleName: str
        :param _ScheduleInfo: 调度信息
        :type ScheduleInfo: :class:`tencentcloud.cdwdoris.v20211228.models.ScheduleInfo`
        :param _UpdateStatus: 更新任务状态：
3-暂停,
2-删除,
1-启动
        :type UpdateStatus: int
        :param _CosBucket: 当前任务的cos桶信息
        :type CosBucket: str
        :param _SnapshotRemainPolicy: 快照保留策略
        :type SnapshotRemainPolicy: :class:`tencentcloud.cdwdoris.v20211228.models.SnapshotRemainPolicy`
        :param _DataRemoteRegion: 备份数据所在地域，当前地域应该为空
        :type DataRemoteRegion: str
        """
        self._InstanceId = None
        self._OperationType = None
        self._ScheduleId = None
        self._WeekDays = None
        self._ExecuteHour = None
        self._BackUpTables = None
        self._BackupType = None
        self._DorisSourceInfo = None
        self._BackupTimeType = None
        self._RestoreType = None
        self._AuthType = None
        self._CosSourceInfo = None
        self._ScheduleName = None
        self._ScheduleInfo = None
        self._UpdateStatus = None
        self._CosBucket = None
        self._SnapshotRemainPolicy = None
        self._DataRemoteRegion = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OperationType(self):
        r"""操作类型 create(创建) update(编辑修改)
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def ScheduleId(self):
        r"""编辑时需要传
        :rtype: int
        """
        return self._ScheduleId

    @ScheduleId.setter
    def ScheduleId(self, ScheduleId):
        self._ScheduleId = ScheduleId

    @property
    def WeekDays(self):
        warnings.warn("parameter `WeekDays` is deprecated", DeprecationWarning) 

        r"""选择的星期 逗号分隔
废弃：使用ScheduleInfo
        :rtype: str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        warnings.warn("parameter `WeekDays` is deprecated", DeprecationWarning) 

        self._WeekDays = WeekDays

    @property
    def ExecuteHour(self):
        warnings.warn("parameter `ExecuteHour` is deprecated", DeprecationWarning) 

        r"""执行小时
废弃：使用ScheduleInfo
        :rtype: int
        """
        return self._ExecuteHour

    @ExecuteHour.setter
    def ExecuteHour(self, ExecuteHour):
        warnings.warn("parameter `ExecuteHour` is deprecated", DeprecationWarning) 

        self._ExecuteHour = ExecuteHour

    @property
    def BackUpTables(self):
        r"""备份表列表
        :rtype: list of BackupTableContent
        """
        return self._BackUpTables

    @BackUpTables.setter
    def BackUpTables(self, BackUpTables):
        self._BackUpTables = BackUpTables

    @property
    def BackupType(self):
        warnings.warn("parameter `BackupType` is deprecated", DeprecationWarning) 

        r"""0为默认。1时是对远端的doris进行备份，不周期，一次性
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        warnings.warn("parameter `BackupType` is deprecated", DeprecationWarning) 

        self._BackupType = BackupType

    @property
    def DorisSourceInfo(self):
        warnings.warn("parameter `DorisSourceInfo` is deprecated", DeprecationWarning) 

        r"""远端doris集群的连接信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        warnings.warn("parameter `DorisSourceInfo` is deprecated", DeprecationWarning) 

        self._DorisSourceInfo = DorisSourceInfo

    @property
    def BackupTimeType(self):
        r"""0为周期备份。1时是立即备份。3时是定时备份。
        :rtype: int
        """
        return self._BackupTimeType

    @BackupTimeType.setter
    def BackupTimeType(self, BackupTimeType):
        self._BackupTimeType = BackupTimeType

    @property
    def RestoreType(self):
        warnings.warn("parameter `RestoreType` is deprecated", DeprecationWarning) 

        r"""0为默认。1时是备份完成后立即恢复
        :rtype: int
        """
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        warnings.warn("parameter `RestoreType` is deprecated", DeprecationWarning) 

        self._RestoreType = RestoreType

    @property
    def AuthType(self):
        warnings.warn("parameter `AuthType` is deprecated", DeprecationWarning) 

        r"""0为默认。1时是提供自定义的secret连接cos
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        warnings.warn("parameter `AuthType` is deprecated", DeprecationWarning) 

        self._AuthType = AuthType

    @property
    def CosSourceInfo(self):
        warnings.warn("parameter `CosSourceInfo` is deprecated", DeprecationWarning) 

        r"""cos认证的信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        warnings.warn("parameter `CosSourceInfo` is deprecated", DeprecationWarning) 

        self._CosSourceInfo = CosSourceInfo

    @property
    def ScheduleName(self):
        r"""调度任务名
        :rtype: str
        """
        return self._ScheduleName

    @ScheduleName.setter
    def ScheduleName(self, ScheduleName):
        self._ScheduleName = ScheduleName

    @property
    def ScheduleInfo(self):
        r"""调度信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScheduleInfo`
        """
        return self._ScheduleInfo

    @ScheduleInfo.setter
    def ScheduleInfo(self, ScheduleInfo):
        self._ScheduleInfo = ScheduleInfo

    @property
    def UpdateStatus(self):
        r"""更新任务状态：
3-暂停,
2-删除,
1-启动
        :rtype: int
        """
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def CosBucket(self):
        r"""当前任务的cos桶信息
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def SnapshotRemainPolicy(self):
        r"""快照保留策略
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.SnapshotRemainPolicy`
        """
        return self._SnapshotRemainPolicy

    @SnapshotRemainPolicy.setter
    def SnapshotRemainPolicy(self, SnapshotRemainPolicy):
        self._SnapshotRemainPolicy = SnapshotRemainPolicy

    @property
    def DataRemoteRegion(self):
        r"""备份数据所在地域，当前地域应该为空
        :rtype: str
        """
        return self._DataRemoteRegion

    @DataRemoteRegion.setter
    def DataRemoteRegion(self, DataRemoteRegion):
        self._DataRemoteRegion = DataRemoteRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OperationType = params.get("OperationType")
        self._ScheduleId = params.get("ScheduleId")
        self._WeekDays = params.get("WeekDays")
        self._ExecuteHour = params.get("ExecuteHour")
        if params.get("BackUpTables") is not None:
            self._BackUpTables = []
            for item in params.get("BackUpTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._BackUpTables.append(obj)
        self._BackupType = params.get("BackupType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        self._BackupTimeType = params.get("BackupTimeType")
        self._RestoreType = params.get("RestoreType")
        self._AuthType = params.get("AuthType")
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        self._ScheduleName = params.get("ScheduleName")
        if params.get("ScheduleInfo") is not None:
            self._ScheduleInfo = ScheduleInfo()
            self._ScheduleInfo._deserialize(params.get("ScheduleInfo"))
        self._UpdateStatus = params.get("UpdateStatus")
        self._CosBucket = params.get("CosBucket")
        if params.get("SnapshotRemainPolicy") is not None:
            self._SnapshotRemainPolicy = SnapshotRemainPolicy()
            self._SnapshotRemainPolicy._deserialize(params.get("SnapshotRemainPolicy"))
        self._DataRemoteRegion = params.get("DataRemoteRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleResponse(AbstractModel):
    r"""CreateBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateCoolDownPolicyRequest(AbstractModel):
    r"""CreateCoolDownPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _CoolDownTtl: cooldown_ttl
        :type CoolDownTtl: str
        :param _CoolDownDatetime: cooldown_datetime
        :type CoolDownDatetime: str
        """
        self._InstanceId = None
        self._PolicyName = None
        self._CoolDownTtl = None
        self._CoolDownDatetime = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        r"""策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CoolDownTtl(self):
        r"""cooldown_ttl
        :rtype: str
        """
        return self._CoolDownTtl

    @CoolDownTtl.setter
    def CoolDownTtl(self, CoolDownTtl):
        self._CoolDownTtl = CoolDownTtl

    @property
    def CoolDownDatetime(self):
        r"""cooldown_datetime
        :rtype: str
        """
        return self._CoolDownDatetime

    @CoolDownDatetime.setter
    def CoolDownDatetime(self, CoolDownDatetime):
        self._CoolDownDatetime = CoolDownDatetime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._CoolDownTtl = params.get("CoolDownTtl")
        self._CoolDownDatetime = params.get("CoolDownDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCoolDownPolicyResponse(AbstractModel):
    r"""CreateCoolDownPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateInstanceNewRequest(AbstractModel):
    r"""CreateInstanceNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _FeSpec: FE规格
        :type FeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _BeSpec: BE规格
        :type BeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _HaFlag: 是否高可用
        :type HaFlag: bool
        :param _UserVPCId: 用户VPCID
        :type UserVPCId: str
        :param _UserSubnetId: 用户子网ID
        :type UserSubnetId: str
        :param _ProductVersion: 产品版本号
        :type ProductVersion: str
        :param _ChargeProperties: 付费类型
        :type ChargeProperties: :class:`tencentcloud.cdwdoris.v20211228.models.ChargeProperties`
        :param _InstanceName: 实例名字
        :type InstanceName: str
        :param _DorisUserPwd: 数据库密码
        :type DorisUserPwd: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _HaType: 高可用类型：
0：非高可用（只有1个FE，FeSpec.CreateInstanceSpec.Count=1），
1：读高可用（至少需部署3个FE，FeSpec.CreateInstanceSpec.Count>=3，且为奇数），
2：读写高可用（至少需部署5个FE，FeSpec.CreateInstanceSpec.Count>=5，且为奇数）。
        :type HaType: int
        :param _CaseSensitive: 表名大小写是否敏感，0：敏感；1：不敏感，以小写进行比较；2：不敏感，表名改为以小写存储
        :type CaseSensitive: int
        :param _EnableMultiZones: 是否开启多可用区
        :type EnableMultiZones: bool
        :param _UserMultiZoneInfos: 开启多可用区后，用户的所有可用区和子网信息
        :type UserMultiZoneInfos: :class:`tencentcloud.cdwdoris.v20211228.models.NetworkInfo`
        :param _UserMultiZoneInfoArr: 开启多可用区后，用户的所有可用区和子网信息
        :type UserMultiZoneInfoArr: list of NetworkInfo
        :param _IsSSC: 是否存算分离
        :type IsSSC: bool
        :param _SSCCU: CU数
        :type SSCCU: int
        :param _CacheDiskSize: 缓存盘大小
        :type CacheDiskSize: str
        :param _CacheDataDiskSize: 缓存盘大小
        :type CacheDataDiskSize: int
        """
        self._Zone = None
        self._FeSpec = None
        self._BeSpec = None
        self._HaFlag = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ProductVersion = None
        self._ChargeProperties = None
        self._InstanceName = None
        self._DorisUserPwd = None
        self._Tags = None
        self._HaType = None
        self._CaseSensitive = None
        self._EnableMultiZones = None
        self._UserMultiZoneInfos = None
        self._UserMultiZoneInfoArr = None
        self._IsSSC = None
        self._SSCCU = None
        self._CacheDiskSize = None
        self._CacheDataDiskSize = None

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FeSpec(self):
        r"""FE规格
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        """
        return self._FeSpec

    @FeSpec.setter
    def FeSpec(self, FeSpec):
        self._FeSpec = FeSpec

    @property
    def BeSpec(self):
        r"""BE规格
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        """
        return self._BeSpec

    @BeSpec.setter
    def BeSpec(self, BeSpec):
        self._BeSpec = BeSpec

    @property
    def HaFlag(self):
        r"""是否高可用
        :rtype: bool
        """
        return self._HaFlag

    @HaFlag.setter
    def HaFlag(self, HaFlag):
        self._HaFlag = HaFlag

    @property
    def UserVPCId(self):
        r"""用户VPCID
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        r"""用户子网ID
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ProductVersion(self):
        r"""产品版本号
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def ChargeProperties(self):
        r"""付费类型
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def InstanceName(self):
        r"""实例名字
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DorisUserPwd(self):
        r"""数据库密码
        :rtype: str
        """
        return self._DorisUserPwd

    @DorisUserPwd.setter
    def DorisUserPwd(self, DorisUserPwd):
        self._DorisUserPwd = DorisUserPwd

    @property
    def Tags(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HaType(self):
        r"""高可用类型：
0：非高可用（只有1个FE，FeSpec.CreateInstanceSpec.Count=1），
1：读高可用（至少需部署3个FE，FeSpec.CreateInstanceSpec.Count>=3，且为奇数），
2：读写高可用（至少需部署5个FE，FeSpec.CreateInstanceSpec.Count>=5，且为奇数）。
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def CaseSensitive(self):
        r"""表名大小写是否敏感，0：敏感；1：不敏感，以小写进行比较；2：不敏感，表名改为以小写存储
        :rtype: int
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def EnableMultiZones(self):
        r"""是否开启多可用区
        :rtype: bool
        """
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserMultiZoneInfos(self):
        warnings.warn("parameter `UserMultiZoneInfos` is deprecated", DeprecationWarning) 

        r"""开启多可用区后，用户的所有可用区和子网信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NetworkInfo`
        """
        return self._UserMultiZoneInfos

    @UserMultiZoneInfos.setter
    def UserMultiZoneInfos(self, UserMultiZoneInfos):
        warnings.warn("parameter `UserMultiZoneInfos` is deprecated", DeprecationWarning) 

        self._UserMultiZoneInfos = UserMultiZoneInfos

    @property
    def UserMultiZoneInfoArr(self):
        r"""开启多可用区后，用户的所有可用区和子网信息
        :rtype: list of NetworkInfo
        """
        return self._UserMultiZoneInfoArr

    @UserMultiZoneInfoArr.setter
    def UserMultiZoneInfoArr(self, UserMultiZoneInfoArr):
        self._UserMultiZoneInfoArr = UserMultiZoneInfoArr

    @property
    def IsSSC(self):
        r"""是否存算分离
        :rtype: bool
        """
        return self._IsSSC

    @IsSSC.setter
    def IsSSC(self, IsSSC):
        self._IsSSC = IsSSC

    @property
    def SSCCU(self):
        r"""CU数
        :rtype: int
        """
        return self._SSCCU

    @SSCCU.setter
    def SSCCU(self, SSCCU):
        self._SSCCU = SSCCU

    @property
    def CacheDiskSize(self):
        warnings.warn("parameter `CacheDiskSize` is deprecated", DeprecationWarning) 

        r"""缓存盘大小
        :rtype: str
        """
        return self._CacheDiskSize

    @CacheDiskSize.setter
    def CacheDiskSize(self, CacheDiskSize):
        warnings.warn("parameter `CacheDiskSize` is deprecated", DeprecationWarning) 

        self._CacheDiskSize = CacheDiskSize

    @property
    def CacheDataDiskSize(self):
        r"""缓存盘大小
        :rtype: int
        """
        return self._CacheDataDiskSize

    @CacheDataDiskSize.setter
    def CacheDataDiskSize(self, CacheDataDiskSize):
        self._CacheDataDiskSize = CacheDataDiskSize


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        if params.get("FeSpec") is not None:
            self._FeSpec = CreateInstanceSpec()
            self._FeSpec._deserialize(params.get("FeSpec"))
        if params.get("BeSpec") is not None:
            self._BeSpec = CreateInstanceSpec()
            self._BeSpec._deserialize(params.get("BeSpec"))
        self._HaFlag = params.get("HaFlag")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._ProductVersion = params.get("ProductVersion")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._InstanceName = params.get("InstanceName")
        self._DorisUserPwd = params.get("DorisUserPwd")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HaType = params.get("HaType")
        self._CaseSensitive = params.get("CaseSensitive")
        self._EnableMultiZones = params.get("EnableMultiZones")
        if params.get("UserMultiZoneInfos") is not None:
            self._UserMultiZoneInfos = NetworkInfo()
            self._UserMultiZoneInfos._deserialize(params.get("UserMultiZoneInfos"))
        if params.get("UserMultiZoneInfoArr") is not None:
            self._UserMultiZoneInfoArr = []
            for item in params.get("UserMultiZoneInfoArr"):
                obj = NetworkInfo()
                obj._deserialize(item)
                self._UserMultiZoneInfoArr.append(obj)
        self._IsSSC = params.get("IsSSC")
        self._SSCCU = params.get("SSCCU")
        self._CacheDiskSize = params.get("CacheDiskSize")
        self._CacheDataDiskSize = params.get("CacheDataDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewResponse(AbstractModel):
    r"""CreateInstanceNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateInstanceSpec(AbstractModel):
    r"""集群规格

    """

    def __init__(self):
        r"""
        :param _SpecName: 规格名字
        :type SpecName: str
        :param _Count: 数量
        :type Count: int
        :param _DiskSize: 云盘大小
        :type DiskSize: int
        """
        self._SpecName = None
        self._Count = None
        self._DiskSize = None

    @property
    def SpecName(self):
        r"""规格名字
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        r"""数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSize(self):
        r"""云盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkloadGroupRequest(AbstractModel):
    r"""CreateWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id	
        :type InstanceId: str
        :param _WorkloadGroup: 资源组配置
        :type WorkloadGroup: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        self._InstanceId = None
        self._WorkloadGroup = None

    @property
    def InstanceId(self):
        r"""集群id	
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroup(self):
        r"""资源组配置
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        return self._WorkloadGroup

    @WorkloadGroup.setter
    def WorkloadGroup(self, WorkloadGroup):
        self._WorkloadGroup = WorkloadGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WorkloadGroup") is not None:
            self._WorkloadGroup = WorkloadGroupConfig()
            self._WorkloadGroup._deserialize(params.get("WorkloadGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkloadGroupResponse(AbstractModel):
    r"""CreateWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DataBaseAuditRecord(AbstractModel):
    r"""数据库审计

    """

    def __init__(self):
        r"""
        :param _OsUser: 查询用户
        :type OsUser: str
        :param _InitialQueryId: 查询ID
        :type InitialQueryId: str
        :param _Sql: SQL语句
        :type Sql: str
        :param _QueryStartTime: 开始时间
        :type QueryStartTime: str
        :param _DurationMs: 执行耗时
        :type DurationMs: int
        :param _ReadRows: 读取行数
        :type ReadRows: int
        :param _ResultRows: 读取字节数
        :type ResultRows: int
        :param _ResultBytes: 结果字节数
        :type ResultBytes: int
        :param _MemoryUsage: 内存
        :type MemoryUsage: int
        :param _InitialAddress: 初始查询IP
        :type InitialAddress: str
        :param _DbName: 数据库
        :type DbName: str
        :param _SqlType: sql类型
        :type SqlType: str
        :param _Catalog: catalog名称
        :type Catalog: str
        :param _State: 状态
        :type State: str
        :param _IsQuery: 是否是查询
        :type IsQuery: bool
        :param _ComputeGroup: 计算组
        :type ComputeGroup: str
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._SqlType = None
        self._Catalog = None
        self._State = None
        self._IsQuery = None
        self._ComputeGroup = None

    @property
    def OsUser(self):
        r"""查询用户
        :rtype: str
        """
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        r"""查询ID
        :rtype: str
        """
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        r"""SQL语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        r"""执行耗时
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        r"""读取行数
        :rtype: int
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        r"""读取字节数
        :rtype: int
        """
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        r"""结果字节数
        :rtype: int
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        r"""内存
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        r"""初始查询IP
        :rtype: str
        """
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        r"""数据库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        r"""sql类型
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Catalog(self):
        r"""catalog名称
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def State(self):
        r"""状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def IsQuery(self):
        r"""是否是查询
        :rtype: bool
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ComputeGroup(self):
        r"""计算组
        :rtype: str
        """
        return self._ComputeGroup

    @ComputeGroup.setter
    def ComputeGroup(self, ComputeGroup):
        self._ComputeGroup = ComputeGroup


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Catalog = params.get("Catalog")
        self._State = params.get("State")
        self._IsQuery = params.get("IsQuery")
        self._ComputeGroup = params.get("ComputeGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataRequest(AbstractModel):
    r"""DeleteBackUpData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        :param _IsDeleteAll: 是否删除所有实例
        :type IsDeleteAll: bool
        :param _IsRecover: true代表恢复删除隔离中的job 默认false就是删除
        :type IsRecover: bool
        """
        self._InstanceId = None
        self._BackUpJobId = None
        self._IsDeleteAll = None
        self._IsRecover = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId

    @property
    def IsDeleteAll(self):
        r"""是否删除所有实例
        :rtype: bool
        """
        return self._IsDeleteAll

    @IsDeleteAll.setter
    def IsDeleteAll(self, IsDeleteAll):
        self._IsDeleteAll = IsDeleteAll

    @property
    def IsRecover(self):
        r"""true代表恢复删除隔离中的job 默认false就是删除
        :rtype: bool
        """
        return self._IsRecover

    @IsRecover.setter
    def IsRecover(self, IsRecover):
        self._IsRecover = IsRecover


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        self._IsDeleteAll = params.get("IsDeleteAll")
        self._IsRecover = params.get("IsRecover")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataResponse(AbstractModel):
    r"""DeleteBackUpData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DeleteWorkloadGroupRequest(AbstractModel):
    r"""DeleteWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _WorkloadGroupName: 需要删除的资源组名称
        :type WorkloadGroupName: str
        """
        self._InstanceId = None
        self._WorkloadGroupName = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroupName(self):
        r"""需要删除的资源组名称
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkloadGroupResponse(AbstractModel):
    r"""DeleteWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeAreaRegionRequest(AbstractModel):
    r"""DescribeAreaRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsInternationalSite: 是否是国际站
        :type IsInternationalSite: bool
        """
        self._IsInternationalSite = None

    @property
    def IsInternationalSite(self):
        r"""是否是国际站
        :rtype: bool
        """
        return self._IsInternationalSite

    @IsInternationalSite.setter
    def IsInternationalSite(self, IsInternationalSite):
        self._IsInternationalSite = IsInternationalSite


    def _deserialize(self, params):
        self._IsInternationalSite = params.get("IsInternationalSite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAreaRegionResponse(AbstractModel):
    r"""DescribeAreaRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 地域列表
        :type Items: list of RegionAreaInfo
        :param _FrontEndRules: 前端规则描述
        :type FrontEndRules: list of FrontEndRule
        :param _AvailableWhiteListNames: 返回可用的白名单名称
        :type AvailableWhiteListNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._FrontEndRules = None
        self._AvailableWhiteListNames = None
        self._RequestId = None

    @property
    def Items(self):
        r"""地域列表
        :rtype: list of RegionAreaInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def FrontEndRules(self):
        r"""前端规则描述
        :rtype: list of FrontEndRule
        """
        return self._FrontEndRules

    @FrontEndRules.setter
    def FrontEndRules(self, FrontEndRules):
        self._FrontEndRules = FrontEndRules

    @property
    def AvailableWhiteListNames(self):
        r"""返回可用的白名单名称
        :rtype: list of str
        """
        return self._AvailableWhiteListNames

    @AvailableWhiteListNames.setter
    def AvailableWhiteListNames(self, AvailableWhiteListNames):
        self._AvailableWhiteListNames = AvailableWhiteListNames

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
                obj = RegionAreaInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("FrontEndRules") is not None:
            self._FrontEndRules = []
            for item in params.get("FrontEndRules"):
                obj = FrontEndRule()
                obj._deserialize(item)
                self._FrontEndRules.append(obj)
        self._AvailableWhiteListNames = params.get("AvailableWhiteListNames")
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobDetailRequest(AbstractModel):
    r"""DescribeBackUpJobDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpJobDetailResponse(AbstractModel):
    r"""DescribeBackUpJobDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableContents: 备份表详情
        :type TableContents: list of BackupTableContent
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _IsUnknownVersion: 是否是未知版本
        :type IsUnknownVersion: bool
        :param _Msg: 返回对象用字符串表示
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableContents = None
        self._ErrorMsg = None
        self._IsUnknownVersion = None
        self._Msg = None
        self._RequestId = None

    @property
    def TableContents(self):
        r"""备份表详情
        :rtype: list of BackupTableContent
        """
        return self._TableContents

    @TableContents.setter
    def TableContents(self, TableContents):
        self._TableContents = TableContents

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def IsUnknownVersion(self):
        r"""是否是未知版本
        :rtype: bool
        """
        return self._IsUnknownVersion

    @IsUnknownVersion.setter
    def IsUnknownVersion(self, IsUnknownVersion):
        self._IsUnknownVersion = IsUnknownVersion

    @property
    def Msg(self):
        r"""返回对象用字符串表示
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
        if params.get("TableContents") is not None:
            self._TableContents = []
            for item in params.get("TableContents"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._TableContents.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._IsUnknownVersion = params.get("IsUnknownVersion")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobRequest(AbstractModel):
    r"""DescribeBackUpJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _ApplicationType: 任务类型：
0-不限制，或使用TypeFilters过滤；
1-备份恢复（包括周期备份和一次性备份）；
2-数据迁移（包括跨集群迁移和cos迁移）	
        :type ApplicationType: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _PageNum: 页号
        :type PageNum: int
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _JobIdFiltersStr: jobid的string类型
        :type JobIdFiltersStr: str
        """
        self._InstanceId = None
        self._ApplicationType = None
        self._PageSize = None
        self._PageNum = None
        self._BeginTime = None
        self._EndTime = None
        self._JobIdFiltersStr = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationType(self):
        r"""任务类型：
0-不限制，或使用TypeFilters过滤；
1-备份恢复（包括周期备份和一次性备份）；
2-数据迁移（包括跨集群迁移和cos迁移）	
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""页号
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def BeginTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

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
    def JobIdFiltersStr(self):
        r"""jobid的string类型
        :rtype: str
        """
        return self._JobIdFiltersStr

    @JobIdFiltersStr.setter
    def JobIdFiltersStr(self, JobIdFiltersStr):
        self._JobIdFiltersStr = JobIdFiltersStr


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ApplicationType = params.get("ApplicationType")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._JobIdFiltersStr = params.get("JobIdFiltersStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpJobResponse(AbstractModel):
    r"""DescribeBackUpJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackUpJobs: 任务列表
        :type BackUpJobs: list of BackUpJobDisplay
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackUpJobs = None
        self._ErrorMsg = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackUpJobs(self):
        r"""任务列表
        :rtype: list of BackUpJobDisplay
        """
        return self._BackUpJobs

    @BackUpJobs.setter
    def BackUpJobs(self, BackUpJobs):
        self._BackUpJobs = BackUpJobs

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def TotalCount(self):
        r"""总数
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
        if params.get("BackUpJobs") is not None:
            self._BackUpJobs = []
            for item in params.get("BackUpJobs"):
                obj = BackUpJobDisplay()
                obj._deserialize(item)
                self._BackUpJobs.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackUpSchedulesRequest(AbstractModel):
    r"""DescribeBackUpSchedules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationType: 任务类型
0-不限制，或使用TypeFilters过滤；
1-备份恢复（包括周期备份和一次性备份）；
2-数据迁移（包括跨集群迁移和cos迁移）
        :type ApplicationType: int
        """
        self._ApplicationType = None

    @property
    def ApplicationType(self):
        r"""任务类型
0-不限制，或使用TypeFilters过滤；
1-备份恢复（包括周期备份和一次性备份）；
2-数据迁移（包括跨集群迁移和cos迁移）
        :rtype: int
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType


    def _deserialize(self, params):
        self._ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpSchedulesResponse(AbstractModel):
    r"""DescribeBackUpSchedules返回参数结构体

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


class DescribeBackUpTablesRequest(AbstractModel):
    r"""DescribeBackUpTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackupType: 0为默认。1时是对远端的doris进行备份，不周期，一次性。2时为cos恢复，一次性
        :type BackupType: int
        :param _DorisSourceInfo: 远端doris集群的连接信息
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _CosSourceInfo: cos信息
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        self._InstanceId = None
        self._BackupType = None
        self._DorisSourceInfo = None
        self._CosSourceInfo = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        r"""0为默认。1时是对远端的doris进行备份，不周期，一次性。2时为cos恢复，一次性
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def DorisSourceInfo(self):
        r"""远端doris集群的连接信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        self._DorisSourceInfo = DorisSourceInfo

    @property
    def CosSourceInfo(self):
        r"""cos信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        self._CosSourceInfo = CosSourceInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpTablesResponse(AbstractModel):
    r"""DescribeBackUpTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableTables: 可备份表列表
        :type AvailableTables: list of BackupTableContent
        :param _Msg: msg
        :type Msg: str
        :param _IsUnknownVersion: 未知version
        :type IsUnknownVersion: bool
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableTables = None
        self._Msg = None
        self._IsUnknownVersion = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def AvailableTables(self):
        r"""可备份表列表
        :rtype: list of BackupTableContent
        """
        return self._AvailableTables

    @AvailableTables.setter
    def AvailableTables(self, AvailableTables):
        self._AvailableTables = AvailableTables

    @property
    def Msg(self):
        r"""msg
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def IsUnknownVersion(self):
        r"""未知version
        :rtype: bool
        """
        return self._IsUnknownVersion

    @IsUnknownVersion.setter
    def IsUnknownVersion(self, IsUnknownVersion):
        self._IsUnknownVersion = IsUnknownVersion

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("AvailableTables") is not None:
            self._AvailableTables = []
            for item in params.get("AvailableTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._AvailableTables.append(obj)
        self._Msg = params.get("Msg")
        self._IsUnknownVersion = params.get("IsUnknownVersion")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeBackUpTaskDetailRequest(AbstractModel):
    r"""DescribeBackUpTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpTaskDetailResponse(AbstractModel):
    r"""DescribeBackUpTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupStatus: 备份任务进度详情
        :type BackupStatus: list of BackupStatus
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupStatus = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def BackupStatus(self):
        r"""备份任务进度详情
        :rtype: list of BackupStatus
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("BackupStatus") is not None:
            self._BackupStatus = []
            for item in params.get("BackupStatus"):
                obj = BackupStatus()
                obj._deserialize(item)
                self._BackupStatus.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeClusterConfigsHistoryRequest(AbstractModel):
    r"""DescribeClusterConfigsHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id名称
        :type InstanceId: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _StartTime: 配置修改历史的时间范围开始
        :type StartTime: str
        :param _EndTime: 配置修改历史的时间范围结束
        :type EndTime: str
        :param _ConfigFileNames: 需要查询的配置文件名称数组，如果为空则查询全部历史记录。目前支持的配置文件名称有：
apache_hdfs_broker.conf、be.conf、fe.conf、core-site.xml、hdfs-site.xml、odbcinst.ini
        :type ConfigFileNames: list of str
        :param _ComputeGroupIds: 需要查询的计算组列表
        :type ComputeGroupIds: list of str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._ConfigFileNames = None
        self._ComputeGroupIds = None

    @property
    def InstanceId(self):
        r"""集群id名称
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        r"""配置修改历史的时间范围开始
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""配置修改历史的时间范围结束
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ConfigFileNames(self):
        r"""需要查询的配置文件名称数组，如果为空则查询全部历史记录。目前支持的配置文件名称有：
apache_hdfs_broker.conf、be.conf、fe.conf、core-site.xml、hdfs-site.xml、odbcinst.ini
        :rtype: list of str
        """
        return self._ConfigFileNames

    @ConfigFileNames.setter
    def ConfigFileNames(self, ConfigFileNames):
        self._ConfigFileNames = ConfigFileNames

    @property
    def ComputeGroupIds(self):
        r"""需要查询的计算组列表
        :rtype: list of str
        """
        return self._ComputeGroupIds

    @ComputeGroupIds.setter
    def ComputeGroupIds(self, ComputeGroupIds):
        self._ComputeGroupIds = ComputeGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ConfigFileNames = params.get("ConfigFileNames")
        self._ComputeGroupIds = params.get("ComputeGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsHistoryResponse(AbstractModel):
    r"""DescribeClusterConfigsHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数
        :type TotalCount: int
        :param _ClusterConfHistory: 配置文件修改历史
        :type ClusterConfHistory: list of ClusterConfigsHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterConfHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterConfHistory(self):
        r"""配置文件修改历史
        :rtype: list of ClusterConfigsHistory
        """
        return self._ClusterConfHistory

    @ClusterConfHistory.setter
    def ClusterConfHistory(self, ClusterConfHistory):
        self._ClusterConfHistory = ClusterConfHistory

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
        if params.get("ClusterConfHistory") is not None:
            self._ClusterConfHistory = []
            for item in params.get("ClusterConfHistory"):
                obj = ClusterConfigsHistory()
                obj._deserialize(item)
                self._ClusterConfHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterConfigsRequest(AbstractModel):
    r"""DescribeClusterConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _ConfigType:  0 公有云查询；1青鹅查询，青鹅查询显示所有需要展示的
        :type ConfigType: int
        :param _FileName: 模糊搜索关键字文件
        :type FileName: str
        :param _ClusterConfigType: 0集群维度 1节点维度 2启动脚本 3计算组维度
        :type ClusterConfigType: int
        :param _IPAddress: eth0的ip地址
        :type IPAddress: str
        :param _ComputeGroupId: 计算组id
        :type ComputeGroupId: str
        """
        self._InstanceId = None
        self._ConfigType = None
        self._FileName = None
        self._ClusterConfigType = None
        self._IPAddress = None
        self._ComputeGroupId = None

    @property
    def InstanceId(self):
        r"""集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigType(self):
        r""" 0 公有云查询；1青鹅查询，青鹅查询显示所有需要展示的
        :rtype: int
        """
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def FileName(self):
        r"""模糊搜索关键字文件
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ClusterConfigType(self):
        r"""0集群维度 1节点维度 2启动脚本 3计算组维度
        :rtype: int
        """
        return self._ClusterConfigType

    @ClusterConfigType.setter
    def ClusterConfigType(self, ClusterConfigType):
        self._ClusterConfigType = ClusterConfigType

    @property
    def IPAddress(self):
        r"""eth0的ip地址
        :rtype: str
        """
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress

    @property
    def ComputeGroupId(self):
        r"""计算组id
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigType = params.get("ConfigType")
        self._FileName = params.get("FileName")
        self._ClusterConfigType = params.get("ClusterConfigType")
        self._IPAddress = params.get("IPAddress")
        self._ComputeGroupId = params.get("ComputeGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsResponse(AbstractModel):
    r"""DescribeClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterConfList: 返回实例的配置文件相关的信息
        :type ClusterConfList: list of ClusterConfigsInfoFromEMR
        :param _BuildVersion: 返回当前内核版本 如果不存在则返回空字符串
        :type BuildVersion: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _HasCN: 是否包含CN节点
        :type HasCN: bool
        :param _ExistingJarConfList: 实例已经存在的jar包列表
        :type ExistingJarConfList: list of ClusterConfigsInfoFromEMR
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterConfList = None
        self._BuildVersion = None
        self._ErrorMsg = None
        self._HasCN = None
        self._ExistingJarConfList = None
        self._RequestId = None

    @property
    def ClusterConfList(self):
        r"""返回实例的配置文件相关的信息
        :rtype: list of ClusterConfigsInfoFromEMR
        """
        return self._ClusterConfList

    @ClusterConfList.setter
    def ClusterConfList(self, ClusterConfList):
        self._ClusterConfList = ClusterConfList

    @property
    def BuildVersion(self):
        r"""返回当前内核版本 如果不存在则返回空字符串
        :rtype: str
        """
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def HasCN(self):
        r"""是否包含CN节点
        :rtype: bool
        """
        return self._HasCN

    @HasCN.setter
    def HasCN(self, HasCN):
        self._HasCN = HasCN

    @property
    def ExistingJarConfList(self):
        r"""实例已经存在的jar包列表
        :rtype: list of ClusterConfigsInfoFromEMR
        """
        return self._ExistingJarConfList

    @ExistingJarConfList.setter
    def ExistingJarConfList(self, ExistingJarConfList):
        self._ExistingJarConfList = ExistingJarConfList

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
        if params.get("ClusterConfList") is not None:
            self._ClusterConfList = []
            for item in params.get("ClusterConfList"):
                obj = ClusterConfigsInfoFromEMR()
                obj._deserialize(item)
                self._ClusterConfList.append(obj)
        self._BuildVersion = params.get("BuildVersion")
        self._ErrorMsg = params.get("ErrorMsg")
        self._HasCN = params.get("HasCN")
        if params.get("ExistingJarConfList") is not None:
            self._ExistingJarConfList = []
            for item in params.get("ExistingJarConfList"):
                obj = ClusterConfigsInfoFromEMR()
                obj._deserialize(item)
                self._ExistingJarConfList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCoolDownBackendsRequest(AbstractModel):
    r"""DescribeCoolDownBackends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class DescribeCoolDownBackendsResponse(AbstractModel):
    r"""DescribeCoolDownBackends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _List: 节点信息列表
        :type List: list of CoolDownBackend
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        r"""节点信息列表
        :rtype: list of CoolDownBackend
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownBackend()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCoolDownPoliciesRequest(AbstractModel):
    r"""DescribeCoolDownPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class DescribeCoolDownPoliciesResponse(AbstractModel):
    r"""DescribeCoolDownPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _List: 冷热分层策略列表
        :type List: list of CoolDownPolicyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        r"""冷热分层策略列表
        :rtype: list of CoolDownPolicyInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCoolDownTableDataRequest(AbstractModel):
    r"""DescribeCoolDownTableData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        """
        self._InstanceId = None
        self._DatabaseName = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DatabaseName(self):
        r"""数据库名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCoolDownTableDataResponse(AbstractModel):
    r"""DescribeCoolDownTableData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _List: 冷热分层Table数据列表
        :type List: list of CoolDownTableDataInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        r"""冷热分层Table数据列表
        :rtype: list of CoolDownTableDataInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownTableDataInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditDownloadRequest(AbstractModel):
    r"""DescribeDatabaseAuditDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _PageSize: 分页
        :type PageSize: int
        :param _PageNum: 分页
        :type PageNum: int
        :param _OrderType: 排序参数
        :type OrderType: str
        :param _User: 用户
        :type User: str
        :param _DbName: 数据库
        :type DbName: str
        :param _SqlType: sql类型
        :type SqlType: str
        :param _Sql: sql语句
        :type Sql: str
        :param _Users: 用户 多选
        :type Users: list of str
        :param _DbNames: 数据库 多选
        :type DbNames: list of str
        :param _SqlTypes: sql类型 多选
        :type SqlTypes: list of str
        :param _Catalogs: catalog名称 （多选）
        :type Catalogs: list of str
        :param _IsQuery: 是否是查询	
        :type IsQuery: list of bool
        :param _ComputeGroups: 计算组列表
        :type ComputeGroups: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None
        self._IsQuery = None
        self._ComputeGroups = None

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
    def PageSize(self):
        r"""分页
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""分页
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        r"""排序参数
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        r"""用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        r"""数据库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        r"""sql类型
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        r"""sql语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        r"""用户 多选
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        r"""数据库 多选
        :rtype: list of str
        """
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        r"""sql类型 多选
        :rtype: list of str
        """
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        r"""catalog名称 （多选）
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs

    @property
    def IsQuery(self):
        r"""是否是查询	
        :rtype: list of bool
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ComputeGroups(self):
        r"""计算组列表
        :rtype: list of str
        """
        return self._ComputeGroups

    @ComputeGroups.setter
    def ComputeGroups(self, ComputeGroups):
        self._ComputeGroups = ComputeGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        self._IsQuery = params.get("IsQuery")
        self._ComputeGroups = params.get("ComputeGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditDownloadResponse(AbstractModel):
    r"""DescribeDatabaseAuditDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosUrl: 日志的cos地址
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        r"""日志的cos地址
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

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
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditRecordsRequest(AbstractModel):
    r"""DescribeDatabaseAuditRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _PageSize: 分页
        :type PageSize: int
        :param _PageNum: 分页
        :type PageNum: int
        :param _OrderType: 排序参数
        :type OrderType: str
        :param _User: 用户
        :type User: str
        :param _DbName: 数据库
        :type DbName: str
        :param _SqlType: sql类型
        :type SqlType: str
        :param _Sql: sql语句
        :type Sql: str
        :param _Users: 用户 （多选）
        :type Users: list of str
        :param _DbNames: 数据库 （多选）
        :type DbNames: list of str
        :param _SqlTypes: sql类型 （多选）
        :type SqlTypes: list of str
        :param _Catalogs: catalog名称（多选）
        :type Catalogs: list of str
        :param _IsQuery: 是否是查询 
        :type IsQuery: list of bool
        :param _ComputeGroups: 计算组列表
        :type ComputeGroups: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None
        self._IsQuery = None
        self._ComputeGroups = None

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
    def PageSize(self):
        r"""分页
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""分页
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        r"""排序参数
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        r"""用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        r"""数据库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        r"""sql类型
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        r"""sql语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        r"""用户 （多选）
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        r"""数据库 （多选）
        :rtype: list of str
        """
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        r"""sql类型 （多选）
        :rtype: list of str
        """
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        r"""catalog名称（多选）
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs

    @property
    def IsQuery(self):
        r"""是否是查询 
        :rtype: list of bool
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ComputeGroups(self):
        r"""计算组列表
        :rtype: list of str
        """
        return self._ComputeGroups

    @ComputeGroups.setter
    def ComputeGroups(self, ComputeGroups):
        self._ComputeGroups = ComputeGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        self._IsQuery = params.get("IsQuery")
        self._ComputeGroups = params.get("ComputeGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditRecordsResponse(AbstractModel):
    r"""DescribeDatabaseAuditRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _SlowQueryRecords: 记录列表
        :type SlowQueryRecords: :class:`tencentcloud.cdwdoris.v20211228.models.DataBaseAuditRecord`
        :param _Records: 记录列表
        :type Records: list of DataBaseAuditRecord
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._Records = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        r"""记录列表
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DataBaseAuditRecord`
        """
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

    @property
    def Records(self):
        r"""记录列表
        :rtype: list of DataBaseAuditRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = DataBaseAuditRecord()
            self._SlowQueryRecords._deserialize(params.get("SlowQueryRecords"))
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = DataBaseAuditRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesInfoRequest(AbstractModel):
    r"""DescribeInstanceNodesInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 集群id
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesInfoResponse(AbstractModel):
    r"""DescribeInstanceNodesInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BeNodes: Be节点
        :type BeNodes: list of str
        :param _FeNodes: Fe节点
        :type FeNodes: list of str
        :param _FeMaster: Fe master节点
        :type FeMaster: str
        :param _BeNodeInfos: Be节点信息
        :type BeNodeInfos: list of NodeInfo
        :param _FeNodeInfos: Fe节点信息
        :type FeNodeInfos: list of NodeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BeNodes = None
        self._FeNodes = None
        self._FeMaster = None
        self._BeNodeInfos = None
        self._FeNodeInfos = None
        self._RequestId = None

    @property
    def BeNodes(self):
        r"""Be节点
        :rtype: list of str
        """
        return self._BeNodes

    @BeNodes.setter
    def BeNodes(self, BeNodes):
        self._BeNodes = BeNodes

    @property
    def FeNodes(self):
        r"""Fe节点
        :rtype: list of str
        """
        return self._FeNodes

    @FeNodes.setter
    def FeNodes(self, FeNodes):
        self._FeNodes = FeNodes

    @property
    def FeMaster(self):
        r"""Fe master节点
        :rtype: str
        """
        return self._FeMaster

    @FeMaster.setter
    def FeMaster(self, FeMaster):
        self._FeMaster = FeMaster

    @property
    def BeNodeInfos(self):
        r"""Be节点信息
        :rtype: list of NodeInfo
        """
        return self._BeNodeInfos

    @BeNodeInfos.setter
    def BeNodeInfos(self, BeNodeInfos):
        self._BeNodeInfos = BeNodeInfos

    @property
    def FeNodeInfos(self):
        r"""Fe节点信息
        :rtype: list of NodeInfo
        """
        return self._FeNodeInfos

    @FeNodeInfos.setter
    def FeNodeInfos(self, FeNodeInfos):
        self._FeNodeInfos = FeNodeInfos

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
        self._BeNodes = params.get("BeNodes")
        self._FeNodes = params.get("FeNodes")
        self._FeMaster = params.get("FeMaster")
        if params.get("BeNodeInfos") is not None:
            self._BeNodeInfos = []
            for item in params.get("BeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._BeNodeInfos.append(obj)
        if params.get("FeNodeInfos") is not None:
            self._FeNodeInfos = []
            for item in params.get("FeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._FeNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    r"""DescribeInstanceNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _NodeRole: 集群角色类型，默认为 "data"数据节点
        :type NodeRole: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _DisplayPolicy: 展现策略，All时显示所有
        :type DisplayPolicy: str
        """
        self._InstanceId = None
        self._NodeRole = None
        self._Offset = None
        self._Limit = None
        self._DisplayPolicy = None

    @property
    def InstanceId(self):
        r"""集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeRole(self):
        r"""集群角色类型，默认为 "data"数据节点
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def Offset(self):
        r"""分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DisplayPolicy(self):
        r"""展现策略，All时显示所有
        :rtype: str
        """
        return self._DisplayPolicy

    @DisplayPolicy.setter
    def DisplayPolicy(self, DisplayPolicy):
        self._DisplayPolicy = DisplayPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeRole = params.get("NodeRole")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DisplayPolicy = params.get("DisplayPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    r"""DescribeInstanceNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _InstanceNodesList: 实例节点总数
        :type InstanceNodesList: list of InstanceNode
        :param _NodeRoles: 节点类型
        :type NodeRoles: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceNodesList = None
        self._NodeRoles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceNodesList(self):
        r"""实例节点总数
        :rtype: list of InstanceNode
        """
        return self._InstanceNodesList

    @InstanceNodesList.setter
    def InstanceNodesList(self, InstanceNodesList):
        self._InstanceNodesList = InstanceNodesList

    @property
    def NodeRoles(self):
        r"""节点类型
        :rtype: list of str
        """
        return self._NodeRoles

    @NodeRoles.setter
    def NodeRoles(self, NodeRoles):
        self._NodeRoles = NodeRoles

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
        if params.get("InstanceNodesList") is not None:
            self._InstanceNodesList = []
            for item in params.get("InstanceNodesList"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNodesList.append(obj)
        self._NodeRoles = params.get("NodeRoles")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRoleRequest(AbstractModel):
    r"""DescribeInstanceNodesRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _IpFilter: 过滤ip
        :type IpFilter: str
        """
        self._InstanceId = None
        self._IpFilter = None

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
    def IpFilter(self):
        r"""过滤ip
        :rtype: str
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IpFilter = params.get("IpFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesRoleResponse(AbstractModel):
    r"""DescribeInstanceNodesRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误码
        :type ErrorMsg: str
        :param _TotalCount: 节点总数
        :type TotalCount: int
        :param _NodeInfos: 无
        :type NodeInfos: list of NodeInfos
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._TotalCount = None
        self._NodeInfos = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误码
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def TotalCount(self):
        r"""节点总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeInfos(self):
        r"""无
        :rtype: list of NodeInfos
        """
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfos()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    r"""DescribeInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Offset: 分页参数，偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页参数，每页数目，默认为10
        :type Limit: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _ComputeGroupId: 计算组ID
        :type ComputeGroupId: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._ComputeGroupId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""分页参数，偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页参数，每页数目，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def ComputeGroupId(self):
        r"""计算组ID
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ComputeGroupId = params.get("ComputeGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    r"""DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 操作记录总数
        :type TotalCount: int
        :param _Operations: 操作记录具体数据
        :type Operations: list of InstanceOperation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""操作记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        r"""操作记录具体数据
        :rtype: list of InstanceOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = InstanceOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    r"""DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群实例ID
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
        


class DescribeInstanceResponse(AbstractModel):
    r"""DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: 实例描述信息
        :type InstanceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        r"""实例描述信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

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
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    r"""DescribeInstanceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例名称
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群实例名称
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
        


class DescribeInstanceStateResponse(AbstractModel):
    r"""DescribeInstanceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态 
 Init  创建中 
Serving   运行中 
Isolated   已隔离 
Changing  变更中
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
        :type FlowProgress: float
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
        :type FlowMsg: str
        :param _ProcessId: 流程ProcessId
        :type ProcessId: str
        :param _JobName: Job名称
        :type JobName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessId = None
        self._JobName = None
        self._RequestId = None

    @property
    def InstanceState(self):
        r"""集群状态 
 Init  创建中 
Serving   运行中 
Isolated   已隔离 
Changing  变更中
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        r"""集群操作创建时间
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        r"""集群操作名称
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        r"""集群操作进度
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        r"""集群状态描述，例如：运行中
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        r"""集群流程错误信息，例如：“创建失败，资源不足”
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessId(self):
        r"""流程ProcessId
        :rtype: str
        """
        return self._ProcessId

    @ProcessId.setter
    def ProcessId(self, ProcessId):
        self._ProcessId = ProcessId

    @property
    def JobName(self):
        r"""Job名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

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
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessId = params.get("ProcessId")
        self._JobName = params.get("JobName")
        self._RequestId = params.get("RequestId")


class DescribeInstanceUsedSubnetsRequest(AbstractModel):
    r"""DescribeInstanceUsedSubnets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class DescribeInstanceUsedSubnetsResponse(AbstractModel):
    r"""DescribeInstanceUsedSubnets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 集群使用的vpc信息
        :type VpcId: str
        :param _UsedSubnets: 集群使用的subnet信息
        :type UsedSubnets: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcId = None
        self._UsedSubnets = None
        self._RequestId = None

    @property
    def VpcId(self):
        r"""集群使用的vpc信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UsedSubnets(self):
        r"""集群使用的subnet信息
        :rtype: list of str
        """
        return self._UsedSubnets

    @UsedSubnets.setter
    def UsedSubnets(self, UsedSubnets):
        self._UsedSubnets = UsedSubnets

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
        self._VpcId = params.get("VpcId")
        self._UsedSubnets = params.get("UsedSubnets")
        self._RequestId = params.get("RequestId")


class DescribeInstancesHealthStateRequest(AbstractModel):
    r"""DescribeInstancesHealthState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 集群Id
        :type InstanceID: str
        :param _Input: 为空：代表当前appId下所有集群 或者  某个集群Id
        :type Input: str
        """
        self._InstanceID = None
        self._Input = None

    @property
    def InstanceID(self):
        warnings.warn("parameter `InstanceID` is deprecated", DeprecationWarning) 

        r"""集群Id
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        warnings.warn("parameter `InstanceID` is deprecated", DeprecationWarning) 

        self._InstanceID = InstanceID

    @property
    def Input(self):
        r"""为空：代表当前appId下所有集群 或者  某个集群Id
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesHealthStateResponse(AbstractModel):
    r"""DescribeInstancesHealthState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: base64编码后的数据，包含了集群的健康信息
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""base64编码后的数据，包含了集群的健康信息
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: 搜索的集群id名称
        :type SearchInstanceId: str
        :param _SearchInstanceName: 搜索的集群name
        :type SearchInstanceName: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _SearchTags: 搜索标签列表，没匹配到则不过滤集群列表
        :type SearchTags: list of SearchTags
        :param _InstanceType: 0 : 存算一体,1：存算分离,2:ALL
        :type InstanceType: int
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None
        self._InstanceType = None

    @property
    def SearchInstanceId(self):
        r"""搜索的集群id名称
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        r"""搜索的集群name
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        r"""分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        r"""搜索标签列表，没匹配到则不过滤集群列表
        :rtype: list of SearchTags
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags

    @property
    def InstanceType(self):
        r"""0 : 存算一体,1：存算分离,2:ALL
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self._SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self._SearchTags.append(obj)
        self._InstanceType = params.get("InstanceType")
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
        :param _TotalCount: 实例总数
        :type TotalCount: int
        :param _InstancesList: 实例数组
        :type InstancesList: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        r"""实例数组
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

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
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTaskDetailRequest(AbstractModel):
    r"""DescribeRestoreTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTaskDetailResponse(AbstractModel):
    r"""DescribeRestoreTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestoreStatus: 恢复任务进度详情
        :type RestoreStatus: list of RestoreStatus
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestoreStatus = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def RestoreStatus(self):
        r"""恢复任务进度详情
        :rtype: list of RestoreStatus
        """
        return self._RestoreStatus

    @RestoreStatus.setter
    def RestoreStatus(self, RestoreStatus):
        self._RestoreStatus = RestoreStatus

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("RestoreStatus") is not None:
            self._RestoreStatus = []
            for item in params.get("RestoreStatus"):
                obj = RestoreStatus()
                obj._deserialize(item)
                self._RestoreStatus.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsDownloadRequest(AbstractModel):
    r"""DescribeSlowQueryRecordsDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _QueryDurationMs: 慢查询时间
        :type QueryDurationMs: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _DurationMs: 排序参数
        :type DurationMs: str
        :param _Sql: 查询sql
        :type Sql: str
        :param _ReadRows: 排序参数
        :type ReadRows: str
        :param _ResultBytes: 排序参数
        :type ResultBytes: str
        :param _MemoryUsage: 排序参数
        :type MemoryUsage: str
        :param _IsQuery: IsQuery条件
        :type IsQuery: int
        :param _DbName: 数据库名称
        :type DbName: list of str
        :param _CatalogName: catalog名称
        :type CatalogName: list of str
        :param _SortField: 排序字段
        :type SortField: str
        :param _SortOrder: 排序方式
        :type SortOrder: str
        :param _UserName: user
        :type UserName: str
        :param _ComputeGroups: 计算组列表
        :type ComputeGroups: list of str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._DurationMs = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._IsQuery = None
        self._DbName = None
        self._CatalogName = None
        self._SortField = None
        self._SortOrder = None
        self._UserName = None
        self._ComputeGroups = None

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
    def QueryDurationMs(self):
        r"""慢查询时间
        :rtype: int
        """
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

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
    def DurationMs(self):
        r"""排序参数
        :rtype: str
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def Sql(self):
        r"""查询sql
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        r"""排序参数
        :rtype: str
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        r"""排序参数
        :rtype: str
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        r"""排序参数
        :rtype: str
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def IsQuery(self):
        r"""IsQuery条件
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def DbName(self):
        r"""数据库名称
        :rtype: list of str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CatalogName(self):
        r"""catalog名称
        :rtype: list of str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def SortField(self):
        r"""排序字段
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        r"""排序方式
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def UserName(self):
        r"""user
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ComputeGroups(self):
        r"""计算组列表
        :rtype: list of str
        """
        return self._ComputeGroups

    @ComputeGroups.setter
    def ComputeGroups(self, ComputeGroups):
        self._ComputeGroups = ComputeGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DurationMs = params.get("DurationMs")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._IsQuery = params.get("IsQuery")
        self._DbName = params.get("DbName")
        self._CatalogName = params.get("CatalogName")
        self._SortField = params.get("SortField")
        self._SortOrder = params.get("SortOrder")
        self._UserName = params.get("UserName")
        self._ComputeGroups = params.get("ComputeGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsDownloadResponse(AbstractModel):
    r"""DescribeSlowQueryRecordsDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosUrl: cos地址
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        r"""cos地址
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

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
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsRequest(AbstractModel):
    r"""DescribeSlowQueryRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _QueryDurationMs: 慢查询时间
        :type QueryDurationMs: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _PageSize: 分页
        :type PageSize: int
        :param _PageNum: 分页
        :type PageNum: int
        :param _DurationMs: 排序参数
        :type DurationMs: str
        :param _DbName: 数据库名称
        :type DbName: list of str
        :param _IsQuery: 是否是查询，0：否， 1：是
        :type IsQuery: int
        :param _CatalogName: catalog名称
        :type CatalogName: list of str
        :param _Sql: sql名
        :type Sql: str
        :param _ReadRows: ReadRows排序字段
        :type ReadRows: str
        :param _ResultBytes: ResultBytes排序字段
        :type ResultBytes: str
        :param _MemoryUsage: MemoryUsage排序字段
        :type MemoryUsage: str
        :param _SortField: 排序字段
        :type SortField: str
        :param _SortOrder: 排序方式
        :type SortOrder: str
        :param _UserName: user
        :type UserName: str
        :param _ComputeGroups: 计算组列表
        :type ComputeGroups: list of str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._DurationMs = None
        self._DbName = None
        self._IsQuery = None
        self._CatalogName = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._SortField = None
        self._SortOrder = None
        self._UserName = None
        self._ComputeGroups = None

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
    def QueryDurationMs(self):
        r"""慢查询时间
        :rtype: int
        """
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

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
    def PageSize(self):
        r"""分页
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""分页
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def DurationMs(self):
        r"""排序参数
        :rtype: str
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def DbName(self):
        r"""数据库名称
        :rtype: list of str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        r"""是否是查询，0：否， 1：是
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def CatalogName(self):
        r"""catalog名称
        :rtype: list of str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def Sql(self):
        r"""sql名
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        r"""ReadRows排序字段
        :rtype: str
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        r"""ResultBytes排序字段
        :rtype: str
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        r"""MemoryUsage排序字段
        :rtype: str
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def SortField(self):
        r"""排序字段
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        r"""排序方式
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def UserName(self):
        r"""user
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ComputeGroups(self):
        r"""计算组列表
        :rtype: list of str
        """
        return self._ComputeGroups

    @ComputeGroups.setter
    def ComputeGroups(self, ComputeGroups):
        self._ComputeGroups = ComputeGroups


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._DurationMs = params.get("DurationMs")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._CatalogName = params.get("CatalogName")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._SortField = params.get("SortField")
        self._SortOrder = params.get("SortOrder")
        self._UserName = params.get("UserName")
        self._ComputeGroups = params.get("ComputeGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsResponse(AbstractModel):
    r"""DescribeSlowQueryRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _SlowQueryRecords: 记录列表
        :type SlowQueryRecords: list of SlowQueryRecord
        :param _DBNameList: 所有数据库名
        :type DBNameList: list of str
        :param _CatalogNameList: 所有catalog名
        :type CatalogNameList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._DBNameList = None
        self._CatalogNameList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        r"""记录列表
        :rtype: list of SlowQueryRecord
        """
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

    @property
    def DBNameList(self):
        r"""所有数据库名
        :rtype: list of str
        """
        return self._DBNameList

    @DBNameList.setter
    def DBNameList(self, DBNameList):
        self._DBNameList = DBNameList

    @property
    def CatalogNameList(self):
        r"""所有catalog名
        :rtype: list of str
        """
        return self._CatalogNameList

    @CatalogNameList.setter
    def CatalogNameList(self, CatalogNameList):
        self._CatalogNameList = CatalogNameList

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
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = []
            for item in params.get("SlowQueryRecords"):
                obj = SlowQueryRecord()
                obj._deserialize(item)
                self._SlowQueryRecords.append(obj)
        self._DBNameList = params.get("DBNameList")
        self._CatalogNameList = params.get("CatalogNameList")
        self._RequestId = params.get("RequestId")


class DescribeSpecRequest(AbstractModel):
    r"""DescribeSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 地域信息，例如"ap-guangzhou-1"
        :type Zone: str
        :param _PayMode: 计费类型，PREPAID 包年包月，POSTPAID_BY_HOUR 按量计费
        :type PayMode: str
        :param _Zones: 多可用区
        :type Zones: list of str
        :param _SpecName: 机型名称
        :type SpecName: str
        :param _IsSSC: 是否存算分离
        :type IsSSC: bool
        """
        self._Zone = None
        self._PayMode = None
        self._Zones = None
        self._SpecName = None
        self._IsSSC = None

    @property
    def Zone(self):
        r"""地域信息，例如"ap-guangzhou-1"
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def PayMode(self):
        r"""计费类型，PREPAID 包年包月，POSTPAID_BY_HOUR 按量计费
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Zones(self):
        r"""多可用区
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SpecName(self):
        r"""机型名称
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def IsSSC(self):
        r"""是否存算分离
        :rtype: bool
        """
        return self._IsSSC

    @IsSSC.setter
    def IsSSC(self, IsSSC):
        self._IsSSC = IsSSC


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._PayMode = params.get("PayMode")
        self._Zones = params.get("Zones")
        self._SpecName = params.get("SpecName")
        self._IsSSC = params.get("IsSSC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecResponse(AbstractModel):
    r"""DescribeSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MasterSpec: fe节点规格描述
        :type MasterSpec: list of ResourceSpec
        :param _CoreSpec: be节点规格描述
        :type CoreSpec: list of ResourceSpec
        :param _AttachCBSSpec: 云盘列表
        :type AttachCBSSpec: list of DiskSpec
        :param _CNSpec: cn节点列表
        :type CNSpec: list of ResourceSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MasterSpec = None
        self._CoreSpec = None
        self._AttachCBSSpec = None
        self._CNSpec = None
        self._RequestId = None

    @property
    def MasterSpec(self):
        r"""fe节点规格描述
        :rtype: list of ResourceSpec
        """
        return self._MasterSpec

    @MasterSpec.setter
    def MasterSpec(self, MasterSpec):
        self._MasterSpec = MasterSpec

    @property
    def CoreSpec(self):
        r"""be节点规格描述
        :rtype: list of ResourceSpec
        """
        return self._CoreSpec

    @CoreSpec.setter
    def CoreSpec(self, CoreSpec):
        self._CoreSpec = CoreSpec

    @property
    def AttachCBSSpec(self):
        r"""云盘列表
        :rtype: list of DiskSpec
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def CNSpec(self):
        r"""cn节点列表
        :rtype: list of ResourceSpec
        """
        return self._CNSpec

    @CNSpec.setter
    def CNSpec(self, CNSpec):
        self._CNSpec = CNSpec

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
        if params.get("MasterSpec") is not None:
            self._MasterSpec = []
            for item in params.get("MasterSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._MasterSpec.append(obj)
        if params.get("CoreSpec") is not None:
            self._CoreSpec = []
            for item in params.get("CoreSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._CoreSpec.append(obj)
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = []
            for item in params.get("AttachCBSSpec"):
                obj = DiskSpec()
                obj._deserialize(item)
                self._AttachCBSSpec.append(obj)
        if params.get("CNSpec") is not None:
            self._CNSpec = []
            for item in params.get("CNSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._CNSpec.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSqlApisRequest(AbstractModel):
    r"""DescribeSqlApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ApiType: GetUsers：获取用户列表；
GetDatabases：获取数据库列表；
GetTables：获取数据库表列表；
GetUserPrivilegesV2：获取用户下的权限，粒度到表级别；
DeleteUser：删除用户；
GetCatalog：获取Catalog列表；
        :type ApiType: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _WhiteHost: 用户链接来自的 IP
        :type WhiteHost: str
        :param _Catalog: catalog名称
        :type Catalog: str
        :param _Catalogs: catalog集合
        :type Catalogs: list of str
        :param _DatabaseName: 数据库名
        :type DatabaseName: str
        :param _TableName: 表名
        :type TableName: str
        :param _UserNames: 用户名列表
        :type UserNames: list of str
        """
        self._InstanceId = None
        self._ApiType = None
        self._UserName = None
        self._WhiteHost = None
        self._Catalog = None
        self._Catalogs = None
        self._DatabaseName = None
        self._TableName = None
        self._UserNames = None

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
    def ApiType(self):
        r"""GetUsers：获取用户列表；
GetDatabases：获取数据库列表；
GetTables：获取数据库表列表；
GetUserPrivilegesV2：获取用户下的权限，粒度到表级别；
DeleteUser：删除用户；
GetCatalog：获取Catalog列表；
        :rtype: str
        """
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def UserName(self):
        r"""用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def WhiteHost(self):
        r"""用户链接来自的 IP
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost

    @property
    def Catalog(self):
        r"""catalog名称
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Catalogs(self):
        r"""catalog集合
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs

    @property
    def DatabaseName(self):
        r"""数据库名
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def UserNames(self):
        r"""用户名列表
        :rtype: list of str
        """
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ApiType = params.get("ApiType")
        self._UserName = params.get("UserName")
        self._WhiteHost = params.get("WhiteHost")
        self._Catalog = params.get("Catalog")
        self._Catalogs = params.get("Catalogs")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._UserNames = params.get("UserNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlApisResponse(AbstractModel):
    r"""DescribeSqlApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnData: 返回的查询数据，大部分情况是list，也可能是bool
        :type ReturnData: str
        :param _ErrorMsg: 错误消息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnData = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ReturnData(self):
        r"""返回的查询数据，大部分情况是list，也可能是bool
        :rtype: str
        """
        return self._ReturnData

    @ReturnData.setter
    def ReturnData(self, ReturnData):
        self._ReturnData = ReturnData

    @property
    def ErrorMsg(self):
        r"""错误消息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ReturnData = params.get("ReturnData")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeTableListRequest(AbstractModel):
    r"""DescribeTableList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源ID，建表所用的TCHouse-D资源ID。
        :type InstanceId: str
        :param _DbName: 需要获取表列表的库
        :type DbName: str
        :param _UserName: 使用该用户进行操作，该用户需要有对应的权限。如果该TCHouse-D集群使用CAM用户注册内核账户，则不需要填写
        :type UserName: str
        :param _PassWord: 用户对应的密码。如果该TCHouse-D集群使用CAM用户注册内核账户，则不需要填写
        :type PassWord: str
        :param _CatalogName: 查询库所在的数据源，不填则默认为内部数据源（internal）。
        :type CatalogName: str
        """
        self._InstanceId = None
        self._DbName = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def InstanceId(self):
        r"""资源ID，建表所用的TCHouse-D资源ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""需要获取表列表的库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def UserName(self):
        r"""使用该用户进行操作，该用户需要有对应的权限。如果该TCHouse-D集群使用CAM用户注册内核账户，则不需要填写
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        r"""用户对应的密码。如果该TCHouse-D集群使用CAM用户注册内核账户，则不需要填写
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        r"""查询库所在的数据源，不填则默认为内部数据源（internal）。
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableListResponse(AbstractModel):
    r"""DescribeTableList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableNames: 表名列表
        :type TableNames: list of str
        :param _Message: 错误信息
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableNames = None
        self._Message = None
        self._RequestId = None

    @property
    def TableNames(self):
        r"""表名列表
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._TableNames = params.get("TableNames")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeUserBindWorkloadGroupRequest(AbstractModel):
    r"""DescribeUserBindWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class DescribeUserBindWorkloadGroupResponse(AbstractModel):
    r"""DescribeUserBindWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserBindInfos: 用户绑定资源组信息
        :type UserBindInfos: list of UserWorkloadGroup
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserBindInfos = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def UserBindInfos(self):
        r"""用户绑定资源组信息
        :rtype: list of UserWorkloadGroup
        """
        return self._UserBindInfos

    @UserBindInfos.setter
    def UserBindInfos(self, UserBindInfos):
        self._UserBindInfos = UserBindInfos

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("UserBindInfos") is not None:
            self._UserBindInfos = []
            for item in params.get("UserBindInfos"):
                obj = UserWorkloadGroup()
                obj._deserialize(item)
                self._UserBindInfos.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeWorkloadGroupRequest(AbstractModel):
    r"""DescribeWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class DescribeWorkloadGroupResponse(AbstractModel):
    r"""DescribeWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkloadGroups: 资源组信息
        :type WorkloadGroups: list of WorkloadGroupConfig
        :param _Status: 是否开启资源组：开启-open、关闭-close
        :type Status: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkloadGroups = None
        self._Status = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def WorkloadGroups(self):
        r"""资源组信息
        :rtype: list of WorkloadGroupConfig
        """
        return self._WorkloadGroups

    @WorkloadGroups.setter
    def WorkloadGroups(self, WorkloadGroups):
        self._WorkloadGroups = WorkloadGroups

    @property
    def Status(self):
        r"""是否开启资源组：开启-open、关闭-close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("WorkloadGroups") is not None:
            self._WorkloadGroups = []
            for item in params.get("WorkloadGroups"):
                obj = WorkloadGroupConfig()
                obj._deserialize(item)
                self._WorkloadGroups.append(obj)
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DestroyInstanceRequest(AbstractModel):
    r"""DestroyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群ID
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
        


class DestroyInstanceResponse(AbstractModel):
    r"""DestroyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpec(AbstractModel):
    r"""磁盘规格描述

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型，例如“CLOUD_SSD", "LOCAL_SSD"等
        :type DiskType: str
        :param _DiskDesc: 磁盘类型说明，例如"云SSD", "本地SSD"等
        :type DiskDesc: str
        :param _MinDiskSize: 磁盘最小规格大小，单位G
        :type MinDiskSize: int
        :param _MaxDiskSize: 磁盘最大规格大小，单位G
        :type MaxDiskSize: int
        :param _DiskCount: 磁盘数目
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskDesc = None
        self._MinDiskSize = None
        self._MaxDiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        r"""磁盘类型，例如“CLOUD_SSD", "LOCAL_SSD"等
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        r"""磁盘类型说明，例如"云SSD", "本地SSD"等
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def MinDiskSize(self):
        r"""磁盘最小规格大小，单位G
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        r"""磁盘最大规格大小，单位G
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def DiskCount(self):
        r"""磁盘数目
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        self._MinDiskSize = params.get("MinDiskSize")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DorisSourceInfo(AbstractModel):
    r"""外部doris集群的连接信息

    """

    def __init__(self):
        r"""
        :param _Host: doris集群的fe的ip
        :type Host: str
        :param _Port: doris集群的fe的端口号
        :type Port: int
        :param _User: doris集群的账号
        :type User: str
        :param _Password: base64编码的doris集群对应用户的密码
        :type Password: str
        """
        self._Host = None
        self._Port = None
        self._User = None
        self._Password = None

    @property
    def Host(self):
        r"""doris集群的fe的ip
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""doris集群的fe的端口号
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        r"""doris集群的账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""base64编码的doris集群对应用户的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrontEndRule(AbstractModel):
    r"""前端规则描述

    """

    def __init__(self):
        r"""
        :param _ID: id序列
        :type ID: int
        :param _Name: 规则名称
        :type Name: str
        :param _Rule: 详细规则
        :type Rule: str
        """
        self._ID = None
        self._Name = None
        self._Rule = None

    @property
    def ID(self):
        r"""id序列
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rule(self):
        r"""详细规则
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Rule = params.get("Rule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigItem(AbstractModel):
    r"""KV配置

    """

    def __init__(self):
        r"""
        :param _ConfKey: key
        :type ConfKey: str
        :param _ConfValue: value
        :type ConfValue: str
        """
        self._ConfKey = None
        self._ConfValue = None

    @property
    def ConfKey(self):
        r"""key
        :rtype: str
        """
        return self._ConfKey

    @ConfKey.setter
    def ConfKey(self, ConfKey):
        self._ConfKey = ConfKey

    @property
    def ConfValue(self):
        r"""value
        :rtype: str
        """
        return self._ConfValue

    @ConfValue.setter
    def ConfValue(self, ConfValue):
        self._ConfValue = ConfValue


    def _deserialize(self, params):
        self._ConfKey = params.get("ConfKey")
        self._ConfValue = params.get("ConfValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    r"""Instance表detail字段

    """

    def __init__(self):
        r"""
        :param _EnableAlarmStrategy: 告警策略是否可用	
        :type EnableAlarmStrategy: bool
        """
        self._EnableAlarmStrategy = None

    @property
    def EnableAlarmStrategy(self):
        r"""告警策略是否可用	
        :rtype: bool
        """
        return self._EnableAlarmStrategy

    @EnableAlarmStrategy.setter
    def EnableAlarmStrategy(self, EnableAlarmStrategy):
        self._EnableAlarmStrategy = EnableAlarmStrategy


    def _deserialize(self, params):
        self._EnableAlarmStrategy = params.get("EnableAlarmStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    r"""实例描述信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID, "cdwdoris-xxxx" 字符串类型
        :type InstanceId: str
        :param _InstanceName: 集群实例名称
        :type InstanceName: str
        :param _Status: 状态,
Init  创建中
Serving   运行中
Isolated   已隔离
Changing  变更中
        :type Status: str
        :param _Version: 版本
        :type Version: str
        :param _Region: 地域, ap-guangzhou
        :type Region: str
        :param _Zone: 可用区， ap-guangzhou-3
        :type Zone: str
        :param _VpcId: 私有网络名称
        :type VpcId: str
        :param _SubnetId: 子网名称
        :type SubnetId: str
        :param _PayMode: 付费类型，"hour", "prepay"
        :type PayMode: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _MasterSummary: 数据节点描述信息
        :type MasterSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _CoreSummary: zookeeper节点描述信息
        :type CoreSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _HA: 高可用，"true" "false"
        :type HA: str
        :param _HaType: 高可用类型：
0：非高可用
1：读高可用
2：读写高可用。
        :type HaType: int
        :param _AccessInfo: 访问地址，例如 "10.0.0.1:9000"
        :type AccessInfo: str
        :param _Id: 记录ID，数值型
        :type Id: int
        :param _RegionId: regionId, 表示地域
        :type RegionId: int
        :param _ZoneDesc: 可用区说明，例如 "广州三区"
        :type ZoneDesc: str
        :param _FlowMsg: 错误流程说明信息
        :type FlowMsg: str
        :param _StatusDesc: 状态描述，例如“运行中”等
        :type StatusDesc: str
        :param _RenewFlag: 自动续费标记
        :type RenewFlag: bool
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _Monitor: 监控信息
        :type Monitor: str
        :param _HasClsTopic: 是否开通日志
        :type HasClsTopic: bool
        :param _ClsTopicId: 日志主题ID
        :type ClsTopicId: str
        :param _ClsLogSetId: 日志集ID
        :type ClsLogSetId: str
        :param _EnableXMLConfig: 是否支持xml配置管理
        :type EnableXMLConfig: int
        :param _RegionDesc: 区域
        :type RegionDesc: str
        :param _Eip: 弹性网卡地址
        :type Eip: str
        :param _CosMoveFactor: 冷热分层系数
        :type CosMoveFactor: int
        :param _Kind: external/local/yunti
        :type Kind: str
        :param _CosBucketName: cos桶
        :type CosBucketName: str
        :param _CanAttachCbs: cbs
        :type CanAttachCbs: bool
        :param _BuildVersion: 小版本
        :type BuildVersion: str
        :param _Components: 组件信息
注：这里返回类型实际为map[string]struct类型，并非显示的string类型，可以参考“示例值”进行数据的解析。
        :type Components: str
        :param _IfExistCatalog: 判断审计日志表是否有catalog字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IfExistCatalog: int
        :param _Characteristic: 页面特性，用于前端屏蔽一些页面入口
        :type Characteristic: list of str
        :param _RestartTimeout: 超时时间 单位s
        :type RestartTimeout: str
        :param _GraceShutdownWaitSeconds: 内核优雅重启超时时间，如果为-1说明未设置
        :type GraceShutdownWaitSeconds: str
        :param _CaseSensitive: 表名大小写是否敏感，0：敏感；1：不敏感，以小写进行比较；2：不敏感，表名改为以小写存储
        :type CaseSensitive: int
        :param _IsWhiteSGs: 用户是否可以绑定安全组
        :type IsWhiteSGs: bool
        :param _BindSGs: 已绑定的安全组信息
        :type BindSGs: list of str
        :param _EnableMultiZones: 是否为多可用区
        :type EnableMultiZones: bool
        :param _UserNetworkInfos: 用户可用区和子网信息
        :type UserNetworkInfos: str
        :param _EnableCoolDown: 是否启用冷热分层。0：未开启 1：已开启
        :type EnableCoolDown: int
        :param _CoolDownBucket: 冷热分层使用COS桶
        :type CoolDownBucket: str
        :param _Details: 实例扩展信息
        :type Details: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceDetail`
        :param _EnableDlc: 是否启用DLC 0:关闭 1:开启
        :type EnableDlc: int
        :param _AccountType: 账户类型 0:普通用户 1:CAM用户
        :type AccountType: int
        :param _MonitorMode: 监控模式 0: 老监控 1：新监控
        :type MonitorMode: int
        :param _CNSummary: cn节点信息
        :type CNSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _ComputeGroupCount: 计算组个数
        :type ComputeGroupCount: int
        :param _CosStorageSize: 存算分离cos存储数据
        :type CosStorageSize: float
        :param _IsMasterNonVM: 存算分离的指标 当是true 不支持新建计算组
        :type IsMasterNonVM: bool
        :param _CosPkgCapacity: Cos容量包大小
        :type CosPkgCapacity: int
        :param _UseManagedBucket: 集群是否使用托管桶
        :type UseManagedBucket: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._Version = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._CreateTime = None
        self._ExpireTime = None
        self._MasterSummary = None
        self._CoreSummary = None
        self._HA = None
        self._HaType = None
        self._AccessInfo = None
        self._Id = None
        self._RegionId = None
        self._ZoneDesc = None
        self._FlowMsg = None
        self._StatusDesc = None
        self._RenewFlag = None
        self._Tags = None
        self._Monitor = None
        self._HasClsTopic = None
        self._ClsTopicId = None
        self._ClsLogSetId = None
        self._EnableXMLConfig = None
        self._RegionDesc = None
        self._Eip = None
        self._CosMoveFactor = None
        self._Kind = None
        self._CosBucketName = None
        self._CanAttachCbs = None
        self._BuildVersion = None
        self._Components = None
        self._IfExistCatalog = None
        self._Characteristic = None
        self._RestartTimeout = None
        self._GraceShutdownWaitSeconds = None
        self._CaseSensitive = None
        self._IsWhiteSGs = None
        self._BindSGs = None
        self._EnableMultiZones = None
        self._UserNetworkInfos = None
        self._EnableCoolDown = None
        self._CoolDownBucket = None
        self._Details = None
        self._EnableDlc = None
        self._AccountType = None
        self._MonitorMode = None
        self._CNSummary = None
        self._ComputeGroupCount = None
        self._CosStorageSize = None
        self._IsMasterNonVM = None
        self._CosPkgCapacity = None
        self._UseManagedBucket = None

    @property
    def InstanceId(self):
        r"""集群实例ID, "cdwdoris-xxxx" 字符串类型
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        r"""状态,
Init  创建中
Serving   运行中
Isolated   已隔离
Changing  变更中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        r"""版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        r"""地域, ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""可用区， ap-guangzhou-3
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""私有网络名称
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网名称
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        r"""付费类型，"hour", "prepay"
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

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
    def ExpireTime(self):
        r"""过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def MasterSummary(self):
        r"""数据节点描述信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        """
        return self._MasterSummary

    @MasterSummary.setter
    def MasterSummary(self, MasterSummary):
        self._MasterSummary = MasterSummary

    @property
    def CoreSummary(self):
        r"""zookeeper节点描述信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        """
        return self._CoreSummary

    @CoreSummary.setter
    def CoreSummary(self, CoreSummary):
        self._CoreSummary = CoreSummary

    @property
    def HA(self):
        r"""高可用，"true" "false"
        :rtype: str
        """
        return self._HA

    @HA.setter
    def HA(self, HA):
        self._HA = HA

    @property
    def HaType(self):
        r"""高可用类型：
0：非高可用
1：读高可用
2：读写高可用。
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def AccessInfo(self):
        r"""访问地址，例如 "10.0.0.1:9000"
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def Id(self):
        r"""记录ID，数值型
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionId(self):
        r"""regionId, 表示地域
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneDesc(self):
        r"""可用区说明，例如 "广州三区"
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def FlowMsg(self):
        r"""错误流程说明信息
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def StatusDesc(self):
        r"""状态描述，例如“运行中”等
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RenewFlag(self):
        r"""自动续费标记
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Tags(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Monitor(self):
        r"""监控信息
        :rtype: str
        """
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor):
        self._Monitor = Monitor

    @property
    def HasClsTopic(self):
        r"""是否开通日志
        :rtype: bool
        """
        return self._HasClsTopic

    @HasClsTopic.setter
    def HasClsTopic(self, HasClsTopic):
        self._HasClsTopic = HasClsTopic

    @property
    def ClsTopicId(self):
        r"""日志主题ID
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def ClsLogSetId(self):
        r"""日志集ID
        :rtype: str
        """
        return self._ClsLogSetId

    @ClsLogSetId.setter
    def ClsLogSetId(self, ClsLogSetId):
        self._ClsLogSetId = ClsLogSetId

    @property
    def EnableXMLConfig(self):
        r"""是否支持xml配置管理
        :rtype: int
        """
        return self._EnableXMLConfig

    @EnableXMLConfig.setter
    def EnableXMLConfig(self, EnableXMLConfig):
        self._EnableXMLConfig = EnableXMLConfig

    @property
    def RegionDesc(self):
        r"""区域
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Eip(self):
        r"""弹性网卡地址
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CosMoveFactor(self):
        r"""冷热分层系数
        :rtype: int
        """
        return self._CosMoveFactor

    @CosMoveFactor.setter
    def CosMoveFactor(self, CosMoveFactor):
        self._CosMoveFactor = CosMoveFactor

    @property
    def Kind(self):
        r"""external/local/yunti
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def CosBucketName(self):
        r"""cos桶
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CanAttachCbs(self):
        r"""cbs
        :rtype: bool
        """
        return self._CanAttachCbs

    @CanAttachCbs.setter
    def CanAttachCbs(self, CanAttachCbs):
        self._CanAttachCbs = CanAttachCbs

    @property
    def BuildVersion(self):
        r"""小版本
        :rtype: str
        """
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

    @property
    def Components(self):
        r"""组件信息
注：这里返回类型实际为map[string]struct类型，并非显示的string类型，可以参考“示例值”进行数据的解析。
        :rtype: str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def IfExistCatalog(self):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        r"""判断审计日志表是否有catalog字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IfExistCatalog

    @IfExistCatalog.setter
    def IfExistCatalog(self, IfExistCatalog):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        self._IfExistCatalog = IfExistCatalog

    @property
    def Characteristic(self):
        r"""页面特性，用于前端屏蔽一些页面入口
        :rtype: list of str
        """
        return self._Characteristic

    @Characteristic.setter
    def Characteristic(self, Characteristic):
        self._Characteristic = Characteristic

    @property
    def RestartTimeout(self):
        r"""超时时间 单位s
        :rtype: str
        """
        return self._RestartTimeout

    @RestartTimeout.setter
    def RestartTimeout(self, RestartTimeout):
        self._RestartTimeout = RestartTimeout

    @property
    def GraceShutdownWaitSeconds(self):
        r"""内核优雅重启超时时间，如果为-1说明未设置
        :rtype: str
        """
        return self._GraceShutdownWaitSeconds

    @GraceShutdownWaitSeconds.setter
    def GraceShutdownWaitSeconds(self, GraceShutdownWaitSeconds):
        self._GraceShutdownWaitSeconds = GraceShutdownWaitSeconds

    @property
    def CaseSensitive(self):
        r"""表名大小写是否敏感，0：敏感；1：不敏感，以小写进行比较；2：不敏感，表名改为以小写存储
        :rtype: int
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def IsWhiteSGs(self):
        r"""用户是否可以绑定安全组
        :rtype: bool
        """
        return self._IsWhiteSGs

    @IsWhiteSGs.setter
    def IsWhiteSGs(self, IsWhiteSGs):
        self._IsWhiteSGs = IsWhiteSGs

    @property
    def BindSGs(self):
        r"""已绑定的安全组信息
        :rtype: list of str
        """
        return self._BindSGs

    @BindSGs.setter
    def BindSGs(self, BindSGs):
        self._BindSGs = BindSGs

    @property
    def EnableMultiZones(self):
        r"""是否为多可用区
        :rtype: bool
        """
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserNetworkInfos(self):
        r"""用户可用区和子网信息
        :rtype: str
        """
        return self._UserNetworkInfos

    @UserNetworkInfos.setter
    def UserNetworkInfos(self, UserNetworkInfos):
        self._UserNetworkInfos = UserNetworkInfos

    @property
    def EnableCoolDown(self):
        r"""是否启用冷热分层。0：未开启 1：已开启
        :rtype: int
        """
        return self._EnableCoolDown

    @EnableCoolDown.setter
    def EnableCoolDown(self, EnableCoolDown):
        self._EnableCoolDown = EnableCoolDown

    @property
    def CoolDownBucket(self):
        r"""冷热分层使用COS桶
        :rtype: str
        """
        return self._CoolDownBucket

    @CoolDownBucket.setter
    def CoolDownBucket(self, CoolDownBucket):
        self._CoolDownBucket = CoolDownBucket

    @property
    def Details(self):
        r"""实例扩展信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceDetail`
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def EnableDlc(self):
        r"""是否启用DLC 0:关闭 1:开启
        :rtype: int
        """
        return self._EnableDlc

    @EnableDlc.setter
    def EnableDlc(self, EnableDlc):
        self._EnableDlc = EnableDlc

    @property
    def AccountType(self):
        r"""账户类型 0:普通用户 1:CAM用户
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def MonitorMode(self):
        r"""监控模式 0: 老监控 1：新监控
        :rtype: int
        """
        return self._MonitorMode

    @MonitorMode.setter
    def MonitorMode(self, MonitorMode):
        self._MonitorMode = MonitorMode

    @property
    def CNSummary(self):
        r"""cn节点信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        """
        return self._CNSummary

    @CNSummary.setter
    def CNSummary(self, CNSummary):
        self._CNSummary = CNSummary

    @property
    def ComputeGroupCount(self):
        r"""计算组个数
        :rtype: int
        """
        return self._ComputeGroupCount

    @ComputeGroupCount.setter
    def ComputeGroupCount(self, ComputeGroupCount):
        self._ComputeGroupCount = ComputeGroupCount

    @property
    def CosStorageSize(self):
        r"""存算分离cos存储数据
        :rtype: float
        """
        return self._CosStorageSize

    @CosStorageSize.setter
    def CosStorageSize(self, CosStorageSize):
        self._CosStorageSize = CosStorageSize

    @property
    def IsMasterNonVM(self):
        r"""存算分离的指标 当是true 不支持新建计算组
        :rtype: bool
        """
        return self._IsMasterNonVM

    @IsMasterNonVM.setter
    def IsMasterNonVM(self, IsMasterNonVM):
        self._IsMasterNonVM = IsMasterNonVM

    @property
    def CosPkgCapacity(self):
        r"""Cos容量包大小
        :rtype: int
        """
        return self._CosPkgCapacity

    @CosPkgCapacity.setter
    def CosPkgCapacity(self, CosPkgCapacity):
        self._CosPkgCapacity = CosPkgCapacity

    @property
    def UseManagedBucket(self):
        r"""集群是否使用托管桶
        :rtype: bool
        """
        return self._UseManagedBucket

    @UseManagedBucket.setter
    def UseManagedBucket(self, UseManagedBucket):
        self._UseManagedBucket = UseManagedBucket


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("MasterSummary") is not None:
            self._MasterSummary = NodesSummary()
            self._MasterSummary._deserialize(params.get("MasterSummary"))
        if params.get("CoreSummary") is not None:
            self._CoreSummary = NodesSummary()
            self._CoreSummary._deserialize(params.get("CoreSummary"))
        self._HA = params.get("HA")
        self._HaType = params.get("HaType")
        self._AccessInfo = params.get("AccessInfo")
        self._Id = params.get("Id")
        self._RegionId = params.get("RegionId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._StatusDesc = params.get("StatusDesc")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Monitor = params.get("Monitor")
        self._HasClsTopic = params.get("HasClsTopic")
        self._ClsTopicId = params.get("ClsTopicId")
        self._ClsLogSetId = params.get("ClsLogSetId")
        self._EnableXMLConfig = params.get("EnableXMLConfig")
        self._RegionDesc = params.get("RegionDesc")
        self._Eip = params.get("Eip")
        self._CosMoveFactor = params.get("CosMoveFactor")
        self._Kind = params.get("Kind")
        self._CosBucketName = params.get("CosBucketName")
        self._CanAttachCbs = params.get("CanAttachCbs")
        self._BuildVersion = params.get("BuildVersion")
        self._Components = params.get("Components")
        self._IfExistCatalog = params.get("IfExistCatalog")
        self._Characteristic = params.get("Characteristic")
        self._RestartTimeout = params.get("RestartTimeout")
        self._GraceShutdownWaitSeconds = params.get("GraceShutdownWaitSeconds")
        self._CaseSensitive = params.get("CaseSensitive")
        self._IsWhiteSGs = params.get("IsWhiteSGs")
        self._BindSGs = params.get("BindSGs")
        self._EnableMultiZones = params.get("EnableMultiZones")
        self._UserNetworkInfos = params.get("UserNetworkInfos")
        self._EnableCoolDown = params.get("EnableCoolDown")
        self._CoolDownBucket = params.get("CoolDownBucket")
        if params.get("Details") is not None:
            self._Details = InstanceDetail()
            self._Details._deserialize(params.get("Details"))
        self._EnableDlc = params.get("EnableDlc")
        self._AccountType = params.get("AccountType")
        self._MonitorMode = params.get("MonitorMode")
        if params.get("CNSummary") is not None:
            self._CNSummary = NodesSummary()
            self._CNSummary._deserialize(params.get("CNSummary"))
        self._ComputeGroupCount = params.get("ComputeGroupCount")
        self._CosStorageSize = params.get("CosStorageSize")
        self._IsMasterNonVM = params.get("IsMasterNonVM")
        self._CosPkgCapacity = params.get("CosPkgCapacity")
        self._UseManagedBucket = params.get("UseManagedBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    r"""实例节点描述信息

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Spec: 机型，如 S1
        :type Spec: str
        :param _Core: cpu核数
        :type Core: int
        :param _Memory: 内存大小
        :type Memory: int
        :param _DiskType: 磁盘类型
        :type DiskType: str
        :param _DiskSize: 磁盘大小
        :type DiskSize: int
        :param _Role: 所属clickhouse cluster名称
        :type Role: str
        :param _Status: 状态
        :type Status: str
        :param _Rip: rip
        :type Rip: str
        :param _FeRole: FE节点角色
        :type FeRole: str
        :param _UUID: UUID
        :type UUID: str
        :param _Zone: 可用区
        :type Zone: str
        :param _VirtualZone: 虚拟可用区
        :type VirtualZone: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ComputeGroupId: 计算组ID
        :type ComputeGroupId: str
        """
        self._Ip = None
        self._Spec = None
        self._Core = None
        self._Memory = None
        self._DiskType = None
        self._DiskSize = None
        self._Role = None
        self._Status = None
        self._Rip = None
        self._FeRole = None
        self._UUID = None
        self._Zone = None
        self._VirtualZone = None
        self._CreateTime = None
        self._ComputeGroupId = None

    @property
    def Ip(self):
        r"""IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Spec(self):
        r"""机型，如 S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Core(self):
        r"""cpu核数
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        r"""内存大小
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskType(self):
        r"""磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""磁盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Role(self):
        r"""所属clickhouse cluster名称
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

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
    def Rip(self):
        r"""rip
        :rtype: str
        """
        return self._Rip

    @Rip.setter
    def Rip(self, Rip):
        self._Rip = Rip

    @property
    def FeRole(self):
        r"""FE节点角色
        :rtype: str
        """
        return self._FeRole

    @FeRole.setter
    def FeRole(self, FeRole):
        self._FeRole = FeRole

    @property
    def UUID(self):
        r"""UUID
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VirtualZone(self):
        r"""虚拟可用区
        :rtype: str
        """
        return self._VirtualZone

    @VirtualZone.setter
    def VirtualZone(self, VirtualZone):
        self._VirtualZone = VirtualZone

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
    def ComputeGroupId(self):
        r"""计算组ID
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Spec = params.get("Spec")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._Rip = params.get("Rip")
        self._FeRole = params.get("FeRole")
        self._UUID = params.get("UUID")
        self._Zone = params.get("Zone")
        self._VirtualZone = params.get("VirtualZone")
        self._CreateTime = params.get("CreateTime")
        self._ComputeGroupId = params.get("ComputeGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperation(AbstractModel):
    r"""集群操作描述

    """

    def __init__(self):
        r"""
        :param _Name: 操作名称，例如“create_instance"、“scaleout_instance”等
        :type Name: str
        :param _Result: 操作结果，“Success"表示成功，”Fail"表示失败
        :type Result: str
        :param _Desc: 操作名称描述，例如“创建”，“修改集群名称”等
        :type Desc: str
        :param _Level: 操作级别，例如“Critical", "Normal"等
        :type Level: str
        :param _LevelDesc: 操作级别描述，例如“高危”，“一般”等
        :type LevelDesc: str
        :param _StartTime: 操作开始时间
        :type StartTime: str
        :param _EndTime: 操作结束时间
        :type EndTime: str
        :param _ResultDesc: 操作结果描述，例如“成功”，“失败”
        :type ResultDesc: str
        :param _OperateUin: 操作用户ID
        :type OperateUin: str
        :param _JobId: 操作对应的jobid
        :type JobId: int
        :param _OperationDetail: 操作明细
        :type OperationDetail: str
        :param _ComputerGroupId: 计算组id
        :type ComputerGroupId: str
        """
        self._Name = None
        self._Result = None
        self._Desc = None
        self._Level = None
        self._LevelDesc = None
        self._StartTime = None
        self._EndTime = None
        self._ResultDesc = None
        self._OperateUin = None
        self._JobId = None
        self._OperationDetail = None
        self._ComputerGroupId = None

    @property
    def Name(self):
        r"""操作名称，例如“create_instance"、“scaleout_instance”等
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        r"""操作结果，“Success"表示成功，”Fail"表示失败
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Desc(self):
        r"""操作名称描述，例如“创建”，“修改集群名称”等
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Level(self):
        r"""操作级别，例如“Critical", "Normal"等
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def LevelDesc(self):
        r"""操作级别描述，例如“高危”，“一般”等
        :rtype: str
        """
        return self._LevelDesc

    @LevelDesc.setter
    def LevelDesc(self, LevelDesc):
        self._LevelDesc = LevelDesc

    @property
    def StartTime(self):
        r"""操作开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""操作结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ResultDesc(self):
        r"""操作结果描述，例如“成功”，“失败”
        :rtype: str
        """
        return self._ResultDesc

    @ResultDesc.setter
    def ResultDesc(self, ResultDesc):
        self._ResultDesc = ResultDesc

    @property
    def OperateUin(self):
        r"""操作用户ID
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def JobId(self):
        r"""操作对应的jobid
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def OperationDetail(self):
        r"""操作明细
        :rtype: str
        """
        return self._OperationDetail

    @OperationDetail.setter
    def OperationDetail(self, OperationDetail):
        self._OperationDetail = OperationDetail

    @property
    def ComputerGroupId(self):
        r"""计算组id
        :rtype: str
        """
        return self._ComputerGroupId

    @ComputerGroupId.setter
    def ComputerGroupId(self, ComputerGroupId):
        self._ComputerGroupId = ComputerGroupId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._Desc = params.get("Desc")
        self._Level = params.get("Level")
        self._LevelDesc = params.get("LevelDesc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ResultDesc = params.get("ResultDesc")
        self._OperateUin = params.get("OperateUin")
        self._JobId = params.get("JobId")
        self._OperationDetail = params.get("OperationDetail")
        self._ComputerGroupId = params.get("ComputerGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsRequest(AbstractModel):
    r"""ModifyClusterConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param _ModifyConfContext: 配置文件修改信息
        :type ModifyConfContext: list of ConfigSubmitContext
        :param _Remark: 修改原因
        :type Remark: str
        """
        self._InstanceId = None
        self._ModifyConfContext = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""集群ID，例如cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyConfContext(self):
        r"""配置文件修改信息
        :rtype: list of ConfigSubmitContext
        """
        return self._ModifyConfContext

    @ModifyConfContext.setter
    def ModifyConfContext(self, ModifyConfContext):
        self._ModifyConfContext = ModifyConfContext

    @property
    def Remark(self):
        r"""修改原因
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ModifyConfContext") is not None:
            self._ModifyConfContext = []
            for item in params.get("ModifyConfContext"):
                obj = ConfigSubmitContext()
                obj._deserialize(item)
                self._ModifyConfContext.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsResponse(AbstractModel):
    r"""ModifyClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程相关信息
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程相关信息
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyCoolDownPolicyRequest(AbstractModel):
    r"""ModifyCoolDownPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _CoolDownTtl: cooldown_ttl
        :type CoolDownTtl: str
        :param _CoolDownDatetime: cooldown_datetime
        :type CoolDownDatetime: str
        """
        self._InstanceId = None
        self._PolicyName = None
        self._CoolDownTtl = None
        self._CoolDownDatetime = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        r"""策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CoolDownTtl(self):
        r"""cooldown_ttl
        :rtype: str
        """
        return self._CoolDownTtl

    @CoolDownTtl.setter
    def CoolDownTtl(self, CoolDownTtl):
        self._CoolDownTtl = CoolDownTtl

    @property
    def CoolDownDatetime(self):
        r"""cooldown_datetime
        :rtype: str
        """
        return self._CoolDownDatetime

    @CoolDownDatetime.setter
    def CoolDownDatetime(self, CoolDownDatetime):
        self._CoolDownDatetime = CoolDownDatetime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._CoolDownTtl = params.get("CoolDownTtl")
        self._CoolDownDatetime = params.get("CoolDownDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCoolDownPolicyResponse(AbstractModel):
    r"""ModifyCoolDownPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyInstanceKeyValConfigsRequest(AbstractModel):
    r"""ModifyInstanceKeyValConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _AddItems: 新增配置列表
        :type AddItems: list of InstanceConfigItem
        :param _UpdateItems: 更新配置列表
        :type UpdateItems: list of InstanceConfigItem
        :param _DelItems: 删除配置列表
        :type DelItems: list of InstanceConfigItem
        :param _Message: 备注（50字以内）
        :type Message: str
        :param _HotUpdateItems: 热更新列表
        :type HotUpdateItems: list of InstanceConfigItem
        :param _DeleteItems: 删除配置列表
        :type DeleteItems: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceConfigItem`
        :param _IPAddress: ip地址
        :type IPAddress: str
        """
        self._InstanceId = None
        self._FileName = None
        self._AddItems = None
        self._UpdateItems = None
        self._DelItems = None
        self._Message = None
        self._HotUpdateItems = None
        self._DeleteItems = None
        self._IPAddress = None

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
    def FileName(self):
        r"""文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AddItems(self):
        r"""新增配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._AddItems

    @AddItems.setter
    def AddItems(self, AddItems):
        self._AddItems = AddItems

    @property
    def UpdateItems(self):
        r"""更新配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._UpdateItems

    @UpdateItems.setter
    def UpdateItems(self, UpdateItems):
        self._UpdateItems = UpdateItems

    @property
    def DelItems(self):
        r"""删除配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._DelItems

    @DelItems.setter
    def DelItems(self, DelItems):
        self._DelItems = DelItems

    @property
    def Message(self):
        r"""备注（50字以内）
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def HotUpdateItems(self):
        r"""热更新列表
        :rtype: list of InstanceConfigItem
        """
        return self._HotUpdateItems

    @HotUpdateItems.setter
    def HotUpdateItems(self, HotUpdateItems):
        self._HotUpdateItems = HotUpdateItems

    @property
    def DeleteItems(self):
        r"""删除配置列表
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceConfigItem`
        """
        return self._DeleteItems

    @DeleteItems.setter
    def DeleteItems(self, DeleteItems):
        self._DeleteItems = DeleteItems

    @property
    def IPAddress(self):
        r"""ip地址
        :rtype: str
        """
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileName = params.get("FileName")
        if params.get("AddItems") is not None:
            self._AddItems = []
            for item in params.get("AddItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._AddItems.append(obj)
        if params.get("UpdateItems") is not None:
            self._UpdateItems = []
            for item in params.get("UpdateItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._UpdateItems.append(obj)
        if params.get("DelItems") is not None:
            self._DelItems = []
            for item in params.get("DelItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._DelItems.append(obj)
        self._Message = params.get("Message")
        if params.get("HotUpdateItems") is not None:
            self._HotUpdateItems = []
            for item in params.get("HotUpdateItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._HotUpdateItems.append(obj)
        if params.get("DeleteItems") is not None:
            self._DeleteItems = InstanceConfigItem()
            self._DeleteItems._deserialize(params.get("DeleteItems"))
        self._IPAddress = params.get("IPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceKeyValConfigsResponse(AbstractModel):
    r"""ModifyInstanceKeyValConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _FlowId: ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._FlowId = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def FlowId(self):
        r"""ID
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
        self._ErrorMsg = params.get("ErrorMsg")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    r"""ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _InstanceName: 新修改的实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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
    def InstanceName(self):
        r"""新修改的实例名称
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
        


class ModifyInstanceResponse(AbstractModel):
    r"""ModifyInstance返回参数结构体

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


class ModifyNodeStatusRequest(AbstractModel):
    r"""ModifyNodeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param _NodeInfos: 节点信息
        :type NodeInfos: list of NodeInfos
        :param _OperationCode: 节点操作
        :type OperationCode: str
        :param _RestartTimeOut: 超时时间（秒）
        :type RestartTimeOut: str
        """
        self._InstanceId = None
        self._NodeInfos = None
        self._OperationCode = None
        self._RestartTimeOut = None

    @property
    def InstanceId(self):
        r"""集群ID，例如cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeInfos(self):
        r"""节点信息
        :rtype: list of NodeInfos
        """
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def OperationCode(self):
        r"""节点操作
        :rtype: str
        """
        return self._OperationCode

    @OperationCode.setter
    def OperationCode(self, OperationCode):
        self._OperationCode = OperationCode

    @property
    def RestartTimeOut(self):
        r"""超时时间（秒）
        :rtype: str
        """
        return self._RestartTimeOut

    @RestartTimeOut.setter
    def RestartTimeOut(self, RestartTimeOut):
        self._RestartTimeOut = RestartTimeOut


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfos()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._OperationCode = params.get("OperationCode")
        self._RestartTimeOut = params.get("RestartTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodeStatusResponse(AbstractModel):
    r"""ModifyNodeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程相关信息
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程相关信息
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupsRequest(AbstractModel):
    r"""ModifySecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _OldSecurityGroupIds: 修改前的安全组信息
        :type OldSecurityGroupIds: list of str
        :param _ModifySecurityGroupIds: 修改后的安全组信息
        :type ModifySecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._OldSecurityGroupIds = None
        self._ModifySecurityGroupIds = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldSecurityGroupIds(self):
        r"""修改前的安全组信息
        :rtype: list of str
        """
        return self._OldSecurityGroupIds

    @OldSecurityGroupIds.setter
    def OldSecurityGroupIds(self, OldSecurityGroupIds):
        self._OldSecurityGroupIds = OldSecurityGroupIds

    @property
    def ModifySecurityGroupIds(self):
        r"""修改后的安全组信息
        :rtype: list of str
        """
        return self._ModifySecurityGroupIds

    @ModifySecurityGroupIds.setter
    def ModifySecurityGroupIds(self, ModifySecurityGroupIds):
        self._ModifySecurityGroupIds = ModifySecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldSecurityGroupIds = params.get("OldSecurityGroupIds")
        self._ModifySecurityGroupIds = params.get("ModifySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupsResponse(AbstractModel):
    r"""ModifySecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyUserBindWorkloadGroupRequest(AbstractModel):
    r"""ModifyUserBindWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BindUsers: 需要绑定资源组的用户信息，如果一个账户拥有多个主机信息，需要将这些信息都传入
        :type BindUsers: list of BindUser
        :param _OldWorkloadGroupName: 修改前绑定的资源组名称
        :type OldWorkloadGroupName: str
        :param _NewWorkloadGroupName: 修改后绑定的资源组名称
        :type NewWorkloadGroupName: str
        """
        self._InstanceId = None
        self._BindUsers = None
        self._OldWorkloadGroupName = None
        self._NewWorkloadGroupName = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BindUsers(self):
        r"""需要绑定资源组的用户信息，如果一个账户拥有多个主机信息，需要将这些信息都传入
        :rtype: list of BindUser
        """
        return self._BindUsers

    @BindUsers.setter
    def BindUsers(self, BindUsers):
        self._BindUsers = BindUsers

    @property
    def OldWorkloadGroupName(self):
        r"""修改前绑定的资源组名称
        :rtype: str
        """
        return self._OldWorkloadGroupName

    @OldWorkloadGroupName.setter
    def OldWorkloadGroupName(self, OldWorkloadGroupName):
        self._OldWorkloadGroupName = OldWorkloadGroupName

    @property
    def NewWorkloadGroupName(self):
        r"""修改后绑定的资源组名称
        :rtype: str
        """
        return self._NewWorkloadGroupName

    @NewWorkloadGroupName.setter
    def NewWorkloadGroupName(self, NewWorkloadGroupName):
        self._NewWorkloadGroupName = NewWorkloadGroupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("BindUsers") is not None:
            self._BindUsers = []
            for item in params.get("BindUsers"):
                obj = BindUser()
                obj._deserialize(item)
                self._BindUsers.append(obj)
        self._OldWorkloadGroupName = params.get("OldWorkloadGroupName")
        self._NewWorkloadGroupName = params.get("NewWorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserBindWorkloadGroupResponse(AbstractModel):
    r"""ModifyUserBindWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyUserPrivilegesV3Request(AbstractModel):
    r"""ModifyUserPrivilegesV3请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _UserPrivileges: 用户权限
        :type UserPrivileges: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateUserPrivileges`
        :param _WhiteHost: 用户链接来自的 IP	
        :type WhiteHost: str
        :param _UpdateType: 更新类型，默认0，1为更新绑定计算组，2为更新默认计算组
        :type UpdateType: int
        :param _UpdateComputeGroups: 需绑定计算组列表
        :type UpdateComputeGroups: list of str
        :param _DefaultComputeGroup: 默认计算组
        :type DefaultComputeGroup: str
        :param _ComputeGroupType: 0: 灵活场景 1: 固定场景
        :type ComputeGroupType: int
        """
        self._InstanceId = None
        self._UserName = None
        self._UserPrivileges = None
        self._WhiteHost = None
        self._UpdateType = None
        self._UpdateComputeGroups = None
        self._DefaultComputeGroup = None
        self._ComputeGroupType = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def UserPrivileges(self):
        r"""用户权限
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateUserPrivileges`
        """
        return self._UserPrivileges

    @UserPrivileges.setter
    def UserPrivileges(self, UserPrivileges):
        self._UserPrivileges = UserPrivileges

    @property
    def WhiteHost(self):
        r"""用户链接来自的 IP	
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost

    @property
    def UpdateType(self):
        r"""更新类型，默认0，1为更新绑定计算组，2为更新默认计算组
        :rtype: int
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def UpdateComputeGroups(self):
        r"""需绑定计算组列表
        :rtype: list of str
        """
        return self._UpdateComputeGroups

    @UpdateComputeGroups.setter
    def UpdateComputeGroups(self, UpdateComputeGroups):
        self._UpdateComputeGroups = UpdateComputeGroups

    @property
    def DefaultComputeGroup(self):
        r"""默认计算组
        :rtype: str
        """
        return self._DefaultComputeGroup

    @DefaultComputeGroup.setter
    def DefaultComputeGroup(self, DefaultComputeGroup):
        self._DefaultComputeGroup = DefaultComputeGroup

    @property
    def ComputeGroupType(self):
        r"""0: 灵活场景 1: 固定场景
        :rtype: int
        """
        return self._ComputeGroupType

    @ComputeGroupType.setter
    def ComputeGroupType(self, ComputeGroupType):
        self._ComputeGroupType = ComputeGroupType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        if params.get("UserPrivileges") is not None:
            self._UserPrivileges = UpdateUserPrivileges()
            self._UserPrivileges._deserialize(params.get("UserPrivileges"))
        self._WhiteHost = params.get("WhiteHost")
        self._UpdateType = params.get("UpdateType")
        self._UpdateComputeGroups = params.get("UpdateComputeGroups")
        self._DefaultComputeGroup = params.get("DefaultComputeGroup")
        self._ComputeGroupType = params.get("ComputeGroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPrivilegesV3Response(AbstractModel):
    r"""ModifyUserPrivilegesV3返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息，为空就是没有错误
        :type ErrorMsg: str
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息，为空就是没有错误
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyWorkloadGroupRequest(AbstractModel):
    r"""ModifyWorkloadGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _WorkloadGroup: 修改的资源组信息
        :type WorkloadGroup: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        self._InstanceId = None
        self._WorkloadGroup = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroup(self):
        r"""修改的资源组信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        return self._WorkloadGroup

    @WorkloadGroup.setter
    def WorkloadGroup(self, WorkloadGroup):
        self._WorkloadGroup = WorkloadGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WorkloadGroup") is not None:
            self._WorkloadGroup = WorkloadGroupConfig()
            self._WorkloadGroup._deserialize(params.get("WorkloadGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkloadGroupResponse(AbstractModel):
    r"""ModifyWorkloadGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息	
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息	
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyWorkloadGroupStatusRequest(AbstractModel):
    r"""ModifyWorkloadGroupStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _OperationType: 是否开启资源组：open-开启、close-关闭
        :type OperationType: str
        """
        self._InstanceId = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OperationType(self):
        r"""是否开启资源组：open-开启、close-关闭
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkloadGroupStatusResponse(AbstractModel):
    r"""ModifyWorkloadGroupStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息	
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息	
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class NetworkInfo(AbstractModel):
    r"""网络信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _SubnetIpNum: 当前子网可用ip数
        :type SubnetIpNum: int
        """
        self._Zone = None
        self._SubnetId = None
        self._SubnetIpNum = None

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        r"""子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetIpNum(self):
        r"""当前子网可用ip数
        :rtype: int
        """
        return self._SubnetIpNum

    @SubnetIpNum.setter
    def SubnetIpNum(self, SubnetIpNum):
        self._SubnetIpNum = SubnetIpNum


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._SubnetIpNum = params.get("SubnetIpNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    r"""NodeInfo

    """

    def __init__(self):
        r"""
        :param _Ip: 用户IP
        :type Ip: str
        :param _Status: 节点状态
        :type Status: int
        :param _NodeName: 节点角色名
        :type NodeName: str
        :param _ComponentName: 组件名
        :type ComponentName: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        :param _LastRestartTime: 节点上次重启的时间
        :type LastRestartTime: str
        :param _Zone: 节点所在可用区
        :type Zone: str
        :param _Id: Id
        :type Id: str
        :param _RIp: RIP
        :type RIp: str
        :param _ComputeGroupId: 计算组ID
        :type ComputeGroupId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VirtualZone: 虚拟可用区
        :type VirtualZone: str
        """
        self._Ip = None
        self._Status = None
        self._NodeName = None
        self._ComponentName = None
        self._NodeRole = None
        self._LastRestartTime = None
        self._Zone = None
        self._Id = None
        self._RIp = None
        self._ComputeGroupId = None
        self._CreateTime = None
        self._VirtualZone = None

    @property
    def Ip(self):
        r"""用户IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        r"""节点状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeName(self):
        r"""节点角色名
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ComponentName(self):
        r"""组件名
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def NodeRole(self):
        r"""节点角色
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def LastRestartTime(self):
        r"""节点上次重启的时间
        :rtype: str
        """
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime

    @property
    def Zone(self):
        r"""节点所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Id(self):
        r"""Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RIp(self):
        r"""RIP
        :rtype: str
        """
        return self._RIp

    @RIp.setter
    def RIp(self, RIp):
        self._RIp = RIp

    @property
    def ComputeGroupId(self):
        r"""计算组ID
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId

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
    def VirtualZone(self):
        r"""虚拟可用区
        :rtype: str
        """
        return self._VirtualZone

    @VirtualZone.setter
    def VirtualZone(self, VirtualZone):
        self._VirtualZone = VirtualZone


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._NodeName = params.get("NodeName")
        self._ComponentName = params.get("ComponentName")
        self._NodeRole = params.get("NodeRole")
        self._LastRestartTime = params.get("LastRestartTime")
        self._Zone = params.get("Zone")
        self._Id = params.get("Id")
        self._RIp = params.get("RIp")
        self._ComputeGroupId = params.get("ComputeGroupId")
        self._CreateTime = params.get("CreateTime")
        self._VirtualZone = params.get("VirtualZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfos(AbstractModel):
    r"""节点信息列表

    """

    def __init__(self):
        r"""
        :param _NodeName: 节点名称
        :type NodeName: str
        :param _Status: 节点状态
        :type Status: int
        :param _Ip: 节点ip
        :type Ip: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        :param _ComponentName: 组件名
        :type ComponentName: str
        :param _LastRestartTime: 上一次重启时间
        :type LastRestartTime: str
        :param _Id: id
        :type Id: str
        :param _Zone: 可用区
        :type Zone: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ComputeGroupId: 计算组id
        :type ComputeGroupId: str
        :param _RIp: rip
        :type RIp: str
        :param _VirtualZone: 虚拟可用区
        :type VirtualZone: str
        """
        self._NodeName = None
        self._Status = None
        self._Ip = None
        self._NodeRole = None
        self._ComponentName = None
        self._LastRestartTime = None
        self._Id = None
        self._Zone = None
        self._CreateTime = None
        self._ComputeGroupId = None
        self._RIp = None
        self._VirtualZone = None

    @property
    def NodeName(self):
        r"""节点名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Status(self):
        r"""节点状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ip(self):
        r"""节点ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def NodeRole(self):
        r"""节点角色
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ComponentName(self):
        r"""组件名
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def LastRestartTime(self):
        r"""上一次重启时间
        :rtype: str
        """
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime

    @property
    def Id(self):
        r"""id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def ComputeGroupId(self):
        r"""计算组id
        :rtype: str
        """
        return self._ComputeGroupId

    @ComputeGroupId.setter
    def ComputeGroupId(self, ComputeGroupId):
        self._ComputeGroupId = ComputeGroupId

    @property
    def RIp(self):
        r"""rip
        :rtype: str
        """
        return self._RIp

    @RIp.setter
    def RIp(self, RIp):
        self._RIp = RIp

    @property
    def VirtualZone(self):
        r"""虚拟可用区
        :rtype: str
        """
        return self._VirtualZone

    @VirtualZone.setter
    def VirtualZone(self, VirtualZone):
        self._VirtualZone = VirtualZone


    def _deserialize(self, params):
        self._NodeName = params.get("NodeName")
        self._Status = params.get("Status")
        self._Ip = params.get("Ip")
        self._NodeRole = params.get("NodeRole")
        self._ComponentName = params.get("ComponentName")
        self._LastRestartTime = params.get("LastRestartTime")
        self._Id = params.get("Id")
        self._Zone = params.get("Zone")
        self._CreateTime = params.get("CreateTime")
        self._ComputeGroupId = params.get("ComputeGroupId")
        self._RIp = params.get("RIp")
        self._VirtualZone = params.get("VirtualZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodesSummary(AbstractModel):
    r"""节点角色描述信息

    """

    def __init__(self):
        r"""
        :param _Spec: 机型，如 S1
        :type Spec: str
        :param _NodeSize: 节点数目
        :type NodeSize: int
        :param _Core: cpu核数，单位个
        :type Core: int
        :param _Memory: 内存大小，单位G
        :type Memory: int
        :param _Disk: 磁盘大小，单位G
        :type Disk: int
        :param _DiskType: 磁盘类型
        :type DiskType: str
        :param _DiskDesc: 磁盘描述
        :type DiskDesc: str
        :param _AttachCBSSpec: 挂载云盘信息
        :type AttachCBSSpec: :class:`tencentcloud.cdwdoris.v20211228.models.AttachCBSSpec`
        :param _SubProductType: 子产品名称
        :type SubProductType: str
        :param _SpecCore: 规格核数
        :type SpecCore: int
        :param _SpecMemory: 规格内存
        :type SpecMemory: int
        :param _DiskCount: 磁盘大小
        :type DiskCount: int
        :param _Encrypt: 是否加密
        :type Encrypt: int
        :param _MaxDiskSize: 最大磁盘
        :type MaxDiskSize: int
        """
        self._Spec = None
        self._NodeSize = None
        self._Core = None
        self._Memory = None
        self._Disk = None
        self._DiskType = None
        self._DiskDesc = None
        self._AttachCBSSpec = None
        self._SubProductType = None
        self._SpecCore = None
        self._SpecMemory = None
        self._DiskCount = None
        self._Encrypt = None
        self._MaxDiskSize = None

    @property
    def Spec(self):
        r"""机型，如 S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def NodeSize(self):
        r"""节点数目
        :rtype: int
        """
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize

    @property
    def Core(self):
        r"""cpu核数，单位个
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        r"""内存大小，单位G
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        r"""磁盘大小，单位G
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def DiskType(self):
        r"""磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        r"""磁盘描述
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def AttachCBSSpec(self):
        r"""挂载云盘信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.AttachCBSSpec`
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def SubProductType(self):
        r"""子产品名称
        :rtype: str
        """
        return self._SubProductType

    @SubProductType.setter
    def SubProductType(self, SubProductType):
        self._SubProductType = SubProductType

    @property
    def SpecCore(self):
        r"""规格核数
        :rtype: int
        """
        return self._SpecCore

    @SpecCore.setter
    def SpecCore(self, SpecCore):
        self._SpecCore = SpecCore

    @property
    def SpecMemory(self):
        r"""规格内存
        :rtype: int
        """
        return self._SpecMemory

    @SpecMemory.setter
    def SpecMemory(self, SpecMemory):
        self._SpecMemory = SpecMemory

    @property
    def DiskCount(self):
        r"""磁盘大小
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def Encrypt(self):
        r"""是否加密
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def MaxDiskSize(self):
        r"""最大磁盘
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._NodeSize = params.get("NodeSize")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = AttachCBSSpec()
            self._AttachCBSSpec._deserialize(params.get("AttachCBSSpec"))
        self._SubProductType = params.get("SubProductType")
        self._SpecCore = params.get("SpecCore")
        self._SpecMemory = params.get("SpecMemory")
        self._DiskCount = params.get("DiskCount")
        self._Encrypt = params.get("Encrypt")
        self._MaxDiskSize = params.get("MaxDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenCoolDownPolicyRequest(AbstractModel):
    r"""OpenCoolDownPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _DatabaseName: db名称
        :type DatabaseName: str
        :param _TableName: table名称
        :type TableName: str
        :param _OperationType: 操作类型
        :type OperationType: str
        :param _BatchOpenCoolDownTables: 逗号分隔 需要带上db的名字 db1.tb1,db1.tb2,db2.tb1
        :type BatchOpenCoolDownTables: str
        :param _PolicyName: 绑定的时候用 策略名称
        :type PolicyName: str
        :param _BatchOpenCoolDownPartitions: 逗号分隔 p1,p2,p3
        :type BatchOpenCoolDownPartitions: str
        """
        self._InstanceId = None
        self._DatabaseName = None
        self._TableName = None
        self._OperationType = None
        self._BatchOpenCoolDownTables = None
        self._PolicyName = None
        self._BatchOpenCoolDownPartitions = None

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
    def DatabaseName(self):
        r"""db名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""table名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def OperationType(self):
        r"""操作类型
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def BatchOpenCoolDownTables(self):
        r"""逗号分隔 需要带上db的名字 db1.tb1,db1.tb2,db2.tb1
        :rtype: str
        """
        return self._BatchOpenCoolDownTables

    @BatchOpenCoolDownTables.setter
    def BatchOpenCoolDownTables(self, BatchOpenCoolDownTables):
        self._BatchOpenCoolDownTables = BatchOpenCoolDownTables

    @property
    def PolicyName(self):
        r"""绑定的时候用 策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def BatchOpenCoolDownPartitions(self):
        r"""逗号分隔 p1,p2,p3
        :rtype: str
        """
        return self._BatchOpenCoolDownPartitions

    @BatchOpenCoolDownPartitions.setter
    def BatchOpenCoolDownPartitions(self, BatchOpenCoolDownPartitions):
        self._BatchOpenCoolDownPartitions = BatchOpenCoolDownPartitions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._OperationType = params.get("OperationType")
        self._BatchOpenCoolDownTables = params.get("BatchOpenCoolDownTables")
        self._PolicyName = params.get("PolicyName")
        self._BatchOpenCoolDownPartitions = params.get("BatchOpenCoolDownPartitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenCoolDownPolicyResponse(AbstractModel):
    r"""OpenCoolDownPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _QueryDocument: 返回信息
        :type QueryDocument: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._QueryDocument = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def QueryDocument(self):
        r"""返回信息
        :rtype: str
        """
        return self._QueryDocument

    @QueryDocument.setter
    def QueryDocument(self, QueryDocument):
        self._QueryDocument = QueryDocument

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._QueryDocument = params.get("QueryDocument")
        self._RequestId = params.get("RequestId")


class OpenCoolDownRequest(AbstractModel):
    r"""OpenCoolDown请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群id
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
        


class OpenCoolDownResponse(AbstractModel):
    r"""OpenCoolDown返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RecoverBackUpJobRequest(AbstractModel):
    r"""RecoverBackUpJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        :param _ReplicationNum: 恢复出来的新表副本数
        :type ReplicationNum: int
        :param _ReserveSourceConfig: 恢复是否保持源表中的配置，1时表示保留源表中的配置
        :type ReserveSourceConfig: int
        :param _RecoverType: 0默认 1cos恢复
        :type RecoverType: int
        :param _CosSourceInfo: CosSourceInfo对象
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        :param _ScheduleType: 0默认 1定期执行
        :type ScheduleType: int
        :param _NextTime: 年-月-日 时:分:秒
        :type NextTime: str
        :param _ScheduleName: 调度名称
        :type ScheduleName: str
        :param _OperationType: create update
        :type OperationType: str
        :param _RecoverScope: 恢复粒度：All全量、Database按库、Table按表
        :type RecoverScope: str
        :param _RecoverDatabase: 恢复库：如果是按库备份，则需要该字段，库之间用","分割
        :type RecoverDatabase: str
        :param _ReserveStoragePolicy: 1:恢复后，不保留降冷策略，数据变为热数据；
2:恢复后，沿用备份表的降冷策略；
0:默认值，该版本没有这个配置（2.1版本2.1.8之前；2.0版本2.0.16之前）
        :type ReserveStoragePolicy: int
        """
        self._InstanceId = None
        self._BackUpJobId = None
        self._ReplicationNum = None
        self._ReserveSourceConfig = None
        self._RecoverType = None
        self._CosSourceInfo = None
        self._ScheduleType = None
        self._NextTime = None
        self._ScheduleName = None
        self._OperationType = None
        self._RecoverScope = None
        self._RecoverDatabase = None
        self._ReserveStoragePolicy = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        r"""任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId

    @property
    def ReplicationNum(self):
        r"""恢复出来的新表副本数
        :rtype: int
        """
        return self._ReplicationNum

    @ReplicationNum.setter
    def ReplicationNum(self, ReplicationNum):
        self._ReplicationNum = ReplicationNum

    @property
    def ReserveSourceConfig(self):
        r"""恢复是否保持源表中的配置，1时表示保留源表中的配置
        :rtype: int
        """
        return self._ReserveSourceConfig

    @ReserveSourceConfig.setter
    def ReserveSourceConfig(self, ReserveSourceConfig):
        self._ReserveSourceConfig = ReserveSourceConfig

    @property
    def RecoverType(self):
        warnings.warn("parameter `RecoverType` is deprecated", DeprecationWarning) 

        r"""0默认 1cos恢复
        :rtype: int
        """
        return self._RecoverType

    @RecoverType.setter
    def RecoverType(self, RecoverType):
        warnings.warn("parameter `RecoverType` is deprecated", DeprecationWarning) 

        self._RecoverType = RecoverType

    @property
    def CosSourceInfo(self):
        warnings.warn("parameter `CosSourceInfo` is deprecated", DeprecationWarning) 

        r"""CosSourceInfo对象
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        warnings.warn("parameter `CosSourceInfo` is deprecated", DeprecationWarning) 

        self._CosSourceInfo = CosSourceInfo

    @property
    def ScheduleType(self):
        warnings.warn("parameter `ScheduleType` is deprecated", DeprecationWarning) 

        r"""0默认 1定期执行
        :rtype: int
        """
        return self._ScheduleType

    @ScheduleType.setter
    def ScheduleType(self, ScheduleType):
        warnings.warn("parameter `ScheduleType` is deprecated", DeprecationWarning) 

        self._ScheduleType = ScheduleType

    @property
    def NextTime(self):
        warnings.warn("parameter `NextTime` is deprecated", DeprecationWarning) 

        r"""年-月-日 时:分:秒
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        warnings.warn("parameter `NextTime` is deprecated", DeprecationWarning) 

        self._NextTime = NextTime

    @property
    def ScheduleName(self):
        warnings.warn("parameter `ScheduleName` is deprecated", DeprecationWarning) 

        r"""调度名称
        :rtype: str
        """
        return self._ScheduleName

    @ScheduleName.setter
    def ScheduleName(self, ScheduleName):
        warnings.warn("parameter `ScheduleName` is deprecated", DeprecationWarning) 

        self._ScheduleName = ScheduleName

    @property
    def OperationType(self):
        warnings.warn("parameter `OperationType` is deprecated", DeprecationWarning) 

        r"""create update
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        warnings.warn("parameter `OperationType` is deprecated", DeprecationWarning) 

        self._OperationType = OperationType

    @property
    def RecoverScope(self):
        r"""恢复粒度：All全量、Database按库、Table按表
        :rtype: str
        """
        return self._RecoverScope

    @RecoverScope.setter
    def RecoverScope(self, RecoverScope):
        self._RecoverScope = RecoverScope

    @property
    def RecoverDatabase(self):
        r"""恢复库：如果是按库备份，则需要该字段，库之间用","分割
        :rtype: str
        """
        return self._RecoverDatabase

    @RecoverDatabase.setter
    def RecoverDatabase(self, RecoverDatabase):
        self._RecoverDatabase = RecoverDatabase

    @property
    def ReserveStoragePolicy(self):
        r"""1:恢复后，不保留降冷策略，数据变为热数据；
2:恢复后，沿用备份表的降冷策略；
0:默认值，该版本没有这个配置（2.1版本2.1.8之前；2.0版本2.0.16之前）
        :rtype: int
        """
        return self._ReserveStoragePolicy

    @ReserveStoragePolicy.setter
    def ReserveStoragePolicy(self, ReserveStoragePolicy):
        self._ReserveStoragePolicy = ReserveStoragePolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        self._ReplicationNum = params.get("ReplicationNum")
        self._ReserveSourceConfig = params.get("ReserveSourceConfig")
        self._RecoverType = params.get("RecoverType")
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        self._ScheduleType = params.get("ScheduleType")
        self._NextTime = params.get("NextTime")
        self._ScheduleName = params.get("ScheduleName")
        self._OperationType = params.get("OperationType")
        self._RecoverScope = params.get("RecoverScope")
        self._RecoverDatabase = params.get("RecoverDatabase")
        self._ReserveStoragePolicy = params.get("ReserveStoragePolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverBackUpJobResponse(AbstractModel):
    r"""RecoverBackUpJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 恢复任务总数量
        :type TotalCount: int
        :param _DuplicateTables: 重复的表名
        :type DuplicateTables: list of str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DuplicateTables = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""恢复任务总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DuplicateTables(self):
        r"""重复的表名
        :rtype: list of str
        """
        return self._DuplicateTables

    @DuplicateTables.setter
    def DuplicateTables(self, DuplicateTables):
        self._DuplicateTables = DuplicateTables

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._DuplicateTables = params.get("DuplicateTables")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ReduceInstanceRequest(AbstractModel):
    r"""ReduceInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _DelHosts: 节点列表
        :type DelHosts: list of str
        :param _Type: 角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :type Type: str
        :param _HaType: 缩容后集群高可用类型：0：非高可用，1：读高可用，2：读写高可用。
        :type HaType: int
        :param _CheckAuth: 前端鉴权使用
        :type CheckAuth: bool
        """
        self._InstanceId = None
        self._DelHosts = None
        self._Type = None
        self._HaType = None
        self._CheckAuth = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DelHosts(self):
        r"""节点列表
        :rtype: list of str
        """
        return self._DelHosts

    @DelHosts.setter
    def DelHosts(self, DelHosts):
        self._DelHosts = DelHosts

    @property
    def Type(self):
        r"""角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HaType(self):
        r"""缩容后集群高可用类型：0：非高可用，1：读高可用，2：读写高可用。
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def CheckAuth(self):
        r"""前端鉴权使用
        :rtype: bool
        """
        return self._CheckAuth

    @CheckAuth.setter
    def CheckAuth(self, CheckAuth):
        self._CheckAuth = CheckAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DelHosts = params.get("DelHosts")
        self._Type = params.get("Type")
        self._HaType = params.get("HaType")
        self._CheckAuth = params.get("CheckAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReduceInstanceResponse(AbstractModel):
    r"""ReduceInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RegionAreaInfo(AbstractModel):
    r"""可用区的地域大类描述

    """

    def __init__(self):
        r"""
        :param _Name: 大类地域信息，如"south_china", "east_china"等
        :type Name: str
        :param _Desc: 对应Name的描述，例如“华南地区”，“华东地区”等
        :type Desc: str
        :param _Regions: 具体地域列表1
        :type Regions: list of RegionInfo
        """
        self._Name = None
        self._Desc = None
        self._Regions = None

    @property
    def Name(self):
        r"""大类地域信息，如"south_china", "east_china"等
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""对应Name的描述，例如“华南地区”，“华东地区”等
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Regions(self):
        r"""具体地域列表1
        :rtype: list of RegionInfo
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    r"""地域描述信息

    """

    def __init__(self):
        r"""
        :param _Name: 地域名称，例如“ap-guangzhou"
        :type Name: str
        :param _Desc: 地域描述，例如"广州”
        :type Desc: str
        :param _RegionId: 地域唯一标记
        :type RegionId: int
        :param _Zones: 地域下所有可用区列表
        :type Zones: list of ZoneInfo
        :param _Count: 该地域下集群数目
        :type Count: int
        :param _IsInternationalSite: 0代表是国际站 1代表不是
        :type IsInternationalSite: int
        :param _Bucket: 桶
        :type Bucket: str
        :param _SSCCount: 存算分离集群数
        :type SSCCount: int
        :param _EnableSSC: 是否开通存算分离
        :type EnableSSC: bool
        """
        self._Name = None
        self._Desc = None
        self._RegionId = None
        self._Zones = None
        self._Count = None
        self._IsInternationalSite = None
        self._Bucket = None
        self._SSCCount = None
        self._EnableSSC = None

    @property
    def Name(self):
        r"""地域名称，例如“ap-guangzhou"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""地域描述，例如"广州”
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RegionId(self):
        r"""地域唯一标记
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zones(self):
        r"""地域下所有可用区列表
        :rtype: list of ZoneInfo
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Count(self):
        r"""该地域下集群数目
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def IsInternationalSite(self):
        r"""0代表是国际站 1代表不是
        :rtype: int
        """
        return self._IsInternationalSite

    @IsInternationalSite.setter
    def IsInternationalSite(self, IsInternationalSite):
        self._IsInternationalSite = IsInternationalSite

    @property
    def Bucket(self):
        r"""桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def SSCCount(self):
        r"""存算分离集群数
        :rtype: int
        """
        return self._SSCCount

    @SSCCount.setter
    def SSCCount(self, SSCCount):
        self._SSCCount = SSCCount

    @property
    def EnableSSC(self):
        r"""是否开通存算分离
        :rtype: bool
        """
        return self._EnableSSC

    @EnableSSC.setter
    def EnableSSC(self, EnableSSC):
        self._EnableSSC = EnableSSC


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._Count = params.get("Count")
        self._IsInternationalSite = params.get("IsInternationalSite")
        self._Bucket = params.get("Bucket")
        self._SSCCount = params.get("SSCCount")
        self._EnableSSC = params.get("EnableSSC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskRequest(AbstractModel):
    r"""ResizeDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Type: 角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :type Type: str
        :param _DiskSize: 云盘大小
        :type DiskSize: int
        """
        self._InstanceId = None
        self._Type = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskSize(self):
        r"""云盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    r"""ResizeDisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

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
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ResourceSpec(AbstractModel):
    r"""资源规格描述信息

    """

    def __init__(self):
        r"""
        :param _Name: 规格名称，例如“SCH1"
        :type Name: str
        :param _Cpu: cpu核数
        :type Cpu: int
        :param _Mem: 内存大小，单位G
        :type Mem: int
        :param _Type: 分类标记，STANDARD/BIGDATA/HIGHIO分别表示标准型/大数据型/高IO
        :type Type: str
        :param _SystemDisk: 系统盘描述信息
        :type SystemDisk: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        :param _DataDisk: 数据盘描述信息
        :type DataDisk: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        :param _MaxNodeSize: 最大节点数目限制
        :type MaxNodeSize: int
        :param _Available: 是否可用，false代表售罄
        :type Available: bool
        :param _ComputeSpecDesc: 规格描述信息
        :type ComputeSpecDesc: str
        :param _InstanceQuota: cvm库存
        :type InstanceQuota: int
        """
        self._Name = None
        self._Cpu = None
        self._Mem = None
        self._Type = None
        self._SystemDisk = None
        self._DataDisk = None
        self._MaxNodeSize = None
        self._Available = None
        self._ComputeSpecDesc = None
        self._InstanceQuota = None

    @property
    def Name(self):
        r"""规格名称，例如“SCH1"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cpu(self):
        r"""cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""内存大小，单位G
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Type(self):
        r"""分类标记，STANDARD/BIGDATA/HIGHIO分别表示标准型/大数据型/高IO
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SystemDisk(self):
        r"""系统盘描述信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisk(self):
        r"""数据盘描述信息
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def MaxNodeSize(self):
        r"""最大节点数目限制
        :rtype: int
        """
        return self._MaxNodeSize

    @MaxNodeSize.setter
    def MaxNodeSize(self, MaxNodeSize):
        self._MaxNodeSize = MaxNodeSize

    @property
    def Available(self):
        r"""是否可用，false代表售罄
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def ComputeSpecDesc(self):
        r"""规格描述信息
        :rtype: str
        """
        return self._ComputeSpecDesc

    @ComputeSpecDesc.setter
    def ComputeSpecDesc(self, ComputeSpecDesc):
        self._ComputeSpecDesc = ComputeSpecDesc

    @property
    def InstanceQuota(self):
        r"""cvm库存
        :rtype: int
        """
        return self._InstanceQuota

    @InstanceQuota.setter
    def InstanceQuota(self, InstanceQuota):
        self._InstanceQuota = InstanceQuota


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Type = params.get("Type")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = DiskSpec()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisk") is not None:
            self._DataDisk = DiskSpec()
            self._DataDisk._deserialize(params.get("DataDisk"))
        self._MaxNodeSize = params.get("MaxNodeSize")
        self._Available = params.get("Available")
        self._ComputeSpecDesc = params.get("ComputeSpecDesc")
        self._InstanceQuota = params.get("InstanceQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForConfigsRequest(AbstractModel):
    r"""RestartClusterForConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param _ConfigName: 配置文件名称
        :type ConfigName: str
        :param _OperationType: grace_restart为优雅滚动重启 不填默认立刻重启
        :type OperationType: str
        """
        self._InstanceId = None
        self._ConfigName = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""集群ID，例如cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigName(self):
        r"""配置文件名称
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def OperationType(self):
        r"""grace_restart为优雅滚动重启 不填默认立刻重启
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigName = params.get("ConfigName")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForConfigsResponse(AbstractModel):
    r"""RestartClusterForConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程相关信息
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程相关信息
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RestartClusterForNodeRequest(AbstractModel):
    r"""RestartClusterForNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param _ConfigName: 配置文件名称
        :type ConfigName: str
        :param _BatchSize: 每次重启的批次
        :type BatchSize: int
        :param _NodeList: 重启节点
        :type NodeList: list of str
        :param _RollingRestart: false表示非滚动重启，true表示滚动重启
        :type RollingRestart: bool
        """
        self._InstanceId = None
        self._ConfigName = None
        self._BatchSize = None
        self._NodeList = None
        self._RollingRestart = None

    @property
    def InstanceId(self):
        r"""集群ID，例如cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigName(self):
        r"""配置文件名称
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def BatchSize(self):
        r"""每次重启的批次
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def NodeList(self):
        r"""重启节点
        :rtype: list of str
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def RollingRestart(self):
        r"""false表示非滚动重启，true表示滚动重启
        :rtype: bool
        """
        return self._RollingRestart

    @RollingRestart.setter
    def RollingRestart(self, RollingRestart):
        self._RollingRestart = RollingRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigName = params.get("ConfigName")
        self._BatchSize = params.get("BatchSize")
        self._NodeList = params.get("NodeList")
        self._RollingRestart = params.get("RollingRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForNodeResponse(AbstractModel):
    r"""RestartClusterForNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程相关信息
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程相关信息
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RestoreStatus(AbstractModel):
    r"""恢复任务信息

    """

    def __init__(self):
        r"""
        :param _JobId: 恢复任务id
        :type JobId: int
        :param _Label: 恢复任务标签
        :type Label: str
        :param _Timestamp: 恢复任务时间戳
        :type Timestamp: str
        :param _DbName: 恢复任务所在库
        :type DbName: str
        :param _State: 恢复任务状态
        :type State: str
        :param _AllowLoad: 恢复时是否允许导入
        :type AllowLoad: bool
        :param _ReplicationNum: 副本数
        :type ReplicationNum: str
        :param _ReplicaAllocation: 副本数
        :type ReplicaAllocation: str
        :param _RestoreObjects: 恢复对象
        :type RestoreObjects: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _MetaPreparedTime: 元数据准备时间
        :type MetaPreparedTime: str
        :param _SnapshotFinishedTime: 快照结束时间
        :type SnapshotFinishedTime: str
        :param _DownloadFinishedTime: 下载结束时间
        :type DownloadFinishedTime: str
        :param _FinishedTime: 结束时间
        :type FinishedTime: str
        :param _UnfinishedTasks: 未完成任务
        :type UnfinishedTasks: str
        :param _Progress: 进度
        :type Progress: str
        :param _TaskErrMsg: 错误信息
        :type TaskErrMsg: str
        :param _Status: 状态
        :type Status: str
        :param _Timeout: 作业超时时间
        :type Timeout: int
        :param _ReserveReplica: 是否保持源表中的副本数
        :type ReserveReplica: bool
        :param _ReserveDynamicPartitionEnable: 是否保持源表中的动态分区
        :type ReserveDynamicPartitionEnable: bool
        :param _BackupJobId: 备份实例id
        :type BackupJobId: int
        :param _TaskId: 实例对应snapshot的id
        :type TaskId: int
        :param _ID: 恢复任务id
        :type ID: int
        """
        self._JobId = None
        self._Label = None
        self._Timestamp = None
        self._DbName = None
        self._State = None
        self._AllowLoad = None
        self._ReplicationNum = None
        self._ReplicaAllocation = None
        self._RestoreObjects = None
        self._CreateTime = None
        self._MetaPreparedTime = None
        self._SnapshotFinishedTime = None
        self._DownloadFinishedTime = None
        self._FinishedTime = None
        self._UnfinishedTasks = None
        self._Progress = None
        self._TaskErrMsg = None
        self._Status = None
        self._Timeout = None
        self._ReserveReplica = None
        self._ReserveDynamicPartitionEnable = None
        self._BackupJobId = None
        self._TaskId = None
        self._ID = None

    @property
    def JobId(self):
        r"""恢复任务id
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Label(self):
        r"""恢复任务标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Timestamp(self):
        r"""恢复任务时间戳
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def DbName(self):
        r"""恢复任务所在库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def State(self):
        r"""恢复任务状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AllowLoad(self):
        r"""恢复时是否允许导入
        :rtype: bool
        """
        return self._AllowLoad

    @AllowLoad.setter
    def AllowLoad(self, AllowLoad):
        self._AllowLoad = AllowLoad

    @property
    def ReplicationNum(self):
        r"""副本数
        :rtype: str
        """
        return self._ReplicationNum

    @ReplicationNum.setter
    def ReplicationNum(self, ReplicationNum):
        self._ReplicationNum = ReplicationNum

    @property
    def ReplicaAllocation(self):
        r"""副本数
        :rtype: str
        """
        return self._ReplicaAllocation

    @ReplicaAllocation.setter
    def ReplicaAllocation(self, ReplicaAllocation):
        self._ReplicaAllocation = ReplicaAllocation

    @property
    def RestoreObjects(self):
        r"""恢复对象
        :rtype: str
        """
        return self._RestoreObjects

    @RestoreObjects.setter
    def RestoreObjects(self, RestoreObjects):
        self._RestoreObjects = RestoreObjects

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
    def MetaPreparedTime(self):
        r"""元数据准备时间
        :rtype: str
        """
        return self._MetaPreparedTime

    @MetaPreparedTime.setter
    def MetaPreparedTime(self, MetaPreparedTime):
        self._MetaPreparedTime = MetaPreparedTime

    @property
    def SnapshotFinishedTime(self):
        r"""快照结束时间
        :rtype: str
        """
        return self._SnapshotFinishedTime

    @SnapshotFinishedTime.setter
    def SnapshotFinishedTime(self, SnapshotFinishedTime):
        self._SnapshotFinishedTime = SnapshotFinishedTime

    @property
    def DownloadFinishedTime(self):
        r"""下载结束时间
        :rtype: str
        """
        return self._DownloadFinishedTime

    @DownloadFinishedTime.setter
    def DownloadFinishedTime(self, DownloadFinishedTime):
        self._DownloadFinishedTime = DownloadFinishedTime

    @property
    def FinishedTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def UnfinishedTasks(self):
        r"""未完成任务
        :rtype: str
        """
        return self._UnfinishedTasks

    @UnfinishedTasks.setter
    def UnfinishedTasks(self, UnfinishedTasks):
        self._UnfinishedTasks = UnfinishedTasks

    @property
    def Progress(self):
        r"""进度
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskErrMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._TaskErrMsg

    @TaskErrMsg.setter
    def TaskErrMsg(self, TaskErrMsg):
        self._TaskErrMsg = TaskErrMsg

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
    def Timeout(self):
        r"""作业超时时间
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ReserveReplica(self):
        r"""是否保持源表中的副本数
        :rtype: bool
        """
        return self._ReserveReplica

    @ReserveReplica.setter
    def ReserveReplica(self, ReserveReplica):
        self._ReserveReplica = ReserveReplica

    @property
    def ReserveDynamicPartitionEnable(self):
        r"""是否保持源表中的动态分区
        :rtype: bool
        """
        return self._ReserveDynamicPartitionEnable

    @ReserveDynamicPartitionEnable.setter
    def ReserveDynamicPartitionEnable(self, ReserveDynamicPartitionEnable):
        self._ReserveDynamicPartitionEnable = ReserveDynamicPartitionEnable

    @property
    def BackupJobId(self):
        r"""备份实例id
        :rtype: int
        """
        return self._BackupJobId

    @BackupJobId.setter
    def BackupJobId(self, BackupJobId):
        self._BackupJobId = BackupJobId

    @property
    def TaskId(self):
        r"""实例对应snapshot的id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ID(self):
        r"""恢复任务id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Label = params.get("Label")
        self._Timestamp = params.get("Timestamp")
        self._DbName = params.get("DbName")
        self._State = params.get("State")
        self._AllowLoad = params.get("AllowLoad")
        self._ReplicationNum = params.get("ReplicationNum")
        self._ReplicaAllocation = params.get("ReplicaAllocation")
        self._RestoreObjects = params.get("RestoreObjects")
        self._CreateTime = params.get("CreateTime")
        self._MetaPreparedTime = params.get("MetaPreparedTime")
        self._SnapshotFinishedTime = params.get("SnapshotFinishedTime")
        self._DownloadFinishedTime = params.get("DownloadFinishedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._UnfinishedTasks = params.get("UnfinishedTasks")
        self._Progress = params.get("Progress")
        self._TaskErrMsg = params.get("TaskErrMsg")
        self._Status = params.get("Status")
        self._Timeout = params.get("Timeout")
        self._ReserveReplica = params.get("ReserveReplica")
        self._ReserveDynamicPartitionEnable = params.get("ReserveDynamicPartitionEnable")
        self._BackupJobId = params.get("BackupJobId")
        self._TaskId = params.get("TaskId")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceRequest(AbstractModel):
    r"""ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Type: 角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :type Type: str
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _HaType: 扩容后集群高可用类型：0：非高可用，1：读高可用，2：读写高可用。
        :type HaType: int
        :param _CheckAuth: 前端鉴权使用
        :type CheckAuth: bool
        """
        self._InstanceId = None
        self._Type = None
        self._NodeCount = None
        self._HaType = None
        self._CheckAuth = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""角色（MATER/CORE），MASTER 对应 FE，CORE对应BE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeCount(self):
        r"""节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def HaType(self):
        r"""扩容后集群高可用类型：0：非高可用，1：读高可用，2：读写高可用。
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def CheckAuth(self):
        r"""前端鉴权使用
        :rtype: bool
        """
        return self._CheckAuth

    @CheckAuth.setter
    def CheckAuth(self, CheckAuth):
        self._CheckAuth = CheckAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._NodeCount = params.get("NodeCount")
        self._HaType = params.get("HaType")
        self._CheckAuth = params.get("CheckAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    r"""ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    r"""ScaleUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _SpecName: 节点规格
        :type SpecName: str
        :param _Type: 角色（MASTER/CORE），MASTER 对应 FE，CORE对应BE
        :type Type: str
        :param _CheckAuth: 前端鉴权使用，后端API调用传false，传true不会执行变配
        :type CheckAuth: bool
        :param _RollingRestart: 是否滚动重启
        :type RollingRestart: bool
        """
        self._InstanceId = None
        self._SpecName = None
        self._Type = None
        self._CheckAuth = None
        self._RollingRestart = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecName(self):
        r"""节点规格
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Type(self):
        r"""角色（MASTER/CORE），MASTER 对应 FE，CORE对应BE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CheckAuth(self):
        r"""前端鉴权使用，后端API调用传false，传true不会执行变配
        :rtype: bool
        """
        return self._CheckAuth

    @CheckAuth.setter
    def CheckAuth(self, CheckAuth):
        self._CheckAuth = CheckAuth

    @property
    def RollingRestart(self):
        r"""是否滚动重启
        :rtype: bool
        """
        return self._RollingRestart

    @RollingRestart.setter
    def RollingRestart(self, RollingRestart):
        self._RollingRestart = RollingRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecName = params.get("SpecName")
        self._Type = params.get("Type")
        self._CheckAuth = params.get("CheckAuth")
        self._RollingRestart = params.get("RollingRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    r"""ScaleUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScheduleInfo(AbstractModel):
    r"""调度信息

    """

    def __init__(self):
        r"""
        :param _EffectivePeriod: 生效周期
        :type EffectivePeriod: str
        :param _ScheduleType: 调度类型，不传该参数时为立即执行：
Day-天
Week-周
Month-月
Quarter-季度
Year-年
Once-单次

        :type ScheduleType: str
        :param _ScheduleData: 执行调度的日期。调度类型为周和月时以英文逗号分隔；
调度类型为单次时，该值是个日期
        :type ScheduleData: str
        :param _ScheduleHour: 执行时间：时
        :type ScheduleHour: int
        :param _ScheduleMin: 执行时间：分
        :type ScheduleMin: int
        :param _BackupScope: 备份粒度：
All-全量
Database-按库
Table-按表
        :type BackupScope: str
        :param _BackupDatabase: 备份库：如果是按库备份，则需要该字段，库之间用英文逗号分割
        :type BackupDatabase: str
        """
        self._EffectivePeriod = None
        self._ScheduleType = None
        self._ScheduleData = None
        self._ScheduleHour = None
        self._ScheduleMin = None
        self._BackupScope = None
        self._BackupDatabase = None

    @property
    def EffectivePeriod(self):
        r"""生效周期
        :rtype: str
        """
        return self._EffectivePeriod

    @EffectivePeriod.setter
    def EffectivePeriod(self, EffectivePeriod):
        self._EffectivePeriod = EffectivePeriod

    @property
    def ScheduleType(self):
        r"""调度类型，不传该参数时为立即执行：
Day-天
Week-周
Month-月
Quarter-季度
Year-年
Once-单次

        :rtype: str
        """
        return self._ScheduleType

    @ScheduleType.setter
    def ScheduleType(self, ScheduleType):
        self._ScheduleType = ScheduleType

    @property
    def ScheduleData(self):
        r"""执行调度的日期。调度类型为周和月时以英文逗号分隔；
调度类型为单次时，该值是个日期
        :rtype: str
        """
        return self._ScheduleData

    @ScheduleData.setter
    def ScheduleData(self, ScheduleData):
        self._ScheduleData = ScheduleData

    @property
    def ScheduleHour(self):
        r"""执行时间：时
        :rtype: int
        """
        return self._ScheduleHour

    @ScheduleHour.setter
    def ScheduleHour(self, ScheduleHour):
        self._ScheduleHour = ScheduleHour

    @property
    def ScheduleMin(self):
        r"""执行时间：分
        :rtype: int
        """
        return self._ScheduleMin

    @ScheduleMin.setter
    def ScheduleMin(self, ScheduleMin):
        self._ScheduleMin = ScheduleMin

    @property
    def BackupScope(self):
        r"""备份粒度：
All-全量
Database-按库
Table-按表
        :rtype: str
        """
        return self._BackupScope

    @BackupScope.setter
    def BackupScope(self, BackupScope):
        self._BackupScope = BackupScope

    @property
    def BackupDatabase(self):
        r"""备份库：如果是按库备份，则需要该字段，库之间用英文逗号分割
        :rtype: str
        """
        return self._BackupDatabase

    @BackupDatabase.setter
    def BackupDatabase(self, BackupDatabase):
        self._BackupDatabase = BackupDatabase


    def _deserialize(self, params):
        self._EffectivePeriod = params.get("EffectivePeriod")
        self._ScheduleType = params.get("ScheduleType")
        self._ScheduleData = params.get("ScheduleData")
        self._ScheduleHour = params.get("ScheduleHour")
        self._ScheduleMin = params.get("ScheduleMin")
        self._BackupScope = params.get("BackupScope")
        self._BackupDatabase = params.get("BackupDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTags(AbstractModel):
    r"""列表页搜索的标记列表

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        :param _AllValue: 1表示只输入标签的键，没有输入值；非1则表示输入键时且输入值
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

    @property
    def TagKey(self):
        r"""标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签的值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def AllValue(self):
        r"""1表示只输入标签的键，没有输入值；非1则表示输入键时且输入值
        :rtype: int
        """
        return self._AllValue

    @AllValue.setter
    def AllValue(self, AllValue):
        self._AllValue = AllValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowQueryRecord(AbstractModel):
    r"""慢查询记录

    """

    def __init__(self):
        r"""
        :param _OsUser: 查询用户
        :type OsUser: str
        :param _InitialQueryId: 查询ID
        :type InitialQueryId: str
        :param _Sql: SQL语句
        :type Sql: str
        :param _QueryStartTime: 开始时间
        :type QueryStartTime: str
        :param _DurationMs: 执行耗时
        :type DurationMs: int
        :param _ReadRows: 读取行数
        :type ReadRows: int
        :param _ResultRows: 读取字节数
        :type ResultRows: int
        :param _ResultBytes: 结果字节数
        :type ResultBytes: int
        :param _MemoryUsage: 内存
        :type MemoryUsage: int
        :param _InitialAddress: 初始查询IP
        :type InitialAddress: str
        :param _DbName: 数据库名
        :type DbName: str
        :param _IsQuery: 是否是查询，0：否，1：查询语句
        :type IsQuery: int
        :param _ResultBytesMB: ResultBytes的MB格式
        :type ResultBytesMB: float
        :param _MemoryUsageMB: MemoryUsage的MB表示
        :type MemoryUsageMB: float
        :param _DurationSec: DurationMs的秒表示
        :type DurationSec: float
        :param _State: 状态
        :type State: str
        :param _CatalogName: Catalog  Name
        :type CatalogName: str
        :param _CpuTimeMs: cpu执行时间 
        :type CpuTimeMs: int
        :param _ComputeGroup: 计算组
        :type ComputeGroup: str
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._IsQuery = None
        self._ResultBytesMB = None
        self._MemoryUsageMB = None
        self._DurationSec = None
        self._State = None
        self._CatalogName = None
        self._CpuTimeMs = None
        self._ComputeGroup = None

    @property
    def OsUser(self):
        r"""查询用户
        :rtype: str
        """
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        r"""查询ID
        :rtype: str
        """
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        r"""SQL语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        r"""执行耗时
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        r"""读取行数
        :rtype: int
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        r"""读取字节数
        :rtype: int
        """
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        r"""结果字节数
        :rtype: int
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        r"""内存
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        r"""初始查询IP
        :rtype: str
        """
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        r"""数据库名
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        r"""是否是查询，0：否，1：查询语句
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ResultBytesMB(self):
        r"""ResultBytes的MB格式
        :rtype: float
        """
        return self._ResultBytesMB

    @ResultBytesMB.setter
    def ResultBytesMB(self, ResultBytesMB):
        self._ResultBytesMB = ResultBytesMB

    @property
    def MemoryUsageMB(self):
        r"""MemoryUsage的MB表示
        :rtype: float
        """
        return self._MemoryUsageMB

    @MemoryUsageMB.setter
    def MemoryUsageMB(self, MemoryUsageMB):
        self._MemoryUsageMB = MemoryUsageMB

    @property
    def DurationSec(self):
        r"""DurationMs的秒表示
        :rtype: float
        """
        return self._DurationSec

    @DurationSec.setter
    def DurationSec(self, DurationSec):
        self._DurationSec = DurationSec

    @property
    def State(self):
        r"""状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CatalogName(self):
        r"""Catalog  Name
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def CpuTimeMs(self):
        r"""cpu执行时间 
        :rtype: int
        """
        return self._CpuTimeMs

    @CpuTimeMs.setter
    def CpuTimeMs(self, CpuTimeMs):
        self._CpuTimeMs = CpuTimeMs

    @property
    def ComputeGroup(self):
        r"""计算组
        :rtype: str
        """
        return self._ComputeGroup

    @ComputeGroup.setter
    def ComputeGroup(self, ComputeGroup):
        self._ComputeGroup = ComputeGroup


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._ResultBytesMB = params.get("ResultBytesMB")
        self._MemoryUsageMB = params.get("MemoryUsageMB")
        self._DurationSec = params.get("DurationSec")
        self._State = params.get("State")
        self._CatalogName = params.get("CatalogName")
        self._CpuTimeMs = params.get("CpuTimeMs")
        self._ComputeGroup = params.get("ComputeGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotRemainPolicy(AbstractModel):
    r"""备份快照保留策略

    """

    def __init__(self):
        r"""
        :param _Type: 0-不主动删除；1-超过指定时间周期自动删除；2-保留指定数据快照
        :type Type: int
        :param _RemainDays: 保留快照的时间
        :type RemainDays: int
        :param _RemainLatestNum: 保留最新快照的数量
        :type RemainLatestNum: int
        """
        self._Type = None
        self._RemainDays = None
        self._RemainLatestNum = None

    @property
    def Type(self):
        r"""0-不主动删除；1-超过指定时间周期自动删除；2-保留指定数据快照
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RemainDays(self):
        r"""保留快照的时间
        :rtype: int
        """
        return self._RemainDays

    @RemainDays.setter
    def RemainDays(self, RemainDays):
        self._RemainDays = RemainDays

    @property
    def RemainLatestNum(self):
        r"""保留最新快照的数量
        :rtype: int
        """
        return self._RemainLatestNum

    @RemainLatestNum.setter
    def RemainLatestNum(self, RemainLatestNum):
        self._RemainLatestNum = RemainLatestNum


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._RemainDays = params.get("RemainDays")
        self._RemainLatestNum = params.get("RemainLatestNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签描述

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签的值
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
        


class UpdateCoolDownRequest(AbstractModel):
    r"""UpdateCoolDown请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _Enable: 是否启用 0：不启用 1：启用
        :type Enable: int
        :param _Bucket: 用户存放冷热分层数据Cos桶地址
        :type Bucket: str
        """
        self._InstanceId = None
        self._Enable = None
        self._Bucket = None

    @property
    def InstanceId(self):
        r"""集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Enable(self):
        r"""是否启用 0：不启用 1：启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Bucket(self):
        r"""用户存放冷热分层数据Cos桶地址
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Enable = params.get("Enable")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCoolDownResponse(AbstractModel):
    r"""UpdateCoolDown返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class UpdateUserPrivileges(AbstractModel):
    r"""更新用户权限结构体

    """

    def __init__(self):
        r"""
        :param _IsSetGlobalCatalog: 是否设置catalog权限
        :type IsSetGlobalCatalog: bool
        """
        self._IsSetGlobalCatalog = None

    @property
    def IsSetGlobalCatalog(self):
        r"""是否设置catalog权限
        :rtype: bool
        """
        return self._IsSetGlobalCatalog

    @IsSetGlobalCatalog.setter
    def IsSetGlobalCatalog(self, IsSetGlobalCatalog):
        self._IsSetGlobalCatalog = IsSetGlobalCatalog


    def _deserialize(self, params):
        self._IsSetGlobalCatalog = params.get("IsSetGlobalCatalog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    r"""新增或是修改用户

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例id
        :type InstanceId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _PassWord: 密码
        :type PassWord: str
        :param _WhiteHost: 用户链接来自的 IP
        :type WhiteHost: str
        :param _OldWhiteHost: 修改前用户链接来自的 IP
        :type OldWhiteHost: str
        :param _Describe: 描述
        :type Describe: str
        :param _OldPwd: 旧密码
        :type OldPwd: str
        :param _CamUin: 绑定的子用户uin
        :type CamUin: str
        :param _CamRangerGroupIds: ranger group id列表
        :type CamRangerGroupIds: list of int
        :param _ComputeGroupType: 0: 灵活场景 1: 固定场景
        :type ComputeGroupType: int
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._WhiteHost = None
        self._OldWhiteHost = None
        self._Describe = None
        self._OldPwd = None
        self._CamUin = None
        self._CamRangerGroupIds = None
        self._ComputeGroupType = None

    @property
    def InstanceId(self):
        r"""集群实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PassWord(self):
        r"""密码
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def WhiteHost(self):
        r"""用户链接来自的 IP
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost

    @property
    def OldWhiteHost(self):
        r"""修改前用户链接来自的 IP
        :rtype: str
        """
        return self._OldWhiteHost

    @OldWhiteHost.setter
    def OldWhiteHost(self, OldWhiteHost):
        self._OldWhiteHost = OldWhiteHost

    @property
    def Describe(self):
        r"""描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def OldPwd(self):
        r"""旧密码
        :rtype: str
        """
        return self._OldPwd

    @OldPwd.setter
    def OldPwd(self, OldPwd):
        self._OldPwd = OldPwd

    @property
    def CamUin(self):
        r"""绑定的子用户uin
        :rtype: str
        """
        return self._CamUin

    @CamUin.setter
    def CamUin(self, CamUin):
        self._CamUin = CamUin

    @property
    def CamRangerGroupIds(self):
        r"""ranger group id列表
        :rtype: list of int
        """
        return self._CamRangerGroupIds

    @CamRangerGroupIds.setter
    def CamRangerGroupIds(self, CamRangerGroupIds):
        self._CamRangerGroupIds = CamRangerGroupIds

    @property
    def ComputeGroupType(self):
        r"""0: 灵活场景 1: 固定场景
        :rtype: int
        """
        return self._ComputeGroupType

    @ComputeGroupType.setter
    def ComputeGroupType(self, ComputeGroupType):
        self._ComputeGroupType = ComputeGroupType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._WhiteHost = params.get("WhiteHost")
        self._OldWhiteHost = params.get("OldWhiteHost")
        self._Describe = params.get("Describe")
        self._OldPwd = params.get("OldPwd")
        self._CamUin = params.get("CamUin")
        self._CamRangerGroupIds = params.get("CamRangerGroupIds")
        self._ComputeGroupType = params.get("ComputeGroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserWorkloadGroup(AbstractModel):
    r"""用户绑定资源组信息

    """

    def __init__(self):
        r"""
        :param _UserName: test
        :type UserName: str
        :param _WorkloadGroupName: normal
        :type WorkloadGroupName: str
        """
        self._UserName = None
        self._WorkloadGroupName = None

    @property
    def UserName(self):
        r"""test
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def WorkloadGroupName(self):
        r"""normal
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadGroupConfig(AbstractModel):
    r"""资源组相关配置

    """

    def __init__(self):
        r"""
        :param _WorkloadGroupName: 资源组名称
        :type WorkloadGroupName: str
        :param _CpuShare: CPU权重
        :type CpuShare: int
        :param _MemoryLimit: 内存限制，所有资源组的内存限制值之和应该小于等于100
        :type MemoryLimit: int
        :param _EnableMemoryOverCommit: 是否允许超配分配
        :type EnableMemoryOverCommit: bool
        :param _CpuHardLimit: cpu硬限制
        :type CpuHardLimit: str
        """
        self._WorkloadGroupName = None
        self._CpuShare = None
        self._MemoryLimit = None
        self._EnableMemoryOverCommit = None
        self._CpuHardLimit = None

    @property
    def WorkloadGroupName(self):
        r"""资源组名称
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName

    @property
    def CpuShare(self):
        r"""CPU权重
        :rtype: int
        """
        return self._CpuShare

    @CpuShare.setter
    def CpuShare(self, CpuShare):
        self._CpuShare = CpuShare

    @property
    def MemoryLimit(self):
        r"""内存限制，所有资源组的内存限制值之和应该小于等于100
        :rtype: int
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def EnableMemoryOverCommit(self):
        r"""是否允许超配分配
        :rtype: bool
        """
        return self._EnableMemoryOverCommit

    @EnableMemoryOverCommit.setter
    def EnableMemoryOverCommit(self, EnableMemoryOverCommit):
        self._EnableMemoryOverCommit = EnableMemoryOverCommit

    @property
    def CpuHardLimit(self):
        r"""cpu硬限制
        :rtype: str
        """
        return self._CpuHardLimit

    @CpuHardLimit.setter
    def CpuHardLimit(self, CpuHardLimit):
        self._CpuHardLimit = CpuHardLimit


    def _deserialize(self, params):
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        self._CpuShare = params.get("CpuShare")
        self._MemoryLimit = params.get("MemoryLimit")
        self._EnableMemoryOverCommit = params.get("EnableMemoryOverCommit")
        self._CpuHardLimit = params.get("CpuHardLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""可用区描述信息

    """

    def __init__(self):
        r"""
        :param _Name: 可用区名称，例如"ap-guangzhou-1"
        :type Name: str
        :param _Desc: 可用区描述信息，例如“广州一区”
        :type Desc: str
        :param _ZoneId: 可用区唯一标记
        :type ZoneId: int
        :param _Encrypt: Encrypted
        :type Encrypt: int
        :param _Main: 是否为主力园区
        :type Main: bool
        :param _ContainerEnabled: 0表示未开通容器化，1表示已开通容器化
        :type ContainerEnabled: int
        """
        self._Name = None
        self._Desc = None
        self._ZoneId = None
        self._Encrypt = None
        self._Main = None
        self._ContainerEnabled = None

    @property
    def Name(self):
        r"""可用区名称，例如"ap-guangzhou-1"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""可用区描述信息，例如“广州一区”
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ZoneId(self):
        r"""可用区唯一标记
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Encrypt(self):
        r"""Encrypted
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Main(self):
        r"""是否为主力园区
        :rtype: bool
        """
        return self._Main

    @Main.setter
    def Main(self, Main):
        self._Main = Main

    @property
    def ContainerEnabled(self):
        r"""0表示未开通容器化，1表示已开通容器化
        :rtype: int
        """
        return self._ContainerEnabled

    @ContainerEnabled.setter
    def ContainerEnabled(self, ContainerEnabled):
        self._ContainerEnabled = ContainerEnabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ZoneId = params.get("ZoneId")
        self._Encrypt = params.get("Encrypt")
        self._Main = params.get("Main")
        self._ContainerEnabled = params.get("ContainerEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        