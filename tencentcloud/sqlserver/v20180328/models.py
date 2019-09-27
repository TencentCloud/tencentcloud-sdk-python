# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AccountCreateInfo(AbstractModel):
    """账号创建信息

    """

    def __init__(self):
        """
        :param UserName: 实例用户名
        :type UserName: str
        :param Password: 实例密码
        :type Password: str
        :param DBPrivileges: DB权限列表
        :type DBPrivileges: list of DBPrivilege
        :param Remark: 账号备注信息
        :type Remark: str
        """
        self.UserName = None
        self.Password = None
        self.DBPrivileges = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)
        self.Remark = params.get("Remark")


class AccountDetail(AbstractModel):
    """账户信息详情

    """

    def __init__(self):
        """
        :param Name: 账户名
        :type Name: str
        :param Remark: 账户备注
        :type Remark: str
        :param CreateTime: 账户创建时间
        :type CreateTime: str
        :param Status: 账户状态，1-创建中，2-正常，3-修改中，4-密码重置中，-1-删除中
        :type Status: int
        :param UpdateTime: 账户更新时间
        :type UpdateTime: str
        :param PassTime: 密码更新时间
        :type PassTime: str
        :param InternalStatus: 账户内部状态，正常为enable
        :type InternalStatus: str
        :param Dbs: 该账户对相关db的读写权限信息
        :type Dbs: list of DBPrivilege
        """
        self.Name = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.UpdateTime = None
        self.PassTime = None
        self.InternalStatus = None
        self.Dbs = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.PassTime = params.get("PassTime")
        self.InternalStatus = params.get("InternalStatus")
        if params.get("Dbs") is not None:
            self.Dbs = []
            for item in params.get("Dbs"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.Dbs.append(obj)


class AccountPassword(AbstractModel):
    """实例账号密码信息

    """

    def __init__(self):
        """
        :param UserName: 用户名
        :type UserName: str
        :param Password: 密码
        :type Password: str
        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class AccountPrivilege(AbstractModel):
    """数据库账号权限信息。创建数据库时设置

    """

    def __init__(self):
        """
        :param UserName: 数据库用户名
        :type UserName: str
        :param Privilege: 数据库权限。ReadWrite表示可读写，ReadOnly表示只读
        :type Privilege: str
        """
        self.UserName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Privilege = params.get("Privilege")


class AccountPrivilegeModifyInfo(AbstractModel):
    """数据库账号权限变更信息

    """

    def __init__(self):
        """
        :param UserName: 数据库用户名
        :type UserName: str
        :param DBPrivileges: 账号权限变更信息
        :type DBPrivileges: list of DBPrivilegeModifyInfo
        """
        self.UserName = None
        self.DBPrivileges = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilegeModifyInfo()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)


class AccountRemark(AbstractModel):
    """账户备注信息

    """

    def __init__(self):
        """
        :param UserName: 账户名
        :type UserName: str
        :param Remark: 对应账户新的备注信息
        :type Remark: str
        """
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")


class Backup(AbstractModel):
    """备份文件详细信息

    """

    def __init__(self):
        """
        :param FileName: 文件名
        :type FileName: str
        :param Size: 文件大小，单位 KB
        :type Size: int
        :param StartTime: 备份开始时间
        :type StartTime: str
        :param EndTime: 备份结束时间
        :type EndTime: str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param Id: 备份文件唯一标识，RestoreInstance接口会用到该字段
        :type Id: int
        :param Status: 备份文件状态（0-创建中；1-成功；2-失败）
        :type Status: int
        :param DBs: 多库备份时的DB列表
        :type DBs: list of str
        :param Strategy: 备份策略（0-实例备份；1-多库备份）
        :type Strategy: int
        :param BackupWay: 备份方式，0-定时备份；1-手动临时备份
        :type BackupWay: int
        """
        self.FileName = None
        self.Size = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Id = None
        self.Status = None
        self.DBs = None
        self.Strategy = None
        self.BackupWay = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Size = params.get("Size")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.DBs = params.get("DBs")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 数据库实例账户信息
        :type Accounts: list of AccountCreateInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountCreateInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param Strategy: 备份策略(0-实例备份 1-多库备份)
        :type Strategy: int
        :param DBNames: 需要备份库名的列表(多库备份才填写)
        :type DBNames: list of str
        :param InstanceId: 实例ID，形如mssql-i1z41iwd
        :type InstanceId: str
        """
        self.Strategy = None
        self.DBNames = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Strategy = params.get("Strategy")
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param Memory: 实例内存大小，单位GB
        :type Memory: int
        :param Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.ProjectId = None
        self.GoodsNum = None
        self.SubnetId = None
        self.VpcId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.DBVersion = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.DBVersion = params.get("DBVersion")


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    """CreateDB请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param DBs: 数据库创建信息
        :type DBs: list of DBCreateInfo
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBs") is not None:
            self.DBs = []
            for item in params.get("DBs"):
                obj = DBCreateInfo()
                obj._deserialize(item)
                self.DBs.append(obj)


class CreateDBResponse(AbstractModel):
    """CreateDB返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateMigrationRequest(AbstractModel):
    """CreateMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateName: 迁移任务的名称
        :type MigrateName: str
        :param MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）
        :type MigrateType: int
        :param SourceType: 迁移源的类型 1:CDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param Source: 迁移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 迁移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 迁移DB对象 ，离线迁移不使用（SourceType=4或SourceType=5）。
        :type MigrateDBSet: list of MigrateDB
        """
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None


    def _deserialize(self, params):
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)


class CreateMigrationResponse(AbstractModel):
    """CreateMigration返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")


class DBCreateInfo(AbstractModel):
    """数据库创建信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名
        :type DBName: str
        :param Charset: 字符集。可选值包括：Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, Chinese_PRC_BIN, Chinese_Taiwan_Stroke_CI_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS。不填默认为Chinese_PRC_CI_AS
        :type Charset: str
        :param Accounts: 数据库账号权限信息
        :type Accounts: list of AccountPrivilege
        :param Remark: 备注
        :type Remark: str
        """
        self.DBName = None
        self.Charset = None
        self.Accounts = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Charset = params.get("Charset")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Remark = params.get("Remark")


class DBDetail(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        """
        :param Name: 数据库名称
        :type Name: str
        :param Charset: 字符集
        :type Charset: str
        :param Remark: 备注
        :type Remark: str
        :param CreateTime: 数据库创建时间
        :type CreateTime: str
        :param Status: 数据库状态。1--创建中， 2--运行中， 3--修改中，-1--删除中
        :type Status: int
        :param Accounts: 数据库账号权限信息
        :type Accounts: list of AccountPrivilege
        :param InternalStatus: 内部状态。ONLINE表示运行中
        :type InternalStatus: str
        """
        self.Name = None
        self.Charset = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.Accounts = None
        self.InternalStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Charset = params.get("Charset")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.InternalStatus = params.get("InternalStatus")


class DBInstance(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Name: 实例名称
        :type Name: str
        :param ProjectId: 实例所在项目ID
        :type ProjectId: int
        :param RegionId: 实例所在地域ID
        :type RegionId: int
        :param ZoneId: 实例所在可用区ID
        :type ZoneId: int
        :param VpcId: 实例所在私有网络ID，基础网络时为 0
        :type VpcId: int
        :param SubnetId: 实例所在私有网络子网ID，基础网络时为 0
        :type SubnetId: int
        :param Status: 实例状态。取值范围： <li>1：申请中</li> <li>2：运行中</li> <li>3：受限运行中 (主备切换中)</li> <li>4：已隔离</li> <li>5：回收中</li> <li>6：已回收</li> <li>7：任务执行中 (实例做备份、回档等操作)</li> <li>8：已下线</li> <li>9：实例扩容中</li> <li>10：实例迁移中</li> <li>11：只读</li> <li>12：重启中</li>
        :type Status: int
        :param Vip: 实例访问IP
        :type Vip: str
        :param Vport: 实例访问端口
        :type Vport: int
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例更新时间
        :type UpdateTime: str
        :param StartTime: 实例计费开始时间
        :type StartTime: str
        :param EndTime: 实例计费结束时间
        :type EndTime: str
        :param IsolateTime: 实例隔离时间
        :type IsolateTime: str
        :param Memory: 实例内存大小，单位G
        :type Memory: int
        :param UsedStorage: 实例已经使用存储空间大小，单位G
        :type UsedStorage: int
        :param Storage: 实例存储空间大小，单位G
        :type Storage: int
        :param VersionName: 实例版本
        :type VersionName: str
        :param RenewFlag: 实例续费标记，0-正常续费，1-自动续费，2-到期不续费
        :type RenewFlag: int
        :param Model: 实例高可用， 1-双机高可用，2-单机
        :type Model: int
        :param Region: 实例所在地域名称，如 ap-guangzhou
        :type Region: str
        :param Zone: 实例所在可用区名称，如 ap-guangzhou-1
        :type Zone: str
        :param BackupTime: 备份时间点
        :type BackupTime: str
        :param PayMode: 实例付费模式， 0-按量计费，1-包年包月
        :type PayMode: int
        :param Uid: 实例唯一UID
        :type Uid: str
        :param Cpu: 实例cpu核心数
        :type Cpu: int
        :param Version: 实例版本代号
        :type Version: str
        :param Type: 物理机代号
        :type Type: str
        :param Pid: 计费ID
        :type Pid: int
        """
        self.InstanceId = None
        self.Name = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.IsolateTime = None
        self.Memory = None
        self.UsedStorage = None
        self.Storage = None
        self.VersionName = None
        self.RenewFlag = None
        self.Model = None
        self.Region = None
        self.Zone = None
        self.BackupTime = None
        self.PayMode = None
        self.Uid = None
        self.Cpu = None
        self.Version = None
        self.Type = None
        self.Pid = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsolateTime = params.get("IsolateTime")
        self.Memory = params.get("Memory")
        self.UsedStorage = params.get("UsedStorage")
        self.Storage = params.get("Storage")
        self.VersionName = params.get("VersionName")
        self.RenewFlag = params.get("RenewFlag")
        self.Model = params.get("Model")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.BackupTime = params.get("BackupTime")
        self.PayMode = params.get("PayMode")
        self.Uid = params.get("Uid")
        self.Cpu = params.get("Cpu")
        self.Version = params.get("Version")
        self.Type = params.get("Type")
        self.Pid = params.get("Pid")


class DBPrivilege(AbstractModel):
    """账号的数据库权限信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名
        :type DBName: str
        :param Privilege: 数据库权限，ReadWrite表示可读写，ReadOnly表示只读
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")


class DBPrivilegeModifyInfo(AbstractModel):
    """数据库权限变更信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名
        :type DBName: str
        :param Privilege: 权限变更信息。ReadWrite表示可读写，ReadOnly表示只读，Delete表示删除账号对该DB的权限
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")


class DBRemark(AbstractModel):
    """数据库备注信息

    """

    def __init__(self):
        """
        :param Name: 据库名
        :type Name: str
        :param Remark: 备注信息
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")


class DbRollbackTimeInfo(AbstractModel):
    """数据库可回档时间范围信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名称
        :type DBName: str
        :param StartTime: 可回档开始时间
        :type StartTime: str
        :param EndTime: 可回档结束时间
        :type EndTime: str
        """
        self.DBName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DealInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单名
        :type DealName: str
        :param Count: 商品数量
        :type Count: int
        :param FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param InstanceIdSet: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
        :type InstanceIdSet: list of str
        :param OwnerUin: 所属账号
        :type OwnerUin: str
        :param InstanceChargeType: 实例付费类型
        :type InstanceChargeType: str
        """
        self.DealName = None
        self.Count = None
        self.FlowId = None
        self.InstanceIdSet = None
        self.OwnerUin = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.OwnerUin = params.get("OwnerUin")
        self.InstanceChargeType = params.get("InstanceChargeType")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param UserNames: 实例用户名数组
        :type UserNames: list of str
        """
        self.InstanceId = None
        self.UserNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserNames = params.get("UserNames")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteDBRequest(AbstractModel):
    """DeleteDB请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param Names: 数据库名数组
        :type Names: list of str
        """
        self.InstanceId = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Names = params.get("Names")


class DeleteDBResponse(AbstractModel):
    """DeleteDB返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param Offset: 分页返回，从第几页开始返回。从第0页开始，默认第0页
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Accounts: 账户信息列表
        :type Accounts: list of AccountDetail
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param EndTime: 结束时间(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Limit: 分页返回，每页返回数量，默认为20，最大值为 100
        :type Limit: int
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 备份总数量
        :type TotalCount: int
        :param Backups: 备份列表详情
        :type Backups: list of Backup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Backups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Backups") is not None:
            self.Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self.Backups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Status: 实例状态。取值范围：
<li>1：申请中</li>
<li>2：运行中</li>
<li>3：受限运行中 (主备切换中)</li>
<li>4：已隔离</li>
<li>5：回收中</li>
<li>6：已回收</li>
<li>7：任务执行中 (实例做备份、回档等操作)</li>
<li>8：已下线</li>
<li>9：实例扩容中</li>
<li>10：实例迁移中</li>
<li>11：只读</li>
<li>12：重启中</li>
        :type Status: int
        :param Offset: 页数，默认为 0
        :type Offset: int
        :param Limit: 页大小，默认为50
        :type Limit: int
        :param InstanceIdSet: 一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl
        :type InstanceIdSet: list of str
        :param PayMode: 付费类型检索 1-包年包月，0-按量计费
        :type PayMode: int
        """
        self.ProjectId = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.InstanceIdSet = None
        self.PayMode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.PayMode = params.get("PayMode")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例总数。分页返回的话，这个值指的是所有符合条件的实例的个数，而非当前根据Limit和Offset值返回的实例个数
        :type TotalCount: int
        :param DBInstances: 实例列表
        :type DBInstances: list of DBInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 实例ID
        :type InstanceIdSet: list of str
        :param Limit: 每页记录数，最大为100，默认20
        :type Limit: int
        :param Offset: 页编号，从第0页开始
        :type Offset: int
        """
        self.InstanceIdSet = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 数据库数量
        :type TotalCount: int
        :param DBInstances: 实例数据库列表
        :type DBInstances: list of InstanceDBDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowStatusRequest(AbstractModel):
    """DescribeFlowStatus请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 流程状态，0：成功，1：失败，2：运行中
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        :param MigrateName: 迁移任务名称
        :type MigrateName: str
        :param AppId: 迁移任务所属的用户ID
        :type AppId: int
        :param Region: 迁移任务所属的地域
        :type Region: str
        :param SourceType: 迁移源的类型 1:CDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param CreateTime: 迁移任务的创建时间
        :type CreateTime: str
        :param StartTime: 迁移任务的开始时间
        :type StartTime: str
        :param EndTime: 迁移任务的结束时间
        :type EndTime: str
        :param Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功）
        :type Status: int
        :param Progress: 迁移任务当前进度
        :type Progress: int
        :param MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）
        :type MigrateType: int
        :param Source: 迁移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 迁移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用。
        :type MigrateDBSet: list of MigrateDB
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Progress = None
        self.MigrateType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.MigrateType = params.get("MigrateType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationsRequest(AbstractModel):
    """DescribeMigrations请求参数结构体

    """

    def __init__(self):
        """
        :param StatusSet: 状态集合。只要符合集合中某一状态的迁移任务，就会查出来
        :type StatusSet: list of int
        :param MigrateName: 迁移任务的名称，模糊匹配
        :type MigrateName: str
        :param Limit: 每页的记录数
        :type Limit: int
        :param Offset: 查询第几页的记录
        :type Offset: int
        :param OrderBy: 查询结果按照关键字排序，可选值为name、createTime、startTime，endTime，status
        :type OrderBy: str
        :param OrderByType: 排序方式，可选值为desc、asc
        :type OrderByType: str
        """
        self.StatusSet = None
        self.MigrateName = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.StatusSet = params.get("StatusSet")
        self.MigrateName = params.get("MigrateName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询结果的总数
        :type TotalCount: int
        :param MigrateTaskSet: 查询结果的列表
        :type MigrateTaskSet: list of MigrateTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MigrateTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MigrateTaskSet") is not None:
            self.MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self.MigrateTaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单数组。发货时会返回订单名字，利用该订单名字调用DescribeOrders接口查询发货情况
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        """
        :param Deals: 订单信息数组
        :type Deals: list of DealInfo
        :param TotalCount: 返回多少个订单的信息
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Deals = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区英文ID，形如ap-guangzhou-1
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        """
        :param SpecInfoList: 规格信息数组
        :type SpecInfoList: list of SpecInfo
        :param TotalCount: 返回总共多少条数据
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回地域信息总的条目
        :type TotalCount: int
        :param RegionSet: 地域信息数组
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeRequest(AbstractModel):
    """DescribeRollbackTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param DBs: 需要查询的数据库列表
        :type DBs: list of str
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DBs = params.get("DBs")


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime返回参数结构体

    """

    def __init__(self):
        """
        :param Details: 数据库可回档实例信息
        :type Details: list of DbRollbackTimeInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowlogsRequest(AbstractModel):
    """DescribeSlowlogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Limit: 分页返回结果，分页大小，默认20，不超过100
        :type Limit: int
        :param Offset: 从第几页开始返回，起始页，从0开始，默认为0
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询总数
        :type TotalCount: int
        :param Slowlogs: 慢查询日志信息列表
        :type Slowlogs: list of SlowlogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Slowlogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Slowlogs") is not None:
            self.Slowlogs = []
            for item in params.get("Slowlogs"):
                obj = SlowlogInfo()
                obj._deserialize(item)
                self.Slowlogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回多少个可用区信息
        :type TotalCount: int
        :param ZoneSet: 可用区数组
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param Memory: 内存大小，单位：GB
        :type Memory: int
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceChargeType: 计费类型，取值支持 PREPAID，POSTPAID。
        :type InstanceChargeType: str
        :param Period: 购买时长，单位：月。取值为1到48，默认为1
        :type Period: int
        :param GoodsNum: 一次性购买的实例数量。取值1-100，默认取值为1
        :type GoodsNum: int
        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。默认为2008R2版本
        :type DBVersion: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.Period = None
        self.GoodsNum = None
        self.DBVersion = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.DBVersion = params.get("DBVersion")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折前价格，其值除以100表示多少钱。比如10010表示100.10元
        :type OriginalPrice: int
        :param Price: 实际需要支付的价格，其值除以100表示多少钱。比如10010表示100.10元
        :type Price: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    """InquiryPriceRenewDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Period: 续费周期。按月续费最多48个月。默认查询续费一个月的价格
        :type Period: int
        :param TimeUnit: 续费周期单位。month表示按月续费，当前只支持按月付费查询价格
        :type TimeUnit: str
        """
        self.InstanceId = None
        self.Period = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.TimeUnit = params.get("TimeUnit")


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。比如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 实际需要支付价格，其值除以100表示最终的价格。比如10094表示100.94元
        :type Price: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Memory: 实例升级后的内存大小，单位GB，其值不能比当前实例内存小
        :type Memory: int
        :param Storage: 实例升级后的磁盘大小，单位GB，其值不能比当前实例磁盘小
        :type Storage: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。比如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 实际需要支付价格，其值除以100表示最终的价格。比如10094表示100.94元
        :type Price: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InstanceDBDetail(AbstractModel):
    """实例的数据库信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param DBDetails: 数据库信息列表
        :type DBDetails: list of DBDetail
        """
        self.InstanceId = None
        self.DBDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBDetails") is not None:
            self.DBDetails = []
            for item in params.get("DBDetails"):
                obj = DBDetail()
                obj._deserialize(item)
                self.DBDetails.append(obj)


class InstanceRenewInfo(AbstractModel):
    """实例续费状态信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param RenewFlag: 实例续费标记。0：正常续费，1：自动续费，2：到期不续
        :type RenewFlag: int
        """
        self.InstanceId = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RenewFlag = params.get("RenewFlag")


class MigrateDB(AbstractModel):
    """需要迁移的DB列表

    """

    def __init__(self):
        """
        :param DBName: 迁移数据库的名称
        :type DBName: str
        """
        self.DBName = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")


class MigrateDetail(AbstractModel):
    """迁移的进度详情类型

    """

    def __init__(self):
        """
        :param StepName: 当前环节的名称
        :type StepName: str
        :param Progress: 当前环节的进度（单位是%）
        :type Progress: int
        """
        self.StepName = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.Progress = params.get("Progress")


class MigrateSource(AbstractModel):
    """迁移任务的源类型

    """

    def __init__(self):
        """
        :param InstanceId: 迁移源实例的ID，MigrateType=1(CDB for SQLServers)时使用，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param CvmId: 迁移源Cvm的ID，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type CvmId: str
        :param VpcId: 迁移源Cvm的Vpc网络标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：vpc-6ys9ont9
        :type VpcId: str
        :param SubnetId: 迁移源Cvm的Vpc下的子网标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：subnet-h9extioi
        :type SubnetId: str
        :param UserName: 用户名，MigrateType=1或MigrateType=2使用
        :type UserName: str
        :param Password: 密码，MigrateType=1或MigrateType=2使用
        :type Password: str
        :param Ip: 迁移源Cvm自建库的内网IP，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type Ip: str
        :param Port: 迁移源Cvm自建库的端口号，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type Port: int
        :param Url: 离线迁移的源备份地址，MigrateType=4或MigrateType=5使用
        :type Url: list of str
        :param UrlPassword: 离线迁移的源备份密码，MigrateType=4或MigrateType=5使用
        :type UrlPassword: str
        """
        self.InstanceId = None
        self.CvmId = None
        self.VpcId = None
        self.SubnetId = None
        self.UserName = None
        self.Password = None
        self.Ip = None
        self.Port = None
        self.Url = None
        self.UrlPassword = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CvmId = params.get("CvmId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Url = params.get("Url")
        self.UrlPassword = params.get("UrlPassword")


class MigrateTarget(AbstractModel):
    """迁移任务的目标类型

    """

    def __init__(self):
        """
        :param InstanceId: 迁移目标实例的ID，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param UserName: 迁移目标实例的用户名
        :type UserName: str
        :param Password: 迁移目标实例的密码
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class MigrateTask(AbstractModel):
    """查询迁移任务列表类型

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        :param MigrateName: 迁移任务名称
        :type MigrateName: str
        :param AppId: 迁移任务所属的用户ID
        :type AppId: int
        :param Region: 迁移任务所属的地域
        :type Region: str
        :param SourceType: 迁移源的类型 1:CDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param CreateTime: 迁移任务的创建时间
        :type CreateTime: str
        :param StartTime: 迁移任务的开始时间
        :type StartTime: str
        :param EndTime: 迁移任务的结束时间
        :type EndTime: str
        :param Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功）
        :type Status: int
        :param Message: 信息
        :type Message: str
        :param CheckFlag: 是否迁移任务经过检查（0:未校验,1:校验成功,2:校验失败,3:校验中）
        :type CheckFlag: int
        :param Progress: 迁移任务当前进度（单位%）
        :type Progress: int
        :param MigrateDetail: 迁移任务进度细节
        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Message = None
        self.CheckFlag = None
        self.Progress = None
        self.MigrateDetail = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.CheckFlag = params.get("CheckFlag")
        self.Progress = params.get("Progress")
        if params.get("MigrateDetail") is not None:
            self.MigrateDetail = MigrateDetail()
            self.MigrateDetail._deserialize(params.get("MigrateDetail"))


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 账号权限变更信息
        :type Accounts: list of AccountPrivilegeModifyInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilegeModifyInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Accounts: 修改备注的账户信息
        :type Accounts: list of AccountRemark
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountRemark()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param InstanceName: 新的数据库实例名字
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 实例ID数组，形如mssql-j8kv137v
        :type InstanceIdSet: list of str
        :param ProjectId: 项目ID，为0的话表示默认项目
        :type ProjectId: int
        """
        self.InstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 修改成功的实例个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceRenewFlagRequest(AbstractModel):
    """ModifyDBInstanceRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param RenewFlags: 实例续费状态标记信息
        :type RenewFlags: list of InstanceRenewInfo
        """
        self.RenewFlags = None


    def _deserialize(self, params):
        if params.get("RenewFlags") is not None:
            self.RenewFlags = []
            for item in params.get("RenewFlags"):
                obj = InstanceRenewInfo()
                obj._deserialize(item)
                self.RenewFlags.append(obj)


class ModifyDBInstanceRenewFlagResponse(AbstractModel):
    """ModifyDBInstanceRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 修改成功的个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param OldDBName: 旧数据库名
        :type OldDBName: str
        :param NewDBName: 新数据库名
        :type NewDBName: str
        """
        self.InstanceId = None
        self.OldDBName = None
        self.NewDBName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldDBName = params.get("OldDBName")
        self.NewDBName = params.get("NewDBName")


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBRemarkRequest(AbstractModel):
    """ModifyDBRemark请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param DBRemarks: 数据库名称及备注数组，每个元素包含数据库名和对应的备注
        :type DBRemarks: list of DBRemark
        """
        self.InstanceId = None
        self.DBRemarks = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBRemarks") is not None:
            self.DBRemarks = []
            for item in params.get("DBRemarks"):
                obj = DBRemark()
                obj._deserialize(item)
                self.DBRemarks.append(obj)


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        :param MigrateName: 新的迁移任务的名称，若不填则不修改
        :type MigrateName: str
        :param MigrateType: 新的迁移类型（1:结构迁移 2:数据迁移 3:增量同步），若不填则不修改
        :type MigrateType: int
        :param SourceType: 迁移源的类型 1:CDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式），若不填则不修改
        :type SourceType: int
        :param Source: 迁移源，若不填则不修改
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 迁移目标，若不填则不修改
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用，若不填则不修改
        :type MigrateDBSet: list of MigrateDB
        """
        self.MigrateId = None
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID，类似ap-guanghou
        :type Region: str
        :param RegionName: 地域中文名称
        :type RegionName: str
        :param RegionId: 地域数字ID
        :type RegionId: int
        :param RegionState: 该地域目前是否可以售卖，UNAVAILABLE-不可售卖；AVAILABLE-可售卖
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Period: 续费多少个月，取值范围为1-48，默认为1
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券，0-不使用；1-使用；默认不实用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID数组，目前只支持使用1张代金券
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 更新后的账户密码信息数组
        :type Accounts: list of AccountPassword
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPassword()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 修改帐号密码的异步任务流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param BackupId: 备份文件ID，该ID可以通过DescribeBackups接口返回数据中的Id字段获得
        :type BackupId: int
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步流程任务ID，使用FlowId调用DescribeFlowStatus接口获取任务执行状态
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RollbackInstanceRequest(AbstractModel):
    """RollbackInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Type: 回档类型，0-回档的数据库覆盖原库；1-回档的数据库以重命名的形式生成，不覆盖原库
        :type Type: int
        :param DBs: 需要回档的数据库
        :type DBs: list of str
        :param Time: 回档目标时间点
        :type Time: str
        """
        self.InstanceId = None
        self.Type = None
        self.DBs = None
        self.Time = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.DBs = params.get("DBs")
        self.Time = params.get("Time")


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RunMigrationRequest(AbstractModel):
    """RunMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class RunMigrationResponse(AbstractModel):
    """RunMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 迁移流程启动后，返回流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SlowlogInfo(AbstractModel):
    """慢查询日志文件信息

    """

    def __init__(self):
        """
        :param Id: 慢查询日志文件唯一标识
        :type Id: int
        :param StartTime: 文件生成的开始时间
        :type StartTime: str
        :param EndTime: 文件生成的结束时间
        :type EndTime: str
        :param Size: 文件大小（KB）
        :type Size: int
        :param Count: 文件中log条数
        :type Count: int
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param Status: 状态（1成功 2失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Count = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Count = params.get("Count")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Status = params.get("Status")


class SpecInfo(AbstractModel):
    """实例可售卖的规格信息

    """

    def __init__(self):
        """
        :param SpecId: 实例规格ID，利用DescribeZones返回的SpecId，结合DescribeProductConfig返回的可售卖规格信息，可获悉某个可用区下可购买什么规格的实例
        :type SpecId: int
        :param MachineType: 机型ID
        :type MachineType: str
        :param MachineTypeName: 机型中文名称
        :type MachineTypeName: str
        :param Version: 数据库版本信息。取值为2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        :param VersionName: Version字段对应的版本名称
        :type VersionName: str
        :param Memory: 内存大小，单位GB
        :type Memory: int
        :param CPU: CPU核数
        :type CPU: int
        :param MinStorage: 此规格下最小的磁盘大小，单位GB
        :type MinStorage: int
        :param MaxStorage: 此规格下最大的磁盘大小，单位GB
        :type MaxStorage: int
        :param QPS: 此规格对应的QPS大小
        :type QPS: int
        :param SuitInfo: 此规格的中文描述信息
        :type SuitInfo: str
        :param Pid: 此规格对应的包年包月Pid
        :type Pid: int
        :param PostPid: 此规格对应的按量计费Pid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPid: list of int
        :param PayModeStatus: 此规格下支持的付费模式，POST-仅支持按量计费 PRE-仅支持包年包月 ALL-支持所有
        :type PayModeStatus: str
        """
        self.SpecId = None
        self.MachineType = None
        self.MachineTypeName = None
        self.Version = None
        self.VersionName = None
        self.Memory = None
        self.CPU = None
        self.MinStorage = None
        self.MaxStorage = None
        self.QPS = None
        self.SuitInfo = None
        self.Pid = None
        self.PostPid = None
        self.PayModeStatus = None


    def _deserialize(self, params):
        self.SpecId = params.get("SpecId")
        self.MachineType = params.get("MachineType")
        self.MachineTypeName = params.get("MachineTypeName")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Memory = params.get("Memory")
        self.CPU = params.get("CPU")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.QPS = params.get("QPS")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")
        self.PostPid = params.get("PostPid")
        self.PayModeStatus = params.get("PayModeStatus")


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 主动销毁的实例ID列表，格式如：[mssql-3l3fgqn7]。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Memory: 实例升级后内存大小，单位GB，其值不能小于当前实例内存大小
        :type Memory: int
        :param Storage: 实例升级后磁盘大小，单位GB，其值不能小于当前实例磁盘大小
        :type Storage: int
        :param AutoVoucher: 是否自动使用代金券，0 - 不使用；1 - 默认使用。取值默认为0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID，目前单个订单只能使用一张代金券
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        """
        :param Zone: 可用区英文ID，形如ap-guangzhou-1，表示广州一区
        :type Zone: str
        :param ZoneName: 可用区中文名称
        :type ZoneName: str
        :param ZoneId: 可用区数字ID
        :type ZoneId: int
        :param SpecId: 该可用区目前可售卖的规格ID，利用SpecId，结合接口DescribeProductConfig返回的数据，可获悉该可用区目前可售卖的规格大小
        :type SpecId: int
        :param Version: 当前可用区与规格下，可售卖的数据库版本，形如2008R2（表示SQL Server 2008 R2）。其可选值有2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.SpecId = None
        self.Version = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.SpecId = params.get("SpecId")
        self.Version = params.get("Version")