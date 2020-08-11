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
        :param IsAdmin: 是否为管理员账户，默认为否
        :type IsAdmin: bool
        """
        self.UserName = None
        self.Password = None
        self.DBPrivileges = None
        self.Remark = None
        self.IsAdmin = None


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
        self.IsAdmin = params.get("IsAdmin")


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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。
        :type InstanceIdSet: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIdSet = params.get("InstanceIdSet")


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param BackupName: 备份名称，可自定义
        :type BackupName: str
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
        self.BackupName = None


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
        self.BackupName = params.get("BackupName")


class CompleteExpansionRequest(AbstractModel):
    """CompleteExpansion请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CompleteExpansionResponse(AbstractModel):
    """CompleteExpansion返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CompleteMigrationRequest(AbstractModel):
    """CompleteMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class CompleteMigrationResponse(AbstractModel):
    """CompleteMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 完成迁移流程发起后，返回的流程id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


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
        :param FlowId: 任务流ID
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
        :param BackupName: 备份名称，若不填则自动生成“实例ID_备份开始时间戳”
        :type BackupName: str
        """
        self.Strategy = None
        self.DBNames = None
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.Strategy = params.get("Strategy")
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")


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


class CreateBasicDBInstancesRequest(AbstractModel):
    """CreateBasicDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param Cpu: 实例的CPU核心数
        :type Cpu: int
        :param Memory: 实例内存大小，单位GB
        :type Memory: int
        :param Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa
        :type SubnetId: str
        :param VpcId: VPC网络ID，形如vpc-dsp338hz
        :type VpcId: str
        :param MachineType: 购买实例的宿主机类型, CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘
        :type MachineType: str
        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard），2017（SQL Server 2017 Enterprise），201202（SQL Server 2012 Standard），201402（SQL Server 2014 Standard），2014SP2（SQL Server 2014 Enterprise），201702（SQL Server 2017 Standard）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        """
        self.Zone = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.SubnetId = None
        self.VpcId = None
        self.MachineType = None
        self.InstanceChargeType = None
        self.ProjectId = None
        self.GoodsNum = None
        self.DBVersion = None
        self.Period = None
        self.SecurityGroupList = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.Weekly = None
        self.StartTime = None
        self.Span = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.MachineType = params.get("MachineType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.DBVersion = params.get("DBVersion")
        self.Period = params.get("Period")
        self.SecurityGroupList = params.get("SecurityGroupList")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")


class CreateBasicDBInstancesResponse(AbstractModel):
    """CreateBasicDBInstances返回参数结构体

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
        :param AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param HAType: 购买高可用实例的类型：DUAL-双机高可用  CLUSTER-集群，默认值为DUAL
        :type HAType: str
        :param MultiZones: 是否跨可用区部署，默认值为false
        :type MultiZones: bool
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
        self.AutoRenewFlag = None
        self.SecurityGroupList = None
        self.Weekly = None
        self.StartTime = None
        self.Span = None
        self.HAType = None
        self.MultiZones = None


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
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SecurityGroupList = params.get("SecurityGroupList")
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")
        self.HAType = params.get("HAType")
        self.MultiZones = params.get("MultiZones")


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称
        :type DealName: str
        :param DealNames: 订单名称数组
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    """CreateDB请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
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
        :param FlowId: 任务流ID
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
        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
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


class CreatePublishSubscribeRequest(AbstractModel):
    """CreatePublishSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param PublishInstanceId: 发布实例ID，形如mssql-j8kv137v
        :type PublishInstanceId: str
        :param SubscribeInstanceId: 订阅实例ID，形如mssql-j8kv137v
        :type SubscribeInstanceId: str
        :param DatabaseTupleSet: 数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTuple
        :param PublishSubscribeName: 发布订阅的名称，默认值为：default_name
        :type PublishSubscribeName: str
        """
        self.PublishInstanceId = None
        self.SubscribeInstanceId = None
        self.DatabaseTupleSet = None
        self.PublishSubscribeName = None


    def _deserialize(self, params):
        self.PublishInstanceId = params.get("PublishInstanceId")
        self.SubscribeInstanceId = params.get("SubscribeInstanceId")
        if params.get("DatabaseTupleSet") is not None:
            self.DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self.DatabaseTupleSet.append(obj)
        self.PublishSubscribeName = params.get("PublishSubscribeName")


class CreatePublishSubscribeResponse(AbstractModel):
    """CreatePublishSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyDBInstancesRequest(AbstractModel):
    """CreateReadOnlyDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param ReadOnlyGroupType: 只读组类型选项，1-按照一个实例一个只读组的方式发货，2-新建只读组后发货，所有实例都在这个只读组下面， 3-发货的所有实例都在已有的只读组下面
        :type ReadOnlyGroupType: int
        :param Memory: 实例内存大小，单位GB
        :type Memory: int
        :param Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param ReadOnlyGroupForcedUpgrade: 0-默认不升级主实例，1-强制升级主实例完成ro部署；主实例为非集群版时需要填1，强制升级为集群版。填1 说明您已同意将主实例升级到集群版实例。
        :type ReadOnlyGroupForcedUpgrade: int
        :param ReadOnlyGroupId: ReadOnlyGroupType=3时必填,已存在的只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: ReadOnlyGroupType=2时必填，新建的只读组名称
        :type ReadOnlyGroupName: str
        :param ReadOnlyGroupIsOfflineDelay: ReadOnlyGroupType=2时必填，新建的只读组是否开启延迟剔除功能，1-开启，0-关闭。当只读副本与主实例延迟大于阈值后，自动剔除。
        :type ReadOnlyGroupIsOfflineDelay: int
        :param ReadOnlyGroupMaxDelayTime: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除的阈值。
        :type ReadOnlyGroupMaxDelayTime: int
        :param ReadOnlyGroupMinInGroup: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除后至少保留只读副本的个数。
        :type ReadOnlyGroupMinInGroup: int
        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param GoodsNum: 本次购买几个只读实例，默认值为1。
        :type GoodsNum: int
        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Zone = None
        self.ReadOnlyGroupType = None
        self.Memory = None
        self.Storage = None
        self.ReadOnlyGroupForcedUpgrade = None
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.ReadOnlyGroupIsOfflineDelay = None
        self.ReadOnlyGroupMaxDelayTime = None
        self.ReadOnlyGroupMinInGroup = None
        self.InstanceChargeType = None
        self.GoodsNum = None
        self.SubnetId = None
        self.VpcId = None
        self.Period = None
        self.SecurityGroupList = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.ReadOnlyGroupType = params.get("ReadOnlyGroupType")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ReadOnlyGroupForcedUpgrade = params.get("ReadOnlyGroupForcedUpgrade")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.ReadOnlyGroupIsOfflineDelay = params.get("ReadOnlyGroupIsOfflineDelay")
        self.ReadOnlyGroupMaxDelayTime = params.get("ReadOnlyGroupMaxDelayTime")
        self.ReadOnlyGroupMinInGroup = params.get("ReadOnlyGroupMinInGroup")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.GoodsNum = params.get("GoodsNum")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Period = params.get("Period")
        self.SecurityGroupList = params.get("SecurityGroupList")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class CreateReadOnlyDBInstancesResponse(AbstractModel):
    """CreateReadOnlyDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单名称数组
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
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
        :param UniqVpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，基础网络时为空字符串
        :type UniqVpcId: str
        :param UniqSubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，基础网络时为空字符串
        :type UniqSubnetId: str
        :param IsolateOperator: 实例隔离操作
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateOperator: str
        :param SubFlag: 发布订阅标识，SUB-订阅实例，PUB-发布实例，空值-没有发布订阅的普通实例
注意：此字段可能返回 null，表示取不到有效值。
        :type SubFlag: str
        :param ROFlag: 只读标识，RO-只读实例，MASTER-有RO实例的主实例，空值-没有只读组的非RO实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ROFlag: str
        :param HAFlag: 容灾类型，MIRROR-镜像，ALWAYSON-AlwaysOn, SINGLE-单例
注意：此字段可能返回 null，表示取不到有效值。
        :type HAFlag: str
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
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.IsolateOperator = None
        self.SubFlag = None
        self.ROFlag = None
        self.HAFlag = None


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
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.IsolateOperator = params.get("IsolateOperator")
        self.SubFlag = params.get("SubFlag")
        self.ROFlag = params.get("ROFlag")
        self.HAFlag = params.get("HAFlag")


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
        :param Name: 数据库名称
        :type Name: str
        :param Remark: 备注信息
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")


class DatabaseTuple(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库。

    """

    def __init__(self):
        """
        :param PublishDatabase: 发布数据库名称
        :type PublishDatabase: str
        :param SubscribeDatabase: 订阅数据库名称
        :type SubscribeDatabase: str
        """
        self.PublishDatabase = None
        self.SubscribeDatabase = None


    def _deserialize(self, params):
        self.PublishDatabase = params.get("PublishDatabase")
        self.SubscribeDatabase = params.get("SubscribeDatabase")


class DatabaseTupleStatus(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库，以及其之间发布订阅的状态信息。

    """

    def __init__(self):
        """
        :param PublishDatabase: 发布数据库名称
        :type PublishDatabase: str
        :param SubscribeDatabase: 订阅数据库名称
        :type SubscribeDatabase: str
        :param LastSyncTime: 最近一次同步时间
        :type LastSyncTime: str
        :param Status: 数据库之间的发布订阅状态 running，success，fail，unknow
        :type Status: str
        """
        self.PublishDatabase = None
        self.SubscribeDatabase = None
        self.LastSyncTime = None
        self.Status = None


    def _deserialize(self, params):
        self.PublishDatabase = params.get("PublishDatabase")
        self.SubscribeDatabase = params.get("SubscribeDatabase")
        self.LastSyncTime = params.get("LastSyncTime")
        self.Status = params.get("Status")


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
        :param FlowId: 关联的流程 ID，可用于查询流程执行状态
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
        :param FlowId: 任务流ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteDBInstanceResponse(AbstractModel):
    """DeleteDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param FlowId: 任务流ID
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


class DeletePublishSubscribeRequest(AbstractModel):
    """DeletePublishSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param PublishSubscribeId: 发布订阅ID，可通过DescribePublishSubscribe接口获得
        :type PublishSubscribeId: int
        :param DatabaseTupleSet: 待删除的数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTuple
        """
        self.PublishSubscribeId = None
        self.DatabaseTupleSet = None


    def _deserialize(self, params):
        self.PublishSubscribeId = params.get("PublishSubscribeId")
        if params.get("DatabaseTupleSet") is not None:
            self.DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self.DatabaseTupleSet.append(obj)


class DeletePublishSubscribeResponse(AbstractModel):
    """DeletePublishSubscribe返回参数结构体

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
        :param Offset: 分页返回，页编号，默认值为第0页
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


class DescribeBackupByFlowIdRequest(AbstractModel):
    """DescribeBackupByFlowId请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param FlowId: 创建备份流程ID
        :type FlowId: str
        """
        self.InstanceId = None
        self.FlowId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FlowId = params.get("FlowId")


class DescribeBackupByFlowIdResponse(AbstractModel):
    """DescribeBackupByFlowId返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 备份文件唯一标识，RestoreInstance接口会用到该字段
        :type Id: int
        :param FileName: 存储文件名
        :type FileName: str
        :param BackupName: 备份名称，可自定义
        :type BackupName: str
        :param StartTime: 备份开始时间
        :type StartTime: str
        :param EndTime: 备份结束时间
        :type EndTime: str
        :param Size: 文件大小，单位 KB
        :type Size: int
        :param Strategy: 备份策略，0-实例备份；1-多库备份；实例状态是0-创建中时，该字段为默认值0，无实际意义
        :type Strategy: int
        :param BackupWay: 备份方式，0-定时备份；1-手动临时备份；实例状态是0-创建中时，该字段为默认值0，无实际意义
        :type BackupWay: int
        :param Status: 备份文件状态，0-创建中；1-成功；2-失败
        :type Status: int
        :param DBs: 多库备份时的DB列表
        :type DBs: list of str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.FileName = None
        self.BackupName = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Strategy = None
        self.BackupWay = None
        self.Status = None
        self.DBs = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.FileName = params.get("FileName")
        self.BackupName = params.get("BackupName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")
        self.Status = params.get("Status")
        self.DBs = params.get("DBs")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
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
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param BackupName: 按照备份名称筛选，不填则不筛选此项
        :type BackupName: str
        :param Strategy: 按照备份策略筛选，0-实例备份，1-多库备份，不填则不筛选此项
        :type Strategy: int
        :param BackupWay: 按照备份方式筛选，0-后台自动定时备份，1-用户手动临时备份，不填则不筛选此项
        :type BackupWay: int
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BackupName = None
        self.Strategy = None
        self.BackupWay = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BackupName = params.get("BackupName")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")


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


class DescribeCrossRegionZoneRequest(AbstractModel):
    """DescribeCrossRegionZone请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeCrossRegionZoneResponse(AbstractModel):
    """DescribeCrossRegionZone返回参数结构体

    """

    def __init__(self):
        """
        :param Region: 备机所在地域的字符串ID，形如：ap-guangzhou
        :type Region: str
        :param Zone: 备机所在可用区的字符串ID，形如：ap-guangzhou-1
        :type Zone: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Region = None
        self.Zone = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
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
        :param Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100
        :type Limit: int
        :param InstanceIdSet: 一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl
        :type InstanceIdSet: list of str
        :param PayMode: 付费类型检索 1-包年包月，0-按量计费
        :type PayMode: int
        :param VpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，传空字符串(“”)则按照基础网络筛选。
        :type VpcId: str
        :param SubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，传空字符串(“”)则按照基础网络筛选。
        :type SubnetId: str
        """
        self.ProjectId = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.InstanceIdSet = None
        self.PayMode = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.PayMode = params.get("PayMode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


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


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-c1nl9rpv或者mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全组详情。
        :type SecurityGroupSet: list of SecurityGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 实例ID
        :type InstanceIdSet: list of str
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param Offset: 分页返回，页编号，默认值为第0页
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


class DescribeMaintenanceSpanRequest(AbstractModel):
    """DescribeMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeMaintenanceSpanResponse(AbstractModel):
    """DescribeMaintenanceSpan返回参数结构体

    """

    def __init__(self):
        """
        :param Weekly: 以周为单位，表示周几允许维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日。
        :type Weekly: list of int
        :param StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始。
        :type StartTime: str
        :param Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时。
        :type Span: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Weekly = None
        self.StartTime = None
        self.Span = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")
        self.RequestId = params.get("RequestId")


class DescribeMigrationDatabasesRequest(AbstractModel):
    """DescribeMigrationDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 迁移源实例的ID，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param UserName: 迁移源实例用户名
        :type UserName: str
        :param Password: 迁移源实例密码
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class DescribeMigrationDatabasesResponse(AbstractModel):
    """DescribeMigrationDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param Amount: 数据库数量
        :type Amount: int
        :param MigrateDBSet: 数据库名称数组
        :type MigrateDBSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Amount = None
        self.MigrateDBSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Amount = params.get("Amount")
        self.MigrateDBSet = params.get("MigrateDBSet")
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
        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
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
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100
        :type Limit: int
        :param Offset: 分页返回，页编号，默认值为第0页
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


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID。
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全组详情。
        :type SecurityGroupSet: list of SecurityGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePublishSubscribeRequest(AbstractModel):
    """DescribePublishSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param PubOrSubInstanceId: 订阅/发布实例ID，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例ID做筛选；当InstanceId为订阅实例时，本字段按照发布实例ID做筛选；
        :type PubOrSubInstanceId: str
        :param PubOrSubInstanceIp: 订阅/发布实例内网IP，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例内网IP做筛选；当InstanceId为订阅实例时，本字段按照发布实例内网IP做筛选；
        :type PubOrSubInstanceIp: str
        :param PublishSubscribeId: 订阅发布ID，用于筛选
        :type PublishSubscribeId: int
        :param PublishSubscribeName: 订阅发布名字，用于筛选
        :type PublishSubscribeName: str
        :param PublishDBName: 发布库名字，用于筛选
        :type PublishDBName: str
        :param SubscribeDBName: 订阅库名字，用于筛选
        :type SubscribeDBName: str
        :param Offset: 分页，页数
        :type Offset: int
        :param Limit: 分页，页大小
        :type Limit: int
        """
        self.InstanceId = None
        self.PubOrSubInstanceId = None
        self.PubOrSubInstanceIp = None
        self.PublishSubscribeId = None
        self.PublishSubscribeName = None
        self.PublishDBName = None
        self.SubscribeDBName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PubOrSubInstanceId = params.get("PubOrSubInstanceId")
        self.PubOrSubInstanceIp = params.get("PubOrSubInstanceIp")
        self.PublishSubscribeId = params.get("PublishSubscribeId")
        self.PublishSubscribeName = params.get("PublishSubscribeName")
        self.PublishDBName = params.get("PublishDBName")
        self.SubscribeDBName = params.get("SubscribeDBName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePublishSubscribeResponse(AbstractModel):
    """DescribePublishSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param PublishSubscribeSet: 发布订阅列表
        :type PublishSubscribeSet: list of PublishSubscribe
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PublishSubscribeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PublishSubscribeSet") is not None:
            self.PublishSubscribeSet = []
            for item in params.get("PublishSubscribeSet"):
                obj = PublishSubscribe()
                obj._deserialize(item)
                self.PublishSubscribeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReadOnlyGroupByReadOnlyInstanceRequest(AbstractModel):
    """DescribeReadOnlyGroupByReadOnlyInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeReadOnlyGroupByReadOnlyInstanceResponse(AbstractModel):
    """DescribeReadOnlyGroupByReadOnlyInstance返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param RegionId: 只读组的地域ID
        :type RegionId: str
        :param ZoneId: 只读组的可用区ID
        :type ZoneId: str
        :param IsOfflineDelay: 是否启动超时剔除功能 ,0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，单位是秒
        :type ReadOnlyMaxDelayTime: int
        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param Vip: 只读组vip
        :type Vip: str
        :param Vport: 只读组vport
        :type Vport: int
        :param VpcId: 只读组在私有网络ID
        :type VpcId: str
        :param SubnetId: 只读组在私有网络子网ID
        :type SubnetId: str
        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.RegionId = None
        self.ZoneId = None
        self.IsOfflineDelay = None
        self.ReadOnlyMaxDelayTime = None
        self.MinReadOnlyInGroup = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.MasterInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.IsOfflineDelay = params.get("IsOfflineDelay")
        self.ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self.MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.RequestId = params.get("RequestId")


class DescribeReadOnlyGroupDetailsRequest(AbstractModel):
    """DescribeReadOnlyGroupDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param ReadOnlyGroupId: 只读组ID，格式如：mssqlrg-3l3fgqn7
        :type ReadOnlyGroupId: str
        """
        self.InstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")


class DescribeReadOnlyGroupDetailsResponse(AbstractModel):
    """DescribeReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param RegionId: 只读组的地域ID，与主实例相同
        :type RegionId: str
        :param ZoneId: 只读组的可用区ID，与主实例相同
        :type ZoneId: str
        :param IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值
        :type ReadOnlyMaxDelayTime: int
        :param MinReadOnlyInGroup: 启动超时剔除功能后，至少只读组保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param Vip: 只读组vip
        :type Vip: str
        :param Vport: 只读组vport
        :type Vport: int
        :param VpcId: 只读组私有网络ID
        :type VpcId: str
        :param SubnetId: 只读组私有网络子网ID
        :type SubnetId: str
        :param ReadOnlyInstanceSet: 只读实例副本集合
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param Status: 只读组状态: 1-申请成功运行中，5-申请中
        :type Status: int
        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.RegionId = None
        self.ZoneId = None
        self.IsOfflineDelay = None
        self.ReadOnlyMaxDelayTime = None
        self.MinReadOnlyInGroup = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.ReadOnlyInstanceSet = None
        self.Status = None
        self.MasterInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.IsOfflineDelay = params.get("IsOfflineDelay")
        self.ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self.MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self.ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self.ReadOnlyInstanceSet.append(obj)
        self.Status = params.get("Status")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.RequestId = params.get("RequestId")


class DescribeReadOnlyGroupListRequest(AbstractModel):
    """DescribeReadOnlyGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeReadOnlyGroupListResponse(AbstractModel):
    """DescribeReadOnlyGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupSet: 只读组列表
        :type ReadOnlyGroupSet: list of ReadOnlyGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupSet") is not None:
            self.ReadOnlyGroupSet = []
            for item in params.get("ReadOnlyGroupSet"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self.ReadOnlyGroupSet.append(obj)
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
        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param Offset: 分页返回，页编号，默认值为第0页
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


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。
        :type InstanceIdSet: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIdSet = params.get("InstanceIdSet")


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param Cpu: 预购买实例的CPU核心数
        :type Cpu: int
        :param InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本，SI-基础版，默认取值HA
        :type InstanceType: str
        :param MachineType: 购买实例的宿主机类型，PM-物理机, CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘，默认取值PM
        :type MachineType: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.Period = None
        self.GoodsNum = None
        self.DBVersion = None
        self.Cpu = None
        self.InstanceType = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.DBVersion = params.get("DBVersion")
        self.Cpu = params.get("Cpu")
        self.InstanceType = params.get("InstanceType")
        self.MachineType = params.get("MachineType")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折前价格，其值除以100表示多少钱。例如10010表示100.10元
        :type OriginalPrice: int
        :param Price: 实际需要支付的价格，其值除以100表示多少钱。例如10010表示100.10元
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
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元
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
        :param Cpu: 实例升级后的CPU核心数，其值不能比当前实例CPU小
        :type Cpu: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Cpu = params.get("Cpu")


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元
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
        :param InstanceId: 实例ID
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
        :param InstanceId: 迁移源实例的ID，MigrateType=1(TencentDB for SQLServers)时使用，格式如：mssql-si2823jyl
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
        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param CreateTime: 迁移任务的创建时间
        :type CreateTime: str
        :param StartTime: 迁移任务的开始时间
        :type StartTime: str
        :param EndTime: 迁移任务的结束时间
        :type EndTime: str
        :param Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功,7已中止,8已删除,9中止中,10完成中,11中止失败,12完成失败）
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


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param BackupId: 要修改名称的备份ID，可通过DescribeBackups 接口获取。
        :type BackupId: int
        :param BackupName: 修改的备份名称
        :type BackupName: str
        """
        self.InstanceId = None
        self.BackupId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.BackupName = params.get("BackupName")


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupStrategyRequest(AbstractModel):
    """ModifyBackupStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param BackupType: 备份类型，当前只支持按天备份，取值为daily
        :type BackupType: str
        :param BackupTime: 备份时间点，取值为0-23的整数
        :type BackupTime: int
        :param BackupDay: BackupType取值为daily时，表示备份间隔天数。当前取值只能为1
        :type BackupDay: int
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupTime = None
        self.BackupDay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupTime = params.get("BackupTime")
        self.BackupDay = params.get("BackupDay")


class ModifyBackupStrategyResponse(AbstractModel):
    """ModifyBackupStrategy返回参数结构体

    """

    def __init__(self):
        """
        :param Errno: 返回错误码
        :type Errno: int
        :param Msg: 返回错误信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Errno = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Errno = params.get("Errno")
        self.Msg = params.get("Msg")
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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，格式如：mssql-c1nl9rpv 或者 mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param SecurityGroupIdSet: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIdSet: list of str
        """
        self.InstanceId = None
        self.SecurityGroupIdSet = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIdSet = params.get("SecurityGroupIdSet")


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
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
        :param FlowId: 任务流ID
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


class ModifyMaintenanceSpanRequest(AbstractModel):
    """ModifyMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        :param Weekly: 以周为单位，表示允许周几维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日，本参数不填，则不修改此值。
        :type Weekly: list of int
        :param StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始，本参数不填，则不修改此值。
        :type StartTime: str
        :param Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时，本参数不填，则不修改此值。
        :type Span: int
        """
        self.InstanceId = None
        self.Weekly = None
        self.StartTime = None
        self.Span = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")


class ModifyMaintenanceSpanResponse(AbstractModel):
    """ModifyMaintenanceSpan返回参数结构体

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
        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式），若不填则不修改
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


class ModifyPublishSubscribeNameRequest(AbstractModel):
    """ModifyPublishSubscribeName请求参数结构体

    """

    def __init__(self):
        """
        :param PublishSubscribeId: 发布订阅ID
        :type PublishSubscribeId: int
        :param PublishSubscribeName: 待修改的发布订阅名称
        :type PublishSubscribeName: str
        """
        self.PublishSubscribeId = None
        self.PublishSubscribeName = None


    def _deserialize(self, params):
        self.PublishSubscribeId = params.get("PublishSubscribeId")
        self.PublishSubscribeName = params.get("PublishSubscribeName")


class ModifyPublishSubscribeNameResponse(AbstractModel):
    """ModifyPublishSubscribeName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyReadOnlyGroupDetailsRequest(AbstractModel):
    """ModifyReadOnlyGroupDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称，不填此参数，则不修改
        :type ReadOnlyGroupName: str
        :param IsOfflineDelay: 是否启动超时剔除功能,0-不开启剔除功能，1-开启剔除功能，不填此参数，则不修改
        :type IsOfflineDelay: int
        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，不填此参数，则不修改
        :type ReadOnlyMaxDelayTime: int
        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数，不填此参数，则不修改
        :type MinReadOnlyInGroup: int
        :param WeightPairs: 只读组实例权重修改集合，不填此参数，则不修改
        :type WeightPairs: list of ReadOnlyInstanceWeightPair
        :param AutoWeight: 0-用户自定义权重（根据WeightPairs调整）,1-系统自动分配权重(WeightPairs无效)， 默认为0
        :type AutoWeight: int
        :param BalanceWeight: 0-不重新均衡负载，1-重新均衡负载，默认为0
        :type BalanceWeight: int
        """
        self.InstanceId = None
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.IsOfflineDelay = None
        self.ReadOnlyMaxDelayTime = None
        self.MinReadOnlyInGroup = None
        self.WeightPairs = None
        self.AutoWeight = None
        self.BalanceWeight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.IsOfflineDelay = params.get("IsOfflineDelay")
        self.ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self.MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        if params.get("WeightPairs") is not None:
            self.WeightPairs = []
            for item in params.get("WeightPairs"):
                obj = ReadOnlyInstanceWeightPair()
                obj._deserialize(item)
                self.WeightPairs.append(obj)
        self.AutoWeight = params.get("AutoWeight")
        self.BalanceWeight = params.get("BalanceWeight")


class ModifyReadOnlyGroupDetailsResponse(AbstractModel):
    """ModifyReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishSubscribe(AbstractModel):
    """发布订阅对象

    """

    def __init__(self):
        """
        :param Id: 发布订阅ID
        :type Id: int
        :param Name: 发布订阅名称
        :type Name: str
        :param PublishInstanceId: 发布实例ID
        :type PublishInstanceId: str
        :param PublishInstanceName: 发布实例名称
        :type PublishInstanceName: str
        :param PublishInstanceIp: 发布实例IP
        :type PublishInstanceIp: str
        :param SubscribeInstanceId: 订阅实例ID
        :type SubscribeInstanceId: str
        :param SubscribeInstanceName: 订阅实例名称
        :type SubscribeInstanceName: str
        :param SubscribeInstanceIp: 订阅实例IP
        :type SubscribeInstanceIp: str
        :param DatabaseTupleSet: 数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTupleStatus
        """
        self.Id = None
        self.Name = None
        self.PublishInstanceId = None
        self.PublishInstanceName = None
        self.PublishInstanceIp = None
        self.SubscribeInstanceId = None
        self.SubscribeInstanceName = None
        self.SubscribeInstanceIp = None
        self.DatabaseTupleSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.PublishInstanceId = params.get("PublishInstanceId")
        self.PublishInstanceName = params.get("PublishInstanceName")
        self.PublishInstanceIp = params.get("PublishInstanceIp")
        self.SubscribeInstanceId = params.get("SubscribeInstanceId")
        self.SubscribeInstanceName = params.get("SubscribeInstanceName")
        self.SubscribeInstanceIp = params.get("SubscribeInstanceIp")
        if params.get("DatabaseTupleSet") is not None:
            self.DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTupleStatus()
                obj._deserialize(item)
                self.DatabaseTupleSet.append(obj)


class QueryMigrationCheckProcessRequest(AbstractModel):
    """QueryMigrationCheckProcess请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class QueryMigrationCheckProcessResponse(AbstractModel):
    """QueryMigrationCheckProcess返回参数结构体

    """

    def __init__(self):
        """
        :param TotalStep: 总步骤数量
        :type TotalStep: int
        :param CurrentStep: 当前步骤编号，从1开始
        :type CurrentStep: int
        :param StepDetails: 所有步骤详情
        :type StepDetails: list of StepDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalStep = None
        self.CurrentStep = None
        self.StepDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalStep = params.get("TotalStep")
        self.CurrentStep = params.get("CurrentStep")
        if params.get("StepDetails") is not None:
            self.StepDetails = []
            for item in params.get("StepDetails"):
                obj = StepDetail()
                obj._deserialize(item)
                self.StepDetails.append(obj)
        self.RequestId = params.get("RequestId")


class ReadOnlyGroup(AbstractModel):
    """只读组对象

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param RegionId: 只读组的地域ID，与主实例相同
        :type RegionId: str
        :param ZoneId: 只读组的可用区ID，与主实例相同
        :type ZoneId: str
        :param IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值
        :type ReadOnlyMaxDelayTime: int
        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param Vip: 只读组vip
        :type Vip: str
        :param Vport: 只读组vport
        :type Vport: int
        :param VpcId: 只读组私有网络ID
        :type VpcId: str
        :param SubnetId: 只读组私有网络子网ID
        :type SubnetId: str
        :param Status: 只读组状态: 1-申请成功运行中，5-申请中
        :type Status: int
        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param ReadOnlyInstanceSet: 只读实例副本集合
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.RegionId = None
        self.ZoneId = None
        self.IsOfflineDelay = None
        self.ReadOnlyMaxDelayTime = None
        self.MinReadOnlyInGroup = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.MasterInstanceId = None
        self.ReadOnlyInstanceSet = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.IsOfflineDelay = params.get("IsOfflineDelay")
        self.ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self.MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.MasterInstanceId = params.get("MasterInstanceId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self.ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self.ReadOnlyInstanceSet.append(obj)


class ReadOnlyInstance(AbstractModel):
    """只读副本实例

    """

    def __init__(self):
        """
        :param InstanceId: 只读副本ID，格式如：mssqlro-3l3fgqn7
        :type InstanceId: str
        :param Name: 只读副本名称
        :type Name: str
        :param Uid: 只读副本唯一UID
        :type Uid: str
        :param ProjectId: 只读副本所在项目ID
        :type ProjectId: int
        :param Status: 只读副本状态。1：申请中 2：运行中 3：被延迟剔除 4：已隔离 5：回收中 6：已回收 7：任务执行中 8：已下线 9：实例扩容中 10：实例迁移中  12：重启中
        :type Status: int
        :param CreateTime: 只读副本创建时间
        :type CreateTime: str
        :param UpdateTime: 只读副本更新时间
        :type UpdateTime: str
        :param Memory: 只读副本内存大小，单位G
        :type Memory: int
        :param Storage: 只读副本存储空间大小，单位G
        :type Storage: int
        :param Cpu: 只读副本cpu核心数
        :type Cpu: int
        :param Version: 只读副本版本代号
        :type Version: str
        :param Type: 宿主机代号
        :type Type: str
        :param Model: 只读副本模式，2-单机
        :type Model: int
        :param PayMode: 只读副本计费模式，1-包年包月，0-按量计费
        :type PayMode: int
        :param Weight: 只读副本权重
        :type Weight: int
        :param DelayTime: 只读副本延迟时间，单位秒
        :type DelayTime: str
        :param SynStatus: 只读副本与主实例的同步状态。
Init:初始化
DeployReadOnlyInPorgress:部署副本进行中
DeployReadOnlySuccess:部署副本成功
DeployReadOnlyFail:部署副本失败
DeployMasterDBInPorgress:主节点上加入副本数据库进行中
DeployMasterDBSuccess:主节点上加入副本数据库成功
DeployMasterDBFail:主节点上加入副本数据库进失败
DeployReadOnlyDBInPorgress:副本还原加入数据库开始
DeployReadOnlyDBSuccess:副本还原加入数据库成功
DeployReadOnlyDBFail:副本还原加入数据库失败
SyncDelay:同步延迟
SyncFail:同步故障
SyncExcluded:已剔除只读组
SyncNormal:正常
        :type SynStatus: str
        :param DatabaseDifference: 只读副本与主实例没有同步的库
        :type DatabaseDifference: str
        :param AccountDifference: 只读副本与主实例没有同步的账户
        :type AccountDifference: str
        :param StartTime: 只读副本计费开始时间
        :type StartTime: str
        :param EndTime: 只读副本计费结束时间
        :type EndTime: str
        :param IsolateTime: 只读副本隔离时间
        :type IsolateTime: str
        """
        self.InstanceId = None
        self.Name = None
        self.Uid = None
        self.ProjectId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Memory = None
        self.Storage = None
        self.Cpu = None
        self.Version = None
        self.Type = None
        self.Model = None
        self.PayMode = None
        self.Weight = None
        self.DelayTime = None
        self.SynStatus = None
        self.DatabaseDifference = None
        self.AccountDifference = None
        self.StartTime = None
        self.EndTime = None
        self.IsolateTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Cpu = params.get("Cpu")
        self.Version = params.get("Version")
        self.Type = params.get("Type")
        self.Model = params.get("Model")
        self.PayMode = params.get("PayMode")
        self.Weight = params.get("Weight")
        self.DelayTime = params.get("DelayTime")
        self.SynStatus = params.get("SynStatus")
        self.DatabaseDifference = params.get("DatabaseDifference")
        self.AccountDifference = params.get("AccountDifference")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsolateTime = params.get("IsolateTime")


class ReadOnlyInstanceWeightPair(AbstractModel):
    """只读实例与权重对应关系

    """

    def __init__(self):
        """
        :param ReadOnlyInstanceId: 只读实例ID，格式如：mssqlro-3l3fgqn7
        :type ReadOnlyInstanceId: str
        :param ReadOnlyWeight: 只读实例权重 ，范围是0-100
        :type ReadOnlyWeight: int
        """
        self.ReadOnlyInstanceId = None
        self.ReadOnlyWeight = None


    def _deserialize(self, params):
        self.ReadOnlyInstanceId = params.get("ReadOnlyInstanceId")
        self.ReadOnlyWeight = params.get("ReadOnlyWeight")


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


class RemoveBackupsRequest(AbstractModel):
    """RemoveBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param BackupNames: 待删除的备份名称，备份名称可通过DescribeBackups接口的FileName字段获得。单次请求批量删除备份数不能超过10个。
        :type BackupNames: list of str
        """
        self.InstanceId = None
        self.BackupNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupNames = params.get("BackupNames")


class RemoveBackupsResponse(AbstractModel):
    """RemoveBackups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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


class RenewPostpaidDBInstanceRequest(AbstractModel):
    """RenewPostpaidDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class RenewPostpaidDBInstanceResponse(AbstractModel):
    """RenewPostpaidDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class SecurityGroup(AbstractModel):
    """安全组

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param InboundSet: 入站规则
        :type InboundSet: list of SecurityGroupPolicy
        :param OutboundSet: 出站规则
        :type OutboundSet: list of SecurityGroupPolicy
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self.ProjectId = None
        self.CreateTime = None
        self.InboundSet = None
        self.OutboundSet = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("InboundSet") is not None:
            self.InboundSet = []
            for item in params.get("InboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.InboundSet.append(obj)
        if params.get("OutboundSet") is not None:
            self.OutboundSet = []
            for item in params.get("OutboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.OutboundSet.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")


class SecurityGroupPolicy(AbstractModel):
    """安全组策略

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param CidrIp: 目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param PortRange: 端口或者端口范围
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP等
        :type IpProtocol: str
        :param Dir: 规则限定的方向，OUTPUT-出战规则  INPUT-进站规则
        :type Dir: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")


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


class StartMigrationCheckRequest(AbstractModel):
    """StartMigrationCheck请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务id
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class StartMigrationCheckResponse(AbstractModel):
    """StartMigrationCheck返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 迁移检查流程发起后，返回的流程id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class StepDetail(AbstractModel):
    """进度步骤详情

    """

    def __init__(self):
        """
        :param Msg: 具体步骤返回信息
        :type Msg: str
        :param Status: 当前步骤状态，0成功，-2未开始
        :type Status: int
        :param Name: 步骤名称
        :type Name: str
        """
        self.Msg = None
        self.Status = None
        self.Name = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.Status = params.get("Status")
        self.Name = params.get("Name")


class StopMigrationRequest(AbstractModel):
    """StopMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class StopMigrationResponse(AbstractModel):
    """StopMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 中止迁移流程发起后，返回的流程id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


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
        :param Cpu: 实例升级后的CPU核心数
        :type Cpu: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.Cpu = params.get("Cpu")


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