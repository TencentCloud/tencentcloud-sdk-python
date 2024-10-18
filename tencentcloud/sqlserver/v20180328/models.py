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
        r"""
        :param _UserName: 实例用户名
        :type UserName: str
        :param _Password: 实例密码
        :type Password: str
        :param _DBPrivileges: DB权限列表
        :type DBPrivileges: list of DBPrivilege
        :param _Remark: 账号备注信息
        :type Remark: str
        :param _IsAdmin: 是否为管理员账户，当值为true 等价于单节点AccountType=L0，双节点AccountType=L1，当值为false，等价于AccountType=L3
        :type IsAdmin: bool
        :param _Authentication: win-windows鉴权,sql-sqlserver鉴权，不填默认值为sql-sqlserver鉴权
        :type Authentication: str
        :param _AccountType: 账号类型，IsAdmin的扩展字段。 L0-超级权限(基础版独有),L1-高级权限,L2-特殊权限,L3-普通权限，默认L3
        :type AccountType: str
        :param _IsCam: 是否开启CAM验证
        :type IsCam: bool
        """
        self._UserName = None
        self._Password = None
        self._DBPrivileges = None
        self._Remark = None
        self._IsAdmin = None
        self._Authentication = None
        self._AccountType = None
        self._IsCam = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DBPrivileges(self):
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsAdmin(self):
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def IsCam(self):
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        if params.get("DBPrivileges") is not None:
            self._DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._DBPrivileges.append(obj)
        self._Remark = params.get("Remark")
        self._IsAdmin = params.get("IsAdmin")
        self._Authentication = params.get("Authentication")
        self._AccountType = params.get("AccountType")
        self._IsCam = params.get("IsCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountDetail(AbstractModel):
    """账号信息详情

    """

    def __init__(self):
        r"""
        :param _Name: 账户名
        :type Name: str
        :param _Remark: 账户备注
        :type Remark: str
        :param _CreateTime: 账户创建时间
        :type CreateTime: str
        :param _Status: 账户状态，1-创建中，2-正常，3-修改中，4-密码重置中，-1-删除中
        :type Status: int
        :param _UpdateTime: 账户更新时间
        :type UpdateTime: str
        :param _PassTime: 密码更新时间
        :type PassTime: str
        :param _InternalStatus: 账户内部状态，正常为enable
        :type InternalStatus: str
        :param _Dbs: 该账户对相关db的读写权限信息
        :type Dbs: list of DBPrivilege
        :param _IsAdmin: 是否为管理员账户
        :type IsAdmin: bool
        :param _IsCam: 是否为cam托管账户
        :type IsCam: bool
        :param _Authentication: win-windows鉴权,sql-sqlserver鉴权
        :type Authentication: str
        :param _Host: win-windows鉴权账户需要host
        :type Host: str
        :param _AccountType: 账号类型。L0-超级权限(基础版独有),L1-高级权限,L2-特殊权限,L3-普通权限
        :type AccountType: str
        """
        self._Name = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._UpdateTime = None
        self._PassTime = None
        self._InternalStatus = None
        self._Dbs = None
        self._IsAdmin = None
        self._IsCam = None
        self._Authentication = None
        self._Host = None
        self._AccountType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PassTime(self):
        return self._PassTime

    @PassTime.setter
    def PassTime(self, PassTime):
        self._PassTime = PassTime

    @property
    def InternalStatus(self):
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Dbs(self):
        return self._Dbs

    @Dbs.setter
    def Dbs(self, Dbs):
        self._Dbs = Dbs

    @property
    def IsAdmin(self):
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def IsCam(self):
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._PassTime = params.get("PassTime")
        self._InternalStatus = params.get("InternalStatus")
        if params.get("Dbs") is not None:
            self._Dbs = []
            for item in params.get("Dbs"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._Dbs.append(obj)
        self._IsAdmin = params.get("IsAdmin")
        self._IsCam = params.get("IsCam")
        self._Authentication = params.get("Authentication")
        self._Host = params.get("Host")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPassword(AbstractModel):
    """实例账号密码信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        """
        self._UserName = None
        self._Password = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilege(AbstractModel):
    """数据库账号权限信息。创建数据库时设置

    """

    def __init__(self):
        r"""
        :param _UserName: 数据库用户名
        :type UserName: str
        :param _Privilege: 数据库权限。ReadWrite表示可读写，ReadOnly表示只读,Delete表示删除DB对该账户的权限，DBOwner所有者
        :type Privilege: str
        :param _AccountType: 账户名称，L0-超级权限(基础版独有),L1-高级权限,L2-特殊权限,L3-普通权限
        :type AccountType: str
        """
        self._UserName = None
        self._Privilege = None
        self._AccountType = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Privilege = params.get("Privilege")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilegeModifyInfo(AbstractModel):
    """数据库账号权限变更信息

    """

    def __init__(self):
        r"""
        :param _UserName: 数据库用户名
        :type UserName: str
        :param _DBPrivileges: 账号权限变更信息。参数DBPrivileges和AccAllDB只能二选一
        :type DBPrivileges: list of DBPrivilegeModifyInfo
        :param _IsAdmin: 表示是否为管理员账户，当值为true，表示是 管理员。若实例 是 单节点，则管理员所在的 账号类型为超级权限账号 ，即AccountType=L0；若实例 是 双节点，则管理员所在的 账号类型为高级权限账号，即AccountType=L1；当值为false，表示 不是管理员，则账号类型为普通账号，即AccountType=L3
        :type IsAdmin: bool
        :param _AccountType: 账号类型，IsAdmin字段的扩展字段。 L0-超级权限(基础版独有),L1-高级权限,L2-特殊权限,L3-普通权限，默认L3
        :type AccountType: str
        :param _AccAllDB: 全量修改指定账号下的所有DB权限，只支持特殊权限账号和普通权限账号。参数DBPrivileges和AccAllDB只能二选一
        :type AccAllDB: :class:`tencentcloud.sqlserver.v20180328.models.SelectAllDB`
        """
        self._UserName = None
        self._DBPrivileges = None
        self._IsAdmin = None
        self._AccountType = None
        self._AccAllDB = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DBPrivileges(self):
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def IsAdmin(self):
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def AccAllDB(self):
        return self._AccAllDB

    @AccAllDB.setter
    def AccAllDB(self, AccAllDB):
        self._AccAllDB = AccAllDB


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        if params.get("DBPrivileges") is not None:
            self._DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilegeModifyInfo()
                obj._deserialize(item)
                self._DBPrivileges.append(obj)
        self._IsAdmin = params.get("IsAdmin")
        self._AccountType = params.get("AccountType")
        if params.get("AccAllDB") is not None:
            self._AccAllDB = SelectAllDB()
            self._AccAllDB._deserialize(params.get("AccAllDB"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountRemark(AbstractModel):
    """账户备注信息

    """

    def __init__(self):
        r"""
        :param _UserName: 账户名
        :type UserName: str
        :param _Remark: 对应账户新的备注信息
        :type Remark: str
        """
        self._UserName = None
        self._Remark = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。
        :type InstanceIdSet: list of str
        """
        self._SecurityGroupId = None
        self._InstanceIdSet = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class Backup(AbstractModel):
    """备份文件详细信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名，对于单库备份文件不返回此值；单库备份文件通过DescribeBackupFiles接口获取文件名
        :type FileName: str
        :param _Size: 文件大小，单位 KB，对于单库备份文件不返回此值；单库备份文件通过DescribeBackupFiles接口获取文件大小
        :type Size: int
        :param _StartTime: 备份开始时间
        :type StartTime: str
        :param _EndTime: 备份结束时间
        :type EndTime: str
        :param _InternalAddr: 内网下载地址，对于单库备份文件不返回此值；单库备份文件通过DescribeBackupFiles接口获取下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址，对于单库备份文件不返回此值；单库备份文件通过DescribeBackupFiles接口获取下载地址
        :type ExternalAddr: str
        :param _Id: 备份文件唯一标识，RestoreInstance接口会用到该字段，对于单库备份文件不返回此值；单库备份文件通过DescribeBackupFiles接口获取可回档的ID
        :type Id: int
        :param _Status: 备份文件状态（0-创建中；1-成功；2-失败）
        :type Status: int
        :param _DBs: 多库备份时的DB列表
        :type DBs: list of str
        :param _Strategy: 备份策略（0-实例备份；1-多库备份）
        :type Strategy: int
        :param _StorageStrategy: 备份存储策略 0-跟随自定义备份保留策略 1-跟随实例生命周期直到实例下线
        :type StorageStrategy: int
        :param _BackupWay: 备份方式，0-定时备份；1-手动临时备份；2-定期备份
        :type BackupWay: int
        :param _BackupName: 备份任务名称，可自定义
        :type BackupName: str
        :param _GroupId: 聚合Id，对于打包备份文件不返回此值。通过此值调用DescribeBackupFiles接口，获取单库备份文件的详细信息
        :type GroupId: str
        :param _BackupFormat: 备份文件形式（pkg-打包备份文件，single-单库备份文件）
        :type BackupFormat: str
        :param _Region: 实例当前地域Code
        :type Region: str
        :param _CrossBackupAddr: 跨地域备份的目的地域下载链接
        :type CrossBackupAddr: list of CrossBackupAddr
        :param _CrossBackupStatus: 跨地域备份的目标地域和备份状态
        :type CrossBackupStatus: list of CrossRegionStatus
        """
        self._FileName = None
        self._Size = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Id = None
        self._Status = None
        self._DBs = None
        self._Strategy = None
        self._StorageStrategy = None
        self._BackupWay = None
        self._BackupName = None
        self._GroupId = None
        self._BackupFormat = None
        self._Region = None
        self._CrossBackupAddr = None
        self._CrossBackupStatus = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def StorageStrategy(self):
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy

    @property
    def BackupWay(self):
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def BackupFormat(self):
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        return self._CrossBackupAddr

    @CrossBackupAddr.setter
    def CrossBackupAddr(self, CrossBackupAddr):
        self._CrossBackupAddr = CrossBackupAddr

    @property
    def CrossBackupStatus(self):
        return self._CrossBackupStatus

    @CrossBackupStatus.setter
    def CrossBackupStatus(self, CrossBackupStatus):
        self._CrossBackupStatus = CrossBackupStatus


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._DBs = params.get("DBs")
        self._Strategy = params.get("Strategy")
        self._StorageStrategy = params.get("StorageStrategy")
        self._BackupWay = params.get("BackupWay")
        self._BackupName = params.get("BackupName")
        self._GroupId = params.get("GroupId")
        self._BackupFormat = params.get("BackupFormat")
        self._Region = params.get("Region")
        if params.get("CrossBackupAddr") is not None:
            self._CrossBackupAddr = []
            for item in params.get("CrossBackupAddr"):
                obj = CrossBackupAddr()
                obj._deserialize(item)
                self._CrossBackupAddr.append(obj)
        if params.get("CrossBackupStatus") is not None:
            self._CrossBackupStatus = []
            for item in params.get("CrossBackupStatus"):
                obj = CrossRegionStatus()
                obj._deserialize(item)
                self._CrossBackupStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFile(AbstractModel):
    """在非打包上传备份模式下，每个库对应一个备份文件

    """

    def __init__(self):
        r"""
        :param _Id: 备份文件唯一标识
        :type Id: int
        :param _FileName: 备份文件名称
        :type FileName: str
        :param _Size: 文件大小(K)
        :type Size: int
        :param _DBs: 备份文件的库的名称
        :type DBs: list of str
        :param _DownloadLink: 下载地址
        :type DownloadLink: str
        :param _Region: 当前实例地域码
        :type Region: str
        :param _CrossBackupAddr: 备份的跨地域region和所对应的下载地址
        :type CrossBackupAddr: list of CrossBackupAddr
        """
        self._Id = None
        self._FileName = None
        self._Size = None
        self._DBs = None
        self._DownloadLink = None
        self._Region = None
        self._CrossBackupAddr = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def DownloadLink(self):
        return self._DownloadLink

    @DownloadLink.setter
    def DownloadLink(self, DownloadLink):
        self._DownloadLink = DownloadLink

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        return self._CrossBackupAddr

    @CrossBackupAddr.setter
    def CrossBackupAddr(self, CrossBackupAddr):
        self._CrossBackupAddr = CrossBackupAddr


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._DBs = params.get("DBs")
        self._DownloadLink = params.get("DownloadLink")
        self._Region = params.get("Region")
        if params.get("CrossBackupAddr") is not None:
            self._CrossBackupAddr = []
            for item in params.get("CrossBackupAddr"):
                obj = CrossBackupAddr()
                obj._deserialize(item)
                self._CrossBackupAddr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceReadOnlyGroupRequest(AbstractModel):
    """BalanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _ReadOnlyGroupId: 只读组ID，格式如：mssqlrg-dj5i29c5n
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceReadOnlyGroupResponse(AbstractModel):
    """BalanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BusinessIntelligenceFile(AbstractModel):
    """商业智能服务文件类型

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _FileURL: 文件的COS_URL
        :type FileURL: str
        :param _FilePath: 文件在服务器上的路径
        :type FilePath: str
        :param _FileSize: 文件大小，单位时Byte
        :type FileSize: int
        :param _FileMd5: 文件md5值
        :type FileMd5: str
        :param _Status: 部署文件状态 1-初始化待部署 2-部署中 3-部署成功 4-部署失败
        :type Status: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _CreateTime: 文件创建时间
        :type CreateTime: str
        :param _StartTime: 文件部署开始时间
        :type StartTime: str
        :param _EndTime: 文件部署结束时间
        :type EndTime: str
        :param _Message: 报错信息返回
        :type Message: str
        :param _InstanceId: 商业智能实例ID
        :type InstanceId: str
        :param _Action: 动作相关信息
        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.FileAction`
        """
        self._FileName = None
        self._FileType = None
        self._FileURL = None
        self._FilePath = None
        self._FileSize = None
        self._FileMd5 = None
        self._Status = None
        self._Remark = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Message = None
        self._InstanceId = None
        self._Action = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileURL(self):
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileMd5(self):
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileURL = params.get("FileURL")
        self._FilePath = params.get("FilePath")
        self._FileSize = params.get("FileSize")
        self._FileMd5 = params.get("FileMd5")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        if params.get("Action") is not None:
            self._Action = FileAction()
            self._Action._deserialize(params.get("Action"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckItem(AbstractModel):
    """实例变配检查条目

    """

    def __init__(self):
        r"""
        :param _CheckName: 检查项目名称，CK_CPU-变配后CPU风险检查；CK_MASTER_STORAGE-只读副本变配下，只读副本磁盘空间不小于主实例空间检查；CK_MEMORY-变配后内存风险检查；CK_STORAGE-变配后磁盘空间风险检查；CK_UPGRATE-变配是否需要迁移检查；
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckName: str
        :param _CurrentValue: 检查项目返回值，CK_CPU-当前CPU近7天最大的使用率(%) ；CK_MASTER_STORAGE-主实例的磁盘空间(GB)；CK_MEMORY-当前内存近7天最大的使用值（GB)；
CK_STORAGE-当前磁盘近7天最大的使用值（GB)；CK_UPGRATE- 当前变配检查是否需要迁移，MIGRATE需要迁移变配，LOCAL本地变配；
        :type CurrentValue: str
        :param _Passed: 检查条目是否通过 0-不通过，不能变配； 1-通过，可以变配
        :type Passed: int
        :param _IsAffect: 本条目变配是否对实例有影响 0-没有影响 1-有影响
        :type IsAffect: int
        :param _Msg: 有影响或者不通过的情况下的必要描述
        :type Msg: str
        :param _MsgCode: 描述对应的代码
        :type MsgCode: int
        """
        self._CheckName = None
        self._CurrentValue = None
        self._Passed = None
        self._IsAffect = None
        self._Msg = None
        self._MsgCode = None

    @property
    def CheckName(self):
        return self._CheckName

    @CheckName.setter
    def CheckName(self, CheckName):
        self._CheckName = CheckName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Passed(self):
        return self._Passed

    @Passed.setter
    def Passed(self, Passed):
        self._Passed = Passed

    @property
    def IsAffect(self):
        return self._IsAffect

    @IsAffect.setter
    def IsAffect(self, IsAffect):
        self._IsAffect = IsAffect

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def MsgCode(self):
        return self._MsgCode

    @MsgCode.setter
    def MsgCode(self, MsgCode):
        self._MsgCode = MsgCode


    def _deserialize(self, params):
        self._CheckName = params.get("CheckName")
        self._CurrentValue = params.get("CurrentValue")
        self._Passed = params.get("Passed")
        self._IsAffect = params.get("IsAffect")
        self._Msg = params.get("Msg")
        self._MsgCode = params.get("MsgCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBRequest(AbstractModel):
    """CloneDB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _RenameRestore: 按照ReNameRestoreDatabase中的库进行克隆，并重命名，新库名称必须指定
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._RenameRestore = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenameRestore(self):
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBResponse(AbstractModel):
    """CloneDB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程任务ID，使用FlowId调用DescribeFlowStatus接口获取任务执行状态
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseInterCommunicationRequest(AbstractModel):
    """CloseInterCommunication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 关闭互通的实例ID集合
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseInterCommunicationResponse(AbstractModel):
    """CloseInterCommunication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InterInstanceFlowSet: 实例和异步流程ID
        :type InterInstanceFlowSet: list of InterInstanceFlow
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InterInstanceFlowSet = None
        self._RequestId = None

    @property
    def InterInstanceFlowSet(self):
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InterInstanceFlowSet") is not None:
            self._InterInstanceFlowSet = []
            for item in params.get("InterInstanceFlowSet"):
                obj = InterInstanceFlow()
                obj._deserialize(item)
                self._InterInstanceFlowSet.append(obj)
        self._RequestId = params.get("RequestId")


class CompleteExpansionRequest(AbstractModel):
    """CompleteExpansion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class CompleteExpansionResponse(AbstractModel):
    """CompleteExpansion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CompleteMigrationRequest(AbstractModel):
    """CompleteMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrationResponse(AbstractModel):
    """CompleteMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 完成迁移流程发起后，返回的流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CosUploadBackupFile(AbstractModel):
    """查询已经上传的备份文件大小。

    """

    def __init__(self):
        r"""
        :param _FileName: 备份名称
        :type FileName: str
        :param _Size: 备份大小
        :type Size: int
        """
        self._FileName = None
        self._Size = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: 数据库实例账户信息
        :type Accounts: list of AccountCreateInfo
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountCreateInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateBackupMigrationRequest(AbstractModel):
    """CreateBackupMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _RecoveryType: 迁移任务恢复类型，FULL-全量备份恢复，FULL_LOG-全量备份+事务日志恢复，FULL_DIFF-全量备份+差异备份恢复
        :type RecoveryType: str
        :param _UploadType: 备份上传类型，COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，需要用户上传。
        :type UploadType: str
        :param _MigrationName: 任务名称
        :type MigrationName: str
        :param _BackupFiles: UploadType是COS_URL时这里填URL，COS_UPLOAD这里填备份文件的名字。只支持1个备份文件，但1个备份文件内可包含多个库
        :type BackupFiles: list of str
        """
        self._InstanceId = None
        self._RecoveryType = None
        self._UploadType = None
        self._MigrationName = None
        self._BackupFiles = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def MigrationName(self):
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._MigrationName = params.get("MigrationName")
        self._BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupMigrationResponse(AbstractModel):
    """CreateBackupMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: 备份导入任务ID
        :type BackupMigrationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupMigrationId = None
        self._RequestId = None

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Strategy: 备份策略(0-实例备份 1-多库备份)
        :type Strategy: int
        :param _DBNames: 需要备份库名的列表(多库备份才填写)
        :type DBNames: list of str
        :param _InstanceId: 实例ID（必填），形如mssql-i1z41iwd
        :type InstanceId: str
        :param _BackupName: 备份名称，若不填则自动生成“实例ID_备份开始时间戳”
        :type BackupName: str
        :param _StorageStrategy: 备份存储策略 0-跟随自定义备份保留策略 1-跟随实例生命周期直到实例下线，默认取值0
        :type StorageStrategy: int
        """
        self._Strategy = None
        self._DBNames = None
        self._InstanceId = None
        self._BackupName = None
        self._StorageStrategy = None

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def DBNames(self):
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StorageStrategy(self):
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy


    def _deserialize(self, params):
        self._Strategy = params.get("Strategy")
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._StorageStrategy = params.get("StorageStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateBasicDBInstancesRequest(AbstractModel):
    """CreateBasicDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _Cpu: 实例的CPU核心数
        :type Cpu: int
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz
        :type VpcId: str
        :param _MachineType: 购买实例的宿主机类型，CLOUD_PREMIUM-虚拟机高性能云硬盘，CLOUD_SSD-虚拟机SSD云硬盘,CLOUD_HSSD-虚拟机增强型SSD云硬盘，CLOUD_BSSD-虚拟机通用型SSD云盘
        :type MachineType: str
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param _AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param _Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param _StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param _Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        """
        self._Zone = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._SubnetId = None
        self._VpcId = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._DBVersion = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDBInstancesResponse(AbstractModel):
    """CreateBasicDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateBusinessDBInstancesRequest(AbstractModel):
    """CreateBusinessDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _Cpu: 预购买实例的CPU核心数
        :type Cpu: int
        :param _MachineType: 购买实例的宿主机类型，CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘
        :type MachineType: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsNum: 本次购买几个实例，默认值为1
        :type GoodsNum: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _DBVersion: 商业智能服务器版本，目前只支持：201603（SQL Server 2016 Integration Services），201703（SQL Server 2017 Integration Services），201903（SQL Server 2019 Integration Services）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本201903。
        :type DBVersion: str
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param _StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param _Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._DBVersion = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._ResourceTags = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._DBVersion = params.get("DBVersion")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBusinessDBInstancesResponse(AbstractModel):
    """CreateBusinessDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _InstanceIdSet: 实例ID集合
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._FlowId = None
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._FlowId = params.get("FlowId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateBusinessIntelligenceFileRequest(AbstractModel):
    """CreateBusinessIntelligenceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileURL: COS_URL
        :type FileURL: str
        :param _FileType: 文件类型 FLAT-作为数据源的平面文件， SSIS-ssis项目包
        :type FileType: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._FileURL = None
        self._FileType = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileURL(self):
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileURL = params.get("FileURL")
        self._FileType = params.get("FileType")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBusinessIntelligenceFileResponse(AbstractModel):
    """CreateBusinessIntelligenceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileTaskId: 文件名称
        :type FileTaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileTaskId = None
        self._RequestId = None

    @property
    def FileTaskId(self):
        return self._FileTaskId

    @FileTaskId.setter
    def FileTaskId(self, FileTaskId):
        self._FileTaskId = FileTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileTaskId = params.get("FileTaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudDBInstancesRequest(AbstractModel):
    """CreateCloudDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _Cpu: 实例核心数
        :type Cpu: int
        :param _MachineType: 购买实例的宿主机磁盘类型,CLOUD_HSSD-虚拟机加强型SSD云盘，CLOUD_TSSD-虚拟机极速型SSD云盘，CLOUD_BSSD-虚拟机通用型SSD云盘
        :type MachineType: str
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param _StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param _Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param _MultiZones: 是否跨可用区部署，默认值为false
        :type MultiZones: bool
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._DBVersion = None
        self._AutoRenewFlag = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._MultiZones = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def MultiZones(self):
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._DBVersion = params.get("DBVersion")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudDBInstancesResponse(AbstractModel):
    """CreateCloudDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateCloudReadOnlyDBInstancesRequest(AbstractModel):
    """CreateCloudReadOnlyDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _ReadOnlyGroupType: 只读组类型选项，1-按照一个实例一个只读组的方式发货，2-新建只读组后发货，所有实例都在这个只读组下面， 3-发货的所有实例都在已有的只读组下面
        :type ReadOnlyGroupType: int
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _Cpu: 实例核心数
        :type Cpu: int
        :param _MachineType: 购买实例的宿主机磁盘类型,CLOUD_HSSD-虚拟机加强型SSD云盘，CLOUD_TSSD-虚拟机极速型SSD云盘，CLOUD_BSSD-虚拟机通用型SSD云盘
        :type MachineType: str
        :param _ReadOnlyGroupForcedUpgrade: 0-默认不升级主实例，1-强制升级主实例完成ro部署；主实例为非集群版时需要填1，强制升级为集群版。填1 说明您已同意将主实例升级到集群版实例。
        :type ReadOnlyGroupForcedUpgrade: int
        :param _ReadOnlyGroupId: ReadOnlyGroupType=3时必填,已存在的只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: ReadOnlyGroupType=2时必填，新建的只读组名称
        :type ReadOnlyGroupName: str
        :param _ReadOnlyGroupIsOfflineDelay: ReadOnlyGroupType=2时必填，新建的只读组是否开启延迟剔除功能，1-开启，0-关闭。当只读副本与主实例延迟大于阈值后，自动剔除。
        :type ReadOnlyGroupIsOfflineDelay: int
        :param _ReadOnlyGroupMaxDelayTime: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除的阈值。
        :type ReadOnlyGroupMaxDelayTime: int
        :param _ReadOnlyGroupMinInGroup: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除后至少保留只读副本的个数。
        :type ReadOnlyGroupMinInGroup: int
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _GoodsNum: 本次即将购买的实例数量，默认取值2。
        :type GoodsNum: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        """
        self._InstanceId = None
        self._Zone = None
        self._ReadOnlyGroupType = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._ReadOnlyGroupForcedUpgrade = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReadOnlyGroupIsOfflineDelay = None
        self._ReadOnlyGroupMaxDelayTime = None
        self._ReadOnlyGroupMinInGroup = None
        self._InstanceChargeType = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._ReadOnlyGroupType = params.get("ReadOnlyGroupType")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._ReadOnlyGroupForcedUpgrade = params.get("ReadOnlyGroupForcedUpgrade")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReadOnlyGroupIsOfflineDelay = params.get("ReadOnlyGroupIsOfflineDelay")
        self._ReadOnlyGroupMaxDelayTime = params.get("ReadOnlyGroupMaxDelayTime")
        self._ReadOnlyGroupMinInGroup = params.get("ReadOnlyGroupMinInGroup")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudReadOnlyDBInstancesResponse(AbstractModel):
    """CreateCloudReadOnlyDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单名称数组
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param _StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param _Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param _HAType: 购买高可用实例的类型：DUAL-双机高可用  CLUSTER-集群，默认值为DUAL
        :type HAType: str
        :param _MultiZones: 是否跨可用区部署，默认值为false
        :type MultiZones: bool
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._DBVersion = None
        self._AutoRenewFlag = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._HAType = None
        self._MultiZones = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def HAType(self):
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._DBVersion = params.get("DBVersion")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _DealNames: 订单名称数组
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._DealNames = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    """CreateDB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DBs: 数据库创建信息
        :type DBs: list of DBCreateInfo
        """
        self._InstanceId = None
        self._DBs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBs") is not None:
            self._DBs = []
            for item in params.get("DBs"):
                obj = DBCreateInfo()
                obj._deserialize(item)
                self._DBs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBResponse(AbstractModel):
    """CreateDB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateIncrementalMigrationRequest(AbstractModel):
    """CreateIncrementalMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _BackupFiles: 增量备份文件，全量备份任务UploadType是COS_URL时这里填URL，是COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库
        :type BackupFiles: list of str
        :param _IsRecovery: 是否需要恢复，NO-不需要，YES-需要，默认不需要
        :type IsRecovery: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._BackupFiles = None
        self._IsRecovery = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def IsRecovery(self):
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._BackupFiles = params.get("BackupFiles")
        self._IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIncrementalMigrationResponse(AbstractModel):
    """CreateIncrementalMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IncrementalMigrationId: 增量备份导入任务ID
        :type IncrementalMigrationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IncrementalMigrationId = None
        self._RequestId = None

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._RequestId = params.get("RequestId")


class CreateMigrationRequest(AbstractModel):
    """CreateMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateName: 迁移任务的名称
        :type MigrateName: str
        :param _MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）
        :type MigrateType: int
        :param _SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param _Source: 迁移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: 迁移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: 迁移DB对象 ，离线迁移不使用（SourceType=4或SourceType=5）。
        :type MigrateDBSet: list of MigrateDB
        :param _RenameRestore: 按照ReNameRestoreDatabase中的库进行恢复，并重命名，不填则按照默认方式命名恢复的库，且恢复所有的库。SourceType=5的情况下有效。
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._MigrateName = None
        self._MigrateType = None
        self._SourceType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None
        self._RenameRestore = None

    @property
    def MigrateName(self):
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RenameRestore(self):
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._MigrateName = params.get("MigrateName")
        self._MigrateType = params.get("MigrateType")
        self._SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationResponse(AbstractModel):
    """CreateMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MigrateId = None
        self._RequestId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class CreatePublishSubscribeRequest(AbstractModel):
    """CreatePublishSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PublishInstanceId: 发布实例ID，形如mssql-j8kv137v
        :type PublishInstanceId: str
        :param _SubscribeInstanceId: 订阅实例ID，形如mssql-j8kv137v
        :type SubscribeInstanceId: str
        :param _DatabaseTupleSet: 数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTuple
        :param _PublishSubscribeName: 发布订阅的名称，默认值为：default_name
        :type PublishSubscribeName: str
        """
        self._PublishInstanceId = None
        self._SubscribeInstanceId = None
        self._DatabaseTupleSet = None
        self._PublishSubscribeName = None

    @property
    def PublishInstanceId(self):
        return self._PublishInstanceId

    @PublishInstanceId.setter
    def PublishInstanceId(self, PublishInstanceId):
        self._PublishInstanceId = PublishInstanceId

    @property
    def SubscribeInstanceId(self):
        return self._SubscribeInstanceId

    @SubscribeInstanceId.setter
    def SubscribeInstanceId(self, SubscribeInstanceId):
        self._SubscribeInstanceId = SubscribeInstanceId

    @property
    def DatabaseTupleSet(self):
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet

    @property
    def PublishSubscribeName(self):
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName


    def _deserialize(self, params):
        self._PublishInstanceId = params.get("PublishInstanceId")
        self._SubscribeInstanceId = params.get("SubscribeInstanceId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePublishSubscribeResponse(AbstractModel):
    """CreatePublishSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID，可通过接口DescribeFlowStatus查询立即切换升级任务的状态。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyDBInstancesRequest(AbstractModel):
    """CreateReadOnlyDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _ReadOnlyGroupType: 只读组类型选项，1-按照一个实例一个只读组的方式发货，2-新建只读组后发货，所有实例都在这个只读组下面， 3-发货的所有实例都在已有的只读组下面
        :type ReadOnlyGroupType: int
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _ReadOnlyGroupForcedUpgrade: 0-默认不升级主实例，1-强制升级主实例完成ro部署；主实例为非集群版时需要填1，强制升级为集群版。填1 说明您已同意将主实例升级到集群版实例。
        :type ReadOnlyGroupForcedUpgrade: int
        :param _ReadOnlyGroupId: ReadOnlyGroupType=3时必填,已存在的只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: ReadOnlyGroupType=2时必填，新建的只读组名称
        :type ReadOnlyGroupName: str
        :param _ReadOnlyGroupIsOfflineDelay: ReadOnlyGroupType=2时必填，新建的只读组是否开启延迟剔除功能，1-开启，0-关闭。当只读副本与主实例延迟大于阈值后，自动剔除。
        :type ReadOnlyGroupIsOfflineDelay: int
        :param _ReadOnlyGroupMaxDelayTime: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除的阈值。
        :type ReadOnlyGroupMaxDelayTime: int
        :param _ReadOnlyGroupMinInGroup: ReadOnlyGroupType=2 且 ReadOnlyGroupIsOfflineDelay=1时必填，新建的只读组延迟剔除后至少保留只读副本的个数。
        :type ReadOnlyGroupMinInGroup: int
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _GoodsNum: 本次购买几个只读实例，默认值为2。
        :type GoodsNum: int
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _AutoVoucher: 是否自动使用代金券；1 - 是，0 - 否，默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前单个订单只能使用一张
        :type VoucherIds: list of str
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        """
        self._InstanceId = None
        self._Zone = None
        self._ReadOnlyGroupType = None
        self._Memory = None
        self._Storage = None
        self._ReadOnlyGroupForcedUpgrade = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReadOnlyGroupIsOfflineDelay = None
        self._ReadOnlyGroupMaxDelayTime = None
        self._ReadOnlyGroupMinInGroup = None
        self._InstanceChargeType = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._ReadOnlyGroupType = params.get("ReadOnlyGroupType")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ReadOnlyGroupForcedUpgrade = params.get("ReadOnlyGroupForcedUpgrade")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReadOnlyGroupIsOfflineDelay = params.get("ReadOnlyGroupIsOfflineDelay")
        self._ReadOnlyGroupMaxDelayTime = params.get("ReadOnlyGroupMaxDelayTime")
        self._ReadOnlyGroupMinInGroup = params.get("ReadOnlyGroupMinInGroup")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstancesResponse(AbstractModel):
    """CreateReadOnlyDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单名称数组
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CrossBackupAddr(AbstractModel):
    """跨地域备份下载地址集合

    """

    def __init__(self):
        r"""
        :param _CrossRegion: 跨地域备份目标地域
        :type CrossRegion: str
        :param _CrossInternalAddr: 跨地域备份内网下载地址
        :type CrossInternalAddr: str
        :param _CrossExternalAddr: 跨地域备份外网下载地址
        :type CrossExternalAddr: str
        """
        self._CrossRegion = None
        self._CrossInternalAddr = None
        self._CrossExternalAddr = None

    @property
    def CrossRegion(self):
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossInternalAddr(self):
        return self._CrossInternalAddr

    @CrossInternalAddr.setter
    def CrossInternalAddr(self, CrossInternalAddr):
        self._CrossInternalAddr = CrossInternalAddr

    @property
    def CrossExternalAddr(self):
        return self._CrossExternalAddr

    @CrossExternalAddr.setter
    def CrossExternalAddr(self, CrossExternalAddr):
        self._CrossExternalAddr = CrossExternalAddr


    def _deserialize(self, params):
        self._CrossRegion = params.get("CrossRegion")
        self._CrossInternalAddr = params.get("CrossInternalAddr")
        self._CrossExternalAddr = params.get("CrossExternalAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossRegionStatus(AbstractModel):
    """跨地域备份的目标地域和备份状态

    """

    def __init__(self):
        r"""
        :param _CrossRegion: 跨地域备份目标地域
        :type CrossRegion: str
        :param _CrossStatus: 备份跨地域的同步状态 0-创建中；1-成功；2-失败；4-同步中
        :type CrossStatus: int
        """
        self._CrossRegion = None
        self._CrossStatus = None

    @property
    def CrossRegion(self):
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossStatus(self):
        return self._CrossStatus

    @CrossStatus.setter
    def CrossStatus(self, CrossStatus):
        self._CrossStatus = CrossStatus


    def _deserialize(self, params):
        self._CrossRegion = params.get("CrossRegion")
        self._CrossStatus = params.get("CrossStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossSummaryDetailRes(AbstractModel):
    """跨地域备份实时统计列表项

    """

    def __init__(self):
        r"""
        :param _Status: 实例状态
        :type Status: int
        :param _Region: 实例所属地域
        :type Region: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _CrossBackupEnabled: 跨地域备份状态 enable-开启，disable-关闭
        :type CrossBackupEnabled: str
        :param _CrossRegions: 跨地域备份目标地域
        :type CrossRegions: list of str
        :param _LastBackupStartTime: 最新备份开始时间
        :type LastBackupStartTime: str
        :param _CrossBackupSaveDays: 跨地域备份保留天数
        :type CrossBackupSaveDays: int
        :param _DataBackupSpace: 跨地域数据备份总空间
        :type DataBackupSpace: int
        :param _DataBackupCount: 跨地域数据备份文件总个数
        :type DataBackupCount: int
        :param _LogBackupSpace: 跨地域日志备份总空间
        :type LogBackupSpace: int
        :param _LogBackupCount: 跨地域日志备份文件总个数
        :type LogBackupCount: int
        :param _ActualUsedSpace: 跨地域备份总空间
        :type ActualUsedSpace: int
        :param _ActualUsedCount: 跨地域备份总个数
        :type ActualUsedCount: int
        """
        self._Status = None
        self._Region = None
        self._InstanceId = None
        self._Name = None
        self._CrossBackupEnabled = None
        self._CrossRegions = None
        self._LastBackupStartTime = None
        self._CrossBackupSaveDays = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._ActualUsedSpace = None
        self._ActualUsedCount = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CrossBackupEnabled(self):
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def CrossRegions(self):
        return self._CrossRegions

    @CrossRegions.setter
    def CrossRegions(self, CrossRegions):
        self._CrossRegions = CrossRegions

    @property
    def LastBackupStartTime(self):
        return self._LastBackupStartTime

    @LastBackupStartTime.setter
    def LastBackupStartTime(self, LastBackupStartTime):
        self._LastBackupStartTime = LastBackupStartTime

    @property
    def CrossBackupSaveDays(self):
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def DataBackupSpace(self):
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def LogBackupSpace(self):
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def ActualUsedSpace(self):
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def ActualUsedCount(self):
        return self._ActualUsedCount

    @ActualUsedCount.setter
    def ActualUsedCount(self, ActualUsedCount):
        self._ActualUsedCount = ActualUsedCount


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._CrossRegions = params.get("CrossRegions")
        self._LastBackupStartTime = params.get("LastBackupStartTime")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._ActualUsedCount = params.get("ActualUsedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CutXEventsRequest(AbstractModel):
    """CutXEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class CutXEventsResponse(AbstractModel):
    """CutXEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DBCreateInfo(AbstractModel):
    """数据库创建信息

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名
        :type DBName: str
        :param _Charset: 字符集。可通过接口DescribeDBCharsets查到支持的字符集，不填默认为Chinese_PRC_CI_AS。
        :type Charset: str
        :param _Accounts: 数据库账号权限信息
        :type Accounts: list of AccountPrivilege
        :param _Remark: 备注
        :type Remark: str
        """
        self._DBName = None
        self._Charset = None
        self._Accounts = None
        self._Remark = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Charset = params.get("Charset")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBDetail(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        r"""
        :param _Name: 数据库名称
        :type Name: str
        :param _Charset: 字符集
        :type Charset: str
        :param _Remark: 备注
        :type Remark: str
        :param _CreateTime: 数据库创建时间
        :type CreateTime: str
        :param _Status: 数据库状态。1--创建中， 2--运行中， 3--修改中，-1--删除中
        :type Status: int
        :param _Accounts: 数据库账号权限信息
        :type Accounts: list of AccountPrivilege
        :param _InternalStatus: 内部状态。ONLINE表示运行中
        :type InternalStatus: str
        :param _Encryption: 是否已开启TDE加密，enable-已加密，disable-未加密
        :type Encryption: str
        """
        self._Name = None
        self._Charset = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._Accounts = None
        self._InternalStatus = None
        self._Encryption = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def InternalStatus(self):
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Charset = params.get("Charset")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._InternalStatus = params.get("InternalStatus")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _ProjectId: 实例所在项目ID
        :type ProjectId: int
        :param _RegionId: 实例所在地域ID
        :type RegionId: int
        :param _ZoneId: 实例所在可用区ID
        :type ZoneId: int
        :param _VpcId: 实例所在私有网络ID，基础网络时为 0
        :type VpcId: int
        :param _SubnetId: 实例所在私有网络子网ID，基础网络时为 0
        :type SubnetId: int
        :param _Status: 实例状态。取值范围： <li>1：申请中</li> <li>2：运行中</li> <li>3：受限运行中 (主备切换中)</li> <li>4：已隔离</li> <li>5：回收中</li> <li>6：已回收</li> <li>7：任务执行中 (实例做备份、回档等操作)</li> <li>8：已下线</li> <li>9：实例扩容中</li> <li>10：实例迁移中</li> <li>11：只读</li> <li>12：重启中</li>  <li>13：实例修改中且待切换</li> <li>14：订阅发布创建中</li> <li>15：订阅发布修改中</li> <li>16：实例修改中且切换中</li> <li>17：创建RO副本中</li>
        :type Status: int
        :param _Vip: 实例访问IP
        :type Vip: str
        :param _Vport: 实例访问端口
        :type Vport: int
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _UpdateTime: 实例更新时间
        :type UpdateTime: str
        :param _StartTime: 实例计费开始时间
        :type StartTime: str
        :param _EndTime: 实例计费结束时间
        :type EndTime: str
        :param _IsolateTime: 实例隔离时间
        :type IsolateTime: str
        :param _Memory: 实例内存大小，单位G
        :type Memory: int
        :param _UsedStorage: 实例已经使用存储空间大小，单位G
        :type UsedStorage: int
        :param _Storage: 实例存储空间大小，单位G
        :type Storage: int
        :param _VersionName: 实例版本
        :type VersionName: str
        :param _RenewFlag: 实例续费标记，0-正常续费，1-自动续费，2-到期不续费
        :type RenewFlag: int
        :param _Model: 实例高可用， 1-双机高可用，2-单机，3-跨可用区，4-集群跨可用区，5-集群，9-自研机房
        :type Model: int
        :param _Region: 实例所在地域名称，如 ap-guangzhou
        :type Region: str
        :param _Zone: 实例所在可用区名称，如 ap-guangzhou-1
        :type Zone: str
        :param _BackupTime: 备份时间点
        :type BackupTime: str
        :param _PayMode: 实例付费模式， 0-按量计费，1-包年包月
        :type PayMode: int
        :param _Uid: 实例唯一UID
        :type Uid: str
        :param _Cpu: 实例cpu核心数
        :type Cpu: int
        :param _Version: 实例版本代号
        :type Version: str
        :param _Type: 实例类型代号："TS85"-物理机，本地SSD硬盘；"Z3"-物理机早期版本，本地SSD硬盘；"CLOUD_BASIC"-虚拟机，普通云硬盘；"CLOUD_PREMIUM"-虚拟机，高性能云硬盘；"CLOUD_SSD"-虚拟机，云SSD硬盘；"CLOUD_HSSD"-虚拟机，增强型SSD云硬盘；"CLOUD_TSSD"-虚拟机，极速型SSD云硬盘；"CLOUD_BSSD"-虚拟机，通用型SSD云硬盘
        :type Type: str
        :param _Pid: 计费ID
        :type Pid: int
        :param _UniqVpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，基础网络时为空字符串
        :type UniqVpcId: str
        :param _UniqSubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，基础网络时为空字符串
        :type UniqSubnetId: str
        :param _IsolateOperator: 实例隔离操作
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateOperator: str
        :param _SubFlag: 发布订阅标识，SUB-订阅实例，PUB-发布实例，空值-没有发布订阅的普通实例
注意：此字段可能返回 null，表示取不到有效值。
        :type SubFlag: str
        :param _ROFlag: 只读标识，RO-只读实例，MASTER-有RO实例的主实例，空值-没有只读组的非RO实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ROFlag: str
        :param _HAFlag: 容灾类型，MIRROR-镜像，ALWAYSON-AlwaysOn, SINGLE-单例
注意：此字段可能返回 null，表示取不到有效值。
        :type HAFlag: str
        :param _ResourceTags: 实例绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of ResourceTag
        :param _BackupModel: 备份模式，master_pkg-主节点打包备份(默认) ；master_no_pkg-主节点不打包备份；slave_pkg-从节点打包备份(always on集群有效)；slave_no_pkg-从节点不打包备份(always on集群有效)；只读副本对该值无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupModel: str
        :param _InstanceNote: 实例备份信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNote: str
        :param _BackupCycle: 备份周期
        :type BackupCycle: list of int
        :param _BackupCycleType: 备份周期类型，[daily、weekly、monthly]
        :type BackupCycleType: str
        :param _BackupSaveDays: 数据(日志)备份保留时间
        :type BackupSaveDays: int
        :param _InstanceType: 实例类型 HA-高可用 RO-只读实例 SI-基础版 BI-商业智能服务
        :type InstanceType: str
        :param _CrossRegions: 跨地域备份目的地域，如果为空，则表示未开启跨地域备份
        :type CrossRegions: list of str
        :param _CrossBackupEnabled: 跨地域备份状态 enable-开启，disable-关闭
        :type CrossBackupEnabled: str
        :param _CrossBackupSaveDays: 跨地域备份保留天数，则默认7天
        :type CrossBackupSaveDays: int
        :param _DnsPodDomain: 外网地址域名
        :type DnsPodDomain: str
        :param _TgwWanVPort: 外网端口号
        :type TgwWanVPort: int
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        :param _IsDrZone: 是否跨AZ
        :type IsDrZone: bool
        :param _SlaveZones: 备可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: :class:`tencentcloud.sqlserver.v20180328.models.SlaveZones`
        :param _Architecture: 架构标识，SINGLE-单节点 DOUBLE-双节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: str
        :param _Style: 类型标识，EXCLUSIVE-独享型，SHARED-共享型
注意：此字段可能返回 null，表示取不到有效值。
        :type Style: str
        """
        self._InstanceId = None
        self._Name = None
        self._ProjectId = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._IsolateTime = None
        self._Memory = None
        self._UsedStorage = None
        self._Storage = None
        self._VersionName = None
        self._RenewFlag = None
        self._Model = None
        self._Region = None
        self._Zone = None
        self._BackupTime = None
        self._PayMode = None
        self._Uid = None
        self._Cpu = None
        self._Version = None
        self._Type = None
        self._Pid = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._IsolateOperator = None
        self._SubFlag = None
        self._ROFlag = None
        self._HAFlag = None
        self._ResourceTags = None
        self._BackupModel = None
        self._InstanceNote = None
        self._BackupCycle = None
        self._BackupCycleType = None
        self._BackupSaveDays = None
        self._InstanceType = None
        self._CrossRegions = None
        self._CrossBackupEnabled = None
        self._CrossBackupSaveDays = None
        self._DnsPodDomain = None
        self._TgwWanVPort = None
        self._Collation = None
        self._TimeZone = None
        self._IsDrZone = None
        self._SlaveZones = None
        self._Architecture = None
        self._Style = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UsedStorage(self):
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BackupTime(self):
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def IsolateOperator(self):
        return self._IsolateOperator

    @IsolateOperator.setter
    def IsolateOperator(self, IsolateOperator):
        self._IsolateOperator = IsolateOperator

    @property
    def SubFlag(self):
        return self._SubFlag

    @SubFlag.setter
    def SubFlag(self, SubFlag):
        self._SubFlag = SubFlag

    @property
    def ROFlag(self):
        return self._ROFlag

    @ROFlag.setter
    def ROFlag(self, ROFlag):
        self._ROFlag = ROFlag

    @property
    def HAFlag(self):
        return self._HAFlag

    @HAFlag.setter
    def HAFlag(self, HAFlag):
        self._HAFlag = HAFlag

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def BackupModel(self):
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def InstanceNote(self):
        return self._InstanceNote

    @InstanceNote.setter
    def InstanceNote(self, InstanceNote):
        self._InstanceNote = InstanceNote

    @property
    def BackupCycle(self):
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupCycleType(self):
        return self._BackupCycleType

    @BackupCycleType.setter
    def BackupCycleType(self, BackupCycleType):
        self._BackupCycleType = BackupCycleType

    @property
    def BackupSaveDays(self):
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CrossRegions(self):
        return self._CrossRegions

    @CrossRegions.setter
    def CrossRegions(self, CrossRegions):
        self._CrossRegions = CrossRegions

    @property
    def CrossBackupEnabled(self):
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def CrossBackupSaveDays(self):
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def DnsPodDomain(self):
        return self._DnsPodDomain

    @DnsPodDomain.setter
    def DnsPodDomain(self, DnsPodDomain):
        self._DnsPodDomain = DnsPodDomain

    @property
    def TgwWanVPort(self):
        return self._TgwWanVPort

    @TgwWanVPort.setter
    def TgwWanVPort(self, TgwWanVPort):
        self._TgwWanVPort = TgwWanVPort

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def IsDrZone(self):
        return self._IsDrZone

    @IsDrZone.setter
    def IsDrZone(self, IsDrZone):
        self._IsDrZone = IsDrZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsolateTime = params.get("IsolateTime")
        self._Memory = params.get("Memory")
        self._UsedStorage = params.get("UsedStorage")
        self._Storage = params.get("Storage")
        self._VersionName = params.get("VersionName")
        self._RenewFlag = params.get("RenewFlag")
        self._Model = params.get("Model")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._BackupTime = params.get("BackupTime")
        self._PayMode = params.get("PayMode")
        self._Uid = params.get("Uid")
        self._Cpu = params.get("Cpu")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        self._Pid = params.get("Pid")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._IsolateOperator = params.get("IsolateOperator")
        self._SubFlag = params.get("SubFlag")
        self._ROFlag = params.get("ROFlag")
        self._HAFlag = params.get("HAFlag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._BackupModel = params.get("BackupModel")
        self._InstanceNote = params.get("InstanceNote")
        self._BackupCycle = params.get("BackupCycle")
        self._BackupCycleType = params.get("BackupCycleType")
        self._BackupSaveDays = params.get("BackupSaveDays")
        self._InstanceType = params.get("InstanceType")
        self._CrossRegions = params.get("CrossRegions")
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._DnsPodDomain = params.get("DnsPodDomain")
        self._TgwWanVPort = params.get("TgwWanVPort")
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        self._IsDrZone = params.get("IsDrZone")
        if params.get("SlaveZones") is not None:
            self._SlaveZones = SlaveZones()
            self._SlaveZones._deserialize(params.get("SlaveZones"))
        self._Architecture = params.get("Architecture")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilege(AbstractModel):
    """账号的数据库权限信息

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名
        :type DBName: str
        :param _Privilege: 数据库权限，ReadWrite表示可读写，ReadOnly表示只读，DBOwner所有者
        :type Privilege: str
        """
        self._DBName = None
        self._Privilege = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilegeModifyInfo(AbstractModel):
    """数据库权限变更信息

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名
        :type DBName: str
        :param _Privilege: 权限变更信息。ReadWrite表示可读写，ReadOnly表示只读，Delete表示删除账号对该DB的权限，DBOwner所有者
        :type Privilege: str
        """
        self._DBName = None
        self._Privilege = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBRemark(AbstractModel):
    """数据库备注信息

    """

    def __init__(self):
        r"""
        :param _Name: 数据库名称
        :type Name: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._Name = None
        self._Remark = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBRenameRes(AbstractModel):
    """数据库重命名返回参数

    """

    def __init__(self):
        r"""
        :param _NewName: 新数据库名称
        :type NewName: str
        :param _OldName: 老数据库名称
        :type OldName: str
        """
        self._NewName = None
        self._OldName = None

    @property
    def NewName(self):
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def OldName(self):
        return self._OldName

    @OldName.setter
    def OldName(self, OldName):
        self._OldName = OldName


    def _deserialize(self, params):
        self._NewName = params.get("NewName")
        self._OldName = params.get("OldName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBTDEEncrypt(AbstractModel):
    """开启、关闭TDE数据库加密

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名称
        :type DBName: str
        :param _Encryption: enable-开启数据库TDE加密，disable-关闭数据库TDE加密
        :type Encryption: str
        """
        self._DBName = None
        self._Encryption = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataBasePrivilegeModifyInfo(AbstractModel):
    """数据库账号权限变更信息

    """

    def __init__(self):
        r"""
        :param _DataBaseName: 数据库名称
        :type DataBaseName: str
        :param _AccountPrivileges: 数据库权限变更信息
        :type AccountPrivileges: list of AccountPrivilege
        """
        self._DataBaseName = None
        self._AccountPrivileges = None

    @property
    def DataBaseName(self):
        return self._DataBaseName

    @DataBaseName.setter
    def DataBaseName(self, DataBaseName):
        self._DataBaseName = DataBaseName

    @property
    def AccountPrivileges(self):
        return self._AccountPrivileges

    @AccountPrivileges.setter
    def AccountPrivileges(self, AccountPrivileges):
        self._AccountPrivileges = AccountPrivileges


    def _deserialize(self, params):
        self._DataBaseName = params.get("DataBaseName")
        if params.get("AccountPrivileges") is not None:
            self._AccountPrivileges = []
            for item in params.get("AccountPrivileges"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._AccountPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTuple(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库。

    """

    def __init__(self):
        r"""
        :param _PublishDatabase: 发布数据库名称
        :type PublishDatabase: str
        :param _SubscribeDatabase: 订阅数据库名称
        :type SubscribeDatabase: str
        """
        self._PublishDatabase = None
        self._SubscribeDatabase = None

    @property
    def PublishDatabase(self):
        return self._PublishDatabase

    @PublishDatabase.setter
    def PublishDatabase(self, PublishDatabase):
        self._PublishDatabase = PublishDatabase

    @property
    def SubscribeDatabase(self):
        return self._SubscribeDatabase

    @SubscribeDatabase.setter
    def SubscribeDatabase(self, SubscribeDatabase):
        self._SubscribeDatabase = SubscribeDatabase


    def _deserialize(self, params):
        self._PublishDatabase = params.get("PublishDatabase")
        self._SubscribeDatabase = params.get("SubscribeDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTupleStatus(AbstractModel):
    """该数据结构表示具有发布订阅关系的两个数据库，以及其之间发布订阅的状态信息。

    """

    def __init__(self):
        r"""
        :param _PublishDatabase: 发布数据库名称
        :type PublishDatabase: str
        :param _SubscribeDatabase: 订阅数据库名称
        :type SubscribeDatabase: str
        :param _LastSyncTime: 最近一次同步时间
        :type LastSyncTime: str
        :param _Status: 数据库之间的发布订阅状态 running，success，fail，unknow
        :type Status: str
        """
        self._PublishDatabase = None
        self._SubscribeDatabase = None
        self._LastSyncTime = None
        self._Status = None

    @property
    def PublishDatabase(self):
        return self._PublishDatabase

    @PublishDatabase.setter
    def PublishDatabase(self, PublishDatabase):
        self._PublishDatabase = PublishDatabase

    @property
    def SubscribeDatabase(self):
        return self._SubscribeDatabase

    @SubscribeDatabase.setter
    def SubscribeDatabase(self, SubscribeDatabase):
        self._SubscribeDatabase = SubscribeDatabase

    @property
    def LastSyncTime(self):
        return self._LastSyncTime

    @LastSyncTime.setter
    def LastSyncTime(self, LastSyncTime):
        self._LastSyncTime = LastSyncTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PublishDatabase = params.get("PublishDatabase")
        self._SubscribeDatabase = params.get("SubscribeDatabase")
        self._LastSyncTime = params.get("LastSyncTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbNormalDetail(AbstractModel):
    """数据库配置信息

    """

    def __init__(self):
        r"""
        :param _IsSubscribed: 是否已订阅 0：否 1：是
        :type IsSubscribed: str
        :param _CollationName: 数据库排序规则
        :type CollationName: str
        :param _IsAutoCleanupOn: 开启CT之后是否自动清理 0：否 1：是
        :type IsAutoCleanupOn: str
        :param _IsBrokerEnabled: 是否已启用代理  0：否 1：是
        :type IsBrokerEnabled: str
        :param _IsCdcEnabled: 是否已开启/关闭CDC 0：关闭 1：开启
        :type IsCdcEnabled: str
        :param _IsDbChainingOn: 是否已启用/ 禁用CT 0：禁用 1：启用
        :type IsDbChainingOn: str
        :param _IsEncrypted: 是否加密 0：否 1：是
        :type IsEncrypted: str
        :param _IsFulltextEnabled: 是否全文启用 0：否 1：是
        :type IsFulltextEnabled: str
        :param _IsMirroring: 是否是镜像 0：否 1：是
        :type IsMirroring: str
        :param _IsPublished: 是否已发布 0：否 1：是
        :type IsPublished: str
        :param _IsReadCommittedSnapshotOn: 是否开启快照 0：否 1：是
        :type IsReadCommittedSnapshotOn: str
        :param _IsTrustworthyOn: 是否可信任 0：否 1：是
        :type IsTrustworthyOn: str
        :param _MirroringState: 镜像状态
        :type MirroringState: str
        :param _Name: 数据库名称
        :type Name: str
        :param _RecoveryModelDesc: 恢复模式
        :type RecoveryModelDesc: str
        :param _RetentionPeriod: 保留天数
        :type RetentionPeriod: str
        :param _StateDesc: 数据库状态
        :type StateDesc: str
        :param _UserAccessDesc: 用户类型
        :type UserAccessDesc: str
        :param _CreateTime: 数据库创建时间
        :type CreateTime: str
        :param _IsFullTextEnabled: 是否全文启用 0：否 1：是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFullTextEnabled: str
        """
        self._IsSubscribed = None
        self._CollationName = None
        self._IsAutoCleanupOn = None
        self._IsBrokerEnabled = None
        self._IsCdcEnabled = None
        self._IsDbChainingOn = None
        self._IsEncrypted = None
        self._IsFulltextEnabled = None
        self._IsMirroring = None
        self._IsPublished = None
        self._IsReadCommittedSnapshotOn = None
        self._IsTrustworthyOn = None
        self._MirroringState = None
        self._Name = None
        self._RecoveryModelDesc = None
        self._RetentionPeriod = None
        self._StateDesc = None
        self._UserAccessDesc = None
        self._CreateTime = None
        self._IsFullTextEnabled = None

    @property
    def IsSubscribed(self):
        return self._IsSubscribed

    @IsSubscribed.setter
    def IsSubscribed(self, IsSubscribed):
        self._IsSubscribed = IsSubscribed

    @property
    def CollationName(self):
        return self._CollationName

    @CollationName.setter
    def CollationName(self, CollationName):
        self._CollationName = CollationName

    @property
    def IsAutoCleanupOn(self):
        return self._IsAutoCleanupOn

    @IsAutoCleanupOn.setter
    def IsAutoCleanupOn(self, IsAutoCleanupOn):
        self._IsAutoCleanupOn = IsAutoCleanupOn

    @property
    def IsBrokerEnabled(self):
        return self._IsBrokerEnabled

    @IsBrokerEnabled.setter
    def IsBrokerEnabled(self, IsBrokerEnabled):
        self._IsBrokerEnabled = IsBrokerEnabled

    @property
    def IsCdcEnabled(self):
        return self._IsCdcEnabled

    @IsCdcEnabled.setter
    def IsCdcEnabled(self, IsCdcEnabled):
        self._IsCdcEnabled = IsCdcEnabled

    @property
    def IsDbChainingOn(self):
        return self._IsDbChainingOn

    @IsDbChainingOn.setter
    def IsDbChainingOn(self, IsDbChainingOn):
        self._IsDbChainingOn = IsDbChainingOn

    @property
    def IsEncrypted(self):
        return self._IsEncrypted

    @IsEncrypted.setter
    def IsEncrypted(self, IsEncrypted):
        self._IsEncrypted = IsEncrypted

    @property
    def IsFulltextEnabled(self):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        return self._IsFulltextEnabled

    @IsFulltextEnabled.setter
    def IsFulltextEnabled(self, IsFulltextEnabled):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        self._IsFulltextEnabled = IsFulltextEnabled

    @property
    def IsMirroring(self):
        return self._IsMirroring

    @IsMirroring.setter
    def IsMirroring(self, IsMirroring):
        self._IsMirroring = IsMirroring

    @property
    def IsPublished(self):
        return self._IsPublished

    @IsPublished.setter
    def IsPublished(self, IsPublished):
        self._IsPublished = IsPublished

    @property
    def IsReadCommittedSnapshotOn(self):
        return self._IsReadCommittedSnapshotOn

    @IsReadCommittedSnapshotOn.setter
    def IsReadCommittedSnapshotOn(self, IsReadCommittedSnapshotOn):
        self._IsReadCommittedSnapshotOn = IsReadCommittedSnapshotOn

    @property
    def IsTrustworthyOn(self):
        return self._IsTrustworthyOn

    @IsTrustworthyOn.setter
    def IsTrustworthyOn(self, IsTrustworthyOn):
        self._IsTrustworthyOn = IsTrustworthyOn

    @property
    def MirroringState(self):
        return self._MirroringState

    @MirroringState.setter
    def MirroringState(self, MirroringState):
        self._MirroringState = MirroringState

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RecoveryModelDesc(self):
        return self._RecoveryModelDesc

    @RecoveryModelDesc.setter
    def RecoveryModelDesc(self, RecoveryModelDesc):
        self._RecoveryModelDesc = RecoveryModelDesc

    @property
    def RetentionPeriod(self):
        return self._RetentionPeriod

    @RetentionPeriod.setter
    def RetentionPeriod(self, RetentionPeriod):
        self._RetentionPeriod = RetentionPeriod

    @property
    def StateDesc(self):
        return self._StateDesc

    @StateDesc.setter
    def StateDesc(self, StateDesc):
        self._StateDesc = StateDesc

    @property
    def UserAccessDesc(self):
        return self._UserAccessDesc

    @UserAccessDesc.setter
    def UserAccessDesc(self, UserAccessDesc):
        self._UserAccessDesc = UserAccessDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsFullTextEnabled(self):
        return self._IsFullTextEnabled

    @IsFullTextEnabled.setter
    def IsFullTextEnabled(self, IsFullTextEnabled):
        self._IsFullTextEnabled = IsFullTextEnabled


    def _deserialize(self, params):
        self._IsSubscribed = params.get("IsSubscribed")
        self._CollationName = params.get("CollationName")
        self._IsAutoCleanupOn = params.get("IsAutoCleanupOn")
        self._IsBrokerEnabled = params.get("IsBrokerEnabled")
        self._IsCdcEnabled = params.get("IsCdcEnabled")
        self._IsDbChainingOn = params.get("IsDbChainingOn")
        self._IsEncrypted = params.get("IsEncrypted")
        self._IsFulltextEnabled = params.get("IsFulltextEnabled")
        self._IsMirroring = params.get("IsMirroring")
        self._IsPublished = params.get("IsPublished")
        self._IsReadCommittedSnapshotOn = params.get("IsReadCommittedSnapshotOn")
        self._IsTrustworthyOn = params.get("IsTrustworthyOn")
        self._MirroringState = params.get("MirroringState")
        self._Name = params.get("Name")
        self._RecoveryModelDesc = params.get("RecoveryModelDesc")
        self._RetentionPeriod = params.get("RetentionPeriod")
        self._StateDesc = params.get("StateDesc")
        self._UserAccessDesc = params.get("UserAccessDesc")
        self._CreateTime = params.get("CreateTime")
        self._IsFullTextEnabled = params.get("IsFullTextEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbRollbackTimeInfo(AbstractModel):
    """数据库可回档时间范围信息

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名称
        :type DBName: str
        :param _StartTime: 可回档开始时间
        :type StartTime: str
        :param _EndTime: 可回档结束时间
        :type EndTime: str
        """
        self._DBName = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名
        :type DealName: str
        :param _Count: 商品数量
        :type Count: int
        :param _FlowId: 关联的流程 ID，可用于查询流程执行状态
        :type FlowId: int
        :param _InstanceIdSet: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
        :type InstanceIdSet: list of str
        :param _OwnerUin: 所属账号
        :type OwnerUin: str
        :param _InstanceChargeType: 实例付费类型
        :type InstanceChargeType: str
        """
        self._DealName = None
        self._Count = None
        self._FlowId = None
        self._InstanceIdSet = None
        self._OwnerUin = None
        self._InstanceChargeType = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._Count = params.get("Count")
        self._FlowId = params.get("FlowId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._OwnerUin = params.get("OwnerUin")
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInstance(AbstractModel):
    """订单号对应的资源ID列表

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: list of str
        :param _DealName: 订单号
        :type DealName: str
        """
        self._InstanceId = None
        self._DealName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _UserNames: 实例用户名数组
        :type UserNames: list of str
        """
        self._InstanceId = None
        self._UserNames = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserNames(self):
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserNames = params.get("UserNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DeleteBackupMigrationRequest(AbstractModel):
    """DeleteBackupMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 目标实例ID，由DescribeBackupMigration接口返回
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由DescribeBackupMigration接口返回
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupMigrationResponse(AbstractModel):
    """DeleteBackupMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteBusinessIntelligenceFileRequest(AbstractModel):
    """DeleteBusinessIntelligenceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileNameSet: 文件名称集合
        :type FileNameSet: list of str
        """
        self._InstanceId = None
        self._FileNameSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileNameSet(self):
        return self._FileNameSet

    @FileNameSet.setter
    def FileNameSet(self, FileNameSet):
        self._FileNameSet = FileNameSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileNameSet = params.get("FileNameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBusinessIntelligenceFileResponse(AbstractModel):
    """DeleteBusinessIntelligenceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DeleteDBInstanceResponse(AbstractModel):
    """DeleteDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteDBRequest(AbstractModel):
    """DeleteDB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param _Names: 数据库名数组
        :type Names: list of str
        """
        self._InstanceId = None
        self._Names = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBResponse(AbstractModel):
    """DeleteDB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DeleteIncrementalMigrationRequest(AbstractModel):
    """DeleteIncrementalMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: 增量备份导入任务ID，由CreateIncrementalMigration接口返回
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIncrementalMigrationResponse(AbstractModel):
    """DeleteIncrementalMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeletePublishSubscribeRequest(AbstractModel):
    """DeletePublishSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PublishSubscribeId: 发布订阅ID，可通过DescribePublishSubscribe接口获得
        :type PublishSubscribeId: int
        :param _DatabaseTupleSet: 待删除的数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTuple
        """
        self._PublishSubscribeId = None
        self._DatabaseTupleSet = None

    @property
    def PublishSubscribeId(self):
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def DatabaseTupleSet(self):
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePublishSubscribeResponse(AbstractModel):
    """DeletePublishSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRestoreTaskRequest(AbstractModel):
    """DeleteRestoreTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RestoreIds: 回档任务记录ID集合，一次最多删除10条
        :type RestoreIds: list of int
        """
        self._InstanceId = None
        self._RestoreIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RestoreIds(self):
        return self._RestoreIds

    @RestoreIds.setter
    def RestoreIds(self, RestoreIds):
        self._RestoreIds = RestoreIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RestoreIds = params.get("RestoreIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRestoreTaskResponse(AbstractModel):
    """DeleteRestoreTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAccountPrivilegeByDBRequest(AbstractModel):
    """DescribeAccountPrivilegeByDB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _DBName: 数据库名称
        :type DBName: str
        :param _AccountName: 数据库属于账号名称
        :type AccountName: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        """
        self._InstanceId = None
        self._DBName = None
        self._AccountName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBName = params.get("DBName")
        self._AccountName = params.get("AccountName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegeByDBResponse(AbstractModel):
    """DescribeAccountPrivilegeByDB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 账号总数量
        :type TotalCount: int
        :param _Accounts: 账号权限列表
        :type Accounts: list of AccountPrivilege
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _Name: 账号名称
        :type Name: str
        :param _OrderBy: createTime,updateTime,passTime" note:"排序字段，默认按照账号创建时间倒序
        :type OrderBy: str
        :param _OrderByType: 排序规则（desc-降序，asc-升序），默认desc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Accounts: 账户信息列表
        :type Accounts: list of AccountDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupByFlowIdRequest(AbstractModel):
    """DescribeBackupByFlowId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _FlowId: 创建备份流程ID，可通过 [CreateBackup](https://cloud.tencent.com/document/product/238/19946) 接口获取
        :type FlowId: str
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupByFlowIdResponse(AbstractModel):
    """DescribeBackupByFlowId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 备份文件唯一标识，RestoreInstance接口会用到该字段，对于单库备份文件只返回第一条记录的备份文件唯一标识；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的可回档的ID
        :type Id: int
        :param _FileName: 文件名，对于单库备份文件只返回第一条记录的文件名；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的文件名
        :type FileName: str
        :param _BackupName: 备份任务名称，可自定义
        :type BackupName: str
        :param _StartTime: 备份开始时间
        :type StartTime: str
        :param _EndTime: 备份结束时间
        :type EndTime: str
        :param _Size: 文件大小，单位 KB，对于单库备份文件只返回第一条记录的文件大小；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的文件大小
        :type Size: int
        :param _Strategy: 备份策略，0-实例备份；1-多库备份；实例状态是0-创建中时，该字段为默认值0，无实际意义
        :type Strategy: int
        :param _Status: 备份文件状态，0-创建中；1-成功；2-失败
        :type Status: int
        :param _BackupWay: 备份方式，0-定时备份；1-手动临时备份；实例状态是0-创建中时，该字段为默认值0，无实际意义
        :type BackupWay: int
        :param _DBs: DB列表，对于单库备份文件只返回第一条记录包含的库名；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的库名。
        :type DBs: list of str
        :param _InternalAddr: 内网下载地址，对于单库备份文件只返回第一条记录的内网下载地址；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址，对于单库备份文件只返回第一条记录的外网下载地址；单库备份文件需要通过DescribeBackupFiles接口获取全部记录的下载地址
        :type ExternalAddr: str
        :param _GroupId: 聚合Id，对于打包备份文件不返回此值。通过此值调用DescribeBackupFiles接口，获取单库备份文件的详细信息
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._FileName = None
        self._BackupName = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Strategy = None
        self._Status = None
        self._BackupWay = None
        self._DBs = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._GroupId = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BackupWay(self):
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def InternalAddr(self):
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._BackupName = params.get("BackupName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Strategy = params.get("Strategy")
        self._Status = params.get("Status")
        self._BackupWay = params.get("BackupWay")
        self._DBs = params.get("DBs")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class DescribeBackupCommandRequest(AbstractModel):
    """DescribeBackupCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupFileType: 备份文件类型，FULL-全量备份，FULL_LOG-全量备份需要日志增量，FULL_DIFF-全量备份需要差异增量，LOG-日志备份，DIFF-差异备份
        :type BackupFileType: str
        :param _DataBaseName: 数据库名称
        :type DataBaseName: str
        :param _IsRecovery: 是否需要恢复，NO-不需要，YES-需要
        :type IsRecovery: str
        :param _LocalPath: 备份文件保存的路径；如果不填则默认在D:\\
        :type LocalPath: str
        """
        self._BackupFileType = None
        self._DataBaseName = None
        self._IsRecovery = None
        self._LocalPath = None

    @property
    def BackupFileType(self):
        return self._BackupFileType

    @BackupFileType.setter
    def BackupFileType(self, BackupFileType):
        self._BackupFileType = BackupFileType

    @property
    def DataBaseName(self):
        return self._DataBaseName

    @DataBaseName.setter
    def DataBaseName(self, DataBaseName):
        self._DataBaseName = DataBaseName

    @property
    def IsRecovery(self):
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def LocalPath(self):
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._BackupFileType = params.get("BackupFileType")
        self._DataBaseName = params.get("DataBaseName")
        self._IsRecovery = params.get("IsRecovery")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupCommandResponse(AbstractModel):
    """DescribeBackupCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Command: 创建备份命令
        :type Command: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Command = None
        self._RequestId = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Command = params.get("Command")
        self._RequestId = params.get("RequestId")


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _GroupId: 单库备份的聚合ID, 可通过接口DescribeBackups获取（不支持查询打包备份记录）
        :type GroupId: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _DatabaseName: 按照备份的库名称筛选，不填则不筛选此项
        :type DatabaseName: str
        :param _OrderBy: 列表项排序，目前只按照备份大小排序（desc-降序，asc-升序），默认desc
        :type OrderBy: str
        """
        self._InstanceId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None
        self._DatabaseName = None
        self._OrderBy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份总数量
        :type TotalCount: int
        :param _BackupFiles: 备份文件列表详情
        :type BackupFiles: list of BackupFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupFiles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupFiles") is not None:
            self._BackupFiles = []
            for item in params.get("BackupFiles"):
                obj = BackupFile()
                obj._deserialize(item)
                self._BackupFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupMigrationRequest(AbstractModel):
    """DescribeBackupMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _MigrationName: 导入任务名称
        :type MigrationName: str
        :param _BackupFileName: 备份文件名称
        :type BackupFileName: str
        :param _StatusSet: 导入任务状态集合
        :type StatusSet: list of int
        :param _RecoveryType: 导入任务恢复类型，FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param _UploadType: COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传
        :type UploadType: str
        :param _Limit: 分页，页大小，默认值：100
        :type Limit: int
        :param _Offset: 分页，页数，默认值：0
        :type Offset: int
        :param _OrderBy: 排序字段，name；createTime；startTime；endTime，默认按照createTime递增排序。
        :type OrderBy: str
        :param _OrderByType: 排序方式，desc-递减排序，asc-递增排序。默认按照asc排序，且在OrderBy为有效值时，本参数有效
        :type OrderByType: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._MigrationName = None
        self._BackupFileName = None
        self._StatusSet = None
        self._RecoveryType = None
        self._UploadType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFileName(self):
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def RecoveryType(self):
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._MigrationName = params.get("MigrationName")
        self._BackupFileName = params.get("BackupFileName")
        self._StatusSet = params.get("StatusSet")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupMigrationResponse(AbstractModel):
    """DescribeBackupMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 迁移任务总数
        :type TotalCount: int
        :param _BackupMigrationSet: 迁移任务集合
        :type BackupMigrationSet: list of Migration
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupMonitorRequest(AbstractModel):
    """DescribeBackupMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 备份空间使用详情开始时间
        :type StartTime: str
        :param _EndTime: 备份空间使用详情结束时间
        :type EndTime: str
        :param _Type: 备份趋势查询类型，local-本地备份，cross-跨地域备份
        :type Type: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Type = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupMonitorResponse(AbstractModel):
    """DescribeBackupMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeStamp: 备份趋势图时间轴
        :type TimeStamp: list of str
        :param _FreeSpace: 免费备份空间
        :type FreeSpace: list of float
        :param _ActualUsedSpace: 实际总备份空间
        :type ActualUsedSpace: list of float
        :param _LogBackupSpace: 日志备份空间
        :type LogBackupSpace: list of float
        :param _DataBackupSpace: 数据备份空间
        :type DataBackupSpace: list of float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TimeStamp = None
        self._FreeSpace = None
        self._ActualUsedSpace = None
        self._LogBackupSpace = None
        self._DataBackupSpace = None
        self._RequestId = None

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

    @property
    def FreeSpace(self):
        return self._FreeSpace

    @FreeSpace.setter
    def FreeSpace(self, FreeSpace):
        self._FreeSpace = FreeSpace

    @property
    def ActualUsedSpace(self):
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def LogBackupSpace(self):
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def DataBackupSpace(self):
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TimeStamp = params.get("TimeStamp")
        self._FreeSpace = params.get("FreeSpace")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._RequestId = params.get("RequestId")


class DescribeBackupStatisticalRequest(AbstractModel):
    """DescribeBackupStatistical请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页。
        :type Offset: int
        :param _InstanceIdSet: 一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl。
        :type InstanceIdSet: list of str
        :param _InstanceNameSet: 实例名称列表，模糊查询。
        :type InstanceNameSet: list of str
        :param _OrderBy: 排序字段，默认default，则按照备份空间降序。
default 按照备份空间排序
data 数据备份排序
log 日志备份排序
auto 自动备份排序
manual 手动备份排序
        :type OrderBy: str
        :param _OrderByType: 默认降序，[desc-降序，asc-升序]。
        :type OrderByType: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceIdSet = None
        self._InstanceNameSet = None
        self._OrderBy = None
        self._OrderByType = None

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
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceNameSet(self):
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupStatisticalResponse(AbstractModel):
    """DescribeBackupStatistical返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例总数。分页返回的话，这个值指的是所有符合条件的实例的个数，而非当前根据Limit和Offset值返回的实例个数。
        :type TotalCount: int
        :param _Items: 实例列表。
        :type Items: list of SummaryDetailRes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SummaryDetailRes()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupSummaryRequest(AbstractModel):
    """DescribeBackupSummary请求参数结构体

    """


class DescribeBackupSummaryResponse(AbstractModel):
    """DescribeBackupSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FreeSpace: 实际免费总空间，单位(KB)。
        :type FreeSpace: int
        :param _ActualUsedSpace: 备份实际使用空间，单位(KB)。
        :type ActualUsedSpace: int
        :param _BackupFilesTotal: 备份文件总个数。
        :type BackupFilesTotal: int
        :param _BillingSpace: 备份占用收费空间，单位(KB)。
        :type BillingSpace: int
        :param _DataBackupSpace: 数据备份使用空间，单位(KB)。
        :type DataBackupSpace: int
        :param _DataBackupCount: 数据备份文件总个数。
        :type DataBackupCount: int
        :param _ManualBackupSpace: 数据备份中手动备份使用空间，单位(KB)。
        :type ManualBackupSpace: int
        :param _ManualBackupCount: 数据备份中手动备份文件总个数。
        :type ManualBackupCount: int
        :param _AutoBackupSpace: 数据备份中自动备份使用空间，单位(KB)。
        :type AutoBackupSpace: int
        :param _AutoBackupCount: 数据备份中自动备份文件总个数。
        :type AutoBackupCount: int
        :param _LogBackupSpace: 日志备份使用空间，单位(KB)。
        :type LogBackupSpace: int
        :param _LogBackupCount: 日志备份文件总个数。
        :type LogBackupCount: int
        :param _EstimatedAmount: 预估收费金额，单位（元/小时）。
        :type EstimatedAmount: float
        :param _LocalBackupFilesTotal: 本地备份文件总个数
        :type LocalBackupFilesTotal: int
        :param _CrossBackupFilesTotal: 跨地域备份文件总个数
        :type CrossBackupFilesTotal: int
        :param _CrossBillingSpace: 跨地域备份占用收费空间，单位（KB）
        :type CrossBillingSpace: int
        :param _CrossAutoBackupSpace: 跨地域自动数据备份使用空间，单位（KB）
        :type CrossAutoBackupSpace: int
        :param _CrossAutoBackupCount: 跨地域自动数据备份文件总个数
        :type CrossAutoBackupCount: int
        :param _LocalLogBackupSpace: 本地日志备份使用空间，单位（KB）
        :type LocalLogBackupSpace: int
        :param _LocalLogBackupCount: 本地日志备份文件总个数
        :type LocalLogBackupCount: int
        :param _CrossLogBackupSpace: 跨地域日志备份使用空间，单位（KB）
        :type CrossLogBackupSpace: int
        :param _CrossLogBackupCount: 跨地域日志备份文件总个数
        :type CrossLogBackupCount: int
        :param _CrossEstimatedAmount: 跨地域备份预估收费金额，单位（元/小时）
        :type CrossEstimatedAmount: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FreeSpace = None
        self._ActualUsedSpace = None
        self._BackupFilesTotal = None
        self._BillingSpace = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._ManualBackupSpace = None
        self._ManualBackupCount = None
        self._AutoBackupSpace = None
        self._AutoBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._EstimatedAmount = None
        self._LocalBackupFilesTotal = None
        self._CrossBackupFilesTotal = None
        self._CrossBillingSpace = None
        self._CrossAutoBackupSpace = None
        self._CrossAutoBackupCount = None
        self._LocalLogBackupSpace = None
        self._LocalLogBackupCount = None
        self._CrossLogBackupSpace = None
        self._CrossLogBackupCount = None
        self._CrossEstimatedAmount = None
        self._RequestId = None

    @property
    def FreeSpace(self):
        return self._FreeSpace

    @FreeSpace.setter
    def FreeSpace(self, FreeSpace):
        self._FreeSpace = FreeSpace

    @property
    def ActualUsedSpace(self):
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def BackupFilesTotal(self):
        return self._BackupFilesTotal

    @BackupFilesTotal.setter
    def BackupFilesTotal(self, BackupFilesTotal):
        self._BackupFilesTotal = BackupFilesTotal

    @property
    def BillingSpace(self):
        return self._BillingSpace

    @BillingSpace.setter
    def BillingSpace(self, BillingSpace):
        self._BillingSpace = BillingSpace

    @property
    def DataBackupSpace(self):
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def ManualBackupSpace(self):
        return self._ManualBackupSpace

    @ManualBackupSpace.setter
    def ManualBackupSpace(self, ManualBackupSpace):
        self._ManualBackupSpace = ManualBackupSpace

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def AutoBackupSpace(self):
        return self._AutoBackupSpace

    @AutoBackupSpace.setter
    def AutoBackupSpace(self, AutoBackupSpace):
        self._AutoBackupSpace = AutoBackupSpace

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def LogBackupSpace(self):
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def EstimatedAmount(self):
        return self._EstimatedAmount

    @EstimatedAmount.setter
    def EstimatedAmount(self, EstimatedAmount):
        self._EstimatedAmount = EstimatedAmount

    @property
    def LocalBackupFilesTotal(self):
        return self._LocalBackupFilesTotal

    @LocalBackupFilesTotal.setter
    def LocalBackupFilesTotal(self, LocalBackupFilesTotal):
        self._LocalBackupFilesTotal = LocalBackupFilesTotal

    @property
    def CrossBackupFilesTotal(self):
        return self._CrossBackupFilesTotal

    @CrossBackupFilesTotal.setter
    def CrossBackupFilesTotal(self, CrossBackupFilesTotal):
        self._CrossBackupFilesTotal = CrossBackupFilesTotal

    @property
    def CrossBillingSpace(self):
        return self._CrossBillingSpace

    @CrossBillingSpace.setter
    def CrossBillingSpace(self, CrossBillingSpace):
        self._CrossBillingSpace = CrossBillingSpace

    @property
    def CrossAutoBackupSpace(self):
        return self._CrossAutoBackupSpace

    @CrossAutoBackupSpace.setter
    def CrossAutoBackupSpace(self, CrossAutoBackupSpace):
        self._CrossAutoBackupSpace = CrossAutoBackupSpace

    @property
    def CrossAutoBackupCount(self):
        return self._CrossAutoBackupCount

    @CrossAutoBackupCount.setter
    def CrossAutoBackupCount(self, CrossAutoBackupCount):
        self._CrossAutoBackupCount = CrossAutoBackupCount

    @property
    def LocalLogBackupSpace(self):
        return self._LocalLogBackupSpace

    @LocalLogBackupSpace.setter
    def LocalLogBackupSpace(self, LocalLogBackupSpace):
        self._LocalLogBackupSpace = LocalLogBackupSpace

    @property
    def LocalLogBackupCount(self):
        return self._LocalLogBackupCount

    @LocalLogBackupCount.setter
    def LocalLogBackupCount(self, LocalLogBackupCount):
        self._LocalLogBackupCount = LocalLogBackupCount

    @property
    def CrossLogBackupSpace(self):
        return self._CrossLogBackupSpace

    @CrossLogBackupSpace.setter
    def CrossLogBackupSpace(self, CrossLogBackupSpace):
        self._CrossLogBackupSpace = CrossLogBackupSpace

    @property
    def CrossLogBackupCount(self):
        return self._CrossLogBackupCount

    @CrossLogBackupCount.setter
    def CrossLogBackupCount(self, CrossLogBackupCount):
        self._CrossLogBackupCount = CrossLogBackupCount

    @property
    def CrossEstimatedAmount(self):
        return self._CrossEstimatedAmount

    @CrossEstimatedAmount.setter
    def CrossEstimatedAmount(self, CrossEstimatedAmount):
        self._CrossEstimatedAmount = CrossEstimatedAmount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FreeSpace = params.get("FreeSpace")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._BackupFilesTotal = params.get("BackupFilesTotal")
        self._BillingSpace = params.get("BillingSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._ManualBackupSpace = params.get("ManualBackupSpace")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._AutoBackupSpace = params.get("AutoBackupSpace")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._EstimatedAmount = params.get("EstimatedAmount")
        self._LocalBackupFilesTotal = params.get("LocalBackupFilesTotal")
        self._CrossBackupFilesTotal = params.get("CrossBackupFilesTotal")
        self._CrossBillingSpace = params.get("CrossBillingSpace")
        self._CrossAutoBackupSpace = params.get("CrossAutoBackupSpace")
        self._CrossAutoBackupCount = params.get("CrossAutoBackupCount")
        self._LocalLogBackupSpace = params.get("LocalLogBackupSpace")
        self._LocalLogBackupCount = params.get("LocalLogBackupCount")
        self._CrossLogBackupSpace = params.get("CrossLogBackupSpace")
        self._CrossLogBackupCount = params.get("CrossLogBackupCount")
        self._CrossEstimatedAmount = params.get("CrossEstimatedAmount")
        self._RequestId = params.get("RequestId")


class DescribeBackupUploadSizeRequest(AbstractModel):
    """DescribeBackupUploadSize请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: 增量导入任务ID
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUploadSizeResponse(AbstractModel):
    """DescribeBackupUploadSize返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosUploadBackupFileSet: 已上传的备份的信息
        :type CosUploadBackupFileSet: list of CosUploadBackupFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosUploadBackupFileSet = None
        self._RequestId = None

    @property
    def CosUploadBackupFileSet(self):
        return self._CosUploadBackupFileSet

    @CosUploadBackupFileSet.setter
    def CosUploadBackupFileSet(self, CosUploadBackupFileSet):
        self._CosUploadBackupFileSet = CosUploadBackupFileSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CosUploadBackupFileSet") is not None:
            self._CosUploadBackupFileSet = []
            for item in params.get("CosUploadBackupFileSet"):
                obj = CosUploadBackupFile()
                obj._deserialize(item)
                self._CosUploadBackupFileSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param _EndTime: 结束时间(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param _InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _BackupName: 按照备份名称筛选，不填则不筛选此项
        :type BackupName: str
        :param _Strategy: 按照备份策略筛选，0-实例备份，1-多库备份，不填则不筛选此项
        :type Strategy: int
        :param _BackupWay: 按照备份方式筛选，0-后台自动定时备份，1-用户手动临时备份，2-定期备份，不填则不筛选此项
        :type BackupWay: int
        :param _BackupId: 按照备份ID筛选，不填则不筛选此项
        :type BackupId: int
        :param _DatabaseName: 按照备份的库名称筛选，不填则不筛选此项
        :type DatabaseName: str
        :param _Group: 是否分组查询，默认是0，单库备份情况下 0-兼容老方式不分组，1-单库备份分组后展示
        :type Group: int
        :param _Type: 备份类型，1-数据备份，2-日志备份，默认值为1
        :type Type: int
        :param _BackupFormat: 按照备份文件形式筛选，pkg-打包备份文件，single-单库备份文件
        :type BackupFormat: str
        :param _StorageStrategy: 备份存储策略 0-跟随自定义备份保留策略 1-跟随实例生命周期直到实例下线，默认取值0
        :type StorageStrategy: int
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._BackupName = None
        self._Strategy = None
        self._BackupWay = None
        self._BackupId = None
        self._DatabaseName = None
        self._Group = None
        self._Type = None
        self._BackupFormat = None
        self._StorageStrategy = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def BackupWay(self):
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BackupFormat(self):
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat

    @property
    def StorageStrategy(self):
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BackupName = params.get("BackupName")
        self._Strategy = params.get("Strategy")
        self._BackupWay = params.get("BackupWay")
        self._BackupId = params.get("BackupId")
        self._DatabaseName = params.get("DatabaseName")
        self._Group = params.get("Group")
        self._Type = params.get("Type")
        self._BackupFormat = params.get("BackupFormat")
        self._StorageStrategy = params.get("StorageStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份总数量
        :type TotalCount: int
        :param _Backups: 备份列表详情
        :type Backups: list of Backup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Backups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Backups(self):
        return self._Backups

    @Backups.setter
    def Backups(self, Backups):
        self._Backups = Backups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Backups") is not None:
            self._Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self._Backups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBusinessIntelligenceFileRequest(AbstractModel):
    """DescribeBusinessIntelligenceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _StatusSet: 迁移任务状态集合,1-初始化待部署 2-部署中 3-部署成功 4-部署失败
        :type StatusSet: list of int
        :param _FileType: 文件类型 FLAT-平面文件，SSIS商业智能服务项目文件
        :type FileType: str
        :param _Limit: 分页，页大小，范围1-100
        :type Limit: int
        :param _Offset: 分页,页数，默认0
        :type Offset: int
        :param _OrderBy: 排序字段，可选值file_name,create_time,start_time
        :type OrderBy: str
        :param _OrderByType: 排序方式，desc,asc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._FileName = None
        self._StatusSet = None
        self._FileType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def StatusSet(self):
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileName = params.get("FileName")
        self._StatusSet = params.get("StatusSet")
        self._FileType = params.get("FileType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBusinessIntelligenceFileResponse(AbstractModel):
    """DescribeBusinessIntelligenceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 文件部署任务总数
        :type TotalCount: int
        :param _BackupMigrationSet: 文件部署任务集合
        :type BackupMigrationSet: list of BusinessIntelligenceFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = BusinessIntelligenceFile()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCollationTimeZoneRequest(AbstractModel):
    """DescribeCollationTimeZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineType: 购买实例的宿主机类型，PM-物理机, CLOUD_PREMIUM-云服务器高性能云盘，
CLOUD_SSD-云服务器SSD云盘,CLOUD_HSSD-云服务器加强型SSD云盘，CLOUD_TSSD-云服务器极速型SSD云盘，CLOUD_BSSD-云服务器通用型SSD云盘,CLOUD_BASIC-云服务器云硬盘，默认取值PM
        :type MachineType: str
        :param _DBVersion: 购买实例版本号
        :type DBVersion: str
        """
        self._MachineType = None
        self._DBVersion = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._DBVersion = params.get("DBVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCollationTimeZoneResponse(AbstractModel):
    """DescribeCollationTimeZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Collation: 系统字符集排序规则列表
        :type Collation: list of str
        :param _TimeZone: 系统时区列表
        :type TimeZone: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Collation = None
        self._TimeZone = None
        self._RequestId = None

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        self._RequestId = params.get("RequestId")


class DescribeCrossBackupStatisticalRequest(AbstractModel):
    """DescribeCrossBackupStatistical请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页,页数
        :type Offset: int
        :param _Limit: 分页，页大小
        :type Limit: int
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param _InstanceNameSet: 实例名称列表
        :type InstanceNameSet: list of str
        :param _CrossBackupStatus: 跨地域备份状态，enable-开启，disable-关闭
        :type CrossBackupStatus: str
        :param _CrossRegion: 跨地域备份目标地域
        :type CrossRegion: str
        :param _OrderBy: 排序字段，默认default-按照备份空间降序排序，data-按照数据备份排序，log-按照日志备份培训
        :type OrderBy: str
        :param _OrderByType: 排序规则（desc-降序，asc-升序），默认desc
        :type OrderByType: str
        """
        self._Offset = None
        self._Limit = None
        self._InstanceIdSet = None
        self._InstanceNameSet = None
        self._CrossBackupStatus = None
        self._CrossRegion = None
        self._OrderBy = None
        self._OrderByType = None

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
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceNameSet(self):
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def CrossBackupStatus(self):
        return self._CrossBackupStatus

    @CrossBackupStatus.setter
    def CrossBackupStatus(self, CrossBackupStatus):
        self._CrossBackupStatus = CrossBackupStatus

    @property
    def CrossRegion(self):
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._CrossBackupStatus = params.get("CrossBackupStatus")
        self._CrossRegion = params.get("CrossRegion")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBackupStatisticalResponse(AbstractModel):
    """DescribeCrossBackupStatistical返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 跨地域备份概览实时统计总条数
        :type TotalCount: int
        :param _Items: 跨地域备份概览实时统计列表
        :type Items: list of CrossSummaryDetailRes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CrossSummaryDetailRes()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCrossRegionZoneRequest(AbstractModel):
    """DescribeCrossRegionZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeCrossRegionZoneResponse(AbstractModel):
    """DescribeCrossRegionZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Region: 备机所在地域的字符串ID，形如：ap-guangzhou
        :type Region: str
        :param _Zone: 备机所在可用区的字符串ID，形如：ap-guangzhou-1
        :type Zone: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Region = None
        self._Zone = None
        self._RequestId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RequestId = params.get("RequestId")


class DescribeCrossRegionsRequest(AbstractModel):
    """DescribeCrossRegions请求参数结构体

    """


class DescribeCrossRegionsResponse(AbstractModel):
    """DescribeCrossRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: 支持跨地域备份的目标地域集合
        :type Regions: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class DescribeDBCharsetsRequest(AbstractModel):
    """DescribeDBCharsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeDBCharsetsResponse(AbstractModel):
    """DescribeDBCharsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseCharsets: 数据库字符集列表
        :type DatabaseCharsets: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DatabaseCharsets = None
        self._RequestId = None

    @property
    def DatabaseCharsets(self):
        return self._DatabaseCharsets

    @DatabaseCharsets.setter
    def DatabaseCharsets(self, DatabaseCharsets):
        self._DatabaseCharsets = DatabaseCharsets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DatabaseCharsets = params.get("DatabaseCharsets")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceInterRequest(AbstractModel):
    """DescribeDBInstanceInter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页，页大小，范围是1-100
        :type Limit: int
        :param _InstanceId: 按照实例ID筛选
        :type InstanceId: str
        :param _Status: 按照状态筛选 1-互通IP打开中；2-互通IP已经打开；3-加入到互通组中；4-已加入到互通组；5-互通IP回收中；6-互通IP已回收；7-从互通组移除中；8-已从互通组中移除
        :type Status: int
        :param _VersionSet: 实例版本代号列表
        :type VersionSet: list of str
        :param _Zone: 实例所在可用区，格式如：ap-guangzhou-2
        :type Zone: str
        :param _Offset: 分页，页数，默认是0
        :type Offset: int
        """
        self._Limit = None
        self._InstanceId = None
        self._Status = None
        self._VersionSet = None
        self._Zone = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionSet(self):
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._VersionSet = params.get("VersionSet")
        self._Zone = params.get("Zone")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInterResponse(AbstractModel):
    """DescribeDBInstanceInter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 互通组内总条数
        :type TotalCount: int
        :param _InterInstanceSet: 互通组内实例信息详情
        :type InterInstanceSet: list of InterInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InterInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InterInstanceSet(self):
        return self._InterInstanceSet

    @InterInstanceSet.setter
    def InterInstanceSet(self, InterInstanceSet):
        self._InterInstanceSet = InterInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InterInstanceSet") is not None:
            self._InterInstanceSet = []
            for item in params.get("InterInstanceSet"):
                obj = InterInstance()
                obj._deserialize(item)
                self._InterInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesAttributeRequest(AbstractModel):
    """DescribeDBInstancesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeDBInstancesAttributeResponse(AbstractModel):
    """DescribeDBInstancesAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RegularBackupEnable: 定期备份状态 enable-开启，disable-关闭
        :type RegularBackupEnable: str
        :param _RegularBackupSaveDays: 定期备份保留天数 [90 - 3650]天
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: 定期备份策略 years-每年，quarters-每季度，months-每月
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: 定期备份保留个数
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: 定期备份开始日期，格式-YYYY-MM-DD 默认当前日期
        :type RegularBackupStartTime: str
        :param _BlockedThreshold: 阻塞进程阈值，单位毫秒
        :type BlockedThreshold: int
        :param _EventSaveDays: 慢SQL、阻塞、死锁扩展事件文件保留时长
        :type EventSaveDays: int
        :param _TDEConfig: TDE透明数据加密配置
        :type TDEConfig: :class:`tencentcloud.sqlserver.v20180328.models.TDEConfigAttribute`
        :param _SSLConfig: SSL加密
        :type SSLConfig: :class:`tencentcloud.sqlserver.v20180328.models.SSLConfig`
        :param _DrReadableInfo: 备机只读信息
        :type DrReadableInfo: :class:`tencentcloud.sqlserver.v20180328.models.DrReadableInfo`
        :param _OldVipList: 等待回收的IP列表
        :type OldVipList: list of OldVip
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RegularBackupEnable = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None
        self._BlockedThreshold = None
        self._EventSaveDays = None
        self._TDEConfig = None
        self._SSLConfig = None
        self._DrReadableInfo = None
        self._OldVipList = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegularBackupEnable(self):
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime

    @property
    def BlockedThreshold(self):
        return self._BlockedThreshold

    @BlockedThreshold.setter
    def BlockedThreshold(self, BlockedThreshold):
        self._BlockedThreshold = BlockedThreshold

    @property
    def EventSaveDays(self):
        return self._EventSaveDays

    @EventSaveDays.setter
    def EventSaveDays(self, EventSaveDays):
        self._EventSaveDays = EventSaveDays

    @property
    def TDEConfig(self):
        return self._TDEConfig

    @TDEConfig.setter
    def TDEConfig(self, TDEConfig):
        self._TDEConfig = TDEConfig

    @property
    def SSLConfig(self):
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def DrReadableInfo(self):
        return self._DrReadableInfo

    @DrReadableInfo.setter
    def DrReadableInfo(self, DrReadableInfo):
        self._DrReadableInfo = DrReadableInfo

    @property
    def OldVipList(self):
        return self._OldVipList

    @OldVipList.setter
    def OldVipList(self, OldVipList):
        self._OldVipList = OldVipList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RegularBackupEnable = params.get("RegularBackupEnable")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        self._BlockedThreshold = params.get("BlockedThreshold")
        self._EventSaveDays = params.get("EventSaveDays")
        if params.get("TDEConfig") is not None:
            self._TDEConfig = TDEConfigAttribute()
            self._TDEConfig._deserialize(params.get("TDEConfig"))
        if params.get("SSLConfig") is not None:
            self._SSLConfig = SSLConfig()
            self._SSLConfig._deserialize(params.get("SSLConfig"))
        if params.get("DrReadableInfo") is not None:
            self._DrReadableInfo = DrReadableInfo()
            self._DrReadableInfo._deserialize(params.get("DrReadableInfo"))
        if params.get("OldVipList") is not None:
            self._OldVipList = []
            for item in params.get("OldVipList"):
                obj = OldVip()
                obj._deserialize(item)
                self._OldVipList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Status: 实例状态。取值范围：
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
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100
        :type Limit: int
        :param _InstanceIdSet: 一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl
        :type InstanceIdSet: list of str
        :param _PayMode: 付费类型检索 1-包年包月，0-按量计费
        :type PayMode: int
        :param _VpcId: 实例所属VPC的唯一字符串ID，格式如：vpc-xxx，传空字符串(“”)则按照基础网络筛选。
        :type VpcId: str
        :param _SubnetId: 实例所属子网的唯一字符串ID，格式如： subnet-xxx，传空字符串(“”)则按照基础网络筛选。
        :type SubnetId: str
        :param _VipSet: 实例内网地址列表，格式如：172.1.0.12
        :type VipSet: list of str
        :param _InstanceNameSet: 实例名称列表，模糊查询
        :type InstanceNameSet: list of str
        :param _VersionSet: 实例版本代号列表，格式如：2008R2，2012SP3等
        :type VersionSet: list of str
        :param _Zone: 实例可用区，格式如：ap-guangzhou-2
        :type Zone: str
        :param _TagKeys: 实例标签列表
        :type TagKeys: list of str
        :param _SearchKey: 模糊查询关键字，支持实例id、实例名、内网ip
        :type SearchKey: str
        :param _UidSet: 实例唯一Uid列表
        :type UidSet: list of str
        :param _InstanceType: 实例类型 HA-高可用 RO-只读实例 SI-基础版 BI-商业智能服务
        :type InstanceType: str
        :param _PaginationType: 分页查询方式 offset-按照偏移量分页查询，pageNumber-按照页数分页查询，默认取值pageNumber
        :type PaginationType: str
        """
        self._ProjectId = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._InstanceIdSet = None
        self._PayMode = None
        self._VpcId = None
        self._SubnetId = None
        self._VipSet = None
        self._InstanceNameSet = None
        self._VersionSet = None
        self._Zone = None
        self._TagKeys = None
        self._SearchKey = None
        self._UidSet = None
        self._InstanceType = None
        self._PaginationType = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VipSet(self):
        return self._VipSet

    @VipSet.setter
    def VipSet(self, VipSet):
        self._VipSet = VipSet

    @property
    def InstanceNameSet(self):
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def VersionSet(self):
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def UidSet(self):
        return self._UidSet

    @UidSet.setter
    def UidSet(self, UidSet):
        self._UidSet = UidSet

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PaginationType(self):
        return self._PaginationType

    @PaginationType.setter
    def PaginationType(self, PaginationType):
        self._PaginationType = PaginationType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._PayMode = params.get("PayMode")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VipSet = params.get("VipSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._VersionSet = params.get("VersionSet")
        self._Zone = params.get("Zone")
        self._TagKeys = params.get("TagKeys")
        self._SearchKey = params.get("SearchKey")
        self._UidSet = params.get("UidSet")
        self._InstanceType = params.get("InstanceType")
        self._PaginationType = params.get("PaginationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例总数。分页返回的话，这个值指的是所有符合条件的实例的个数，而非当前根据Limit和Offset值返回的实例个数
        :type TotalCount: int
        :param _DBInstances: 实例列表
        :type DBInstances: list of DBInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBPrivilegeByAccountRequest(AbstractModel):
    """DescribeDBPrivilegeByAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _AccountName: 账号名称
        :type AccountName: str
        :param _DBName: 账号关联的数据库名称
        :type DBName: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        """
        self._InstanceId = None
        self._AccountName = None
        self._DBName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._DBName = params.get("DBName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPrivilegeByAccountResponse(AbstractModel):
    """DescribeDBPrivilegeByAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总库数量
        :type TotalCount: int
        :param _DBList: 数据库权限列表
        :type DBList: list of DBPrivilege
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBRestoreTimeRequest(AbstractModel):
    """DescribeDBRestoreTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 原实例ID
        :type InstanceId: str
        :param _TargetInstanceId: 回档的目标实例ID，不填则回档到原实例ID
        :type TargetInstanceId: str
        :param _Time: 按时间点查询可回档数据库，时间格式 YYYY-MM-DD HH:MM:SS。BackupId，Time二选一，不能同时为空
        :type Time: str
        :param _BackupId: 按备份集ID查询可回档数据库，可通过DescribeBackups接口获取。BackupId，Time二选一不能同时为空
        :type BackupId: int
        :param _DBName: 数据库名称
        :type DBName: str
        """
        self._InstanceId = None
        self._TargetInstanceId = None
        self._Time = None
        self._BackupId = None
        self._DBName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetInstanceId(self):
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._Time = params.get("Time")
        self._BackupId = params.get("BackupId")
        self._DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBRestoreTimeResponse(AbstractModel):
    """DescribeDBRestoreTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可回档数据库总数量
        :type TotalCount: int
        :param _Details: 可回档数据库列表
        :type Details: list of DBRenameRes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DBRenameRes()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-c1nl9rpv或者mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupSet: 安全组详情。
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBsNormalRequest(AbstractModel):
    """DescribeDBsNormal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-7vfv3rk3
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeDBsNormalResponse(AbstractModel):
    """DescribeDBsNormal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表示当前实例下的数据库总个数
        :type TotalCount: int
        :param _DBList: 返回数据库的详细配置信息，例如：数据库是否开启CDC、CT等
        :type DBList: list of DbNormalDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 实例ID
        :type InstanceIdSet: list of str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _Name: 数据库名称
        :type Name: str
        :param _OrderByType: 排序规则（desc-降序，asc-升序），默认desc
        :type OrderByType: str
        :param _Encryption: 是否已开启TDE加密，enable-已加密，disable-未加密
        :type Encryption: str
        """
        self._InstanceIdSet = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderByType = None
        self._Encryption = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._OrderByType = params.get("OrderByType")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据库数量
        :type TotalCount: int
        :param _DBInstances: 实例数据库列表
        :type DBInstances: list of InstanceDBDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseNamesRequest(AbstractModel):
    """DescribeDatabaseNames请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param _AccountName: 账户名称
        :type AccountName: str
        """
        self._InstanceId = None
        self._AccountName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseNamesResponse(AbstractModel):
    """DescribeDatabaseNames返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 账户关联的数据库总数
        :type TotalCount: int
        :param _DatabaseNameSet: 数据库名称集合
        :type DatabaseNameSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DatabaseNameSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DatabaseNameSet(self):
        return self._DatabaseNameSet

    @DatabaseNameSet.setter
    def DatabaseNameSet(self, DatabaseNameSet):
        self._DatabaseNameSet = DatabaseNameSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._DatabaseNameSet = params.get("DatabaseNameSet")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesNormalRequest(AbstractModel):
    """DescribeDatabasesNormal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-7vfv3rk3
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeDatabasesNormalResponse(AbstractModel):
    """DescribeDatabasesNormal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 表示当前实例下的数据库总个数
        :type TotalCount: int
        :param _DBList: 返回数据库的详细配置信息，例如：数据库是否开启CDC、CT等
        :type DBList: list of DbNormalDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 实例ID
        :type InstanceIdSet: list of str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _Name: 数据库名称
        :type Name: str
        :param _OrderByType: 排序规则（desc-降序，asc-升序），默认desc
        :type OrderByType: str
        :param _Encryption: 是否已开启TDE加密，enable-已加密，disable-未加密
        :type Encryption: str
        """
        self._InstanceIdSet = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderByType = None
        self._Encryption = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._OrderByType = params.get("OrderByType")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据库数量
        :type TotalCount: int
        :param _DBInstances: 实例数据库列表
        :type DBInstances: list of InstanceDBDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowStatusRequest(AbstractModel):
    """DescribeFlowStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 流程状态，0：成功，1：失败，2：运行中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeHASwitchLogRequest(AbstractModel):
    """DescribeHASwitchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param _EndTime: 结束时间(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param _SwitchType: 切换模式 0-系统自动切换，1-手动切换，不填默认查全部。
        :type SwitchType: int
        :param _Limit: 分页，页大小
        :type Limit: int
        :param _Offset: 分页,页数
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SwitchType = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SwitchType(self):
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SwitchType = params.get("SwitchType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHASwitchLogResponse(AbstractModel):
    """DescribeHASwitchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 日志总数量
        :type TotalCount: int
        :param _SwitchLog: 主备切换日志
        :type SwitchLog: list of SwitchLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SwitchLog = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SwitchLog(self):
        return self._SwitchLog

    @SwitchLog.setter
    def SwitchLog(self, SwitchLog):
        self._SwitchLog = SwitchLog

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SwitchLog") is not None:
            self._SwitchLog = []
            for item in params.get("SwitchLog"):
                obj = SwitchLog()
                obj._deserialize(item)
                self._SwitchLog.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIncrementalMigrationRequest(AbstractModel):
    """DescribeIncrementalMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupFileName: 备份文件名称
        :type BackupFileName: str
        :param _StatusSet: 导入任务状态集合
        :type StatusSet: list of int
        :param _Limit: 分页，页大小，默认值：100
        :type Limit: int
        :param _Offset: 分页，页数，默认值：0
        :type Offset: int
        :param _OrderBy: 排序字段，name；createTime；startTime；endTime，默认按照createTime递增排序。
        :type OrderBy: str
        :param _OrderByType: 排序方式，desc-递减排序，asc-递增排序。默认按照asc排序，且在OrderBy为有效值时，本参数有效
        :type OrderByType: str
        :param _IncrementalMigrationId: 增量备份导入任务ID，由CreateIncrementalMigration接口返回
        :type IncrementalMigrationId: str
        """
        self._BackupMigrationId = None
        self._InstanceId = None
        self._BackupFileName = None
        self._StatusSet = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._IncrementalMigrationId = None

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupFileName(self):
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._InstanceId = params.get("InstanceId")
        self._BackupFileName = params.get("BackupFileName")
        self._StatusSet = params.get("StatusSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementalMigrationResponse(AbstractModel):
    """DescribeIncrementalMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 增量导入任务总数
        :type TotalCount: int
        :param _IncrementalMigrationSet: 增量导入任务集合
        :type IncrementalMigrationSet: list of Migration
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IncrementalMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IncrementalMigrationSet(self):
        return self._IncrementalMigrationSet

    @IncrementalMigrationSet.setter
    def IncrementalMigrationSet(self, IncrementalMigrationSet):
        self._IncrementalMigrationSet = IncrementalMigrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IncrementalMigrationSet") is not None:
            self._IncrementalMigrationSet = []
            for item in params.get("IncrementalMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._IncrementalMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInquiryPriceParameterRequest(AbstractModel):
    """DescribeInquiryPriceParameter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param _Memory: 内存大小，单位：GB
        :type Memory: int
        :param _Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param _InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-单节点型,cvmHA-新版高可用,cvmRO-新版只读
        :type InstanceType: str
        :param _InstanceChargeType: 计费类型，取值支持 PREPAID，POSTPAID。
        :type InstanceChargeType: str
        :param _Cpu: 预购买实例的CPU核心数
        :type Cpu: int
        :param _Period: 购买时长，单位：月。取值为1到48，默认为1
        :type Period: int
        :param _GoodsNum: 一次性购买的实例数量。取值1-100，默认取值为1
        :type GoodsNum: int
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _MachineType: 购买实例的宿主机类型，PM-物理机, CLOUD_PREMIUM-云服务器高性能云盘，CLOUD_SSD-云服务器SSD云盘,
CLOUD_HSSD-云服务器加强型SSD云盘，CLOUD_TSSD-云服务器极速型SSD云盘，CLOUD_BSSD-云服务器通用型SSD云盘
        :type MachineType: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._InstanceChargeType = None
        self._Cpu = None
        self._Period = None
        self._GoodsNum = None
        self._DBVersion = None
        self._MachineType = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Cpu = params.get("Cpu")
        self._Period = params.get("Period")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInquiryPriceParameterResponse(AbstractModel):
    """DescribeInquiryPriceParameter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Parameter: 计费参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameter: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Parameter = None
        self._RequestId = None

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Parameter = params.get("Parameter")
        self._RequestId = params.get("RequestId")


class DescribeInstanceByOrdersRequest(AbstractModel):
    """DescribeInstanceByOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单号集合
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceByOrdersResponse(AbstractModel):
    """DescribeInstanceByOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealInstance: 资源ID集合
        :type DealInstance: list of DealInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealInstance = None
        self._RequestId = None

    @property
    def DealInstance(self):
        return self._DealInstance

    @DealInstance.setter
    def DealInstance(self, DealInstance):
        self._DealInstance = DealInstance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DealInstance") is not None:
            self._DealInstance = []
            for item in params.get("DealInstance"):
                obj = DealInstance()
                obj._deserialize(item)
                self._DealInstance.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：mssql-dj5i29c5n，与云数据库控制台页面中显示的实例 ID 相同，可使用 DescribeDBInstances 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _Offset: 分页，页数，默认0
        :type Offset: int
        :param _Limit: 分页，页大小，默认20，最大不超过100
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录数
        :type TotalCount: int
        :param _Items: 参数修改记录
        :type Items: list of ParamRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：mssql-dj5i29c5n，与云数据库控制台页面中显示的实例 ID 相同，可使用 DescribeDBInstances 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例的参数总数
        :type TotalCount: int
        :param _Items: 参数详情
        :type Items: list of ParameterDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTasksRequest(AbstractModel):
    """DescribeInstanceTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Limit: 分页大小
        :type Limit: int
        :param _Status: 异步任务状态 1-运行中，2-运行成功，3-运行失败
        :type Status: int
        :param _Offset: 分页偏移量
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Status = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTasksResponse(AbstractModel):
    """DescribeInstanceTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 异步任务总条数
        :type TotalCount: int
        :param _InstanceTaskSet: 异步任务信息数组
        :type InstanceTaskSet: list of InstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTaskSet(self):
        return self._InstanceTaskSet

    @InstanceTaskSet.setter
    def InstanceTaskSet(self, InstanceTaskSet):
        self._InstanceTaskSet = InstanceTaskSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceTaskSet") is not None:
            self._InstanceTaskSet = []
            for item in params.get("InstanceTaskSet"):
                obj = InstanceTask()
                obj._deserialize(item)
                self._InstanceTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTradeParameterRequest(AbstractModel):
    """DescribeInstanceTradeParameter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取
        :type Zone: str
        :param _Cpu: 实例核心数
        :type Cpu: int
        :param _Memory: 实例内存大小，单位GB
        :type Memory: int
        :param _Storage: 实例磁盘大小，单位GB
        :type Storage: int
        :param _InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-单节点型,BI-商业智能服务,cvmHA-新版高可用,cvmRO-新版只读
        :type InstanceType: str
        :param _MachineType: 购买实例的宿主机磁盘类型,CLOUD_HSSD-云服务器加强型SSD云盘，CLOUD_TSSD-云服务器极速型SSD云盘，CLOUD_BSSD-云服务器通用型SSD云盘
        :type MachineType: str
        :param _InstanceChargeType: 付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。
        :type InstanceChargeType: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsNum: 本次购买几个实例，默认值为1。取值不超过10
        :type GoodsNum: int
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _SubnetId: VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置
        :type SubnetId: str
        :param _VpcId: VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置
        :type VpcId: str
        :param _Period: 购买实例周期，默认取值为1，表示一个月。取值不超过48
        :type Period: int
        :param _SecurityGroupList: 安全组列表，填写形如sg-xxx的安全组ID
        :type SecurityGroupList: list of str
        :param _AutoRenewFlag: 自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。
        :type AutoRenewFlag: int
        :param _Weekly: 可维护时间窗配置，以周为单位，表示周几允许维护，1-7分别代表周一到周末
        :type Weekly: list of int
        :param _StartTime: 可维护时间窗配置，每天可维护的开始时间
        :type StartTime: str
        :param _Span: 可维护时间窗配置，持续时间，单位：小时
        :type Span: int
        :param _MultiZones: 是否跨可用区部署，默认值为false
        :type MultiZones: bool
        :param _ResourceTags: 新建实例绑定的标签集合
        :type ResourceTags: list of ResourceTag
        :param _TimeZone: 系统时区，默认：China Standard Time
        :type TimeZone: str
        :param _Collation: 系统字符集排序规则，默认：Chinese_PRC_CI_AS
        :type Collation: str
        """
        self._Zone = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._DBVersion = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoRenewFlag = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._MultiZones = None
        self._ResourceTags = None
        self._TimeZone = None
        self._Collation = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def MultiZones(self):
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Collation(self):
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._TimeZone = params.get("TimeZone")
        self._Collation = params.get("Collation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTradeParameterResponse(AbstractModel):
    """DescribeInstanceTradeParameter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Parameter: 计费参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameter: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Parameter = None
        self._RequestId = None

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Parameter = params.get("Parameter")
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceSpanRequest(AbstractModel):
    """DescribeMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeMaintenanceSpanResponse(AbstractModel):
    """DescribeMaintenanceSpan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Weekly: 以周为单位，表示周几允许维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日。
        :type Weekly: list of int
        :param _StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始。
        :type StartTime: str
        :param _Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时。
        :type Span: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._RequestId = None

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDatabasesRequest(AbstractModel):
    """DescribeMigrationDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 迁移源实例的ID，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param _UserName: 迁移源实例用户名
        :type UserName: str
        :param _Password: 迁移源实例密码
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDatabasesResponse(AbstractModel):
    """DescribeMigrationDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Amount: 数据库数量
        :type Amount: int
        :param _MigrateDBSet: 数据库名称数组
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrateDBSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Amount = None
        self._MigrateDBSet = None
        self._RequestId = None

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def MigrateDBSet(self):
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Amount = params.get("Amount")
        self._MigrateDBSet = params.get("MigrateDBSet")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        :param _MigrateName: 迁移任务名称
        :type MigrateName: str
        :param _AppId: 迁移任务所属的用户ID
        :type AppId: int
        :param _Region: 迁移任务所属的地域
        :type Region: str
        :param _SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param _CreateTime: 迁移任务的创建时间
        :type CreateTime: str
        :param _StartTime: 迁移任务的开始时间
        :type StartTime: str
        :param _EndTime: 迁移任务的结束时间
        :type EndTime: str
        :param _Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功）
        :type Status: int
        :param _Progress: 迁移任务当前进度
        :type Progress: int
        :param _MigrateType: 迁移类型（1:结构迁移 2:数据迁移 3:增量同步）
        :type MigrateType: int
        :param _Source: 迁移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: 迁移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用。
        :type MigrateDBSet: list of MigrateDB
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MigrateId = None
        self._MigrateName = None
        self._AppId = None
        self._Region = None
        self._SourceType = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Progress = None
        self._MigrateType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None
        self._RequestId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateType(self):
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._SourceType = params.get("SourceType")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._MigrateType = params.get("MigrateType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationsRequest(AbstractModel):
    """DescribeMigrations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StatusSet: 状态集合。只要符合集合中某一状态的迁移任务，就会查出来
        :type StatusSet: list of int
        :param _MigrateName: 迁移任务的名称，模糊匹配
        :type MigrateName: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为100
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _OrderBy: 查询结果按照关键字排序，可选值为name、createTime、startTime，endTime，status
        :type OrderBy: str
        :param _OrderByType: 排序方式，可选值为desc、asc
        :type OrderByType: str
        """
        self._StatusSet = None
        self._MigrateName = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def StatusSet(self):
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def MigrateName(self):
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._StatusSet = params.get("StatusSet")
        self._MigrateName = params.get("MigrateName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总数
        :type TotalCount: int
        :param _MigrateTaskSet: 查询结果的列表
        :type MigrateTaskSet: list of MigrateTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrateTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrateTaskSet(self):
        return self._MigrateTaskSet

    @MigrateTaskSet.setter
    def MigrateTaskSet(self, MigrateTaskSet):
        self._MigrateTaskSet = MigrateTaskSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MigrateTaskSet") is not None:
            self._MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self._MigrateTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单数组。发货时会返回订单名字，利用该订单名字调用DescribeOrders接口查询发货情况
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deals: 订单信息数组
        :type Deals: list of DealInfo
        :param _TotalCount: 返回多少个订单的信息
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deals = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Deals(self):
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区英文ID，形如ap-guangzhou-1
        :type Zone: str
        :param _InstanceType: 购买实例的类型 HA-本地盘高可用(包括双机高可用，alwaysOn集群)，RO-本地盘只读副本，SI-云盘版单节点,BI-商业智能服务，cvmHA-云盘版高可用，cvmRO-云盘版只读副本
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: 规格信息数组
        :type SpecInfoList: list of SpecInfo
        :param _TotalCount: 返回总共多少条数据
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProductSpecRequest(AbstractModel):
    """DescribeProductSpec请求参数结构体

    """


class DescribeProductSpecResponse(AbstractModel):
    """DescribeProductSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 配置地域分的个数
        :type TotalCount: int
        :param _SpecInfoList: 规格信息数组
        :type SpecInfoList: list of ProductSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SpecInfoList(self):
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = ProductSpec()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID，可通过控制台项目管理中查看
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupSet: 安全组详情。
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublishSubscribeRequest(AbstractModel):
    """DescribePublishSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _PubOrSubInstanceId: 订阅/发布实例ID，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例ID做筛选；当InstanceId为订阅实例时，本字段按照发布实例ID做筛选；
        :type PubOrSubInstanceId: str
        :param _PubOrSubInstanceIp: 订阅/发布实例内网IP，与InstanceId是发布实例还是订阅实例有关；当InstanceId为发布实例时，本字段按照订阅实例内网IP做筛选；当InstanceId为订阅实例时，本字段按照发布实例内网IP做筛选；
        :type PubOrSubInstanceIp: str
        :param _PublishSubscribeId: 订阅发布ID，用于筛选
        :type PublishSubscribeId: int
        :param _PublishSubscribeName: 订阅发布名字，用于筛选
        :type PublishSubscribeName: str
        :param _PublishDBName: 发布库名字，用于筛选
        :type PublishDBName: str
        :param _SubscribeDBName: 订阅库名字，用于筛选
        :type SubscribeDBName: str
        :param _Offset: 分页，页数
        :type Offset: int
        :param _Limit: 分页，页大小
        :type Limit: int
        """
        self._InstanceId = None
        self._PubOrSubInstanceId = None
        self._PubOrSubInstanceIp = None
        self._PublishSubscribeId = None
        self._PublishSubscribeName = None
        self._PublishDBName = None
        self._SubscribeDBName = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PubOrSubInstanceId(self):
        return self._PubOrSubInstanceId

    @PubOrSubInstanceId.setter
    def PubOrSubInstanceId(self, PubOrSubInstanceId):
        self._PubOrSubInstanceId = PubOrSubInstanceId

    @property
    def PubOrSubInstanceIp(self):
        return self._PubOrSubInstanceIp

    @PubOrSubInstanceIp.setter
    def PubOrSubInstanceIp(self, PubOrSubInstanceIp):
        self._PubOrSubInstanceIp = PubOrSubInstanceIp

    @property
    def PublishSubscribeId(self):
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def PublishSubscribeName(self):
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName

    @property
    def PublishDBName(self):
        return self._PublishDBName

    @PublishDBName.setter
    def PublishDBName(self, PublishDBName):
        self._PublishDBName = PublishDBName

    @property
    def SubscribeDBName(self):
        return self._SubscribeDBName

    @SubscribeDBName.setter
    def SubscribeDBName(self, SubscribeDBName):
        self._SubscribeDBName = SubscribeDBName

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PubOrSubInstanceId = params.get("PubOrSubInstanceId")
        self._PubOrSubInstanceIp = params.get("PubOrSubInstanceIp")
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        self._PublishDBName = params.get("PublishDBName")
        self._SubscribeDBName = params.get("SubscribeDBName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishSubscribeResponse(AbstractModel):
    """DescribePublishSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PublishSubscribeSet: 发布订阅列表
        :type PublishSubscribeSet: list of PublishSubscribe
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PublishSubscribeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PublishSubscribeSet(self):
        return self._PublishSubscribeSet

    @PublishSubscribeSet.setter
    def PublishSubscribeSet(self, PublishSubscribeSet):
        self._PublishSubscribeSet = PublishSubscribeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PublishSubscribeSet") is not None:
            self._PublishSubscribeSet = []
            for item in params.get("PublishSubscribeSet"):
                obj = PublishSubscribe()
                obj._deserialize(item)
                self._PublishSubscribeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupAutoWeightRequest(AbstractModel):
    """DescribeReadOnlyGroupAutoWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _ReadOnlyGroupId: 只读组ID，格式如：mssqlro-3l3fgqn7
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupAutoWeightResponse(AbstractModel):
    """DescribeReadOnlyGroupAutoWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID，格式如：mssqlro-3l3fgqn7
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param _RegionId: 只读组的地域ID，与主实例相同
        :type RegionId: str
        :param _ZoneId: 只读组的可用区，与主实例相同
        :type ZoneId: str
        :param _IsOfflineDelay: 是否启动超时剔除功能，1-开启，0-不开启
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值(秒)
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 启动超时剔除功能后，至少只读组保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param _Vip: 只读组vip
        :type Vip: str
        :param _Vport: 只读组vport
        :type Vport: int
        :param _VpcId: 只读组在私有网络ID
        :type VpcId: str
        :param _SubnetId: 只读组在私有网络子网ID
        :type SubnetId: str
        :param _ReadOnlyInstanceSet: 只读实例副本集合
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _Status: 只读组状态: 1-申请成功运行中，5-申请中
        :type Status: int
        :param _MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._ReadOnlyInstanceSet = None
        self._Status = None
        self._MasterInstanceId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReadOnlyInstanceSet(self):
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupByReadOnlyInstanceRequest(AbstractModel):
    """DescribeReadOnlyGroupByReadOnlyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeReadOnlyGroupByReadOnlyInstanceResponse(AbstractModel):
    """DescribeReadOnlyGroupByReadOnlyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param _RegionId: 只读组的地域ID
        :type RegionId: str
        :param _ZoneId: 只读组的可用区ID
        :type ZoneId: str
        :param _IsOfflineDelay: 是否启动超时剔除功能 ,0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，单位是秒
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param _Vip: 只读组vip
        :type Vip: str
        :param _Vport: 只读组vport
        :type Vport: int
        :param _VpcId: 只读组在私有网络ID
        :type VpcId: str
        :param _SubnetId: 只读组在私有网络子网ID
        :type SubnetId: str
        :param _MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param _MasterRegionId: 主实例的地域ID
        :type MasterRegionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._MasterInstanceId = None
        self._MasterRegionId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def MasterRegionId(self):
        return self._MasterRegionId

    @MasterRegionId.setter
    def MasterRegionId(self, MasterRegionId):
        self._MasterRegionId = MasterRegionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._MasterRegionId = params.get("MasterRegionId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupDetailsRequest(AbstractModel):
    """DescribeReadOnlyGroupDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _ReadOnlyGroupId: 只读组ID，格式如：mssqlrg-3l3fgqn7
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupDetailsResponse(AbstractModel):
    """DescribeReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param _RegionId: 只读组的地域ID，与主实例相同
        :type RegionId: str
        :param _ZoneId: 只读组的可用区ID，与主实例相同
        :type ZoneId: str
        :param _IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 启动超时剔除功能后，至少只读组保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param _Vip: 只读组vip
        :type Vip: str
        :param _Vport: 只读组vport
        :type Vport: int
        :param _VpcId: 只读组私有网络ID
        :type VpcId: str
        :param _SubnetId: 只读组私有网络子网ID
        :type SubnetId: str
        :param _ReadOnlyInstanceSet: 只读实例副本集合
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _Status: 只读组状态: 1-申请成功运行中，5-申请中
        :type Status: int
        :param _MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._ReadOnlyInstanceSet = None
        self._Status = None
        self._MasterInstanceId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReadOnlyInstanceSet(self):
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupListRequest(AbstractModel):
    """DescribeReadOnlyGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeReadOnlyGroupListResponse(AbstractModel):
    """DescribeReadOnlyGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupSet: 只读组列表
        :type ReadOnlyGroupSet: list of ReadOnlyGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReadOnlyGroupSet = None
        self._RequestId = None

    @property
    def ReadOnlyGroupSet(self):
        return self._ReadOnlyGroupSet

    @ReadOnlyGroupSet.setter
    def ReadOnlyGroupSet(self, ReadOnlyGroupSet):
        self._ReadOnlyGroupSet = ReadOnlyGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupSet") is not None:
            self._ReadOnlyGroupSet = []
            for item in params.get("ReadOnlyGroupSet"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self._ReadOnlyGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回地域信息总的条目
        :type TotalCount: int
        :param _RegionSet: 地域信息数组
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegularBackupPlanRequest(AbstractModel):
    """DescribeRegularBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RegularBackupSaveDays: 定期备份保留天数 [90 - 3650]天，默认365天
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: 定期备份策略 years-每年，quarters-每季度，months-每月，默认months
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: 定期备份保留个数，默认1个
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: 定期备份开始日期，格式-YYYY-MM-DD 默认当前日期
        :type RegularBackupStartTime: str
        :param _BackupCycle: 常规备份周期
        :type BackupCycle: list of int non-negative
        """
        self._InstanceId = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None
        self._BackupCycle = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegularBackupSaveDays(self):
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime

    @property
    def BackupCycle(self):
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        self._BackupCycle = params.get("BackupCycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegularBackupPlanResponse(AbstractModel):
    """DescribeRegularBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SaveModePeriod: 常规备份计划
        :type SaveModePeriod: list of str
        :param _SaveModeRegular: 定期备份计划
        :type SaveModeRegular: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SaveModePeriod = None
        self._SaveModeRegular = None
        self._RequestId = None

    @property
    def SaveModePeriod(self):
        return self._SaveModePeriod

    @SaveModePeriod.setter
    def SaveModePeriod(self, SaveModePeriod):
        self._SaveModePeriod = SaveModePeriod

    @property
    def SaveModeRegular(self):
        return self._SaveModeRegular

    @SaveModeRegular.setter
    def SaveModeRegular(self, SaveModeRegular):
        self._SaveModeRegular = SaveModeRegular

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SaveModePeriod = params.get("SaveModePeriod")
        self._SaveModeRegular = params.get("SaveModeRegular")
        self._RequestId = params.get("RequestId")


class DescribeRestoreTaskRequest(AbstractModel):
    """DescribeRestoreTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 源实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _RestoreType: 回档方式，0-按照时间点回档，1-按照备份集回档
        :type RestoreType: int
        :param _TargetRegion: 回档的目标实例所在地域
        :type TargetRegion: str
        :param _TargetType: 回档到目标实例的类型，0-当前实例，1-已有实例，2-全新实例
        :type TargetType: int
        :param _Status: 回档状态，0-初始化，1-运行中，2-成功，3-失败
        :type Status: int
        :param _Offset: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Offset: int
        :param _Limit: 分页返回，页编号，默认值为第0页
        :type Limit: int
        :param _OrderBy: 排序字段，restoreTime-回档时间，startTime-任务开始时间，endTime-任务结束时间，默认按照任务开始时间降序
        :type OrderBy: str
        :param _OrderByType: 排序规则（desc-降序，asc-升序），默认desc
        :type OrderByType: str
        :param _FlowId: 回档异步任务ID
        :type FlowId: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._RestoreType = None
        self._TargetRegion = None
        self._TargetType = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None
        self._FlowId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RestoreType(self):
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        self._RestoreType = RestoreType

    @property
    def TargetRegion(self):
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RestoreType = params.get("RestoreType")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetType = params.get("TargetType")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTaskResponse(AbstractModel):
    """DescribeRestoreTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 回档任务总数量
        :type TotalCount: int
        :param _Tasks: 回档任务记录列表
        :type Tasks: list of RestoreTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTimeRangeRequest(AbstractModel):
    """DescribeRestoreTimeRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _TargetInstanceId: 回档的目标实例ID，不填默认回档到原实例
        :type TargetInstanceId: str
        """
        self._InstanceId = None
        self._TargetInstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetInstanceId(self):
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTimeRangeResponse(AbstractModel):
    """DescribeRestoreTimeRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 按照时间点可回档的最小时间
        :type MinTime: str
        :param _MaxTime: 按照时间点可回档的最大时间
        :type MaxTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._RequestId = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._RequestId = params.get("RequestId")


class DescribeRollbackTimeRequest(AbstractModel):
    """DescribeRollbackTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DBs: 需要查询的数据库列表
        :type DBs: list of str
        """
        self._InstanceId = None
        self._DBs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBs = params.get("DBs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: 数据库可回档实例信息
        :type Details: list of DbRollbackTimeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowlogsRequest(AbstractModel):
    """DescribeSlowlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        :param _StartTime: 开始时间(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param _EndTime: 结束时间(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param _Limit: 分页返回，每页返回的数目，取值为1-100，默认值为20
        :type Limit: int
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Slowlogs: 慢查询日志信息列表
        :type Slowlogs: list of SlowlogInfo
        :param _SlowLogs: 慢查询日志信息列表
        :type SlowLogs: list of SlowLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Slowlogs = None
        self._SlowLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Slowlogs(self):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        return self._Slowlogs

    @Slowlogs.setter
    def Slowlogs(self, Slowlogs):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        self._Slowlogs = Slowlogs

    @property
    def SlowLogs(self):
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Slowlogs") is not None:
            self._Slowlogs = []
            for item in params.get("Slowlogs"):
                obj = SlowlogInfo()
                obj._deserialize(item)
                self._Slowlogs.append(obj)
        if params.get("SlowLogs") is not None:
            self._SlowLogs = []
            for item in params.get("SlowLogs"):
                obj = SlowLog()
                obj._deserialize(item)
                self._SlowLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSpecSellStatusRequest(AbstractModel):
    """DescribeSpecSellStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区英文ID，形如ap-guangzhou-3
        :type Zone: str
        :param _SpecIdSet: 实例规格ID，可通过DescribeProductConfig接口获取。
        :type SpecIdSet: list of int non-negative
        :param _DBVersion: 数据库版本信息，可通过DescribeProductConfig接口获取。
        :type DBVersion: str
        :param _Pid: 产品ID，可通过DescribeProductConfig接口获取。
        :type Pid: int
        :param _PayMode: 付费模式，POST-按量计费 PRE-包年包月
        :type PayMode: str
        :param _Currency: 付费模式，CNY-人民币 USD-美元
        :type Currency: str
        """
        self._Zone = None
        self._SpecIdSet = None
        self._DBVersion = None
        self._Pid = None
        self._PayMode = None
        self._Currency = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecIdSet(self):
        return self._SpecIdSet

    @SpecIdSet.setter
    def SpecIdSet(self, SpecIdSet):
        self._SpecIdSet = SpecIdSet

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecIdSet = params.get("SpecIdSet")
        self._DBVersion = params.get("DBVersion")
        self._Pid = params.get("Pid")
        self._PayMode = params.get("PayMode")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecSellStatusResponse(AbstractModel):
    """DescribeSpecSellStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DescribeSpecSellStatusSet: 规格在不同地域状态集合
        :type DescribeSpecSellStatusSet: list of SpecSellStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DescribeSpecSellStatusSet = None
        self._RequestId = None

    @property
    def DescribeSpecSellStatusSet(self):
        return self._DescribeSpecSellStatusSet

    @DescribeSpecSellStatusSet.setter
    def DescribeSpecSellStatusSet(self, DescribeSpecSellStatusSet):
        self._DescribeSpecSellStatusSet = DescribeSpecSellStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeSpecSellStatusSet") is not None:
            self._DescribeSpecSellStatusSet = []
            for item in params.get("DescribeSpecSellStatusSet"):
                obj = SpecSellStatus()
                obj._deserialize(item)
                self._DescribeSpecSellStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUpgradeInstanceCheckRequest(AbstractModel):
    """DescribeUpgradeInstanceCheck请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Cpu: 实例变配后的CPU核心数，不填则不修改
        :type Cpu: int
        :param _Memory: 实例变配后内存大小，单位GB，不填则不修改
        :type Memory: int
        :param _Storage: 实例变配后磁盘大小，单位GB，不填则不修改
        :type Storage: int
        :param _DBVersion: 实例版本，不填则不修改
        :type DBVersion: str
        :param _HAType: 实例变配后的类型，可选值：CLUSTER-集群，不填则不修改
        :type HAType: str
        :param _MultiZones: 实例变配后的跨可用区类型，可选值： SameZones-修改为同可用区 MultiZones-修改为跨可用区，不填则不修改
        :type MultiZones: str
        """
        self._InstanceId = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._DBVersion = None
        self._HAType = None
        self._MultiZones = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def HAType(self):
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._DBVersion = params.get("DBVersion")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpgradeInstanceCheckResponse(AbstractModel):
    """DescribeUpgradeInstanceCheck返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAffect: 本变配是否对实例有影响，0-没有影响 1-有影响
        :type IsAffect: int
        :param _Passed: 本变配是否可以执行 0-不通过，不能变配 1-通过，可以变配
        :type Passed: int
        :param _ModifyMode: 本变配是升配还是降配，down-降配 up-升配
        :type ModifyMode: str
        :param _CheckItems: 检查项列表
        :type CheckItems: list of CheckItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsAffect = None
        self._Passed = None
        self._ModifyMode = None
        self._CheckItems = None
        self._RequestId = None

    @property
    def IsAffect(self):
        return self._IsAffect

    @IsAffect.setter
    def IsAffect(self, IsAffect):
        self._IsAffect = IsAffect

    @property
    def Passed(self):
        return self._Passed

    @Passed.setter
    def Passed(self, Passed):
        self._Passed = Passed

    @property
    def ModifyMode(self):
        return self._ModifyMode

    @ModifyMode.setter
    def ModifyMode(self, ModifyMode):
        self._ModifyMode = ModifyMode

    @property
    def CheckItems(self):
        return self._CheckItems

    @CheckItems.setter
    def CheckItems(self, CheckItems):
        self._CheckItems = CheckItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsAffect = params.get("IsAffect")
        self._Passed = params.get("Passed")
        self._ModifyMode = params.get("ModifyMode")
        if params.get("CheckItems") is not None:
            self._CheckItems = []
            for item in params.get("CheckItems"):
                obj = CheckItem()
                obj._deserialize(item)
                self._CheckItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUploadBackupInfoRequest(AbstractModel):
    """DescribeUploadBackupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadBackupInfoResponse(AbstractModel):
    """DescribeUploadBackupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketName: 存储桶名称
        :type BucketName: str
        :param _Region: 存储桶地域信息
        :type Region: str
        :param _Path: 存储路径
        :type Path: str
        :param _TmpSecretId: 临时密钥ID
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Key
        :type TmpSecretKey: str
        :param _XCosSecurityToken: 临时密钥Token
        :type XCosSecurityToken: str
        :param _StartTime: 临时密钥开始时间
        :type StartTime: str
        :param _ExpiredTime: 临时密钥到期时间
        :type ExpiredTime: str
        :param _CosSecurityToken: 临时密钥Token
        :type CosSecurityToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BucketName = None
        self._Region = None
        self._Path = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._XCosSecurityToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._CosSecurityToken = None
        self._RequestId = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def XCosSecurityToken(self):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        return self._XCosSecurityToken

    @XCosSecurityToken.setter
    def XCosSecurityToken(self, XCosSecurityToken):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        self._XCosSecurityToken = XCosSecurityToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CosSecurityToken(self):
        return self._CosSecurityToken

    @CosSecurityToken.setter
    def CosSecurityToken(self, CosSecurityToken):
        self._CosSecurityToken = CosSecurityToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._XCosSecurityToken = params.get("XCosSecurityToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CosSecurityToken = params.get("CosSecurityToken")
        self._RequestId = params.get("RequestId")


class DescribeUploadIncrementalInfoRequest(AbstractModel):
    """DescribeUploadIncrementalInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: 增量导入任务ID
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadIncrementalInfoResponse(AbstractModel):
    """DescribeUploadIncrementalInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketName: 存储桶名称
        :type BucketName: str
        :param _Region: 存储桶地域信息
        :type Region: str
        :param _Path: 存储路径
        :type Path: str
        :param _TmpSecretId: 临时密钥ID
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥Key
        :type TmpSecretKey: str
        :param _XCosSecurityToken: 临时密钥Token
        :type XCosSecurityToken: str
        :param _StartTime: 临时密钥开始时间
        :type StartTime: str
        :param _ExpiredTime: 临时密钥到期时间
        :type ExpiredTime: str
        :param _CosSecurityToken: 临时密钥Token
        :type CosSecurityToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BucketName = None
        self._Region = None
        self._Path = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._XCosSecurityToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._CosSecurityToken = None
        self._RequestId = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def XCosSecurityToken(self):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        return self._XCosSecurityToken

    @XCosSecurityToken.setter
    def XCosSecurityToken(self, XCosSecurityToken):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        self._XCosSecurityToken = XCosSecurityToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CosSecurityToken(self):
        return self._CosSecurityToken

    @CosSecurityToken.setter
    def CosSecurityToken(self, CosSecurityToken):
        self._CosSecurityToken = CosSecurityToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._XCosSecurityToken = params.get("XCosSecurityToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CosSecurityToken = params.get("CosSecurityToken")
        self._RequestId = params.get("RequestId")


class DescribeXEventsRequest(AbstractModel):
    """DescribeXEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _EventType: 事件类型，slow-慢SQL事件，blocked-阻塞事件，deadlock-死锁事件
        :type EventType: str
        :param _StartTime: 扩展文件生成开始时间(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param _EndTime: 扩展文件生成结束时间(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param _Offset: 分页返回，页编号，默认值为第0页
        :type Offset: int
        :param _Limit: 分页返回，每页返回的数目，取值为1~100，默认值为20
        :type Limit: int
        """
        self._InstanceId = None
        self._EventType = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventType = params.get("EventType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeXEventsResponse(AbstractModel):
    """DescribeXEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 扩展事件列表
        :type Events: list of Events
        :param _TotalCount: 扩展事件总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Events()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回多少个可用区信息
        :type TotalCount: int
        :param _ZoneSet: 可用区数组
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _InstanceIdSet: 实例ID 列表，一个或者多个实例ID组成的数组。多个实例必须是同一个地域，同一个可用区，同一个项目下的。
        :type InstanceIdSet: list of str
        """
        self._SecurityGroupId = None
        self._InstanceIdSet = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DrReadableInfo(AbstractModel):
    """备机只读信息

    """

    def __init__(self):
        r"""
        :param _SlaveStatus: 备机状态，enable-运行中，disable-不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveStatus: str
        :param _ReadableStatus: 备机可读状态，enable-已开启，disable-已关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadableStatus: str
        :param _Vip: 备机只读vip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _VPort: 备机只读端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: int
        :param _UniqVpcId: 备机所在私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 备机所在私有网络子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        """
        self._SlaveStatus = None
        self._ReadableStatus = None
        self._Vip = None
        self._VPort = None
        self._UniqVpcId = None
        self._UniqSubnetId = None

    @property
    def SlaveStatus(self):
        return self._SlaveStatus

    @SlaveStatus.setter
    def SlaveStatus(self, SlaveStatus):
        self._SlaveStatus = SlaveStatus

    @property
    def ReadableStatus(self):
        return self._ReadableStatus

    @ReadableStatus.setter
    def ReadableStatus(self, ReadableStatus):
        self._ReadableStatus = ReadableStatus

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId


    def _deserialize(self, params):
        self._SlaveStatus = params.get("SlaveStatus")
        self._ReadableStatus = params.get("ReadableStatus")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventConfig(AbstractModel):
    """设置实例扩展事件阈值

    """

    def __init__(self):
        r"""
        :param _EventType: 事件类型，slow-设置慢SQL阈值，blocked-设置阻塞、死锁阈值
        :type EventType: str
        :param _Threshold: 阈值，单位毫秒。0表示关闭，大于0表示开启
        :type Threshold: int
        """
        self._EventType = None
        self._Threshold = None

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Events(AbstractModel):
    """实例扩展事件详情

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _FileName: 扩展事件文件名称
        :type FileName: str
        :param _Size: 扩展事件文件大小
        :type Size: int
        :param _EventType: 事件类型，slow-慢SQL事件，blocked-阻塞事件，deadlock-死锁事件
        :type EventType: str
        :param _Status: 事件记录状态，1-成功，2-失败
        :type Status: int
        :param _StartTime: 扩展文件生成开始时间
        :type StartTime: str
        :param _EndTime: 扩展文件生成开始时间
        :type EndTime: str
        :param _InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        """
        self._Id = None
        self._FileName = None
        self._Size = None
        self._EventType = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._EventType = params.get("EventType")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAction(AbstractModel):
    """允许动作信息

    """

    def __init__(self):
        r"""
        :param _AllAction: 支持的所有操作，值包括：view(查看列表) remark(修改备注)，deploy(部署)，delete(删除文件)
        :type AllAction: list of str
        :param _AllowedAction: 当前状态允许的操作，AllAction的子集,为空表示禁止所有操作
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        return self._AllowedAction

    @AllowedAction.setter
    def AllowedAction(self, AllowedAction):
        self._AllowedAction = AllowedAction


    def _deserialize(self, params):
        self._AllAction = params.get("AllAction")
        self._AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param _Memory: 内存大小，单位：GB
        :type Memory: int
        :param _Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param _InstanceChargeType: 计费类型，取值支持 PREPAID，POSTPAID。
        :type InstanceChargeType: str
        :param _Period: 购买时长，单位：月。取值为1到48，默认为1
        :type Period: int
        :param _GoodsNum: 一次性购买的实例数量。取值1-100，默认取值为1
        :type GoodsNum: int
        :param _DBVersion: sqlserver版本，目前所有支持的版本有：2008R2 (SQL Server 2008 R2 Enterprise)，2012SP3 (SQL Server 2012 Enterprise)，201202 (SQL Server 2012 Standard)，2014SP2 (SQL Server 2014 Enterprise)，201402 (SQL Server 2014 Standard)，2016SP1 (SQL Server 2016 Enterprise)，201602 (SQL Server 2016 Standard)，2017 (SQL Server 2017 Enterprise)，201702 (SQL Server 2017 Standard)，2019 (SQL Server 2019 Enterprise)，201902 (SQL Server 2019 Standard)。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。
        :type DBVersion: str
        :param _Cpu: 预购买实例的CPU核心数
        :type Cpu: int
        :param _InstanceType: 购买实例的类型 HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-单节点型,cvmHA-虚拟机双机高可用,cvmRO-虚拟机只读
        :type InstanceType: str
        :param _MachineType: 购买实例的宿主机类型，PM-物理机, CLOUD_PREMIUM-虚拟机高性能云盘，CLOUD_SSD-虚拟机SSD云盘,
CLOUD_HSSD-虚拟机加强型SSD云盘，CLOUD_TSSD-虚拟机极速型SSD云盘，CLOUD_BSSD-虚拟机通用型SSD云盘
        :type MachineType: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._InstanceChargeType = None
        self._Period = None
        self._GoodsNum = None
        self._DBVersion = None
        self._Cpu = None
        self._InstanceType = None
        self._MachineType = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Period = params.get("Period")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._Cpu = params.get("Cpu")
        self._InstanceType = params.get("InstanceType")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 未打折前价格，其值除以100表示最终的价格。
InstanceChargeType=PREPAID时，单位是"每月"。
InstanceChargeType=POSTPAID时，单位是"每小时"。
例如10010，在InstanceChargeType=PREPAID情况下，表示每月100.10元。
        :type OriginalPrice: int
        :param _Price: 实际需要支付的价格，其值除以100表示最终的价格。
InstanceChargeType=PREPAID时，单位是"每月"。
InstanceChargeType=POSTPAID时，单位是"每小时"。
例如10010，在InstanceChargeType=PREPAID情况下，表示每月100.10元。
        :type Price: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    """InquiryPriceRenewDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Period: 续费周期。按月续费最多48个月。默认查询续费一个月的价格
        :type Period: int
        :param _TimeUnit: 续费周期单位。month表示按月续费，当前只支持按月付费查询价格
        :type TimeUnit: str
        """
        self._InstanceId = None
        self._Period = None
        self._TimeUnit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元
        :type OriginalPrice: int
        :param _Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元
        :type Price: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Memory: 实例升级后的内存大小，单位GB，其值不能比当前实例内存小
        :type Memory: int
        :param _Storage: 实例升级后的磁盘大小，单位GB，其值不能比当前实例磁盘小
        :type Storage: int
        :param _Cpu: 实例升级后的CPU核心数，其值不能比当前实例CPU小
        :type Cpu: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 未打折的原价，其值除以100表示最终的价格。例如10094表示100.94元
        :type OriginalPrice: int
        :param _Price: 实际需要支付价格，其值除以100表示最终的价格。例如10094表示100.94元
        :type Price: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InstanceDBDetail(AbstractModel):
    """实例的数据库信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DBDetails: 数据库信息列表
        :type DBDetails: list of DBDetail
        """
        self._InstanceId = None
        self._DBDetails = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBDetails(self):
        return self._DBDetails

    @DBDetails.setter
    def DBDetails(self, DBDetails):
        self._DBDetails = DBDetails


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBDetails") is not None:
            self._DBDetails = []
            for item in params.get("DBDetails"):
                obj = DBDetail()
                obj._deserialize(item)
                self._DBDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRenewInfo(AbstractModel):
    """实例续费状态信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _RenewFlag: 实例续费标记。0：正常续费，1：自动续费，2：到期不续
        :type RenewFlag: int
        """
        self._InstanceId = None
        self._RenewFlag = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTask(AbstractModel):
    """实例异步任务

    """

    def __init__(self):
        r"""
        :param _Id: 唯一id
        :type Id: int
        :param _Type: Job类型
        :type Type: int
        :param _Status: Job状态
        :type Status: int
        :param _Progress: 进度百分比0~100
        :type Progress: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _ErrorCode: 错误代码
        :type ErrorCode: int
        :param _Message: 错误信息描述
        :type Message: str
        """
        self._Id = None
        self._Type = None
        self._Status = None
        self._Progress = None
        self._StartTime = None
        self._EndTime = None
        self._ErrorCode = None
        self._Message = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ErrorCode = params.get("ErrorCode")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InterInstance(AbstractModel):
    """互通组内实例信息详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InterVip: 实例互通IP，用于加入互通组后访问
        :type InterVip: str
        :param _InterPort: 实例互通端口，用于加入互通组后访问
        :type InterPort: int
        :param _Status: 实例互通状态，1 -互通ipprot打开中 2 -互通ipprot已经打开 3 -已经打开互通ip的实例加入到互通组中 4 -已经打开互通ip的实例已加入到互通组 5 -互通ipprot回收中 6 -互通ipprot已回收 7 -已回收的实例从互通组中移除中 8 -已回收的实例从互通组中已经移除
        :type Status: int
        :param _Region: 实例所在地域名称，如 ap-guangzhou
        :type Region: str
        :param _Zone: 实例所在可用区名称，如 ap-guangzhou-1
        :type Zone: str
        :param _Version: 实例版本代号
        :type Version: str
        :param _VersionName: 实例版本
        :type VersionName: str
        :param _Name: 实例名称
        :type Name: str
        :param _Vip: 实例访问IP
        :type Vip: str
        :param _Vport: 实例访问端口
        :type Vport: int
        """
        self._InstanceId = None
        self._InterVip = None
        self._InterPort = None
        self._Status = None
        self._Region = None
        self._Zone = None
        self._Version = None
        self._VersionName = None
        self._Name = None
        self._Vip = None
        self._Vport = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InterVip(self):
        return self._InterVip

    @InterVip.setter
    def InterVip(self, InterVip):
        self._InterVip = InterVip

    @property
    def InterPort(self):
        return self._InterPort

    @InterPort.setter
    def InterPort(self, InterPort):
        self._InterPort = InterPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InterVip = params.get("InterVip")
        self._InterPort = params.get("InterPort")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Name = params.get("Name")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InterInstanceFlow(AbstractModel):
    """实例开通或者关闭互通组后的状态

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，例如：mssql-sdf32n1d
        :type InstanceId: str
        :param _FlowId: 实例开通或者关闭互通组的流程ID，FlowId小于0-开通或者关闭失败，反之则成功。
        :type FlowId: int
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDB(AbstractModel):
    """需要迁移的DB列表

    """

    def __init__(self):
        r"""
        :param _DBName: 迁移数据库的名称
        :type DBName: str
        """
        self._DBName = None

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetail(AbstractModel):
    """迁移的进度详情类型

    """

    def __init__(self):
        r"""
        :param _StepName: 当前环节的名称
        :type StepName: str
        :param _Progress: 当前环节的进度（单位是%）
        :type Progress: int
        """
        self._StepName = None
        self._Progress = None

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateSource(AbstractModel):
    """迁移任务的源类型

    """

    def __init__(self):
        r"""
        :param _InstanceId: 迁移源实例的ID，MigrateType=1(TencentDB for SQLServers)时使用，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param _CvmId: 迁移源Cvm的ID，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type CvmId: str
        :param _VpcId: 迁移源Cvm的Vpc网络标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：vpc-6ys9ont9
        :type VpcId: str
        :param _SubnetId: 迁移源Cvm的Vpc下的子网标识，MigrateType=2(云服务器自建SQLServer数据库)时使用，格式如：subnet-h9extioi
        :type SubnetId: str
        :param _UserName: 用户名，MigrateType=1或MigrateType=2使用
        :type UserName: str
        :param _Password: 密码，MigrateType=1或MigrateType=2使用
        :type Password: str
        :param _Ip: 迁移源Cvm自建库的内网IP，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type Ip: str
        :param _Port: 迁移源Cvm自建库的端口号，MigrateType=2(云服务器自建SQLServer数据库)时使用
        :type Port: int
        :param _Url: 离线迁移的源备份地址，MigrateType=4或MigrateType=5使用
        :type Url: list of str
        :param _UrlPassword: 离线迁移的源备份密码，MigrateType=4或MigrateType=5使用
        :type UrlPassword: str
        """
        self._InstanceId = None
        self._CvmId = None
        self._VpcId = None
        self._SubnetId = None
        self._UserName = None
        self._Password = None
        self._Ip = None
        self._Port = None
        self._Url = None
        self._UrlPassword = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmId(self):
        return self._CvmId

    @CvmId.setter
    def CvmId(self, CvmId):
        self._CvmId = CvmId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UrlPassword(self):
        return self._UrlPassword

    @UrlPassword.setter
    def UrlPassword(self, UrlPassword):
        self._UrlPassword = UrlPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CvmId = params.get("CvmId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Url = params.get("Url")
        self._UrlPassword = params.get("UrlPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTarget(AbstractModel):
    """迁移任务的目标类型

    """

    def __init__(self):
        r"""
        :param _InstanceId: 迁移目标实例的ID，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param _UserName: 迁移目标实例的用户名
        :type UserName: str
        :param _Password: 迁移目标实例的密码
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTask(AbstractModel):
    """查询迁移任务列表类型

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        :param _MigrateName: 迁移任务名称
        :type MigrateName: str
        :param _AppId: 迁移任务所属的用户ID
        :type AppId: int
        :param _Region: 迁移任务所属的地域
        :type Region: str
        :param _SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）
        :type SourceType: int
        :param _CreateTime: 迁移任务的创建时间
        :type CreateTime: str
        :param _StartTime: 迁移任务的开始时间
        :type StartTime: str
        :param _EndTime: 迁移任务的结束时间
        :type EndTime: str
        :param _Status: 迁移任务的状态（1:初始化,4:迁移中,5.迁移失败,6.迁移成功,7已中止,8已删除,9中止中,10完成中,11中止失败,12完成失败）
        :type Status: int
        :param _Message: 信息
        :type Message: str
        :param _CheckFlag: 是否迁移任务经过检查（0:未校验,1:校验成功,2:校验失败,3:校验中）
        :type CheckFlag: int
        :param _Progress: 迁移任务当前进度（单位%）
        :type Progress: int
        :param _MigrateDetail: 迁移任务进度细节
        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        self._MigrateId = None
        self._MigrateName = None
        self._AppId = None
        self._Region = None
        self._SourceType = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Message = None
        self._CheckFlag = None
        self._Progress = None
        self._MigrateDetail = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CheckFlag(self):
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateDetail(self):
        return self._MigrateDetail

    @MigrateDetail.setter
    def MigrateDetail(self, MigrateDetail):
        self._MigrateDetail = MigrateDetail


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._SourceType = params.get("SourceType")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._CheckFlag = params.get("CheckFlag")
        self._Progress = params.get("Progress")
        if params.get("MigrateDetail") is not None:
            self._MigrateDetail = MigrateDetail()
            self._MigrateDetail._deserialize(params.get("MigrateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Migration(AbstractModel):
    """冷备迁移导入

    """

    def __init__(self):
        r"""
        :param _MigrationId: 备份导入任务ID 或 增量导入任务ID
        :type MigrationId: str
        :param _MigrationName: 备份导入名称，增量导入任务该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrationName: str
        :param _AppId: 应用ID
        :type AppId: int
        :param _Region: 地域
        :type Region: str
        :param _InstanceId: 迁移目标实例ID
        :type InstanceId: str
        :param _RecoveryType: 迁移任务恢复类型
        :type RecoveryType: str
        :param _UploadType: 备份用户上传类型，COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传
        :type UploadType: str
        :param _BackupFiles: 备份文件列表，UploadType确定，COS_URL则保存URL，COS_UPLOAD则保存备份名称
        :type BackupFiles: list of str
        :param _Status: 迁移任务状态，2-创建完成，7-全量导入中，8-等待增量，9-导入成功，10-导入失败，12-增量导入中
        :type Status: int
        :param _CreateTime: 迁移任务创建时间
        :type CreateTime: str
        :param _StartTime: 迁移任务开始时间
        :type StartTime: str
        :param _EndTime: 迁移任务结束时间
        :type EndTime: str
        :param _Message: 说明信息
        :type Message: str
        :param _Detail: 迁移细节
        :type Detail: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`
        :param _Action: 当前状态允许的操作
        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`
        :param _IsRecovery: 是否是最终恢复，全量导入任务该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRecovery: str
        :param _DBRename: 重命名的数据库名称集合
注意：此字段可能返回 null，表示取不到有效值。
        :type DBRename: list of DBRenameRes
        """
        self._MigrationId = None
        self._MigrationName = None
        self._AppId = None
        self._Region = None
        self._InstanceId = None
        self._RecoveryType = None
        self._UploadType = None
        self._BackupFiles = None
        self._Status = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Message = None
        self._Detail = None
        self._Action = None
        self._IsRecovery = None
        self._DBRename = None

    @property
    def MigrationId(self):
        return self._MigrationId

    @MigrationId.setter
    def MigrationId(self, MigrationId):
        self._MigrationId = MigrationId

    @property
    def MigrationName(self):
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def IsRecovery(self):
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def DBRename(self):
        return self._DBRename

    @DBRename.setter
    def DBRename(self, DBRename):
        self._DBRename = DBRename


    def _deserialize(self, params):
        self._MigrationId = params.get("MigrationId")
        self._MigrationName = params.get("MigrationName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._BackupFiles = params.get("BackupFiles")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Message = params.get("Message")
        if params.get("Detail") is not None:
            self._Detail = MigrationDetail()
            self._Detail._deserialize(params.get("Detail"))
        if params.get("Action") is not None:
            self._Action = MigrationAction()
            self._Action._deserialize(params.get("Action"))
        self._IsRecovery = params.get("IsRecovery")
        if params.get("DBRename") is not None:
            self._DBRename = []
            for item in params.get("DBRename"):
                obj = DBRenameRes()
                obj._deserialize(item)
                self._DBRename.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationAction(AbstractModel):
    """冷备导入任务允许的操作

    """

    def __init__(self):
        r"""
        :param _AllAction: 支持的所有操作，值包括：view(查看任务) ，modify(修改任务)， start(启动任务)，incremental(创建增量任务)，delete(删除任务)，upload(获取上传权限)。
        :type AllAction: list of str
        :param _AllowedAction: 当前状态允许的操作，AllAction的子集,为空表示禁止所有操作
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        return self._AllowedAction

    @AllowedAction.setter
    def AllowedAction(self, AllowedAction):
        self._AllowedAction = AllowedAction


    def _deserialize(self, params):
        self._AllAction = params.get("AllAction")
        self._AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationDetail(AbstractModel):
    """冷备导入任务迁移细节

    """

    def __init__(self):
        r"""
        :param _StepAll: 总步骤数
        :type StepAll: int
        :param _StepNow: 当前步骤
        :type StepNow: int
        :param _Progress: 总进度,如："30"表示30%
        :type Progress: int
        :param _StepInfo: 步骤信息，null表示还未开始迁移
注意：此字段可能返回 null，表示取不到有效值。
        :type StepInfo: list of MigrationStep
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._StepInfo = None

    @property
    def StepAll(self):
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrationStep()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationStep(AbstractModel):
    """冷备导入任务迁移步骤细节

    """

    def __init__(self):
        r"""
        :param _StepNo: 步骤序列
        :type StepNo: int
        :param _StepName: 步骤展现名称
        :type StepName: str
        :param _StepId: 英文ID标识
        :type StepId: str
        :param _Status: 步骤状态:0-默认值,1-成功,2-失败,3-执行中,4-未执行
        :type Status: int
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None

    @property
    def StepNo(self):
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: 账号权限变更信息
        :type Accounts: list of AccountPrivilegeModifyInfo
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilegeModifyInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _Accounts: 修改备注的账户信息
        :type Accounts: list of AccountRemark
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountRemark()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyBackupMigrationRequest(AbstractModel):
    """ModifyBackupMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _MigrationName: 任务名称
        :type MigrationName: str
        :param _RecoveryType: 迁移任务恢复类型，FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param _UploadType: COS_URL-备份放在用户的对象存储上，提供URL。COS_UPLOAD-备份放在业务的对象存储上，用户上传
        :type UploadType: str
        :param _BackupFiles: UploadType是COS_URL时这里时URL，COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库
        :type BackupFiles: list of str
        :param _DBRename: 需要重命名的数据库名称集合
        :type DBRename: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._MigrationName = None
        self._RecoveryType = None
        self._UploadType = None
        self._BackupFiles = None
        self._DBRename = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def RecoveryType(self):
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def DBRename(self):
        return self._DBRename

    @DBRename.setter
    def DBRename(self, DBRename):
        self._DBRename = DBRename


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._MigrationName = params.get("MigrationName")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._BackupFiles = params.get("BackupFiles")
        if params.get("DBRename") is not None:
            self._DBRename = []
            for item in params.get("DBRename"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._DBRename.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupMigrationResponse(AbstractModel):
    """ModifyBackupMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: 备份导入任务ID
        :type BackupMigrationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupMigrationId = None
        self._RequestId = None

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._RequestId = params.get("RequestId")


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _BackupName: 修改的备份名称
        :type BackupName: str
        :param _BackupId: 备份ID 可通过 [DescribeBackups](https://cloud.tencent.com/document/product/238/19943)  接口获取。当GroupId为空时，BackupId必填。
        :type BackupId: int
        :param _GroupId: 备份任务组ID，在单库备份文件模式下，可通过[DescribeBackups](https://cloud.tencent.com/document/product/238/19943) 接口获得。
 BackupId 和 GroupId 同时存在，按照BackupId进行修改。
        :type GroupId: str
        """
        self._InstanceId = None
        self._BackupName = None
        self._BackupId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._BackupId = params.get("BackupId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyBackupStrategyRequest(AbstractModel):
    """ModifyBackupStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _BackupType: 备份类型，当length(BackupDay) <=7 && length(BackupDay) >=2时，取值为weekly，当length(BackupDay)=1时，取值daily，默认daily
        :type BackupType: str
        :param _BackupTime: 备份时间点，取值为0-23的整数
        :type BackupTime: int
        :param _BackupDay: BackupType取值为daily时，表示备份间隔天数。当前取值只能为1
        :type BackupDay: int
        :param _BackupModel: 备份模式（必填），master_pkg-主节点上打包备份文件；master_no_pkg-主节点单库备份文件；slave_pkg-从节点上打包备份文件；slave_no_pkg-从节点上单库备份文件，从节点上备份只有在always on容灾模式下支持。
        :type BackupModel: str
        :param _BackupCycle: BackupType取值为weekly时，表示每周的星期N做备份。（如果数据备份保留时间<7天，则取值[1,2,3,4,5,6,7]。如果数据备份保留时间>=7天，则备份周期取值至少是一周的任意2天）
        :type BackupCycle: list of int non-negative
        :param _BackupSaveDays: 数据(日志)备份保留天数（必填），取值[3-1830]天，默认7天
        :type BackupSaveDays: int
        :param _RegularBackupEnable: 定期备份状态 enable-开启，disable-关闭，默认关闭
        :type RegularBackupEnable: str
        :param _RegularBackupSaveDays: 定期备份保留天数 [90 - 3650]天，默认365天
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: 定期备份策略 years-每年，quarters-每季度，months-每月，默认months
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: 定期备份保留个数，默认1个
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: 定期备份开始日期，格式-YYYY-MM-DD 默认当前日期
        :type RegularBackupStartTime: str
        """
        self._InstanceId = None
        self._BackupType = None
        self._BackupTime = None
        self._BackupDay = None
        self._BackupModel = None
        self._BackupCycle = None
        self._BackupSaveDays = None
        self._RegularBackupEnable = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupTime(self):
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupDay(self):
        return self._BackupDay

    @BackupDay.setter
    def BackupDay(self, BackupDay):
        self._BackupDay = BackupDay

    @property
    def BackupModel(self):
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def BackupCycle(self):
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupSaveDays(self):
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def RegularBackupEnable(self):
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupTime = params.get("BackupTime")
        self._BackupDay = params.get("BackupDay")
        self._BackupModel = params.get("BackupModel")
        self._BackupCycle = params.get("BackupCycle")
        self._BackupSaveDays = params.get("BackupSaveDays")
        self._RegularBackupEnable = params.get("RegularBackupEnable")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupStrategyResponse(AbstractModel):
    """ModifyBackupStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Errno: 返回错误码
        :type Errno: int
        :param _Msg: 返回错误信息
        :type Msg: str
        :param _Code: 返回错误码
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Errno = None
        self._Msg = None
        self._Code = None
        self._RequestId = None

    @property
    def Errno(self):
        warnings.warn("parameter `Errno` is deprecated", DeprecationWarning) 

        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        warnings.warn("parameter `Errno` is deprecated", DeprecationWarning) 

        self._Errno = Errno

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Errno = params.get("Errno")
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class ModifyCloseWanIpRequest(AbstractModel):
    """ModifyCloseWanIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例资源ID
        :type InstanceId: str
        :param _RoGroupId: RO只读组Id
        :type RoGroupId: str
        """
        self._InstanceId = None
        self._RoGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloseWanIpResponse(AbstractModel):
    """ModifyCloseWanIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 关闭外网流程Id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyCrossBackupStrategyRequest(AbstractModel):
    """ModifyCrossBackupStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CrossBackupEnabled: 跨地域备份开关(数据备份&日志备份) enable-开启，disable-关闭
        :type CrossBackupEnabled: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param _CrossBackupSaveDays: 跨地域备份保留天数，取值：7~1830，默认7天
        :type CrossBackupSaveDays: int
        :param _CrossBackupRegion: 跨地域备份的目标地域ID，最多两个，最少一个
        :type CrossBackupRegion: list of str
        :param _CleanUpCrossBackup: 是否立即清理跨地域备份(数据备份&日志备份) ，只有在BackupEnabled = disable时有效。1-是，0-否，默认：0
        :type CleanUpCrossBackup: int
        """
        self._CrossBackupEnabled = None
        self._InstanceId = None
        self._InstanceIdSet = None
        self._CrossBackupSaveDays = None
        self._CrossBackupRegion = None
        self._CleanUpCrossBackup = None

    @property
    def CrossBackupEnabled(self):
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def CrossBackupSaveDays(self):
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def CrossBackupRegion(self):
        return self._CrossBackupRegion

    @CrossBackupRegion.setter
    def CrossBackupRegion(self, CrossBackupRegion):
        self._CrossBackupRegion = CrossBackupRegion

    @property
    def CleanUpCrossBackup(self):
        return self._CleanUpCrossBackup

    @CleanUpCrossBackup.setter
    def CleanUpCrossBackup(self, CleanUpCrossBackup):
        self._CleanUpCrossBackup = CleanUpCrossBackup


    def _deserialize(self, params):
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._InstanceId = params.get("InstanceId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._CrossBackupRegion = params.get("CrossBackupRegion")
        self._CleanUpCrossBackup = params.get("CleanUpCrossBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCrossBackupStrategyResponse(AbstractModel):
    """ModifyCrossBackupStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DBTDEEncrypt: 开启、关闭数据库TDE加密
        :type DBTDEEncrypt: list of DBTDEEncrypt
        """
        self._InstanceId = None
        self._DBTDEEncrypt = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBTDEEncrypt(self):
        return self._DBTDEEncrypt

    @DBTDEEncrypt.setter
    def DBTDEEncrypt(self, DBTDEEncrypt):
        self._DBTDEEncrypt = DBTDEEncrypt


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBTDEEncrypt") is not None:
            self._DBTDEEncrypt = []
            for item in params.get("DBTDEEncrypt"):
                obj = DBTDEEncrypt()
                obj._deserialize(item)
                self._DBTDEEncrypt.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _InstanceName: 新的数据库实例名字
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
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
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDBInstanceNetworkRequest(AbstractModel):
    """ModifyDBInstanceNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _NewVpcId: 新VPC网络Id
        :type NewVpcId: str
        :param _NewSubnetId: 新子网Id
        :type NewSubnetId: str
        :param _OldIpRetainTime: 原vip保留时长，单位小时，默认为0，代表立即回收，最大为168小时
        :type OldIpRetainTime: int
        :param _Vip: 指定VIP地址
        :type Vip: str
        :param _DRNetwork: 目标节点，0-修改主节点网络，1-修改备节点网络，默认取值0

        :type DRNetwork: int
        """
        self._InstanceId = None
        self._NewVpcId = None
        self._NewSubnetId = None
        self._OldIpRetainTime = None
        self._Vip = None
        self._DRNetwork = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewVpcId(self):
        return self._NewVpcId

    @NewVpcId.setter
    def NewVpcId(self, NewVpcId):
        self._NewVpcId = NewVpcId

    @property
    def NewSubnetId(self):
        return self._NewSubnetId

    @NewSubnetId.setter
    def NewSubnetId(self, NewSubnetId):
        self._NewSubnetId = NewSubnetId

    @property
    def OldIpRetainTime(self):
        return self._OldIpRetainTime

    @OldIpRetainTime.setter
    def OldIpRetainTime(self, OldIpRetainTime):
        self._OldIpRetainTime = OldIpRetainTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def DRNetwork(self):
        return self._DRNetwork

    @DRNetwork.setter
    def DRNetwork(self, DRNetwork):
        self._DRNetwork = DRNetwork


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewVpcId = params.get("NewVpcId")
        self._NewSubnetId = params.get("NewSubnetId")
        self._OldIpRetainTime = params.get("OldIpRetainTime")
        self._Vip = params.get("Vip")
        self._DRNetwork = params.get("DRNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkResponse(AbstractModel):
    """ModifyDBInstanceNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 实例转网流程id，可通过[DescribeFlowStatus](https://cloud.tencent.com/document/product/238/19967)接口查询流程状态
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNoteRequest(AbstractModel):
    """ModifyDBInstanceNote请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _InstanceNote: 实例备注信息
        :type InstanceNote: str
        """
        self._InstanceId = None
        self._InstanceNote = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceNote(self):
        return self._InstanceNote

    @InstanceNote.setter
    def InstanceNote(self, InstanceNote):
        self._InstanceNote = InstanceNote


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceNote = params.get("InstanceNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNoteResponse(AbstractModel):
    """ModifyDBInstanceNote返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 实例ID数组，形如mssql-j8kv137v
        :type InstanceIdSet: list of str
        :param _ProjectId: 项目ID，为0的话表示默认项目
        :type ProjectId: int
        """
        self._InstanceIdSet = None
        self._ProjectId = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 修改成功的实例个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceRenewFlagRequest(AbstractModel):
    """ModifyDBInstanceRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RenewFlags: 实例续费状态标记信息
        :type RenewFlags: list of InstanceRenewInfo
        """
        self._RenewFlags = None

    @property
    def RenewFlags(self):
        return self._RenewFlags

    @RenewFlags.setter
    def RenewFlags(self, RenewFlags):
        self._RenewFlags = RenewFlags


    def _deserialize(self, params):
        if params.get("RenewFlags") is not None:
            self._RenewFlags = []
            for item in params.get("RenewFlags"):
                obj = InstanceRenewInfo()
                obj._deserialize(item)
                self._RenewFlags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceRenewFlagResponse(AbstractModel):
    """ModifyDBInstanceRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 修改成功的个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSSLRequest(AbstractModel):
    """ModifyDBInstanceSSL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 操作类型。enable-开启SSL，disable-关闭SSL，renew-更新证书有效期
        :type Type: str
        :param _WaitSwitch: 操作设置。0-立即执行，1- 维护时间内执行，默认取值0。
        :type WaitSwitch: int
        """
        self._InstanceId = None
        self._Type = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSSLResponse(AbstractModel):
    """ModifyDBInstanceSSL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：mssql-c1nl9rpv 或者 mssqlro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _SecurityGroupIdSet: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIdSet: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIdSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIdSet(self):
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _OldDBName: 旧数据库名
        :type OldDBName: str
        :param _NewDBName: 新数据库名
        :type NewDBName: str
        """
        self._InstanceId = None
        self._OldDBName = None
        self._NewDBName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldDBName(self):
        return self._OldDBName

    @OldDBName.setter
    def OldDBName(self, OldDBName):
        self._OldDBName = OldDBName

    @property
    def NewDBName(self):
        return self._NewDBName

    @NewDBName.setter
    def NewDBName(self, NewDBName):
        self._NewDBName = NewDBName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldDBName = params.get("OldDBName")
        self._NewDBName = params.get("NewDBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBRemarkRequest(AbstractModel):
    """ModifyDBRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param _DBRemarks: 数据库名称及备注数组，每个元素包含数据库名和对应的备注
        :type DBRemarks: list of DBRemark
        """
        self._InstanceId = None
        self._DBRemarks = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBRemarks(self):
        return self._DBRemarks

    @DBRemarks.setter
    def DBRemarks(self, DBRemarks):
        self._DBRemarks = DBRemarks


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBRemarks") is not None:
            self._DBRemarks = []
            for item in params.get("DBRemarks"):
                obj = DBRemark()
                obj._deserialize(item)
                self._DBRemarks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDReadableRequest(AbstractModel):
    """ModifyDReadable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 操作类型。enable-开启备机只读，disable-关闭备机只读
        :type Type: str
        :param _VpcId: 备机网络ID，不填默认和主实例保持一致
        :type VpcId: str
        :param _SubnetId: 备机网络子网ID，不填默认和主实例保持一致
        :type SubnetId: str
        :param _Vip: 指定的备机只读vip，不填自动分配
        :type Vip: str
        """
        self._InstanceId = None
        self._Type = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDReadableResponse(AbstractModel):
    """ModifyDReadable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDataBaseTuple(AbstractModel):
    """要修改的数据库订阅发布关系集合

    """

    def __init__(self):
        r"""
        :param _DatabaseTuple: 要修改的订阅关系
        :type DatabaseTuple: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        :param _NewDatabaseTuple: 修改后的订阅关系。DeleteDataBasesTuple为false时有效
        :type NewDatabaseTuple: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        :param _DeleteDataBasesTuple: 是否删除订阅关系。此选项为true时，NewDatabaseTuple无效
        :type DeleteDataBasesTuple: bool
        """
        self._DatabaseTuple = None
        self._NewDatabaseTuple = None
        self._DeleteDataBasesTuple = None

    @property
    def DatabaseTuple(self):
        return self._DatabaseTuple

    @DatabaseTuple.setter
    def DatabaseTuple(self, DatabaseTuple):
        self._DatabaseTuple = DatabaseTuple

    @property
    def NewDatabaseTuple(self):
        return self._NewDatabaseTuple

    @NewDatabaseTuple.setter
    def NewDatabaseTuple(self, NewDatabaseTuple):
        self._NewDatabaseTuple = NewDatabaseTuple

    @property
    def DeleteDataBasesTuple(self):
        return self._DeleteDataBasesTuple

    @DeleteDataBasesTuple.setter
    def DeleteDataBasesTuple(self, DeleteDataBasesTuple):
        self._DeleteDataBasesTuple = DeleteDataBasesTuple


    def _deserialize(self, params):
        if params.get("DatabaseTuple") is not None:
            self._DatabaseTuple = DatabaseTuple()
            self._DatabaseTuple._deserialize(params.get("DatabaseTuple"))
        if params.get("NewDatabaseTuple") is not None:
            self._NewDatabaseTuple = DatabaseTuple()
            self._NewDatabaseTuple._deserialize(params.get("NewDatabaseTuple"))
        self._DeleteDataBasesTuple = params.get("DeleteDataBasesTuple")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCDCRequest(AbstractModel):
    """ModifyDatabaseCDC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBNames: 数据库名数组
        :type DBNames: list of str
        :param _ModifyType: 开启、关闭数据库CDC功能 enable；开启，disable：关闭
        :type ModifyType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._DBNames = None
        self._ModifyType = None
        self._InstanceId = None

    @property
    def DBNames(self):
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._ModifyType = params.get("ModifyType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCDCResponse(AbstractModel):
    """ModifyDatabaseCDC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseCTRequest(AbstractModel):
    """ModifyDatabaseCT请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBNames: 数据库名数组
        :type DBNames: list of str
        :param _ModifyType: 启用、禁用数据库CT功能 enable；启用，disable：禁用
        :type ModifyType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ChangeRetentionDay: 启用CT时额外保留天数，默认保留3天，最小3天，最大30天
        :type ChangeRetentionDay: int
        """
        self._DBNames = None
        self._ModifyType = None
        self._InstanceId = None
        self._ChangeRetentionDay = None

    @property
    def DBNames(self):
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChangeRetentionDay(self):
        return self._ChangeRetentionDay

    @ChangeRetentionDay.setter
    def ChangeRetentionDay(self, ChangeRetentionDay):
        self._ChangeRetentionDay = ChangeRetentionDay


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._ModifyType = params.get("ModifyType")
        self._InstanceId = params.get("InstanceId")
        self._ChangeRetentionDay = params.get("ChangeRetentionDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCTResponse(AbstractModel):
    """ModifyDatabaseCT返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseMdfRequest(AbstractModel):
    """ModifyDatabaseMdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBNames: 数据库名数组
        :type DBNames: list of str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._DBNames = None
        self._InstanceId = None

    @property
    def DBNames(self):
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseMdfResponse(AbstractModel):
    """ModifyDatabaseMdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabasePrivilegeRequest(AbstractModel):
    """ModifyDatabasePrivilege请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _DataBaseSet: 数据库权限变更信息
        :type DataBaseSet: list of DataBasePrivilegeModifyInfo
        """
        self._InstanceId = None
        self._DataBaseSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataBaseSet(self):
        return self._DataBaseSet

    @DataBaseSet.setter
    def DataBaseSet(self, DataBaseSet):
        self._DataBaseSet = DataBaseSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataBaseSet") is not None:
            self._DataBaseSet = []
            for item in params.get("DataBaseSet"):
                obj = DataBasePrivilegeModifyInfo()
                obj._deserialize(item)
                self._DataBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabasePrivilegeResponse(AbstractModel):
    """ModifyDatabasePrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseShrinkMDFRequest(AbstractModel):
    """ModifyDatabaseShrinkMDF请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DBNames: 数据库名数组
        :type DBNames: list of str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._DBNames = None
        self._InstanceId = None

    @property
    def DBNames(self):
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseShrinkMDFResponse(AbstractModel):
    """ModifyDatabaseShrinkMDF返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyIncrementalMigrationRequest(AbstractModel):
    """ModifyIncrementalMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: 增量导入任务ID，由CreateIncrementalMigration接口返回
        :type IncrementalMigrationId: str
        :param _IsRecovery: 是否需要恢复，NO-不需要，YES-需要，默认不修改增量备份导入任务是否需要恢复的属性。
        :type IsRecovery: str
        :param _BackupFiles: UploadType是COS_URL时这里时URL，COS_UPLOAD这里填备份文件的名字；只支持1个备份文件，但1个备份文件内可包含多个库
        :type BackupFiles: list of str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None
        self._IsRecovery = None
        self._BackupFiles = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def IsRecovery(self):
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def BackupFiles(self):
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._IsRecovery = params.get("IsRecovery")
        self._BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIncrementalMigrationResponse(AbstractModel):
    """ModifyIncrementalMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IncrementalMigrationId: 增量备份导入任务ID
        :type IncrementalMigrationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IncrementalMigrationId = None
        self._RequestId = None

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceEncryptAttributesRequest(AbstractModel):
    """ModifyInstanceEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CertificateAttribution: 证书归属。self-表示使用该账号自身的证书，others-表示引用其他账号的证书，默认取值self。
        :type CertificateAttribution: str
        :param _QuoteUin: 引用的其他主账号ID，当CertificateAttribution 为others时必填。
        :type QuoteUin: str
        """
        self._InstanceId = None
        self._CertificateAttribution = None
        self._QuoteUin = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CertificateAttribution(self):
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        return self._QuoteUin

    @QuoteUin.setter
    def QuoteUin(self, QuoteUin):
        self._QuoteUin = QuoteUin


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CertificateAttribution = params.get("CertificateAttribution")
        self._QuoteUin = params.get("QuoteUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceEncryptAttributesResponse(AbstractModel):
    """ModifyInstanceEncryptAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例短 ID 列表
        :type InstanceIds: list of str
        :param _ParamList: 要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改的值。<b>注意</b>：如果修改的参数需要<b>重启</b>实例，那么您的实例将会在执行修改时<b>重启</b>。您可以通过DescribeInstanceParams接口查询修改参数时是否会重启实例，以免导致您的实例不符合预期重启。
        :type ParamList: list of Parameter
        :param _WaitSwitch: 执行参数调整任务的方式，默认为 0。支持值包括：0 - 立刻执行，1 - 时间窗执行。
        :type WaitSwitch: int
        """
        self._InstanceIds = None
        self._ParamList = None
        self._WaitSwitch = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyMaintenanceSpanRequest(AbstractModel):
    """ModifyMaintenanceSpan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        :param _Weekly: 以周为单位，表示允许周几维护，例如：[1,2,3,4,5,6,7]表示周一到周日均为可维护日，本参数不填，则不修改此值。
        :type Weekly: list of int
        :param _StartTime: 每天可维护的开始时间，例如：10:24标识可维护时间窗10点24分开始，本参数不填，则不修改此值。
        :type StartTime: str
        :param _Span: 每天可维护的持续时间，单位是h，例如：1 表示从可维护的开始时间起持续1小时，本参数不填，则不修改此值。
        :type Span: int
        """
        self._InstanceId = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weekly(self):
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceSpanResponse(AbstractModel):
    """ModifyMaintenanceSpan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        :param _MigrateName: 新的迁移任务的名称，若不填则不修改
        :type MigrateName: str
        :param _MigrateType: 新的迁移类型（1:结构迁移 2:数据迁移 3:增量同步），若不填则不修改
        :type MigrateType: int
        :param _SourceType: 迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式），若不填则不修改
        :type SourceType: int
        :param _Source: 迁移源，若不填则不修改
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: 迁移目标，若不填则不修改
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: 迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用，若不填则不修改
        :type MigrateDBSet: list of MigrateDB
        """
        self._MigrateId = None
        self._MigrateName = None
        self._MigrateType = None
        self._SourceType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._MigrateType = params.get("MigrateType")
        self._SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MigrateId = None
        self._RequestId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class ModifyOpenWanIpRequest(AbstractModel):
    """ModifyOpenWanIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例资源ID
        :type InstanceId: str
        :param _RoGroupId: RO只读组Id
        :type RoGroupId: str
        """
        self._InstanceId = None
        self._RoGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOpenWanIpResponse(AbstractModel):
    """ModifyOpenWanIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 开通外网流程Id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyPublishSubscribeNameRequest(AbstractModel):
    """ModifyPublishSubscribeName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PublishSubscribeId: 发布订阅ID
        :type PublishSubscribeId: int
        :param _PublishSubscribeName: 待修改的发布订阅名称
        :type PublishSubscribeName: str
        """
        self._PublishSubscribeId = None
        self._PublishSubscribeName = None

    @property
    def PublishSubscribeId(self):
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def PublishSubscribeName(self):
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName


    def _deserialize(self, params):
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublishSubscribeNameResponse(AbstractModel):
    """ModifyPublishSubscribeName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyPublishSubscribeRequest(AbstractModel):
    """ModifyPublishSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，例如：mssql-dg32dcv
        :type InstanceId: str
        :param _PublishSubscribeId: 发布订阅ID
        :type PublishSubscribeId: int
        :param _DatabaseTupleSet: 修改的数据库订阅发布关系集合
        :type DatabaseTupleSet: list of ModifyDataBaseTuple
        """
        self._InstanceId = None
        self._PublishSubscribeId = None
        self._DatabaseTupleSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PublishSubscribeId(self):
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def DatabaseTupleSet(self):
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = ModifyDataBaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublishSubscribeResponse(AbstractModel):
    """ModifyPublishSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyReadOnlyGroupDetailsRequest(AbstractModel):
    """ModifyReadOnlyGroupDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例ID，格式如：mssql-3l3fgqn7
        :type InstanceId: str
        :param _ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称，不填此参数，则不修改
        :type ReadOnlyGroupName: str
        :param _IsOfflineDelay: 是否启动超时剔除功能,0-不开启剔除功能，1-开启剔除功能，不填此参数，则不修改
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值，不填此参数，则不修改
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数，不填此参数，则不修改
        :type MinReadOnlyInGroup: int
        :param _WeightPairs: 只读组实例权重修改集合，不填此参数，则不修改
        :type WeightPairs: list of ReadOnlyInstanceWeightPair
        :param _AutoWeight: 0-用户自定义权重（根据WeightPairs调整）,1-系统自动分配权重(WeightPairs无效)， 默认为0
        :type AutoWeight: int
        :param _BalanceWeight: 0-不重新均衡负载，1-重新均衡负载，默认为0
        :type BalanceWeight: int
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._WeightPairs = None
        self._AutoWeight = None
        self._BalanceWeight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def IsOfflineDelay(self):
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def WeightPairs(self):
        return self._WeightPairs

    @WeightPairs.setter
    def WeightPairs(self, WeightPairs):
        self._WeightPairs = WeightPairs

    @property
    def AutoWeight(self):
        return self._AutoWeight

    @AutoWeight.setter
    def AutoWeight(self, AutoWeight):
        self._AutoWeight = AutoWeight

    @property
    def BalanceWeight(self):
        return self._BalanceWeight

    @BalanceWeight.setter
    def BalanceWeight(self, BalanceWeight):
        self._BalanceWeight = BalanceWeight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        if params.get("WeightPairs") is not None:
            self._WeightPairs = []
            for item in params.get("WeightPairs"):
                obj = ReadOnlyInstanceWeightPair()
                obj._deserialize(item)
                self._WeightPairs.append(obj)
        self._AutoWeight = params.get("AutoWeight")
        self._BalanceWeight = params.get("BalanceWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupDetailsResponse(AbstractModel):
    """ModifyReadOnlyGroupDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class OldVip(AbstractModel):
    """用于返回实例存在的未回收的ip数量

    """

    def __init__(self):
        r"""
        :param _Vip: 未回收的旧ip
        :type Vip: str
        :param _RecycleTime: ip回收时间
        :type RecycleTime: str
        :param _OldIpRetainTime: 旧IP保留时间小时数
注意：此字段可能返回 null，表示取不到有效值。
        :type OldIpRetainTime: int
        """
        self._Vip = None
        self._RecycleTime = None
        self._OldIpRetainTime = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def RecycleTime(self):
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime

    @property
    def OldIpRetainTime(self):
        return self._OldIpRetainTime

    @OldIpRetainTime.setter
    def OldIpRetainTime(self, OldIpRetainTime):
        self._OldIpRetainTime = OldIpRetainTime


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._RecycleTime = params.get("RecycleTime")
        self._OldIpRetainTime = params.get("OldIpRetainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenInterCommunicationRequest(AbstractModel):
    """OpenInterCommunication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 打开互通组的实例ID集合
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenInterCommunicationResponse(AbstractModel):
    """OpenInterCommunication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InterInstanceFlowSet: 实例和异步流程ID
        :type InterInstanceFlowSet: list of InterInstanceFlow
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InterInstanceFlowSet = None
        self._RequestId = None

    @property
    def InterInstanceFlowSet(self):
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InterInstanceFlowSet") is not None:
            self._InterInstanceFlowSet = []
            for item in params.get("InterInstanceFlowSet"):
                obj = InterInstanceFlow()
                obj._deserialize(item)
                self._InterInstanceFlowSet.append(obj)
        self._RequestId = params.get("RequestId")


class ParamRecord(AbstractModel):
    """实例参数修改记录

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _OldValue: 参数修改前的值
        :type OldValue: str
        :param _NewValue: 参数修改后的值
        :type NewValue: str
        :param _Status: 参数修改状态，1-初始化等待被执行，2-执行成功，3-执行失败，4-参数修改中
        :type Status: int
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._Status = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """数据库实例参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _CurrentValue: 参数值
        :type CurrentValue: str
        """
        self._Name = None
        self._CurrentValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """实例参数的详细描述

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _ParamType: 参数类型，integer-整型，enum-枚举型
        :type ParamType: str
        :param _Default: 参数默认值
        :type Default: str
        :param _Description: 参数描述
        :type Description: str
        :param _CurrentValue: 参数当前值
        :type CurrentValue: str
        :param _NeedReboot: 修改参数后，是否需要重启数据库以使参数生效，0-不需要重启，1-需要重启
        :type NeedReboot: int
        :param _Max: 参数允许的最大值
        :type Max: int
        :param _Min: 参数允许的最小值
        :type Min: int
        :param _EnumValue: 参数允许的枚举类型
        :type EnumValue: list of str
        :param _Status: 参数状态 0-状态正常 1-在修改中
        :type Status: int
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """参考价格，该价格为CPU、内存规格价格，不包括磁盘用量，实际价格以询价接口为准。

    """

    def __init__(self):
        r"""
        :param _PrepaidPrice: 包年包月参考价格，单位-分
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidPrice: int
        :param _PrepaidPriceUnit: 包年包月价格单位，M-月
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidPriceUnit: str
        :param _PostpaidPrice: 按量付费价格，单位-分
注意：此字段可能返回 null，表示取不到有效值。
        :type PostpaidPrice: int
        :param _PostpaidPriceUnit: 按量付费价格单位，H-小时
注意：此字段可能返回 null，表示取不到有效值。
        :type PostpaidPriceUnit: str
        """
        self._PrepaidPrice = None
        self._PrepaidPriceUnit = None
        self._PostpaidPrice = None
        self._PostpaidPriceUnit = None

    @property
    def PrepaidPrice(self):
        return self._PrepaidPrice

    @PrepaidPrice.setter
    def PrepaidPrice(self, PrepaidPrice):
        self._PrepaidPrice = PrepaidPrice

    @property
    def PrepaidPriceUnit(self):
        return self._PrepaidPriceUnit

    @PrepaidPriceUnit.setter
    def PrepaidPriceUnit(self, PrepaidPriceUnit):
        self._PrepaidPriceUnit = PrepaidPriceUnit

    @property
    def PostpaidPrice(self):
        return self._PostpaidPrice

    @PostpaidPrice.setter
    def PostpaidPrice(self, PostpaidPrice):
        self._PostpaidPrice = PostpaidPrice

    @property
    def PostpaidPriceUnit(self):
        return self._PostpaidPriceUnit

    @PostpaidPriceUnit.setter
    def PostpaidPriceUnit(self, PostpaidPriceUnit):
        self._PostpaidPriceUnit = PostpaidPriceUnit


    def _deserialize(self, params):
        self._PrepaidPrice = params.get("PrepaidPrice")
        self._PrepaidPriceUnit = params.get("PrepaidPriceUnit")
        self._PostpaidPrice = params.get("PostpaidPrice")
        self._PostpaidPriceUnit = params.get("PostpaidPriceUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductSpec(AbstractModel):
    """包括地域的产品规格配置

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _Info: 配置信息
        :type Info: list of SpecInfo
        """
        self._RegionId = None
        self._ZoneId = None
        self._Info = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishSubscribe(AbstractModel):
    """发布订阅对象

    """

    def __init__(self):
        r"""
        :param _Id: 发布订阅ID
        :type Id: int
        :param _Name: 发布订阅名称
        :type Name: str
        :param _PublishInstanceId: 发布实例ID
        :type PublishInstanceId: str
        :param _PublishInstanceName: 发布实例名称
        :type PublishInstanceName: str
        :param _PublishInstanceIp: 发布实例IP
        :type PublishInstanceIp: str
        :param _SubscribeInstanceId: 订阅实例ID
        :type SubscribeInstanceId: str
        :param _SubscribeInstanceName: 订阅实例名称
        :type SubscribeInstanceName: str
        :param _SubscribeInstanceIp: 订阅实例IP
        :type SubscribeInstanceIp: str
        :param _DatabaseTupleSet: 数据库的订阅发布关系集合
        :type DatabaseTupleSet: list of DatabaseTupleStatus
        """
        self._Id = None
        self._Name = None
        self._PublishInstanceId = None
        self._PublishInstanceName = None
        self._PublishInstanceIp = None
        self._SubscribeInstanceId = None
        self._SubscribeInstanceName = None
        self._SubscribeInstanceIp = None
        self._DatabaseTupleSet = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PublishInstanceId(self):
        return self._PublishInstanceId

    @PublishInstanceId.setter
    def PublishInstanceId(self, PublishInstanceId):
        self._PublishInstanceId = PublishInstanceId

    @property
    def PublishInstanceName(self):
        return self._PublishInstanceName

    @PublishInstanceName.setter
    def PublishInstanceName(self, PublishInstanceName):
        self._PublishInstanceName = PublishInstanceName

    @property
    def PublishInstanceIp(self):
        return self._PublishInstanceIp

    @PublishInstanceIp.setter
    def PublishInstanceIp(self, PublishInstanceIp):
        self._PublishInstanceIp = PublishInstanceIp

    @property
    def SubscribeInstanceId(self):
        return self._SubscribeInstanceId

    @SubscribeInstanceId.setter
    def SubscribeInstanceId(self, SubscribeInstanceId):
        self._SubscribeInstanceId = SubscribeInstanceId

    @property
    def SubscribeInstanceName(self):
        return self._SubscribeInstanceName

    @SubscribeInstanceName.setter
    def SubscribeInstanceName(self, SubscribeInstanceName):
        self._SubscribeInstanceName = SubscribeInstanceName

    @property
    def SubscribeInstanceIp(self):
        return self._SubscribeInstanceIp

    @SubscribeInstanceIp.setter
    def SubscribeInstanceIp(self, SubscribeInstanceIp):
        self._SubscribeInstanceIp = SubscribeInstanceIp

    @property
    def DatabaseTupleSet(self):
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._PublishInstanceId = params.get("PublishInstanceId")
        self._PublishInstanceName = params.get("PublishInstanceName")
        self._PublishInstanceIp = params.get("PublishInstanceIp")
        self._SubscribeInstanceId = params.get("SubscribeInstanceId")
        self._SubscribeInstanceName = params.get("SubscribeInstanceName")
        self._SubscribeInstanceIp = params.get("SubscribeInstanceIp")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTupleStatus()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMigrationCheckProcessRequest(AbstractModel):
    """QueryMigrationCheckProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMigrationCheckProcessResponse(AbstractModel):
    """QueryMigrationCheckProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalStep: 总步骤数量
        :type TotalStep: int
        :param _CurrentStep: 当前步骤编号，从1开始
        :type CurrentStep: int
        :param _StepDetails: 所有步骤详情
        :type StepDetails: list of StepDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalStep = None
        self._CurrentStep = None
        self._StepDetails = None
        self._RequestId = None

    @property
    def TotalStep(self):
        return self._TotalStep

    @TotalStep.setter
    def TotalStep(self, TotalStep):
        self._TotalStep = TotalStep

    @property
    def CurrentStep(self):
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def StepDetails(self):
        return self._StepDetails

    @StepDetails.setter
    def StepDetails(self, StepDetails):
        self._StepDetails = StepDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalStep = params.get("TotalStep")
        self._CurrentStep = params.get("CurrentStep")
        if params.get("StepDetails") is not None:
            self._StepDetails = []
            for item in params.get("StepDetails"):
                obj = StepDetail()
                obj._deserialize(item)
                self._StepDetails.append(obj)
        self._RequestId = params.get("RequestId")


class ReadOnlyGroup(AbstractModel):
    """只读组对象

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param _RegionId: 只读组的地域ID，与主实例相同
        :type RegionId: str
        :param _ZoneId: 只读组的可用区ID，与主实例相同
        :type ZoneId: str
        :param _IsOfflineDelay: 是否启动超时剔除功能，0-不开启剔除功能，1-开启剔除功能
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 启动超时剔除功能后，使用的超时阈值
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 启动超时剔除功能后，只读组至少保留的只读副本数
        :type MinReadOnlyInGroup: int
        :param _Vip: 只读组vip
        :type Vip: str
        :param _Vport: 只读组vport
        :type Vport: int
        :param _VpcId: 只读组私有网络ID
        :type VpcId: str
        :param _SubnetId: 只读组私有网络子网ID
        :type SubnetId: str
        :param _Status: 只读组状态: 1-申请成功运行中，5-申请中
        :type Status: int
        :param _MasterInstanceId: 主实例ID，形如mssql-sgeshe3th
        :type MasterInstanceId: str
        :param _ReadOnlyInstanceSet: 只读实例副本集合
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _DnsPodDomain: RO组外网地址域名
        :type DnsPodDomain: str
        :param _TgwWanVPort: RO组外网地址端口
        :type TgwWanVPort: int
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._MasterInstanceId = None
        self._ReadOnlyInstanceSet = None
        self._DnsPodDomain = None
        self._TgwWanVPort = None

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def ReadOnlyInstanceSet(self):
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def DnsPodDomain(self):
        return self._DnsPodDomain

    @DnsPodDomain.setter
    def DnsPodDomain(self, DnsPodDomain):
        self._DnsPodDomain = DnsPodDomain

    @property
    def TgwWanVPort(self):
        return self._TgwWanVPort

    @TgwWanVPort.setter
    def TgwWanVPort(self, TgwWanVPort):
        self._TgwWanVPort = TgwWanVPort


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._DnsPodDomain = params.get("DnsPodDomain")
        self._TgwWanVPort = params.get("TgwWanVPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstance(AbstractModel):
    """只读副本实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 只读副本ID，格式如：mssqlro-3l3fgqn7
        :type InstanceId: str
        :param _Name: 只读副本名称
        :type Name: str
        :param _Uid: 只读副本唯一UID
        :type Uid: str
        :param _ProjectId: 只读副本所在项目ID
        :type ProjectId: int
        :param _Status: 只读副本状态。1：申请中 2：运行中 3：被延迟剔除 4：已隔离 5：回收中 6：已回收 7：任务执行中 8：已下线 9：实例扩容中 10：实例迁移中  12：重启中
        :type Status: int
        :param _CreateTime: 只读副本创建时间
        :type CreateTime: str
        :param _UpdateTime: 只读副本更新时间
        :type UpdateTime: str
        :param _Memory: 只读副本内存大小，单位G
        :type Memory: int
        :param _Storage: 只读副本存储空间大小，单位G
        :type Storage: int
        :param _Cpu: 只读副本cpu核心数
        :type Cpu: int
        :param _Version: 只读副本版本代号
        :type Version: str
        :param _Type: 宿主机代号
        :type Type: str
        :param _Model: 只读副本模式，2-单机
        :type Model: int
        :param _PayMode: 只读副本计费模式，1-包年包月，0-按量计费
        :type PayMode: int
        :param _Weight: 只读副本权重
        :type Weight: int
        :param _DelayTime: 只读副本延迟时间，单位秒
        :type DelayTime: str
        :param _SynStatus: 只读副本与主实例的同步状态。
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
        :param _DatabaseDifference: 只读副本与主实例没有同步的库
        :type DatabaseDifference: str
        :param _AccountDifference: 只读副本与主实例没有同步的账户
        :type AccountDifference: str
        :param _StartTime: 只读副本计费开始时间
        :type StartTime: str
        :param _EndTime: 只读副本计费结束时间
        :type EndTime: str
        :param _IsolateTime: 只读副本隔离时间
        :type IsolateTime: str
        :param _RegionId: 只读副本所在地域
        :type RegionId: str
        :param _ZoneId: 只读副本所在可用区
        :type ZoneId: str
        """
        self._InstanceId = None
        self._Name = None
        self._Uid = None
        self._ProjectId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._Version = None
        self._Type = None
        self._Model = None
        self._PayMode = None
        self._Weight = None
        self._DelayTime = None
        self._SynStatus = None
        self._DatabaseDifference = None
        self._AccountDifference = None
        self._StartTime = None
        self._EndTime = None
        self._IsolateTime = None
        self._RegionId = None
        self._ZoneId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def DelayTime(self):
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def SynStatus(self):
        return self._SynStatus

    @SynStatus.setter
    def SynStatus(self, SynStatus):
        self._SynStatus = SynStatus

    @property
    def DatabaseDifference(self):
        return self._DatabaseDifference

    @DatabaseDifference.setter
    def DatabaseDifference(self, DatabaseDifference):
        self._DatabaseDifference = DatabaseDifference

    @property
    def AccountDifference(self):
        return self._AccountDifference

    @AccountDifference.setter
    def AccountDifference(self, AccountDifference):
        self._AccountDifference = AccountDifference

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        self._Model = params.get("Model")
        self._PayMode = params.get("PayMode")
        self._Weight = params.get("Weight")
        self._DelayTime = params.get("DelayTime")
        self._SynStatus = params.get("SynStatus")
        self._DatabaseDifference = params.get("DatabaseDifference")
        self._AccountDifference = params.get("AccountDifference")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsolateTime = params.get("IsolateTime")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstanceWeightPair(AbstractModel):
    """只读实例与权重对应关系

    """

    def __init__(self):
        r"""
        :param _ReadOnlyInstanceId: 只读实例ID，格式如：mssqlro-3l3fgqn7
        :type ReadOnlyInstanceId: str
        :param _ReadOnlyWeight: 只读实例权重 ，范围是0-100
        :type ReadOnlyWeight: int
        """
        self._ReadOnlyInstanceId = None
        self._ReadOnlyWeight = None

    @property
    def ReadOnlyInstanceId(self):
        return self._ReadOnlyInstanceId

    @ReadOnlyInstanceId.setter
    def ReadOnlyInstanceId(self, ReadOnlyInstanceId):
        self._ReadOnlyInstanceId = ReadOnlyInstanceId

    @property
    def ReadOnlyWeight(self):
        return self._ReadOnlyWeight

    @ReadOnlyWeight.setter
    def ReadOnlyWeight(self, ReadOnlyWeight):
        self._ReadOnlyWeight = ReadOnlyWeight


    def _deserialize(self, params):
        self._ReadOnlyInstanceId = params.get("ReadOnlyInstanceId")
        self._ReadOnlyWeight = params.get("ReadOnlyWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleDBInstanceRequest(AbstractModel):
    """RecycleDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class RecycleDBInstanceResponse(AbstractModel):
    """RecycleDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RecycleReadOnlyGroupRequest(AbstractModel):
    """RecycleReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 主实例的ID
        :type InstanceId: str
        :param _ReadOnlyGroupId: 只读组的ID
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleReadOnlyGroupResponse(AbstractModel):
    """RecycleReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域英文ID，类似ap-guanghou
        :type Region: str
        :param _RegionName: 地域中文名称
        :type RegionName: str
        :param _RegionId: 地域数字ID
        :type RegionId: int
        :param _RegionState: 该地域目前是否可以售卖，UNAVAILABLE-不可售卖；AVAILABLE-可售卖
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionState = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBackupsRequest(AbstractModel):
    """RemoveBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _BackupNames: 待删除的备份名称，备份名称可通过DescribeBackups接口的FileName字段获得，单次请求批量删除备份数不能超过10个。当StartTime、EndTime为空时，此字段必填。
        :type BackupNames: list of str
        :param _StartTime: 批量删除手动备份起始时间。当BackupNames为空时，此字段必填。
        :type StartTime: str
        :param _EndTime: 批量删除手动备份截止时间。当BackupNames为空时，此字段必填。
        :type EndTime: str
        """
        self._InstanceId = None
        self._BackupNames = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupNames(self):
        return self._BackupNames

    @BackupNames.setter
    def BackupNames(self, BackupNames):
        self._BackupNames = BackupNames

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupNames = params.get("BackupNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBackupsResponse(AbstractModel):
    """RemoveBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RenameRestoreDatabase(AbstractModel):
    """用于RestoreInstance，RollbackInstance，CreateMigration、CloneDB、ModifyBackupMigration 等接口；对恢复的库进行重命名，且支持选择要恢复的库。

    """

    def __init__(self):
        r"""
        :param _OldName: 库的名字，如果oldName不存在则返回失败。
在用于离线迁移任务时可不填。
        :type OldName: str
        :param _NewName: 库的新名字，在用于离线迁移时，不填则按照OldName命名，OldName和NewName不能同时不填。在用于克隆数据库时，OldName和NewName都必须填写，且不能重复
        :type NewName: str
        """
        self._OldName = None
        self._NewName = None

    @property
    def OldName(self):
        return self._OldName

    @OldName.setter
    def OldName(self, OldName):
        self._OldName = OldName

    @property
    def NewName(self):
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._OldName = params.get("OldName")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _Period: 续费多少个月，取值范围为1-48，默认为1
        :type Period: int
        :param _AutoVoucher: 是否自动使用代金券，0-不使用；1-使用；默认不使用
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID数组，目前只支持使用1张代金券
        :type VoucherIds: list of str
        :param _AutoRenewFlag: 续费标记 0:正常续费 1:自动续费：只用于按量计费转包年包月时有效。
        :type AutoRenewFlag: int
        """
        self._InstanceId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._AutoRenewFlag = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class RenewPostpaidDBInstanceRequest(AbstractModel):
    """RenewPostpaidDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：mssql-3l3fgqn7 或 mssqlro-3l3fgqn7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class RenewPostpaidDBInstanceResponse(AbstractModel):
    """RenewPostpaidDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: 更新后的账户密码信息数组
        :type Accounts: list of AccountPassword
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPassword()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 修改账号密码的异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """实例绑定的标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签key
        :type TagKey: str
        :param _TagValue: 标签value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库实例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _BackupId: 备份文件ID，该ID可以通过DescribeBackups接口返回数据中的Id字段获得
        :type BackupId: int
        :param _TargetInstanceId: 备份恢复到的同一个APPID下的实例ID，不填则恢复到原实例ID
        :type TargetInstanceId: str
        :param _RenameRestore: 按照ReNameRestoreDatabase中的库进行恢复，并重命名，不填则按照默认方式命名恢复的库，且恢复所有的库。
        :type RenameRestore: list of RenameRestoreDatabase
        :param _Type: 回档类型，0-覆盖方式；1-重命名方式，默认1
        :type Type: int
        :param _DBList: 需要覆盖回档的数据库，只有覆盖回档时必填
        :type DBList: list of str
        :param _GroupId: 备份任务组ID，在单库备份文件模式下
        :type GroupId: str
        """
        self._InstanceId = None
        self._BackupId = None
        self._TargetInstanceId = None
        self._RenameRestore = None
        self._Type = None
        self._DBList = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def TargetInstanceId(self):
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DBList(self):
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        self._Type = params.get("Type")
        self._DBList = params.get("DBList")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程任务ID，使用FlowId调用DescribeFlowStatus接口获取任务执行状态
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RestoreTask(AbstractModel):
    """回档任务记录

    """

    def __init__(self):
        r"""
        :param _TargetInstanceId: 目标实例ID
        :type TargetInstanceId: str
        :param _TargetInstanceName: 目标实例名称
        :type TargetInstanceName: str
        :param _TargetInstanceStatus: 目标实例状态。取值范围：
1：申请中
2：运行中
3：受限运行中 (主备切换中)
4：已隔离
5：回收中
6：已回收
7：任务执行中 (实例做备份、回档等操作)
8：已下线
9：实例扩容中
10：实例迁移中
11：只读
12：重启中
        :type TargetInstanceStatus: int
        :param _TargetRegion: 目标实例所在地域
        :type TargetRegion: str
        :param _RestoreId: 回档记录ID
        :type RestoreId: int
        :param _TargetType: 回档到目标实例的类型，0-当前实例，1-已有实例，2-全新实例
        :type TargetType: int
        :param _RestoreType: 回档方式，0-按照时间点回档，1-按照备份集回档
        :type RestoreType: int
        :param _RestoreTime: 回档目标时间
        :type RestoreTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Status: 回档状态，0-初始化，1-运行中，2-成功，3-失败
        :type Status: int
        :param _FlowId: 回档异步任务ID
        :type FlowId: int
        """
        self._TargetInstanceId = None
        self._TargetInstanceName = None
        self._TargetInstanceStatus = None
        self._TargetRegion = None
        self._RestoreId = None
        self._TargetType = None
        self._RestoreType = None
        self._RestoreTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._FlowId = None

    @property
    def TargetInstanceId(self):
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def TargetInstanceName(self):
        return self._TargetInstanceName

    @TargetInstanceName.setter
    def TargetInstanceName(self, TargetInstanceName):
        self._TargetInstanceName = TargetInstanceName

    @property
    def TargetInstanceStatus(self):
        return self._TargetInstanceStatus

    @TargetInstanceStatus.setter
    def TargetInstanceStatus(self, TargetInstanceStatus):
        self._TargetInstanceStatus = TargetInstanceStatus

    @property
    def TargetRegion(self):
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def RestoreId(self):
        return self._RestoreId

    @RestoreId.setter
    def RestoreId(self, RestoreId):
        self._RestoreId = RestoreId

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def RestoreType(self):
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        self._RestoreType = RestoreType

    @property
    def RestoreTime(self):
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._TargetInstanceName = params.get("TargetInstanceName")
        self._TargetInstanceStatus = params.get("TargetInstanceStatus")
        self._TargetRegion = params.get("TargetRegion")
        self._RestoreId = params.get("RestoreId")
        self._TargetType = params.get("TargetType")
        self._RestoreType = params.get("RestoreType")
        self._RestoreTime = params.get("RestoreTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceRequest(AbstractModel):
    """RollbackInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 回档类型，0-回档的数据库覆盖原库；1-回档的数据库以重命名的形式生成，不覆盖原库
        :type Type: int
        :param _Time: 回档目标时间点
        :type Time: str
        :param _DBs: 需要回档的数据库
        :type DBs: list of str
        :param _TargetInstanceId: 备份恢复到的同一个APPID下的实例ID，不填则恢复到原实例ID
        :type TargetInstanceId: str
        :param _RenameRestore: 按照ReNameRestoreDatabase中的库进行重命名，仅在Type = 1重命名回档方式有效；不填则按照默认方式命名库，DBs参数确定要恢复的库
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._Type = None
        self._Time = None
        self._DBs = None
        self._TargetInstanceId = None
        self._RenameRestore = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DBs(self):
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def TargetInstanceId(self):
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._DBs = params.get("DBs")
        self._TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RunMigrationRequest(AbstractModel):
    """RunMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMigrationResponse(AbstractModel):
    """RunMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 迁移流程启动后，返回流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SSLConfig(AbstractModel):
    """SSL加密配置

    """

    def __init__(self):
        r"""
        :param _Encryption: SSL加密状态，
enable-已开启
disable-未开启
enable_doing-开启中
disable_doing-关闭中
renew_doing-更新中
wait_doing-等待维护时间内执行
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: str
        :param _SSLValidityPeriod: SSL证书有效期，时间格式 YYYY-MM-DD HH:MM:SS
注意：此字段可能返回 null，表示取不到有效值。
        :type SSLValidityPeriod: str
        :param _SSLValidity: SSL证书有效性，0-无效，1-有效
注意：此字段可能返回 null，表示取不到有效值。
        :type SSLValidity: int
        """
        self._Encryption = None
        self._SSLValidityPeriod = None
        self._SSLValidity = None

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def SSLValidityPeriod(self):
        return self._SSLValidityPeriod

    @SSLValidityPeriod.setter
    def SSLValidityPeriod(self, SSLValidityPeriod):
        self._SSLValidityPeriod = SSLValidityPeriod

    @property
    def SSLValidity(self):
        return self._SSLValidity

    @SSLValidity.setter
    def SSLValidity(self, SSLValidity):
        self._SSLValidity = SSLValidity


    def _deserialize(self, params):
        self._Encryption = params.get("Encryption")
        self._SSLValidityPeriod = params.get("SSLValidityPeriod")
        self._SSLValidity = params.get("SSLValidity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _InboundSet: 入站规则
        :type InboundSet: list of SecurityGroupPolicy
        :param _OutboundSet: 出站规则
        :type OutboundSet: list of SecurityGroupPolicy
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._InboundSet = None
        self._OutboundSet = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InboundSet(self):
        return self._InboundSet

    @InboundSet.setter
    def InboundSet(self, InboundSet):
        self._InboundSet = InboundSet

    @property
    def OutboundSet(self):
        return self._OutboundSet

    @OutboundSet.setter
    def OutboundSet(self, OutboundSet):
        self._OutboundSet = OutboundSet

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("InboundSet") is not None:
            self._InboundSet = []
            for item in params.get("InboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._InboundSet.append(obj)
        if params.get("OutboundSet") is not None:
            self._OutboundSet = []
            for item in params.get("OutboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._OutboundSet.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """安全组策略

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _CidrIp: 目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param _PortRange: 端口或者端口范围
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP等
        :type IpProtocol: str
        :param _Dir: 规则限定的方向，OUTPUT-出战规则  INPUT-进站规则
        :type Dir: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectAllDB(AbstractModel):
    """DB权限修改类型

    """

    def __init__(self):
        r"""
        :param _Privilege: 权限变更信息。ReadWrite表示可读写，ReadOnly表示只读，Delete表示删除账号对该DB的权限，DBOwner所有者
        :type Privilege: str
        """
        self._Privilege = None

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege


    def _deserialize(self, params):
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveZones(AbstractModel):
    """备可用区信息

    """

    def __init__(self):
        r"""
        :param _SlaveZone: 备可用区地域码
        :type SlaveZone: str
        :param _SlaveZoneName: 备可用区
        :type SlaveZoneName: str
        """
        self._SlaveZone = None
        self._SlaveZoneName = None

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def SlaveZoneName(self):
        return self._SlaveZoneName

    @SlaveZoneName.setter
    def SlaveZoneName(self, SlaveZoneName):
        self._SlaveZoneName = SlaveZoneName


    def _deserialize(self, params):
        self._SlaveZone = params.get("SlaveZone")
        self._SlaveZoneName = params.get("SlaveZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLog(AbstractModel):
    """慢查询日志文件信息

    """

    def __init__(self):
        r"""
        :param _Id: 慢查询日志文件唯一标识
        :type Id: int
        :param _StartTime: 文件生成的开始时间
        :type StartTime: str
        :param _EndTime: 文件生成的结束时间
        :type EndTime: str
        :param _Size: 文件大小（KB）
        :type Size: int
        :param _Count: 文件中log条数
        :type Count: int
        :param _InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param _Status: 状态（1成功 2失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Count = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Count = params.get("Count")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowlogInfo(AbstractModel):
    """慢查询日志文件信息

    """

    def __init__(self):
        r"""
        :param _Id: 慢查询日志文件唯一标识
        :type Id: int
        :param _StartTime: 文件生成的开始时间
        :type StartTime: str
        :param _EndTime: 文件生成的结束时间
        :type EndTime: str
        :param _Size: 文件大小（KB）
        :type Size: int
        :param _Count: 文件中log条数
        :type Count: int
        :param _InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param _ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param _Status: 状态（1成功 2失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Count = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Count = params.get("Count")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    """实例可售卖的规格信息

    """

    def __init__(self):
        r"""
        :param _SpecId: 实例规格ID，利用DescribeZones返回的SpecId，结合DescribeProductConfig返回的可售卖规格信息，可获悉某个可用区下可购买什么规格的实例
        :type SpecId: int
        :param _MachineType: 机型ID
        :type MachineType: str
        :param _MachineTypeName: 机型中文名称
        :type MachineTypeName: str
        :param _Version: 数据库版本信息。取值为2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        :param _VersionName: Version字段对应的版本名称
        :type VersionName: str
        :param _Memory: 内存大小，单位GB
        :type Memory: int
        :param _CPU: CPU核数
        :type CPU: int
        :param _MinStorage: 此规格下最小的磁盘大小，单位GB
        :type MinStorage: int
        :param _MaxStorage: 此规格下最大的磁盘大小，单位GB
        :type MaxStorage: int
        :param _QPS: 此规格对应的QPS大小
        :type QPS: int
        :param _SuitInfo: 此规格的中文描述信息
        :type SuitInfo: str
        :param _Pid: 此规格对应的包年包月Pid
        :type Pid: int
        :param _PostPid: 此规格对应的按量计费Pid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPid: list of int
        :param _PayModeStatus: 此规格下支持的付费模式，POST-仅支持按量计费 PRE-仅支持包年包月 ALL-支持所有
        :type PayModeStatus: str
        :param _InstanceType: 产品类型，HA-高可用型(包括双机高可用，alwaysOn集群)，RO-只读副本型，SI-基础版本型
        :type InstanceType: str
        :param _MultiZonesStatus: 跨可用区类型，MultiZones-只支持跨可用区，SameZones-只支持同可用区，ALL-支持所有
        :type MultiZonesStatus: str
        """
        self._SpecId = None
        self._MachineType = None
        self._MachineTypeName = None
        self._Version = None
        self._VersionName = None
        self._Memory = None
        self._CPU = None
        self._MinStorage = None
        self._MaxStorage = None
        self._QPS = None
        self._SuitInfo = None
        self._Pid = None
        self._PostPid = None
        self._PayModeStatus = None
        self._InstanceType = None
        self._MultiZonesStatus = None

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineTypeName(self):
        return self._MachineTypeName

    @MachineTypeName.setter
    def MachineTypeName(self, MachineTypeName):
        self._MachineTypeName = MachineTypeName

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def MinStorage(self):
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def QPS(self):
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS

    @property
    def SuitInfo(self):
        return self._SuitInfo

    @SuitInfo.setter
    def SuitInfo(self, SuitInfo):
        self._SuitInfo = SuitInfo

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def PostPid(self):
        return self._PostPid

    @PostPid.setter
    def PostPid(self, PostPid):
        self._PostPid = PostPid

    @property
    def PayModeStatus(self):
        return self._PayModeStatus

    @PayModeStatus.setter
    def PayModeStatus(self, PayModeStatus):
        self._PayModeStatus = PayModeStatus

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MultiZonesStatus(self):
        return self._MultiZonesStatus

    @MultiZonesStatus.setter
    def MultiZonesStatus(self, MultiZonesStatus):
        self._MultiZonesStatus = MultiZonesStatus


    def _deserialize(self, params):
        self._SpecId = params.get("SpecId")
        self._MachineType = params.get("MachineType")
        self._MachineTypeName = params.get("MachineTypeName")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Memory = params.get("Memory")
        self._CPU = params.get("CPU")
        self._MinStorage = params.get("MinStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._QPS = params.get("QPS")
        self._SuitInfo = params.get("SuitInfo")
        self._Pid = params.get("Pid")
        self._PostPid = params.get("PostPid")
        self._PayModeStatus = params.get("PayModeStatus")
        self._InstanceType = params.get("InstanceType")
        self._MultiZonesStatus = params.get("MultiZonesStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecSellStatus(AbstractModel):
    """售卖配置状态

    """

    def __init__(self):
        r"""
        :param _Id: 可售卖的规格唯一ID
        :type Id: str
        :param _SpecId: 实例规格ID
        :type SpecId: int
        :param _PayModeStatus: 此规格下支持的付费模式，POST-仅支持按量计费 PRE-仅支持包年包月 ALL-支持所有
        :type PayModeStatus: str
        :param _InstanceType: 产品类型
        :type InstanceType: str
        :param _MultiZonesStatus: 该规格支持的是否跨可用去，MultiZones-只支持跨可用区，SameZones-只支持同可用区，ALL-支持所有
        :type MultiZonesStatus: str
        :param _Architecture: 架构标识，SINGLE-单节点 DOUBLE-双节点 TRIPLE-三节点
        :type Architecture: str
        :param _Style: 类型标识，EXCLUSIVE-独享型，SHARED-共享型
        :type Style: str
        :param _Version: 数据库版本信息
        :type Version: str
        :param _ZoneStatusSet: 每个可用区的售卖状态集合
        :type ZoneStatusSet: list of ZoneStatus
        :param _Price: 规格的参考价格，实际价格以询价接口为准
        :type Price: :class:`tencentcloud.sqlserver.v20180328.models.Price`
        :param _Status: 规格售卖状态 1-正常 2-关闭售卖但是可以升级 3-完全关闭售卖
        :type Status: int
        """
        self._Id = None
        self._SpecId = None
        self._PayModeStatus = None
        self._InstanceType = None
        self._MultiZonesStatus = None
        self._Architecture = None
        self._Style = None
        self._Version = None
        self._ZoneStatusSet = None
        self._Price = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def PayModeStatus(self):
        return self._PayModeStatus

    @PayModeStatus.setter
    def PayModeStatus(self, PayModeStatus):
        self._PayModeStatus = PayModeStatus

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MultiZonesStatus(self):
        return self._MultiZonesStatus

    @MultiZonesStatus.setter
    def MultiZonesStatus(self, MultiZonesStatus):
        self._MultiZonesStatus = MultiZonesStatus

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneStatusSet(self):
        return self._ZoneStatusSet

    @ZoneStatusSet.setter
    def ZoneStatusSet(self, ZoneStatusSet):
        self._ZoneStatusSet = ZoneStatusSet

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SpecId = params.get("SpecId")
        self._PayModeStatus = params.get("PayModeStatus")
        self._InstanceType = params.get("InstanceType")
        self._MultiZonesStatus = params.get("MultiZonesStatus")
        self._Architecture = params.get("Architecture")
        self._Style = params.get("Style")
        self._Version = params.get("Version")
        if params.get("ZoneStatusSet") is not None:
            self._ZoneStatusSet = []
            for item in params.get("ZoneStatusSet"):
                obj = ZoneStatus()
                obj._deserialize(item)
                self._ZoneStatusSet.append(obj)
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationRequest(AbstractModel):
    """StartBackupMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationResponse(AbstractModel):
    """StartBackupMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class StartIncrementalMigrationRequest(AbstractModel):
    """StartIncrementalMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 导入目标实例ID
        :type InstanceId: str
        :param _BackupMigrationId: 备份导入任务ID，由CreateBackupMigration接口返回
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: 增量备份导入任务ID
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartIncrementalMigrationResponse(AbstractModel):
    """StartIncrementalMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class StartInstanceXEventRequest(AbstractModel):
    """StartInstanceXEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _EventConfig: 开启、关闭扩展事件
        :type EventConfig: list of EventConfig
        """
        self._InstanceId = None
        self._EventConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventConfig(self):
        return self._EventConfig

    @EventConfig.setter
    def EventConfig(self, EventConfig):
        self._EventConfig = EventConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("EventConfig") is not None:
            self._EventConfig = []
            for item in params.get("EventConfig"):
                obj = EventConfig()
                obj._deserialize(item)
                self._EventConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceXEventResponse(AbstractModel):
    """StartInstanceXEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class StartMigrationCheckRequest(AbstractModel):
    """StartMigrationCheck请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务id
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrationCheckResponse(AbstractModel):
    """StartMigrationCheck返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 迁移检查流程发起后，返回的流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class StepDetail(AbstractModel):
    """进度步骤详情

    """

    def __init__(self):
        r"""
        :param _Msg: 具体步骤返回信息
        :type Msg: str
        :param _Status: 当前步骤状态，0成功，-2未开始
        :type Status: int
        :param _Name: 步骤名称
        :type Name: str
        """
        self._Msg = None
        self._Status = None
        self._Name = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationRequest(AbstractModel):
    """StopMigration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MigrateId: 迁移任务ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationResponse(AbstractModel):
    """StopMigration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 中止迁移流程发起后，返回的流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SummaryDetailRes(AbstractModel):
    """备份概览实时统计项

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域标识
        :type RegionId: int
        :param _Status: 实例状态。1：申请中2：运行中3：受限运行中 (主备切换中)4：已隔离5：回收中6：已回收7：任务执行中 (实例做备份、回档等操作)8：已下线9：实例扩容中10：实例迁移中
        :type Status: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _ActualUsedSpace: 备份空间
        :type ActualUsedSpace: int
        :param _DataBackupSpace: 数据备份空间
        :type DataBackupSpace: int
        :param _DataBackupCount: 数据备份文件总个数
        :type DataBackupCount: int
        :param _LogBackupSpace: 日志备份空间
        :type LogBackupSpace: int
        :param _LogBackupCount: 日志备份文件总个数
        :type LogBackupCount: int
        :param _AutoBackupSpace: 自动备份空间
        :type AutoBackupSpace: int
        :param _AutoBackupCount: 自动备份文件总个数
        :type AutoBackupCount: int
        :param _ManualBackupSpace: 手动备份空间
        :type ManualBackupSpace: int
        :param _ManualBackupCount: 手动备份文件总个数
        :type ManualBackupCount: int
        :param _Region: 实例所属地域码
        :type Region: str
        """
        self._RegionId = None
        self._Status = None
        self._InstanceId = None
        self._Name = None
        self._ActualUsedSpace = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._AutoBackupSpace = None
        self._AutoBackupCount = None
        self._ManualBackupSpace = None
        self._ManualBackupCount = None
        self._Region = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActualUsedSpace(self):
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def DataBackupSpace(self):
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def LogBackupSpace(self):
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def AutoBackupSpace(self):
        return self._AutoBackupSpace

    @AutoBackupSpace.setter
    def AutoBackupSpace(self, AutoBackupSpace):
        self._AutoBackupSpace = AutoBackupSpace

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def ManualBackupSpace(self):
        return self._ManualBackupSpace

    @ManualBackupSpace.setter
    def ManualBackupSpace(self, ManualBackupSpace):
        self._ManualBackupSpace = ManualBackupSpace

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._AutoBackupSpace = params.get("AutoBackupSpace")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._ManualBackupSpace = params.get("ManualBackupSpace")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCloudInstanceHARequest(AbstractModel):
    """SwitchCloudInstanceHA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _WaitSwitch: 切换执行方式，0-立刻执行，1-时间窗内执行，默认取值为0。
        :type WaitSwitch: int
        """
        self._InstanceId = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCloudInstanceHAResponse(AbstractModel):
    """SwitchCloudInstanceHA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SwitchLog(AbstractModel):
    """主备切换日志

    """

    def __init__(self):
        r"""
        :param _EventId: 切换事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param _SwitchType: 切换模式 0-系统自动切换，1-手动切换
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchType: int
        :param _StartTime: 切换开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 切换结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Reason: 机器故障导致自动切换
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._EventId = None
        self._SwitchType = None
        self._StartTime = None
        self._EndTime = None
        self._Reason = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def SwitchType(self):
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._SwitchType = params.get("SwitchType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TDEConfigAttribute(AbstractModel):
    """TDE透明数据加密配置

    """

    def __init__(self):
        r"""
        :param _Encryption: 是否已开通TDE加密，enable-已开通，disable-未开通
        :type Encryption: str
        :param _CertificateAttribution: 证书归属。self-表示使用该账号自身的证书，others-表示引用其他账号的证书，none-表示没有证书
        :type CertificateAttribution: str
        :param _QuoteUin: 开通TDE加密时引用的其他主账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type QuoteUin: str
        """
        self._Encryption = None
        self._CertificateAttribution = None
        self._QuoteUin = None

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def CertificateAttribution(self):
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        return self._QuoteUin

    @QuoteUin.setter
    def QuoteUin(self, QuoteUin):
        self._QuoteUin = QuoteUin


    def _deserialize(self, params):
        self._Encryption = params.get("Encryption")
        self._CertificateAttribution = params.get("CertificateAttribution")
        self._QuoteUin = params.get("QuoteUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 主动销毁的实例ID列表，格式如：[mssql-3l3fgqn7]。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param _Memory: 实例升级后内存大小，单位GB，其值不能小于当前实例内存大小
        :type Memory: int
        :param _Storage: 实例升级后磁盘大小，单位GB，其值不能小于当前实例磁盘大小
        :type Storage: int
        :param _AutoVoucher: 是否自动使用代金券，0 - 不使用；1 - 默认使用。取值默认为0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID，目前单个订单只能使用一张代金券
        :type VoucherIds: list of str
        :param _Cpu: 实例升级后的CPU核心数
        :type Cpu: int
        :param _DBVersion: 升级sqlserver的版本，目前支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise）版本等。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息，版本不支持降级，不填则不修改版本
        :type DBVersion: str
        :param _HAType: 升级sqlserver的高可用架构,从镜像容灾升级到always on集群容灾，仅支持2017及以上版本且支持always on高可用的实例，不支持降级到镜像方式容灾，CLUSTER-升级为always on容灾，不填则不修改高可用架构
        :type HAType: str
        :param _MultiZones: 修改实例是否为跨可用区容灾，SameZones-修改为同可用区 MultiZones-修改为跨可用区
        :type MultiZones: str
        :param _WaitSwitch: 执行变配的方式，默认为 1。支持值包括：0 - 立刻执行，1 - 维护时间窗执行
        :type WaitSwitch: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Storage = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Cpu = None
        self._DBVersion = None
        self._HAType = None
        self._MultiZones = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def HAType(self):
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._Cpu = params.get("Cpu")
        self._DBVersion = params.get("DBVersion")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单名称
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区英文ID，形如ap-guangzhou-1，表示广州一区
        :type Zone: str
        :param _ZoneName: 可用区中文名称
        :type ZoneName: str
        :param _ZoneId: 可用区数字ID
        :type ZoneId: int
        :param _SpecId: 该可用区目前可售卖的规格ID，利用SpecId，结合接口DescribeProductConfig返回的数据，可获悉该可用区目前可售卖的规格大小
        :type SpecId: int
        :param _Version: 当前可用区与规格下，可售卖的数据库版本，形如2008R2（表示SQL Server 2008 R2）。其可选值有2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._SpecId = None
        self._Version = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._SpecId = params.get("SpecId")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneStatus(AbstractModel):
    """某个地域可用区下的规格售卖状态。

    """

    def __init__(self):
        r"""
        :param _Zone: 规格地域
        :type Zone: str
        :param _Region: 规格可用区
        :type Region: str
        :param _Status: 规格在该可用区的售卖状态 1-正常 2-关闭售卖但是可以升级 3-完全关闭售卖
        :type Status: int
        """
        self._Zone = None
        self._Region = None
        self._Status = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        