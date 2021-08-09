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


class AccountCreateInfo(AbstractModel):
    """账号创建信息

    """

    def __init__(self):
        """
        :param UserName: 实例用户名\n        :type UserName: str\n        :param Password: 实例密码\n        :type Password: str\n        :param DBPrivileges: DB权限列表\n        :type DBPrivileges: list of DBPrivilege\n        :param Remark: 账号备注信息\n        :type Remark: str\n        :param IsAdmin: 是否为管理员账户，默认为否\n        :type IsAdmin: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountDetail(AbstractModel):
    """账户信息详情

    """

    def __init__(self):
        """
        :param Name: 账户名\n        :type Name: str\n        :param Remark: 账户备注\n        :type Remark: str\n        :param CreateTime: 账户创建时间\n        :type CreateTime: str\n        :param Status: 账户状态，1-创建中，2-正常，3-修改中，4-密码重置中，-1-删除中\n        :type Status: int\n        :param UpdateTime: 账户更新时间\n        :type UpdateTime: str\n        :param PassTime: 密码更新时间\n        :type PassTime: str\n        :param InternalStatus: 账户内部状态，正常为enable\n        :type InternalStatus: str\n        :param Dbs: 该账户对相关db的读写权限信息\n        :type Dbs: list of DBPrivilege\n        :param IsAdmin: 是否为管理员账户\n        :type IsAdmin: bool\n        """
        self.Name = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.UpdateTime = None
        self.PassTime = None
        self.InternalStatus = None
        self.Dbs = None
        self.IsAdmin = None


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
        self.IsAdmin = params.get("IsAdmin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPassword(AbstractModel):
    """实例账号密码信息

    """

    def __init__(self):
        """
        :param UserName: 用户名\n        :type UserName: str\n        :param Password: 密码\n        :type Password: str\n        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilege(AbstractModel):
    """数据库账号权限信息。创建数据库时设置

    """

    def __init__(self):
        """
        :param UserName: 数据库用户名\n        :type UserName: str\n        :param Privilege: 数据库权限。ReadWrite表示可读写，ReadOnly表示只读\n        :type Privilege: str\n        """
        self.UserName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilegeModifyInfo(AbstractModel):
    """数据库账号权限变更信息

    """

    def __init__(self):
        """
        :param UserName: 数据库用户名\n        :type UserName: str\n        :param DBPrivileges: 账号权限变更信息\n        :type DBPrivileges: list of DBPrivilegeModifyInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountRemark(AbstractModel):
    """账户备注信息

    """

    def __init__(self):
        """
        :param UserName: 账户名\n        :type UserName: str\n        :param Remark: 对应账户新的备注信息\n        :type Remark: str\n        """
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组ID。\n        :type SecurityGroupId: str\n        :param InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。\n        :type InstanceIdSet: list of str\n        """
        self.SecurityGroupId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backup(AbstractModel):
    """备份文件详细信息

    """

    def __init__(self):
        """
        :param FileName: 文件名\n        :type FileName: str\n        :param Size: 文件大小，单位 KB\n        :type Size: int\n        :param StartTime: 备份开始时间\n        :type StartTime: str\n        :param EndTime: 备份结束时间\n        :type EndTime: str\n        :param InternalAddr: 内网下载地址\n        :type InternalAddr: str\n        :param ExternalAddr: 外网下载地址\n        :type ExternalAddr: str\n        :param Id: 备份文件唯一标识，RestoreInstance接口会用到该字段\n        :type Id: int\n        :param Status: 备份文件状态（0-创建中；1-成功；2-失败）\n        :type Status: int\n        :param DBs: 多库备份时的DB列表\n        :type DBs: list of str\n        :param Strategy: 备份策略（0-实例备份；1-多库备份）\n        :type Strategy: int\n        :param BackupWay: 备份方式，0-定时备份；1-手动临时备份\n        :type BackupWay: int\n        :param BackupName: 备份名称，可自定义\n        :type BackupName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBRequest(AbstractModel):
    """CloneDB请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param RenameRestore: 按照ReNameRestoreDatabase中的库进行克隆，并重命名，新库名称必须指定\n        :type RenameRestore: list of RenameRestoreDatabase\n        """
        self.InstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBResponse(AbstractModel):
    """CloneDB返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步流程任务ID，使用FlowId调用DescribeFlowStatus接口获取任务执行状态\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CompleteExpansionRequest(AbstractModel):
    """CompleteExpansion请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteExpansionResponse(AbstractModel):
    """CompleteExpansion返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrationResponse(AbstractModel):
    """CompleteMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 完成迁移流程发起后，返回的流程id\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CosUploadBackupFile(AbstractModel):
    """查询已经上传的备份文件大小。

    """

    def __init__(self):
        """
        :param FileName: 备份名称\n        :type FileName: str\n        :param Size: 备份大小\n        :type Size: int\n        """
        self.FileName = None
        self.Size = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param Accounts: 数据库实例账户信息\n        :type Accounts: list of AccountCreateInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateBackupMigrationRequest(AbstractModel):
    """CreateBackupMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param RecoveryType: 迁移任务恢复类型，FULL-全量备份恢复，FULL_LOG-全量备份+事务日志恢复，FULL_DIFF-全量备份+差异备份恢复\n        :type RecoveryType: str\n        :param UploadType: 备份上传类型，COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，需要用户上传。\n        :type UploadType: str\n        :param MigrationName: 任务名称\n        :type MigrationName: str\n        :param BackupFiles: UploadType是COS_URL时这里填URL，COS_UPLOAD这里填备份文件的名字。只支持1个备份文件，但1个备份文件内可包含多个库\n        :type BackupFiles: list of str\n        """
        self.InstanceId = None
        self.RecoveryType = None
        self.UploadType = None
        self.MigrationName = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.MigrationName = params.get("MigrationName")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupMigrationResponse(AbstractModel):
    """CreateBackupMigration返回参数结构体

    """

    def __init__(self):
        """
        :param BackupMigrationId: 备份导入任务ID\n        :type BackupMigrationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BackupMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param Strategy: 备份策略(0-实例备份 1-多库备份)\n        :type Strategy: int\n        :param DBNames: 需要备份库名的列表(多库备份才填写)\n        :type DBNames: list of str\n        :param InstanceId: 实例ID，形如mssql-i1z41iwd\n        :type InstanceId: str\n        :param BackupName: 备份名称，若不填则自动生成“实例ID_备份开始时间戳”\n        :type BackupName: str\n        """
        self.Strategy = None
        self.DBNames = None
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.Strategy = params.get("Strategy")
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取\n        :type Zone: str\n        :param Cpu: 实例的CPU核心数\n        :type Cpu: int\n        :param Memory: 实例内存大小，单位GB\n        :type Memory: int\n        :param Storage: 实例磁盘大小，单位GB\n        :type Storage: int\n        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa\n        :type SubnetId: str\n        :param VpcId: VPC网络ID，形如vpc-dsp338hz\n        :type VpcId: str\n        :param MachineType: 购买实例的宿主机类型, CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘\n        :type MachineType: str\n        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。\n        :type InstanceChargeType: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param GoodsNum: 本次购买几个实例，默认值为1。取值不超过10\n        :type GoodsNum: int\n        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard），2017（SQL Server 2017 Enterprise），201202（SQL Server 2012 Standard），201402（SQL Server 2014 Standard），2014SP2（SQL Server 2014 Enterprise），201702（SQL Server 2017 Standard）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。\n        :type DBVersion: str\n        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48\n        :type Period: int\n        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID\n        :type SecurityGroupList: list of str\n        :param AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。\n        :type AutoRenewFlag: int\n        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张\n        :type VoucherIds: list of str\n        :param Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末\n        :type Weekly: list of int\n        :param StartTime: 可维护时间窗配置，每天可维护的开始时间\n        :type StartTime: str\n        :param Span: 可维护时间窗配置，持续时间，单位：小时\n        :type Span: int\n        :param ResourceTags: 新建实例绑定的标签集合\n        :type ResourceTags: list of ResourceTag\n        """
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
        self.ResourceTags = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDBInstancesResponse(AbstractModel):
    """CreateBasicDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称\n        :type DealName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取\n        :type Zone: str\n        :param Memory: 实例内存大小，单位GB\n        :type Memory: int\n        :param Storage: 实例磁盘大小，单位GB\n        :type Storage: int\n        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。\n        :type InstanceChargeType: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param GoodsNum: 本次购买几个实例，默认值为1。取值不超过10\n        :type GoodsNum: int\n        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置\n        :type SubnetId: str\n        :param VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置\n        :type VpcId: str\n        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48\n        :type Period: int\n        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张\n        :type VoucherIds: list of str\n        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。\n        :type DBVersion: str\n        :param AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。\n        :type AutoRenewFlag: int\n        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID\n        :type SecurityGroupList: list of str\n        :param Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末\n        :type Weekly: list of int\n        :param StartTime: 可维护时间窗配置，每天可维护的开始时间\n        :type StartTime: str\n        :param Span: 可维护时间窗配置，持续时间，单位：小时\n        :type Span: int\n        :param HAType: 购买高可用实例的类型：DUAL-双机高可用  CLUSTER-集群，默认值为DUAL\n        :type HAType: str\n        :param MultiZones: 是否跨可用区部署，默认值为false\n        :type MultiZones: bool\n        :param ResourceTags: 新建实例绑定的标签集合\n        :type ResourceTags: list of ResourceTag\n        """
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
        self.ResourceTags = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称\n        :type DealName: str\n        :param DealNames: 订单名称数组\n        :type DealNames: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param DBs: 数据库创建信息\n        :type DBs: list of DBCreateInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBResponse(AbstractModel):
    """CreateDB返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateIncrementalMigrationRequest(AbstractModel):
    """CreateIncrementalMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param BackupFiles: 增量备份文件，全量备份任务UploadType是COS_URL时这里填URL，是COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库\n        :type BackupFiles: list of str\n        :param IsRecovery: 是否需要恢复，NO-不需要，YES-需要，默认不需要\n        :type IsRecovery: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.BackupFiles = None
        self.IsRecovery = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.BackupFiles = params.get("BackupFiles")
        self.IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIncrementalMigrationResponse(AbstractModel):
    """CreateIncrementalMigration返回参数结构体

    """

    def __init__(self):
        """
        :param IncrementalMigrationId: 增量备份导入任务ID\n        :type IncrementalMigrationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IncrementalMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.RequestId = params.get("RequestId")


class CreateMigrationRequest(AbstractModel):
    """CreateMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateName: 迁移任务的名称\n        :type MigrateName: str\n        :param MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）\n        :type MigrateType: int\n        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）\n        :type SourceType: int\n        :param Source: 迁移源\n        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`\n        :param Target: 迁移目标\n        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`\n        :param MigrateDBSet: 迁移DB对象 ，离线迁移不使用（SourceType=4或SourceType=5）。\n        :type MigrateDBSet: list of MigrateDB\n        :param RenameRestore: 按照ReNameRestoreDatabase中的库进行恢复，并重命名，不填则按照默认方式命名恢复的库，且恢复所有的库。SourceType=5的情况下有效。\n        :type RenameRestore: list of RenameRestoreDatabase\n        """
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None
        self.RenameRestore = None


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
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationResponse(AbstractModel):
    """CreateMigration返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PublishInstanceId: 发布实例ID，形如mssql-j8kv137v\n        :type PublishInstanceId: str\n        :param SubscribeInstanceId: 订阅实例ID，形如mssql-j8kv137v\n        :type SubscribeInstanceId: str\n        :param DatabaseTupleSet: 数据库的订阅发布关系集合\n        :type DatabaseTupleSet: list of DatabaseTuple\n        :param PublishSubscribeName: 发布订阅的名称，默认值为：default_name\n        :type PublishSubscribeName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePublishSubscribeResponse(AbstractModel):
    """CreatePublishSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        :param Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取\n        :type Zone: str\n        :param ReadOnlyGroupType: 只读组类型选项，1-按照一个实例一个只读组的方式发货，2-新建只读组后发货，所有实例都在这个只读组下面， 3-发货的所有实例都在已有的只读组下面\n        :type ReadOnlyGroupType: int\n        :param Memory: 实例内存大小，单位GB\n        :type Memory: int\n        :param Storage: 实例磁盘大小，单位GB\n        :type Storage: int\n        :param ReadOnlyGroupForcedUpgrade: 0-默认不升级主实例，1-强制升级主实例完成ro部署；主实例为非集群版时需要填1，强制升级为集群版。填1 说明您已同意将主实例升级到集群版实例。\n        :type ReadOnlyGroupForcedUpgrade: int\n        :param ReadOnlyGroupId: ReadOnlyGroupType=3时必填,已存在的只读组ID\n        :type ReadOnlyGroupId: str\n        :param ReadOnlyGroupName: ReadOnlyGroupType=2时必填，新建的只读组名称\n        :type ReadOnlyGroupName: str\n        :param ReadOnlyGroupIsOfflineDelay: ReadOnlyGroupType=2时必填，新建的只读组是否开启延迟剔除功能，1-开启，0-关闭。当只读副本与主实例延迟大于阈值后，自动剔除。\n        :type ReadOnlyGroupIsOfflineDelay: int\n        :param ReadOnlyGroupMaxDelayTime: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除的阈值。\n        :type ReadOnlyGroupMaxDelayTime: int\n        :param ReadOnlyGroupMinInGroup: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除后至少保留只读副本的个数。\n        :type ReadOnlyGroupMinInGroup: int\n        :param InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。\n        :type InstanceChargeType: str\n        :param GoodsNum: 本次购买几个只读实例，默认值为1。\n        :type GoodsNum: int\n        :param SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置\n        :type SubnetId: str\n        :param VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置\n        :type VpcId: str\n        :param Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48\n        :type Period: int\n        :param SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID\n        :type SecurityGroupList: list of str\n        :param AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID数组，目前单个订单只能使用一张\n        :type VoucherIds: list of str\n        :param ResourceTags: 新建实例绑定的标签集合\n        :type ResourceTags: list of ResourceTag\n        """
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
        self.ResourceTags = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstancesResponse(AbstractModel):
    """CreateReadOnlyDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单名称数组\n        :type DealNames: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DBName: 数据库名\n        :type DBName: str\n        :param Charset: 字符集。可通过接口DescribeDBCharsets查到支持的字符集，不填默认为Chinese_PRC_CI_AS。\n        :type Charset: str\n        :param Accounts: 数据库账号权限信息\n        :type Accounts: list of AccountPrivilege\n        :param Remark: 备注\n        :type Remark: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBDetail(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        """
        :param Name: 数据库名称\n        :type Name: str\n        :param Charset: 字符集\n        :type Charset: str\n        :param Remark: 备注\n        :type Remark: str\n        :param CreateTime: 数据库创建时间\n        :type CreateTime: str\n        :param Status: 数据库状态。1--创建中， 2--运行中， 3--修改中，-1--删除中\n        :type Status: int\n        :param Accounts: 数据库账号权限信息\n        :type Accounts: list of AccountPrivilege\n        :param InternalStatus: 内部状态。ONLINE表示运行中\n        :type InternalStatus: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Name: 实例名称\n        :type Name: str\n        :param ProjectId: 实例所在项目ID\n        :type ProjectId: int\n        :param RegionId: 实例所在地域ID\n        :type RegionId: int\n        :param ZoneId: 实例所在可用区ID\n        :type ZoneId: int\n        :param VpcId: 实例所在私有网络ID，基础网络时为 0\n        :type VpcId: int\n        :param SubnetId: 实例所在私有网络子网ID，基础网络时为 0\n        :type SubnetId: int\n        :param Status: 实例状态。取值范围： <li>1：申请中</li> <li>2：运行中</li> <li>3：受限运行中 (主备切换中)</li> <li>4：已隔离</li> <li>5：回收中</li> <li>6：已回收</li> <li>7：任务执行中 (实例做备份、回档等操作)</li> <li>8：已下线</li> <li>9：实例扩容中</li> <li>10：实例迁移中</li> <li>11：只读</li> <li>12：重启中</li>\n        :type Status: int\n        :param Vip: 实例访问IP\n        :type Vip: str\n        :param Vport: 实例访问端口\n        :type Vport: int\n        :param CreateTime: 实例创建时间\n        :type CreateTime: str\n        :param UpdateTime: 实例更新时间\n        :type UpdateTime: str\n        :param StartTime: 实例计费开始时间\n        :type StartTime: str\n        :param EndTime: 实例计费结束时间\n        :type EndTime: str\n        :param IsolateTime: 实例隔离时间\n        :type IsolateTime: str\n        :param Memory: 实例内存大小，单位G\n        :type Memory: int\n        :param UsedStorage: 实例已经使用存储空间大小，单位G\n        :type UsedStorage: int\n        :param Storage: 实例存储空间大小，单位G\n        :type Storage: int\n        :param VersionName: 实例版本\n        :type VersionName: str\n        :param RenewFlag: 实例续费标记，0-正常续费，1-自动续费，2-到期不续费\n        :type RenewFlag: int\n        :param Model: 实例高可用， 1-双机高可用，2-单机，3-跨可用区，4-集群跨可用区，5-集群，9-自研机房\n        :type Model: int\n        :param Region: 实例所在地域名称，如 ap-guangzhou\n        :type Region: str\n        :param Zone: 实例所在可用区名称，如 ap-guangzhou-1\n        :type Zone: str\n        :param BackupTime: 备份时间点\n        :type BackupTime: str\n        :param PayMode: 实例付费模式， 0-按量计费，1-包年包月\n        :type PayMode: int\n        :param Uid: 实例唯一UID\n        :type Uid: str\n        :param Cpu: 实例cpu核心数\n        :type Cpu: int\n        :param Version: 实例版本代号\n        :type Version: str\n        :param Type: 物理机代号\n        :type Type: str\n        :param Pid: 计费ID\n        :type Pid: int\n        :param UniqVpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，基础网络时为空字符串\n        :type UniqVpcId: str\n        :param UniqSubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，基础网络时为空字符串\n        :type UniqSubnetId: str\n        :param IsolateOperator: 实例隔离操作
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsolateOperator: str\n        :param SubFlag: 发布订阅标识，SUB-订阅实例，PUB-发布实例，空值-没有发布订阅的普通实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubFlag: str\n        :param ROFlag: 只读标识，RO-只读实例，MASTER-有RO实例的主实例，空值-没有只读组的非RO实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type ROFlag: str\n        :param HAFlag: 容灾类型，MIRROR-镜像，ALWAYSON-AlwaysOn, SINGLE-单例
注意：此字段可能返回 null，表示取不到有效值。\n        :type HAFlag: str\n        :param ResourceTags: 实例绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceTags: list of ResourceTag\n        """
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
        self.ResourceTags = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilege(AbstractModel):
    """账号的数据库权限信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名\n        :type DBName: str\n        :param Privilege: 数据库权限，ReadWrite表示可读写，ReadOnly表示只读\n        :type Privilege: str\n        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilegeModifyInfo(AbstractModel):
    """数据库权限变更信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名\n        :type DBName: str\n        :param Privilege: 权限变更信息。ReadWrite表示可读写，ReadOnly表示只读，Delete表示删除账号对该DB的权限\n        :type Privilege: str\n        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBRemark(AbstractModel):
    """数据库备注信息

    """

    def __init__(self):
        """
        :param Name: 数据库名称\n        :type Name: str\n        :param Remark: 备注信息\n        :type Remark: str\n        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTuple(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库。

    """

    def __init__(self):
        """
        :param PublishDatabase: 发布数据库名称\n        :type PublishDatabase: str\n        :param SubscribeDatabase: 订阅数据库名称\n        :type SubscribeDatabase: str\n        """
        self.PublishDatabase = None
        self.SubscribeDatabase = None


    def _deserialize(self, params):
        self.PublishDatabase = params.get("PublishDatabase")
        self.SubscribeDatabase = params.get("SubscribeDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTupleStatus(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库，以及其之间发布订阅的状态信息。

    """

    def __init__(self):
        """
        :param PublishDatabase: 发布数据库名称\n        :type PublishDatabase: str\n        :param SubscribeDatabase: 订阅数据库名称\n        :type SubscribeDatabase: str\n        :param LastSyncTime: 最近一次同步时间\n        :type LastSyncTime: str\n        :param Status: 数据库之间的发布订阅状态 running，success，fail，unknow\n        :type Status: str\n        """
        self.PublishDatabase = None
        self.SubscribeDatabase = None
        self.LastSyncTime = None
        self.Status = None


    def _deserialize(self, params):
        self.PublishDatabase = params.get("PublishDatabase")
        self.SubscribeDatabase = params.get("SubscribeDatabase")
        self.LastSyncTime = params.get("LastSyncTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbNormalDetail(AbstractModel):
    """数据库配置信息

    """

    def __init__(self):
        """
        :param IsSubscribed: 是否已订阅 0：否 1：是\n        :type IsSubscribed: str\n        :param CollationName: 数据库排序规则\n        :type CollationName: str\n        :param IsAutoCleanupOn: 开启CT之后是否自动清理 0：否 1：是\n        :type IsAutoCleanupOn: str\n        :param IsBrokerEnabled: 是否已启用代理  0：否 1：是\n        :type IsBrokerEnabled: str\n        :param IsCdcEnabled: 是否已开启/关闭CDC 0：关闭 1：开启\n        :type IsCdcEnabled: str\n        :param IsDbChainingOn: 是否已启用/ 禁用CT 0：禁用 1：启用\n        :type IsDbChainingOn: str\n        :param IsEncrypted: 是否加密 0：否 1：是\n        :type IsEncrypted: str\n        :param IsFulltextEnabled: 是否全文启用 0：否 1：是\n        :type IsFulltextEnabled: str\n        :param IsMirroring: 是否是镜像 0：否 1：是\n        :type IsMirroring: str\n        :param IsPublished: 是否已发布 0：否 1：是\n        :type IsPublished: str\n        :param IsReadCommittedSnapshotOn: 是否开启快照 0：否 1：是\n        :type IsReadCommittedSnapshotOn: str\n        :param IsTrustworthyOn: 是否可信任 0：否 1：是\n        :type IsTrustworthyOn: str\n        :param MirroringState: 镜像状态\n        :type MirroringState: str\n        :param Name: 数据库名称\n        :type Name: str\n        :param RecoveryModelDesc: 恢复模式\n        :type RecoveryModelDesc: str\n        :param RetentionPeriod: 保留天数\n        :type RetentionPeriod: str\n        :param StateDesc: 数据库状态\n        :type StateDesc: str\n        :param UserAccessDesc: 用户类型\n        :type UserAccessDesc: str\n        """
        self.IsSubscribed = None
        self.CollationName = None
        self.IsAutoCleanupOn = None
        self.IsBrokerEnabled = None
        self.IsCdcEnabled = None
        self.IsDbChainingOn = None
        self.IsEncrypted = None
        self.IsFulltextEnabled = None
        self.IsMirroring = None
        self.IsPublished = None
        self.IsReadCommittedSnapshotOn = None
        self.IsTrustworthyOn = None
        self.MirroringState = None
        self.Name = None
        self.RecoveryModelDesc = None
        self.RetentionPeriod = None
        self.StateDesc = None
        self.UserAccessDesc = None


    def _deserialize(self, params):
        self.IsSubscribed = params.get("IsSubscribed")
        self.CollationName = params.get("CollationName")
        self.IsAutoCleanupOn = params.get("IsAutoCleanupOn")
        self.IsBrokerEnabled = params.get("IsBrokerEnabled")
        self.IsCdcEnabled = params.get("IsCdcEnabled")
        self.IsDbChainingOn = params.get("IsDbChainingOn")
        self.IsEncrypted = params.get("IsEncrypted")
        self.IsFulltextEnabled = params.get("IsFulltextEnabled")
        self.IsMirroring = params.get("IsMirroring")
        self.IsPublished = params.get("IsPublished")
        self.IsReadCommittedSnapshotOn = params.get("IsReadCommittedSnapshotOn")
        self.IsTrustworthyOn = params.get("IsTrustworthyOn")
        self.MirroringState = params.get("MirroringState")
        self.Name = params.get("Name")
        self.RecoveryModelDesc = params.get("RecoveryModelDesc")
        self.RetentionPeriod = params.get("RetentionPeriod")
        self.StateDesc = params.get("StateDesc")
        self.UserAccessDesc = params.get("UserAccessDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbRollbackTimeInfo(AbstractModel):
    """数据库可回档时间范围信息

    """

    def __init__(self):
        """
        :param DBName: 数据库名称\n        :type DBName: str\n        :param StartTime: 可回档开始时间\n        :type StartTime: str\n        :param EndTime: 可回档结束时间\n        :type EndTime: str\n        """
        self.DBName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单名\n        :type DealName: str\n        :param Count: 商品数量\n        :type Count: int\n        :param FlowId: 关联的流程 ID，可用于查询流程执行状态\n        :type FlowId: int\n        :param InstanceIdSet: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。\n        :type InstanceIdSet: list of str\n        :param OwnerUin: 所属账号\n        :type OwnerUin: str\n        :param InstanceChargeType: 实例付费类型\n        :type InstanceChargeType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param UserNames: 实例用户名数组\n        :type UserNames: list of str\n        """
        self.InstanceId = None
        self.UserNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserNames = params.get("UserNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteBackupMigrationRequest(AbstractModel):
    """DeleteBackupMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 目标实例ID，由DescribeBackupMigration接口返回\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由DescribeBackupMigration接口返回\n        :type BackupMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupMigrationResponse(AbstractModel):
    """DeleteBackupMigration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBInstanceResponse(AbstractModel):
    """DeleteDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDBRequest(AbstractModel):
    """DeleteDB请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-rljoi3bf\n        :type InstanceId: str\n        :param Names: 数据库名数组\n        :type Names: list of str\n        """
        self.InstanceId = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBResponse(AbstractModel):
    """DeleteDB返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteIncrementalMigrationRequest(AbstractModel):
    """DeleteIncrementalMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param IncrementalMigrationId: 增量备份导入任务ID，由CreateIncrementalMigration接口返回\n        :type IncrementalMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIncrementalMigrationResponse(AbstractModel):
    """DeleteIncrementalMigration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePublishSubscribeRequest(AbstractModel):
    """DeletePublishSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param PublishSubscribeId: 发布订阅ID，可通过DescribePublishSubscribe接口获得\n        :type PublishSubscribeId: int\n        :param DatabaseTupleSet: 待删除的数据库的订阅发布关系集合\n        :type DatabaseTupleSet: list of DatabaseTuple\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePublishSubscribeResponse(AbstractModel):
    """DeletePublishSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20\n        :type Limit: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Accounts: 账户信息列表\n        :type Accounts: list of AccountDetail\n        :param TotalCount: 总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        :param FlowId: 创建备份流程ID，可通过 [CreateBackup](https://cloud.tencent.com/document/product/238/19946) 接口获取\n        :type FlowId: str\n        """
        self.InstanceId = None
        self.FlowId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupByFlowIdResponse(AbstractModel):
    """DescribeBackupByFlowId返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 备份文件唯一标识，RestoreInstance接口会用到该字段\n        :type Id: int\n        :param FileName: 存储文件名\n        :type FileName: str\n        :param BackupName: 备份名称，可自定义\n        :type BackupName: str\n        :param StartTime: 备份开始时间\n        :type StartTime: str\n        :param EndTime: 备份结束时间\n        :type EndTime: str\n        :param Size: 文件大小，单位 KB\n        :type Size: int\n        :param Strategy: 备份策略，0-实例备份；1-多库备份；实例状态是0-创建中时，该字段为默认值0，无实际意义\n        :type Strategy: int\n        :param BackupWay: 备份方式，0-定时备份；1-手动临时备份；实例状态是0-创建中时，该字段为默认值0，无实际意义\n        :type BackupWay: int\n        :param Status: 备份文件状态，0-创建中；1-成功；2-失败\n        :type Status: int\n        :param DBs: 多库备份时的DB列表\n        :type DBs: list of str\n        :param InternalAddr: 内网下载地址\n        :type InternalAddr: str\n        :param ExternalAddr: 外网下载地址\n        :type ExternalAddr: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeBackupCommandRequest(AbstractModel):
    """DescribeBackupCommand请求参数结构体

    """

    def __init__(self):
        """
        :param BackupFileType: 备份文件类型，FULL-全量备份，FULL_LOG-全量备份需要日志增量，FULL_DIFF-全量备份需要差异增量，LOG-日志备份，DIFF-差异备份\n        :type BackupFileType: str\n        :param DataBaseName: 数据库名称\n        :type DataBaseName: str\n        :param IsRecovery: 是否需要恢复，NO-不需要，YES-需要\n        :type IsRecovery: str\n        :param LocalPath: 备份文件保存的路径；如果不填则默认在D:\\\n        :type LocalPath: str\n        """
        self.BackupFileType = None
        self.DataBaseName = None
        self.IsRecovery = None
        self.LocalPath = None


    def _deserialize(self, params):
        self.BackupFileType = params.get("BackupFileType")
        self.DataBaseName = params.get("DataBaseName")
        self.IsRecovery = params.get("IsRecovery")
        self.LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupCommandResponse(AbstractModel):
    """DescribeBackupCommand返回参数结构体

    """

    def __init__(self):
        """
        :param Command: 创建备份命令\n        :type Command: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Command = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.RequestId = params.get("RequestId")


class DescribeBackupMigrationRequest(AbstractModel):
    """DescribeBackupMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param MigrationName: 导入任务名称\n        :type MigrationName: str\n        :param BackupFileName: 备份文件名称\n        :type BackupFileName: str\n        :param StatusSet: 导入任务状态集合\n        :type StatusSet: list of int\n        :param RecoveryType: 导入任务恢复类型，FULL,FULL_LOG,FULL_DIFF\n        :type RecoveryType: str\n        :param UploadType: COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传\n        :type UploadType: str\n        :param Limit: 分页，页大小，默认值：100\n        :type Limit: int\n        :param Offset: 分页，页数，默认值：0\n        :type Offset: int\n        :param OrderBy: 排序字段，name；createTime；startTime；endTime，默认按照createTime递增排序。\n        :type OrderBy: str\n        :param OrderByType: 排序方式，desc-递减排序，asc-递增排序。默认按照asc排序，且在OrderBy为有效值时，本参数有效\n        :type OrderByType: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.MigrationName = None
        self.BackupFileName = None
        self.StatusSet = None
        self.RecoveryType = None
        self.UploadType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.MigrationName = params.get("MigrationName")
        self.BackupFileName = params.get("BackupFileName")
        self.StatusSet = params.get("StatusSet")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupMigrationResponse(AbstractModel):
    """DescribeBackupMigration返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 迁移任务总数\n        :type TotalCount: int\n        :param BackupMigrationSet: 迁移任务集合\n        :type BackupMigrationSet: list of Migration\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.BackupMigrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupMigrationSet") is not None:
            self.BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self.BackupMigrationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupUploadSizeRequest(AbstractModel):
    """DescribeBackupUploadSize请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param IncrementalMigrationId: 增量导入任务ID\n        :type IncrementalMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUploadSizeResponse(AbstractModel):
    """DescribeBackupUploadSize返回参数结构体

    """

    def __init__(self):
        """
        :param CosUploadBackupFileSet: 已上传的备份的信息\n        :type CosUploadBackupFileSet: list of CosUploadBackupFile\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CosUploadBackupFileSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CosUploadBackupFileSet") is not None:
            self.CosUploadBackupFileSet = []
            for item in params.get("CosUploadBackupFileSet"):
                obj = CosUploadBackupFile()
                obj._deserialize(item)
                self.CosUploadBackupFileSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间(yyyy-MM-dd HH:mm:ss)\n        :type StartTime: str\n        :param EndTime: 结束时间(yyyy-MM-dd HH:mm:ss)\n        :type EndTime: str\n        :param InstanceId: 实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20\n        :type Limit: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        :param BackupName: 按照备份名称筛选，不填则不筛选此项\n        :type BackupName: str\n        :param Strategy: 按照备份策略筛选，0-实例备份，1-多库备份，不填则不筛选此项\n        :type Strategy: int\n        :param BackupWay: 按照备份方式筛选，0-后台自动定时备份，1-用户手动临时备份，不填则不筛选此项\n        :type BackupWay: int\n        :param BackupId: 按照备份ID筛选，不填则不筛选此项\n        :type BackupId: int\n        :param DatabaseName: 按照备份的库名称筛选，不填则不筛选此项\n        :type DatabaseName: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BackupName = None
        self.Strategy = None
        self.BackupWay = None
        self.BackupId = None
        self.DatabaseName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BackupName = params.get("BackupName")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")
        self.BackupId = params.get("BackupId")
        self.DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 备份总数量\n        :type TotalCount: int\n        :param Backups: 备份列表详情\n        :type Backups: list of Backup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossRegionZoneResponse(AbstractModel):
    """DescribeCrossRegionZone返回参数结构体

    """

    def __init__(self):
        """
        :param Region: 备机所在地域的字符串ID，形如：ap-guangzhou\n        :type Region: str\n        :param Zone: 备机所在可用区的字符串ID，形如：ap-guangzhou-1\n        :type Zone: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Region = None
        self.Zone = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.RequestId = params.get("RequestId")


class DescribeDBCharsetsRequest(AbstractModel):
    """DescribeDBCharsets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCharsetsResponse(AbstractModel):
    """DescribeDBCharsets返回参数结构体

    """

    def __init__(self):
        """
        :param DatabaseCharsets: 数据库字符集列表\n        :type DatabaseCharsets: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DatabaseCharsets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DatabaseCharsets = params.get("DatabaseCharsets")
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param Status: 实例状态。取值范围：
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
<li>12：重启中</li>\n        :type Status: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100\n        :type Limit: int\n        :param InstanceIdSet: 一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl\n        :type InstanceIdSet: list of str\n        :param PayMode: 付费类型检索 1-包年包月，0-按量计费\n        :type PayMode: int\n        :param VpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，传空字符串(“”)则按照基础网络筛选。\n        :type VpcId: str\n        :param SubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，传空字符串(“”)则按照基础网络筛选。\n        :type SubnetId: str\n        :param VipSet: 实例内网地址列表，格式如：172.1.0.12\n        :type VipSet: list of str\n        :param InstanceNameSet: 实例名称列表，模糊查询\n        :type InstanceNameSet: list of str\n        :param VersionSet: 实例版本代号列表，格式如：2008R2，2012SP3等\n        :type VersionSet: list of str\n        :param Zone: 实例可用区，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param TagKeys: 实例标签列表\n        :type TagKeys: list of str\n        :param SearchKey: 模糊查询关键字，支持实例id、实例名、内网ip\n        :type SearchKey: str\n        """
        self.ProjectId = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.InstanceIdSet = None
        self.PayMode = None
        self.VpcId = None
        self.SubnetId = None
        self.VipSet = None
        self.InstanceNameSet = None
        self.VersionSet = None
        self.Zone = None
        self.TagKeys = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.PayMode = params.get("PayMode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.VipSet = params.get("VipSet")
        self.InstanceNameSet = params.get("InstanceNameSet")
        self.VersionSet = params.get("VersionSet")
        self.Zone = params.get("Zone")
        self.TagKeys = params.get("TagKeys")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例总数。分页返回的话，这个值指的是所有符合条件的实例的个数，而非当前根据Limit和Offset值返回的实例个数\n        :type TotalCount: int\n        :param DBInstances: 实例列表\n        :type DBInstances: list of DBInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，格式如：mssql-c1nl9rpv或者mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全组详情。\n        :type SecurityGroupSet: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDBsNormalRequest(AbstractModel):
    """DescribeDBsNormal请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-7vfv3rk3\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBsNormalResponse(AbstractModel):
    """DescribeDBsNormal返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表示当前实例下的数据库总个数\n        :type TotalCount: int\n        :param DBList: 返回数据库的详细配置信息，例如：数据库是否开启CDC、CT等\n        :type DBList: list of DbNormalDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DBList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBList") is not None:
            self.DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self.DBList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 实例ID\n        :type InstanceIdSet: list of str\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20\n        :type Limit: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        """
        self.InstanceIdSet = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 数据库数量\n        :type TotalCount: int\n        :param DBInstances: 实例数据库列表\n        :type DBInstances: list of InstanceDBDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FlowId: 流程ID\n        :type FlowId: int\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 流程状态，0：成功，1：失败，2：运行中\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeIncrementalMigrationRequest(AbstractModel):
    """DescribeIncrementalMigration请求参数结构体

    """

    def __init__(self):
        """
        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupFileName: 备份文件名称\n        :type BackupFileName: str\n        :param StatusSet: 导入任务状态集合\n        :type StatusSet: list of int\n        :param Limit: 分页，页大小，默认值：100\n        :type Limit: int\n        :param Offset: 分页，页数，默认值：0\n        :type Offset: int\n        :param OrderBy: 排序字段，name；createTime；startTime；endTime，默认按照createTime递增排序。\n        :type OrderBy: str\n        :param OrderByType: 排序方式，desc-递减排序，asc-递增排序。默认按照asc排序，且在OrderBy为有效值时，本参数有效\n        :type OrderByType: str\n        :param IncrementalMigrationId: 增量备份导入任务ID，由CreateIncrementalMigration接口返回\n        :type IncrementalMigrationId: str\n        """
        self.BackupMigrationId = None
        self.InstanceId = None
        self.BackupFileName = None
        self.StatusSet = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.InstanceId = params.get("InstanceId")
        self.BackupFileName = params.get("BackupFileName")
        self.StatusSet = params.get("StatusSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementalMigrationResponse(AbstractModel):
    """DescribeIncrementalMigration返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 增量导入任务总数\n        :type TotalCount: int\n        :param IncrementalMigrationSet: 增量导入任务集合\n        :type IncrementalMigrationSet: list of Migration\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.IncrementalMigrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IncrementalMigrationSet") is not None:
            self.IncrementalMigrationSet = []
            for item in params.get("IncrementalMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self.IncrementalMigrationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，格式如：mssql-dj5i29c5n，与云数据库控制台页面中显示的实例 ID 相同，可使用 DescribeDBInstances 接口获取，其值为输出参数中字段 InstanceId 的值。\n        :type InstanceId: str\n        :param Offset: 分页，页数，默认0\n        :type Offset: int\n        :param Limit: 分页，页大小，默认20，最大不超过100\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录数\n        :type TotalCount: int\n        :param Items: 参数修改记录\n        :type Items: list of ParamRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，格式如：mssql-dj5i29c5n，与云数据库控制台页面中显示的实例 ID 相同，可使用 DescribeDBInstances 接口获取，其值为输出参数中字段 InstanceId 的值。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例的参数总数\n        :type TotalCount: int\n        :param Items: 参数详情\n        :type Items: list of ParameterDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintenanceSpanRequest(AbstractModel):
    """DescribeMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-k8voqdlz\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintenanceSpanResponse(AbstractModel):
    """DescribeMaintenanceSpan返回参数结构体

    """

    def __init__(self):
        """
        :param Weekly: 以周为单位，表示周几允许维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日。\n        :type Weekly: list of int\n        :param StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始。\n        :type StartTime: str\n        :param Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时。\n        :type Span: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 迁移源实例的ID，格式如：mssql-si2823jyl\n        :type InstanceId: str\n        :param UserName: 迁移源实例用户名\n        :type UserName: str\n        :param Password: 迁移源实例密码\n        :type Password: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDatabasesResponse(AbstractModel):
    """DescribeMigrationDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param Amount: 数据库数量\n        :type Amount: int\n        :param MigrateDBSet: 数据库名称数组\n        :type MigrateDBSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        :param MigrateName: 迁移任务名称\n        :type MigrateName: str\n        :param AppId: 迁移任务所属的用户ID\n        :type AppId: int\n        :param Region: 迁移任务所属的地域\n        :type Region: str\n        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）\n        :type SourceType: int\n        :param CreateTime: 迁移任务的创建时间\n        :type CreateTime: str\n        :param StartTime: 迁移任务的开始时间\n        :type StartTime: str\n        :param EndTime: 迁移任务的结束时间\n        :type EndTime: str\n        :param Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功）\n        :type Status: int\n        :param Progress: 迁移任务当前进度\n        :type Progress: int\n        :param MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）\n        :type MigrateType: int\n        :param Source: 迁移源\n        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`\n        :param Target: 迁移目标\n        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`\n        :param MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用。\n        :type MigrateDBSet: list of MigrateDB\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param StatusSet: 状态集合。只要符合集合中某一状态的迁移任务，就会查出来\n        :type StatusSet: list of int\n        :param MigrateName: 迁移任务的名称，模糊匹配\n        :type MigrateName: str\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100\n        :type Limit: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        :param OrderBy: 查询结果按照关键字排序，可选值为name、createTime、startTime，endTime，status\n        :type OrderBy: str\n        :param OrderByType: 排序方式，可选值为desc、asc\n        :type OrderByType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询结果的总数\n        :type TotalCount: int\n        :param MigrateTaskSet: 查询结果的列表\n        :type MigrateTaskSet: list of MigrateTask\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DealNames: 订单数组。发货时会返回订单名字，利用该订单名字调用DescribeOrders接口查询发货情况\n        :type DealNames: list of str\n        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        """
        :param Deals: 订单信息数组\n        :type Deals: list of DealInfo\n        :param TotalCount: 返回多少个订单的信息\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Zone: 可用区英文ID，形如ap-guangzhou-1\n        :type Zone: str\n        :param InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-基础版本型\n        :type InstanceType: str\n        """
        self.Zone = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        """
        :param SpecInfoList: 规格信息数组\n        :type SpecInfoList: list of SpecInfo\n        :param TotalCount: 返回总共多少条数据\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProjectId: 项目ID，可通过控制台项目管理中查看\n        :type ProjectId: int\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全组详情。\n        :type SecurityGroupSet: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param PubOrSubInstanceId: 订阅/发布实例ID，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例ID做筛选；当InstanceId为订阅实例时，本字段按照发布实例ID做筛选；\n        :type PubOrSubInstanceId: str\n        :param PubOrSubInstanceIp: 订阅/发布实例内网IP，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例内网IP做筛选；当InstanceId为订阅实例时，本字段按照发布实例内网IP做筛选；\n        :type PubOrSubInstanceIp: str\n        :param PublishSubscribeId: 订阅发布ID，用于筛选\n        :type PublishSubscribeId: int\n        :param PublishSubscribeName: 订阅发布名字，用于筛选\n        :type PublishSubscribeName: str\n        :param PublishDBName: 发布库名字，用于筛选\n        :type PublishDBName: str\n        :param SubscribeDBName: 订阅库名字，用于筛选\n        :type SubscribeDBName: str\n        :param Offset: 分页，页数\n        :type Offset: int\n        :param Limit: 分页，页大小\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishSubscribeResponse(AbstractModel):
    """DescribePublishSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param PublishSubscribeSet: 发布订阅列表\n        :type PublishSubscribeSet: list of PublishSubscribe\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，格式如：mssqlro-3l3fgqn7\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupByReadOnlyInstanceResponse(AbstractModel):
    """DescribeReadOnlyGroupByReadOnlyInstance返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID\n        :type ReadOnlyGroupId: str\n        :param ReadOnlyGroupName: 只读组名称\n        :type ReadOnlyGroupName: str\n        :param RegionId: 只读组的地域ID\n        :type RegionId: str\n        :param ZoneId: 只读组的可用区ID\n        :type ZoneId: str\n        :param IsOfflineDelay: 是否启动超时剔除功能 ,0-不开启剔除功能，1-开启剔除功能\n        :type IsOfflineDelay: int\n        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，单位是秒\n        :type ReadOnlyMaxDelayTime: int\n        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数\n        :type MinReadOnlyInGroup: int\n        :param Vip: 只读组vip\n        :type Vip: str\n        :param Vport: 只读组vport\n        :type Vport: int\n        :param VpcId: 只读组在私有网络ID\n        :type VpcId: str\n        :param SubnetId: 只读组在私有网络子网ID\n        :type SubnetId: str\n        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th\n        :type MasterInstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        :param ReadOnlyGroupId: 只读组ID，格式如：mssqlrg-3l3fgqn7\n        :type ReadOnlyGroupId: str\n        """
        self.InstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupDetailsResponse(AbstractModel):
    """DescribeReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID\n        :type ReadOnlyGroupId: str\n        :param ReadOnlyGroupName: 只读组名称\n        :type ReadOnlyGroupName: str\n        :param RegionId: 只读组的地域ID，与主实例相同\n        :type RegionId: str\n        :param ZoneId: 只读组的可用区ID，与主实例相同\n        :type ZoneId: str\n        :param IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能\n        :type IsOfflineDelay: int\n        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值\n        :type ReadOnlyMaxDelayTime: int\n        :param MinReadOnlyInGroup: 启动超时剔除功能后，至少只读组保留的只读副本数\n        :type MinReadOnlyInGroup: int\n        :param Vip: 只读组vip\n        :type Vip: str\n        :param Vport: 只读组vport\n        :type Vport: int\n        :param VpcId: 只读组私有网络ID\n        :type VpcId: str\n        :param SubnetId: 只读组私有网络子网ID\n        :type SubnetId: str\n        :param ReadOnlyInstanceSet: 只读实例副本集合\n        :type ReadOnlyInstanceSet: list of ReadOnlyInstance\n        :param Status: 只读组状态: 1-申请成功运行中，5-申请中\n        :type Status: int\n        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th\n        :type MasterInstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupListResponse(AbstractModel):
    """DescribeReadOnlyGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupSet: 只读组列表\n        :type ReadOnlyGroupSet: list of ReadOnlyGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TotalCount: 返回地域信息总的条目\n        :type TotalCount: int\n        :param RegionSet: 地域信息数组\n        :type RegionSet: list of RegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param DBs: 需要查询的数据库列表\n        :type DBs: list of str\n        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DBs = params.get("DBs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime返回参数结构体

    """

    def __init__(self):
        """
        :param Details: 数据库可回档实例信息\n        :type Details: list of DbRollbackTimeInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-k8voqdlz\n        :type InstanceId: str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        :param Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20\n        :type Limit: int\n        :param Offset: 分页返回，页编号，默认值为第0页\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询总数\n        :type TotalCount: int\n        :param Slowlogs: 慢查询日志信息列表\n        :type Slowlogs: list of SlowlogInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeUploadBackupInfoRequest(AbstractModel):
    """DescribeUploadBackupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadBackupInfoResponse(AbstractModel):
    """DescribeUploadBackupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param BucketName: 存储桶名称\n        :type BucketName: str\n        :param Region: 存储桶地域信息\n        :type Region: str\n        :param Path: 存储路径\n        :type Path: str\n        :param TmpSecretId: 临时密钥ID\n        :type TmpSecretId: str\n        :param TmpSecretKey: 临时密钥Key\n        :type TmpSecretKey: str\n        :param XCosSecurityToken: 临时密钥Token\n        :type XCosSecurityToken: str\n        :param StartTime: 临时密钥开始时间\n        :type StartTime: str\n        :param ExpiredTime: 临时密钥到期时间\n        :type ExpiredTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BucketName = None
        self.Region = None
        self.Path = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.XCosSecurityToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.XCosSecurityToken = params.get("XCosSecurityToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DescribeUploadIncrementalInfoRequest(AbstractModel):
    """DescribeUploadIncrementalInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param IncrementalMigrationId: 增量导入任务ID\n        :type IncrementalMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadIncrementalInfoResponse(AbstractModel):
    """DescribeUploadIncrementalInfo返回参数结构体

    """

    def __init__(self):
        """
        :param BucketName: 存储桶名称\n        :type BucketName: str\n        :param Region: 存储桶地域信息\n        :type Region: str\n        :param Path: 存储路径\n        :type Path: str\n        :param TmpSecretId: 临时密钥ID\n        :type TmpSecretId: str\n        :param TmpSecretKey: 临时密钥Key\n        :type TmpSecretKey: str\n        :param XCosSecurityToken: 临时密钥Token\n        :type XCosSecurityToken: str\n        :param StartTime: 临时密钥开始时间\n        :type StartTime: str\n        :param ExpiredTime: 临时密钥到期时间\n        :type ExpiredTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BucketName = None
        self.Region = None
        self.Path = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.XCosSecurityToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.XCosSecurityToken = params.get("XCosSecurityToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回多少个可用区信息\n        :type TotalCount: int\n        :param ZoneSet: 可用区数组\n        :type ZoneSet: list of ZoneInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SecurityGroupId: 安全组ID。\n        :type SecurityGroupId: str\n        :param InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。\n        :type InstanceIdSet: list of str\n        """
        self.SecurityGroupId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。\n        :type Zone: str\n        :param Memory: 内存大小，单位：GB\n        :type Memory: int\n        :param Storage: 实例容量大小，单位：GB。\n        :type Storage: int\n        :param InstanceChargeType: 计费类型，取值支持 PREPAID，POSTPAID。\n        :type InstanceChargeType: str\n        :param Period: 购买时长，单位：月。取值为1到48，默认为1\n        :type Period: int\n        :param GoodsNum: 一次性购买的实例数量。取值1-100，默认取值为1\n        :type GoodsNum: int\n        :param DBVersion: sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。默认为2008R2版本\n        :type DBVersion: str\n        :param Cpu: 预购买实例的CPU核心数\n        :type Cpu: int\n        :param InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本，SI-基础版，默认取值HA\n        :type InstanceType: str\n        :param MachineType: 购买实例的宿主机类型，PM-物理机, CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘，默认取值PM\n        :type MachineType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折前价格，其值除以100表示多少钱。例如10010表示100.10元\n        :type OriginalPrice: int\n        :param Price: 实际需要支付的价格，其值除以100表示多少钱。例如10010表示100.10元\n        :type Price: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Period: 续费周期。按月续费最多48个月。默认查询续费一个月的价格\n        :type Period: int\n        :param TimeUnit: 续费周期单位。month表示按月续费，当前只支持按月付费查询价格\n        :type TimeUnit: str\n        """
        self.InstanceId = None
        self.Period = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元\n        :type OriginalPrice: int\n        :param Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元\n        :type Price: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param Memory: 实例升级后的内存大小，单位GB，其值不能比当前实例内存小\n        :type Memory: int\n        :param Storage: 实例升级后的磁盘大小，单位GB，其值不能比当前实例磁盘小\n        :type Storage: int\n        :param Cpu: 实例升级后的CPU核心数，其值不能比当前实例CPU小\n        :type Cpu: int\n        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元\n        :type OriginalPrice: int\n        :param Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元\n        :type Price: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param DBDetails: 数据库信息列表\n        :type DBDetails: list of DBDetail\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRenewInfo(AbstractModel):
    """实例续费状态信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param RenewFlag: 实例续费标记。0：正常续费，1：自动续费，2：到期不续\n        :type RenewFlag: int\n        """
        self.InstanceId = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDB(AbstractModel):
    """需要迁移的DB列表

    """

    def __init__(self):
        """
        :param DBName: 迁移数据库的名称\n        :type DBName: str\n        """
        self.DBName = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetail(AbstractModel):
    """迁移的进度详情类型

    """

    def __init__(self):
        """
        :param StepName: 当前环节的名称\n        :type StepName: str\n        :param Progress: 当前环节的进度（单位是%）\n        :type Progress: int\n        """
        self.StepName = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateSource(AbstractModel):
    """迁移任务的源类型

    """

    def __init__(self):
        """
        :param InstanceId: 迁移源实例的ID，MigrateType=1(TencentDB for SQLServers)时使用，格式如：mssql-si2823jyl\n        :type InstanceId: str\n        :param CvmId: 迁移源Cvm的ID，MigrateType=2(云服务器自建SQLServer数据库)时使用\n        :type CvmId: str\n        :param VpcId: 迁移源Cvm的Vpc网络标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：vpc-6ys9ont9\n        :type VpcId: str\n        :param SubnetId: 迁移源Cvm的Vpc下的子网标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：subnet-h9extioi\n        :type SubnetId: str\n        :param UserName: 用户名，MigrateType=1或MigrateType=2使用\n        :type UserName: str\n        :param Password: 密码，MigrateType=1或MigrateType=2使用\n        :type Password: str\n        :param Ip: 迁移源Cvm自建库的内网IP，MigrateType=2(云服务器自建SQLServer数据库)时使用\n        :type Ip: str\n        :param Port: 迁移源Cvm自建库的端口号，MigrateType=2(云服务器自建SQLServer数据库)时使用\n        :type Port: int\n        :param Url: 离线迁移的源备份地址，MigrateType=4或MigrateType=5使用\n        :type Url: list of str\n        :param UrlPassword: 离线迁移的源备份密码，MigrateType=4或MigrateType=5使用\n        :type UrlPassword: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTarget(AbstractModel):
    """迁移任务的目标类型

    """

    def __init__(self):
        """
        :param InstanceId: 迁移目标实例的ID，格式如：mssql-si2823jyl\n        :type InstanceId: str\n        :param UserName: 迁移目标实例的用户名\n        :type UserName: str\n        :param Password: 迁移目标实例的密码\n        :type Password: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTask(AbstractModel):
    """查询迁移任务列表类型

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        :param MigrateName: 迁移任务名称\n        :type MigrateName: str\n        :param AppId: 迁移任务所属的用户ID\n        :type AppId: int\n        :param Region: 迁移任务所属的地域\n        :type Region: str\n        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）\n        :type SourceType: int\n        :param CreateTime: 迁移任务的创建时间\n        :type CreateTime: str\n        :param StartTime: 迁移任务的开始时间\n        :type StartTime: str\n        :param EndTime: 迁移任务的结束时间\n        :type EndTime: str\n        :param Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功,7已中止,8已删除,9中止中,10完成中,11中止失败,12完成失败）\n        :type Status: int\n        :param Message: 信息\n        :type Message: str\n        :param CheckFlag: 是否迁移任务经过检查（0:未校验,1:校验成功,2:校验失败,3:校验中）\n        :type CheckFlag: int\n        :param Progress: 迁移任务当前进度（单位%）\n        :type Progress: int\n        :param MigrateDetail: 迁移任务进度细节\n        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Migration(AbstractModel):
    """冷备迁移导入

    """

    def __init__(self):
        """
        :param MigrationId: 备份导入任务ID 或 增量导入任务ID\n        :type MigrationId: str\n        :param MigrationName: 备份导入名称，增量导入任务该字段为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type MigrationName: str\n        :param AppId: 应用ID\n        :type AppId: int\n        :param Region: 地域\n        :type Region: str\n        :param InstanceId: 迁移目标实例ID\n        :type InstanceId: str\n        :param RecoveryType: 迁移任务恢复类型\n        :type RecoveryType: str\n        :param UploadType: 备份用户上传类型，COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传\n        :type UploadType: str\n        :param BackupFiles: 备份文件列表，UploadType确定，COS_URL则保存URL，COS_UPLOAD则保存备份名称\n        :type BackupFiles: list of str\n        :param Status: 迁移任务状态，2-创建完成，7-全量导入中，8-等待增量，9-导入成功，10-导入失败，12-增量导入中\n        :type Status: int\n        :param CreateTime: 迁移任务创建时间\n        :type CreateTime: str\n        :param StartTime: 迁移任务开始时间\n        :type StartTime: str\n        :param EndTime: 迁移任务结束时间\n        :type EndTime: str\n        :param Message: 说明信息\n        :type Message: str\n        :param Detail: 迁移细节\n        :type Detail: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`\n        :param Action: 当前状态允许的操作\n        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`\n        :param IsRecovery: 是否是最终恢复，全量导入任务该字段为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsRecovery: str\n        """
        self.MigrationId = None
        self.MigrationName = None
        self.AppId = None
        self.Region = None
        self.InstanceId = None
        self.RecoveryType = None
        self.UploadType = None
        self.BackupFiles = None
        self.Status = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Message = None
        self.Detail = None
        self.Action = None
        self.IsRecovery = None


    def _deserialize(self, params):
        self.MigrationId = params.get("MigrationId")
        self.MigrationName = params.get("MigrationName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.BackupFiles = params.get("BackupFiles")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Message = params.get("Message")
        if params.get("Detail") is not None:
            self.Detail = MigrationDetail()
            self.Detail._deserialize(params.get("Detail"))
        if params.get("Action") is not None:
            self.Action = MigrationAction()
            self.Action._deserialize(params.get("Action"))
        self.IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationAction(AbstractModel):
    """冷备导入任务允许的操作

    """

    def __init__(self):
        """
        :param AllAction: 支持的所有操作，值包括：view(查看任务) ，modify(修改任务)， start(启动任务)，incremental(创建增量任务)，delete(删除任务)，upload(获取上传权限)。\n        :type AllAction: list of str\n        :param AllowedAction: 当前状态允许的操作，AllAction的子集,为空表示禁止所有操作\n        :type AllowedAction: list of str\n        """
        self.AllAction = None
        self.AllowedAction = None


    def _deserialize(self, params):
        self.AllAction = params.get("AllAction")
        self.AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationDetail(AbstractModel):
    """冷备导入任务迁移细节

    """

    def __init__(self):
        """
        :param StepAll: 总步骤数\n        :type StepAll: int\n        :param StepNow: 当前步骤\n        :type StepNow: int\n        :param Progress: 总进度,如："30"表示30%\n        :type Progress: int\n        :param StepInfo: 步骤信息，null表示还未开始迁移
注意：此字段可能返回 null，表示取不到有效值。\n        :type StepInfo: list of MigrationStep\n        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrationStep()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationStep(AbstractModel):
    """冷备导入任务迁移步骤细节

    """

    def __init__(self):
        """
        :param StepNo: 步骤序列\n        :type StepNo: int\n        :param StepName: 步骤展现名称\n        :type StepName: str\n        :param StepId: 英文ID标识\n        :type StepId: str\n        :param Status: 步骤状态:0-默认值,1-成功,2-失败,3-执行中,4-未执行\n        :type Status: int\n        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param Accounts: 账号权限变更信息\n        :type Accounts: list of AccountPrivilegeModifyInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param Accounts: 修改备注的账户信息\n        :type Accounts: list of AccountRemark\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupMigrationRequest(AbstractModel):
    """ModifyBackupMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param MigrationName: 任务名称\n        :type MigrationName: str\n        :param RecoveryType: 迁移任务恢复类型，FULL,FULL_LOG,FULL_DIFF\n        :type RecoveryType: str\n        :param UploadType: COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传\n        :type UploadType: str\n        :param BackupFiles: UploadType是COS_URL时这里时URL，COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库\n        :type BackupFiles: list of str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.MigrationName = None
        self.RecoveryType = None
        self.UploadType = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.MigrationName = params.get("MigrationName")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupMigrationResponse(AbstractModel):
    """ModifyBackupMigration返回参数结构体

    """

    def __init__(self):
        """
        :param BackupMigrationId: 备份导入任务ID\n        :type BackupMigrationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BackupMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.RequestId = params.get("RequestId")


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        :param BackupId: 要修改名称的备份ID，可通过 [DescribeBackups](https://cloud.tencent.com/document/product/238/19943)  接口获取。\n        :type BackupId: int\n        :param BackupName: 修改的备份名称\n        :type BackupName: str\n        """
        self.InstanceId = None
        self.BackupId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupStrategyRequest(AbstractModel):
    """ModifyBackupStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param BackupType: 备份类型，当前只支持按天备份，取值为daily\n        :type BackupType: str\n        :param BackupTime: 备份时间点，取值为0-23的整数\n        :type BackupTime: int\n        :param BackupDay: BackupType取值为daily时，表示备份间隔天数。当前取值只能为1\n        :type BackupDay: int\n        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupTime = None
        self.BackupDay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupTime = params.get("BackupTime")
        self.BackupDay = params.get("BackupDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupStrategyResponse(AbstractModel):
    """ModifyBackupStrategy返回参数结构体

    """

    def __init__(self):
        """
        :param Errno: 返回错误码\n        :type Errno: int\n        :param Msg: 返回错误信息\n        :type Msg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param InstanceName: 新的数据库实例名字\n        :type InstanceName: str\n        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNetworkRequest(AbstractModel):
    """ModifyDBInstanceNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param NewVpcId: 新VPC网络Id\n        :type NewVpcId: str\n        :param NewSubnetId: 新子网Id\n        :type NewSubnetId: str\n        :param OldIpRetainTime: 原vip保留时长，单位小时，默认为0，代表立即回收，最大为168小时\n        :type OldIpRetainTime: int\n        """
        self.InstanceId = None
        self.NewVpcId = None
        self.NewSubnetId = None
        self.OldIpRetainTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewVpcId = params.get("NewVpcId")
        self.NewSubnetId = params.get("NewSubnetId")
        self.OldIpRetainTime = params.get("OldIpRetainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkResponse(AbstractModel):
    """ModifyDBInstanceNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 实例转网流程id，可通过[DescribeFlowStatus](https://cloud.tencent.com/document/product/238/19967)接口查询流程状态\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 实例ID数组，形如mssql-j8kv137v\n        :type InstanceIdSet: list of str\n        :param ProjectId: 项目ID，为0的话表示默认项目\n        :type ProjectId: int\n        """
        self.InstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 修改成功的实例个数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RenewFlags: 实例续费状态标记信息\n        :type RenewFlags: list of InstanceRenewInfo\n        """
        self.RenewFlags = None


    def _deserialize(self, params):
        if params.get("RenewFlags") is not None:
            self.RenewFlags = []
            for item in params.get("RenewFlags"):
                obj = InstanceRenewInfo()
                obj._deserialize(item)
                self.RenewFlags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceRenewFlagResponse(AbstractModel):
    """ModifyDBInstanceRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 修改成功的个数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例 ID，格式如：mssql-c1nl9rpv 或者 mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。\n        :type InstanceId: str\n        :param SecurityGroupIdSet: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。\n        :type SecurityGroupIdSet: list of str\n        """
        self.InstanceId = None
        self.SecurityGroupIdSet = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param OldDBName: 旧数据库名\n        :type OldDBName: str\n        :param NewDBName: 新数据库名\n        :type NewDBName: str\n        """
        self.InstanceId = None
        self.OldDBName = None
        self.NewDBName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldDBName = params.get("OldDBName")
        self.NewDBName = params.get("NewDBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-rljoi3bf\n        :type InstanceId: str\n        :param DBRemarks: 数据库名称及备注数组，每个元素包含数据库名和对应的备注\n        :type DBRemarks: list of DBRemark\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDatabaseCDCRequest(AbstractModel):
    """ModifyDatabaseCDC请求参数结构体

    """

    def __init__(self):
        """
        :param DBNames: 数据库名数组\n        :type DBNames: list of str\n        :param ModifyType: 开启、关闭数据库CDC功能 enable；开启，disable：关闭\n        :type ModifyType: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.DBNames = None
        self.ModifyType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.DBNames = params.get("DBNames")
        self.ModifyType = params.get("ModifyType")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCDCResponse(AbstractModel):
    """ModifyDatabaseCDC返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDatabaseCTRequest(AbstractModel):
    """ModifyDatabaseCT请求参数结构体

    """

    def __init__(self):
        """
        :param DBNames: 数据库名数组\n        :type DBNames: list of str\n        :param ModifyType: 启用、禁用数据库CT功能 enable；启用，disable：禁用\n        :type ModifyType: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ChangeRetentionDay: 启用CT时额外保留天数，默认保留3天，最小3天，最大30天\n        :type ChangeRetentionDay: int\n        """
        self.DBNames = None
        self.ModifyType = None
        self.InstanceId = None
        self.ChangeRetentionDay = None


    def _deserialize(self, params):
        self.DBNames = params.get("DBNames")
        self.ModifyType = params.get("ModifyType")
        self.InstanceId = params.get("InstanceId")
        self.ChangeRetentionDay = params.get("ChangeRetentionDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCTResponse(AbstractModel):
    """ModifyDatabaseCT返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDatabaseMdfRequest(AbstractModel):
    """ModifyDatabaseMdf请求参数结构体

    """

    def __init__(self):
        """
        :param DBNames: 数据库名数组\n        :type DBNames: list of str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.DBNames = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseMdfResponse(AbstractModel):
    """ModifyDatabaseMdf返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyIncrementalMigrationRequest(AbstractModel):
    """ModifyIncrementalMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param IncrementalMigrationId: 增量导入任务ID，由CreateIncrementalMigration接口返回\n        :type IncrementalMigrationId: str\n        :param IsRecovery: 是否需要恢复，NO-不需要，YES-需要，默认不修改增量备份导入任务是否需要恢复的属性。\n        :type IsRecovery: str\n        :param BackupFiles: UploadType是COS_URL时这里时URL，COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库\n        :type BackupFiles: list of str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None
        self.IsRecovery = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.IsRecovery = params.get("IsRecovery")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIncrementalMigrationResponse(AbstractModel):
    """ModifyIncrementalMigration返回参数结构体

    """

    def __init__(self):
        """
        :param IncrementalMigrationId: 增量备份导入任务ID\n        :type IncrementalMigrationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IncrementalMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例短 ID 列表\n        :type InstanceIds: list of str\n        :param ParamList: 要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改的值。<b>注意</b>：如果修改的参数需要<b>重启</b>实例，那么您的实例将会在执行修改时<b>重启</b>。您可以通过DescribeInstanceParams接口查询修改参数时是否会重启实例，以免导致您的实例不符合预期重启。\n        :type ParamList: list of Parameter\n        :param WaitSwitch: 执行参数调整任务的方式，默认为 0。支持值包括：0 - 立刻执行，1 - 时间窗执行。\n        :type WaitSwitch: int\n        """
        self.InstanceIds = None
        self.ParamList = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintenanceSpanRequest(AbstractModel):
    """ModifyMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-k8voqdlz\n        :type InstanceId: str\n        :param Weekly: 以周为单位，表示允许周几维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日，本参数不填，则不修改此值。\n        :type Weekly: list of int\n        :param StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始，本参数不填，则不修改此值。\n        :type StartTime: str\n        :param Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时，本参数不填，则不修改此值。\n        :type Span: int\n        """
        self.InstanceId = None
        self.Weekly = None
        self.StartTime = None
        self.Span = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceSpanResponse(AbstractModel):
    """ModifyMaintenanceSpan返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        :param MigrateName: 新的迁移任务的名称，若不填则不修改\n        :type MigrateName: str\n        :param MigrateType: 新的迁移类型（1:结构迁移 2:数据迁移 3:增量同步），若不填则不修改\n        :type MigrateType: int\n        :param SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式），若不填则不修改\n        :type SourceType: int\n        :param Source: 迁移源，若不填则不修改\n        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`\n        :param Target: 迁移目标，若不填则不修改\n        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`\n        :param MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用，若不填则不修改\n        :type MigrateDBSet: list of MigrateDB\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration返回参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PublishSubscribeId: 发布订阅ID\n        :type PublishSubscribeId: int\n        :param PublishSubscribeName: 待修改的发布订阅名称\n        :type PublishSubscribeName: str\n        """
        self.PublishSubscribeId = None
        self.PublishSubscribeName = None


    def _deserialize(self, params):
        self.PublishSubscribeId = params.get("PublishSubscribeId")
        self.PublishSubscribeName = params.get("PublishSubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublishSubscribeNameResponse(AbstractModel):
    """ModifyPublishSubscribeName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyReadOnlyGroupDetailsRequest(AbstractModel):
    """ModifyReadOnlyGroupDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例ID，格式如：mssql-3l3fgqn7\n        :type InstanceId: str\n        :param ReadOnlyGroupId: 只读组ID\n        :type ReadOnlyGroupId: str\n        :param ReadOnlyGroupName: 只读组名称，不填此参数，则不修改\n        :type ReadOnlyGroupName: str\n        :param IsOfflineDelay: 是否启动超时剔除功能,0-不开启剔除功能，1-开启剔除功能，不填此参数，则不修改\n        :type IsOfflineDelay: int\n        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，不填此参数，则不修改\n        :type ReadOnlyMaxDelayTime: int\n        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数，不填此参数，则不修改\n        :type MinReadOnlyInGroup: int\n        :param WeightPairs: 只读组实例权重修改集合，不填此参数，则不修改\n        :type WeightPairs: list of ReadOnlyInstanceWeightPair\n        :param AutoWeight: 0-用户自定义权重（根据WeightPairs调整）,1-系统自动分配权重(WeightPairs无效)， 默认为0\n        :type AutoWeight: int\n        :param BalanceWeight: 0-不重新均衡负载，1-重新均衡负载，默认为0\n        :type BalanceWeight: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupDetailsResponse(AbstractModel):
    """ModifyReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ParamRecord(AbstractModel):
    """实例参数修改记录

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ParamName: 参数名称\n        :type ParamName: str\n        :param OldValue: 参数修改前的值\n        :type OldValue: str\n        :param NewValue: 参数修改后的值\n        :type NewValue: str\n        :param Status: 参数修改状态，1-初始化等待被执行，2-执行成功，3-执行失败，4-参数修改中\n        :type Status: int\n        :param ModifyTime: 修改时间\n        :type ModifyTime: str\n        """
        self.InstanceId = None
        self.ParamName = None
        self.OldValue = None
        self.NewValue = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ParamName = params.get("ParamName")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """数据库实例参数

    """

    def __init__(self):
        """
        :param Name: 参数名称\n        :type Name: str\n        :param CurrentValue: 参数值\n        :type CurrentValue: str\n        """
        self.Name = None
        self.CurrentValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """实例参数的详细描述

    """

    def __init__(self):
        """
        :param Name: 参数名称\n        :type Name: str\n        :param ParamType: 参数类型，integer-整型，enum-枚举型\n        :type ParamType: str\n        :param Default: 参数默认值\n        :type Default: str\n        :param Description: 参数描述\n        :type Description: str\n        :param CurrentValue: 参数当前值\n        :type CurrentValue: str\n        :param NeedReboot: 修改参数后，是否需要重启数据库以使参数生效，0-不需要重启，1-需要重启\n        :type NeedReboot: int\n        :param Max: 参数允许的最大值\n        :type Max: int\n        :param Min: 参数允许的最小值\n        :type Min: int\n        :param EnumValue: 参数允许的枚举类型\n        :type EnumValue: list of str\n        :param Status: 参数状态 0-状态正常 1-在修改中\n        :type Status: int\n        """
        self.Name = None
        self.ParamType = None
        self.Default = None
        self.Description = None
        self.CurrentValue = None
        self.NeedReboot = None
        self.Max = None
        self.Min = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ParamType = params.get("ParamType")
        self.Default = params.get("Default")
        self.Description = params.get("Description")
        self.CurrentValue = params.get("CurrentValue")
        self.NeedReboot = params.get("NeedReboot")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishSubscribe(AbstractModel):
    """发布订阅对象

    """

    def __init__(self):
        """
        :param Id: 发布订阅ID\n        :type Id: int\n        :param Name: 发布订阅名称\n        :type Name: str\n        :param PublishInstanceId: 发布实例ID\n        :type PublishInstanceId: str\n        :param PublishInstanceName: 发布实例名称\n        :type PublishInstanceName: str\n        :param PublishInstanceIp: 发布实例IP\n        :type PublishInstanceIp: str\n        :param SubscribeInstanceId: 订阅实例ID\n        :type SubscribeInstanceId: str\n        :param SubscribeInstanceName: 订阅实例名称\n        :type SubscribeInstanceName: str\n        :param SubscribeInstanceIp: 订阅实例IP\n        :type SubscribeInstanceIp: str\n        :param DatabaseTupleSet: 数据库的订阅发布关系集合\n        :type DatabaseTupleSet: list of DatabaseTupleStatus\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMigrationCheckProcessRequest(AbstractModel):
    """QueryMigrationCheckProcess请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMigrationCheckProcessResponse(AbstractModel):
    """QueryMigrationCheckProcess返回参数结构体

    """

    def __init__(self):
        """
        :param TotalStep: 总步骤数量\n        :type TotalStep: int\n        :param CurrentStep: 当前步骤编号，从1开始\n        :type CurrentStep: int\n        :param StepDetails: 所有步骤详情\n        :type StepDetails: list of StepDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ReadOnlyGroupId: 只读组ID\n        :type ReadOnlyGroupId: str\n        :param ReadOnlyGroupName: 只读组名称\n        :type ReadOnlyGroupName: str\n        :param RegionId: 只读组的地域ID，与主实例相同\n        :type RegionId: str\n        :param ZoneId: 只读组的可用区ID，与主实例相同\n        :type ZoneId: str\n        :param IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能\n        :type IsOfflineDelay: int\n        :param ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值\n        :type ReadOnlyMaxDelayTime: int\n        :param MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数\n        :type MinReadOnlyInGroup: int\n        :param Vip: 只读组vip\n        :type Vip: str\n        :param Vport: 只读组vport\n        :type Vport: int\n        :param VpcId: 只读组私有网络ID\n        :type VpcId: str\n        :param SubnetId: 只读组私有网络子网ID\n        :type SubnetId: str\n        :param Status: 只读组状态: 1-申请成功运行中，5-申请中\n        :type Status: int\n        :param MasterInstanceId: 主实例ID，形如mssql-sgeshe3th\n        :type MasterInstanceId: str\n        :param ReadOnlyInstanceSet: 只读实例副本集合\n        :type ReadOnlyInstanceSet: list of ReadOnlyInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstance(AbstractModel):
    """只读副本实例

    """

    def __init__(self):
        """
        :param InstanceId: 只读副本ID，格式如：mssqlro-3l3fgqn7\n        :type InstanceId: str\n        :param Name: 只读副本名称\n        :type Name: str\n        :param Uid: 只读副本唯一UID\n        :type Uid: str\n        :param ProjectId: 只读副本所在项目ID\n        :type ProjectId: int\n        :param Status: 只读副本状态。1：申请中 2：运行中 3：被延迟剔除 4：已隔离 5：回收中 6：已回收 7：任务执行中 8：已下线 9：实例扩容中 10：实例迁移中  12：重启中\n        :type Status: int\n        :param CreateTime: 只读副本创建时间\n        :type CreateTime: str\n        :param UpdateTime: 只读副本更新时间\n        :type UpdateTime: str\n        :param Memory: 只读副本内存大小，单位G\n        :type Memory: int\n        :param Storage: 只读副本存储空间大小，单位G\n        :type Storage: int\n        :param Cpu: 只读副本cpu核心数\n        :type Cpu: int\n        :param Version: 只读副本版本代号\n        :type Version: str\n        :param Type: 宿主机代号\n        :type Type: str\n        :param Model: 只读副本模式，2-单机\n        :type Model: int\n        :param PayMode: 只读副本计费模式，1-包年包月，0-按量计费\n        :type PayMode: int\n        :param Weight: 只读副本权重\n        :type Weight: int\n        :param DelayTime: 只读副本延迟时间，单位秒\n        :type DelayTime: str\n        :param SynStatus: 只读副本与主实例的同步状态。
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
SyncNormal:正常\n        :type SynStatus: str\n        :param DatabaseDifference: 只读副本与主实例没有同步的库\n        :type DatabaseDifference: str\n        :param AccountDifference: 只读副本与主实例没有同步的账户\n        :type AccountDifference: str\n        :param StartTime: 只读副本计费开始时间\n        :type StartTime: str\n        :param EndTime: 只读副本计费结束时间\n        :type EndTime: str\n        :param IsolateTime: 只读副本隔离时间\n        :type IsolateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstanceWeightPair(AbstractModel):
    """只读实例与权重对应关系

    """

    def __init__(self):
        """
        :param ReadOnlyInstanceId: 只读实例ID，格式如：mssqlro-3l3fgqn7\n        :type ReadOnlyInstanceId: str\n        :param ReadOnlyWeight: 只读实例权重 ，范围是0-100\n        :type ReadOnlyWeight: int\n        """
        self.ReadOnlyInstanceId = None
        self.ReadOnlyWeight = None


    def _deserialize(self, params):
        self.ReadOnlyInstanceId = params.get("ReadOnlyInstanceId")
        self.ReadOnlyWeight = params.get("ReadOnlyWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleDBInstanceRequest(AbstractModel):
    """RecycleDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleDBInstanceResponse(AbstractModel):
    """RecycleDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程id\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RecycleReadOnlyGroupRequest(AbstractModel):
    """RecycleReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 主实例的ID\n        :type InstanceId: str\n        :param ReadOnlyGroupId: 只读组的ID\n        :type ReadOnlyGroupId: str\n        """
        self.InstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleReadOnlyGroupResponse(AbstractModel):
    """RecycleReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID，类似ap-guanghou\n        :type Region: str\n        :param RegionName: 地域中文名称\n        :type RegionName: str\n        :param RegionId: 地域数字ID\n        :type RegionId: int\n        :param RegionState: 该地域目前是否可以售卖，UNAVAILABLE-不可售卖；AVAILABLE-可售卖\n        :type RegionState: str\n        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBackupsRequest(AbstractModel):
    """RemoveBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param BackupNames: 待删除的备份名称，备份名称可通过DescribeBackups接口的FileName字段获得。单次请求批量删除备份数不能超过10个。\n        :type BackupNames: list of str\n        """
        self.InstanceId = None
        self.BackupNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupNames = params.get("BackupNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBackupsResponse(AbstractModel):
    """RemoveBackups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenameRestoreDatabase(AbstractModel):
    """用于RestoreInstance，RollbackInstance，CreateMigration、CloneDB 等接口；对恢复的库进行重命名，且支持选择要恢复的库。

    """

    def __init__(self):
        """
        :param OldName: 库的名字，如果oldName不存在则返回失败。
在用于离线迁移任务时可不填。\n        :type OldName: str\n        :param NewName: 库的新名字，在用于离线迁移时，不填则按照OldName命名，OldName和NewName不能同时不填。在用于克隆数据库时，OldName和NewName都必须填写，且不能重复\n        :type NewName: str\n        """
        self.OldName = None
        self.NewName = None


    def _deserialize(self, params):
        self.OldName = params.get("OldName")
        self.NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param Period: 续费多少个月，取值范围为1-48，默认为1\n        :type Period: int\n        :param AutoVoucher: 是否自动使用代金券，0-不使用；1-使用；默认不实用\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID数组，目前只支持使用1张代金券\n        :type VoucherIds: list of str\n        """
        self.InstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称\n        :type DealName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewPostpaidDBInstanceResponse(AbstractModel):
    """RenewPostpaidDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        :param Accounts: 更新后的账户密码信息数组\n        :type Accounts: list of AccountPassword\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 修改帐号密码的异步任务流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """实例绑定的标签信息

    """

    def __init__(self):
        """
        :param TagKey: 标签key\n        :type TagKey: str\n        :param TagValue: 标签value\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 数据库实例ID，形如mssql-njj2mtpl\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param BackupId: 备份文件ID，该ID可以通过DescribeBackups接口返回数据中的Id字段获得\n        :type BackupId: int\n        :param TargetInstanceId: 备份恢复到的同一个APPID下的实例ID，不填则恢复到原实例ID\n        :type TargetInstanceId: str\n        :param RenameRestore: 按照ReNameRestoreDatabase中的库进行恢复，并重命名，不填则按照默认方式命名恢复的库，且恢复所有的库。\n        :type RenameRestore: list of RenameRestoreDatabase\n        """
        self.InstanceId = None
        self.BackupId = None
        self.TargetInstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步流程任务ID，使用FlowId调用DescribeFlowStatus接口获取任务执行状态\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Type: 回档类型，0-回档的数据库覆盖原库；1-回档的数据库以重命名的形式生成，不覆盖原库\n        :type Type: int\n        :param DBs: 需要回档的数据库\n        :type DBs: list of str\n        :param Time: 回档目标时间点\n        :type Time: str\n        :param TargetInstanceId: 备份恢复到的同一个APPID下的实例ID，不填则恢复到原实例ID\n        :type TargetInstanceId: str\n        :param RenameRestore: 按照ReNameRestoreDatabase中的库进行重命名，仅在Type = 1重命名回档方式有效；不填则按照默认方式命名库，DBs参数确定要恢复的库\n        :type RenameRestore: list of RenameRestoreDatabase\n        """
        self.InstanceId = None
        self.Type = None
        self.DBs = None
        self.Time = None
        self.TargetInstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.DBs = params.get("DBs")
        self.Time = params.get("Time")
        self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMigrationResponse(AbstractModel):
    """RunMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 迁移流程启动后，返回流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param InboundSet: 入站规则\n        :type InboundSet: list of SecurityGroupPolicy\n        :param OutboundSet: 出站规则\n        :type OutboundSet: list of SecurityGroupPolicy\n        :param SecurityGroupId: 安全组ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组备注\n        :type SecurityGroupRemark: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """安全组策略

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT 或者 DROP\n        :type Action: str\n        :param CidrIp: 目的 IP 或 IP 段，例如172.16.0.0/12\n        :type CidrIp: str\n        :param PortRange: 端口或者端口范围\n        :type PortRange: str\n        :param IpProtocol: 网络协议，支持 UDP、TCP等\n        :type IpProtocol: str\n        :param Dir: 规则限定的方向，OUTPUT-出战规则  INPUT-进站规则\n        :type Dir: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowlogInfo(AbstractModel):
    """慢查询日志文件信息

    """

    def __init__(self):
        """
        :param Id: 慢查询日志文件唯一标识\n        :type Id: int\n        :param StartTime: 文件生成的开始时间\n        :type StartTime: str\n        :param EndTime: 文件生成的结束时间\n        :type EndTime: str\n        :param Size: 文件大小（KB）\n        :type Size: int\n        :param Count: 文件中log条数\n        :type Count: int\n        :param InternalAddr: 内网下载地址\n        :type InternalAddr: str\n        :param ExternalAddr: 外网下载地址\n        :type ExternalAddr: str\n        :param Status: 状态（1成功 2失败）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    """实例可售卖的规格信息

    """

    def __init__(self):
        """
        :param SpecId: 实例规格ID，利用DescribeZones返回的SpecId，结合DescribeProductConfig返回的可售卖规格信息，可获悉某个可用区下可购买什么规格的实例\n        :type SpecId: int\n        :param MachineType: 机型ID\n        :type MachineType: str\n        :param MachineTypeName: 机型中文名称\n        :type MachineTypeName: str\n        :param Version: 数据库版本信息。取值为2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）\n        :type Version: str\n        :param VersionName: Version字段对应的版本名称\n        :type VersionName: str\n        :param Memory: 内存大小，单位GB\n        :type Memory: int\n        :param CPU: CPU核数\n        :type CPU: int\n        :param MinStorage: 此规格下最小的磁盘大小，单位GB\n        :type MinStorage: int\n        :param MaxStorage: 此规格下最大的磁盘大小，单位GB\n        :type MaxStorage: int\n        :param QPS: 此规格对应的QPS大小\n        :type QPS: int\n        :param SuitInfo: 此规格的中文描述信息\n        :type SuitInfo: str\n        :param Pid: 此规格对应的包年包月Pid\n        :type Pid: int\n        :param PostPid: 此规格对应的按量计费Pid列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostPid: list of int\n        :param PayModeStatus: 此规格下支持的付费模式，POST-仅支持按量计费 PRE-仅支持包年包月 ALL-支持所有\n        :type PayModeStatus: str\n        :param InstanceType: 产品类型，HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-基础版本型\n        :type InstanceType: str\n        :param MultiZonesStatus: 跨可用区类型，MultiZones-只支持跨可用区，SameZones-只支持同可用区，ALL-支持所有\n        :type MultiZonesStatus: str\n        """
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
        self.InstanceType = None
        self.MultiZonesStatus = None


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
        self.InstanceType = params.get("InstanceType")
        self.MultiZonesStatus = params.get("MultiZonesStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationRequest(AbstractModel):
    """StartBackupMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationResponse(AbstractModel):
    """StartBackupMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class StartIncrementalMigrationRequest(AbstractModel):
    """StartIncrementalMigration请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 导入目标实例ID\n        :type InstanceId: str\n        :param BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回\n        :type BackupMigrationId: str\n        :param IncrementalMigrationId: 增量备份导入任务ID\n        :type IncrementalMigrationId: str\n        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartIncrementalMigrationResponse(AbstractModel):
    """StartIncrementalMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class StartMigrationCheckRequest(AbstractModel):
    """StartMigrationCheck请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务id\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrationCheckResponse(AbstractModel):
    """StartMigrationCheck返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 迁移检查流程发起后，返回的流程id\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Msg: 具体步骤返回信息\n        :type Msg: str\n        :param Status: 当前步骤状态，0成功，-2未开始\n        :type Status: int\n        :param Name: 步骤名称\n        :type Name: str\n        """
        self.Msg = None
        self.Status = None
        self.Name = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationRequest(AbstractModel):
    """StopMigration请求参数结构体

    """

    def __init__(self):
        """
        :param MigrateId: 迁移任务ID\n        :type MigrateId: int\n        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationResponse(AbstractModel):
    """StopMigration返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 中止迁移流程发起后，返回的流程id\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceIdSet: 主动销毁的实例ID列表，格式如：[mssql-3l3fgqn7]。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceIdSet: list of str\n        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如mssql-j8kv137v\n        :type InstanceId: str\n        :param Memory: 实例升级后内存大小，单位GB，其值不能小于当前实例内存大小\n        :type Memory: int\n        :param Storage: 实例升级后磁盘大小，单位GB，其值不能小于当前实例磁盘大小\n        :type Storage: int\n        :param AutoVoucher: 是否自动使用代金券，0 - 不使用；1 - 默认使用。取值默认为0\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID，目前单个订单只能使用一张代金券\n        :type VoucherIds: list of str\n        :param Cpu: 实例升级后的CPU核心数\n        :type Cpu: int\n        :param DBVersion: 升级sqlserver的版本，目前支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise）版本等。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息，版本不支持降级，不填则不修改版本\n        :type DBVersion: str\n        :param HAType: 升级sqlserver的高可用架构,从镜像容灾升级到always on集群容灾，仅支持2017及以上版本且支持always on高可用的实例，不支持降级到镜像方式容灾，CLUSTER-升级为always on容灾，不填则不修改高可用架构\n        :type HAType: str\n        :param MultiZones: 修改实例是否为跨可用区容灾，SameZones-修改为同可用区 MultiZones-修改为夸可用区\n        :type MultiZones: str\n        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.Cpu = None
        self.DBVersion = None
        self.HAType = None
        self.MultiZones = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.Cpu = params.get("Cpu")
        self.DBVersion = params.get("DBVersion")
        self.HAType = params.get("HAType")
        self.MultiZones = params.get("MultiZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名称\n        :type DealName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Zone: 可用区英文ID，形如ap-guangzhou-1，表示广州一区\n        :type Zone: str\n        :param ZoneName: 可用区中文名称\n        :type ZoneName: str\n        :param ZoneId: 可用区数字ID\n        :type ZoneId: int\n        :param SpecId: 该可用区目前可售卖的规格ID，利用SpecId，结合接口DescribeProductConfig返回的数据，可获悉该可用区目前可售卖的规格大小\n        :type SpecId: int\n        :param Version: 当前可用区与规格下，可售卖的数据库版本，形如2008R2（表示SQL Server 2008 R2）。其可选值有2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）\n        :type Version: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        