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


class ActionAlterCkUserRequest(AbstractModel):
    """ActionAlterCkUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.cdwch.v20200915.models.CkUserAlterInfo`
        :param _ApiType: api接口类型，
AddSystemUser新增用户，UpdateSystemUser，修改用户
        :type ApiType: str
        """
        self._UserInfo = None
        self._ApiType = None

    @property
    def UserInfo(self):
        """用户信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.CkUserAlterInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def ApiType(self):
        """api接口类型，
AddSystemUser新增用户，UpdateSystemUser，修改用户
        :rtype: str
        """
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = CkUserAlterInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._ApiType = params.get("ApiType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterCkUserResponse(AbstractModel):
    """ActionAlterCkUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrMsg = None
        self._RequestId = None

    @property
    def ErrMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class AttachCBSSpec(AbstractModel):
    """集群内节点的规格磁盘规格描述

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
        """节点磁盘类型，例如“CLOUD_SSD”\"CLOUD_PREMIUM"
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """磁盘容量，单位G
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """磁盘总数
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskDesc(self):
        """描述
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
    """备份任务详情

    """

    def __init__(self):
        r"""
        :param _JobId: 备份任务id
        :type JobId: int
        :param _Snapshot: 备份任务名
        :type Snapshot: str
        :param _BackUpType: 任务类型(元数据),(数据)
        :type BackUpType: str
        :param _BackUpSize: 备份数据量
        :type BackUpSize: int
        :param _BackUpTime: 任务创建时间
        :type BackUpTime: str
        :param _ExpireTime: 任务过期时间
        :type ExpireTime: str
        :param _JobStatus: 任务状态
        :type JobStatus: str
        :param _ProcessSize: 处理数据量
        :type ProcessSize: int
        :param _ErrorReason: 错误原因
        :type ErrorReason: str
        """
        self._JobId = None
        self._Snapshot = None
        self._BackUpType = None
        self._BackUpSize = None
        self._BackUpTime = None
        self._ExpireTime = None
        self._JobStatus = None
        self._ProcessSize = None
        self._ErrorReason = None

    @property
    def JobId(self):
        """备份任务id
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Snapshot(self):
        """备份任务名
        :rtype: str
        """
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def BackUpType(self):
        """任务类型(元数据),(数据)
        :rtype: str
        """
        return self._BackUpType

    @BackUpType.setter
    def BackUpType(self, BackUpType):
        self._BackUpType = BackUpType

    @property
    def BackUpSize(self):
        """备份数据量
        :rtype: int
        """
        return self._BackUpSize

    @BackUpSize.setter
    def BackUpSize(self, BackUpSize):
        self._BackUpSize = BackUpSize

    @property
    def BackUpTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._BackUpTime

    @BackUpTime.setter
    def BackUpTime(self, BackUpTime):
        self._BackUpTime = BackUpTime

    @property
    def ExpireTime(self):
        """任务过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def JobStatus(self):
        """任务状态
        :rtype: str
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def ProcessSize(self):
        """处理数据量
        :rtype: int
        """
        return self._ProcessSize

    @ProcessSize.setter
    def ProcessSize(self, ProcessSize):
        self._ProcessSize = ProcessSize

    @property
    def ErrorReason(self):
        """错误原因
        :rtype: str
        """
        return self._ErrorReason

    @ErrorReason.setter
    def ErrorReason(self, ErrorReason):
        self._ErrorReason = ErrorReason


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Snapshot = params.get("Snapshot")
        self._BackUpType = params.get("BackUpType")
        self._BackUpSize = params.get("BackUpSize")
        self._BackUpTime = params.get("BackUpTime")
        self._ExpireTime = params.get("ExpireTime")
        self._JobStatus = params.get("JobStatus")
        self._ProcessSize = params.get("ProcessSize")
        self._ErrorReason = params.get("ErrorReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTableContent(AbstractModel):
    """备份表信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库
        :type Database: str
        :param _Table: 表
        :type Table: str
        :param _TotalBytes: 表总字节数
        :type TotalBytes: int
        :param _VCluster: 虚拟cluster
        :type VCluster: str
        :param _Ips: 表ip
        :type Ips: str
        :param _ZooPath: zk路径
        :type ZooPath: str
        :param _Rip: cvm的ip地址
        :type Rip: str
        """
        self._Database = None
        self._Table = None
        self._TotalBytes = None
        self._VCluster = None
        self._Ips = None
        self._ZooPath = None
        self._Rip = None

    @property
    def Database(self):
        """数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """表
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TotalBytes(self):
        """表总字节数
        :rtype: int
        """
        return self._TotalBytes

    @TotalBytes.setter
    def TotalBytes(self, TotalBytes):
        self._TotalBytes = TotalBytes

    @property
    def VCluster(self):
        """虚拟cluster
        :rtype: str
        """
        return self._VCluster

    @VCluster.setter
    def VCluster(self, VCluster):
        self._VCluster = VCluster

    @property
    def Ips(self):
        """表ip
        :rtype: str
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def ZooPath(self):
        """zk路径
        :rtype: str
        """
        return self._ZooPath

    @ZooPath.setter
    def ZooPath(self, ZooPath):
        self._ZooPath = ZooPath

    @property
    def Rip(self):
        """cvm的ip地址
        :rtype: str
        """
        return self._Rip

    @Rip.setter
    def Rip(self, Rip):
        self._Rip = Rip


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._TotalBytes = params.get("TotalBytes")
        self._VCluster = params.get("VCluster")
        self._Ips = params.get("Ips")
        self._ZooPath = params.get("ZooPath")
        self._Rip = params.get("Rip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Charge(AbstractModel):
    """集群计费相关信息

    """

    def __init__(self):
        r"""
        :param _ChargeType: 计费类型，“PREPAID” 预付费，“POSTPAID_BY_HOUR” 后付费
        :type ChargeType: str
        :param _RenewFlag: PREPAID需要传递，是否自动续费，1表示自动续费开启
        :type RenewFlag: int
        :param _TimeSpan: 预付费需要传递，计费时间长度，多少个月
        :type TimeSpan: int
        """
        self._ChargeType = None
        self._RenewFlag = None
        self._TimeSpan = None

    @property
    def ChargeType(self):
        """计费类型，“PREPAID” 预付费，“POSTPAID_BY_HOUR” 后付费
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RenewFlag(self):
        """PREPAID需要传递，是否自动续费，1表示自动续费开启
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        """预付费需要传递，计费时间长度，多少个月
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkUserAlterInfo(AbstractModel):
    """新增或是修改ck用户

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例id
        :type InstanceId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _PassWord: base64加密后的密码
        :type PassWord: str
        :param _Describe: 描述
        :type Describe: str
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._Describe = None

    @property
    def InstanceId(self):
        """集群实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """base64加密后的密码
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def Describe(self):
        """描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfigsInfoFromEMR(AbstractModel):
    """用于返回XML格式的配置文件和内容以及其他配置文件有关的信息

    """

    def __init__(self):
        r"""
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
        :param _FilePath: 保存配置文件的路径
        :type FilePath: str
        """
        self._FileName = None
        self._FileConf = None
        self._KeyConf = None
        self._OriParam = None
        self._NeedRestart = None
        self._FilePath = None

    @property
    def FileName(self):
        """配置文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileConf(self):
        """配置文件对应的相关属性信息
        :rtype: str
        """
        return self._FileConf

    @FileConf.setter
    def FileConf(self, FileConf):
        self._FileConf = FileConf

    @property
    def KeyConf(self):
        """配置文件对应的其他属性信息
        :rtype: str
        """
        return self._KeyConf

    @KeyConf.setter
    def KeyConf(self, KeyConf):
        self._KeyConf = KeyConf

    @property
    def OriParam(self):
        """配置文件的内容，base64编码
        :rtype: str
        """
        return self._OriParam

    @OriParam.setter
    def OriParam(self, OriParam):
        self._OriParam = OriParam

    @property
    def NeedRestart(self):
        """用于表示当前配置文件是不是有过修改后没有重启，提醒用户需要重启
        :rtype: int
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def FilePath(self):
        """保存配置文件的路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileConf = params.get("FileConf")
        self._KeyConf = params.get("KeyConf")
        self._OriParam = params.get("OriParam")
        self._NeedRestart = params.get("NeedRestart")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """clickhouse vcluster信息

    """

    def __init__(self):
        r"""
        :param _ClusterName: vcluster名字
        :type ClusterName: str
        :param _NodeIps: 当前cluster的IP列表
        :type NodeIps: list of str
        """
        self._ClusterName = None
        self._NodeIps = None

    @property
    def ClusterName(self):
        """vcluster名字
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NodeIps(self):
        """当前cluster的IP列表
        :rtype: list of str
        """
        return self._NodeIps

    @NodeIps.setter
    def NodeIps(self, NodeIps):
        self._NodeIps = NodeIps


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._NodeIps = params.get("NodeIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSubmitContext(AbstractModel):
    """配置文件修改信息

    """

    def __init__(self):
        r"""
        :param _FileName: 配置文件名称
        :type FileName: str
        :param _OldConfValue: 配置文件旧内容，base64编码
        :type OldConfValue: str
        :param _NewConfValue: 配置文件新内容，base64编码
        :type NewConfValue: str
        :param _FilePath: 保存配置文件的路径
        :type FilePath: str
        """
        self._FileName = None
        self._OldConfValue = None
        self._NewConfValue = None
        self._FilePath = None

    @property
    def FileName(self):
        """配置文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def OldConfValue(self):
        """配置文件旧内容，base64编码
        :rtype: str
        """
        return self._OldConfValue

    @OldConfValue.setter
    def OldConfValue(self, OldConfValue):
        self._OldConfValue = OldConfValue

    @property
    def NewConfValue(self):
        """配置文件新内容，base64编码
        :rtype: str
        """
        return self._NewConfValue

    @NewConfValue.setter
    def NewConfValue(self, NewConfValue):
        self._NewConfValue = NewConfValue

    @property
    def FilePath(self):
        """保存配置文件的路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._OldConfValue = params.get("OldConfValue")
        self._NewConfValue = params.get("NewConfValue")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleRequest(AbstractModel):
    """CreateBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _ScheduleType: 策略类型 meta(元数据)  data (表数据)
        :type ScheduleType: str
        :param _OperationType: 操作类型 create(创建) update(编辑修改)
        :type OperationType: str
        :param _RetainDays: 保留天数 例如7
        :type RetainDays: int
        :param _ScheduleId: 编辑时需要传
        :type ScheduleId: int
        :param _WeekDays: 选择的星期 逗号分隔，例如 2 代表周二
        :type WeekDays: str
        :param _ExecuteHour: 执行小时
        :type ExecuteHour: int
        :param _BackUpTables: 备份表列表
        :type BackUpTables: list of BackupTableContent
        """
        self._InstanceId = None
        self._ScheduleType = None
        self._OperationType = None
        self._RetainDays = None
        self._ScheduleId = None
        self._WeekDays = None
        self._ExecuteHour = None
        self._BackUpTables = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ScheduleType(self):
        """策略类型 meta(元数据)  data (表数据)
        :rtype: str
        """
        return self._ScheduleType

    @ScheduleType.setter
    def ScheduleType(self, ScheduleType):
        self._ScheduleType = ScheduleType

    @property
    def OperationType(self):
        """操作类型 create(创建) update(编辑修改)
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def RetainDays(self):
        """保留天数 例如7
        :rtype: int
        """
        return self._RetainDays

    @RetainDays.setter
    def RetainDays(self, RetainDays):
        self._RetainDays = RetainDays

    @property
    def ScheduleId(self):
        """编辑时需要传
        :rtype: int
        """
        return self._ScheduleId

    @ScheduleId.setter
    def ScheduleId(self, ScheduleId):
        self._ScheduleId = ScheduleId

    @property
    def WeekDays(self):
        """选择的星期 逗号分隔，例如 2 代表周二
        :rtype: str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def ExecuteHour(self):
        """执行小时
        :rtype: int
        """
        return self._ExecuteHour

    @ExecuteHour.setter
    def ExecuteHour(self, ExecuteHour):
        self._ExecuteHour = ExecuteHour

    @property
    def BackUpTables(self):
        """备份表列表
        :rtype: list of BackupTableContent
        """
        return self._BackUpTables

    @BackUpTables.setter
    def BackUpTables(self, BackUpTables):
        self._BackUpTables = BackUpTables


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ScheduleType = params.get("ScheduleType")
        self._OperationType = params.get("OperationType")
        self._RetainDays = params.get("RetainDays")
        self._ScheduleId = params.get("ScheduleId")
        self._WeekDays = params.get("WeekDays")
        self._ExecuteHour = params.get("ExecuteHour")
        if params.get("BackUpTables") is not None:
            self._BackUpTables = []
            for item in params.get("BackUpTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._BackUpTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleResponse(AbstractModel):
    """CreateBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误描述
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """错误描述
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """CreateInstanceNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _HaFlag: 是否高可用
        :type HaFlag: bool
        :param _UserVPCId: 私有网络
        :type UserVPCId: str
        :param _UserSubnetId: 子网
        :type UserSubnetId: str
        :param _ProductVersion: 系统版本
        :type ProductVersion: str
        :param _ChargeProperties: 计费方式
        :type ChargeProperties: :class:`tencentcloud.cdwch.v20200915.models.Charge`
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _DataSpec: 数据节点
SpecName从DescribeSpec接口中返回的DataSpec.Name获取
        :type DataSpec: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        :param _Tags: 标签列表（废弃）
        :type Tags: :class:`tencentcloud.cdwch.v20200915.models.Tag`
        :param _ClsLogSetId: 日志主题ID
        :type ClsLogSetId: str
        :param _CosBucketName: COS桶名称
        :type CosBucketName: str
        :param _MountDiskType: 是否是裸盘挂载，默认值 0 为 未挂载，1 为挂载。
        :type MountDiskType: int
        :param _HAZk: 是否是ZK高可用
        :type HAZk: bool
        :param _CommonSpec: ZK节点
SpecName从DescribeSpec接口中返回的CommonSpec.Name（ZK节点）获取
        :type CommonSpec: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        :param _TagItems: 标签列表
        :type TagItems: list of Tag
        :param _SecondaryZoneInfo: 副可用去信息
        :type SecondaryZoneInfo: list of SecondaryZoneInfo
        """
        self._Zone = None
        self._HaFlag = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ProductVersion = None
        self._ChargeProperties = None
        self._InstanceName = None
        self._DataSpec = None
        self._Tags = None
        self._ClsLogSetId = None
        self._CosBucketName = None
        self._MountDiskType = None
        self._HAZk = None
        self._CommonSpec = None
        self._TagItems = None
        self._SecondaryZoneInfo = None

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def HaFlag(self):
        """是否高可用
        :rtype: bool
        """
        return self._HaFlag

    @HaFlag.setter
    def HaFlag(self, HaFlag):
        self._HaFlag = HaFlag

    @property
    def UserVPCId(self):
        """私有网络
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        """子网
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ProductVersion(self):
        """系统版本
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def ChargeProperties(self):
        """计费方式
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.Charge`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DataSpec(self):
        """数据节点
SpecName从DescribeSpec接口中返回的DataSpec.Name获取
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        """
        return self._DataSpec

    @DataSpec.setter
    def DataSpec(self, DataSpec):
        self._DataSpec = DataSpec

    @property
    def Tags(self):
        warnings.warn("parameter `Tags` is deprecated", DeprecationWarning) 

        """标签列表（废弃）
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.Tag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        warnings.warn("parameter `Tags` is deprecated", DeprecationWarning) 

        self._Tags = Tags

    @property
    def ClsLogSetId(self):
        """日志主题ID
        :rtype: str
        """
        return self._ClsLogSetId

    @ClsLogSetId.setter
    def ClsLogSetId(self, ClsLogSetId):
        self._ClsLogSetId = ClsLogSetId

    @property
    def CosBucketName(self):
        """COS桶名称
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def MountDiskType(self):
        """是否是裸盘挂载，默认值 0 为 未挂载，1 为挂载。
        :rtype: int
        """
        return self._MountDiskType

    @MountDiskType.setter
    def MountDiskType(self, MountDiskType):
        self._MountDiskType = MountDiskType

    @property
    def HAZk(self):
        """是否是ZK高可用
        :rtype: bool
        """
        return self._HAZk

    @HAZk.setter
    def HAZk(self, HAZk):
        self._HAZk = HAZk

    @property
    def CommonSpec(self):
        """ZK节点
SpecName从DescribeSpec接口中返回的CommonSpec.Name（ZK节点）获取
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        """
        return self._CommonSpec

    @CommonSpec.setter
    def CommonSpec(self, CommonSpec):
        self._CommonSpec = CommonSpec

    @property
    def TagItems(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._TagItems

    @TagItems.setter
    def TagItems(self, TagItems):
        self._TagItems = TagItems

    @property
    def SecondaryZoneInfo(self):
        """副可用去信息
        :rtype: list of SecondaryZoneInfo
        """
        return self._SecondaryZoneInfo

    @SecondaryZoneInfo.setter
    def SecondaryZoneInfo(self, SecondaryZoneInfo):
        self._SecondaryZoneInfo = SecondaryZoneInfo


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._HaFlag = params.get("HaFlag")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._ProductVersion = params.get("ProductVersion")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = Charge()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._InstanceName = params.get("InstanceName")
        if params.get("DataSpec") is not None:
            self._DataSpec = NodeSpec()
            self._DataSpec._deserialize(params.get("DataSpec"))
        if params.get("Tags") is not None:
            self._Tags = Tag()
            self._Tags._deserialize(params.get("Tags"))
        self._ClsLogSetId = params.get("ClsLogSetId")
        self._CosBucketName = params.get("CosBucketName")
        self._MountDiskType = params.get("MountDiskType")
        self._HAZk = params.get("HAZk")
        if params.get("CommonSpec") is not None:
            self._CommonSpec = NodeSpec()
            self._CommonSpec._deserialize(params.get("CommonSpec"))
        if params.get("TagItems") is not None:
            self._TagItems = []
            for item in params.get("TagItems"):
                obj = Tag()
                obj._deserialize(item)
                self._TagItems.append(obj)
        if params.get("SecondaryZoneInfo") is not None:
            self._SecondaryZoneInfo = []
            for item in params.get("SecondaryZoneInfo"):
                obj = SecondaryZoneInfo()
                obj._deserialize(item)
                self._SecondaryZoneInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewResponse(AbstractModel):
    """CreateInstanceNew返回参数结构体

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
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DatabasePrivilegeInfo(AbstractModel):
    """数据库权限信息

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        :param _DatabasePrivileges: 库表权限，SELECT、INSERT_ALL、ALTER、TRUNCATE、DROP_TABLE、CREATE_TABLE、DROP_DATABASE
        :type DatabasePrivileges: list of str
        :param _TablePrivilegeList: 库下面的表权限
        :type TablePrivilegeList: list of TablePrivilegeInfo
        """
        self._DatabaseName = None
        self._DatabasePrivileges = None
        self._TablePrivilegeList = None

    @property
    def DatabaseName(self):
        """数据库名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabasePrivileges(self):
        """库表权限，SELECT、INSERT_ALL、ALTER、TRUNCATE、DROP_TABLE、CREATE_TABLE、DROP_DATABASE
        :rtype: list of str
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivilegeList(self):
        """库下面的表权限
        :rtype: list of TablePrivilegeInfo
        """
        return self._TablePrivilegeList

    @TablePrivilegeList.setter
    def TablePrivilegeList(self, TablePrivilegeList):
        self._TablePrivilegeList = TablePrivilegeList


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._DatabasePrivileges = params.get("DatabasePrivileges")
        if params.get("TablePrivilegeList") is not None:
            self._TablePrivilegeList = []
            for item in params.get("TablePrivilegeList"):
                obj = TablePrivilegeInfo()
                obj._deserialize(item)
                self._TablePrivilegeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataRequest(AbstractModel):
    """DeleteBackUpData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _BackUpJobId: 任务id
        :type BackUpJobId: int
        :param _IsDeleteAll: 是否删除所有数据
        :type IsDeleteAll: bool
        """
        self._InstanceId = None
        self._BackUpJobId = None
        self._IsDeleteAll = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """任务id
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId

    @property
    def IsDeleteAll(self):
        """是否删除所有数据
        :rtype: bool
        """
        return self._IsDeleteAll

    @IsDeleteAll.setter
    def IsDeleteAll(self, IsDeleteAll):
        self._IsDeleteAll = IsDeleteAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        self._IsDeleteAll = params.get("IsDeleteAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataResponse(AbstractModel):
    """DeleteBackUpData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobDetailRequest(AbstractModel):
    """DescribeBackUpJobDetail请求参数结构体

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
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """任务id
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
    """DescribeBackUpJobDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableContents: 备份表详情
        :type TableContents: list of BackupTableContent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableContents = None
        self._RequestId = None

    @property
    def TableContents(self):
        """备份表详情
        :rtype: list of BackupTableContent
        """
        return self._TableContents

    @TableContents.setter
    def TableContents(self, TableContents):
        self._TableContents = TableContents

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobRequest(AbstractModel):
    """DescribeBackUpJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _PageNum: 页号
        :type PageNum: int
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._InstanceId = None
        self._PageSize = None
        self._PageNum = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageSize(self):
        """分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """页号
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def BeginTime(self):
        """开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpJobResponse(AbstractModel):
    """DescribeBackUpJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackUpJobs: 任务列表
        :type BackUpJobs: list of BackUpJobDisplay
        :param _ErrorMsg: 错误描述
        :type ErrorMsg: str
        :param _TotalCount: 数量
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
        """任务列表
        :rtype: list of BackUpJobDisplay
        """
        return self._BackUpJobs

    @BackUpJobs.setter
    def BackUpJobs(self, BackUpJobs):
        self._BackUpJobs = BackUpJobs

    @property
    def ErrorMsg(self):
        """错误描述
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeBackUpScheduleRequest(AbstractModel):
    """DescribeBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群id
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
        


class DescribeBackUpScheduleResponse(AbstractModel):
    """DescribeBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackUpOpened: 备份是否开启
        :type BackUpOpened: bool
        :param _MetaStrategy: 元数据备份策略
        :type MetaStrategy: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        :param _DataStrategy: 表数据备份策略
        :type DataStrategy: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        :param _BackUpContents: 备份表列表
        :type BackUpContents: list of BackupTableContent
        :param _BackUpStatus: 备份的状态
        :type BackUpStatus: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackUpOpened = None
        self._MetaStrategy = None
        self._DataStrategy = None
        self._BackUpContents = None
        self._BackUpStatus = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def BackUpOpened(self):
        """备份是否开启
        :rtype: bool
        """
        return self._BackUpOpened

    @BackUpOpened.setter
    def BackUpOpened(self, BackUpOpened):
        self._BackUpOpened = BackUpOpened

    @property
    def MetaStrategy(self):
        """元数据备份策略
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        """
        return self._MetaStrategy

    @MetaStrategy.setter
    def MetaStrategy(self, MetaStrategy):
        self._MetaStrategy = MetaStrategy

    @property
    def DataStrategy(self):
        """表数据备份策略
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        """
        return self._DataStrategy

    @DataStrategy.setter
    def DataStrategy(self, DataStrategy):
        self._DataStrategy = DataStrategy

    @property
    def BackUpContents(self):
        """备份表列表
        :rtype: list of BackupTableContent
        """
        return self._BackUpContents

    @BackUpContents.setter
    def BackUpContents(self, BackUpContents):
        self._BackUpContents = BackUpContents

    @property
    def BackUpStatus(self):
        """备份的状态
        :rtype: int
        """
        return self._BackUpStatus

    @BackUpStatus.setter
    def BackUpStatus(self, BackUpStatus):
        self._BackUpStatus = BackUpStatus

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackUpOpened = params.get("BackUpOpened")
        if params.get("MetaStrategy") is not None:
            self._MetaStrategy = ScheduleStrategy()
            self._MetaStrategy._deserialize(params.get("MetaStrategy"))
        if params.get("DataStrategy") is not None:
            self._DataStrategy = ScheduleStrategy()
            self._DataStrategy._deserialize(params.get("DataStrategy"))
        if params.get("BackUpContents") is not None:
            self._BackUpContents = []
            for item in params.get("BackUpContents"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._BackUpContents.append(obj)
        self._BackUpStatus = params.get("BackUpStatus")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeBackUpTablesRequest(AbstractModel):
    """DescribeBackUpTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群id
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
        


class DescribeBackUpTablesResponse(AbstractModel):
    """DescribeBackUpTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableTables: 可备份表列表
        :type AvailableTables: list of BackupTableContent
        :param _ErrorMsg: 错误描述
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableTables = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def AvailableTables(self):
        """可备份表列表
        :rtype: list of BackupTableContent
        """
        return self._AvailableTables

    @AvailableTables.setter
    def AvailableTables(self, AvailableTables):
        self._AvailableTables = AvailableTables

    @property
    def ErrorMsg(self):
        """错误描述
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeCkSqlApisRequest(AbstractModel):
    """DescribeCkSqlApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ApiType: api接口名称,GetClusters:获取集群cluster列表
GetSystemUsers:获取系统用户列表
CheckNodeCluster: 检查节点是否隶属一个cluster
GetClusterDatabases: 获取一个cluster下的数据库列表
GetClusterTables: 获取一个cluster下的数据库表列表
GetPrivilegeUsers: 获取授权的用户列表
GET_USER_CLUSTER_PRIVILEGES:获取用户cluster下的权限   
GetUserClusterNewPrivileges:获取用户cluster下的权限 (新版）
RevokeClusterUser:解绑cluster用户
DeleteSystemUser:删除系统用户 —— 必须所有cluster先解绑
GetUserOptionMessages:获取用户配置备注信息
GET_USER_CONFIGS:获取用户配置列表  QUOTA、PROFILE、POLICY
        :type ApiType: str
        :param _Cluster: 集群名称，GET_SYSTEM_USERS，GET_PRIVILEGE_USERS，GET_CLUSTER_DATABASES，GET_CLUSTER_TABLES 必填
        :type Cluster: str
        :param _UserName: 用户名称，api与user相关的必填
        :type UserName: str
        :param _UserType: 账户的类型
        :type UserType: str
        """
        self._InstanceId = None
        self._ApiType = None
        self._Cluster = None
        self._UserName = None
        self._UserType = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApiType(self):
        """api接口名称,GetClusters:获取集群cluster列表
GetSystemUsers:获取系统用户列表
CheckNodeCluster: 检查节点是否隶属一个cluster
GetClusterDatabases: 获取一个cluster下的数据库列表
GetClusterTables: 获取一个cluster下的数据库表列表
GetPrivilegeUsers: 获取授权的用户列表
GET_USER_CLUSTER_PRIVILEGES:获取用户cluster下的权限   
GetUserClusterNewPrivileges:获取用户cluster下的权限 (新版）
RevokeClusterUser:解绑cluster用户
DeleteSystemUser:删除系统用户 —— 必须所有cluster先解绑
GetUserOptionMessages:获取用户配置备注信息
GET_USER_CONFIGS:获取用户配置列表  QUOTA、PROFILE、POLICY
        :rtype: str
        """
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Cluster(self):
        """集群名称，GET_SYSTEM_USERS，GET_PRIVILEGE_USERS，GET_CLUSTER_DATABASES，GET_CLUSTER_TABLES 必填
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def UserName(self):
        """用户名称，api与user相关的必填
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserType(self):
        """账户的类型
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ApiType = params.get("ApiType")
        self._Cluster = params.get("Cluster")
        self._UserName = params.get("UserName")
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkSqlApisResponse(AbstractModel):
    """DescribeCkSqlApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnData: 返回的查询数据，大部分情况是list，也可能是bool
        :type ReturnData: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnData = None
        self._RequestId = None

    @property
    def ReturnData(self):
        """返回的查询数据，大部分情况是list，也可能是bool
        :rtype: str
        """
        return self._ReturnData

    @ReturnData.setter
    def ReturnData(self, ReturnData):
        self._ReturnData = ReturnData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnData = params.get("ReturnData")
        self._RequestId = params.get("RequestId")


class DescribeClusterConfigsRequest(AbstractModel):
    """DescribeClusterConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例ID
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
        


class DescribeClusterConfigsResponse(AbstractModel):
    """DescribeClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterConfList: 返回实例的配置文件相关的信息
        :type ClusterConfList: list of ClusterConfigsInfoFromEMR
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterConfList = None
        self._RequestId = None

    @property
    def ClusterConfList(self):
        """返回实例的配置文件相关的信息
        :rtype: list of ClusterConfigsInfoFromEMR
        """
        return self._ClusterConfList

    @ClusterConfList.setter
    def ClusterConfList(self, ClusterConfList):
        self._ClusterConfList = ClusterConfList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = params.get("RequestId")


class DescribeInstanceClustersRequest(AbstractModel):
    """DescribeInstanceClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        


class DescribeInstanceClustersResponse(AbstractModel):
    """DescribeInstanceClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Clusters: cluster列表
        :type Clusters: list of ClusterInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Clusters = None
        self._RequestId = None

    @property
    def Clusters(self):
        """cluster列表
        :rtype: list of ClusterInfo
        """
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceKeyValConfigsRequest(AbstractModel):
    """DescribeInstanceKeyValConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _SearchConfigName: 搜索的配置项名称
        :type SearchConfigName: str
        """
        self._InstanceId = None
        self._SearchConfigName = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchConfigName(self):
        """搜索的配置项名称
        :rtype: str
        """
        return self._SearchConfigName

    @SearchConfigName.setter
    def SearchConfigName(self, SearchConfigName):
        self._SearchConfigName = SearchConfigName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchConfigName = params.get("SearchConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceKeyValConfigsResponse(AbstractModel):
    """DescribeInstanceKeyValConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigItems: 参数列表
        :type ConfigItems: list of InstanceConfigInfo
        :param _UnConfigItems: 未配置的参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UnConfigItems: list of InstanceConfigInfo
        :param _MapConfigItems: 配置的多层级参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MapConfigItems: list of MapConfigItem
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigItems = None
        self._UnConfigItems = None
        self._MapConfigItems = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ConfigItems(self):
        """参数列表
        :rtype: list of InstanceConfigInfo
        """
        return self._ConfigItems

    @ConfigItems.setter
    def ConfigItems(self, ConfigItems):
        self._ConfigItems = ConfigItems

    @property
    def UnConfigItems(self):
        """未配置的参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceConfigInfo
        """
        return self._UnConfigItems

    @UnConfigItems.setter
    def UnConfigItems(self, UnConfigItems):
        self._UnConfigItems = UnConfigItems

    @property
    def MapConfigItems(self):
        """配置的多层级参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MapConfigItem
        """
        return self._MapConfigItems

    @MapConfigItems.setter
    def MapConfigItems(self, MapConfigItems):
        self._MapConfigItems = MapConfigItems

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigItems") is not None:
            self._ConfigItems = []
            for item in params.get("ConfigItems"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self._ConfigItems.append(obj)
        if params.get("UnConfigItems") is not None:
            self._UnConfigItems = []
            for item in params.get("UnConfigItems"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self._UnConfigItems.append(obj)
        if params.get("MapConfigItems") is not None:
            self._MapConfigItems = []
            for item in params.get("MapConfigItems"):
                obj = MapConfigItem()
                obj._deserialize(item)
                self._MapConfigItems.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _NodeRole: 集群角色类型，“DATA” 为数据节点、“COMMON” 为 ZooKeeper 节点，默认为 "DATA" 数据节点。
        :type NodeRole: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _DisplayPolicy: 展现策略，All时显示所有
        :type DisplayPolicy: str
        :param _ForceAll: 当true的时候返回所有节点，即Limit无限大
        :type ForceAll: bool
        """
        self._InstanceId = None
        self._NodeRole = None
        self._Offset = None
        self._Limit = None
        self._DisplayPolicy = None
        self._ForceAll = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeRole(self):
        """集群角色类型，“DATA” 为数据节点、“COMMON” 为 ZooKeeper 节点，默认为 "DATA" 数据节点。
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def Offset(self):
        """分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DisplayPolicy(self):
        """展现策略，All时显示所有
        :rtype: str
        """
        return self._DisplayPolicy

    @DisplayPolicy.setter
    def DisplayPolicy(self, DisplayPolicy):
        self._DisplayPolicy = DisplayPolicy

    @property
    def ForceAll(self):
        """当true的时候返回所有节点，即Limit无限大
        :rtype: bool
        """
        return self._ForceAll

    @ForceAll.setter
    def ForceAll(self, ForceAll):
        self._ForceAll = ForceAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeRole = params.get("NodeRole")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DisplayPolicy = params.get("DisplayPolicy")
        self._ForceAll = params.get("ForceAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    """DescribeInstanceNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _InstanceNodesList: 实例节点总数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNodesList: list of InstanceNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceNodesList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceNodesList(self):
        """实例节点总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNode
        """
        return self._InstanceNodesList

    @InstanceNodesList.setter
    def InstanceNodesList(self, InstanceNodesList):
        self._InstanceNodesList = InstanceNodesList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _IsOpenApi: 是否是open api查询
        :type IsOpenApi: bool
        """
        self._InstanceId = None
        self._IsOpenApi = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsOpenApi(self):
        """是否是open api查询
        :rtype: bool
        """
        return self._IsOpenApi

    @IsOpenApi.setter
    def IsOpenApi(self, IsOpenApi):
        self._IsOpenApi = IsOpenApi


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsOpenApi = params.get("IsOpenApi")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: 实例描述信息
        :type InstanceInfo: :class:`tencentcloud.cdwch.v20200915.models.InstanceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        """实例描述信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例ID
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
        


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceShardsList: 实例shard信息
        :type InstanceShardsList: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceShardsList = None
        self._RequestId = None

    @property
    def InstanceShardsList(self):
        """实例shard信息
        :rtype: str
        """
        return self._InstanceShardsList

    @InstanceShardsList.setter
    def InstanceShardsList(self, InstanceShardsList):
        self._InstanceShardsList = InstanceShardsList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceShardsList = params.get("InstanceShardsList")
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例名称
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例名称
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
    """DescribeInstanceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
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
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
        :type ProcessName: str
        :param _ProcessSubName: 当前步骤的名称，例如：”购买资源中“
        :type ProcessSubName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._ProcessSubName = None
        self._RequestId = None

    @property
    def InstanceState(self):
        """集群状态，例如：Serving
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """集群操作创建时间
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """集群操作名称
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """集群操作进度
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """集群状态描述，例如：运行中
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """集群流程错误信息，例如：“创建失败，资源不足”
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """当前步骤的名称，例如：”购买资源中“
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def ProcessSubName(self):
        """当前步骤的名称，例如：”购买资源中“
        :rtype: str
        """
        return self._ProcessSubName

    @ProcessSubName.setter
    def ProcessSubName(self, ProcessSubName):
        self._ProcessSubName = ProcessSubName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ProcessName = params.get("ProcessName")
        self._ProcessSubName = params.get("ProcessSubName")
        self._RequestId = params.get("RequestId")


class DescribeInstancesNewRequest(AbstractModel):
    """DescribeInstancesNew请求参数结构体

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
        :param _SearchTags: 搜索标签列表
        :type SearchTags: list of SearchTags
        :param _IsSimple: 信息详细与否
        :type IsSimple: bool
        :param _Vips: vip列表
        :type Vips: list of str
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None
        self._IsSimple = None
        self._Vips = None

    @property
    def SearchInstanceId(self):
        """搜索的集群id名称
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """搜索的集群name
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        """搜索标签列表
        :rtype: list of SearchTags
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags

    @property
    def IsSimple(self):
        """信息详细与否
        :rtype: bool
        """
        return self._IsSimple

    @IsSimple.setter
    def IsSimple(self, IsSimple):
        self._IsSimple = IsSimple

    @property
    def Vips(self):
        """vip列表
        :rtype: list of str
        """
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips


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
        self._IsSimple = params.get("IsSimple")
        self._Vips = params.get("Vips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesNewResponse(AbstractModel):
    """DescribeInstancesNew返回参数结构体

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
        """实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """实例数组
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeSpecRequest(AbstractModel):
    """DescribeSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 地域信息，例如"ap-guangzhou-1"
        :type Zone: str
        :param _PayMode: 计费类型，PREPAID 包年包月，POSTPAID_BY_HOUR 按量计费
        :type PayMode: str
        :param _IsElastic: 是否弹性ck
        :type IsElastic: bool
        :param _CaseType: 是否是购买页面需要的spec
        :type CaseType: int
        """
        self._Zone = None
        self._PayMode = None
        self._IsElastic = None
        self._CaseType = None

    @property
    def Zone(self):
        """地域信息，例如"ap-guangzhou-1"
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def PayMode(self):
        """计费类型，PREPAID 包年包月，POSTPAID_BY_HOUR 按量计费
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsElastic(self):
        """是否弹性ck
        :rtype: bool
        """
        return self._IsElastic

    @IsElastic.setter
    def IsElastic(self, IsElastic):
        self._IsElastic = IsElastic

    @property
    def CaseType(self):
        """是否是购买页面需要的spec
        :rtype: int
        """
        return self._CaseType

    @CaseType.setter
    def CaseType(self, CaseType):
        self._CaseType = CaseType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._PayMode = params.get("PayMode")
        self._IsElastic = params.get("IsElastic")
        self._CaseType = params.get("CaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecResponse(AbstractModel):
    """DescribeSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommonSpec: zookeeper节点规格描述
        :type CommonSpec: list of ResourceSpec
        :param _DataSpec: 数据节点规格描述
        :type DataSpec: list of ResourceSpec
        :param _AttachCBSSpec: 云盘列表
        :type AttachCBSSpec: list of DiskSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommonSpec = None
        self._DataSpec = None
        self._AttachCBSSpec = None
        self._RequestId = None

    @property
    def CommonSpec(self):
        """zookeeper节点规格描述
        :rtype: list of ResourceSpec
        """
        return self._CommonSpec

    @CommonSpec.setter
    def CommonSpec(self, CommonSpec):
        self._CommonSpec = CommonSpec

    @property
    def DataSpec(self):
        """数据节点规格描述
        :rtype: list of ResourceSpec
        """
        return self._DataSpec

    @DataSpec.setter
    def DataSpec(self, DataSpec):
        self._DataSpec = DataSpec

    @property
    def AttachCBSSpec(self):
        """云盘列表
        :rtype: list of DiskSpec
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CommonSpec") is not None:
            self._CommonSpec = []
            for item in params.get("CommonSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._CommonSpec.append(obj)
        if params.get("DataSpec") is not None:
            self._DataSpec = []
            for item in params.get("DataSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._DataSpec.append(obj)
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = []
            for item in params.get("AttachCBSSpec"):
                obj = DiskSpec()
                obj._deserialize(item)
                self._AttachCBSSpec.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyInstanceRequest(AbstractModel):
    """DestroyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群id
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
    """DestroyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowID: 作业id
        :type FlowID: str
        :param _InstanceID: 集群id
        :type InstanceID: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowID = None
        self._InstanceID = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowID(self):
        """作业id
        :rtype: str
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID

    @property
    def InstanceID(self):
        """集群id
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowID = params.get("FlowID")
        self._InstanceID = params.get("InstanceID")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpec(AbstractModel):
    """磁盘规格描述

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
        """磁盘类型，例如“CLOUD_SSD", "LOCAL_SSD"等
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """磁盘类型说明，例如"云SSD", "本地SSD"等
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def MinDiskSize(self):
        """磁盘最小规格大小，单位G
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        """磁盘最大规格大小，单位G
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def DiskCount(self):
        """磁盘数目
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
        


class GroupInfo(AbstractModel):
    """集群分组信息描述

    """

    def __init__(self):
        r"""
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _ShardName: 分片变量名称
        :type ShardName: str
        :param _ReplicaName: 副本变量名称
        :type ReplicaName: str
        """
        self._GroupName = None
        self._ShardName = None
        self._ReplicaName = None

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ShardName(self):
        """分片变量名称
        :rtype: str
        """
        return self._ShardName

    @ShardName.setter
    def ShardName(self, ShardName):
        self._ShardName = ShardName

    @property
    def ReplicaName(self):
        """副本变量名称
        :rtype: str
        """
        return self._ReplicaName

    @ReplicaName.setter
    def ReplicaName(self, ReplicaName):
        self._ReplicaName = ReplicaName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._ShardName = params.get("ShardName")
        self._ReplicaName = params.get("ReplicaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigInfo(AbstractModel):
    """集群配置信息

    """

    def __init__(self):
        r"""
        :param _ConfKey: 配置项名称
        :type ConfKey: str
        :param _ConfValue: 配置项内容
        :type ConfValue: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _NeedRestart: 是否需要重启
        :type NeedRestart: bool
        :param _Editable: 是否可编辑
        :type Editable: bool
        :param _ConfDesc: 配置项解释
        :type ConfDesc: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _ModifyRuleType: 规则名称类型
        :type ModifyRuleType: str
        :param _ModifyRuleValue: 规则名称内容
        :type ModifyRuleValue: str
        :param _Uin: 修改人的uin
        :type Uin: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._ConfKey = None
        self._ConfValue = None
        self._DefaultValue = None
        self._NeedRestart = None
        self._Editable = None
        self._ConfDesc = None
        self._FileName = None
        self._ModifyRuleType = None
        self._ModifyRuleValue = None
        self._Uin = None
        self._ModifyTime = None

    @property
    def ConfKey(self):
        """配置项名称
        :rtype: str
        """
        return self._ConfKey

    @ConfKey.setter
    def ConfKey(self, ConfKey):
        self._ConfKey = ConfKey

    @property
    def ConfValue(self):
        """配置项内容
        :rtype: str
        """
        return self._ConfValue

    @ConfValue.setter
    def ConfValue(self, ConfValue):
        self._ConfValue = ConfValue

    @property
    def DefaultValue(self):
        """默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def NeedRestart(self):
        """是否需要重启
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def Editable(self):
        """是否可编辑
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def ConfDesc(self):
        """配置项解释
        :rtype: str
        """
        return self._ConfDesc

    @ConfDesc.setter
    def ConfDesc(self, ConfDesc):
        self._ConfDesc = ConfDesc

    @property
    def FileName(self):
        """文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ModifyRuleType(self):
        """规则名称类型
        :rtype: str
        """
        return self._ModifyRuleType

    @ModifyRuleType.setter
    def ModifyRuleType(self, ModifyRuleType):
        self._ModifyRuleType = ModifyRuleType

    @property
    def ModifyRuleValue(self):
        """规则名称内容
        :rtype: str
        """
        return self._ModifyRuleValue

    @ModifyRuleValue.setter
    def ModifyRuleValue(self, ModifyRuleValue):
        self._ModifyRuleValue = ModifyRuleValue

    @property
    def Uin(self):
        """修改人的uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ConfKey = params.get("ConfKey")
        self._ConfValue = params.get("ConfValue")
        self._DefaultValue = params.get("DefaultValue")
        self._NeedRestart = params.get("NeedRestart")
        self._Editable = params.get("Editable")
        self._ConfDesc = params.get("ConfDesc")
        self._FileName = params.get("FileName")
        self._ModifyRuleType = params.get("ModifyRuleType")
        self._ModifyRuleValue = params.get("ModifyRuleValue")
        self._Uin = params.get("Uin")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigItem(AbstractModel):
    """KV配置

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
        """key
        :rtype: str
        """
        return self._ConfKey

    @ConfKey.setter
    def ConfKey(self, ConfKey):
        self._ConfKey = ConfKey

    @property
    def ConfValue(self):
        """value
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
    """Instance表detail字段

    """

    def __init__(self):
        r"""
        :param _EnableAlarmStrategy: 告警策略是否可用
        :type EnableAlarmStrategy: bool
        """
        self._EnableAlarmStrategy = None

    @property
    def EnableAlarmStrategy(self):
        """告警策略是否可用
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
    """实例描述信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID, "cdw-xxxx" 字符串类型
        :type InstanceId: str
        :param _InstanceName: 集群实例名称
        :type InstanceName: str
        :param _Status: 状态,
Init 创建中; Serving 运行中； 
Deleted已销毁；Deleting 销毁中；
Modify 集群变更中；
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
        :type MasterSummary: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        :param _CommonSummary: zookeeper节点描述信息
        :type CommonSummary: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        :param _HA: 高可用，“true" "false"
        :type HA: str
        :param _AccessInfo: 访问地址，例如 "10.0.0.1:9000"
        :type AccessInfo: str
        :param _Id: 记录ID，数值型
        :type Id: int
        :param _RegionId: regionId, 表示地域
        :type RegionId: int
        :param _ZoneDesc: 可用区说明，例如 "广州二区"
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
        :param _IsElastic: 是否弹性ck
        :type IsElastic: bool
        :param _InstanceStateInfo: 集群详细状态
        :type InstanceStateInfo: :class:`tencentcloud.cdwch.v20200915.models.InstanceStateInfo`
        :param _HAZk: ZK高可用
        :type HAZk: bool
        :param _MountDiskType: 挂载盘,默认0:没有类型；1:裸盘;2:lvm
        :type MountDiskType: int
        :param _CHProxyVip: chproxy连接ip
        :type CHProxyVip: str
        :param _CosBucketName: cos buket的名字
        :type CosBucketName: str
        :param _CanAttachCbs: 是否可以挂载云盘
        :type CanAttachCbs: bool
        :param _CanAttachCbsLvm: 是否可以挂载云盘阵列
        :type CanAttachCbsLvm: bool
        :param _CanAttachCos: 是否可以挂载cos
        :type CanAttachCos: bool
        :param _Components: 服务信息
        :type Components: list of ServiceInfo
        :param _UpgradeVersions: 可升级的内核版本
        :type UpgradeVersions: str
        :param _EsIndexId: ex-index
        :type EsIndexId: str
        :param _EsIndexUsername: username
        :type EsIndexUsername: str
        :param _EsIndexPassword: password
        :type EsIndexPassword: str
        :param _HasEsIndex: true
        :type HasEsIndex: bool
        :param _IsSecondaryZone: true
        :type IsSecondaryZone: bool
        :param _SecondaryZoneInfo: desc
        :type SecondaryZoneInfo: str
        :param _ClickHouseKeeper: 是否clickhouse-keeper
        :type ClickHouseKeeper: bool
        :param _Details: 实例扩展信息
        :type Details: :class:`tencentcloud.cdwch.v20200915.models.InstanceDetail`
        :param _IsWhiteSGs: 安全组白名单
        :type IsWhiteSGs: bool
        :param _BindSGs: 绑定的安全组
        :type BindSGs: list of str
        :param _HasPublicCloudClb: 是否开启公网clb
        :type HasPublicCloudClb: bool
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
        self._CommonSummary = None
        self._HA = None
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
        self._IsElastic = None
        self._InstanceStateInfo = None
        self._HAZk = None
        self._MountDiskType = None
        self._CHProxyVip = None
        self._CosBucketName = None
        self._CanAttachCbs = None
        self._CanAttachCbsLvm = None
        self._CanAttachCos = None
        self._Components = None
        self._UpgradeVersions = None
        self._EsIndexId = None
        self._EsIndexUsername = None
        self._EsIndexPassword = None
        self._HasEsIndex = None
        self._IsSecondaryZone = None
        self._SecondaryZoneInfo = None
        self._ClickHouseKeeper = None
        self._Details = None
        self._IsWhiteSGs = None
        self._BindSGs = None
        self._HasPublicCloudClb = None

    @property
    def InstanceId(self):
        """集群实例ID, "cdw-xxxx" 字符串类型
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """状态,
Init 创建中; Serving 运行中； 
Deleted已销毁；Deleting 销毁中；
Modify 集群变更中；
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        """版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """地域, ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """可用区， ap-guangzhou-3
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """私有网络名称
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网名称
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        """付费类型，"hour", "prepay"
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def MasterSummary(self):
        """数据节点描述信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        """
        return self._MasterSummary

    @MasterSummary.setter
    def MasterSummary(self, MasterSummary):
        self._MasterSummary = MasterSummary

    @property
    def CommonSummary(self):
        """zookeeper节点描述信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        """
        return self._CommonSummary

    @CommonSummary.setter
    def CommonSummary(self, CommonSummary):
        self._CommonSummary = CommonSummary

    @property
    def HA(self):
        """高可用，“true" "false"
        :rtype: str
        """
        return self._HA

    @HA.setter
    def HA(self, HA):
        self._HA = HA

    @property
    def AccessInfo(self):
        """访问地址，例如 "10.0.0.1:9000"
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def Id(self):
        """记录ID，数值型
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionId(self):
        """regionId, 表示地域
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneDesc(self):
        """可用区说明，例如 "广州二区"
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def FlowMsg(self):
        """错误流程说明信息
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def StatusDesc(self):
        """状态描述，例如“运行中”等
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RenewFlag(self):
        """自动续费标记
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Monitor(self):
        """监控信息
        :rtype: str
        """
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor):
        self._Monitor = Monitor

    @property
    def HasClsTopic(self):
        """是否开通日志
        :rtype: bool
        """
        return self._HasClsTopic

    @HasClsTopic.setter
    def HasClsTopic(self, HasClsTopic):
        self._HasClsTopic = HasClsTopic

    @property
    def ClsTopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def ClsLogSetId(self):
        """日志集ID
        :rtype: str
        """
        return self._ClsLogSetId

    @ClsLogSetId.setter
    def ClsLogSetId(self, ClsLogSetId):
        self._ClsLogSetId = ClsLogSetId

    @property
    def EnableXMLConfig(self):
        """是否支持xml配置管理
        :rtype: int
        """
        return self._EnableXMLConfig

    @EnableXMLConfig.setter
    def EnableXMLConfig(self, EnableXMLConfig):
        self._EnableXMLConfig = EnableXMLConfig

    @property
    def RegionDesc(self):
        """区域
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Eip(self):
        """弹性网卡地址
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CosMoveFactor(self):
        """冷热分层系数
        :rtype: int
        """
        return self._CosMoveFactor

    @CosMoveFactor.setter
    def CosMoveFactor(self, CosMoveFactor):
        self._CosMoveFactor = CosMoveFactor

    @property
    def Kind(self):
        """external/local/yunti
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def IsElastic(self):
        """是否弹性ck
        :rtype: bool
        """
        return self._IsElastic

    @IsElastic.setter
    def IsElastic(self, IsElastic):
        self._IsElastic = IsElastic

    @property
    def InstanceStateInfo(self):
        """集群详细状态
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.InstanceStateInfo`
        """
        return self._InstanceStateInfo

    @InstanceStateInfo.setter
    def InstanceStateInfo(self, InstanceStateInfo):
        self._InstanceStateInfo = InstanceStateInfo

    @property
    def HAZk(self):
        """ZK高可用
        :rtype: bool
        """
        return self._HAZk

    @HAZk.setter
    def HAZk(self, HAZk):
        self._HAZk = HAZk

    @property
    def MountDiskType(self):
        """挂载盘,默认0:没有类型；1:裸盘;2:lvm
        :rtype: int
        """
        return self._MountDiskType

    @MountDiskType.setter
    def MountDiskType(self, MountDiskType):
        self._MountDiskType = MountDiskType

    @property
    def CHProxyVip(self):
        """chproxy连接ip
        :rtype: str
        """
        return self._CHProxyVip

    @CHProxyVip.setter
    def CHProxyVip(self, CHProxyVip):
        self._CHProxyVip = CHProxyVip

    @property
    def CosBucketName(self):
        """cos buket的名字
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CanAttachCbs(self):
        """是否可以挂载云盘
        :rtype: bool
        """
        return self._CanAttachCbs

    @CanAttachCbs.setter
    def CanAttachCbs(self, CanAttachCbs):
        self._CanAttachCbs = CanAttachCbs

    @property
    def CanAttachCbsLvm(self):
        """是否可以挂载云盘阵列
        :rtype: bool
        """
        return self._CanAttachCbsLvm

    @CanAttachCbsLvm.setter
    def CanAttachCbsLvm(self, CanAttachCbsLvm):
        self._CanAttachCbsLvm = CanAttachCbsLvm

    @property
    def CanAttachCos(self):
        """是否可以挂载cos
        :rtype: bool
        """
        return self._CanAttachCos

    @CanAttachCos.setter
    def CanAttachCos(self, CanAttachCos):
        self._CanAttachCos = CanAttachCos

    @property
    def Components(self):
        """服务信息
        :rtype: list of ServiceInfo
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def UpgradeVersions(self):
        """可升级的内核版本
        :rtype: str
        """
        return self._UpgradeVersions

    @UpgradeVersions.setter
    def UpgradeVersions(self, UpgradeVersions):
        self._UpgradeVersions = UpgradeVersions

    @property
    def EsIndexId(self):
        """ex-index
        :rtype: str
        """
        return self._EsIndexId

    @EsIndexId.setter
    def EsIndexId(self, EsIndexId):
        self._EsIndexId = EsIndexId

    @property
    def EsIndexUsername(self):
        """username
        :rtype: str
        """
        return self._EsIndexUsername

    @EsIndexUsername.setter
    def EsIndexUsername(self, EsIndexUsername):
        self._EsIndexUsername = EsIndexUsername

    @property
    def EsIndexPassword(self):
        """password
        :rtype: str
        """
        return self._EsIndexPassword

    @EsIndexPassword.setter
    def EsIndexPassword(self, EsIndexPassword):
        self._EsIndexPassword = EsIndexPassword

    @property
    def HasEsIndex(self):
        """true
        :rtype: bool
        """
        return self._HasEsIndex

    @HasEsIndex.setter
    def HasEsIndex(self, HasEsIndex):
        self._HasEsIndex = HasEsIndex

    @property
    def IsSecondaryZone(self):
        """true
        :rtype: bool
        """
        return self._IsSecondaryZone

    @IsSecondaryZone.setter
    def IsSecondaryZone(self, IsSecondaryZone):
        self._IsSecondaryZone = IsSecondaryZone

    @property
    def SecondaryZoneInfo(self):
        """desc
        :rtype: str
        """
        return self._SecondaryZoneInfo

    @SecondaryZoneInfo.setter
    def SecondaryZoneInfo(self, SecondaryZoneInfo):
        self._SecondaryZoneInfo = SecondaryZoneInfo

    @property
    def ClickHouseKeeper(self):
        """是否clickhouse-keeper
        :rtype: bool
        """
        return self._ClickHouseKeeper

    @ClickHouseKeeper.setter
    def ClickHouseKeeper(self, ClickHouseKeeper):
        self._ClickHouseKeeper = ClickHouseKeeper

    @property
    def Details(self):
        """实例扩展信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.InstanceDetail`
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def IsWhiteSGs(self):
        """安全组白名单
        :rtype: bool
        """
        return self._IsWhiteSGs

    @IsWhiteSGs.setter
    def IsWhiteSGs(self, IsWhiteSGs):
        self._IsWhiteSGs = IsWhiteSGs

    @property
    def BindSGs(self):
        """绑定的安全组
        :rtype: list of str
        """
        return self._BindSGs

    @BindSGs.setter
    def BindSGs(self, BindSGs):
        self._BindSGs = BindSGs

    @property
    def HasPublicCloudClb(self):
        """是否开启公网clb
        :rtype: bool
        """
        return self._HasPublicCloudClb

    @HasPublicCloudClb.setter
    def HasPublicCloudClb(self, HasPublicCloudClb):
        self._HasPublicCloudClb = HasPublicCloudClb


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
        if params.get("CommonSummary") is not None:
            self._CommonSummary = NodesSummary()
            self._CommonSummary._deserialize(params.get("CommonSummary"))
        self._HA = params.get("HA")
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
        self._IsElastic = params.get("IsElastic")
        if params.get("InstanceStateInfo") is not None:
            self._InstanceStateInfo = InstanceStateInfo()
            self._InstanceStateInfo._deserialize(params.get("InstanceStateInfo"))
        self._HAZk = params.get("HAZk")
        self._MountDiskType = params.get("MountDiskType")
        self._CHProxyVip = params.get("CHProxyVip")
        self._CosBucketName = params.get("CosBucketName")
        self._CanAttachCbs = params.get("CanAttachCbs")
        self._CanAttachCbsLvm = params.get("CanAttachCbsLvm")
        self._CanAttachCos = params.get("CanAttachCos")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = ServiceInfo()
                obj._deserialize(item)
                self._Components.append(obj)
        self._UpgradeVersions = params.get("UpgradeVersions")
        self._EsIndexId = params.get("EsIndexId")
        self._EsIndexUsername = params.get("EsIndexUsername")
        self._EsIndexPassword = params.get("EsIndexPassword")
        self._HasEsIndex = params.get("HasEsIndex")
        self._IsSecondaryZone = params.get("IsSecondaryZone")
        self._SecondaryZoneInfo = params.get("SecondaryZoneInfo")
        self._ClickHouseKeeper = params.get("ClickHouseKeeper")
        if params.get("Details") is not None:
            self._Details = InstanceDetail()
            self._Details._deserialize(params.get("Details"))
        self._IsWhiteSGs = params.get("IsWhiteSGs")
        self._BindSGs = params.get("BindSGs")
        self._HasPublicCloudClb = params.get("HasPublicCloudClb")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """实例节点描述信息

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
        :param _Cluster: 所属clickhouse cluster名称
        :type Cluster: str
        :param _NodeGroups: 节点所属的分组信息
        :type NodeGroups: list of GroupInfo
        :param _Rip: VPC IP
        :type Rip: str
        :param _IsCHProxy: ture的时候表示该节点上部署了chproxy进程
        :type IsCHProxy: bool
        :param _Status: 节点状态
        :type Status: str
        :param _UUID: 节点uuid
        :type UUID: str
        :param _Zone: 区
        :type Zone: str
        :param _ZoneDesc: 区描述
        :type ZoneDesc: str
        :param _RealResourceId: 真实资源id
        :type RealResourceId: str
        """
        self._Ip = None
        self._Spec = None
        self._Core = None
        self._Memory = None
        self._DiskType = None
        self._DiskSize = None
        self._Cluster = None
        self._NodeGroups = None
        self._Rip = None
        self._IsCHProxy = None
        self._Status = None
        self._UUID = None
        self._Zone = None
        self._ZoneDesc = None
        self._RealResourceId = None

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Spec(self):
        """机型，如 S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Core(self):
        """cpu核数
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        """内存大小
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskType(self):
        """磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """磁盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Cluster(self):
        """所属clickhouse cluster名称
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def NodeGroups(self):
        """节点所属的分组信息
        :rtype: list of GroupInfo
        """
        return self._NodeGroups

    @NodeGroups.setter
    def NodeGroups(self, NodeGroups):
        self._NodeGroups = NodeGroups

    @property
    def Rip(self):
        """VPC IP
        :rtype: str
        """
        return self._Rip

    @Rip.setter
    def Rip(self, Rip):
        self._Rip = Rip

    @property
    def IsCHProxy(self):
        """ture的时候表示该节点上部署了chproxy进程
        :rtype: bool
        """
        return self._IsCHProxy

    @IsCHProxy.setter
    def IsCHProxy(self, IsCHProxy):
        self._IsCHProxy = IsCHProxy

    @property
    def Status(self):
        """节点状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UUID(self):
        """节点uuid
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def Zone(self):
        """区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneDesc(self):
        """区描述
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def RealResourceId(self):
        """真实资源id
        :rtype: str
        """
        return self._RealResourceId

    @RealResourceId.setter
    def RealResourceId(self, RealResourceId):
        self._RealResourceId = RealResourceId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Spec = params.get("Spec")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Cluster = params.get("Cluster")
        if params.get("NodeGroups") is not None:
            self._NodeGroups = []
            for item in params.get("NodeGroups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._NodeGroups.append(obj)
        self._Rip = params.get("Rip")
        self._IsCHProxy = params.get("IsCHProxy")
        self._Status = params.get("Status")
        self._UUID = params.get("UUID")
        self._Zone = params.get("Zone")
        self._ZoneDesc = params.get("ZoneDesc")
        self._RealResourceId = params.get("RealResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStateInfo(AbstractModel):
    """集群状态抽象后的结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
        :type FlowProgress: int
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
        :type FlowMsg: str
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
        :type ProcessName: str
        :param _RequestId: 请求id
        :type RequestId: str
        :param _ProcessSubName: 流程的二级名称
        :type ProcessSubName: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._RequestId = None
        self._ProcessSubName = None

    @property
    def InstanceState(self):
        """集群状态，例如：Serving
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """集群操作创建时间
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """集群操作名称
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """集群操作进度
        :rtype: int
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """集群状态描述，例如：运行中
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """集群流程错误信息，例如：“创建失败，资源不足”
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """当前步骤的名称，例如：”购买资源中“
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def RequestId(self):
        """请求id
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def ProcessSubName(self):
        """流程的二级名称
        :rtype: str
        """
        return self._ProcessSubName

    @ProcessSubName.setter
    def ProcessSubName(self, ProcessSubName):
        self._ProcessSubName = ProcessSubName


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._RequestId = params.get("RequestId")
        self._ProcessSubName = params.get("ProcessSubName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MapConfigItem(AbstractModel):
    """kv配置，多层级item

    """

    def __init__(self):
        r"""
        :param _ConfKey: key
        :type ConfKey: str
        :param _Items: 列表
        :type Items: list of InstanceConfigInfo
        """
        self._ConfKey = None
        self._Items = None

    @property
    def ConfKey(self):
        """key
        :rtype: str
        """
        return self._ConfKey

    @ConfKey.setter
    def ConfKey(self, ConfKey):
        self._ConfKey = ConfKey

    @property
    def Items(self):
        """列表
        :rtype: list of InstanceConfigInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._ConfKey = params.get("ConfKey")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsRequest(AbstractModel):
    """ModifyClusterConfigs请求参数结构体

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
        """集群ID，例如cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyConfContext(self):
        """配置文件修改信息
        :rtype: list of ConfigSubmitContext
        """
        return self._ModifyConfContext

    @ModifyConfContext.setter
    def ModifyConfContext(self, ModifyConfContext):
        self._ModifyConfContext = ModifyConfContext

    @property
    def Remark(self):
        """修改原因
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
    """ModifyClusterConfigs返回参数结构体

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
        """流程相关信息
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstanceKeyValConfigsRequest(AbstractModel):
    """ModifyInstanceKeyValConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AddItems: 新增配置列表
        :type AddItems: list of InstanceConfigItem
        :param _UpdateItems: 更新配置列表
        :type UpdateItems: list of InstanceConfigItem
        :param _DeleteItems: 删除配置列表
        :type DeleteItems: :class:`tencentcloud.cdwch.v20200915.models.InstanceConfigItem`
        :param _DelItems: 删除配置列表
        :type DelItems: list of InstanceConfigItem
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._AddItems = None
        self._UpdateItems = None
        self._DeleteItems = None
        self._DelItems = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddItems(self):
        """新增配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._AddItems

    @AddItems.setter
    def AddItems(self, AddItems):
        self._AddItems = AddItems

    @property
    def UpdateItems(self):
        """更新配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._UpdateItems

    @UpdateItems.setter
    def UpdateItems(self, UpdateItems):
        self._UpdateItems = UpdateItems

    @property
    def DeleteItems(self):
        """删除配置列表
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.InstanceConfigItem`
        """
        return self._DeleteItems

    @DeleteItems.setter
    def DeleteItems(self, DeleteItems):
        self._DeleteItems = DeleteItems

    @property
    def DelItems(self):
        """删除配置列表
        :rtype: list of InstanceConfigItem
        """
        return self._DelItems

    @DelItems.setter
    def DelItems(self, DelItems):
        self._DelItems = DelItems

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
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
        if params.get("DeleteItems") is not None:
            self._DeleteItems = InstanceConfigItem()
            self._DeleteItems._deserialize(params.get("DeleteItems"))
        if params.get("DelItems") is not None:
            self._DelItems = []
            for item in params.get("DelItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._DelItems.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceKeyValConfigsResponse(AbstractModel):
    """ModifyInstanceKeyValConfigs返回参数结构体

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
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def FlowId(self):
        """ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyUserNewPrivilegeRequest(AbstractModel):
    """ModifyUserNewPrivilege请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Cluster: cluster名称
        :type Cluster: str
        :param _UserName: 用户名
        :type UserName: str
        :param _AllDatabase: 是否所有数据库表
        :type AllDatabase: bool
        :param _GlobalPrivileges: 全局权限
        :type GlobalPrivileges: list of str
        :param _DatabasePrivilegeList: 数据库表权限
        :type DatabasePrivilegeList: list of DatabasePrivilegeInfo
        """
        self._InstanceId = None
        self._Cluster = None
        self._UserName = None
        self._AllDatabase = None
        self._GlobalPrivileges = None
        self._DatabasePrivilegeList = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cluster(self):
        """cluster名称
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AllDatabase(self):
        """是否所有数据库表
        :rtype: bool
        """
        return self._AllDatabase

    @AllDatabase.setter
    def AllDatabase(self, AllDatabase):
        self._AllDatabase = AllDatabase

    @property
    def GlobalPrivileges(self):
        """全局权限
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivilegeList(self):
        """数据库表权限
        :rtype: list of DatabasePrivilegeInfo
        """
        return self._DatabasePrivilegeList

    @DatabasePrivilegeList.setter
    def DatabasePrivilegeList(self, DatabasePrivilegeList):
        self._DatabasePrivilegeList = DatabasePrivilegeList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cluster = params.get("Cluster")
        self._UserName = params.get("UserName")
        self._AllDatabase = params.get("AllDatabase")
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivilegeList") is not None:
            self._DatabasePrivilegeList = []
            for item in params.get("DatabasePrivilegeList"):
                obj = DatabasePrivilegeInfo()
                obj._deserialize(item)
                self._DatabasePrivilegeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserNewPrivilegeResponse(AbstractModel):
    """ModifyUserNewPrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NodeSpec(AbstractModel):
    """创建集群时的规格

    """

    def __init__(self):
        r"""
        :param _SpecName: 规格名称
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
        """规格名称
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSize(self):
        """云盘大小
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
        


class NodesSummary(AbstractModel):
    """节点角色描述信息

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
        :type AttachCBSSpec: :class:`tencentcloud.cdwch.v20200915.models.AttachCBSSpec`
        :param _SubProductType: 子产品类型
        :type SubProductType: str
        :param _SpecCore: 规格对应的核数
        :type SpecCore: int
        :param _SpecMemory: 规格对应的内存大小
        :type SpecMemory: int
        :param _DiskCount: 磁盘的数量
        :type DiskCount: int
        :param _MaxDiskSize: 磁盘的最大大小
        :type MaxDiskSize: int
        :param _Encrypt: 是否为加密云盘
        :type Encrypt: int
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
        self._MaxDiskSize = None
        self._Encrypt = None

    @property
    def Spec(self):
        """机型，如 S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def NodeSize(self):
        """节点数目
        :rtype: int
        """
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize

    @property
    def Core(self):
        """cpu核数，单位个
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        """内存大小，单位G
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        """磁盘大小，单位G
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def DiskType(self):
        """磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """磁盘描述
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def AttachCBSSpec(self):
        """挂载云盘信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.AttachCBSSpec`
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def SubProductType(self):
        """子产品类型
        :rtype: str
        """
        return self._SubProductType

    @SubProductType.setter
    def SubProductType(self, SubProductType):
        self._SubProductType = SubProductType

    @property
    def SpecCore(self):
        """规格对应的核数
        :rtype: int
        """
        return self._SpecCore

    @SpecCore.setter
    def SpecCore(self, SpecCore):
        self._SpecCore = SpecCore

    @property
    def SpecMemory(self):
        """规格对应的内存大小
        :rtype: int
        """
        return self._SpecMemory

    @SpecMemory.setter
    def SpecMemory(self, SpecMemory):
        self._SpecMemory = SpecMemory

    @property
    def DiskCount(self):
        """磁盘的数量
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def MaxDiskSize(self):
        """磁盘的最大大小
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def Encrypt(self):
        """是否为加密云盘
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt


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
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBackUpRequest(AbstractModel):
    """OpenBackUp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _OperationType: OPEN 或者CLOSE
        :type OperationType: str
        :param _CosBucketName: 桶名字
        :type CosBucketName: str
        """
        self._InstanceId = None
        self._OperationType = None
        self._CosBucketName = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OperationType(self):
        """OPEN 或者CLOSE
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def CosBucketName(self):
        """桶名字
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OperationType = params.get("OperationType")
        self._CosBucketName = params.get("CosBucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBackUpResponse(AbstractModel):
    """OpenBackUp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RecoverBackUpJobRequest(AbstractModel):
    """RecoverBackUpJob请求参数结构体

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
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """任务id
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
        


class RecoverBackUpJobResponse(AbstractModel):
    """RecoverBackUpJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _InstanceId: 实例唯一ID
        :type InstanceId: str
        :param _Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param _DiskSize: 磁盘扩容后容量，不能小于原有用量。clickhouse最小200，且为100的整数倍。 zk最小100，且为10的整数倍；
        :type DiskSize: int
        """
        self._InstanceId = None
        self._Type = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        """实例唯一ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskSize(self):
        """磁盘扩容后容量，不能小于原有用量。clickhouse最小200，且为100的整数倍。 zk最小100，且为10的整数倍；
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
    """ResizeDisk返回参数结构体

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
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResourceSpec(AbstractModel):
    """资源规格描述信息

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
        :type SystemDisk: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        :param _DataDisk: 数据盘描述信息
        :type DataDisk: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        :param _MaxNodeSize: 最大节点数目限制
        :type MaxNodeSize: int
        :param _Available: 是否可用，false代表售罄
        :type Available: bool
        :param _ComputeSpecDesc: 规格描述信息
        :type ComputeSpecDesc: str
        :param _DisplayName: 规格名
        :type DisplayName: str
        :param _InstanceQuota: 库存数
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
        self._DisplayName = None
        self._InstanceQuota = None

    @property
    def Name(self):
        """规格名称，例如“SCH1"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cpu(self):
        """cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """内存大小，单位G
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Type(self):
        """分类标记，STANDARD/BIGDATA/HIGHIO分别表示标准型/大数据型/高IO
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SystemDisk(self):
        """系统盘描述信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisk(self):
        """数据盘描述信息
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def MaxNodeSize(self):
        """最大节点数目限制
        :rtype: int
        """
        return self._MaxNodeSize

    @MaxNodeSize.setter
    def MaxNodeSize(self, MaxNodeSize):
        self._MaxNodeSize = MaxNodeSize

    @property
    def Available(self):
        """是否可用，false代表售罄
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def ComputeSpecDesc(self):
        """规格描述信息
        :rtype: str
        """
        return self._ComputeSpecDesc

    @ComputeSpecDesc.setter
    def ComputeSpecDesc(self, ComputeSpecDesc):
        self._ComputeSpecDesc = ComputeSpecDesc

    @property
    def DisplayName(self):
        """规格名
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def InstanceQuota(self):
        """库存数
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
        self._DisplayName = params.get("DisplayName")
        self._InstanceQuota = params.get("InstanceQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleCNOutUpInstanceRequest(AbstractModel):
    """ScaleCNOutUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一ID
        :type InstanceId: str
        :param _VirtualCluster: warehouse名称
        :type VirtualCluster: str
        :param _UserSubnetID: 子网id
        :type UserSubnetID: str
        :param _NewCount: 新的warehouse的个数
        :type NewCount: int
        :param _NewSpecName: 集群的规格2X-Small、X-Small、Small
        :type NewSpecName: str
        """
        self._InstanceId = None
        self._VirtualCluster = None
        self._UserSubnetID = None
        self._NewCount = None
        self._NewSpecName = None

    @property
    def InstanceId(self):
        """实例唯一ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualCluster(self):
        """warehouse名称
        :rtype: str
        """
        return self._VirtualCluster

    @VirtualCluster.setter
    def VirtualCluster(self, VirtualCluster):
        self._VirtualCluster = VirtualCluster

    @property
    def UserSubnetID(self):
        """子网id
        :rtype: str
        """
        return self._UserSubnetID

    @UserSubnetID.setter
    def UserSubnetID(self, UserSubnetID):
        self._UserSubnetID = UserSubnetID

    @property
    def NewCount(self):
        """新的warehouse的个数
        :rtype: int
        """
        return self._NewCount

    @NewCount.setter
    def NewCount(self, NewCount):
        self._NewCount = NewCount

    @property
    def NewSpecName(self):
        """集群的规格2X-Small、X-Small、Small
        :rtype: str
        """
        return self._NewSpecName

    @NewSpecName.setter
    def NewSpecName(self, NewSpecName):
        self._NewSpecName = NewSpecName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualCluster = params.get("VirtualCluster")
        self._UserSubnetID = params.get("UserSubnetID")
        self._NewCount = params.get("NewCount")
        self._NewSpecName = params.get("NewSpecName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleCNOutUpInstanceResponse(AbstractModel):
    """ScaleCNOutUpInstance返回参数结构体

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
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一ID
        :type InstanceId: str
        :param _Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param _NodeCount: 调整clickhouse节点数量
        :type NodeCount: int
        :param _ScaleOutCluster: v_cluster分组，	
新增扩容节点将加入到已选择的v_cluster分组中，提交同步VIP生效.
        :type ScaleOutCluster: str
        :param _UserSubnetIPNum: 子网剩余ip数量，用于判断当前实例子网剩余ip数是否能扩容。需要根据实际填写
        :type UserSubnetIPNum: int
        :param _ScaleOutNodeIp: 同步元数据节点IP （uip），扩容的时候必填
        :type ScaleOutNodeIp: str
        :param _ReduceShardInfo: 缩容节点shard的节点IP （uip），其中ha集群需要主副节点ip都传入以逗号分隔，缩容的时候必填
        :type ReduceShardInfo: list of str
        """
        self._InstanceId = None
        self._Type = None
        self._NodeCount = None
        self._ScaleOutCluster = None
        self._UserSubnetIPNum = None
        self._ScaleOutNodeIp = None
        self._ReduceShardInfo = None

    @property
    def InstanceId(self):
        """实例唯一ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeCount(self):
        """调整clickhouse节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ScaleOutCluster(self):
        """v_cluster分组，	
新增扩容节点将加入到已选择的v_cluster分组中，提交同步VIP生效.
        :rtype: str
        """
        return self._ScaleOutCluster

    @ScaleOutCluster.setter
    def ScaleOutCluster(self, ScaleOutCluster):
        self._ScaleOutCluster = ScaleOutCluster

    @property
    def UserSubnetIPNum(self):
        """子网剩余ip数量，用于判断当前实例子网剩余ip数是否能扩容。需要根据实际填写
        :rtype: int
        """
        return self._UserSubnetIPNum

    @UserSubnetIPNum.setter
    def UserSubnetIPNum(self, UserSubnetIPNum):
        self._UserSubnetIPNum = UserSubnetIPNum

    @property
    def ScaleOutNodeIp(self):
        """同步元数据节点IP （uip），扩容的时候必填
        :rtype: str
        """
        return self._ScaleOutNodeIp

    @ScaleOutNodeIp.setter
    def ScaleOutNodeIp(self, ScaleOutNodeIp):
        self._ScaleOutNodeIp = ScaleOutNodeIp

    @property
    def ReduceShardInfo(self):
        """缩容节点shard的节点IP （uip），其中ha集群需要主副节点ip都传入以逗号分隔，缩容的时候必填
        :rtype: list of str
        """
        return self._ReduceShardInfo

    @ReduceShardInfo.setter
    def ReduceShardInfo(self, ReduceShardInfo):
        self._ReduceShardInfo = ReduceShardInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._NodeCount = params.get("NodeCount")
        self._ScaleOutCluster = params.get("ScaleOutCluster")
        self._UserSubnetIPNum = params.get("UserSubnetIPNum")
        self._ScaleOutNodeIp = params.get("ScaleOutNodeIp")
        self._ReduceShardInfo = params.get("ReduceShardInfo")
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
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """ScaleUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一ID
        :type InstanceId: str
        :param _Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param _SpecName: clickhouse节点规格。
        :type SpecName: str
        :param _ScaleUpEnableRolling: 是否滚动重启，false为不滚动重启，true为滚动重启
        :type ScaleUpEnableRolling: bool
        """
        self._InstanceId = None
        self._Type = None
        self._SpecName = None
        self._ScaleUpEnableRolling = None

    @property
    def InstanceId(self):
        """实例唯一ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpecName(self):
        """clickhouse节点规格。
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ScaleUpEnableRolling(self):
        """是否滚动重启，false为不滚动重启，true为滚动重启
        :rtype: bool
        """
        return self._ScaleUpEnableRolling

    @ScaleUpEnableRolling.setter
    def ScaleUpEnableRolling(self, ScaleUpEnableRolling):
        self._ScaleUpEnableRolling = ScaleUpEnableRolling


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._SpecName = params.get("SpecName")
        self._ScaleUpEnableRolling = params.get("ScaleUpEnableRolling")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    """ScaleUpInstance返回参数结构体

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
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ScheduleStrategy(AbstractModel):
    """策略详情

    """

    def __init__(self):
        r"""
        :param _CosBucketName: 备份桶名称
        :type CosBucketName: str
        :param _RetainDays: 备份保留天数
        :type RetainDays: int
        :param _WeekDays: 备份的天
        :type WeekDays: str
        :param _ExecuteHour: 备份小时
        :type ExecuteHour: int
        :param _ScheduleId: 策略id
        :type ScheduleId: int
        :param _NextBackupTime: 下次备份时间
        :type NextBackupTime: str
        """
        self._CosBucketName = None
        self._RetainDays = None
        self._WeekDays = None
        self._ExecuteHour = None
        self._ScheduleId = None
        self._NextBackupTime = None

    @property
    def CosBucketName(self):
        """备份桶名称
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def RetainDays(self):
        """备份保留天数
        :rtype: int
        """
        return self._RetainDays

    @RetainDays.setter
    def RetainDays(self, RetainDays):
        self._RetainDays = RetainDays

    @property
    def WeekDays(self):
        """备份的天
        :rtype: str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def ExecuteHour(self):
        """备份小时
        :rtype: int
        """
        return self._ExecuteHour

    @ExecuteHour.setter
    def ExecuteHour(self, ExecuteHour):
        self._ExecuteHour = ExecuteHour

    @property
    def ScheduleId(self):
        """策略id
        :rtype: int
        """
        return self._ScheduleId

    @ScheduleId.setter
    def ScheduleId(self, ScheduleId):
        self._ScheduleId = ScheduleId

    @property
    def NextBackupTime(self):
        """下次备份时间
        :rtype: str
        """
        return self._NextBackupTime

    @NextBackupTime.setter
    def NextBackupTime(self, NextBackupTime):
        self._NextBackupTime = NextBackupTime


    def _deserialize(self, params):
        self._CosBucketName = params.get("CosBucketName")
        self._RetainDays = params.get("RetainDays")
        self._WeekDays = params.get("WeekDays")
        self._ExecuteHour = params.get("ExecuteHour")
        self._ScheduleId = params.get("ScheduleId")
        self._NextBackupTime = params.get("NextBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTags(AbstractModel):
    """列表页搜索的标记列表

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        :param _AllValue: 1表示只输入标签的键，没有输入值；0表示输入键时且输入值
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

    @property
    def TagKey(self):
        """标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def AllValue(self):
        """1表示只输入标签的键，没有输入值；0表示输入键时且输入值
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
        


class SecondaryZoneInfo(AbstractModel):
    """副可用区详情

    """

    def __init__(self):
        r"""
        :param _SecondaryZone: 副可用区
        :type SecondaryZone: str
        :param _SecondarySubnet: 可用区可用的子网id
        :type SecondarySubnet: str
        :param _UserIpNum: 可用区可用的子网可用ip的数量
        :type UserIpNum: str
        :param _SecondaryUserSubnetIPNum: 可用区可用的子网可用ip的数量
        :type SecondaryUserSubnetIPNum: int
        """
        self._SecondaryZone = None
        self._SecondarySubnet = None
        self._UserIpNum = None
        self._SecondaryUserSubnetIPNum = None

    @property
    def SecondaryZone(self):
        """副可用区
        :rtype: str
        """
        return self._SecondaryZone

    @SecondaryZone.setter
    def SecondaryZone(self, SecondaryZone):
        self._SecondaryZone = SecondaryZone

    @property
    def SecondarySubnet(self):
        """可用区可用的子网id
        :rtype: str
        """
        return self._SecondarySubnet

    @SecondarySubnet.setter
    def SecondarySubnet(self, SecondarySubnet):
        self._SecondarySubnet = SecondarySubnet

    @property
    def UserIpNum(self):
        """可用区可用的子网可用ip的数量
        :rtype: str
        """
        return self._UserIpNum

    @UserIpNum.setter
    def UserIpNum(self, UserIpNum):
        self._UserIpNum = UserIpNum

    @property
    def SecondaryUserSubnetIPNum(self):
        """可用区可用的子网可用ip的数量
        :rtype: int
        """
        return self._SecondaryUserSubnetIPNum

    @SecondaryUserSubnetIPNum.setter
    def SecondaryUserSubnetIPNum(self, SecondaryUserSubnetIPNum):
        self._SecondaryUserSubnetIPNum = SecondaryUserSubnetIPNum


    def _deserialize(self, params):
        self._SecondaryZone = params.get("SecondaryZone")
        self._SecondarySubnet = params.get("SecondarySubnet")
        self._UserIpNum = params.get("UserIpNum")
        self._SecondaryUserSubnetIPNum = params.get("SecondaryUserSubnetIPNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """服务详细信息描述。

    """

    def __init__(self):
        r"""
        :param _Name: 服务名称
        :type Name: str
        :param _Version: 服务的版本
        :type Version: str
        """
        self._Name = None
        self._Version = None

    @property
    def Name(self):
        """服务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        """服务的版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilegeInfo(AbstractModel):
    """表权限

    """

    def __init__(self):
        r"""
        :param _TableName: 表名称
        :type TableName: str
        :param _TablePrivileges: 表权限列表 SELECT、INSERT_ALL、ALTER、TRUNCATE、DROP_TABLE 查询、插入、设置、清空表、删除表
        :type TablePrivileges: list of str
        """
        self._TableName = None
        self._TablePrivileges = None

    @property
    def TableName(self):
        """表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TablePrivileges(self):
        """表权限列表 SELECT、INSERT_ALL、ALTER、TRUNCATE、DROP_TABLE 查询、插入、设置、清空表、删除表
        :rtype: list of str
        """
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TablePrivileges = params.get("TablePrivileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签描述

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
        """标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值
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
        